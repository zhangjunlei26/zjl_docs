#说明#

## 限制最大打开文件数和进程数
launchctl limit maxfiles 120000 unlimited
launchctl limit maxfiles 120000 180000
launchctl limit maxfiles 4096 8192

编辑/etc/sysctl.conf，添加以下行
kern.maxfiles=20480


编辑 /etc/launchd.conf，添加以下行

#limit maxfiles 120000 unlimited
limit maxfiles 8192 20480
limit maxproc 1000 2000
