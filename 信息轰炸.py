from pynput.keyboard import Key, Controller as key_Controller
import time
time.sleep(5)
keyboard = key_Controller()
while True:
    # 这里输入轰炸内容
    keyboard.type("？？？")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # 这里输入两次时间间隔，单位为秒
    time.sleep(0.1)
