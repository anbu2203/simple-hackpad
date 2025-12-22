# You import all the IOs of your board 
import board 

# These are imports from the kmk library 
from kmk.kmk_keyboard import KMKKeyboard 
from kmk.scanners.keypad import KeysScanner 
from kmk.keys import KC 
from kmk.modules.macros import Press, Release, Tap, Macros
# Added for RGB support and Animations
from kmk.extensions.RGB import RGB, AnimationModes

# This is the main instance of your keyboard 
keyboard = KMKKeyboard() 

# Add the macro extension 
macros = Macros() 
keyboard.modules.append(macros) 

# Add the RGB extension with "Screensaver" animation
# Verified: GP0 is the data pin for your SK6812 LEDs
rgb = RGB(
    pixel_pin=board.GP0, 
    num_pixels=4, 
    val_default=150,                       # Brightness (0-255)
    animation_mode=AnimationModes.RAINBOW, # "Screensaver" effect
    animation_speed=1,                     # Cycle speed
)
keyboard.extensions.append(rgb)

# Define your pins here! 
# Verified: Matches your schematic (SW1=GP26 ... SW4=GP29)
PINS = [board.GP26, board.GP27, board.GP28, board.GP29] 

# Tell kmk we are not using a key matrix 
# Verified: value_when_pressed=False is correct for pins wired to GND
keyboard.matrix = KeysScanner( 
    pins=PINS, 
    value_when_pressed=False, 
) 

# Here you define the buttons corresponding to the pins 
keyboard.keymap = [ 
    [
        # 1. Open Browser (Win+R -> Type URL -> Enter)
        KC.MACRO(Press(KC.LWIN), Tap(KC.R), Release(KC.LWIN), "https://google.com", Tap(KC.ENTER)), 
        
        # 2. Open KiCad (Win -> Type "kicad" -> Enter)
        KC.MACRO(Tap(KC.LWIN), "kicad", Tap(KC.ENTER)), 
        
        # 3. Open Spotify (Win -> Type "spotify" -> Enter)
        KC.MACRO(Tap(KC.LWIN), "spotify", Tap(KC.ENTER)), 
        
        # 4. Open Task Manager (Ctrl+Shift+Esc shortcut)
        KC.LCTRL(KC.LSHIFT(KC.ESC)),
    ] 
] 

# Start kmk! 
if __name__ == '__main__': 
    keyboard.go()