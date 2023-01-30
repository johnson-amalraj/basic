////////////////////////////////////////////////
////s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s////
////s           www.testbench.in           s////
////s                                      s////
////s              UVM Tutorial            s////
////s                                      s////
////s            gopi@testbench.in          s////
////s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s////
//////////////////////////////////////////////// 
`ifndef GUARD_ENV
`define GUARD_ENV

class Environment extends uvm_env;

    `uvm_component_utils(Environment)

    function new(string name , uvm_component parent = null);
        super.new(name, parent);
    endfunction: new

    virtual function void build();
        super.build();
       
        uvm_report_info(get_full_name(),"START of build ",UVM_LOW);
      
        uvm_report_info(get_full_name(),"END of build ",UVM_LOW);
    endfunction
    
    virtual function void connect();
        super.connect();
        uvm_report_info(get_full_name(),"START of connect ",UVM_LOW);
    
        uvm_report_info(get_full_name(),"END of connect ",UVM_LOW);
    endfunction

endclass : Environment

`endif 