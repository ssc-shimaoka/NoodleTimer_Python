from microbit import *
import ButtonEvent
import dispTime
import TwoLineNumber

###--------------------------------------
### 変数初期化
appStatus = 0     #タイマー未動作
startTime = 0     #開始時間
setTime = 0
operatingTime = 0 #稼動時間
elapsedTime = 0   #経過時間
blockNumber = 25
blockSurvivalTime = 30
updateInterval = 1000   #更新間隔（ミリ秒）

###--------------------------------------
### タイマー処理
def GetRemainingBlocks():
    #global startTime
    #global setTime
    #global updateInterval
    #global blockSurvivalTime

    #1秒間隔に調整
    sleep(updateInterval)

    keikaTime = running_time() - startTime
    dispTime = int((setTime - keikaTime) / updateInterval / blockSurvivalTime)
    return dispTime

###--------------------------------------
### 起動時処理
### settingファイル読み込み



###

while True:
    ### Timerモード(通常モード)処理

    #共通処理
    #残りブロック数取得
    blocks = GetRemainingBlocks()

    #タイマー未動作状態の場合
    if appStatus == 0 :
        #点灯LED表示
        display.show(dispTime.BlockArrey[blocks])

    #タイマー動作中状態の場合
    if appStatus == 1 :
        #点灯LED表示
        display.show(dispTime.BlockArrey[blocks] - 1)
        #display.show(TwoLineNumber.img(25))

        #点滅LED表示

    #タイマー一時停止状態の場合
    if appStatus == 2 :
        break

    # ボタンイベント登録
    if button_a.is_pressed() and button_b.is_pressed():
        break
    elif button_a.is_pressed():
        ButtonEvent.ButtonCkick_A(appStatus, blockNumber, blockSurvivalTime)
    elif button_b.is_pressed():
        ButtonEvent.ButtonCkick_B()