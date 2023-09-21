# Android-Auto-Install-APK
一个可以给多个安卓设备自动安装多个APK的脚本，可同时对多个安卓设备进行批量安装。
# 运行环境
Pyton 3.8以上
Windows 7以上
~~~bash
> python -V
Python 3.11.5
~~~
~~~bash
OS 名称:  Microsoft Windows 10 专业版
OS 版本:  10.0.19045 暂缺 Build 19045
~~~
# 使用说明
！！！需要手动新建一个名字为apk的文件夹！！！
完整目录结构应该是这样的：
~~~text
G:\ANDROID-TOOLS
│  AdbWinApi.dll
│  AdbWinUsbApi.dll
│  libwinpthread-1.dll
│  main.py
│  NOTICE.txt
│  source.properties
│  adb.exe
└─apk
~~~
将需要安装的所有APK文件放到apk文件夹内，将多个安卓设备的USB调试模式打开，并接入到电脑上。运行main.py，即可自动检查apk文件夹下的所有文件进行安装。
可以将apk文件夹内放入一个或多个安卓apk文件，即可时间对多个安卓设备安装多个应用。
~~~python
python mian.py
~~~
