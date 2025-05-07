from machine import Pin
import time

# ロータリーエンコーダーのA相とB相に接続するピン番号を指定
# ご使用のボードと配線に合わせてピン番号を変更してください
PIN_A = 2 # 例: GPIO16
PIN_B = 3 # 例: GPIO17

# カウンターの初期値
counter = 0

msg = ""

# 前回のA相とB相の状態を保存する変数
# 割り込み関数内で使用するため、グローバル変数とするか、クラス化が必要
last_pin_a_state = 0
last_pin_b_state = 0

# ピンの設定
# Pin.IN: 入力モード
# Pin.PULL_UP: 内部プルアップ抵抗を有効にする（多くのエンコーダーで推奨）
pin_a = Pin(PIN_A, Pin.IN, Pin.PULL_UP)
pin_b = Pin(PIN_B, Pin.IN, Pin.PULL_UP)

# 初期の状態を読み込んでおく
last_pin_a_state = pin_a.value()
last_pin_b_state = pin_b.value()

# 割り込みハンドラ関数
# ピンの状態変化時に呼び出される
def encoder_callback(pin):
    global counter, last_pin_a_state, last_pin_b_state

    # 現在のA相とB相の状態を取得
    current_pin_a_state = pin_a.value()
    current_pin_b_state = pin_b.value()

    # 前回と同じ状態の場合は処理しない (チャタリング対策にもなる)
    # if current_pin_a_state == last_pin_a_state and current_pin_b_state == last_pin_b_state:
    #     return

    # AB相の状態遷移を基に回転方向を判定
    # 多くのロータリーエンコーダーは、1ノッチでAB相が4回状態遷移します
    # (例: 00 -> 01 -> 11 -> 10 -> 00)
    # このコードは、A相またはB相の状態が変化したときに呼ばれ、
    # 現在のAB相の状態と前回のAB相の状態の組み合わせを見て判定します。

    # 簡易的な判定ロジック例（A相の変化で割り込みがかかる前提の場合）
    # A相の立ち上がりで割り込みが発生したとき：
    #   A=1, B=0 なら時計回り
    #   A=1, B=1 なら反時計回り
    # A相の立ち下がりで割り込みが発生したとき：
    #   A=0, B=1 なら時計回り
    #   A=0, B=0 なら反時計回り

    # より一般的な4倍速エンコーディング対応ロジック（ABどちらかの変化で割り込み）
    # 以下の判定ロジックは、ABどちらかのピンに割り込みを設定した場合に有効です。
    # 多くのエンコーダーで安定した検出が可能です。

    # AB相の状態を2ビットの数値として表現
    current_state = (current_pin_a_state << 1) | current_pin_b_state
    last_state = (last_pin_a_state << 1) | last_pin_b_state

    # 状態遷移テーブル (last_state -> current_state)
    # 正常な回転での遷移と、それに対応するカウンターの変化量
    # 00 -> 01 (+1)  | 00 -> 10 (-1)
    # 01 -> 11 (+1)  | 01 -> 00 (-1)
    # 11 -> 10 (+1)  | 11 -> 01 (-1)
    # 10 -> 00 (+1)  | 10 -> 11 (-1)

    # 状態遷移をチェックしてカウンターを増減
    if last_state == 0b00 and current_state == 0b01:
        counter += 1
        msg = 'F'
    elif last_state == 0b01 and current_state == 0b11:
        counter += 1
        msg = 'F'
    elif last_state == 0b11 and current_state == 0b10:
        counter += 1
        msg = 'F'
    elif last_state == 0b10 and current_state == 0b00:
        counter += 1
        msg = 'F'
    elif last_state == 0b00 and current_state == 0b10:
        counter -= 1
        msg = 'B'
    elif last_state == 0b10 and current_state == 0b11:
        counter -= 1
        msg = 'B'
    elif last_state == 0b11 and current_state == 0b01:
        counter -= 1
        msg = 'B'
    elif last_state == 0b01 and current_state == 0b00:
        counter -= 1
        msg = 'B'
    else:
        msg = "X"
    # その他の遷移は無効またはチャタリングとして無視される場合が多い

    # 現在の状態を次の割り込みのために保存
    last_pin_a_state = current_pin_a_state
    last_pin_b_state = current_pin_b_state

    # デバッグ用にカウンター値を表示（リアルタイム性は低い）
    # print("Counter:", counter)


# ピンに割り込みを設定
# Pin.IRQ_RISING: 立ち上がりエッジで割り込み
# Pin.IRQ_FALLING: 立ち下がりエッジで割り込み
# irq=encoder_callback: 割り込み発生時に呼び出される関数を指定
# hard=True: ハードウェア割り込み (高速だが制約あり、通常はTrueでOK)

# A相とB相のどちらかの状態が変化したときに割り込みを発生させる
pin_a.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=encoder_callback, hard=True)
pin_b.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=encoder_callback, hard=True)


# メインループ
# ここでは定期的にカウンター値を表示するだけです
# 割り込みハンドラがバックグラウンドでカウンターを更新します
print("Rotary Encoder Test. Rotate the encoder.")
print("Press Ctrl+C to exit.")

while True:
    # 割り込みによって更新されたカウンターの値を表示
    # 割り込みハンドラ内で直接printすると問題が起きる可能性があるため、
    # メインループで表示するのが安全です。
    #print("Current Counter:", counter)
    print(msg)
    # 適度に待機
    time.sleep(0.01) # 100msごとに表示