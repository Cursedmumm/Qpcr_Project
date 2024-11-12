import pandas as pd
import numpy as np

ct_names = ['Pos','sample','ct','unknown','primer_eff','eff_doubling']

ct_data = pd.read_table('mabra_270524_senescence.ct', names = ct_names)
cdna_melting = pd.read_table('mabra_270524_senescence.txt',header =1)
genes = pd.read_table('LC480_mabra_270524_senescence-markers.txt',names= ['Pos','sample','gene'], skiprows=1)

ct_data_sub = ct_data[['Pos','sample','ct','primer_eff','eff_doubling']]
cdna_melting_sub = cdna_melting[['Pos','Tm1','Tm2']]
genes_sub = genes[['Pos','gene']]

sub_df = pd.merge(genes_sub, ct_data_sub, on='Pos', how='inner')
df= pd.merge(sub_df, cdna_melting_sub, on='Pos', how='inner')

df_filtered = df[~df['sample'].str.contains("Sample", case=False, na=False)]

print(df_filtered)