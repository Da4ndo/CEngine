import requests
from colorama import Fore, init
from tqdm import tqdm
import numpy as np
import pandas as pd

init(autoreset=True)

def fetch_data(url):
    print("::Fetching data from URL")
    response = requests.get(url)
    if response.status_code == 200:
        print("  ->Data fetched successfully")
        return response.json()
    else:
        print("  ->Failed to fetch data")
        print(f"{Fore.RED}Error: Failed to fetch data. Status code: {response.status_code}")
        return None

def process_data(data):
    print("::Processing data")
    if data is None:
        return
    
    df = pd.DataFrame(data)
    
    print("::Performing calculations")
    result = np.mean(df['values'])
    
    print("::Displaying results")
    print(f"{Fore.GREEN}Mean value: {result}")

def main():
    print("::Starting main function")
    url = "https://api.example.com/data"
    data = fetch_data(url)
    
    if data:
        print("  ->Processing fetched data")
        for _ in tqdm(range(100), desc="Processing"):
            process_data(data)
    
    print("::Program completed")
    print(f"{Fore.CYAN}Program execution completed.")

if __name__ == "__main__":
    main()
