木葉商城
專案完整介紹影片：https ://youtu.be/a6QtKTl5-sc
流程圖
![image](https://user-images.githubusercontent.com/110946641/206617312-8da65f11-8a23-4ad0-927a-97d9cd330ade.png)

的
專案內容說明
含base.html總需要7個頁面，3個表格
前端使用HTML、CSS、Javascript、Bootstrap
後端使用python Django
資源庫使用ORM方式編寫，前面開發使用mariadb，後面為將資源庫打包在專案中，改用Django內部構建的sqlite
首頁圖示(index.html)
圖片 圖片 圖片

選擇商品資訊後，進入詳細商品介紹頁面(detail.html)
圖片

選擇商品數量後，點選加入購物車後，進入購物車頁面(cart.html)
圖片

在此處有四個功能按鈕
繼續購買：點選後返回商品目錄(menu.html)
更新購物車：可在數量欄位直接輸入要購買的商品數量，點下更新購物車，購物車的商品數量及金幣平均會調整。
清空購物車: 可清空購物車所有內容。
我要結帳：進入結帳頁面。
在本頁面會出現兩個推薦商品，每次進入頁面就會亂數更新商品。
點選我要結帳點擊後，進入結帳頁面，可核對選購商品內容，以及輸入收件人資訊(cartorder.html)
圖片

此處有三個功能按鈕
繼續購買：點選後，來到商品目錄頁面(menu.html)
修改購物車內容: 點選後，來到購物車頁面(cart.html)
送出：點選後，來到訂購單完成頁面(cartok.html)
購買完成通知
圖片

同時，系統亦會自動寄存到顧客所填的郵箱
圖片
