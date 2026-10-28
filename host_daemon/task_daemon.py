#!/usr/bin/env python3
"""
Host Daemon for the print-a-task terminal.
Responsibility: Communicates via UART/USB with the ESP32-P4 and triggers macOS actions.
"""

import time
import serial
import sys


class TaskDaemon:
    def __init__(self, port="/dev/cu.usbserial-mock", baudrate=115200, mock_mode=True):
        self.port = port
        self.baudrate = baudrate
        self.mock_mode = mock_mode
        self.is_running = True
        self.serial_conn = None

    def trigger_macos_dnd(self, enable: bool):
        """
        TODO (Upcoming): Enables or disables the 'Do Not Disturb' mode in macOS.
        """
        status = "ENABLED" if enable else "DISABLED"
        print(f"[macOS System] 'Do Not Disturb' mode has been {status}.")

    def connect(self):
        if self.mock_mode:
            print(f"[Daemon] Starting in MOCK MODE. Simulating ESP32-P4 on port {self.port}...")
            return True

        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"[Daemon] Successfully connected to {self.port}.")
            return True
        except serial.SerialException as e:
            print(f"[Error] Hardware not found: {e}")
            return False

    def listen(self):
        print("[Daemon] Listening for events from print-a-task terminal...")
        while self.is_running:
            if self.mock_mode:
                # Simulate incoming data from ESP32 every few seconds
                time.sleep(3)
                self.process_payload("EVENT:SESSION_START")
                time.sleep(5)
                self.process_payload("EVENT:SESSION_END")
            else:
                # Real hardware mode
                if self.serial_conn and self.serial_conn.in_waiting > 0:
                    try:
                        line = self.serial_conn.readline().decode("utf-8").strip()
                        if line:
                            self.process_payload(line)
                    except UnicodeDecodeError:
                        pass
                time.sleep(0.05)  # Prevent 100% CPU usage

    def process_payload(self, data: str):
        print(f"[UART Received] -> {data}")

        # Simple protocol parsing for the state machine
        if data == "EVENT:SESSION_START":
            self.trigger_macos_dnd(enable=True)
        elif data == "EVENT:SESSION_END":
            self.trigger_macos_dnd(enable=False)


if __name__ == "__main__":
    # Start daemon in mock mode until hardware is ready
    daemon = TaskDaemon(mock_mode=True)

    if daemon.connect():
        try:
            daemon.listen()
        except KeyboardInterrupt:
            print("\n[Daemon] Shutting down...")
            daemon.is_running = False
            sys.exit(0)
