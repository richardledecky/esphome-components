#include "rc_switch_component.h"

namespace rc_switch_component {

void RCSwitchTransmitter::setup() {
  // inicializacia vysielaca
}

void RCSwitchTransmitter::loop() {
  // loop, ak treba
}

void RCSwitchTransmitter::send_code(uint32_t code) {
  // odoslanie RF kodu
  ESP_LOGD("rc_switch", "Sending code: %u", code);
}

void SendRCSwitchAction::play(int repetitions) {
  if (parent) {
    for (int i = 0; i < repetitions; i++) {
      parent->send_code(code);
    }
  }
}

}  // namespace rc_switch_component
