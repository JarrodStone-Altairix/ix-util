package com.arrowsmith.brainex.~@{Template}.install;

public class Create~@{Template}Tables extends CreatePackageTables  {

  public static void main(String[] args) {
    new Create~@{Template}Tables().innerMain(args);
  }
  public void runBatchCommand(String[] args) {
    new Install_~@{Template}().createTables(args);
  }
}