'''
Created on Nov 17, 2022

@author: lorenzo
'''

import pandas as pd

class Database(object):
    def __init__(self, db_file):
        data = pd.read_excel(db_file, sheet_name=["people", "talks"])
        self.people = data["people"]
        self.talks = data["talks"]
        
        print(self.people)
        