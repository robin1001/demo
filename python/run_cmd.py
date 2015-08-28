#!/bin/env python
import os

def run_cmd(cmd):
    p = os.popen(cmd)
    return p.read()

def copy_to_local(host, username, password, src_file, dest_file):
    cmd = "./scp_to_local %s %s %s %s %s" % (host, username, password, src_file, dest_file)
    run_cmd(cmd)

def copy_to_remote(host, username, password, src_file, dest_file):
    cmd = "./scp_to_remote.sh %s %s %s %s %s" % (host, username, password, src_file, dest_file)
    run_cmd(cmd)

def copy_to_local(host, username, password, src_file, dest_file):
    cmd = "./scp_to_local.sh %s %s %s %s %s" % (host, username, password, src_file, dest_file)
    run_cmd(cmd)

if __name__ == '__main__':
    print run_cmd('ls')
    print run_cmd('ls test.txt') #error no test.txt
