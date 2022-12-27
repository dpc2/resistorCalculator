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

def both():
    print('\Series/Parallel Network\nEnter resistor values, q to stop entry.')
    comboSeries = list()
    
    comboParallel = list()
    subParallel = list()
    indexS = 0
    indexP = 0

    while True:
        choice = input('\nSeries (S) or Parallel (P) sub network?\nq to quit\n')
        if choice == 'S' or choice == 's':
            subSeries = list()
            while True:
                entry = input("\nSeries resistor value:\n")
                if entry != 'q':
                    subSeries.append(entry)
                    indexS =+ 1
                elif entry == 'q':
                    break
            print(subSeries)
            comboSeries.append(subSeries)
            print(comboSeries)

    print('Your resistor values:\n{}\n'.format(comboSeries))

    total = 0
    #for index, item in enumerate(values):
        #total += float(item)
    #print('The series resistance is:\n{:.1f}\u03A9'.format(total))




choice = input('Resistor Calculator!\nEnter S for Series, P for Parallel, or B for both:\n')
values = list()
index = 0

if choice == 'S' or choice == 's':
    print('You chose: series\n')
    series()
elif choice == 'P' or choice == 'p':
    print('You chose: parallel\n')
    parallel()
elif choice == 'B' or choice == 'b':
    print('You chose: both\n')
    both()
else:
    exit()