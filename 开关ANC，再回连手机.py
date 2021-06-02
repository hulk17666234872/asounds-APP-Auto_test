import pytest
import uiautomator2 as u2
import time
d =u2.connect('266a0923')
for i in range (1000):
    d.press("home")
    d(resourceId="com.miui.home:id/icon_icon", description="AUSOUNDS").click()
    d(resourceId="com.realsil.ausounds:id/tab_denoise").click()
    d(resourceId="com.realsil.ausounds:id/lin_anc").click()
    time.sleep(2)
    d(resourceId="com.realsil.ausounds:id/lin_anc").click()
    time.sleep(2)
    d.press("home")
    d(resourceId="com.miui.home:id/icon_icon", description="设置").click()
    d.xpath('//*[@resource-id="com.android.settings:id/scroll_headers"]/android.widget.LinearLayout[5]/android.widget.RelativeLayout[1]').click()
    d(resourceId="android:id/checkbox").click()
    time.sleep(10)
    d(resourceId="android:id/checkbox").click()
    time.sleep(10)
    d.press("home")
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    jg = open(r'D:\test.txt', 'a')
    k = '      '

    name = 'Pass'

    jg.write('\n' + f_time + k + name)

    jg.close()
#d(scrollable=True).scroll.horiz.toBeginning(steps=100, max_swipes=1000)滑动到最左边
