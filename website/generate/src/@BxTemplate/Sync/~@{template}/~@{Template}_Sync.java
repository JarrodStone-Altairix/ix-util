package com.arrowsmith.comm.brainex.~@{Template};

import com.altairix.comm.adf.obj.BaseObject;
import com.altairix.comm.adf.root.log.Logger;
import com.altairix.comm.adf.root.log.LoggerFactory;
import com.arrowsmith.async.acts.~@{template}.obj.~@{Template}AsyncObjectFactory;
import com.arrowsmith.comm.acts.~@{template}.~@{Template}_Common;

public class ~@{Template}_Sync  {

  private static boolean initFg = false;
  private static Logger logger = LoggerFactory.getLogger(~@{Template}_Sync.class.getName());

  public static void init() {
    
  // Only initialize once
  if (initFg) {
    return;
  }

  // Register Object Factor
  BaseObject.registerObjectFactory(new ~@{Template}SyncObjectFactory());

  // set init flag
  initFg = true;

  logger.trace("~@{Template}_Sync initialized");
  }
}