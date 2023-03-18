import tempfile
import pandas as pd
import requests
import zipfilb
import pandas as pd
import numpy as np


input_file=r"https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip"

#create a temporary folder, download the zip file from web, extract the file and read the file into pandas

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory',tmpdirname)

    with requests.get(input_file) as r:
        with open(f'{tmpdirname}/bank.zip','wb') as f:
            f.write(r.content)

    with zipfile.ZipFile(f'{tmpdirname}/bank.zip','r') as zip_ref:
        zip_ref.extractall(path=f'{tmpdirname}') #extract all files into tempdir
        
        df=pd.read_csv(f'{tmpdirname}/bank-full.csv')
        print(df.head())
min(1,2,3)