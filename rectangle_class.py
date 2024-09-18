class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Define the __iter__ method to make the object iterable
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage of the Rectangle class
if __name__ == '__main__':
    rectangle = Rectangle(10, 5)  # Create a rectangle with length 10 and width 5

    # Iterate over the rectangle instance
    for dimension in rectangle:
        print(dimension)
