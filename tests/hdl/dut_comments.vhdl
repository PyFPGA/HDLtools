/*
  Block comments (added in VHDL 2008)
*/
library IEEE; -- aaa
use IEEE.STD_LOGIC_1164.ALL; -- bbb
-- ccc
entity dut is
  port (
    data_i :  in std_logic; -- input
    data_o : out std_logic  -- output
  );
end dut;
-- ddd
-- eee
architecture behav of dut /* fff */is
begin
/* ggg -- */
    data_o <= data_i;
/*
  hhh
-- */
end behav;
