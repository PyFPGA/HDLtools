import pytest

from pathlib import Path
from hdltools.hdl_reader import HDLReader


@pytest.mark.parametrize('ext', [
    'vhdl', 'sv'
], ids=['VHDL', 'Verilog'])
def test_remove_comments(ext):
    file_in = Path(__file__).parent.resolve() / 'hdl' / f'dut_comments.{ext}'
    file_out = Path(__file__).parent.resolve() / 'hdl' / f'dut_final.{ext}'
    vobj1 = HDLReader()
    vobj1.read_file(file_in)
    vobj2 = HDLReader()
    vobj2.read_file(file_out)
    assert vobj1.get_code() == vobj2.get_code()
