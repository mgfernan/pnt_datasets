from dataclasses import dataclass
import enum
import glob
import os
from typing import Tuple

import pandas as pd

X_STR = 'X (m)'
Y_STR = 'Y (m)'
Z_STR = 'Z (m)'
TOA_STR = 'TOA (ns)'
SINGLE_DIFF_STR = 'SD (m)'
RSRP_STR = 'Rsrp (dBm)'
TIMESTAMP_STR = 'timestamp (s)'
BIAS_STR = 'bias (m)'
DTB_STR = 'DTB (m)'
NODE_ID_STR = 'Node ID'

TOA_FMT_STR = 'TOA %d (ns)'
RSRP_FMT_STR = 'Rsrp %d (dBm)'

MODULE_PATH = os.path.dirname(__file__)

class Dataset(enum.Enum):

    IPIN_2022_T8 = enum.auto()
    IPIN_2023_T8 = enum.auto()


@dataclass
class DataBundle:
    nodes: pd.DataFrame
    measurements: pd.DataFrame
    reference_trajectory: pd.DataFrame


def get_dataset_sessions(dataset: Dataset):
    """
    Returns the list of measurements sessions within the dataset
    """

    dataset_folder = os.path.join(MODULE_PATH, dataset.name)

    meas_files = glob.glob(os.path.join(dataset_folder, '*_measurements.parquet'))

    return [os.path.basename(fname).split('_')[0] for fname in meas_files]


def get_data(dataset: Dataset, session: str) -> DataBundle:
    """
    Get data bundle for the dataset and session

    :returns: A tuple with the (nodes, measurements and reference_trajectory)
    """

    dataset_folder = os.path.join(MODULE_PATH, dataset.name)


    nodes = pd.read_parquet(os.path.join(dataset_folder, 'nodes.parquet'))
    measurements = pd.read_parquet(os.path.join(dataset_folder, f'{session}_measurements.parquet'))
    reference_trajectory = pd.read_parquet(os.path.join(dataset_folder, f'{session}_reference.parquet'))

    return DataBundle(nodes, measurements, reference_trajectory)
