csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def read_string(data: str) -> list:
    return [x.split(";") for x in data.split("\n")]


def sort_string(data: list) -> list:
    return sorted(data, key=lambda x: int(x[1]))


def filter_string(data: list) -> list:
    return [x for x in data if int(x[1]) > 10]


def get_filtered_users() -> list:
    data = read_string(csv)
    data = sort_string(data)
    return filter_string(data)


if __name__ == "__main__":
    print(get_filtered_users())
