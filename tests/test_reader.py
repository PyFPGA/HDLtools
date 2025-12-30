import pytest

from pathlib import Path
from hdltools.hdl_reader import HDLReader


@pytest.fixture
def vcode():
    vfile = Path(__file__).parent.resolve() / 'hdl' / 'modules.sv'
    vobj = HDLReader()
    vobj.read_file(vfile)
    return vobj.get_code()


def test_comments(vcode):
    comment_patterns = ['//', '/*', '*/', '--']
    assert not any(pattern in vcode for pattern in comment_patterns)


def test_spaces(vcode):
    assert '\n' not in vcode
    assert '  ' not in vcode
