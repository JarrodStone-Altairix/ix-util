public class Create~@{Template}Data extends CreatePackageData {

  private static String NMSPC          = ~@{Template}Const.NMSPC;
  private static String CLASSNM_SIMPLE = Create~@{Template}Data.class.getSimpleName();

  public static void main(String[] args) {
    new Create~@{Template}Data().innerMain(args, true);
  }

  @Override
  public void runBatchCommand(String[] args) {

    initLoggerTracer();

    tracer.trace("Data creation started for " + NMSPC);
	
	// Create UIDs
    // NextUid.createNextUid(~@{Template}Const.DTREE_UID, "0000000000",  NextUid.UidTcd.BASE34, NextUid.CacheLevelTcd.HIGH);

    // Create Registry Entries
    // createRegistryEntries();

    // Create messages
    // createMessages();

    // Load Install data files
    // reload~@{Template}Data();

    tracer.trace("Data creation ended for " + NMSPC);
  }

  private void createMessages() {

    tracer.trace("Create Messages started for " + CLASSNM_SIMPLE);

    MessageLong msgLong   = new MessageLong();

    msgLong.body.msgTx        .setValue("&0");
    msgLong.body.msgSevCd     .setValue(MsgSevCd.ERROR);
    createMessageEntry("en", "RTHK0001", msgLong);

    tracer.trace("Create Messages ended for " + CLASSNM_SIMPLE);
  }

  private void createRegistryEntries() {

    tracer.trace("Create Registry Entries started for " + CLASSNM_SIMPLE);

    tracer.trace("Create Registry Entries ended for " + CLASSNM_SIMPLE);
  }

  private void reload~@{Template}Data() {

    try {

      // Delete all existing files
      ~@{Template}_Server.deleteDTree(~@{Template}Const.DTREEUID_BRAINEX, ~@{Template}Const.DNODE_PATH_~@{TEMPLATE}, true);

      // Install new files
      Install~@{Template}Files installer = new Install~@{Template}Files();

      BNodeBuilder templateBldr = new BNodeBuilder(Bx~@{Template}Const.DTREEUID_BRAINEX,
          ~@{Template}Const.DNODE_PATH_~@{TEMPLATE}, ~@{Template}Name.AUTO);

      templateBldr
      .setCompressed(false)
      .setDomainCode(~@{Template}Const.DOMAINCD_CONFIG)
      .setOwner(~@{Template}_Server.DNODE_OWNERCD_BRAINEX, ~@{Template}_Server.DNODE_OWNERUID_BRAINEX)
      .setAccess(~@{Template}AccessTcd.CONTROL, ~@{Template}AccessTcd.NONE);

      int installCnt = installer.installFiles(BxFileSystem_Server.INSTALL_ROUTE_ID,
          ~@{Template}Const.FILESYSTEM_PATH_INSTALL_~@{TEMPLATE}, "", templateBldr);

      if (installCnt < 1) {
        throw new RuntimeException(logger.error("Failed to Load ~@{Template} files"));
      }
    }

    catch (Exception e) {
      throw new RuntimeException(logger.error(e, "Failed to Load ~@{Template}  files"));
    }
  }
}
