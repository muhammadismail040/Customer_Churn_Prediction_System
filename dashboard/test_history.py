from history import *

sample = {

    "Prediction": "Yes",

    "Probability": 0.87,

    "Cluster": 2

}

save_prediction(sample)

print(load_history())

print(total_predictions())