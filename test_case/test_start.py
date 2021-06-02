import pytest
import uiautomator2 as u2
import time
d =u2.connect('266a0923')
#@pytest.mark.start
def test_start_start():
    d = u2.connect('266a0923')
    for i in range(5):
        d.app_start('com.kugou.android', wait=True)
        d.app_stop('com.kugou.android')
    assert d.app_start#('com.kugou.android')
#pytest.main(['-m start'])
if __name__ == '__main__':
    pytest.main(['--html=../report/test_start.html', 'test_start.py'])