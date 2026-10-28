# print-a-task

A physical anti-procrastination terminal built on the **ESP32-P4 (RISC-V)** and macOS. Combines a presence radar, RFID time tracking, and a C/FreeRTOS architecture to print current tasks on a thermal receipt printer.

## Directory Structure
- `firmware/`: ESP-IDF (C / FreeRTOS / Rust) project for the ESP32-P4.
- `host_daemon/`: Python background service for macOS (serial communication & Focus mode control).
- `docs/`: Hardware pinout (`pinout.md`) and system architecture documentation.

## Hardware Debugging Checklist (Before blaming the code)
1. **Power & Ground:** Verify 3.3V / 5V levels with a multimeter and ensure common GND.
2. **Clock & Peripherals:** Ensure peripheral drivers are initialized (`ESP_ERROR_CHECK`).
3. **Pin Multiplexing:** Verify pin assignments in `docs/pinout.md` and check RX/TX crossover.
