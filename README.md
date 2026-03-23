# who_isn't_your_fan
看看哪個傢伙沒有回追你

IG - > 個人檔案 -> 右上角三條線 -> 帳號管理中心 -> 你的資訊和權限 -> 匯出你的資訊 -> 建立匯出檔案 -> (選擇你要查詢的帳號) -> 匯出到裝置 -> 設定資料如下：<br>
自訂資訊：僅粉絲及追蹤對象
日期範圍：不限時間
格式：JSON
影像畫質：不限定
-> 開始匯出 -> (輸入密碼) -> (自動開始匯出)
-> 至E-Mail收郵件
首先會收到一個「你的 Meta 下載要求正在處理中」為主旨的郵件，什麼都不要做，稍等即可。
接著你會收到「你要下載的 Meta 資訊已準備就緒」
然後點選郵件中的 「 export your information 」 連結 -> 按下載 -> Download -> (輸入密碼)

解壓縮 -> 進入 `C:\Users\user\Downloads\gay's fans\connections\followers_and_following` 資料夾
裡面的`followers_1.json`是粉絲名單、`following.json`是追蹤者名單

把本程式放到`followers_and_following`中，並利用編輯軟體將 第3行 及 第6行 的檔案位置設定到前述之地址
(例如：`with open('connections\\followers_and_following\\followers_1.json', 'r') as f:`)
運行即可。
