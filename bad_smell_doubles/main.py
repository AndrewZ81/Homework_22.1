class SomeClass:
    def __init__(self):
        self._list = [3, 2, 1, 4, 2, 1]

    def sort_data(self):
        return sorted(self._list, reverse=False)


if __name__ == "__main__":
    some_object = SomeClass()
    print(some_object.sort_data())
