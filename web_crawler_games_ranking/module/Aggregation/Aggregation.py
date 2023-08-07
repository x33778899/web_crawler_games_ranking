import csv
import os
from collections import Counter, defaultdict
from difflib import SequenceMatcher

import module.Common_use as common_use


class Aggregation:
    EQUALS = "equals"
    LIKE = "like"
    SEARCH_MODES = [EQUALS, LIKE]

    # 輸入在這邊可以在這邊選擇如何處理還未處理過的字典資料
    @classmethod
    def _select_mode_calculate(cls, curr_dir, folder_path, group_data, method, top_count):
        if method == cls.EQUALS:
            output_path, value = cls._equals_calculate(curr_dir, folder_path, group_data, method, top_count)
        elif method == cls.LIKE:
            output_path, value = cls._like_calculate(curr_dir, folder_path, group_data, method, top_count)
        return output_path, value

    # 讀取資料夾下的 csv 檔案，並進行聚合計算
    @classmethod
    def start_aggregation(cls, top_count):
        read_folder_path = "./Website_ranking"
        write_folder_path = "./Aggregation_data"
        # 1.清除 write_folder_path 目錄下的 csv 檔案
        cls._delete_csv_files(write_folder_path)
        # 2.讀取檔案得到dictionary
        aggregation_data = cls._read_data(read_folder_path)
        game_count = []
        game_url = defaultdict(list)  # 將字典初始化為默認列表
        for curr_dir, group_data in aggregation_data.items():
            for data in group_data:
                game_count.append(data[0])  # 用來計算
                game_url[data[0]].append(data[1])  # 用來放網址
            for mode in cls.SEARCH_MODES:
                # 3.依照模式處理
                output_path, value = cls._select_mode_calculate(curr_dir, write_folder_path, game_count, mode,
                                                                top_count)
                # 4.寫入檔案
                cls._write_data(game_url, output_path, value)

    # 寫入資料
    @classmethod
    def _write_data(cls, game_url, output_path, value):
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            for data in value:
                game_url_value = game_url[data[0]]
                # 將列表中的每個值都轉換為字符串，並在每個值之間添加一個換行符號
                game_url_str = "\n".join(str(url) for url in game_url_value)
                # 使用雙引號將值包起來，並用逗號連接起來
                writer.writerow([data[0], data[1], game_url_str])

    #  讀取csv資料存在字典
    @classmethod
    def _read_data(cls, read_folder_path):
        data_dict = {}
        prev_dir = None
        # 讀取/Website_ranking目錄下資料夾裡的csv檔
        for subfolder in os.listdir(read_folder_path):
            subfolder_path = os.path.join(read_folder_path, subfolder)
            # 這個資料夾用來放置具聚合玩的資料不參加聚合
            if os.path.isdir(subfolder_path):
                file_paths = [os.path.join(subfolder_path, file) for file in os.listdir(subfolder_path)
                              if file.endswith('.csv')]
                if not file_paths:
                    continue
                # 一個資料夾目錄裝完資料就要開始進行資料處理
                curr_dir = cls._data_handle(prev_dir, subfolder)
                group_data = cls._storing_data(file_paths)
                data_dict[curr_dir] = group_data  # 將 curr_dir 和 group_data_list 存入字典物件中
                prev_dir = curr_dir
        return data_dict  # 回傳字典物件

    # 一個資料夾目錄裝完資料就要開始進行資料處理
    @classmethod
    def _data_handle(cls, prev_dir, subfolder):
        curr_dir = subfolder
        if prev_dir != curr_dir:
            prev_dir = curr_dir
        return curr_dir

    # 模糊搜選擇
    @classmethod
    def _like_calculate(cls, curr_dir, folder_path, group_data, method, top_count):
        aggregated_data = {}
        cls._like_search(aggregated_data, group_data)
        value = Counter(aggregated_data).most_common(top_count)
        output_path = os.path.join(folder_path, curr_dir + common_use.calculateFileName("_" + method))
        return output_path, value

    # 絕對相等搜索
    @classmethod
    def _equals_calculate(cls, curr_dir, folder_path, group_data, method, top_count):

        value = Counter(group_data).most_common(top_count)
        output_path = os.path.join(folder_path, curr_dir + common_use.calculateFileName("_" + method))

        return output_path, value

    # 模糊搜索判斷
    @classmethod
    def _like_search(cls, aggregated_data, array_data):
        for game_name in array_data:
            similar_game = None
            for existing_game in aggregated_data.keys():
                if SequenceMatcher(None, game_name, existing_game).ratio() >= 0.9:  # 判斷相似度
                    similar_game = existing_game
                    break
            if similar_game:
                aggregated_data[similar_game] += 1
            else:
                aggregated_data[game_name] = 1

    # 依照不同目錄存取資料
    @classmethod
    def _storing_data(cls, file_paths):
        group_data = []
        for file_path in file_paths:
            with open(file_path, 'r', encoding="utf-8", newline="") as f:
                reader = csv.reader(f)
                data = list(reader)
                group_data.extend(data)
        return group_data

    # 清除folder_path目錄下的csv
    @staticmethod
    def _delete_csv_files(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
