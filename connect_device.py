import pyautogui
import time
# import gTTS

def open_windows_start_menu():
    try:
        # Add a delay to give time to switch to the desktop or Start menu
        time.sleep(1)

        # Simulate pressing the Win key
        pyautogui.hotkey("winleft")

        print("Windows Start menu opened")

    except Exception as e:
        print(f"Error: {str(e)}")

def open_whatsapp_and_type_message():
    try:
        # Wait for the Start menu to open

        pyautogui.write('WhatsApp')
        time.sleep(1)

        # Press Enter to open WhatsApp
        pyautogui.press('enter')
        time.sleep(1)  # Adjust this delay based on your system's speed

        # Type your WhatsApp message
        pyautogui.write('ckb')
        pyautogui.press('tab')

        pyautogui.press('enter')
        time.sleep(1)  # Adjust this delay based on your system's speed
        pyautogui.write('patrik')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl','n')
        time.sleep(1)
        pyautogui.write('prasadkokrepk')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('fuck pk')
        pyautogui.press('enter')


        print("WhatsApp opened and message typed")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    open_windows_start_menu()
    open_whatsapp_and_type_message()
