import numpy as np
from scipy.optimize import linear_sum_assignment


class Sanctuaries:
    def __init__(self,
                 kou_bou=0,  # M攻防
                 bin_sho=0,  # M敏捷
                 sho_geki=0,  # M衝撃
                 katsu_ryoku=0,  # M活力
                 sei_ki=0,  # M生気
                 tai_ryoku=0,  # M耐力
                 bou_gyo=0,  # M防御
                 bou_gyo_mu_shi=0,  # M防御無視
                 kyo_ko=0,  # M強攻
                 kyo_ko_tei_ko=0  # M強攻抵抗
                 ):
        self.kou_bou = kou_bou
        self.bin_sho = bin_sho
        self.sho_geki = sho_geki
        self.katsu_ryoku = katsu_ryoku
        self.sei_ki = sei_ki
        self.tai_ryoku = tai_ryoku
        self.bou_gyo = bou_gyo
        self.bou_gyo_mu_shi = bou_gyo_mu_shi
        self.kyo_ko = kyo_ko
        self.kyo_ko_tei_ko = kyo_ko_tei_ko

    @property
    def score(self):
        return (
                self.kou_bou +
                self.bin_sho * 2.0 +
                self.sho_geki * 1.0 +
                self.bou_gyo_mu_shi
        )


data = [
    # 極盛マッシュの杖
    [
        Sanctuaries(bin_sho=7875, sei_ki=7275),
        Sanctuaries(kou_bou=10125, kyo_ko_tei_ko=5850),
        Sanctuaries(tai_ryoku=7875, bou_gyo_mu_shi=2550),
        Sanctuaries(katsu_ryoku=8550, kyo_ko=2550),
        Sanctuaries(sho_geki=7275, bou_gyo=12450)
    ],
    # アストラ王の鎧
    [
        Sanctuaries(bin_sho=4800, sei_ki=8730),
        Sanctuaries(kou_bou=11205, kyo_ko_tei_ko=5850),
        Sanctuaries(tai_ryoku=8730, bou_gyo_mu_shi=6262),
        Sanctuaries(katsu_ryoku=8550, kyo_ko=2550),
        Sanctuaries(sho_geki=8355, bou_gyo=23142)
    ],
    # ユピテル王の法環
    [
        Sanctuaries(bin_sho=9075, sei_ki=5850),
        Sanctuaries(kou_bou=7650, kyo_ko_tei_ko=11682),
        Sanctuaries(tai_ryoku=9306, bou_gyo_mu_shi=2550),
        Sanctuaries(katsu_ryoku=12046, kyo_ko=7005),
        Sanctuaries(sho_geki=4800, bou_gyo=12450)
    ],
    # エーギル王の戦矛
    [
        Sanctuaries(bin_sho=4800, sei_ki=9648),
        Sanctuaries(kou_bou=7650, kyo_ko_tei_ko=5850),
        Sanctuaries(tai_ryoku=5850, bou_gyo_mu_shi=7450),
        Sanctuaries(katsu_ryoku=12348, kyo_ko=7450),
        Sanctuaries(sho_geki=9502, bou_gyo=26562)
    ],
    # エーギル王の戦鎧
    [
        Sanctuaries(bin_sho=4800, sei_ki=5850),
        Sanctuaries(kou_bou=13311, kyo_ko_tei_ko=13590),
        Sanctuaries(tai_ryoku=10440, bou_gyo_mu_shi=8472),
        Sanctuaries(katsu_ryoku=13140, kyo_ko=2550),
        Sanctuaries(sho_geki=4800, bou_gyo=12450)
    ],
    # エーギル王の明灯
    # [
    #     Sanctuaries(binSho=11010, seiKi=10890),
    #     Sanctuaries(kyoKouTeiKou=5850, kouBou=7650),
    #     Sanctuaries(taiRyoku=5850, bouGyoMuShi=2550),
    #     Sanctuaries(katsuRyoku=12046, kyoKou=7005),
    #     Sanctuaries(shoGeki=11010, bouGyo=31170)
    # ],
]

# スコアの重み行列作成
weights = np.array([[item.score for item in row] for row in data])
max_value = np.max(weights)
cost_matrix = max_value - weights  # コスト行列（スコア最大化→最小化に変換）

# ハンガリアン法（線形和代入）を適用
row_ind, col_ind = linear_sum_assignment(cost_matrix)

print("最適な割り当て:")
total = 0.0
for i, j in zip(row_ind, col_ind):
    value = weights[i][j]
    print(f"枠 {i + 1} → アイテム {j + 1}（スコア {value}）")
    total += value

print(f"最大スコア合計: {total}")
