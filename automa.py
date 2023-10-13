import pyautogui
import time
from datetime import datetime

# Defina a hora em que deseja enviar a mensagem (formato 24 horas)
hora_agendada = "00:00"

while True:
    # Obtém a hora atual
    hora_atual = datetime.now().strftime("%H:%M")

    # Verifica se é hora de enviar a mensagem
    if hora_atual == hora_agendada:
        # Abra o WhatsApp Web no navegador (certifique-se de estar logado)
        pyautogui.hotkey("ctrl", "esc")
        pyautogui.write("WhatsApp", interval=0.2)
        pyautogui.press("enter")
        time.sleep(3)

        # Digite o nome do contato ou grupo
        pyautogui.write("th")
        pyautogui.press("down")
        pyautogui.press("enter")
        time.sleep(2)

        # Digite a mensagem
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        pyautogui.hotkey("win", "r")
        time.sleep(1)
        pyautogui.press("enter")
        pyautogui.write("shutdown /s /t 10")
        pyautogui.press("enter")
        break