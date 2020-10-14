from microbit import *
import dispTime
import TwoLineNumber

###　変数初期化
appStatus = 0     #タイマー未動作
startTime = 0     #開始時間
operatingTime = 0 #稼動時間
elapsedTime = 0   #経過時間
blockNumber = 25
blockSurvivalTime = 30

###--------------------------------------
###　timerモード　Aボタン押下
def ButtonCkick_A():
    global appStatus
    global startTime
    global setTime
    if appStatus == 0 :
        appStatus = 1
        #タイマー開始時間に現在の時刻を代入（ミリ秒）
        #startTime = system_timer_current_time()
        setTime = blockNumber * blockSurvivalTime * 1000
        #出力
        display.scroll("start")
        s = temperature()
        #display.scroll(s)
        startTime = running_time()
        #display.scroll(startTime)

###　timerモード　Bボタン押下
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

###　タイマー処理
def Timer():
    sleep(1000)
    keikaTime = running_time() - startTime
    dispTime = int((setTime - keikaTime) / 1000 /30)
    return dispTime

###--------------------------------------
###　起動時処理
###　settingファイル読み込み




###　Timerモード開始
while True:
    if appStatus == 1 :
        sleep(1000)
        x = Timer()
        display.show(dispTime.BlockArrey[x])
        #display.show(TwoLineNumber.img(25))

    ### イベント登録
    if button_a.is_pressed() and button_b.is_pressed():
        break
    elif button_a.is_pressed():
        ButtonCkick_A()

    elif button_b.is_pressed():
        ButtonCkick_B()






###　
###　