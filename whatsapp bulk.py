import webbrowser
from time import sleep
import pyautogui
import time

def SendWhatsapp(phone_no, message=''):
    def locateimg(img):
        send = None
        while not send:
            try:
                send = pyautogui.locateOnScreen(img)
            except:
                sleep(0.01)
        send=pyautogui.locateOnScreen(img)
        pyautogui.click(send)
        
    if message:
        webbrowser.open(f'https://web.whatsapp.com/send/?phone={phone_no}&text=Using+whatsapp+automation%21%0ADo+not+reply+back...&type=phone_number&app_absent=1')
        locateimg('OneDrive/Desktop/wh/sendphoto.PNG')
        pyautogui.hotkey('ctrl', 'w')
        
        locateimg('OneDrive/Desktop/wh/leave_btn.PNG')
        

start = time.time()
num = ['XXYYYYYYYYYY']
for n in num:SendWhatsapp(phone_no=n, message='Using whatsapp automation! Do not reply back...')
print(f'executed in: {time.time()-start}s')

#threading all - leave button , sendbutton will be good