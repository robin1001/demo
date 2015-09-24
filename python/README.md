# python tools

## import 
1. current dir
2. parent dir
3. sub dir

## run file in interpreter
```pyhton
>>> variables= {}
>>> execfile( "someFile.py", variables )
>>> print variables # globals from the someFile module
```

### ipython
* shell command(!cmd, like vi)
* %edit %run (%run -d test.py, debug)


## python编码问题
* 字符集 utf8 
    * ASCII:
    * latin1=iso-8859-1=ISO-8859 Latin1是ISO-8859-1的别名，有些环境下写作Latin-1, 兼容ASCII
    * Non-ISO extended-ASCII: ISO之外的扩展ASCII
    * UTF8
    * GBK gb2312
* 查看文件编码linux命令
    * file file_name
    * file -i file_name
    * iconv -f latin1 -t utf8 inputfile
* vim 查看文件编码 
    * 查看 set fileencoding
    * 设置 set encoding=utf-8
    * 检测 set fileencodings=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
* python 编码
    * coding=utf-8
    * 解释器编码 代码文件编码 终端编码
    * codec
    ```python
    import codecs
    fid = codecs.open('file_name', encoding='UTF-8')
    fid.read() #read unicode data
    fid.close()

    ```
