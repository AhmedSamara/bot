#!/usr/bin/env python
# Start various clients, server or tests

import argparse
from subprocess import Popen
import os
import sys
from time import sleep

import lib.lib as lib
import client.cli_client as cli_client_mod
import client.sub_client as sub_client_mod
import planner.fsm_planner as pfsm_mod

# Build parser and argument groups
parser = argparse.ArgumentParser(description="start bot clients, servers and tests")
client_group = parser.add_mutually_exclusive_group()

# Add arguments
parser.add_argument("-T", "--test-mode", action="store_true",
    help="use simulated hardware, to allow running off the bone")
parser.add_argument("-8", "--pep8", action="store_true",
    help="run script to check PEP8 style conformance")
parser.add_argument("-t", "--tests", action="store_true",
    help="run all unit tests")
parser.add_argument("-s", "--server", action="store_true",
    help="start server to provide interface for controlling the bot")
client_group.add_argument("-a", "--auto-client", action="store_true",
    help="autonomously solve the course")
client_group.add_argument("-c", "--cli-client", action="store_true",
    help="CLI interface for controlling the bot")
client_group.add_argument("-u", "--sub-client", action="store_true",
    help="subscribe to bot's published information")

# Parse the given args
args = parser.parse_args()

# Run on simulated hardware or not
lib.set_testing(args.test_mode)

if args.test_mode:
    print "Using simulated hardware"

# Fail if starting the server on the bot and not root
if not args.test_mode and args.server and os.geteuid() != 0:
    print "Error: Running server in non-test mode requires root privileges."
    sys.exit(1)

if args.pep8:
    print "Running PEP8 style checks"
    os.system("./scripts/check_pep8.sh")

if args.tests:
    print "Running unit tests"
    os.system("python -m unittest discover")

if args.server:
    print "Starting server"
    server = Popen(["./server/control_server.py", str(args.test_mode)])
    # Give server a chance to get up and running
    sleep(.3)

if args.auto_client:
    print "Starting autonomous client"
    planner = pfsm_mod.Robot()

if args.cli_client:
    print "Starting CLI client"
    cli_client_mod.CLIClient().cmdloop()

if args.sub_client:
    print "Starting subscriber client"
    sub_client_mod.SubClient().print_msgs()
