import os

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByClass import AbstractWebsite_ByClass


class Bit_Starz(AbstractWebsite_ByClass):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        super().reptile_by_class(save_path + "/Bit_Starz", 'c-game-title__text',
                                 "https://www.bitstarz.com/zh-CN/slots")

