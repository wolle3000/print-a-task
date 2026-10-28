idf_component_register(
    SRCS "main.c"
    INCLUDE_DIRS "."
    REQUIRES sensor_presence ui_peripherals app_state_machine task_queue printer_escpos
)
