import pickle
import numpy as np
import json
__model=None
def predict_price(x):

    return __model.predict(x)[0]
def load_data():
    global __model
    with open("/home/mohaddesse/Documents/machinLearning/my_project/boston_price/server/artifacts/regmodel.pkl","rb") as f:
            __model=pickle.load(f)
                
def agree():
        return "hi!!"
if __name__=="__main__":
    load_data()
