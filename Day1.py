import pandas as pd

report = pd.read_csv('lol.csv')

#part 1

def calc2020(index, value):
    for i, row in enumerate(report.values):
        if row + value == 2020:
            lol = row * value 
            print(lol)
        else:
            pass

def part1():
    for i, row in enumerate(report.values):
        calc2020(i, row)


#part 2

def calc2020find3(value1, value2):
    for i, row in enumerate(report.values):
        if row + value1 + value2 == 2020:
            print(row*value1*value2)
            break
        else:
            pass


def calc2020findfirst2(index, value):
    for i, row in enumerate(report.values):
        if row + value < 2020:
            calc2020find3(row, value)
        else:
            pass

#part 2

def part2():
    for i, row in enumerate(report.values):
        calc2020findfirst2(i, row)


part1()
part2()