import tempfile
import pandas as pd
import requests
import pandas as pd
import numpy as np
import random

import random
# from faker import Faker

# fake = Faker()

person = {}
# person['id'] = fake.ssn()
person = type(random.randrange(1,9))
person=range(11,14)
person=random.randint(11,14)
# person['first_name'] = fake.first_name()
# person['last_name'] = fake.last_name()
# person['email'] = fake.unique.ascii_email()
# person['company'] = fake.company()
# person['phone'] = fake.phone_number()
print(person)

# input_file=r"https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip"

# #create a temporary folder, download the zip file from web, extract the file and read the file into pandas

# with tempfile.TemporaryDirectory() as tmpdirname:
#     print('created temporary directory',tmpdirname)

#     with requests.get(input_file) as r:
#         with open(f'{tmpdirname}/bank.zip','wb') as f:
#             f.write(r.content)

#     with zipfile.ZipFile(f'{tmpdirname}/bank.zip','r') as zip_ref:
#         zip_ref.extractall(path=f'{tmpdirname}') #extract all files into tempdir
        
#         df=pd.read_csv(f'{tmpdirname}/bank-full.csv')
#         print(df.head())
# min(1,2,3)