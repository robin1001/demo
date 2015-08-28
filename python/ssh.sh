#!/usr/bin/expect   

set timeout 5 
set server [lindex $argv 0] 
set user [lindex $argv 1] 
set passwd [lindex $argv 2] 
 
 spawn ssh -l $user $server 
 expect { 
 "(yes/no)" { send "yes\r"; exp_continue } 
 "password:" { send "$passwd\r" } 
 } 
 expect "*Last login*" interact
