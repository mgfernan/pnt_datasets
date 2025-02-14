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

def _reshape_measurement_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    value_vars = [name for name in df.columns if name.startswith('TOA ') or name.startswith('Rsrp ')]

    df_melted = pd.melt(df,
                       id_vars=TIMESTAMP_STR,
                       value_vars=value_vars,
                       var_name='variable',
                       value_name='value')

    df_melted[NODE_ID_STR] = df_melted['variable'].str.extract(r' (\d+) ')
    df_melted['data_type'] = df_melted['variable'].str.split(' ').str[0]

    df_reshaped = pd.pivot_table(df_melted, index=[TIMESTAMP_STR, NODE_ID_STR], columns='data_type', values='value')
    df_reshaped = df_reshaped.reset_index()
    df_reshaped[TOA_STR] = df_reshaped['TOA']
    df_reshaped[RSRP_STR] = df_reshaped['Rsrp']
    df_reshaped = df_reshaped[[TIMESTAMP_STR, NODE_ID_STR, TOA_STR, RSRP_STR]]

    return df_reshaped
