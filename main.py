class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    # Question 1
    def __contains__(self, item):
        return item in self.__myTeam

    # Question 2
    def __iter__(self):
        yield from self.__myTeam
        
def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print(len(classmates))

    # Question 1
    print()
    print('Tim' in classmates)
    print('Sam' in classmates)

    # Question 2
    print()
    for classmate in classmates:
        print(classmate)

main() 