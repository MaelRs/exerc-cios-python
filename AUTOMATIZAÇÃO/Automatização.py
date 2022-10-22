import pyautogui
from time import sleep
from pynput import mouse

pyautogui.alert('O PYTON está rodando, Não mexa em nada até o programa avisar que terminou!')
#clicar no navegador chrome
pyautogui.press('win')
sleep(5)
pyautogui.write('chrome')
sleep(5)
pyautogui.press('enter')
sleep(120)
pyautogui.write('youtube.com.br')
sleep(5)
pyautogui.press('enter')
sleep(10)
pyautogui.press('tab')
sleep(2)
pyautogui.press('tab')
sleep(2)
pyautogui.press('tab')
sleep(2)
pyautogui.press('tab')
sleep(2)
#pyautogui.press('tab')
pyautogui.write('third day')
sleep(1)
pyautogui.press('enter')
pynput.mouse.position(309,300)
pynput.mouse.press(button,left,1)
pyautogui.alert('O código foi concluído, volte a usar o computador normalmente!')


print('TERMINADO')

#
#
#
