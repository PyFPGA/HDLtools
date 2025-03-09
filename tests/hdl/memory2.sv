module memory2 #(
  parameter     [3:0]       AWIDTH = 8,
  parameter int             DWIDTH = 32
)(
  input  wire               clk,
  input                     wr,
  input        [AWIDTH-1:0] addr,
  input        [DWIDTH-1:0] wdata,
  output reg   [DWIDTH-1:0] rdata
);

  localparam DEPTH = 1 << AWIDTH;
  logic [DWIDTH-1:0] mem [DEPTH];

  always @(posedge clk) begin
    if (wr)
        mem[addr] <= wdata;
    else
        rdata <= mem[addr];
  end

endmodule
