import esphome.codegen as cg
import esphome.config_validation as cv

CODEOWNERS = ["@richardledecky"]

rc_switch_ns = cg.esphome_ns.namespace("rc_switch_component")

# Registrácia C++ súborov
cg.add_library("rc-switch", None)
cg.add_source_file("rc_switch_component.cpp")
cg.add_source_file("rc_switch_component.h")
