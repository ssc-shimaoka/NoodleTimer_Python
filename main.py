from microbit import *
import dispTime
import TwoLineNumber

###--------------------------------------
### 変数初期化
appStatus = 0     #タイマー未動作
startTime = 0     #開始時間
setTime = 0
operatingTime = 0 #稼動時間
elapsedTime = 0   #経過時間
blockNumber = 6
blockSurvivalTime = 30
updateInterval = 1000   #更新間隔（ミリ秒）

###--------------------------------------
### タイマー処理
def GetRemainingBlocks():
    keikaTime = running_time() - startTime
    dispTime = int((setTime - keikaTime) / updateInterval / blockSurvivalTime)
    return dispTime

###--------------------------------------
### 起動時処理
### settingファイル読み込み



###--------------------------------------
#ループ処理
while True:
    #ボタンA＋Bイベント
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.BUTTERFLY)#仮

    #ボタンAイベント
    elif button_a.is_pressed():
        #タイマー未動作状態
        if appStatus == 0 :
            #タイマー開始時間に現在の時刻を代入（ミリ秒）
            startTime = running_time()
            #タイマー指定時間 設定
            setTime = blockNumber * blockSurvivalTime * updateInterval
            #タイマー状態更新（未動作→動作中）
            appStatus = 1
            #出力
            display.scroll("start")

    #ボタンBイベント
    elif button_b.is_pressed():
        display.show(Image.BUTTERFLY)#仮


    ### Timerモード(通常モード)処理
    #1秒間隔に調整
    sleep(updateInterval)

    #タイマー未動作状態の場合
    if appStatus == 0 :
        #点灯LED表示
        #display.show(dispTime.BlockArrey[blocks])
        display.show(appStatus) #0

    #タイマー動作中状態の場合
    if appStatus == 1 :
        #残りブロック数取得
        blocks = GetRemainingBlocks()

        #ブロックが0個になった場合
        if blocks == 0 :
            #満了演出
            display.show(Image.HAPPY)

            #状態初期化
            appStatus = 0

        #ブロックが残っている場合
        else :
            #点灯LED表示
            display.show(dispTime.BlockArrey[blocks+1])

            '''
            #点滅LED表示
            #display.show(blocks)
            #display.set_pixel(dispTime.LcdArrey[blocks])
            '''

    #タイマー一時停止状態の場合
    if appStatus == 2 :
        break

