import functions

choice = input('Resistor Calculator!\nEnter S for Series, P for Parallel, or B for both:\n')
values = list()
index = 0

if choice == 'S' or choice == 's':
    print('You chose: series\n')
    myValues = functions.series()
    print(myValues)
    #functions.series()
elif choice == 'P' or choice == 'p':
    print('You chose: parallel\n')
    functions.parallel()
elif choice == 'B' or choice == 'b':
    print('You chose: both\n')
    functions.both()
else:
    exit()