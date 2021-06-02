import pytest
import uiautomator2 as u2
d = u2.connect('266a0923')
import time
def device_connect_():
    d = u2.connect('266a0923')
def open_settings_():
    d.press("home")
    d.app_start("com.android.settings",wait=True)
def test_Pairing_Connect_Phone_check():
    device_connect_()
    open_settings_()
    d(resourceId="android:id/title", text="蓝牙").click()
    time.sleep(2)
    for i in range(100):
        d(resourceId="com.android.settings:id/preference_detail").long_click()
        d(resourceId="android:id/title", text="取消配对").click()
        time.sleep(2)
        d.watcher.start(2.0)
        d.watcher.when('AIHOOR A4').click()
        time.sleep(6)
        d.watcher.reset()
        #d(resourceId="com.android.settings:id/pairing_accept_button").click()备用方案
        d.watcher.start(2.0)
        d.watcher.when("配对").click()
        time.sleep(8)
        d.watcher.reset()
    assert d(resourceId="android:id/title", text="取消配对").click

if __name__ == '__main__':
    pytest.main(['--html=../report/test_paring_connect_phone.html', '草稿2.py'])
















