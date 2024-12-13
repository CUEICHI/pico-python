import machine
import time
from machine import PWM

# GP28をPWMとして使います
pwm  = PWM(machine.Pin(3, machine.Pin.OUT))

# サーボが動作可能な範囲です
ANGLE_RANGE = 180
# サーボに指定するPWMの時間の範囲です
TIME_RANGE  = 1.9
# サーボに指定できる最小の時間です
MIN_TIME    = 0.5
# サーボのPWMの周期時間です
CYCLE_TIME  = 20.0

# 
#  角度⇒PWM信号に変換する関数です
#
def moveServo(pwm, angle ):

    # 入力角度のチェックです。±90以外はエラーにします
    if  angle < -90  or angle > 90 :
        return False

    # 指定角度を、0～180の表現に変えます
    angle = angle + 90

    # 指定角度を、全体(180度)中の割合に変換します
    percent =  angle  / ANGLE_RANGE

    # 割合を時間の範囲に適応して、指定角度を動かす時間を計算します
    addTime = TIME_RANGE * percent

    # 時間範囲は0.5から始まるので0.5に指定角度の時間を足します
    time = MIN_TIME + addTime

    # 指定角度の時間を、20msecの周期中の割合(%)に変換します
    ratio = time / CYCLE_TIME
    
    # 16bit(0~65535)の値(整数)に変換します。
    ratio = (int)(65535 *  ratio)
    
    # 動作実行します
    pwm.duty_u16(ratio)

    return True

#
#  メイン処理
#

#周期を1秒間に50回(50Hz)に設定します
pwm.freq(50)

# -90度、0度,90度に3回動かします。
for i in range(3):

    # -90度
    moveServo(pwm,-90 )
    print("-90")
    time.sleep(2)
    
    # 0度
    moveServo(pwm, 0)
    print("0")
    time.sleep(2)

    # 90度
    moveServo(pwm, 90)
    print("90")
    time.sleep(2)
        