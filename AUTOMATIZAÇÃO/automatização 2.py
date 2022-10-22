import pyautogui
from time import sleep
from pynput.mouse import Button, Controller
# abrir area de trabalho
pyautogui.alert('O PYTON está rodando, Não mexa em nada até o programa avisar que terminou!')
#clicar no navegador chrome
pyautogui.press('win')
sleep(5)
pyautogui.write('chrome')
sleep(5)
pyautogui.press('tab')
sleep(5)
pyautogui.press('enter')
sleep(5)
pyautogui.press('ctrl+t')
sleep(5)
pyautogui.write('https://poloniex.com/wallet')
sleep(5)
pyautogui.press('enter')
sleep(10)



#pyautogui.press('enter')
pyautogui.alert('O código foi concluído, volte a usar o computador normalmente!')


print('TERMINADO')
