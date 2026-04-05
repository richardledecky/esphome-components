import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_CODE

rc_switch_ns = cg.esphome_ns.namespace("rc_switch_component")
SendRCSwitchAction = rc_switch_ns.class_("SendRCSwitchAction", cg.Action)

CONF_GPIO = "gpio"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(SendRCSwitchAction),
        cv.Required(CONF_CODE): cv.uint32_t,
        cv.Optional(CONF_GPIO, default=23): cv.int_,
    }
)


@cg.register_action("rc_switch_component.send", SendRCSwitchAction, CONFIG_SCHEMA)
async def rc_switch_send_to_code(config, action_id, template_arg, args):
    var = cg.new_Pvariable(action_id, template_arg)
    cg.add(var.set_code(config[CONF_CODE]))
    cg.add(var.set_gpio(config[CONF_GPIO]))
    # pridáme C++ súbory a knižnicu
    cg.add_library("rc-switch", None)
    cg.add_source_file("rc_switch_component.cpp")
    cg.add_source_file("rc_switch_component.h")
    return var
