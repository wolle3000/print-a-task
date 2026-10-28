# System Architecture

## Overview
- **MCU:** Waveshare ESP32-P4 (400 MHz Dual-Core RISC-V + 40 MHz LP Core + ESP32-C6 Co-Processor)
- **Host:** macOS (Apple Silicon M1) running Python daemon
- **Sensors & Peripherals:**
  - HLK-LD2410C 24GHz mmWave Presence Radar (GPIO + UART)
  - HC-SR04 Ultrasonic Distance Sensor (GPIO / Timer)
  - 16x2 Character LCD (I2C)
  - RC522 RFID Reader (SPI)
  - 58mm ESC/POS Thermal Receipt Printer (USB Host / UART)
