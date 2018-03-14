#!/usr/bin/env python

import json
import sys
import argparse
import subprocess
from time import sleep


version = '/Rhizocarpon:1.0.1.1/'

parser = argparse.ArgumentParser(description='Ban the peers not running version X\nRequirement: wallet must support the setban command')
parser.add_argument('--outfile', nargs='?',  type=str, help='output json file', default="")
parser.add_argument('--infile', nargs='?', type=str, help='input json file', default="")
parser.add_argument('-s', '--seconds', nargs='?', type=int, dest="seconds", default=86400, help='ban for this many seconds')
parser.add_argument('-c', '--cli', nargs='?', type=str, dest="cli", default="numusd", help="wallet cli command")
parser.add_argument('--subver', nargs='?', type=str, default='/Rhizocarpon:1.0.1.1/', help="Accept only this subversion string")
parser.add_argument('-d', '--delay', nargs='?', type=int, dest="delay", default=3, help="Delay between issued ban commands, in seconds. Default:3")
args = parser.parse_args()

print(args.infile)

#path = os.path.join(os.getcwd(),"testproject","peerinfo.json")

if args.infile:
    jdata = json.load(open(args.infile))
else:
    try:
        output = subprocess.check_output([args.cli, "getpeerinfo"])
        jdata = json.loads(output)
    except subprocess.CalledProcessError as e:
        print("getpeerinfo output:\n", e.output)
    
if args.outfile:
   logFile = open(args.outfile, "w+")

for peer in jdata:
        if  peer["subver"] != args.subver:
                ipaddr = peer["addr"].split(":")[0]
                command = args.cli + " setban " + ipaddr + " add " + str(args.seconds)
                try:
                    if 'logFile' in locals():
                        logFile.write(command + "\n")
                    retcode = subprocess.call(command, shell=True)
                    sleep(args.delay)   
                except OSError as e:
                        print("Execution failed:", e)

