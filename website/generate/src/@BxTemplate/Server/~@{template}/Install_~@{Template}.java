package com.arrowsmith.brainex.~@{Template};

public class Install_~@{Template} extends BatchCommand implements HasRemoteCommand {

  private static String NMSPC = ~@{Template}Const.NMSPC;
  private static String CLASSNM_SIMPLE = Install_~@{Template}.class.getSimpleName();
  private Tracer tracer;

  public static void main(String[] args) {
    
    new Install_~@{Template}().innerMain(args, false);
  
  }
  public boolean createTables(String[] args) {
    
    tracer = Trace.getUserTracer(CLASSNM_SIMPLE);

    tracer.trace("File creation started for " + NMSPC);

    // Create all files
    ~@{Template}File.createTables();

    tracer.trace("File creation ended for " + NMSPC);

    return true;
  
  }
  public void runBatchCommand(String[] args) {
    
    tracer = Trace.getUserTracer(CLASSNM_SIMPLE);

    tracer.trace("Install started for " + NMSPC);

    // Create all files
    new Create~@{Template}Data().runBatchCommand(args);
    new Create~@{Template}Tables().runBatchCommand(args);

    tracer.trace("Install ended for " + NMSPC);
  
  }
}