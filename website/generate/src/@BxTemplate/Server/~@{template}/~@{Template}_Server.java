package com.arrowsmith.brainex.~@{Template};

public class ~@{Template}_Server  {

  private static boolean initFg = false;
  private static Logger logger = LoggerFactory.getLogger(~@{Template}_Server.class.getName());

  public static void init() {
    
    // Only initialize once
    if (initFg) { return; }

    // Initialize Common package
    ~@{Template}_Common.init();

    // Initialize Service package
    // ~@{Template}_Sync.init();

    // Register Server Object Factory
    BaseObject.registerObjectFactory(new ~@{Template}CommonObjectFactory());

    // Register Service Route and Remote Service Factory for Exercise Rollup
    ServiceManager.registerServiceRoute(~@{Template}LocalService.SERVICE_NAME,
        SrvcConst.SRVCROUTE_DEFAULT, ~@{Template}Const.NMSPC,
        new RemoteServiceFactory() {
      @Override
      public RemoteService newRemoteService(ServicePool srvcPool) {
        return new ~@{Template}LocalService(srvcPool);
      }
    });

    // Set init flag
    initFg = true;

    logger.trace("~@{Template} - Server initialized");
  
  }
}