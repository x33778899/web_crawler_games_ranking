import os

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByXPath import AbstractWebsite_ByXPath


class Website_96M(AbstractWebsite_ByXPath):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        dictionary_file_name = {
            "/96M_nextSpin": "https://www.96mheng.com/en-my/slots/nextspin",
            "/96M_spadeGaming": "https://www.96mheng.com/en-my/slots/spadeGaming",
            "/96M_pragmaticPlay": "https://www.96mheng.com/en-my/slots/pragmaticPlay",
            "/96M_jili": "https://www.96mheng.com/en-my/slots/jili",
            "/96M_hcslot": "https://www.96mheng.com/en-my/slots/hcslot",
            "/96M_funkygames": "https://www.96mheng.com/en-my/slots/funkygames",
            "/96M_joker": "https://www.96mheng.com/en-my/slots/joker",
            "/96M_habanero": "https://www.96mheng.com/en-my/slots/habanero",
            "/96M_netent": "https://www.96mheng.com/en-my/slots/netent",
            "/96M_redtiger": "https://www.96mheng.com/en-my/slots/redtiger",
            "/96M_asia-gaming": "https://www.96mheng.com/en-my/slots/asia-gaming",
            "/96M_gameplay": "https://www.96mheng.com/en-my/slots/gameplay",
            "/96M_microGamingPlus": "https://www.96mheng.com/en-my/slots/microGamingPlus",
            "/96M_toptrendgaming": "https://www.96mheng.com/en-my/slots/toptrendgaming",
            "/96M_playTech": "https://www.96mheng.com/en-my/slots/playTech"
        }

        for file_name, url in dictionary_file_name.items():
            super().reptile_by_xpath_one_tab(save_path + file_name,
                                             '//*[@id="root"]/div/div[4]/div/div[4]/div/div/div[',
                                             ']/div/div/div/div',
                                             2,
                                             40,
                                             url,
                                             "//*[@id='root']/div/div[4]/div/div[3]/div/div[1]/div[2]"
                                             )

