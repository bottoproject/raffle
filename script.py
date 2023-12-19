import pandas as pd
import random

# Function to read CSV and return list of accounts and their weights
def read_csv(filename):
    df = pd.read_csv(filename)
    accounts = df['account'].tolist()
    sessions = df['sessions'].tolist()
    return accounts, sessions

# Initialize random seed using block hash from Ethereum block 18830069
# Estimated Target Date: Wednesday, Dec 20, 2023 at 22:16:40
# https://etherscan.io/block/countdown/18830069
block_hash = '0xa60f726913161bd43e4500ab' # TBD
seed = int(block_hash, 16)
random.seed(seed)

# Read the CSV file
filename = 'botto_sessions.csv'
accounts, weights = read_csv(filename)

# Select 3 random accounts based on their weights (sessions)
winners = random.choices(accounts, weights=weights, k=3)

print("Selected winners:", winners)