import pickle
import numpy as np
import json
__model=None
__scalar=None
def predict_price(x):
    return __model.predict(x)[0]
def load_data():
    global __model
    global __scalar
    with open("/home/mohaddesse/Documents/machinLearning/my_project/boston_price/server/artifacts/rfe.pkl","rb") as f:
            __model=pickle.load(f)
    with open("/home/mohaddesse/Documents/machinLearning/my_project/boston_price/server/artifacts/scalarmodel.pkl","rb") as f:
            __scalar=pickle.load(f)
                
def agree():
        return "hi!!"
if __name__=="__main__":
    load_data()
