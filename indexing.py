#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import re
import os
from os.path import basename
from itertools import izip
import json
import pandas as pd


def crawling(url_string, result):
    """
        Crwaling function gets the url and recursively search fro .whl files
        This function goes thorugh each sub directory 
        Function return a array of whl files
    """
    #print url

    if ".whl" in url_string:

        ## searching for .whl file in url, spliting whole url to find .whl file then assigning to res array 
        whl_url = re.search(r"(/.*.whl)", url_string)

        ## finding the full url
        whl_path = whl_url.group()
        #print "match url " + whl_path

        ## getting whl file name from full url
        whl_file = os.path.basename(whl_path)

        print "whl file :" + whl_file

        ## appending whl file to array
        result.append(whl_file)
        return

    ## excluding the urls who has anything other then .whl files as end url
    if re.search(r"(\.tgz|\.zip|\.tar\.gz|\.exe|\.egg|\.bz2|\.msi|\.rpm|\.dmg|\.deb|\.ZIP)", url_string):
        #print "not Valid"
        return

    ## setting a try catch block for retrying when connection drop happen
    try:
        resp = urllib2.urlopen(url_string)
    #except Exception as e: # catches any exception
    except urllib2.URLError as e: # catches urllib2.URLError in e
        print ('Internet connection dropped!! Trying Again...')
        try:
            resp = urllib2.urlopen(url_string)
        except:
            print ('Internet connection really lost !! Exiting loop..')
            print (e) # print outs the exception message

    soup = BeautifulSoup(resp, 'html.parser', from_encoding=resp.info().getparam('charset'))
    ## Soup to give list of links inside a url
    for link in soup.find_all('a', href=True):
        #print link
        sub_url = url_string+link['href']
        #print sub_url
        #print "This is suburl: " + sub_url
        crawling(sub_url, result)
    return result


def get_data(string, result):
    """
        get data function create json file based on wheel file attributes
        and result array from crawling fuction
    """
    crawling(string, result)

    ## empty array for storing dictionary elements for each whl file

    whl_dict_list = []

    ## Wheel file specific attributes

    whl_attribute = ['distribution','version','supported_python','ABI','supported_platform']

    ## This loop will generate the array of dictionary for each file based on wheel attributes

    for whl_file in result:
    
        ##removing .whl form whl file name
        whl = os.path.splitext(whl_file)[0]
        #print whl 

        ## spliting the whl file name based on "-" delimiter 
        each_whl = whl.split('-')
        #print each_whl

        ## creating dictionary for each wheel file and appending it to array
        new_dict = dict(izip(whl_attribute, each_whl))
        whl_dict_list.append(new_dict)
        #print new_dict

    #print whl_dict_list

    ## generation json from array of dictionary
    json_results = json.dumps(whl_dict_list)

    ## writing json output to file
    with open("whl_result.json", "w") as outfile:
        json.dump(json_results, outfile, indent=4)



