import io, sys, time, re, os
import winreg

#表项路径
xpath = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"


# 设定代理,enable:是否开启,proxyIp:代理服务器ip及端口,IgnoreIp:忽略代理的ip或网址
def setProxy(enable, proxyIp, IgnoreIp):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, xpath, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, enable)
        winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxyIp)
        winreg.SetValueEx(key, "ProxyOverride", 0, winreg.REG_SZ, IgnoreIp)
    except Exception as e:
        print("ERROR: " + str(e.args))
    finally:
        None


# 开启，定义代理服务器ip及端口，忽略ip内容(分号分割)
def enableProxy():
    proxyIP = "proxy.huawei.com:8080"
    IgnoreIp = "*.athuawei.com;*.hic.cloud;*.hisilicon.*;*.hisilicon.com;*.huawei.com;*.huaweimarine.com;*.huaweimossel.com;*.huaweimossel.com.cn;*.huaweistatic.com;*.huaweisymantec.com;*.hw3static.com;*.hwht.cn;*.hwht.com;*.hwtrip.com;*.hyhlloan.com;*.inhuawei.com;*.pinjiantrip.com;*.smartcom.cc;*.vmall.huawei.com;10.*;100.10*;100.11*;100.120.*;100.121.*;100.122.*;100.123.*;100.124.*;100.125.*;100.126.*;100.64.*;100.65.*;100.66.*;100.67.*;100.68.*;100.69.*;100.7*;100.8*;100.9*;127.0.0.1;172.16.*;172.17.*;172.18.*;172.19.*;172.20.*;172.21.*;172.22.*;172.23.*;172.24.*;172.25.*;172.26.*;172.27.*;172.28.*;172.29.*;172.30.*;172.31.*;172.32.*;192.168.*;bbs*.huaweidevice.com;meeting.huawei.com;support.huaweidevice.com;vplus.huawei.com;vportal.huawei.com;www*.huaweidevice.com;<local>;"
    print(" Setting proxy")
    setProxy(1, proxyIP, IgnoreIp)
    print(" Setting success")


# 关闭清空代理
def disableProxy():
    print(" Empty proxy")
    setProxy(0, "", "")
    print(" Empty success")


def main():
    place = input("\n\nInternet Settings Proxy: ?(open or close)\n")
    try:
        if place == "close":
            disableProxy()
        elif place == "open":
            enableProxy()
        else:
            print("please input 'open' or 'close'(Internet Settings Proxy)!")
            main()
    except Exception as e:
        print("ERROR: " + str(e.args))
    finally:
        os.system('taskkill /F /IM  iexplore.exe')
        os.system('iexplore.exe')
        place2 = input("Press ENTER to close ...\n")
#   place2 = input("Any key to close ...\n")


if __name__ == '__main__':
    main()