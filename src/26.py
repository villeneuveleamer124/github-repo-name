import sys
import os
import time

def main():
    print("Hello, this is your Python program!")
    # You can add more code here if needed
    print("This program runs every 5 seconds.")

if __name__ == "__main__":
    try:
        main()
        for i in range(5):
            print("Looping...")
            time.sleep(1)  # Add sleep to the loop
    except KeyboardInterrupt:
        print("Program interrupted by user.")
