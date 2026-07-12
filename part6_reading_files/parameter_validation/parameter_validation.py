def new_person(name: str, age: int):
    if len(name) < 2 or age < 0 or age > 150:
        raise ValueError("Wrong input")
    return name,age