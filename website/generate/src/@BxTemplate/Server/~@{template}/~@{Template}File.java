package com.arrowsmith.brainex.~@{Template};

 class ~@{Template}File extends DbFile  {

  public static final String recordName;
  public static final String fileName;
  public static final String description;
  final DbStringField lastSysId = addField(new DbStringField("LAST_SYS_ID", "Last System Id", 32));
  final DbStringField lastUser = addField(new DbStringField("LAST_USER", "Last User", 32));
  final DbTimestampField lastTstp = addField(new DbTimestampField("LAST_TSTP", "Last Timestamp"));
  final DbStringField ~@{Template}Uid = addField(new DbStringField("~@{TEMPLATE}_UID", "~@{Template} Uid", 16));

   ~@{Template}File() {
    super(fileName, description, recordName);
  }
  static void createTables() {
    
    TableManager.createTable(new ~@{Template}File());
    TableManager.createIndex(new ~@{Template}File00(null));
  
  }
  public DbFile copy() {
    
    DbFile newFile = new ~@{Template}File();
    newFile.copyFields(this);
    return newFile;
  
  }
} class ~@{Template}File00 extends DbIndex  {

  private static final String indexName = ~@{Template}File.fileName + "00";
  private static final String description = ~@{Template}File.description + ": ~@{Template}Uid.";
  private final ~@{Template}File file;

   ~@{Template}File00(DbScopeObject dbScopeObj) {
    this(dbScopeObj, OpenMode.READ_ONLY);
  }
   ~@{Template}File00(DbScopeObject dbScopeObj, FileDirection fileDirection) {
    this(dbScopeObj, OpenMode.READ_ONLY, fileDirection);
  }
   ~@{Template}File00(DbScopeObject dbScopeObj, OpenMode openMode) {
    this(dbScopeObj, openMode, FileDirection.FORWARD);
  }
   ~@{Template}File00(DbScopeObject dbScopeObj, OpenMode openMode, FileDirection fileDirection) {
    
    super(dbScopeObj, new ~@{Template}File(), indexName, description, KeyType.UNIQUE, openMode, fileDirection);
    file = (~@{Template}File) super.dbFile;
    addKey(file.~@{Template}Uid, EndValueTcd.EXCLUDE);
  
  }
}