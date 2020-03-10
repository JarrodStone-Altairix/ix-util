package com.arrowsmith.comm.brainex.~@{Template};

public class ~@{Template}_Gwt  {

  private static boolean initFg = false;
  private static Logger logger = LoggerFactory.getLogger(~@{Template}_Gwt.class.getName());

  public static void init() {
    
  // Only initialize once
  if (initFg) {
    return;
  }
  
  // Initialize Async package
  ~@{Template}_Async.init();

  // set init flag
  initFg = true;

  logger.trace("~@{Template}_Gwt initialized");
  }
}