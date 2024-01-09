import operator
from operator import itemgetter

def person_lister(f):
    
    def inner(people):
        # complete the function
        #print(people)
        people.sort(key=lambda x: int(operator.itemgetter(2)(x)))
        #print (people)
        names = []
        for person in people:
            print (person)
            print(f(person))
            names.append(f(person))
        return names
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')