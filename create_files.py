# coding:utf-8
import argparse
import base64
import json
import csv

parser = argparse.ArgumentParser(description='Output files that is created by a csv file and a template.')
parser.add_argument('-i','--inputfile', required=True,
    help='input csv format file that contains output file name in first column.')
parser.add_argument('-o','--outputfile', required=True,
    help='output file name that contains {0} for binding title.')
parser.add_argument('-t','--template', required=True,
    help='template file name for binding input csv file values.')
parser.add_argument('-m','--mode', default='split',
    help='if set mode to "split", splitted file is created. If set mode to "merge", merged file is created.')
parser.add_argument('-ms','--merge_seperater',
    default='\n',
    help='set seperator for delimiter. If not specified, this value defaults to \\n')

args = parser.parse_args()

template_file = open(args.template, "r")
template = template_file.read()
csv_reader = csv.reader(open(args.inputfile, 'rb'), delimiter=',')
if args.mode == 'split':
    for row in csv_reader:
        out_file = open(args.outputfile.format(*row), "w")
        out_file.write(template.format(*row))
        out_file.close()
elif args.mode == 'merge':
    out_file = open(args.outputfile, "w")
    for row in csv_reader:
        out_file.write(template.format(*row) + args.merge_seperater)
    out_file.close()