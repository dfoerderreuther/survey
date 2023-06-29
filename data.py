from tinydb import TinyDB, Query
import pandas as pd
from pandas import json_normalize


class Data:

    def __init__(self):
        self.db = TinyDB('./data.json')
        self.data = []

    def poll(self, id, q1, q2, q3, q4, q5):
        self.db.insert({'id': id, 'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5})

    def results(self, id):
        User = Query()
        list = self.db.search(User.id == id)
        df = json_normalize(list) 
        means = df[['q1', 'q2', 'q3', 'q4', 'q5']].mean()
        print(df)
        print(means)
        return {
            'id': id, 
            'q1': means.q1, 
            'q2': means.q2, 
            'q3': means.q3, 
            'q4': means.q4, 
            'q5': means.q5
        }
