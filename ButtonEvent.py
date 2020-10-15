from microbit import *
#import main

### timerモード Aボタン押下
def ButtonCkick_A(appStatus, blockNumber, blockSurvivalTime):
#def ButtonCkick_A():
    #global appStatus
    global setTime

    if appStatus == 0 :
        #タイマー状態更新（未動作→動作中）
        appStatus = 1

        #タイマー開始時間に現在の時刻を代入（ミリ秒）
        setTime = blockNumber * blockSurvivalTime * 1000

        #出力
        display.scroll("start")

        #s = temperature()		#温度取得
        #startTime = running_time()	#稼働時間取得


### timerモード Bボタン押下
def ButtonCkick_B():
    global appStatus
    if appStatus == 1 :
        appStatus = 2
        display.scroll("stop")

    elif appStatus == 2 :
        appStatus = 1
        display.scroll("restart")

###　timerモード　A＋Bボタン押下
def ButtonCkick_AB():
    return