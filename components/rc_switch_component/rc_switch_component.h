#pragma once
#include "esphome.h"

namespace rc_switch_component {

// jednoduchý RCSwitch transmitér
class RCSwitchTransmitter : public Component {
 public:
  void setup() override {
    // inicializácia, napríklad pin nastavíš neskôr cez lambda
    ESP_LOGD("rc_switch", "RCSwitchTransmitter setup done");
  }

  void send(uint32_t code, uint8_t length) {
    ESP_LOGD("rc_switch", "Sending code: %u with length: %u", code, length);
    // sem vlož skutočný kód pre RC vysielač
  }
};

// akcia pre script
class SendRCSwitchAction : public Action {
 public:
  RCSwitchTransmitter *parent;
  uint32_t code;

  void play(uint8_t repeat = 1) {
    if (!parent) {
      ESP_LOGW("rc_switch", "Parent transmitter not set!");
      return;
    }
    for (uint8_t i = 0; i < repeat; i++) {
      parent->send(code, 24);  // predpokladáme 24-bit kód
    }
  }
};

}  // namespace rc_switch_component
