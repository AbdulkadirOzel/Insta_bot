# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:24:58 2022

@author: Abdulkadir
"""


fastq_size = []

fastq_size_txt = open("C://Users//Abdulkadir//Downloads//1471-2105-10-411-S3.txt", "rt")
lines = fastq_size_txt.readlines()

ID_key = []
ID_value = []


for line in lines:
    trimmed_line = line.strip()
    if len(trimmed_line) > 0:
        if trimmed_line[0] == 'A':
            ID_key.append(trimmed_line)
        elif trimmed_line[0] =='Y' or trimmed_line[0] == 'Q':
            ID_value.append(trimmed_line)


fastq_size_txt.close()

#%%
import pandas as pd

data=pd.read_csv(r"C:\Users\Abdulkadir\Desktop\Yeast_study\raw_data\Oxidative-stress-resistant.tsv", sep='\t')


for i in range(len(data.ID)):
    print(i)
    for y in range(len(ID_key)):
        if data.ID[i] == ID_key[y]:
            data.NEW_ORF[i] = ID_value[y]
            break
            
data.to_csv(r"C:\Users\Abdulkadir\Desktop\Yeast_study\Processed_data\Oxidative-stress-resistant.tsv", sep='\t')
    



data_cob=pd.read_csv(r"C:\Users\Abdulkadir\Desktop\Yeast_study\raw_data\Cobalt-resistant.tsv", sep='\t')


for i in range(len(data_cob.ID)):
    print(i)
    for y in range(len(ID_key)):
        if data_cob.ID[i] == ID_key[y]:
            data_cob.NEW_ORF[i] = ID_value[y]
            break
            
data_cob.to_csv(r"C:\Users\Abdulkadir\Desktop\Yeast_study\Processed_data\Cobalt-resistant.tsv", sep='\t')


data_con=pd.read_csv(r"C:\Users\Abdulkadir\Desktop\Yeast_study\raw_data\Coniferyl-aldehyde-resistant.tsv", sep='\t')


for i in range(len(data_con.ID)):
    print(i)
    for y in range(len(ID_key)):
        if data_con.ID[i] == ID_key[y]:
            data_con.NEW_ORF[i] = ID_value[y]
            break
            
data_con.to_csv(r"C:\Users\Abdulkadir\Desktop\Yeast_study\Processed_data\Coniferyl-aldehyde-resistant.tsv", sep='\t')