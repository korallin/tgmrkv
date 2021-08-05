import json_purifier
import markov
import os

def input_number():
    while True:
        try:
            input_number = int(input("Enter number of results desired: "))
        except ValueError:
            print("Enter an integer and stop wasting my time...")
            continue
        else: 
            return input_number
            break

number = input_number()

for i in range(0, number):
    markov.markov()
    print(" ")

