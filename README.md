# simple-hackpad
A custom 4-key productivity macro pad powered by the Seeed Studio XIAO RP2040 and KMK Firmware. Features dedicated shortcuts for KiCad, Spotify, and system tools, complete with an idle RGB rainbow screensaver.
# 4-Key Macro Pad (XIAO RP2040)

A compact, 4-button macro pad featuring RGB "screensaver" lighting, built using the Seeed Studio XIAO RP2040 and KMK firmware.

## Features
- **Button 1:** Opens Default Web Browser.
- **Button 2:** Launches KiCad.
- **Button 3:** Launches Spotify.
- **Button 4:** Opens Windows Task Manager.
- **RGB Lighting:** Continuous "Rainbow" cycle (Screensaver mode).

## Hardware
- **MCU:** [Seeed Studio XIAO RP2040](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html)
- **Switches:** 4x Mechanical Switches (connected to GP26, GP27, GP28, GP29).
- **LEDs:** 4x SK6812 Mini RGB LEDs (chained on GP0).

## Installation
1. Install [CircuitPython](https://circuitpython.org/board/seeeduino_xiao_rp2040/) onto your XIAO RP2040.
2. Download the [KMK Library](https://github.com/KMKfw/kmk_firmware) and copy the `kmk` folder onto the `CIRCUITPY` drive.
3. Copy the `code.py` from the `/firmware` folder of this repo onto the root of the `CIRCUITPY` drive.

## Schematic
The switches are wired to pull the pins to Ground (GND). The RGB data line starts at GP0.

### Specifications

BOM: 
- 4x Cherry MX Switches
- 4x SK6812 MINI Leds
- 1x XIAO RP2040
- 4x Blank DSA Keycaps
- 4x M3x16 Bolt
- 4x M3 Heatset
- 1x soldering iron
