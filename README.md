# pywheelindexer
Generate index for all wheel files by crawling https://pypi.python.org/simple/

usage:

  index_display.py [-h] [-d DISTRIBUTION] [-a ABI] [-p PYTHON]
                        [-s PLATFORM] [-v VERSION]

  whl file index search script.

  optional arguments:
  -h, --help            show this help message and exit
  -d DISTRIBUTION, --distribution DISTRIBUTION
                        Input python distribution/package name
  -a ABI, --abi ABI     Supported ABI name
  -p PYTHON, --python PYTHON
                        supported python version
  -s PLATFORM, --platform PLATFORM
                        supported platform
  -v VERSION, --version VERSION
                        supported python package version


Features:

  - Generating Panda Dataframe based in whl_result.json
  - whl_result.json generated by crawling pypi.python.org/simple
  - fresh json file will be generated if whl_result.json removed.
  - Generating fresh json document will take time because of crawling whole pypi.python.org/simple
  
Requirements: 

   -  panda
   -  json
   -  os
   -  argparse
   -  bs4
   -  urllib2
   -  re
   -  os.path
   -  itertools


  
