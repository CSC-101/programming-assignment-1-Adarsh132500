import data
import math
from data import Price
from data import Rectangle
from data import Circle
from data import Point

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
def ascending_pairs(lst): # Like the above part, my code does not work when I specify list parameter types: def ascending_pairs(lst: list[list[int]]) -> list[list[int]]:
    result = []
    for x in lst:
        if len(x) == 2:
            result.append(sorted(x))
        else:
            result.append(x)
    return result

# Part 4
def add_prices(price1: Price, price2: Price) -> Price:
    total_cents = price1.cents + price2.cents
    extra_dollars = 0
    if total_cents >= 100:
        extra_dollars = total_cents // 100
        total_cents = total_cents - 100

    total_dollars = price1.dollars + price2.dollars + extra_dollars
    return Price(total_dollars, total_cents)

# Part 5
def rectangle_area(rect: Rectangle) -> float:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y
    return abs(width * height)

# Part 6
def books_by_author(name: str, books):
    return [book for book in books if name in book.authors]

# Part 7
def circle_bound(rect: Rectangle) -> Circle:
    center_x = (rect.top_left.x + rect.bottom_right.x) / 2
    center_y = (rect.top_left.y + rect.bottom_right.y) / 2
    center = Point(center_x, center_y)

    corner = rect.top_left
    radius = math.sqrt((center_x - corner.x) ** 2 + (center_y - corner.y) ** 2)

    return Circle(center, radius)

# Part 8


