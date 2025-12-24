# ⌨️ Simple Hackpad

A custom 4-key macro pad designed for productivity and built with the **Seeed Studio XIAO RP2040**. This project uses **KMK Firmware** (CircuitPython) to handle custom keymaps and RGB lighting effects.

## 🛠️ Hardware
- **Controller:** Seeed Studio XIAO RP2040
- **Switches:** 4x Mechanical switches
- **Lighting:** SK6812 / WS2812B RGB LEDs
- **Design Tool:** KiCad 8.0

## 📸 Design Preview
Below are the design files for the PCB and the 3D models:

### PCB Layout
![PCB Design](README-IMAGES/PCB.png)

### Schematic
![Schematic](README-IMAGES/schematic.png)

### 3D CAD View - Style 1
![3D CAD](README-IMAGES/CAD.png)

### 3D CAD View - Style 2
![3D CAD Alternative](README-IMAGES/3D%20CAD.png)

### 3D CAD View - Full Assembly
![Simple Hackpad V2](README-IMAGES/simple%20hackpad%20v2.png)

## 🏗️ Mechanical Source Files
- **[3D Step File](hardware/simple%20hack%20pad%20v2.step):** Full 3D model of the Hackpad.
- **[Plate DXF](plate-2025-12-15T15_56_35.892Z.dxf):** Laser-cut profile for the switch plate.

## 💻 Firmware & Features
The firmware is built using **KMK**. It includes:
- **Custom Macros:** Configured for KiCad shortcuts and media controls.
- **RGB Screensaver:** A rainbow animation that activates during idle time.
- **CircuitPython:** Easy to edit on the fly by just saving the `code.py` file.

## 📁 Repository Structure
- `/firmware`: The `code.py` and configuration files for KMK.
- `/hardware`: KiCad schematic and the `.step` 3D model.
- `/README-IMAGES`: Visuals used in this documentation.

## 🚀 About the Project
This project was built as part of the **Hack Club Blueprint** program. It helped me learn the end-to-end process of hardware design, from schematic entry to firmware implementation.
