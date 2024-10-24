import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    cnt = 0
    for x in s:
        if x in vowels:
            cnt += 1
    return cnt

# Part 2
def short_lists(lst): # For some reason, my code does not work when I specify list parameter types, here is how I would write this line if it had worked: def short_lists(lst: list[list[int]]) -> list[list[int]]:
    return [x for x in lst if len(x) == 2]

# Part 3


# Part 4


# Part 5


# Part 6


# Part 7


# Part 8


