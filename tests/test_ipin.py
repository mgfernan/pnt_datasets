
from pnt_datasets import ipin

def test__ipin_fetch_data():

    data_bundle = ipin.get_data(ipin.Dataset.IPIN_2023_T8, 'D5')

    assert data_bundle
