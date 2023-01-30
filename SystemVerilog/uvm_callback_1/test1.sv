`include "uvm.svh"
import uvm_pkg::*;

`include "driver.sv"

module test;

Driver drvr;

initial begin
  drvr = new("drvr");
  run_test();
end 

endmodule 
