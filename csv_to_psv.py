# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:00:12 2022

@author: mxka1r54
"""

import os
import pandas as pd


def csv_2_psv():
    files = [x for x in os.listdir() if x.endswith('.csv')]
    for file in files:
        df = pd.read_csv(file)
        print('reading' , file)
        output = f'{file[:-4]}_pipe.csv'
        df.to_csv(output, encoding='utf-8', index=False, sep='|')
        
        
if __name__ == '__main__':
    csv_2_psv()
    
    
#%% CONVERTIR EL ULTIMO ARCHIVO 

import os
os.chdir(r'C:\Users\MXKA1R54\OneDrive - Kellogg Company\Documents\ARG\LH4\OTHERS\MAESTRO CLIENTES BRASIL SAP') # relative path: scripts dir is under Lab
import pandas as pd


file = 'Catálogo Brasil 04.10.2022.csv'
df = pd.read_csv(file, dtype=str)#low_memory=False) #LOW MEMORY ES IGUAL A "FALSE" PARA QUE NO NOS CAMBIE LOS DATA TYPES (O EN DADO CASO DEBEMOS ESPECIFICAR LOS DATA TYPES AQUI MISMO). ESTO SE HIZO POR QUE QUITABA 0s A LA IZQUIERDA
#df = pd.read_csv(file, dtype={"Customer Classific.": "string", "Tax Number 1": "string", "Tax Number 1": "string", "Postal Code":"string"})
print('reading' , file)

#hd = df.head(50)
#list(hd.columns)

#LIMPIAMOS UN POCO LA COLUMNA DE POSTAL CODE 
df['Postal Code'] = df['Postal Code'].replace(['.',' '],['-','-'])



#Ver valores unicos de la fecha y hora de la encuesta
#unicos_fyh_encuesta = df['Sales document'].unique()
#nas = df.loc[df['Sales document'].isna()].head(20)

#Modificamos el tipo de dato de las columnas para una mejor manipulacion 
#df['Customer Classific.'] = df['Customer Classific.'].astype('str')
#df['Tax Number 1'] = df['Tax Number 1'].astype('str')
#df['Tax Number 2'] = df['Tax Number 2'].astype('str')
#df['Postal Code'] = df['Postal Code'].astype('str')
#df['Sold-To Cust Classification'] = df['Sold-To Cust Classification'].astype('int64')
#df['Material'] = df['Material'].astype('str')
#df['Sales Organization'] = df['Sales Organization'].astype('int64')

# EXPORTAMOS A CSV 
output = f'{file[:-4]}_pipe.csv'
df.to_csv(output, encoding='utf-8-sig', index=False, sep='|')
        



# DRAFTS DE POSTAL CODE CLEANING 
# CODIGO POSTAL ANALYSIS
pc = df['Postal Code'].unique()
pc = pd.DataFrame(pc, columns = ['CP'])
pc.dropna(inplace = True)

pc = pc[~pc['CP'].str.contains('-')]

pc2 = pc['CP'] = pc['CP'].replace(['.',' '],['-','-'])


pc.to_csv('pc.csv', encoding='utf-8-sig', index=False) 