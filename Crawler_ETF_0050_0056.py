import datetime
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

#Stock ID
ETF_0050_ID = 'ETF_0050'
ETF_0056_ID = 'ETF_0056'

Start_Date = datetime.datetime(2020, 1, 1) #開始日期
End_Date = datetime.datetime(2020, 12, 31) #結束日期

#Yahoo股市
ETF_0050 = web.DataReader('0050.TW', 'yahoo', Start_Date, End_Date)
ETF_0056 = web.DataReader('0056.TW', 'yahoo', Start_Date, End_Date)

# #顯示最近五筆資料
print('\n')
ETF_0050_Data = pd.DataFrame(ETF_0050)
ETF_0050_Data = ETF_0050_Data.drop(columns=['Volume','Adj Close']) #移除'Volume','Adj Close'欄 
print('0050資訊:    高價   低價   開盤   收盤')
print(round(ETF_0050_Data.tail(10),2))

print('\n')
ETF_0056_Data = pd.DataFrame(ETF_0056)
ETF_0056_Data = ETF_0056_Data.drop(columns=['Volume','Adj Close']) #移除'Volume','Adj Close'欄
print('0056資訊:    高價   低價   開盤   收盤')
print(round(ETF_0056_Data.tail(10),2))

#用to_csv存檔，並命名為“股票代號.csv”
ETF_0050_Data.to_csv(ETF_0050_ID+'.csv')
ETF_0056_Data.to_csv(ETF_0056_ID+'.csv')
print('\n')
print('已將資訊存成.csv檔')

#開啟一個名為”股票代號.db"的檔案，並與sqlite3的資料庫連結
ETF_0050_db = sqlite3.connect(ETF_0050_ID+'.db')
ETF_0056_db = sqlite3.connect(ETF_0056_ID+'.db')

#把Stock_Data寫入sqlite3裡，參數為(檔名, 資料庫, 取代原始資料)
round(ETF_0050_Data,2).to_sql(ETF_0050_ID, ETF_0050_db, if_exists='replace')
round(ETF_0056_Data,2).to_sql(ETF_0056_ID, ETF_0056_db, if_exists='replace')
print('已將資訊存成.db檔')


#繪製圖表與顯示
ETF_0050_Chart = round(ETF_0050_Data["Close"].tail(10),2).plot(grid=True,figsize=(12,5)) 
plt.title('ETF_0050_Chart')
plt.ylabel('Close')
plt.xlabel('Date')
plt.savefig("ETF_0050_Chart.jpg") #儲存圖檔
print('已將ETF_0050_Chart存成.jpg檔')
plt.show() 

ETF_0056_Chart = round(ETF_0056_Data["Close"].tail(10),2).plot(grid=True,figsize=(12,5)) 
plt.title('ETF_0056_Chart')
plt.ylabel('Close')
plt.xlabel('Date')
plt.savefig("ETF_0056_Chart.jpg")
plt.show()
print('已將ETF_0056_Chart存成.jpg檔')
