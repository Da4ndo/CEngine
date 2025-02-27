import random
import time
import os
import sys
from colorama import Fore, init

init(autoreset=True)

def run_test(test_number, test_function):
    print(f"\nRunning Test #{test_number}...")
    try:
        test_function()
        print(f"{Fore.GREEN}Test #{test_number} Successful!")
    except Exception as e:
        print(f"{Fore.RED}Error: Test #{test_number} Failed!")
        print(f"{Fore.RED}Error details: {str(e)}")

def test_1_print():
    print("Hello, World!")

def test_2_for_loop():
    for i in range(5):
        print(f"Iteration {i + 1}")

def test_3_list_comprehension():
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares: {squares}")

def test_4_dictionary():
    fruits = {"apple": 2, "banana": 3, "orange": 1}
    for fruit, count in fruits.items():
        print(f"We have {count} {fruit}(s)")

def test_5_exception_handling():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught zero division error")

def test_6_file_operations():
    with open("test_file.txt", "w") as f:
        f.write("This is a test file.")
    with open("test_file.txt", "r") as f:
        content = f.read()
    print(f"File content: {content}")
    os.remove("test_file.txt")

def test_7_random_numbers():
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    print(f"Random numbers: {random_numbers}")

def test_8_time_operations():
    start_time = time.time()
    time.sleep(1)
    end_time = time.time()
    print(f"Time elapsed: {end_time - start_time:.2f} seconds")

def test_9_set_operations():
    set1 = set([1, 2, 3, 4, 5])
    set2 = set([4, 5, 6, 7, 8])
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")

def test_10_string_manipulation():
    text = "Hello, World!"
    print(f"Original: {text}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Reversed: {text[::-1]}")

def test_11_system_info():
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print(f"Current working directory: {os.getcwd()}")

def main():
    tests = [
        test_1_print,
        test_2_for_loop,
        test_3_list_comprehension,
        test_4_dictionary,
        test_5_exception_handling,
        test_6_file_operations,
        test_7_random_numbers,
        test_8_time_operations,
        test_9_set_operations,
        test_10_string_manipulation,
        test_11_system_info
    ]

    for i, test in enumerate(tests, 1):
        run_test(i, test)

if __name__ == "__main__":
    main()