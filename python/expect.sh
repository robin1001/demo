#!/bin/env bash

#expect -c "
#spawn su
#expect {
#\"Password:\" send \"1234\"
#}
#expect eof"


expect -c "
spawn ssh audio@nj02-audio-engine001.nj02.baidu.com
expect {
\"Are you sure you want to continue connecting (yes/no)?\" {send \"yes\r\"; exp_continue}
\"password:\" {send \"audiotest\r\"}
}
expect eof"
