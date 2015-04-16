#!/bin/env python
import paramiko
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("localhost",22,"audio", "123456")
stdin, stdout, stderr = ssh.exec_command("ls")
print stdout.readlines()
ssh.close()
