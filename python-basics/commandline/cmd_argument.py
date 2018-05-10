#!/usr/bin/python

# This program is to show basic of python programming
# I'm opening a file using python
#

import os
import sys
import time
import getopt
from datetime import datetime

def print_help():
    message = """\n******** Script Information *********\n
Usage : This script takes three arguments. env, action and source zip location.\n
Based on env type it will upload files in Akama NetStorage.\n
******** Arguments Information *********\n
Arguments :\n
    -h or --help    : Help argument which show details of the script
    -e or --env     : Environment argument - test / prod \n
    -a or --action  : Action argument - upload / delete / post \n
    -d or --dir     : File path argument - Full file path needs to be specified here. \n
                        e.g. /tmp/abc/content.zip \n
                    Note: If file ext is zip than script will extract the zip file first and \n
                    uploads all the files. \n
    Example: python cmd_argument.py -e test -a upload -d /tmp/abc/pkr.zip\n

    """

    print message

def print_exception(message):
    print 'Error Message : ' + message
    print_help()

def main():
    print 'Enter main method'
    env = ''
    dir_loc = ''
    action = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "he:a:d:", ["help", "env=", "action=", "dir="])
         
        if len(opts) != 3 :
            print_exception('1 or more arguments were missing in command. Arguments : ' + str(opts))
            sys.exit()
    
    except getopt.GetoptError as err:
        print_exception('Opps.. Invalid option..!! Error message : ' + str(err)) 
        sys.exit(2)
    
    for opt, arg in opts:
        print 'option -- ' + opt
        #print 'arg -- ' + arg
        if opt in ('-h', '--help'):
            print_help()
            sys.exit()
        elif opt in ("-e", "--env"):
            env = arg
        elif opt in ("-d", "--dir"):
            dir_loc = arg
        elif opt in ("-a", "--action"):
            action = arg
        else:
            print ('-- Invalid Option : ', opt) 
            print_help()
            sys.exit()

    print 'Env : ' + env
    print 'Dir : ' + dir_loc
    print 'Action : ' + action
    
if __name__ == "__main__":
    main()