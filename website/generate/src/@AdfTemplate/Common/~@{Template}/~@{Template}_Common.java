package com.altairix.comm.adf.~@{Template};

public class ~@{Template}_Common  {

  private static boolean initFg = false;
  private static Logger logger = LoggerFactor.getLogger(~@{Template}_Common.class.getName());

  public static void init() {

  // Only initialize once
  if (initFg) {
    return;
  }

  // Register Object Factor
  BaseObject.registerObjectFactor(new ~@{Template}CommonObjectFactory());

  // set init flag
  initFg = true;

  logger.trace("~@{Template}_Common initialized");
  }
}