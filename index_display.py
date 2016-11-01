#!/usr/bin/env python
# -*- encoding: utf-8

import json
import pandas as pd
import os
import argparse
import indexing


##Defining blank array
result = []

## This can also be parameterized for any python repository crawling
base_url = "https://pypi.python.org/simple/"

## Taking arguments for searching the dataframe based on attributes 
parser = argparse.ArgumentParser(description='whl file index search script.')
parser.add_argument('-d','--distribution', help='Input python distribution/package name')
parser.add_argument('-a','--abi',help='Supported ABI name')
parser.add_argument('-p','--python',help='supported python version')
parser.add_argument('-s','--platform',help='supported platform')
parser.add_argument('-v','--version',help='supported python package version ')

args = parser.parse_args()
 
## show values ##
print ("Distribution: %s" % args.distribution)
print ("Supported ABI: %s" % args.abi)
print ("supported python version: %s" % args.python)
print ("supported os platform: %s" % args.platform)
print ("python package version: %s" % args.version)

## generating path for whl json file 
json_file = os.path.join(os.path.dirname(__file__), "whl_result.json")

#print "json file " + json_file 

## checking if Json file exist, Existance of file will generate datafrom for this file
if os.path.isfile(json_file):

	print "whl json data file exist, Please remove it for fresh whl json file creation"

else:
	indexing.get_data(base_url, result)
	
data = []

with open(json_file) as data_file:

	data = json.load(data_file)

df = pd.read_json(data) 

if args.distribution is not None:
	print df[df.distribution == args.distribution]

if args.abi is not None:
	print df[df.ABI == args.abi]

if args.python is not None:
	print df[df.supported_python == args.python]

if args.platform is not None:
	print df[df.supported_platform == args.platform]

if args.version is not None:
	print df[df.version == args.version]

else:
	print df
