people = [
    {'name': 'peter', 'age': 21},
    {'name': 'jan', 'age': 30},
    {'name': 'julie', 'age': 20},
    {'name': 'homer', 'age': None},
    {'name': 'lisa', 'age': 30},
    {'name': 'marge', 'age': None},
    {'name': 'leah', 'age': 10},
    {'name': 'john', 'age': 32},
    {'name': 'bart', 'age': None},
    {'name': 'beth', 'age': 10},
    {'name': 'hannah', 'age': 12},
    {'name': 'miriam', 'age': 55},
    {'name': 'james', 'age': 23}
]


def average_age(people):
    total_age = 0
    count_none = 0

    for person in people:
        if person['age'] is None:
            count_none = count_none + 1
            continue

        total_age = total_age + person['age']
    
    return total_age / (len(people) - count_none)


print(
    average_age(people)
)
