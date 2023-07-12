from tinydb import TinyDB, Query
import pandas as pd
from pandas import json_normalize

from models import Values
from models import Config, toConfig

class Data:

    def __init__(self):
        self.db = TinyDB('./data.json')
        #self.data = []
        self.configtbl = self.db.table('config')
        self.valuetbl = self.db.table('values')

    def poll(self, values: Values):
        self.valuetbl.insert(values.to_JSON())
        return { 'msg': 'OK'}

    def results(self, id) -> Values:
        results = self.valuetbl.search(Query().id == id)
        df = json_normalize(results) 
        means = df[['q1', 'q2', 'q3', 'q4', 'q5']].mean().fillna(0)
        values = Values(id=id, q1 = means.q1, q2 = means.q2, q3 = means.q3, q4 = means.q4, q5 = means.q5)
        print(values)
        return values 

    def clear(self): 
        results = self.valuetbl.all()
        self.db.remove(doc_ids=list(map(lambda x: x.doc_id, results)))

    def setConfig(self, config: Config): 
        self.configtbl.insert(config.to_JSON())
        return { 'msg': 'OK'}

    def getConfig(self, id) -> Config: 
        result = self.configtbl.search(Query().id == id) 
        print(result[0])
        return toConfig(result[0])

    def getConfigIds(self): 
        results = self.configtbl.all()
        return list(map(lambda x: x['id'], results))