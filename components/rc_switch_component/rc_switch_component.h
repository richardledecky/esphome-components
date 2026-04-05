#pragma once

#include "esphome/core/automation.h"
#include "esphome/core/component.h"
#include "RCSwitch.h"

namespace esphome {
namespace rc_switch_component {

class SendRCSwitchAction : public esphome::Action<> {
 public:
  void set_code(uint32_t code) { code_ = code; }
  void set_gpio(int gpio) { gpio_ = gpio; }

  template<typename... Ts> void play(Ts... x) {
    RCSwitch sw;
    sw.enableTransmit(gpio_);
    sw.send(code_, 24);
  }

 protected:
  uint32_t code_{0};
  int gpio_{23};
};

}  // namespace rc_switch_component
}  // namespace esphome
