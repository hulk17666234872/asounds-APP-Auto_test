import pytest
import uiautomator2 as u2
d = u2.connect('266a0923')
import time
def device_connect_():
    d = u2.connect('266a0923')
def open_settings_():
    d.press("home")
    d.app_start("com.android.settings",wait=True)
def Play_music_():
    d.app_start('com.kugou.android', wait=True)
    d(resourceId="com.kugou.android:id/l4e").click()
    time.sleep(1)
    d(resourceId="com.kugou.android:id/qe3").click()
    time.sleep(20)
def test_AAC_SBC_Music_check():
    device_connect_()
    open_settings_()
    d(resourceId="android:id/title", text="蓝牙").click()
    for i in range(10):
    d(resourceId="com.android.settings:id/preference_detail").click()
    d(resourceId="android:id/title", text="AAC").click()
    d.watcher.start(2.0)
    d.watcher("功能开启提示").when("确定").click()
    d.watcher.reset()
    time.sleep(2)
    Play_music_()
    AAC_SBC_Music_check()
    d.app_stop("com.kugou.android")
    d.app_stop("com.android.settings")
    assert d(resourceId="android:id/title", text="AAC").click

if __name__ == '__main__':
    pytest.main(['--html=../report/test_paring_connect_phone.html', '草稿1.py'])
















