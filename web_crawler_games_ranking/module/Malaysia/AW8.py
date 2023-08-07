import os

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByXPath import AbstractWebsite_ByXPath


class AW8(AbstractWebsite_ByXPath):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)

        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)

        dictionary_file_name = {
            "/AW8_nextSpin": "https://www.aw8myr2.com/en-my/slots/nextspin",
            "/AW8_spadeGaming": "https://www.aw8myr2.com/en-my/slots/spadeGaming",
            "/AW8_pragmaticPlay": "https://www.aw8myr2.com/en-my/slots/pragmaticPlay",
            "/AW8_jili": "https://www.aw8myr2.com/en-my/slots/jili",
            "/AW8_microGamingPlus": "https://www.aw8myr2.com/en-my/slots/microGamingPlus",
            "/AW8_playTech": "https://www.aw8myr2.com/en-my/slots/playTech",
            "/AW8_gameplay": "https://www.aw8myr2.com/en-my/slots/gameplay",
            "/AW8_asia-gaming": "https://www.aw8myr2.com/en-my/slots/asia-gaming",
            "/AW8_habanero": "https://www.aw8myr2.com/en-my/slots/habanero",
            "/AW8_toptrendgaming": "https://www.aw8myr2.com/en-my/slots/toptrendgaming",
            "/AW8_netent": "https://www.aw8myr2.com/en-my/slots/netent",
            "/AW8_redtiger": "https://www.aw8myr2.com/en-my/slots/netent",
            "/AW8_hcslot": "https://www.aw8myr2.com/en-my/slots/hcslot",
            "/AW8_royalslotgaming": "https://www.aw8myr2.com/en-my/slots/royalslotgaming",
            "/AW8_YesGetRich": "https://www.aw8myr2.com/en-my/slots/ygr"
        }

        super().reptile_by_xpath_multi_tab(dictionary_file_name,
                                           '//*[@id="root"]/div/div[4]/div/div[4]/div/div/div[',
                                           ']/div/div/div[2]/div',
                                           2,
                                           40,
                                           "//*[@id='root']/div/div[4]/div/div[3]/div/div[1]/div[2]", save_path)

        # 不知道什麼原因它的位置不一樣
        cls.reptile_by_xpath_one_tab(save_path + "/AW8_joker",
                                     "//*[@id='root']/div/div[4]/div/div[4]/div/div/div[",
                                     "]/div/div/div/div",
                                     2,
                                     40,
                                     "https://www.aw8myr2.com/en-my/slots/joker",
                                     "//*[@id='root']/div/div[4]/div/div[3]/div/div[1]/div[2]")
