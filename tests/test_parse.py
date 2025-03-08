from pathlib import Path

from hdltools.mod_parse import ModParse

vfile = Path(__file__).parent.resolve() / 'hdl/modules.sv'


def test_modules():
    vobj = ModParse(vfile)
    modules = vobj.get_modules()
    assert len(modules) == 3


def test_empty():
    vobj = ModParse(vfile)
    module = vobj.get_module('mod_empty')
    assert module == {}


def test_params():
    vobj = ModParse(vfile)
    module = vobj.get_module('mod_param')
    assert 'params' in module
    params = {}
    params["INTPARAM1"] = {"value": "8"}
    params["INTPARAM2"] = {"type": "int", "value": "8"}
    params["VECPARAM1"] = {"packed": "[3:0]", "value": "4'b1010"}
    params["VECPARAM2"] = {"type": "logic", "packed": "[3:0]", "value": "'1"}
    params["BITPARAM1"] = {"type": "bit", "value": "1'b0"}
    params["BITPARAM2"] = {"type": "bit", "packed": "[3:0]", "value": "4'h3"}
    params["STRPARAM1"] = {"type": "string", "value": '"test"'}
    params["REAPARAM1"] = {"type": "real", "value": "2.5"}
    assert module["params"] == params


def test_ports():
    vobj = ModParse(vfile)
    module = vobj.get_module('mod_param')
    assert 'ports' in module
    ports = {
        'inputs': {'data_in': {'packed': '[INTPARAM1-1:0]'}},
        'outputs': {'data_out': {'packed': '[INTPARAM1-1:0]'}}
    }
    assert module['ports'] == ports
    module = vobj.get_module('mod_nopar')
    assert 'ports' in module
    assert module['ports']['inputs'] == gen_ports('in')
    assert module['ports']['outputs'] == gen_ports('out')
    assert module['ports']['inouts'] == gen_ports('io')


def gen_ports(prefix):
    ports = {}
    types = [None, 'reg', 'wire', 'logic']
    for i in range(64):
        key = f"{prefix}{i:02d}"
        entry = {}
        if i % 4 != 0:
            entry["type"] = types[i % 4]
        if (i // 4) % 2 == 1:
            entry["sign"] = "signed"
        if (i // 8) % 2 == 1:
            if (i // 2) % 2:
                entry["packed"] = "[7:0][7:0]"
            else:
                entry["packed"] = "[7:0]"
        if (i // 16) % 2 == 1:
            if (i // 2) % 2:
                entry["unpacked"] = "[1:8][1:8]"
            else:
                entry["unpacked"] = "[1:8]"
        if (i // 32) % 2 == 1:
            entry["default"] = "'0" if i % 2 else "1'b0"
            if i >= 40:
                entry["default"] = "'0" if i % 2 else "8'h0"
            if i >= 48:
                entry["default"] = "'{default:0}"
        ports[key] = entry
    return ports
