import time


class ScreenShot(object):

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self):
        current_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        pic_path = '../report/screenshot/' + current_time + '.png'
        self.driver.save_screenshot(pic_path)
        print('screenshot:' + current_time + '.png')
# screen_shot = ScreenShot(self.driver)
# screen_shot.screen_shot("testscreenshotname")
