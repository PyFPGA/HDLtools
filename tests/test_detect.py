import pytest
from hdltools.hdl_detect import HdlDetect


code = {
  'vhdl': """
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Example is
  Port (
    data_i : in  STD_LOGIC;
    data_o : out STD_LOGIC
  );
end Example;

architecture Behavioral of Example is
begin
  data_o <= data_i;
end Behavioral;
""",
  'vlog': """
module Example (
  input  data_i,
  output data_o
);
  assign data_o = data_i;
endmodule
""",
  'slog': """
module Example (
  input  logic data_i,
  output logic data_o
);
  assign data_o = data_i;
endmodule
"""
}


@pytest.mark.parametrize("lang", ['vhdl', 'vlog', 'slog'])
def test_detect(lang):
    obj = HdlDetect(code[lang])
    assert obj.get_lang() == lang
