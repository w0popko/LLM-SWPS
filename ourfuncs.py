from openai import OpenAI
import pandas as pd
import pickle
import openai
from tqdm import tqdm  # For progress bar, useful for large datasets

def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
    print(f"Data saved to {filename}")

def load_data(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def apikey():
    return open("key.txt", "r").read().strip("\n")