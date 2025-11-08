# This mini project is a calculator that calculates the mean, median, mode, range, and SD of numbers that the user inputs.
from collections import Counter
import math


prompt = f"Hello welcome to my first mini project statistic calculator. You the user input as many numbers as you want and the statistic calculator will calculate "
prompt += "the mean, median, mode, range and SD."
print(prompt)

userNums = []

while True:
    nums = (input("Please insert as many numbers as you want for the stat calculator input 'quit' to exit the loop: "))
    if nums.lower() == 'quit':
        break
    else:
        userNums.append(float(nums))

def mean(userNums):
    s = sum(userNums)
    l = len(userNums)
    mean = s / l
    return mean

def median(userNums):
    orderedUserNums = sorted(userNums)
    n = len(orderedUserNums)
    mid = n // 2
    if n % 2 == 0:
        return (orderedUserNums[mid - 1] + orderedUserNums[mid]) / 2
    else:
        return orderedUserNums[mid]

def mode(userNums):
    frequency = Counter(userNums)
    max_count = max(frequency.values())
    mode = [num for num, count in frequency.items() if count == max_count]
    
    if len(mode) != 1 or max_count == 1:
        return None
    else:
        return mode[0]


def calc_range(userNums):
    ordered = sorted(userNums)
    return ordered[-1] - ordered[0]
    
    

def sd(userNums):
    mean_value = mean(userNums)
    squared_diffs = [(x - mean_value) ** 2 for x in userNums]
    variance = sum(squared_diffs) / len(userNums)
    return math.sqrt(variance)

print(f"Here are the statistics for your numbers")
print(f"Mean: {mean(userNums):.2f}")
print(f"Median: {median(userNums):.2f}")
print(f"Mode: {mode(userNums)}")
print(f"Range: {calc_range(userNums)}")
print(f"Standard Deviation: {sd(userNums):.2f}")



