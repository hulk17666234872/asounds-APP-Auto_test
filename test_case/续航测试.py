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
#def Screenshot():
    #d.screenshot(r'D:\续航测试\未连接.png')
def xuhang_txt_():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\续航测试\xuhan.txt', 'a')
    k = '      '
    name = '最后续航'
    jg.write('\n' + f_time + k + name)
    jg.close()
def test_xuhan():
    open_settingsss_()
    for i in range(1000000):
        d(resourceId="android:id/summary").click()
        time.sleep(10)
        d(resourceId="android:id/button2").click()
        time.sleep(2)
        d.screenshot(r'D:\续航测试\未连接.png')
        #d.watcher.start(2.0)
        #d.watcher("已连接 | 电量为 100% | 使用中")
        #d.watcher.reset()
        xuhang_txt_()
    assert d(resourceId="android:id/button2").click
if __name__ == '__main__':
    pytest.main(['--html=../report/test_xuhan.html', '续航测试.py'])




