from tinydb import TinyDB, Query
import pandas as pd
from pandas import json_normalize

from values import Values

class Data:

    def __init__(self):
        self.db = TinyDB('./data.json')
        self.data = []

    def poll(self, values: Values):
        self.db.insert({'id': values.id, 'q1': values.q1, 'q2': values.q2, 'q3': values.q3, 'q4': values.q4, 'q5': values.q5})
        return { 'msg': 'OK'}

    def results(self, id) -> Values:
        User = Query()
        list = self.db.search(User.id == id)
        df = json_normalize(list) 
        means = df[['q1', 'q2', 'q3', 'q4', 'q5']].mean()
        values = Values(id=id, q1 = means.q1, q2 = means.q2, q3 = means.q3, q4 = means.q4, q5 = means.q5)
        return values 
