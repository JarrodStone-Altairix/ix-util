package com.arrowsmith.comm.brainex.~@{template};

import com.altairix.comm.adf.obj.BaseObject;
import com.altairix.comm.adf.root.log.Logger;
import com.altairix.comm.adf.root.log.LoggerFactory;
import com.arrowsmith.async.acts.~@{template}.obj.~@{Template}AsyncObjectFactory;
import com.arrowsmith.comm.acts.~@{template}.~@{Template}_Common;

public class ~@{Template}_Async  {

  private static boolean initFg = false;
  private static Logger logger = LoggerFactory.getLogger(~@{Template}_Async.class.getName());

  public static void init() {
    
  // Only initialize once
  if (initFg) {
    return;
  }
  
  // Initialize Common package
  ~@{Template}_Common.init();

  // Register Object Factor
  BaseObject.registerObjectFactory(new ~@{Template}AsyncObjectFactory());

  // set init flag
  initFg = true;

  logger.trace("~@{Template}_Async initialized");
  }
}