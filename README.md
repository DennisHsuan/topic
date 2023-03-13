# <p align="center">木葉商城</p>
## 專案完整介紹影片：https://www.youtube.com/watch?v=a6QtKTl5-sc
## 流程圖
![image](https://user-images.githubusercontent.com/110946641/206617312-8da65f11-8a23-4ad0-927a-97d9cd330ade.png)
## 專案內容說明
- 含base.html總需要7個頁面，3個表格
- 前端使用HTML、CSS、Javascript、Bootstrap
- 後端使用python Django
- 資源庫使用ORM方式編寫，前面開發使用mariadb，後面為將資源庫打包在專案中，改用Django內部構建的sqlite

## 首頁圖示(index.html)
![image](https://user-images.githubusercontent.com/109893487/199408197-42797186-c258-47a4-935b-603284949e74.png)
![image](https://user-images.githubusercontent.com/109893487/199409886-7fc575bf-f914-43a7-876a-891be7791d35.png)
![image](https://user-images.githubusercontent.com/109893487/199410000-0eed3dd0-6019-496d-9035-ef10e59e3026.png)

## 圖選商品資訊後，進入詳細商品介紹頁面(detail.html)
![image](https://user-images.githubusercontent.com/109893487/199410175-1a8f5cf4-25d9-45a9-87bb-9f3c71fbf1a4.png)

## 選取商品數量後，點選加入購物車後，進入購物車頁面(cart.html)
![image](https://user-images.githubusercontent.com/109893487/199410331-cac207cd-7f4d-4a39-9230-f011b2379ccb.png)
- 在此處有四個功能按鈕
  - 繼續購物: 點選後回到商品目錄(menu.html)
  - 更新購物車: 可在數量欄位直接輸入想要購買的商品數量，點下更新購物車，購物車的商品數量及金額均會調整。
  - 清空購物車: 可清空購物車所有內容。
  - 我要結帳： 進入結帳頁面。
- 在此頁面會出面兩個推薦商品，每次進入頁面就會亂數更新商品。

## 點選我要結帳按鈕後，進入結帳頁面，可核對選購商品內容，及輸入收件人資訊(cartorder.html)
![image](https://user-images.githubusercontent.com/109893487/199411120-a4f04b8c-2294-4a1a-8dc3-f7b060780293.png)
- 此處有三個功能按鈕
  - 繼續購物: 點選後，來到商品目錄頁面(menu.html)
  - 修改購物車內容: 點選後，來到購物車頁面(cart.html)
  - 送出: 點選後，來到訂單完成頁面(cartok.html)

## 購單完成通知
![image](https://user-images.githubusercontent.com/109893487/199411461-232c0cf2-7fc1-419c-90ac-20f389e4515b.png)

## 同時，系統亦會自動寄信到顧客所填的email信箱
![image](https://user-images.githubusercontent.com/109893487/199411779-54031eb1-3cbd-43b1-87eb-ecd493857a5c.png)



