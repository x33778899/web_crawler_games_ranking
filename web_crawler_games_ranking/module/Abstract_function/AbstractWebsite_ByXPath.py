# 定義父類別
from selenium.webdriver.common.by import By

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite import AbstractWebsite


# 使用xpath的方式抓取資料可以抓取大部分的東西
# 但是並非所有網站資料區間迴圈範圍超出邊界不會發生意外
# 有少部分超出邊界會抓到奇怪的東西,所以要視情況選擇抓取方式
class AbstractWebsite_ByXPath(AbstractWebsite):
    def __init__(self):
        super().__init__()

    # 透過xpath針對一個頁籤爬蟲
    @classmethod
    def reptile_by_xpath_one_tab(cls, name, path_header, path_tail, start, end, url, button, target="textContent"):
        # 1. 建立網頁驅動
        wd = common_use.createWd(url)

        # 2. 網頁睡眠
        common_use.web_sleep()

        # 3. 計算檔名
        file_name = common_use.calculateFileName(name)

        # 4. 按按鈕
        common_use.press_the_button(wd, By.XPATH, button)

        # 5. 計算網頁排名陣列
        web_rank_string_array = common_use.calculateWebRankDataByXPathElements(wd,
                                                                               start,
                                                                               end,
                                                                               path_header,
                                                                               path_tail,
                                                                               target)

        common_use.write_data(web_rank_string_array, file_name, url)

    # 透過xpath針對多個頁籤爬蟲
    @classmethod
    def reptile_by_xpath_multi_tab(cls, dictionary, path_header, path_tail, start, end, button, save_path,
                                   target="textContent"):
        for file_name, url in dictionary.items():
            cls.reptile_by_xpath_one_tab(save_path + file_name, path_header, path_tail, start, end, url, button, target)
