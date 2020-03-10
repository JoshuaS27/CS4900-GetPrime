'''primeio.py has methods write_primes and read_primes. The module handles .csv
files. It writes to them from a list and reads to a list from a .csv file'''

import csv


def write_primes(l, file_name):
    '''write_primes takes a list filled with integer values and writes it to a
    .csv file'''

    with open(file_name, "w") as outfile:
        for i in l:
            outfile.write(str(i))
            outfile.write("\n")


def read_primes(file_name):
    '''read_primes takes a .csv file, reads it, and writes that to a list'''

    outputList = []
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            outputList.append(row)
            # print(row)

    return outputList
