package com.arrowsmith.brainex.~@{Template}.install;

public class Create~@{Template}Data extends CreatePackageData  {

  private static String NMSPC = ~@{Template}Const.NMSPC;
  private static String CLASSNM = Create~@{Template}Data.class.getName();
  private static String CLASSNM_SIMPLE = Create~@{Template}Data.class.getSimpleName();
  private static Logger logger;
  private Tracer tracer;

  public static void main(String[] args) {
    new Create~@{Template}Data().innerMain(args, false);
  }
  public void runBatchCommand(String[] args) {
    
    // Initialize the logger
    logger = LoggerFactory.getLogger(CLASSNM);
    logger.setLevel(AdfLogLevel.INFO);

    tracer = Trace.getUserTracer(CLASSNM_SIMPLE);

    tracer.trace("Data creation started for " + NMSPC);

    // Create Uids
    NextUid.createNextUid(~@{Template}Const.~@{TEMPLATE}_UID, "0000000000",  NextUid.UidTcd.BASE34, NextUid.CacheLevelTcd.HIGH);

    // Create Domain Values 
    //createDomainValues();

    // Create DNode messages
    //createMessages();

    tracer.trace("Data creation ended for " + NMSPC);
  
  }
}