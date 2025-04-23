from typing import List, Any


def process_data(data):
    return


def concatenate_strings(strings: List[str]) -> str:
    return ''.join(strings)


def display_name(message: str):
    print(message)


def main():
    data=process_data("example data")
    print(data)
    strings = ["hello", "world"]
    concatenate = concatenate_strings(strings)
    display_name(concatenate)


if __name__=="__main__":
    main()