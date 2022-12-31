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
    print('Series Resistors\nEnter resistor values, q to stop entry.')
    values = list()

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
    return values

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
                try:
                    float(entry)
                except:
                    print("Please enter a number.\n")
                    break
                if entry != 'q':
                    subSeries.append(entry)
                    indexS =+ 1
                elif entry == 'q':
                    break
            print(subSeries)
            comboSeries.append(subSeries)
            print(comboSeries)

        if choice == 'P' or choice == 'p':
            subParallel = list()
            while True:
                entry = input("\nParallel resistor value:\n")
                if entry != 'q':
                    subParallel.append(entry)
                    indexP =+ 1
                elif entry == 'q':
                    break
            print(subParallel)
            comboParallel.append(subParallel)
            print(comboParallel)

        if choice == 'q':
            break

    print('Your series resistor values:\n{}\n'.format(comboSeries))
    print('Your parallel resistor values:\n{}\n'.format(comboParallel))

    total = 0
    seriesTotal = 0
    parallelTotal = 0
    
    for index, item in enumerate(comboSeries):
        for index, item in enumerate(item):
            seriesTotal += float(item)
    for index, item in enumerate(comboParallel):
        for index, item in enumerate(item):
            parallelTotal += 1/float(item)
    parallelTotal = 1/parallelTotal
    total = seriesTotal + parallelTotal

    print('The series resistance is:\n{:.1f}\u03A9'.format(seriesTotal))
    print('The parallel resistance is:\n{:.1f}\u03A9'.format(parallelTotal))
    print('Total resistance:\n{:.1f}\u03A9'.format(total))

def draw(input):
    return