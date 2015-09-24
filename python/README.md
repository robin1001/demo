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


## python��������
* �ַ��� utf8 
    * ASCII:
    * latin1=iso-8859-1=ISO-8859 Latin1��ISO-8859-1�ı�������Щ������д��Latin-1, ����ASCII
    * Non-ISO extended-ASCII: ISO֮�����չASCII
    * UTF8
    * GBK gb2312
* �鿴�ļ�����linux����
    * file file_name
    * file -i file_name
    * iconv -f latin1 -t utf8 inputfile
* vim �鿴�ļ����� 
    * �鿴 set fileencoding
    * ���� set encoding=utf-8
    * ��� set fileencodings=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
* python ����
    * coding=utf-8
    * ���������� �����ļ����� �ն˱���
    * codec
    ```python
    import codecs
    fid = codecs.open('file_name', encoding='UTF-8')
    fid.read() #read unicode data
    fid.close()

    ```
