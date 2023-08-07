from enum import IntEnum

from module.Aggregation.Aggregation import Aggregation
from module.Malaysia.AW8 import AW8
from module.Malaysia.B9_Casino import B9_Casino
from module.Malaysia.BK8 import BK8
from module.Malaysia.K9Win import K9Win
from module.Malaysia.Lucky_Block import Lucky_Block
from module.Malaysia.ME88 import ME88
from module.Malaysia.Maxim88 import Maxim88
from module.Malaysia.UEA8 import UEA8
from module.Malaysia.Website_12Play import Website_12Play
from module.Malaysia.Website_22bet import Website_22bet
from module.Malaysia.Website_96M import Website_96M
from module.Philippines.Bcasino import Bcasino
from module.Philippines.Bit_Starz import Bit_Starz
from module.Philippines.Ice_Casino import Ice_Casino
from module.Philippines.King_Billy_Casino import King_Billy_Casino
from module.Philippines.Mansioncasino import Mansioncasino
from module.Philippines.Megaslot import Megaslot
from module.Philippines.Wazamba import Wazamba
from module.Philippines.Website_20_Bet import Website_20_Bet
from module.Philippines.White_Lion import White_Lion


class Action_execution(IntEnum):
    REPTILE = 1
    AGGREGATION = 2

    @classmethod
    def reptile(cls):
        # # 菲律賓
        Ice_Casino().reptile()
        Website_20_Bet().reptile()
        Megaslot().reptile()
        King_Billy_Casino().reptile()
        Bit_Starz().reptile()
        Mansioncasino.reptile()
        Bcasino().reptile()
        White_Lion().reptile()  # 熱門遊戲隨機順序
        Wazamba().reptile()  # 特別處理slot
        #
        # # 馬來西亞
        BK8().reptile()
        Website_12Play().reptile()
        ME88().reptile()
        Maxim88().reptile()
        B9_Casino().reptile()  # 用定位抓會很奇怪
        Lucky_Block().reptile()
        UEA8().reptile()
        AW8().reptile()  # 與96M 幾乎相同只有網址不同
        K9Win().reptile()
        Website_22bet().reptile()
        Website_96M().reptile()  # 與AW8 幾乎相同只有網址不同

    @classmethod
    def aggregate(cls, top_count):
        Aggregation.start_aggregation(top_count)
