"""
-----------------------------------+
Metagal - Laboratório de Qualidade |
Controlador do teste de Tilt Down  |
-----------------------------------+
"""

# To get the cursor coordinates: http://www.brenz.net/snippets/xy.asp#:~:text=Tracking%20the%20Cursor%20X%2FY%20Coordinates&text=On%20this%20page%2C%20press%20and,with%20the%20%27z%27%20accesskey.
# (X, +70Y)

import pyautogui
from time import sleep

sleep(3)

# ===============================================| SetUp |============================================== #

sample_name = pyautogui.prompt('Nome da amostra:')

configuracoes_button = pyautogui.locateCenterOnScreen('images/configuracoes_button.png')
pyautogui.moveTo(configuracoes_button) # "Configurações" button
pyautogui.click()

daq_digital_inputs_reference = pyautogui.locateCenterOnScreen('images/daq_digital_inputs_reference.png')
pyautogui.moveTo(daq_digital_inputs_reference.x + 150, daq_digital_inputs_reference.y + 30, 0.2) # Changing DAQ's name
pyautogui.click()
# for _ in range(7): # Removing "line0:3"
#     pyautogui.press('backspace')
# pyautogui.write('Dev3')

daq_analog_inputs_reference = pyautogui.locateCenterOnScreen('images/daq_analog_inputs_reference.png')
pyautogui.moveTo(daq_analog_inputs_reference.x + 150, daq_analog_inputs_reference.y + 30, 0.2) # Changing DAQ's name
pyautogui.click()
# for _ in range(5): # Removing "ai6:7"
#     pyautogui.press('backspace')
# pyautogui.write('Dev3')

run_button = pyautogui.locateCenterOnScreen('images/run_button.png')
pyautogui.moveTo(run_button) # "Run" button
pyautogui.click()

full_screen = pyautogui.locateCenterOnScreen('images/full_screen.png')
pyautogui.moveTo(full_screen)
pyautogui.click()

tilt_down_tab = pyautogui.locateCenterOnScreen('images/tilt_down_tab.png')
pyautogui.moveTo(tilt_down_tab) # "Tilt Down" tab
pyautogui.click()

# =================================| Tilt Down and Drive positions |=================================== #

def press_plus_horizontal_position():
    """ Press plus horizontal position button """
    control_reference = pyautogui.locateCenterOnScreen('images/control_reference.png')
    pyautogui.moveTo(control_reference.x + 65, control_reference.y + 105, 0.2)
    pyautogui.click(duration=0.2)

def press_plus_vertical_position():
    """ Press plus vertical position button """
    control_reference = pyautogui.locateCenterOnScreen('images/control_reference.png')
    pyautogui.moveTo(control_reference.x, control_reference.y + 45, 0.2)
    pyautogui.click(duration=0.2)

# ---------------------------------- Align horizontal Tilt Down axis

tilt_down_horizontal_aligned = False
# while tilt_down_horizontal_aligned == False:
#         if pyautogui.locateCenterOnScreen('images/horizontal_1.9V.png') is not None: # Picture "Horizontal: 1.9"
#             tilt_down_horizontal_aligned = True
#         else:
#             press_plus_horizontal_position()
#             tilt_down_horizontal_aligned = False

# ---------------------------------- Align vertical Tilt Down axis

tilt_down_vertical_aligned = False
# while tilt_down_vertical_aligned == False:
#         if pyautogui.locateCenterOnScreen('images/vertical_1.3V.png') is not None: # Picture "Vertical: 1.3"
#             tilt_down_vertical_aligned = True
#         else:
#             press_plus_vertical_position()
#             tilt_down_vertical_aligned = False

# tilt_down_button = pyautogui.locateCenterOnScreen('images/tilt_down_button.png')
pyautogui.click() # Saving Tilt Down position (1.9, 1.3)

# ---------------------------------- Align horizontal Drive axis

drive_horizontal_aligned = False
# while drive_horizontal_aligned == False:
#         if pyautogui.locateCenterOnScreen('images/horizontal_3.4V.png') is not None: # Picture "Horizontal: 3.4"
#             drive_horizontal_aligned = True
#         else:
#             press_plus_horizontal_position()
#             drive_horizontal_aligned = False

# ---------------------------------- Align vertical Drive axis

drive_vertical_aligned = False
# while drive_vertical_aligned == False:
#         if pyautogui.locateCenterOnScreen('images/vertical_3.4V.png') is not None: # Picture "Vertical: 3.4"
#             drive_vertical_aligned = True
#         else:
#             press_plus_horizontal_position()
#             drive_vertical_aligned = False

tilt_down_button = pyautogui.locateCenterOnScreen('images/drive_button.png')
pyautogui.click() # Saving Drive position (3.4, 3.4)

# ==========================================| 3 Cycles Test |=========================================== #

# ---------------------------------- Disabling AutoScaleX

grafico_de_posicao_reference = pyautogui.locateCenterOnScreen('images/grafico_de_posicao_reference.png')
pyautogui.moveTo(grafico_de_posicao_reference.x, grafico_de_posicao_reference.y + 50)
pyautogui.rightClick()
auto_scale_x = pyautogui.locateCenterOnScreen('images/auto_scale_x.png')
pyautogui.moveTo(auto_scale_x)
pyautogui.click()

# ---------------------------------- Adjusting graphic time axis

pyautogui.moveTo(grafico_de_posicao_reference.x - 100, grafico_de_posicao_reference.y + 250)
pyautogui.doubleClick()
pyautogui.press('delete')

from datetime import datetime, timedelta

now = datetime.now()
p_1min = now + timedelta(minutes=1)

pyautogui.write(now.strftime('%H:%M:%S'))

pyautogui.moveTo(grafico_de_posicao_reference.x + 110, grafico_de_posicao_reference.y + 250)
pyautogui.doubleClick()
pyautogui.press('delete')


pyautogui.write(p_1min.strftime('%H:%M:%S'))

pyautogui.press('enter')

# ---------------------------------- Doing the 3 clycles test

for _ in range(3):
    d_button = pyautogui.locateCenterOnScreen('images/d_button.png')
    pyautogui.moveTo(d_button)
    pyautogui.click()
    r_button = pyautogui.locateCenterOnScreen('images/r_button.png')
    pyautogui.moveTo(r_button)
    pyautogui.click()

sleep(50) # Time to wait complete signal appears on the graph
pyautogui.screenshot('graphs/3_cycles/{}.png'.format(sample_name))

# ==========================================| 10 Cycles Test |========================================== #

ciclagem_tab = pyautogui.locateCenterOnScreen('images/ciclagem_tab.png')
pyautogui.moveTo(ciclagem_tab)
pyautogui.click()

# ---------------------------------- Changing the number of cycles

metagal_logo = pyautogui.locateCenterOnScreen('images/metagal_logo.png')
pyautogui.moveTo(metagal_logo.x + 40, metagal_logo.y + 80)
pyautogui.doubleClick()
pyautogui.press('delete')
pyautogui.write('10')
pyautogui.press('enter')

# ---------------------------------- Disabling AutoScaleX

pyautogui.moveTo(metagal_logo.x + 300, metagal_logo.y + 300)
pyautogui.rightClick()
auto_scale_x = pyautogui.locateCenterOnScreen('images/auto_scale_x.png')
pyautogui.moveTo(auto_scale_x)
pyautogui.click()

# ---------------------------------- Adjusting graphic time axis

reference_0V = pyautogui.locateCenterOnScreen('images/0v.png')
pyautogui.moveTo(reference_0V.x + 10, reference_0V.y + 5)
pyautogui.doubleClick()
pyautogui.press('delete')

from datetime import datetime, timedelta

now = datetime.now()
p_5min = now + timedelta(minutes=5)

pyautogui.write(now.strftime('%H:%M:%S'))

pyautogui.moveTo(reference_0V.x + 200, reference_0V.y + 5)
pyautogui.doubleClick()
pyautogui.press('delete')


pyautogui.write(p_5min.strftime('%H:%M:%S'))

pyautogui.press('enter')

# ---------------------------------- Starting the test

comecar_button = pyautogui.locateCenterOnScreen('images/comecar_button.png')
pyautogui.moveTo(comecar_button)
pyautogui.click()

sleep(5) # Time to wait complete signal appears on the graph (300s)
pyautogui.screenshot('graphs/10_cycles/{}.png'.format(sample_name))

# ============================================| End of Test |=========================================== #

pyautogui.confirm('Teste da {} finalizado.'.format(sample_name))
