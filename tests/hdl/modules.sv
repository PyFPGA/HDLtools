// input|output|inout [reg|wire|logic] [signed|unsigned] [range] name [dimensions] [= value]

/*
  Empty module
*/

module mod_empty ();
endmodule

/*
  Module without parameters
*/

module mod_nopar (
  input                     in00 = 1'b0,
  input  reg                in01,
  input  wire               in02,
  input  logic              in03,
  input        signed       in04,
  input  reg   signed       in05,
  input  wire  signed       in06,
  input  logic signed       in07,
  input               [7:0] in08,
  input  reg          [7:0] in09,
  input  wire         [7:0] in10,
  input  logic        [7:0] in11,
  input        signed [7:0] in12,
  input  reg   signed [7:0] in13,
  input  wire  signed [7:0] in14,
  input  logic signed [7:0] in15,
  input                     in16 [1:8],
  input  reg                in17 [1:8],
  input  wire               in18 [1:8][1:8],
  input  logic              in19 [1:8][1:8],
  input        signed       in20 [1:8],
  input  reg   signed       in21 [1:8],
  input  wire  signed       in22 [1:8][1:8],
  input  logic signed       in23 [1:8][1:8],
  input               [7:0] in24 [1:8],
  input  wire         [7:0] in25 [1:8],
  input  reg          [7:0] in26 [1:8][1:8],
  input  logic        [7:0] in27 [1:8][1:8],
  input        signed [7:0] in28 [1:8],
  input  reg   signed [7:0] in29 [1:8],
  input  wire  signed [7:0] in30 [1:8][1:8],
  input  logic signed [7:0] in31 [1:8][1:8],
  input                     in32            = 1'b0,
  input  reg                in33            = '0,
  input  wire               in34            = 1'b0,
  input  logic              in35            = '0,
  input        signed       in36            = 1'b0,
  input  reg   signed       in37            = '0,
  input  wire  signed       in38            = 1'b0,
  input  logic signed       in39            = '0,
  input               [7:0] in40            = 8'h0,
  input  reg          [7:0] in41            = '0,
  input  wire         [7:0] in42            = 8'h0,
  input  logic        [7:0] in43            = '0,
  input        signed [7:0] in44            = 8'h0,
  input  reg   signed [7:0] in45            = '0,
  input  wire  signed [7:0] in46            = 8'h0,
  input  logic signed [7:0] in47            = '0,
  input                     in48 [1:8]      = '{default:0},
  input  reg                in49 [1:8]      = '{default:0},
  input  wire               in50 [1:8][1:8] = '{default:0},
  input  logic              in51 [1:8][1:8] = '{default:0},
  input        signed       in52 [1:8]      = '{default:0},
  input  reg   signed       in53 [1:8]      = '{default:0},
  input  wire  signed       in54 [1:8][1:8] = '{default:0},
  input  logic signed       in55 [1:8][1:8] = '{default:0},
  input               [7:0] in56 [1:8]      = '{default:0},
  input  wire         [7:0] in57 [1:8]      = '{default:0},
  input  reg          [7:0] in58 [1:8][1:8] = '{default:0},
  input  logic        [7:0] in59 [1:8][1:8] = '{default:0},
  input        signed [7:0] in60 [1:8]      = '{default:0},
  input  reg   signed [7:0] in61 [1:8]      = '{default:0},
  input  wire  signed [7:0] in62 [1:8][1:8] = '{default:0},
  input  logic signed [7:0] in63 [1:8][1:8] = '{default:0},
  //
  output                    out00,
  output reg                out01,
  output wire               out02,
  output logic              out03,
  output       signed       out04,
  output reg   signed       out05,
  output wire  signed       out06,
  output logic signed       out07,
  output              [7:0] out08,
  output reg          [7:0] out09,
  output wire         [7:0] out10,
  output logic        [7:0] out11,
  output       signed [7:0] out12,
  output reg   signed [7:0] out13,
  output wire  signed [7:0] out14,
  output logic signed [7:0] out15,
  output                    out16 [1:8],
  output reg                out17 [1:8],
  output wire               out18 [1:8][1:8],
  output logic              out19 [1:8][1:8],
  output       signed       out20 [1:8],
  output reg   signed       out21 [1:8],
  output wire  signed       out22 [1:8][1:8],
  output logic signed       out23 [1:8][1:8],
  output              [7:0] out24 [1:8],
  output wire         [7:0] out25 [1:8],
  output reg          [7:0] out26 [1:8][1:8],
  output logic        [7:0] out27 [1:8][1:8],
  output       signed [7:0] out28 [1:8],
  output reg   signed [7:0] out29 [1:8],
  output wire  signed [7:0] out30 [1:8][1:8],
  output logic signed [7:0] out31 [1:8][1:8],
  output                    out32            = 1'b0,
  output reg                out33            = '0,
  output wire               out34            = 1'b0,
  output logic              out35            = '0,
  output       signed       out36            = 1'b0,
  output reg   signed       out37            = '0,
  output wire  signed       out38            = 1'b0,
  output logic signed       out39            = '0,
  output              [7:0] out40            = 8'b0,
  output reg          [7:0] out41            = '0,
  output wire         [7:0] out42            = 8'b0,
  output logic        [7:0] out43            = '0,
  output       signed [7:0] out44            = 8'b0,
  output reg   signed [7:0] out45            = '0,
  output wire  signed [7:0] out46            = 8'b0,
  output logic signed [7:0] out47            = '0,
  output                    out48 [1:8]      = '{default:0},
  output reg                out49 [1:8]      = '{default:0},
  output wire               out50 [1:8][1:8] = '{default:0},
  output logic              out51 [1:8][1:8] = '{default:0},
  output       signed       out52 [1:8]      = '{default:0},
  output reg   signed       out53 [1:8]      = '{default:0},
  output wire  signed       out54 [1:8][1:8] = '{default:0},
  output logic signed       out55 [1:8][1:8] = '{default:0},
  output              [7:0] out56 [1:8]      = '{default:0},
  output wire         [7:0] out57 [1:8]      = '{default:0},
  output reg          [7:0] out58 [1:8][1:8] = '{default:0},
  output logic        [7:0] out59 [1:8][1:8] = '{default:0},
  output       signed [7:0] out60 [1:8]      = '{default:0},
  output reg   signed [7:0] out61 [1:8]      = '{default:0},
  output wire  signed [7:0] out62 [1:8][1:8] = '{default:0},
  output logic signed [7:0] out63 [1:8][1:8] = '{default:0},
  //
  inout                     io00,
  inout  reg                io01,
  inout  wire               io02,
  inout  logic              io03,
  inout        signed       io04,
  inout  reg   signed       io05,
  inout  wire  signed       io06,
  inout  logic signed       io07,
  inout               [7:0] io08,
  inout  reg          [7:0] io09,
  inout  wire         [7:0] io10,
  inout  logic        [7:0] io11,
  inout        signed [7:0] io12,
  inout  reg   signed [7:0] io13,
  inout  wire  signed [7:0] io14,
  inout  logic signed [7:0] io15,
  inout                     io16 [1:8],
  inout  reg                io17 [1:8],
  inout  wire               io18 [1:8][1:8],
  inout  logic              io19 [1:8][1:8],
  inout        signed       io20 [1:8],
  inout  reg   signed       io21 [1:8],
  inout  wire  signed       io22 [1:8][1:8],
  inout  logic signed       io23 [1:8][1:8],
  inout               [7:0] io24 [1:8],
  inout  reg          [7:0] io25 [1:8],
  inout  wire         [7:0] io26 [1:8][1:8],
  inout  logic        [7:0] io27 [1:8][1:8],
  inout        signed [7:0] io28 [1:8],
  inout  reg   signed [7:0] io29 [1:8],
  inout  wire  signed [7:0] io30 [1:8][1:8],
  inout  logic signed [7:0] io31 [1:8][1:8],

  inout                     io00            = 1'b0,
  inout  reg                io01            = '0,
  inout  wire               io02            = 1'b0,
  inout  logic              io03            = '0,
  inout        signed       io04            = 1'b0,
  inout  reg   signed       io05            = '0,
  inout  wire  signed       io06            = 1'b0,
  inout  logic signed       io07            = '0,
  inout               [7:0] io08            = 8'b0,
  inout  reg          [7:0] io09            = '0,
  inout  wire         [7:0] io10            = 8'b0,
  inout  logic        [7:0] io11            = '0,
  inout        signed [7:0] io12            = 8'b0,
  inout  reg   signed [7:0] io13            = '0,
  inout  wire  signed [7:0] io14            = 8'b0,
  inout  logic signed [7:0] io15            = '0,
  inout                     io16 [1:8]      = '{default:0},
  inout  reg                io17 [1:8]      = '{default:0},
  inout  wire               io18 [1:8][1:8] = '{default:0},
  inout  logic              io19 [1:8][1:8] = '{default:0},
  inout        signed       io20 [1:8]      = '{default:0},
  inout  reg   signed       io21 [1:8]      = '{default:0},
  inout  wire  signed       io22 [1:8][1:8] = '{default:0},
  inout  logic signed       io23 [1:8][1:8] = '{default:0},
  inout               [7:0] io24 [1:8]      = '{default:0},
  inout  reg          [7:0] io25 [1:8]      = '{default:0},
  inout  wire         [7:0] io26 [1:8][1:8] = '{default:0},
  inout  logic        [7:0] io27 [1:8][1:8] = '{default:0},
  inout        signed [7:0] io28 [1:8]      = '{default:0},
  inout  reg   signed [7:0] io29 [1:8]      = '{default:0},
  inout  wire  signed [7:0] io30 [1:8][1:8] = '{default:0},
  inout  logic signed [7:0] io31 [1:8][1:8] = '{default:0}
);

  always_comb begin
    out00 = in00;
    out01 = in01;
    out02 = in02;
    out03 = in03;
    out04 = in04;
    out05 = in05;
    out06 = in06;
    out07 = in07;
    out08 = in08;
    out09 = in09;
    out10 = in10;
    out11 = in11;
    out12 = in12;
    out13 = in13;
    out14 = in14;
    out15 = in15;
    out16 = in16;
    out17 = in17;
    out18 = in18;
    out19 = in19;
    out20 = in20;
    out21 = in21;
    out22 = in22;
    out23 = in23;
    out24 = in24;
    out25 = in25;
    out26 = in26;
    out27 = in27;
    out28 = in28;
    out29 = in29;
    out30 = in30;
    out31 = in31;
    out32 = in32;
    out33 = in33;
    out34 = in34;
    out35 = in35;
    out36 = in36;
    out37 = in37;
    out38 = in38;
    out39 = in39;
    out40 = in40;
    out41 = in41;
    out42 = in42;
    out43 = in43;
    out44 = in44;
    out45 = in45;
    out46 = in46;
    out47 = in47;
    out48 = in48;
    out49 = in49;
    out50 = in50;
    out51 = in51;
    out52 = in52;
    out53 = in53;
    out54 = in54;
    out55 = in55;
    out56 = in56;
    out57 = in57;
    out58 = in58;
    out59 = in59;
    out60 = in60;
    out61 = in61;
    out62 = in62;
    out63 = in63;
  end

  always_comb begin
    io00 = in00;
    io01 = in01;
    io02 = in02;
    io03 = in03;
    io04 = in04;
    io05 = in05;
    io06 = in06;
    io07 = in07;
    io08 = in08;
    io09 = in09;
    io10 = in10;
    io11 = in11;
    io12 = in12;
    io13 = in13;
    io14 = in14;
    io15 = in15;
    io16 = in16;
    io17 = in17;
    io18 = in18;
    io19 = in19;
    io20 = in20;
    io21 = in21;
    io22 = in22;
    io23 = in23;
    io24 = in24;
    io25 = in25;
    io26 = in26;
    io27 = in27;
    io28 = in28;
    io29 = in29;
    io30 = in30;
    io31 = in31;
    io32 = in32;
    io33 = in33;
    io34 = in34;
    io35 = in35;
    io36 = in36;
    io37 = in37;
    io38 = in38;
    io39 = in39;
    io40 = in40;
    io41 = in41;
    io42 = in42;
    io43 = in43;
    io44 = in44;
    io45 = in45;
    io46 = in46;
    io47 = in47;
    io48 = in48;
    io49 = in49;
    io50 = in50;
    io51 = in51;
    io52 = in52;
    io53 = in53;
    io54 = in54;
    io55 = in55;
    io56 = in56;
    io57 = in57;
    io58 = in58;
    io59 = in59;
    io60 = in60;
    io61 = in61;
    io62 = in62;
    io63 = in63;
  end

endmodule

/*
  Module with parameters
*/

module mod_param #(
  parameter              INTPARAM1 = 8,
  parameter int          INTPARAM2 = 8,
  parameter        [3:0] VECPARAM2 = 4'b1010,
  parameter logic  [3:0] VECPARAM1 = '1,
  parameter bit          BITPARAM2 = 1'b0,
  parameter bit    [3:0] BITPARAM1 = 4'b1010,
  parameter string       STRPARAM1 = "test",
  parameter real         REAPARAM1 = 2.5
)(
  input  [INTPARAM1-1:0] data_in,
  output [INTPARAM1-1:0] data_out
);

  assign data_out = data_in;

endmodule
