import pytest
import uiautomator2 as u2
import time
d =u2.connect('266a0923')
def device_connect_():
    d = u2.connect('266a0923')
def open_settingsss_():
    d.press("home")
    d.app_start("com.android.settings",wait=True)
    d(resourceId="android:id/title", text="蓝牙").click()
    time.sleep(2)
def Screenshot100():
    d.screenshot(r'D:\续航测试\100.png')
def Screenshot90():
    d.screenshot(r'D:\续航测试\90.png')
def Screenshot80():
    d.screenshot(r'D:\续航测试\80.png')
def Screenshot70():
    d.screenshot(r'D:\续航测试\70.png')
def Screenshot60():
    d.screenshot(r'D:\续航测试\60.png')
def Screenshot50():
    d.screenshot(r'D:\续航测试\50.png')
def Screenshot40():
    d.screenshot(r'D:\续航测试\40.png')
def Screenshot30():
    d.screenshot(r'D:\续航测试\30.png')
def Screenshot20():
    d.screenshot(r'D:\续航测试\20.png')
def Screenshot10():
    d.screenshot(r'D:\续航测试\10.png')
def Screenshot0():
        d.screenshot(r'D:\续航测试\0.png')
def Battery100_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\100.txt', 'a')
    k = '      '
    name = '100电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Battery90_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\90.txt', 'a')
    k = '      '
    name = '90电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Battery80_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\80.txt', 'a')
    k = '      '
    name = '80电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Battery70_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\70.txt', 'a')
    k = '      '
    name = '70电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Battery60_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\60.txt', 'a')
    k = '      '
    name = '60电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Battery50_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\50.txt', 'a')
    k = '      '
    name = '50电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Battery40_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\40.txt', 'a')
    k = '      '
    name = '40电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Battery30_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\30.txt', 'a')
    k = '      '
    name = '30电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Battery20_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\20.txt', 'a')
    k = '      '
    name = '20电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Battery10_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\10.txt', 'a')
    k = '      '
    name = '10电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Battery0_txt():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\0.txt', 'a')
    k = '      '
    name = '0电量持续时间'
    jg.write('\n' + f_time + k + name)
    jg.close()
def test_xuhan100():
    open_settingsss_()
    time.sleep(2)
    for i in range(100000000):
        d.watcher.start(2.0)
        d.watcher.when('已连接 | 电量为 100% | 使用中').click()
        time.sleep(2)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Battery100_txt()
        Screenshot100()
assert d.watcher.when('已连接 | 电量为 100% | 使用中').click

def test_xuhan90():
    open_settingsss_()
    time.sleep(2)
    for i in range(100000000):
        d.watcher.start(2.0)
        d.watcher.when('已连接 | 电量为 90% | 使用中').click()
        time.sleep(2)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Battery90_txt()
        Screenshot90()
assert d.watcher.when('已连接 | 电量为 90% | 使用中').click
def test_xuhan80():
    open_settingsss_()
    time.sleep(2)
    for i in range(100000000):
        d.watcher.start(2.0)
        d.watcher.when('已连接 | 电量为 80% | 使用中').click()
        time.sleep(2)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Battery80_txt()
        Screenshot80()
assert d.watcher.when('已连接 | 电量为 80% | 使用中').click
def test_xuhan70():
    open_settingsss_()
    time.sleep(2)
    for i in range(100000000):
        d.watcher.start(2.0)
        d.watcher.when('已连接 | 电量为 70% | 使用中').click()
        time.sleep(2)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Battery70_txt()
        Screenshot70()
assert d.watcher.when('已连接 | 电量为 70% | 使用中').click
def test_xuhan60():
    open_settingsss_()
    time.sleep(2)
    for i in range(100000000):
        d.watcher.start(2.0)
        d.watcher.when('已连接 | 电量为 60% | 使用中').click()
        time.sleep(2)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Battery60_txt()
        Screenshot60()
assert d.watcher.when('已连接 | 电量为 60% | 使用中').click
def test_xuhan50():
    open_settingsss_()
    time.sleep(2)
    for i in range(100000000):
        d.watcher.start(2.0)
        d.watcher.when('已连接 | 电量为 50% | 使用中').click()
        time.sleep(2)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Battery50_txt()
        Screenshot50()
assert d.watcher.when('已连接 | 电量为 50% | 使用中').click
def test_xuhan40():
    open_settingsss_()
    time.sleep(2)
    for i in range(100000000):
        d.watcher.start(2.0)
        d.watcher.when('已连接 | 电量为 40% | 使用中').click()
        time.sleep(2)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Battery40_txt()
        Screenshot40()
assert d.watcher.when('已连接 | 电量为 40% | 使用中').click
def test_xuhan30():
    open_settingsss_()
    time.sleep(2)
    for i in range(100000000):
        d.watcher.start(2.0)
        d.watcher.when('已连接 | 电量为 30% | 使用中').click()
        time.sleep(2)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Battery30_txt()
        Screenshot30()
assert d.watcher.when('已连接 | 电量为 30% | 使用中').click
def test_xuhan20():
    open_settingsss_()
    time.sleep(2)
    for i in range(100000000):
        d.watcher.start(2.0)
        d.watcher.when('已连接 | 电量为 20% | 使用中').click()
        time.sleep(2)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Battery20_txt()
        Screenshot20()
assert d.watcher.when('已连接 | 电量为 20% | 使用中').click
def test_xuhan10():
    open_settingsss_()
    time.sleep(2)
    for i in range(100000000):
        d.watcher.start(2.0)
        d.watcher.when('已连接 | 电量为 10% | 使用中').click()
        time.sleep(2)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Battery10_txt()
        Screenshot10()
assert d.watcher.when('已连接 | 电量为 10% | 使用中').click
def test_Power_off():
    open_settingsss_()
    for i in range(1000000):
        d(resourceId="android:id/summary").click()
        time.sleep(10)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        Screenshot0()
        Battery0_txt()
assert d(resourceId="android:id/button2").click

if __name__ == '__main__':
    pytest.main(['--html=../report/test_Total.html', '续航监控草稿.py'])




