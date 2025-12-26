#  Simple Hackpad

A custom 4-key macro pad designed for productivity and built with the Seeed Studio XIAO RP2040. This project uses KMK Firmware (CircuitPython) to handle custom keymaps and RGB lighting effects.


### PCB Layout
![PCB Design](README-IMAGES/PCB.png)
This layout features optimized trace widths for power delivery to the LEDs.

### Schematic
![Schematic](README-IMAGES/schematic.png)
The circuit design utilizes a direct-pin connection, avoiding the complexity of a diode matrix for a small 4-key setup.

### 3D CAD View - Style 1
![3D CAD](README-IMAGES/CAD.png)

### 3D CAD View - Style 2
![3D CAD Alternative](README-IMAGES/3D%20CAD.png)

### 3D CAD View - Full Assembly
![Simple Hack pad V2](README-IMAGES/simple%20hack%20pad%20v2.png)
This view was critical for ensuring the USB-C port on the XIAO would be easily accessible through a case cutout.


### 3D PCB VIEW:
![PCB 3D](README-IMAGES/PCB%203D.png)
This is a 3D render generated within KiCad to preview the final manufactured board.

### 3D full hackpad 
 ![Simple Hack pad V2 full](README-IMAGES/simple%20hack%20pad%20v2%20full.png)
 It helped me visualize the spacing between the mechanical switches and the board edge.
 This is the master assembly model combining the PCB, switches, and the switch plate.



## Firmware & Features
The firmware is built using KMK. It includes:
- Custom Macros: Configured for KiCad shortcuts and media controls.
- RGB Screensaver:A rainbow animation that activates during idle time.
- CircuitPython: Easy to edit on the fly by just saving the `code.py` file.

## Repository Structure
- `firmware`: The `code.py` and configuration files for KMK.
- `hardware`: KiCad schematic and the `.step` 3D model.
- `README-IMAGES`: Visuals used in this documentation.


### Specifications BOM:

- 4x Cherry MX Switches
- 2x SK6812 MINI Leds
- 1x XIAO RP2040
- 4x Blank DSA Keycaps
- 4x M3x16 Bolt
- 4x M3 Heatset
