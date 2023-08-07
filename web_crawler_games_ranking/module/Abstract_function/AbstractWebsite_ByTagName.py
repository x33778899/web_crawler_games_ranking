# 定義父類別

import module.Common_use as common_use

from module.Abstract_function.AbstractWebsite import AbstractWebsite


class AbstractWebsite_ByTagName(AbstractWebsite):
    def __init__(self):
        super().__init__()

    # 透過tag-name針對一個頁籤爬蟲
    @classmethod
    def reptile_by_tag(cls, name, attributes, url, target="textContent"):
        # 1. 建立網頁驅動
        wd = common_use.createWd(url)

        # 2. 網頁睡眠
        common_use.web_sleep()

        # 3. 計算檔名
        file_name = common_use.calculateFileName(name)

        # 4. 計算網頁排名陣列
        web_rank_string_array = common_use.calculateWebRankDataByTagNameElements(attributes,
                                                                                 wd,
                                                                                 target)

        # 5. 寫檔
        common_use.write_data(web_rank_string_array, file_name, url)


