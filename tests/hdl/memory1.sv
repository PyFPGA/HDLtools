module memory1 #(
  parameter                 AWIDTH = 8,
  parameter                 DWIDTH = 32
)(
  input                     clk,
  input                     ce,
  input        [AWIDTH-1:0] addr,
  input        [DWIDTH-1:0] wdata,
  output logic [DWIDTH-1:0] rdata
);

  localparam DEPTH = 1 << AWIDTH;
  logic [DWIDTH-1:0] mem [DEPTH];

  always @(posedge clk) begin
    if (ce) begin
      rdata <= mem[addr];
      mem[addr] <= wdata;
    end
  end

endmodule
