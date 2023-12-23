from pynput.keyboard import Key, Controller as key_Controller
import time
print("请勿将本程序用于非法用途")
time.sleep(1)
print("5 秒后开始轰炸")
time.sleep(5)
keyboard = key_Controller()
while True:
    # 这里输入轰炸内容
    keyboard.type("？？？")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # 这里输入两次时间间隔，单位为秒
    time.sleep(0.1)
