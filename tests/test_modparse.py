from pathlib import Path

from hdltools.mod_parse import ModParse

vfile = Path(__file__).parent.resolve() / 'hdl/modules.sv'


def test_modules():
    vobj = ModParse(vfile)
    modules = vobj.get_modules()
    assert len(modules) == 3


def test_params():
    vobj = ModParse(vfile)
    modules = vobj.get_modules()
    assert 'params' in modules['mod_param']


def test_ports():
    vobj = ModParse(vfile)
    modules = vobj.get_modules()
    assert 'ports' in modules['mod_param']
    assert 'ports' in modules['mod_nopar']
