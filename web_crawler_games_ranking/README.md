main: 
    ACTION == Action_execution.REPTILE      執行爬蟲會把已經產生class的網站爬蟲遊戲抓下來
    ACTION == Action_execution.AGGREGATION  執行聚合 將已經產生的csv檔依國家分類顯示出重複較多次數的遊戲
    Action_execution.polymerization(Country)   裡面的參數選擇國家
                                        

要新增網站只要在該國家目錄下新增class即可

如果要新增國家在File_placement目錄下新增國家資料夾,並且在module新增相同的資料夾

爬蟲:
    可以依照class_name , tag_name , xpath 三種方式進行爬蟲

