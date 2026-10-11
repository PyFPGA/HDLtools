// parameter [int|bit|logic|real|string] "[packed]" <name> = <value>
// input|output|inout [reg|wire|logic] [signed|unsigned] "[packed]" <name> "[unpacked]" [= <value>]

/*
  Empty module
*/

module mod_empty ();
endmodule

/*
  Commented module
*/

//module mod_commented ();
//endmodule

/*
  Module without parameters
*/

module mod_nopar (
  input                          port0,
  output reg                     port1,
  inout  wire                    port2,
  input      unsigned            port3, port4 [8], port5 = '1,
  output              [7:0]      port6,
  inout                          port7 [1:8],
  input                          port8            = 1'b0,
  output logic signed [7:0][7:0] port9 [1:8][1:8] = '{default:0}, portA, portB
);
endmodule

/*
  Module with parameters
*/

// `define DEFINE1 80

module mod_param #(
  parameter              PARAM0,
  parameter int          PARAM1,
  parameter        [3:0] PARAM2,
  parameter              PARAM3 = 1'b0,
  parameter logic  [3:0] PARAM4 = '1, PARAM5, PARAM6,
  localparam             LOCAL0 = PARAM3 + PARAM4, LOCAL1 = $clog2(PARAM0)
)(
  input  [$clog2(PARAM0)-1:0] port0,
  output [`DEFINE1-1:0]       port1,
  inout  [32]                 port2,
  inout  [`DEFINE2]           port3,
  inout  [PARAM1]             port4
);
endmodule

module mod_non_ansi (port0, port1, port2, port3, port4, port5, port6);

  // Parameters defined in the module body
  parameter int               PARAM0 = 32;
  parameter logic [7:0]       PARAM1 = 8'hAA, PARAM2= 8'hBB;
  localparam int signed       LOCAL0 = 16;

  // Port declarations in the module body
  input                       port0;
  wire                        port0 = 1'b1;
  output reg                  port1;
  inout                       port2;
  input                       port3, port4;
  logic signed [7:0]          port3 = 8'h99, port4;
  output              [15:0]  port5 [0:3];
  input  var logic            port6;

endmodule

// User-defined type outside the module
typedef logic [31:0] custom_data_t;

module mod_edge_cases (
  port0,
  port1,
  port2
);

  // 1. localparam in body
  localparam int              LOCAL0 = 16;

  // 2. Custom typedef and alternative net types
  input  custom_data_t        port0;
  output tri           [1:0]  port1;

  // 3. Legacy split declaration with interleaved RTL noise
  output                      port2;

  wire internal_sig = 1'b0;

  always_comb begin
    if (port0[0]) begin
        // some logic
    end
  end

  reg                         port2;

  assign port1 = 2'bzz;

endmodule
