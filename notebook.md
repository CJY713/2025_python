# 課堂筆記

### 創建虛擬環境

* 下載 virtualenv
    > pip install virtualenv

* 查看python、pip的位置
    > get-command python
    
    > get-command pip

* 創建虛擬環境
    - virtualenv --python=<直譯器路徑> <環境名稱>  
        >EX: virtualenv --python="C:\Users\Student\AppData\Local\Microsoft\WindowsApps\python.exe" scraper_venv
    - python -m virtualenv <環境名稱>
        >EX: python -m virtualenv scraper_venv
    - python -m virtualenv --python=<直譯器路徑> <環境名稱>

* 開啟虛擬環境
    - .\<環境名稱>\Scripts\activate
        > EX: .\scraper_venv\Scripts\activate

* 執行程式
    - python .\<檔案名稱>
        > EX: python .\test.py

* 離開虛擬環境
    > deactivate

* 權限設定 (PowerShell)
    > Set-ExecutionPolicy Unrestricted -Scope LocalMachine


### git 指令
* 顯示目前Git版控狀態
    > git status

* 顯示Git版控歷史
    > git log

* 加入檔案到站存區
    > git add <你的檔案路徑>

* 提交目前暫存區的內容
    > git commit -m "你的提交訊息"

* 上傳到remote
    > git push

    > git push <remote_name> <remote_branch>

* 下載(同步)目前的雲端的版本
    > git pull

    > git pull <remote_name> <remote_branch> 

    > git pull --rebase
    
    > git pull --rebase <remote_name> <remote_branch>


