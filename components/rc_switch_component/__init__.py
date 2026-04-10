import logging
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID
from esphome import automation

_LOGGER = logging.getLogger(__name__)

CODEOWNERS = ["@richardledecky"]
DEPENDENCIES = ["rc_switch_component"]

rc_switch_ns = cg.esphome_ns.namespace("rc_switch_component")

RCSwitchComponent = rc_switch_ns.class_("RCSwitchComponent", cg.Component)
SendRCSwitchAction = rc_switch_ns.class_("SendRCSwitchAction", automation.Action)

CONF_CODE = "code"
CONF_GPIO = "gpio"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(RCSwitchComponent),
    cv.Optional(CONF_GPIO, default=23): cv.int_,
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_gpio(config[CONF_GPIO]))
    await cg.register_component(var, config)

# ========== ACTION ==========

RC_SWITCH_SEND_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.use_id(RCSwitchComponent),
    cv.Required(CONF_CODE): cv.positive_int,
})

@automation.register_action(
    "rc_switch_component.send",
    SendRCSwitchAction,
    RC_SWITCH_SEND_SCHEMA
)
async def rc_switch_send_to_code(config, action_id, template_arg, args):

    var = cg.new_Pvariable(action_id, template_arg)

    parent = await cg.get_variable(config[CONF_ID])

    cg.add(var.set_parent(parent))
    cg.add(var.set_code(config[CONF_CODE]))
    cg.add(var.set_gpio(0))

    return var
