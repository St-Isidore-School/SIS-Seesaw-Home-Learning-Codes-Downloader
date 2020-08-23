#!/usr/bin/env python

# Parsing Command Line: https://www.tutorialspoint.com/python3/python_command_line_arguments.htm
# Downloading files: https://likegeeks.com/downloading-files-using-python/
# Iterate through Pandas rows: https://cmdlinetips.com/2018/12/how-to-loop-through-pandas-rows-or-how-to-iterate-over-pandas-rows/
# Named tuples by position label: https://stackoverflow.com/questions/45716038/type-of-return-value-in-itertuples-and-print-column-names-of-itertuples-in-panda
# Join Strings: https://realpython.com/python-string-split-concatenate-join/

import sys
import getopt
import requests
import os
import pandas


def main(argv):
    inputfile = ''
    outputfolder = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('PDF_downloader.py -i <inputfile> -o <outputfolder>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('PDF_downloader.py -i <inputfile> -o <outputfolder>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfolder = arg
    print('Input file is: ', inputfile)
    print('Output file is: ', outputfolder)

    df = pandas.read_csv(inputfile)
    # print(df)
    # print(df.dtypes)

    for row in df.itertuples():
        print(row[1])
        print(row[4])
        # print(row.Index)
        url = row[4]
        myfile = requests.get(url)
        filename = outputfolder + '/' + \
            row[1] + '\'s Seesaw Home Learning Code.pdf'
        open(filename, 'wb').write(myfile.content)


if __name__ == "__main__":
    main(sys.argv[1:])
