from typing import List
def calculate_average(numbers : List[int]) -> float:
    return sum(numbers) / len(numbers)

print(calculate_average([123]))