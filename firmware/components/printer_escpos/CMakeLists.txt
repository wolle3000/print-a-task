idf_component_register(
    SRCS "printer_escpos.c"
    INCLUDE_DIRS "include"
    REQUIRES driver esp_timer
)
