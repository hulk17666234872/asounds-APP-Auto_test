import pytest
import uiautomator2 as u2
d = u2.connect('266a0923')
import time
def device_connect_():
    d = u2.connect('266a0923')

def reconnect_txt_():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\reconnecttest.txt', 'a')
    k = '      '
    name = '回连成功'
    jg.write('\n' + f_time + k + name)
    jg.close()
def open_settings_():
    d.press("home")
    d.app_start("com.android.settings",wait=True)
def test_reconnecteded():
    device_connect_()
    d.press("home")
    open_settings_()
    d(resourceId="android:id/title", text="蓝牙").click(timeout=2)
    for i in range(100):
        d(resourceId="android:id/summary").click()
        time.sleep(1)
        d(resourceId="android:id/button1").click()
        time.sleep(1)
        d(resourceId="android:id/summary").click()
        time.sleep(8)
        reconnect_txt_()
    assert d(resourceId="android:id/button1").click
if __name__ == '__main__':
    pytest.main(['--html=../report/test_discbyhand.html', '草稿3.py'])














