
import itertools
import collections

def is_increasing(arr):
    return arr == sorted(arr)

def is_decreasing(arr):
    return arr == sorted(arr, reverse=True)

def is_palindrome(arr):
    return arr == arr[::-1]

def is_unique(arr):
    return len(arr) == len(set(arr))

def remove_all(arr, vals: list):
    vals = set(vals)
    return [x for x in arr if x not in vals]

def remove_duplicates(arr):
    return list(set(arr))

def follow_rule_iter(arr, rule):
    # Where rule is a lambda function of a, b where a and b are elements of arr
    return all(rule(a, b) for a, b in zip(arr, arr[1:]))

def flatten(arr):
    # Flattens a nested list into a single list
    return [item for sublist in arr for item in sublist]

def chunk_list(arr, chunk_size):
    # Divides the list into chunks of a specified size
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

def find_duplicates(arr):
    # Returns a list of duplicate items in the list
    counts = collections.Counter(arr)
    return [item for item, count in counts.items() if count > 1]

def rotate_list(arr, n):
    # Rotates the list by n positions
    return arr[n:] + arr[:n]