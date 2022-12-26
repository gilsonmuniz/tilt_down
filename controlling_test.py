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

sleep(2)

screenWidth, screenHeight = pyautogui.size()

configuracoes_button = pyautogui.locateCenterOnScreen('images/configuracoes_button.png')
pyautogui.moveTo(configuracoes_button) # "Configurações" button
pyautogui.click()

daq_digital_inputs_reference = pyautogui.locateCenterOnScreen('images/daq_digital_inputs_reference.png')
pyautogui.moveTo(daq_digital_inputs_reference.x + 150, daq_digital_inputs_reference.y + 30, 0.2) # Changing DAQ's name
pyautogui.click()
for _ in range(7): # Removing "line0:3"
    pyautogui.press('backspace')
pyautogui.write('Dev3')

daq_analog_inputs_reference = pyautogui.locateCenterOnScreen('images/daq_analog_inputs_reference.png')
pyautogui.moveTo(daq_analog_inputs_reference.x + 150, daq_analog_inputs_reference.y + 30, 0.2) # Changing DAQ's name
pyautogui.click()
for _ in range(5): # Removing "ai6:7"
    pyautogui.press('backspace')
pyautogui.write('Dev3')

run_button = pyautogui.locateCenterOnScreen('images/run_button.png')
pyautogui.moveTo(run_button) # "Run" button
pyautogui.click()

tilt_down_tab = pyautogui.locateCenterOnScreen('images/tilt_down_tab.png')
pyautogui.moveTo(tilt_down_tab) # "Tilt Down" tab
pyautogui.click()

# ---------------------------------- Align vertical Tilt Down axis

def press_plus_vertical_position():
    control_reference = pyautogui.locateCenterOnScreen('images/control_reference.png')
    pyautogui.moveTo(control_reference.x, control_reference.y + 45, 0.2)
    pyautogui.click(duration=0.2)

tilt_down_vertical_aligned = False
while tilt_down_vertical_aligned == False:
        if pyautogui.locateCenterOnScreen('images/vertical_1.3V.png') is not None: # Picture "Vertical: 1.3"
            tilt_down_vertical_aligned = True
        else:
            press_plus_vertical_position()
            tilt_down_vertical_aligned = False

tilt_down_button = pyautogui.locateCenterOnScreen('images/tilt_down_button.png')
pyautogui.click() # Saving Tilt Down position (1.9, 1.3)
