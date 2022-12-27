def parallel():
    print('\nParallel Resistors\nEnter resistor values, q to stop entry.')

    while True:
        entry = input("\nResistor value:\n")
        if entry != 'q':
            values.append(entry)
            index =+ 1
        else:
            break
    print('Your resistor values:\n{}\n'.format(values))

    total = 0
    for index, item in enumerate(values):
        total += 1/float(item)
    total = 1/total
    print('The parallel resistance is:\n{:.1f}\u03A9'.format(total))

def series():
    print('\Series Resistors\nEnter resistor values, q to stop entry.')

    while True:
        entry = input("\nResistor value:\n")
        if entry != 'q':
            values.append(entry)
            index =+ 1
        else:
            break
    print('Your resistor values:\n{}\n'.format(values))

    total = 0
    for index, item in enumerate(values):
        total += float(item)
    print('The series resistance is:\n{:.1f}\u03A9'.format(total))

choice = input('Resistor Calculator!\nEnter S for Series or P for Parallel:\n')
values = list()
index = 0

if choice == 'S' or choice == 's':
    print('You chose: series\n')
    series()
elif choice == 'P' or choice == 'p':
    print('You chose: parallel\n')
    parallel()
else:
    exit()