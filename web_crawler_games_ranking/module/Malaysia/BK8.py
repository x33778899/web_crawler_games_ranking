import os

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByXPath import AbstractWebsite_ByXPath


class BK8(AbstractWebsite_ByXPath):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        dictionary_file_name = {
            "/BK8_nextspin": "https://www.bk8link18.com/en-my/slots/nextspin",
            "/BK8_spadeGaming": "https://www.bk8link18.com/en-my/slots/spadeGaming",
            "/BK8_pragmaticPlay": "https://www.bk8link18.com/en-my/slots/pragmaticPlay",
            "/BK8_jili": "https://www.bk8link18.com/en-my/slots/jili",
            "/BK8_hcslot": "https://www.bk8link18.com/en-my/slots/hcslot",
            "/BK8_ygr": "https://www.bk8link18.com/en-my/slots/ygr",
            "/BK8_funkygames": "https://www.bk8link18.com/en-my/slots/ygr",
            "/BK8_joker": "https://www.bk8link18.com/en-my/slots/joker",
            "/BK8_habanero": "https://www.bk8link18.com/en-my/slots/habanero",
            "/BK8_netent": "https://www.bk8link18.com/en-my/slots/netent",
            "/BK8_redtiger": "https://www.bk8link18.com/en-my/slots/redtiger",
            "/BK8_asia-gaming": "https://www.bk8link18.com/en-my/slots/asia-gaming",
            "/BK8_asia-gameplay": "https://www.bk8link18.com/en-my/slots/gameplay",
            "/BK8_microGamingPlus": "https://www.bk8link18.com/en-my/slots/microGamingPlus",
            "/BK8_toptrendgaming": "https://www.bk8link18.com/en-my/slots/toptrendgaming",
            "/BK8_playTech": "https://www.bk8link18.com/en-my/slots/playTech",
            "/BK8_cq9": "https://www.bk8link18.com/en-my/slots/cq9"
        }

        super().reptile_by_xpath_multi_tab(dictionary_file_name,
                                           "//*[@id='root']/div/div[6]/div/div[4]/div[2]/div[",
                                           ']/div/div[2]/div/p',
                                           1,
                                           40,
                                           "//*[@id='root']/div/div[6]/div/div[4]/div[1]/div[1]/div[2]", save_path)

