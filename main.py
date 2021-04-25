import sys
from predictor import predict_runs

runs = predict_runs('input_test_data(2).csv')
print("Predicted Runs: ", runs)
