#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"
#include "esp_err.h"

// Custom modular headers
#include "sensor_presence.h"
#include "ui_peripherals.h"
#include "app_state_machine.h"
#include "task_queue.h"
#include "printer_escpos.h"

static const char *TAG = "MAIN_APP";

void app_main(void) {
    ESP_LOGI(TAG, "print-a-task firmware booting on ESP32-P4 (RISC-V)...");

    // TODO (Milestone 1): Call sensor_presence_init() wrapped in ESP_ERROR_CHECK()

    while (1) {
        // TODO (Milestone 1): Poll sensor state or handle events
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
