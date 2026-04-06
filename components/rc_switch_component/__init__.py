import logging
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

_LOGGER = logging.getLogger(__name__)

CODEOWNERS = ["@richardledecky"]
DEPENDENCIES = []

rc_switch_ns = cg.esphome_ns.namespace("rc_switch_component")

SendRCSwitchAction = rc_switch_ns.class_(
    "SendRCSwitchAction", cg.Action
)

CONF_CODE = "code"
CONF_GPIO = "gpio"

CONFIG_SCHEMA = cv.Schema({})

async def to_code(config):
    pass

RC_SWITCH_SEND_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(SendRCSwitchAction),
        cv.Required(CONF_CODE): cv.positive_int,
        cv.Optional(CONF_GPIO, default=23): cv.int_,
    }
)

@cg.register_action(
    "rc_switch_component.send",
    SendRCSwitchAction,
    RC_SWITCH_SEND_SCHEMA,
)
async def rc_switch_send_to_code(config, action_id, template_arg, args):
    _LOGGER.info("rc_switch_component action called!")
    var = cg.new_Pvariable(action_id, template_arg)
    cg.add(var.set_code(config[CONF_CODE]))
    cg.add(var.set_gpio(config[CONF_GPIO]))
    cg.add_library("sui77/rc-switch", None)
    return var
