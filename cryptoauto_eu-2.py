import time
import pyupbit
import datetime
import requests
import numpy
import pandas


access = "yRF8Aum2SlUCxN0FuH4iAA2wsI1eOxjP8LS40lHF"
secret = "wVoI8Gx3GMv3REKGmSi1eQDOtS6DOCc2ouj04Uf6"
myToken = "ETC"

upbit = pyupbit.Upbit(access, secret)




#보유 코인 보유 현금 조회
while True:
    print(upbit.get_balance("KRW-ETC"))     # KRW-XRP 조회
    print(upbit.get_balance("KRW"))         # 보유 현금 조회
 
    ETCBAL=upbit.get_balance("KRW-ETC")
    KRWBAL=upbit.get_balance("KRW")

    import pyupbit
    import numpy as np



# OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
    df = pyupbit.get_ohlcv("KRW-ETC", interval="minute5", count=21)

    tickerETC=pyupbit.get_current_price("KRW-ETC") #해당 코인 현재가

    print(tickerETC)

    w= 20 # 기준 이동평균일 
    k= 2 # 기준 상수
 
#중심선 (MBB) : n일 이동평균선
    df["mbb"]=df["close"].rolling(w).mean()
    df["MA20_std"]=df["close"].rolling(w).std()
 
#상한선 (UBB) : 중심선 + (표준편차 × K)
#하한선 (LBB) : 중심선 - (표준편차 × K)
    df["ubb"]=df.apply(lambda x: x["mbb"]+k*x["MA20_std"],1)
    df["lbb"]=df.apply(lambda x: x["mbb"]-k*x["MA20_std"],1)
 
# df[['종가','mbb', 'ubb', 'lbb']][-200:].plot.line()

    print(df.iloc[19]["open"], df.iloc[19]["mbb"], df.iloc[19]["ubb"], df.iloc[19]["lbb"])
    print(df.iloc[20]["open"], df.iloc[20]["mbb"], df.iloc[20]["ubb"], df.iloc[20]["lbb"])
    open=df.iloc[20]["open"]
    mbb=df.iloc[20]["mbb"]
    lbb=df.iloc[20]["lbb"]
    ubb=df.iloc[20]["ubb"]
    selltap=open+(ubb-open)*2   #매도 타겟 금액
    buytap=open-(open-lbb)*2    #매수 타겟 금액
    #selltap2=mbb+(ubb-lbb)      #매도 타겟 긐액2
    #buytap2=mbb-(ubb-lbb)       #매수 타겟 금액2

    if tickerETC > selltap and (selltap-ubb)/selltap > 0.01: # 매도 논리(타겟 가격보다 현재가격이 높을때)
    
        #현재 가격이 타겟 가격보다 높은경우 
        #타겟 가격-볼벤가격 을 타겟 가격으로 나눈 값이 1% 이상일때
        #판매 수량 함수 지정(매수매도에 사용)
         upbit.sell_market_order("KRW-ETC", ETCBAL*0.5)
         #time.sleep(20)
         #upbit.buy_limit_order("KRW-ETC",ubb, ETCBAL)
         time.sleep(900)
    
    #if tickerETC > selltap2:
    
        #현재 가격이 타겟 가격보다 높은경우 
        #타겟 가격-볼벤가격 을 타겟 가격으로 나눈 값이 1% 이상일때
        #판매 수량 함수 지정(매수매도에 사용)
         #upbit.sell_market_order("KRW-ETC", ETCBAL*0.5)
         #time.sleep(20) # 볼벤 상단가 재구매를 위한 20초 sleep 타임
         #upbit.buy_limit_order("KRW-ETC",ubb, ETCBAL) #볼벤 상단가에 재구매
         #time.sleep(900)


     #불필요 # 타겟 가격이 양의 값일때
    if tickerETC < buytap and (lbb-buytap)/lbb > 0.01 and KRWBAL>5000: # 타겟 가격이 매수 가격이보다 높은 경우(함수를 만들어서 이전 매매 가격을 날짜베이스로 변수 생성)
           #매수 금액 / 수량 함수 지정(매수매도에사용)
         upbit.buy_market_order("KRW-ETC", KRWBAL*0.9995)
         #time.sleep(20) # 볼벤 상단가 재구매를 위한 20초 sleep 타임
         #upbit.sell_limit_order("KRW-ETC", KRWBAL*0.9995) #볼벤 상단가에 재구매
         time.sleep(900)
    
    #if tickerETC < buytap2 and KRWBAL>5000: # 타겟 가격이 매수 가격이보다 높은 경우(함수를 만들어서 이전 매매 가격을 날짜베이스로 변수 생성)
           #매수 금액 / 수량 함수 지정(매수매도에사용)
         #upbit.buy_market_order("KRW-ETC", KRWBAL*0.9995)
         #time.sleep(20) # 볼벤 상단가 재구매를 위한 20초 sleep 타임
         #upbit.sell_limit_order("KRW-ETC", KRWBAL*0.9995) # 볼벤 상단가 재구매를 위한 20초 sleep 타임
         #time.sleep(900)

    # 타겟 가격에 50% 매도
    # 매도 이후 매수 타겟가 로 매도 금액 만큼 매수(코인수량 늘리기)
    # 매도 이후 다음 봉 이전에 매도 하지 않음 
    
    #볼벤중단 + (상단-하단) < tickerETC 일때

#if #현재 가격이 타겟 가격보다 높은경우 
    # 타겟 가격이 매수 가격이보다 높은 경우
    # 타겟 가격에 매수
    # 타겟 가격에 매도(매수가격 보다 높은경우)
print(1)  



##RSI메모
#U(up): n일 동안의 종가 상승 분
#D(down): n일 동안의 종가 하락 분
#AU(average ups): U값의 평균
#DU(average downs): D값의 평균



#자동 매매 시작
#while True:
#if tickerETC>selltap:
#ETCBAL









# 이하 메모 또는 참고 코드

#print("bollinger_band_lower_line")


#def bollinger_band_lower_line(ticker):
#    print ('bollinger_band_lower_line')

## 매도
#print(upbit.sell_limit_order("KRW-XRP", 600, 20))
## 매수
#print(upbit.buy_limit_order("KRW-XRP", 613, 10))
