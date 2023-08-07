import os

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByXPath import AbstractWebsite_ByXPath


class UEA8(AbstractWebsite_ByXPath):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        dictionary_file_name = {
            "/UEA8_NextSpin": "https://www.uea8a.com/en-my/slots-landing/nextspin",
            "/UEA8_spadeGaming": "https://www.uea8a.com/en-my/slots-landing/spadeGaming",
            "/UEA8_pragmaticPlay": "https://www.uea8a.com/en-my/slots-landing/pragmaticPlay",
            "/UEA8_jilt": "https://www.uea8a.com/en-my/slots-landing/jili",
            "/UEA8_microGamingPlus": "https://www.uea8a.com/en-my/slots-landing/microGamingPlus",
            "/UEA8_joker": "https://www.uea8a.com/en-my/slots-landing/joker",
            "/UEA8_playTech": "https://www.uea8a.com/en-my/slots-landing/playTech",
            "/UEA8_funkygames": "https://www.uea8a.com/en-my/slots-landing/funkygames",
            "/UEA8_gameplay": "https://www.uea8a.com/en-my/slots-landing/gameplay",
            "/UEA8_asia-gaming": "https://www.uea8a.com/en-my/slots-landing/asia-gaming",
            "/UEA8_habanero": "https://www.uea8a.com/en-my/slots-landing/habanero",
            "/UEA8_toptrendgaming": "https://www.uea8a.com/en-my/slots-landing/toptrendgaming",
            "/UEA8_redtiger": "https://www.uea8a.com/en-my/slots-landing/redtiger",
            "/UEA8_hcslot": "https://www.uea8a.com/en-my/slots-landing/hcslot"
        }
        super().reptile_by_xpath_multi_tab(dictionary_file_name,
                                           '//*[@id="root"]/div/div[4]/div/div[2]/div[2]/div[2]/div[',
                                           ']/div/div/div[2]/div[1]',
                                           1,
                                           30,
                                           "//*[@id='root']/div/div[4]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]",
                                           save_path)

