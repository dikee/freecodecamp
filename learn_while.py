people = [
    {'name': 'peter', 'age': 21},
    {'name': 'jan', 'age': 30},
    {'name': 'julie', 'age': 20},
    {'name': 'lisa', 'age': 30},
    {'name': 'leah', 'age': 10},
    {'name': 'john', 'age': 32},
    {'name': 'beth', 'age': 10},
    {'name': 'hannah', 'age': 12},
    {'name': 'miriam', 'age': 55},
    {'name': 'james', 'age': 23}
]



def starts_with_j(people):
    """Take in list of names and return list of people whose name starts with j
    """
    j_people = []

    for person in people:
        if person['name'].startswith('j'):
            j_people.append(person['name'])
    return j_people


final_list = starts_with_j(people)


def does_name_start_with_j(name):
    return name.startswith('j')


def starts_with_j_while_loop(people):
    """Take in list of names and return list of people whose name starts with j
    """
    j_people = []

    while True:
        if len(people) == 0:
            break

        person = people.pop()
        if does_name_start_with_j(person['name']):
            j_people.append(person['name'])
        else:
            continue

    return j_people


# print(final_list)

# for name in final_list:
#     print(name)

print(starts_with_j_while_loop(people))
