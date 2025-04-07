from pathlib import Path

from hdltools.hdl_reader import HDLReader

vfile = Path(__file__).parent.resolve() / 'hdl' / 'modules.sv'


def test_comments():
    vobj = HDLReader()
    vobj.read_file(vfile)
    vcode = vobj.get_code()
    comment_patterns = ['//', '/*', '*/', '--']
    assert not any(pattern in vcode for pattern in comment_patterns)


def test_spaces():
    vobj = HDLReader()
    vobj.read_file(vfile)
    vcode = vobj.get_code()
    assert '\n' not in vcode
    assert '  ' not in vcode
