from pathlib import Path

from hdltools.hdl_sanitize import HdlSanitize

vfile = Path(__file__).parent.resolve() / 'hdl/modules.sv'


def test_comments():
    vobj = HdlSanitize(vfile)
    vcode = vobj.get_code()
    comment_patterns = ['//', '/*', '*/', '--']
    assert not any(pattern in vcode for pattern in comment_patterns)


def test_spaces():
    vobj = HdlSanitize(vfile)
    vcode = vobj.get_code()
    assert '\n' not in vcode
    assert '  ' not in vcode
