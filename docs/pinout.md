# Hardware Pinout (Waveshare ESP32-P4)

> **IMPORTANT:** Document every GPIO pin assignment here before wiring components on the breadboard!

| Component | Signal | ESP32-P4 GPIO | Bus / Type | Voltage | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Status LED** | Anode (+) | `TODO` | GPIO Out | 3.3V | Use 220 Ohm series resistor |
| **LD2410C Radar** | OUT | `TODO` | GPIO In | 3.3V logic | Sensor VCC requires 5V! |
| **LD2410C Radar** | TX / RX | `TODO` | UART | 3.3V logic | Milestone 1c |
| **HC-SR04 Ultrasonic**| TRIG / ECHO | `TODO` | GPIO | Warning: 5V! | ECHO pin requires voltage divider to 3.3V! |
| **LCD 16x2 Display** | SDA / SCL | `TODO` | I2C | 5V / 3.3V | Milestone 2 |
| **RC522 RFID** | MOSI/MISO/SCK/CS | `TODO` | SPI | 3.3V | **NEVER connect VCC to 5V!** |
