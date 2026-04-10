#pragma once

#include "esphome/core/component.h"
#include "esphome/core/automation.h"
#include <RCSwitch.h>

namespace esphome {
namespace rc_switch_component {

class RCSwitchComponent : public Component {
 public:
  void set_gpio(int gpio) { gpio_ = gpio; }

  void setup() override {
    sw_.enableTransmit(gpio_);
    sw_.setProtocol(1);
    sw_.setPulseLength(350);
    sw_.setRepeatTransmit(10);
  }

  void send(uint32_t code, uint8_t length) {
    sw_.send(code, length);
  }

 protected:
  RCSwitch sw_;
  int gpio_{23};
};

// ================= ACTION =================

template<typename... Ts>
class SendRCSwitchAction : public Action<Ts...> {
 public:
  void set_parent(RCSwitchComponent *parent) { parent_ = parent; }
  void set_code(uint32_t code) { code_ = code; }
  void set_gpio(int gpio) { gpio_ = gpio; }

  void play(Ts... x) override {
    if (parent_ == nullptr)
      return;

    parent_->send(code_, 24);
  }

 protected:
  RCSwitchComponent *parent_{nullptr};
  uint32_t code_{0};
  int gpio_{23};
};

}  // namespace rc_switch_component
}  // namespace esphome
