import time
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver import Firefox, FirefoxProfile


class ChapterDownloader:

    def __init__(
            self, executable_path='/Users/soumikrakshit/webDrivers/geckodriver',
            dump_path='/Users/soumikrakshit/Workspace/comicsDownloader/dump/'):
        profile = FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", dump_path)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
        self.browser = Firefox(profile, executable_path=executable_path)

    def download_images(self, url):
        self.browser.get(url)
        ul_tag = self.browser.find_elements_by_class_name('container-chapter-reader')[0]
        img_tags = ul_tag.find_elements_by_tag_name('img')
        action = ActionChains(self.browser)
        for index, img_tag in enumerate(img_tags):
            self.browser.execute_script("arguments[0].scrollIntoView();", img_tag)
            action.move_to_element(img_tag)
            pyautogui.moveTo(960, 540)
            pyautogui.click(button='right')
            for _ in range(4):
                pyautogui.press('down')
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(3)
        self.browser.quit()
