import pandas as pd
import get_silicon as gs

df = pd.read_csv('decat_YSE_list_20210219.txt',delim_whitespace=True).dropna()
df['candCCD'],df['cand_edge_RA_arcsec'],df['cand_edge_DEC_arcsec'] = gs.is_on_silicon(df['RA'],df['Dec'],df['RACand'],df['DecCand'])


print(df)
