# Tools
some key note for install or using tools

## linux install 
1. vim 
2. openssh openssh-server
3. sudo reconfigure dash
4. git 
5. .bashrc color
6. trash-cli
7. ipython notebook
8. vsftpd

## bashrc
``` bash
alias goagent='cd ~/goagent/local && python proxy.py'
alias emacs='emacs -nw'
alias rm='trash'
alias trash-restore='restore-trash'
alias goto115='ssh robin1001@pc115'
```

## vsftpd
``` bash
anonymous_enable=YES
anon_world_readable_only=YES
local_root=/home/robin1001/ftp
chroot_local_user=YES
anon_root=/home/robin1001/ftp
```

** git & ssh 
``` bash
git config --global user.name "robin1001"
git config --global user.email "811364747@qq.com"

ssh-keygen -C "811364747@qq.com" -t rsa
ssh-copy-id robin1001@pc115 #copy ssh id, no password needed
```

## ganglia
``` bash
sudo service ganglia-monitor restart && sudo service gmetad restart && sudo service apache2 restart
```
## flash
``` bash
sudo apt-get install pepperflashplugin-nonfree
sudo update-pepperflashplugin-nonfree --install
```

** man color
``` bash
#man color
#30 – black 31 – red 32 – green 33 – orange 34 – blue 35 – magenta
#36 – cyan  37 – white
export LESS_TERMCAP_mb=$(printf '\e[01;31m') # enter blinking mode – red
export LESS_TERMCAP_md=$(printf '\e[01;33m') # enter double-bright mode – bold, orange 
export LESS_TERMCAP_me=$(printf '\e[0m') # turn off all appearance modes (mb, md, so, us)
export LESS_TERMCAP_se=$(printf '\e[0m') # leave standout mode
export LESS_TERMCAP_so=$(printf '\e[01;44;37m') # enter standout mode – bg_blue, fg_white
export LESS_TERMCAP_ue=$(printf '\e[0m') # leave underline mode
export LESS_TERMCAP_us=$(printf '\e[01;32m') # enter -green
```
## emacs24.4
1. remove other emacs
2. sudo apt-get install build-essential
3. sudo apt-get build-dep emacs24
4. download emacs lastest http://ftp.gnu.org/gnu/emacs/
5. ./configure make sudo make install
6. 可能少x的库
``` bash
sudo apt-get install libgtk2.0-dev
sudo apt-get install libxpm-dev
sudo apt-get install libjpeg62-dev
sudo apt-get install libgif-dev
sudo apt-get install libtiff4-dev
```
