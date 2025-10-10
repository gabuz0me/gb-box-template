# Game Boy (Color/Advance) Templates

Here you can find templates for Game Boy boxes and inlay insert trays.

---

## Already exported templates

### Inlay Insert Tray

|   | GB/GBC | GBA |
|--:|:------:|:---:|
| SVG | ![GB](./Exported/inlay%20insert%20tray/side/tray_side_gb.svg) | ![GB](./Exported/inlay%20insert%20tray/side/tray_side_gba.svg) |
| PDF | [Download](./Exported/inlay%20insert%20tray/side/tray_side_gb.pdf) | [Download](./Exported/inlay%20insert%20tray/side/tray_side_gba.pdf) |

## What are these files?

They are CAD files I made with [FreeCAD](https://www.freecad.org/), describing the patterns for game boxes and inlay insert trays. Being CAD files, you can adjust the dimensions dynamically, from regular box or cartridge sizes to custom ones without any trouble. You can then export the drawing to SVG or PDF to print it. For simplicity, I've already created SVG and PDF versions for GB/GBC/GBA standard dimensions.

| ![Updating dimensions dynamically](./Images/cad_constraints_update.gif) |
|:-:|
| Updating dimensions dynamically |

## What are the dimensions of boxes and cartridges?

For the boxes, I measured one and found 125x125x25 mm.

For the cartridges, I used [ConsoleMods.org](https://consolemods.org/wiki/Dimensions_for_Game_Cartridges) and found:
- GB: 65x57x8 mm
- GBA: 35x60x9 mm

I removed 1 mm for clearance for the cartridge space in the inlay insert tray, and set the tray dimensions to 121x121x22 mm so it fits well inside a box.