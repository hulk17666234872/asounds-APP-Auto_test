import pytest
import uiautomator2 as u2
import time
d =u2.connect('266a0923')
#@pytest.mark.start
def open_settings_():
    d.press("home")
    d.app_start("com.android.settings",wait=True)

def device_connect_():
    d = u2.connect('266a0923')
def Play_music_():
    d.app_start('com.kugou.android', wait=True)
    d(resourceId="com.kugou.android:id/l4e").click()
    time.sleep(2)
    d(resourceId="com.kugou.android:id/qe3").click()
    time.sleep(20)

def reconnect_txt_():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\reconnecttest.txt', 'a')
    k = '      '
    name = '蓝牙回连成功'
    jg.write('\n' + f_time + k + name)
    jg.close()
def ANC_txt_():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\ANCtest.txt', 'a')
    k = '      '
    name = 'Pass'
    jg.write('\n' + f_time + k + name)
    jg.close()

def AAC_SBC_Music_check():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\AAC_SBC_Check.txt', 'a')
    k = '      '
    name = 'Pass'
    jg.write('\n' + f_time + k + name)
    jg.close()
def Pairing_Connect_Phone():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\Pairing_Connect_Phone.txt', 'a')
    k = '      '
    name = 'Pass'
    jg.write('\n' + f_time + k + name)
    jg.close()
def dis_reconnect_by_hand():
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\dis_reconnect_by_hand.txt', 'a')
    k = '      '
    name = 'Pass'
    jg.write('\n' + f_time + k + name)
    jg.close()
@pytest.mark.shit
def test_reconnect_():
    device_connect_()
    d.press("home")
    open_settings_()
    d(resourceId="android:id/title", text="蓝牙").click(timeout=2)
    print("开始耳机回连测试，请耐心等待结果")
    time.sleep(2)
    for i in range(100):
        d(resourceId="android:id/title", text="开启蓝牙").click()
        time.sleep(1)
        d(resourceId="android:id/title", text="开启蓝牙").click()
        time.sleep(8)
        reconnect_txt_()
    d(resourceId="android:id/summary").click()
    time.sleep(1)
    d.toast.get_message(default='要断开与该设备的连接吗？')
    time.sleep(1)
    d.press("home")
    d.app_stop("com.android.settings")
    assert d.toast.get_message(default='要断开与该设备的连接吗？')
def test_startANC_ausound():
    device_connect_()
    print("开始耳机ANC开关压力测试测试，请耐心等待结果")
    time.sleep(2)
    for i in range(100):
        d.app_start('com.realsil.ausounds', wait = True)
        time.sleep(5)
        d(resourceId="com.realsil.ausounds:id/tab_denoise").click()
        d(resourceId="com.realsil.ausounds:id/lin_anc").click()
        time.sleep(1)
        d(resourceId="com.realsil.ausounds:id/lin_anc").click()
        time.sleep(1)
        d.app_stop("com.realsil.ausounds")
        ANC_txt_()
        assert d(resourceId="com.realsil.ausounds:id/lin_anc").click
def test_AAC_SBC_Music_check():
    device_connect_()
    open_settings_()
    print("---开始耳机ANC开关压力测试，请耐心等待结果---")
    time.sleep(2)
    d(resourceId="android:id/title", text="蓝牙").click()
    d(resourceId="com.android.settings:id/preference_detail").click()
    time.sleep(2)
    d.swipe(410, 1258, 455, 650, 0.1)  # h向下滑动找到AAC元素
    time.sleep(2)
    for i in range(10):
        d(resourceId="android:id/title", text="AAC").click()
        time.sleep(5)
        d.watcher.start(2.0)
        d.watcher("功能开启提示").when("确定").click()
        time.sleep(5)
        d.watcher.reset()
        AAC_SBC_Music_check()
    Play_music_()
    d.app_stop("com.kugou.android")
    d.press("home")
    assert d(resourceId="android:id/title", text="AAC").click
    '''执行完毕后需要连接手机主观判断耳机播放音乐有无声音'''
@pytest.mark.cancal
def test_Pairing_Connect_Phone_check():
    device_connect_()
    open_settings_()
    print("---开始耳机取消配再连接压力测试，请耐心等待结果---")
    time.sleep(2)
    d(resourceId="android:id/title", text="蓝牙").click()
    time.sleep(2)
    for i in range(100):
        d(resourceId="com.android.settings:id/preference_detail").long_click()
        d(resourceId="android:id/title", text="取消配对").click()
        time.sleep(2)
        d.watcher.start(2.0)
        d.watcher.when('AU-Frequency ANC').click()
        time.sleep(6)
        d.watcher.reset()
        #d(resourceId="com.android.settings:id/pairing_accept_button").click()备用点击配对方案
        d.watcher.start(2.0)
        d.watcher.when("配对").click()
        time.sleep(5)
        d.watcher.reset()
        Pairing_Connect_Phone()
    assert d(resourceId="android:id/title", text="取消配对").click

def test_phone_music():
    device_connect_()
    Play_music_()
    d.app_start('com.android.contacts')
    d.xpath('//android.widget.HorizontalScrollView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
    time.sleep(3)
    d(resourceId="com.android.contacts:id/name", text="紧急电话号码").click()
    assert  d(resourceId="com.android.contacts:id/name", text="紧急电话号码").click
def test_app_backgrpund_check():
    device_connect_()
    d.app_start('com.realsil.ausounds')
    time.sleep(4)
    d.app_stop('com.realsil.ausounds')
    d.press("home")
    test_reconnect_()
    assert d.toast.get_message(default='要断开与该设备的连接吗？')
def test_RF_bluethonh_check():
    test_reconnect_()
    assert d.toast.get_message(default='要断开与该设备的连接吗？')
def test_Ausound_icon_check():
    device_connect_()
    d.app_start('com.realsil.ausounds',wait=True)
    time.sleep(2)
    d(resourceId="com.realsil.ausounds:id/tab_state").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_equilzer").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_denoise").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_ambience").click()
    time.sleep(1)
    d.app_stop('com.realsil.ausounds')
    assert d(resourceId="com.realsil.ausounds:id/tab_state").click

def test_Ausound_icon_check2():
    device_connect_()
    d.app_start('com.realsil.ausounds', wait=True)
    time.sleep(2)
    d(resourceId="com.realsil.ausounds:id/tab_state").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_equilzer").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_denoise").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_ambience").click()
    time.sleep(1)
    d.app_stop('com.realsil.ausounds')
    assert d(resourceId="com.realsil.ausounds:id/tab_equilzer").click

def test_Ausound_icon_check3():
    device_connect_()
    d.app_start('com.realsil.ausounds', wait=True)
    time.sleep(2)
    d(resourceId="com.realsil.ausounds:id/tab_state").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_equilzer").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_denoise").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_ambience").click()
    time.sleep(1)
    d.app_stop('com.realsil.ausounds')
    assert d(resourceId="com.realsil.ausounds:id/tab_denoise").click

def test_Ausound_icon_check4():
    device_connect_()
    d.app_start('com.realsil.ausounds', wait=True)
    time.sleep(2)
    d(resourceId="com.realsil.ausounds:id/tab_state").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_equilzer").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_denoise").click()
    time.sleep(1)
    d(resourceId="com.realsil.ausounds:id/tab_ambience").click()
    time.sleep(1)
    d.app_stop('com.realsil.ausounds')
    assert d(resourceId="com.realsil.ausounds:id/tab_ambience").click
#@pytest.mark.dis
def test_Disconnect_by_hand():
    device_connect_()
    d.press("home")
    open_settings_()
    d(resourceId="android:id/title", text="蓝牙").click(timeout=2)
    print("---开始断连压力测试，请耐心等待结果---")
    time.sleep(2)
    for i in range(10):
        d(resourceId="android:id/summary").click()
        time.sleep(1)
        d(resourceId="android:id/button1").click()
        time.sleep(1)
        d(resourceId="android:id/summary").click()
        time.sleep(6)
        dis_reconnect_by_hand()
    assert d(resourceId="android:id/button1").click

#def test_



#if __name__ == '__main__':
    #pytest.main(["-m","cancal"])
if __name__ == '__main__':
    pytest.main(['--html=../report/test_re.html', 'test_reconnect.py'])
    print("---测试结束，请点击Report查看测试结果！")
