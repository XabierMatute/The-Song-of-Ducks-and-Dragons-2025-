input = """
82:8,1,7,4,9,6,4,5,9,2,3,6,7,8,6,8,3,7,1,2,8,5,8,8,3,9,1,6,4,9
"""

class Segment:
    def __init__(self, main_value):
        self.main_value = main_value
        self.minor_value = None
        self.mayor_value = None

    def isFull(self):
        return self.minor_value is not None and self.mayor_value is not None

    def __repr__(self):
        # return f"{self.minor_value}-{self.main_value}-{self.mayor_value}"
        return f"{self.minor_value if self.minor_value is not None else ' '}-{self.main_value}-{self.mayor_value if self.mayor_value is not None else ' '}"

identifier, numbers = input.strip().split(":")
numbers = list(map(int, numbers.split(",")))
print(identifier)
print(numbers)
spine : list[Segment] = list()
for number in numbers:
    print("number", number)
    for segment in spine:
        print("segment", segment)
        print("mv", segment.main_value)
        if segment.isFull():
            continue
        print(segment.main_value)
        if number < segment.main_value and segment.minor_value is None:
            segment.minor_value = number
            break
        if number > segment.main_value and segment.mayor_value is None:
            segment.mayor_value = number
            break
    else:
        spine.append(Segment(number))

quality = ""
for segment in spine:
    print(segment)
    quality += segment.main_value.__str__()

print(quality)