#pragma once
#include "esphome.h"

namespace rc_switch_component {

class RCSwitchTransmitter : public Component {
 public:
  void setup() override;
  void loop() override;

  void send_code(uint32_t code);
};

class SendRCSwitchAction : public Action {
 public:
  RCSwitchTransmitter* parent;
  uint32_t code;

  void play(int repetitions) override;
};

}  // namespace rc_switch_component
