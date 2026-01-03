library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity dut is
  port (
    data_i :  in std_logic;
    data_o : out std_logic
  );
end dut;

architecture behav of dut is
begin

    data_o <= data_i;

end behav;
