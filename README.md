# PNT datasets

This repository contains several datasets used to test and validate positioning
algorithms. The repositories contained here are

## IPIN 5G positioning

This data has been extracted from the competition organized by the Indoor Position and Indoor Navigtaion conference[^ipin]. The competition[^ipin_competition] has various tracks that offer challenges in various positioning technologies. In particular, the 5G positioning track focuses on  ToA[^1] positioning and offsers measurements extracted from a network of nodes. The `dataset` contains the data from two editions of the competition (2022 and 2023) and each edition has several measurements `sessions`. Each session has:

- Position of the nodes (anchor points)
- Measurements from the receiver to each of the nodes
- Reference trajectory

This repository contains the data of the CSV files published by the competition. This format of the data has been homogenized so that is the same through all editions and has been stored in [Apache `parquet`](https://parquet.apache.org/) files, which can be access easily into Python `pandas` using the [`read_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html) method:

```{python}
import pandas as pd

# Load the Node data of the IPIN 2022 edition into a dataframe directly from the parquet
df = pd.read_csv('pnt_datasets/ipin/IPIN_2022_T8/nodes.parquet')
```

Alternatively you can have the complete session data (in a `DataBundle`) by importing this package (published in Pypi). To install the package:

```bash
pip install pnt_datasets
```

Then you can access a `session` dataset with the following commands:

```{python}
from pnt_datasets import ipin

edition = ipin.Dataset.IPIN_2022_T8
sessions = ipin.get_dataset_sessions(edition)

data_bundle = ipin.get_data(edition, sessions[0])
```

The `data_bundle` (`DataBundle`) is a `dataclass` with three members:

- `nodes`, a `DataFrame` with the timestamp, and coordinates of the node
- `measurements`, a `DataFrame` with the timestamp, ToA, received power and node of each measurement
- `reference_trajectory`, a series of timestamped positions with the true position of the receiver (this could be used to train your algorithm)


[^1]: Time of Arrival
[^ipin] [IPIN Conference](https://ipin-conference.org/)
[^ipin_competition] https://competition.ipin-conference.org/
