package com.arrowsmith.brainex.~@{Template};

import com.altairix.adf.dbio.DbIndex;
import com.altairix.adf.dbio.Dbio.OpenMode;
import com.altairix.adf.srvc.ObjectListConfig;
import com.altairix.adf.srvc.ServiceEvent;
import com.altairix.adf.srvc.ServiceEventHandlerStub;
import com.altairix.adf.srvc.ServiceEventId;
import com.altairix.adf.srvc.ServicePool;
import com.altairix.adf.srvc.SimpleService;
import com.altairix.adf.srvc.SimpleService.Call;
import com.altairix.comm.adf.fields.AdfEnums.ServiceEventTcd;
import com.altairix.comm.adf.root.log.Logger;
import com.altairix.comm.adf.root.log.LoggerFactory;
import com.altairix.comm.adf.root.trace.Trace;
import com.altairix.comm.adf.root.trace.Tracer;
import com.altairix.comm.adf.root.user.HasUserData;
import com.altairix.comm.adf.srvc.ParmList;
import com.altairix.comm.adf.srvc.obj.ControlStub;
import com.altairix.comm.adf.srvc.obj.DataObjectStub;
import com.altairix.comm.adf.srvc.obj.SelectStub;
import com.arrowsmith.acts.Acts_Server;
import com.arrowsmith.comm.acts.qnaire.BxQnaireConst;
import com.arrowsmith.comm.acts.qnaire.obj.qnaire.BxQnaireControl;
import com.arrowsmith.comm.acts.qnaire.obj.qnaire.BxQnaireSelect;

public class ~@{Template}LocalService extends SimpleService  {

  public static final String CLASSNM = ~@{Template}LocalService.class.getName();
  public static final String CLASSNM_SIMPLE = ~@{Template}LocalService.class.getSimpleName();
  public static final String SERVICE_NAME = "~@{Template}";
  public static final ServiceEventId SERVICE_EVENT_ID = new ServiceEventId(~@{Template}Const.NMSPC, SERVICE_NAME);
  private static Logger logger = LoggerFactory.getLogger(CLASSNM);
  private Tracer tracer = Trace.getUserTracer(CLASSNM_SIMPLE);;
  private ~@{Template}File00 ~@{Template}File00r = registerIndex(new ~@{Template}File00(this, OpenMode.READ_ONLY));
  private ~@{Template}File00 ~@{Template}File00w = registerIndex(new ~@{Template}File00(this, OpenMode.WRITE));

   ~@{Template}LocalService(ServicePool srvcPool) {
    super(srvcPool);
  }
  public String getServiceName() {
    return SERVICE_NAME;
  }
  public boolean handleServiceEvent(ServiceEventHandlerStub hdlr, ServiceEvent event, ParmList parmLs) {
     
    // TODO_JS Add service events
    return super.handleServiceEvent(hdlr, event, parmLs);
  
  }
  protected int calcAccessPath(ControlStub ctl, SelectStub sel, ObjectListConfig objLsCfg) {
    
  if (logger.isTraceEnabled()) {
    logger.trace("Starting calcAccessPath(). ControlStub({}) SelectStub({}) ObjectListConfig({}).", ctl, sel, objLsCfg);
  }

  @SuppressWarnings("unused")
  ~@{Template}Control ~@{Template}Ctl = (~@{Template}Control) ctl;
  ~@{Template}Select ~@{Template}Sel = (~@{Template}Select) sel;

  // Set default access path
  int accPath = SimpleService.ACCESSPATH_ERROR;

  // TODO_JS Implement this method 

  return accPath;
  
  }
  protected DbIndex getIndex(int accessPath) {
    
    // TODO_JS Implement this method 
    switch (accessPath) {
      default: return null;
    }
  
  }
  protected ServiceEventId getServiceEventId() {
    return SERVICE_EVENT_ID;
  }
  protected String getServiceEventKey(ServiceEventTcd eventTcd, ControlStub ctl, DataObjectStub dataObj) {
    
    if (dataObj == null) {
      ~@{Template}Control ~@{Template}Ctl = (~@{Template}Control) ctl;
      return SERVICE_NAME + ":" + ~@{Template}Ctl.~@{Template}Uid.getString();
    }

    ~@{Template}Long ~@{Template}Long = (~@{Template}Long) dataObj;
    return SERVICE_NAME + ":" + ~@{Template}Long.stat.~@{Template}Uid.getString();
  
  }
  protected DbIndex getUniqueReadIndex() {
    return ~@{Template}File00r;
  }
  protected DbIndex getUniqueUpdateIndex() {
    return ~@{Template}File00w;
  }
  protected boolean isRecordSelected(DbIndex dbIndex, ControlStub ctl, SelectStub sel) {
    
      ~@{Template}Control ~@{Template}Ctl = (~@{Template}Control) ctl;
      ~@{Template}File ~@{Template}File = (~@{Template}File) dbIndex.dbFile;
      ~@{Template}Select ~@{Template}Sel = (~@{Template}Select) sel;

      // TODO_JS Implement this method 

      return true;
  
  }
  protected boolean isUserAuthorized_Create(DbIndex dbIndex, ControlStub ctl, DataObjectStub dataObj) {
    
    // TODO_JS Implement this method
    logUnsupportedMethod("isUserAuthorized_Create");
    return false;
  }
  protected boolean isUserAuthorized_Delete(DbIndex dbIndex, ControlStub ctl) {
    
    // TODO_JS Implement this method
    logUnsupportedMethod("isUserAuthorizedDelete");
    return false;
  }
  protected boolean isUserAuthorized_Retrieve(DbIndex dbIndex, ControlStub ctl, boolean logSecurityFg) {
    
    // TODO_JS Implement this method
    logUnsupportedMethod("isUserAuthorized_Retrieve");
    return false;
  }
  protected boolean isUserAuthorized_Update(DbIndex dbIndex, ControlStub ctl, DataObjectStub dataObj) {
    
    // TODO_JS Implement this method
    logUnsupportedMethod("isUserAuthorized_Update");
    return false;
  }
  protected boolean isValidCreate(ControlStub ctl, DataObjectStub dataObj) {
    
    // TODO_JS Implement this method
    logUnsupportedMethod("isValidCreate");
    return false;
  }
  protected boolean isValidCtl(ControlStub ctl, Call call) {
    
    // TODO_JS Implement this method
    logUnsupportedMethod("isValidDelete");
    return false;
  }
  protected boolean isValidDataObj(DataObjectStub dataObj, Call call) {
    
    // TODO_JS Implement this method
    logUnsupportedMethod("isValidRetrieve");
    return false;
  }
  protected boolean isValidSel(SelectStub sel, Call call) {
    
    // TODO_JS Implement this method
    logUnsupportedMethod("isValidSel");
    return false;
  }
  protected void logUnsupportedMethod(String methodNm) {
    
    Acts_Server.logSecurityViolation("perform unsupported method {}.{}", getServiceName(), methodNm);
  
  }
  protected void logUnsupportedMethod(String methodNm, Object[] logObj) {
    
    Acts_Server.logSecurityViolation(logObj, "perform unsupported method {}.{}", new Object[] {getServiceName(), methodNm});
  
  }
  protected void moveCtlToIndex(ControlStub ctl, DbIndex dbIndex, Call call) {
    
    ~@{Template}File ~@{Template}File = (~@{Template}File) dbIndex.dbFile;
    ~@{Template}Control ~@{Template}Ctl = (~@{Template}Control) ctl;
    // TODO_JS Implement this method
  
  }
  protected void moveDataObjToIndex(ControlStub ctl, DataObjectStub dataObj, DbIndex dbIndex, Call call) {
    
    ~@{Template}File ~@{Template}File = (~@{Template}File) dbIndex.dbFile;
    ~@{Template}Control ~@{Template}Ctl = (~@{Template}Control) ctl;
    // TODO_JS Implement this method
    if (dataObj instanceof ~@{Template}Long) { moveLongToFile((~@{Template}Long) dataObj, (~@{Template}File) dbIndex.dbFile); }
    else if (dataObj instanceof ~@{Template}Short) { moveShortToFile((~@{Template}Short) dataObj, (~@{Template}File) dbIndex.dbFile); }
  
  }
  protected void moveIndexToDataObj(DbIndex dbIndex, ControlStub ctl, DataObjectStub dataObj) {
    
    ~@{Template}File ~@{Template}File = (~@{Template}File) dbIndex.dbFile;
    ~@{Template}Control ~@{Template}Ctl = (~@{Template}Control) ctl;
    // TODO_JS Implement this method
    if (dataObj instanceof ~@{Template}Long) { moveFileToLong((~@{Template}File) dbIndex.dbFile, (~@{Template}Long) dataObj); }
    else if (dataObj instanceof ~@{Template}Short) { moveFileToShort((~@{Template}File) dbIndex.dbFile, (~@{Template}Short) dataObj); }
  
  }
  protected void moveIndexToDataObjStat(DbIndex dbIndex, DataObjectStub dataObj) {
    
    ~@{Template}File ~@{Template}File = (~@{Template}File) dbIndex.dbFile;
    // TODO_JS Implement this method
  
  }
  protected void moveSelToIndex(SelectStub sel, DbIndex dbIndex, Call call) {
    
    ~@{Template}File ~@{Template}File = (~@{Template}File) dbIndex.dbFile;
    ~@{Template}Select ~@{Template}Sel = (~@{Template}Select) sel;
    // TODO_JS Implement this method
  
  }
  protected void retrieveDataObjInfo(Call call, ControlStub ctl, DataObjectStub dataObj) {
    
    // TODO_JS Implement this method
    if (dataObj instanceof ~@{Template}Long) { retrieveLongInfo(call, (~@{Template}Control) ctl, (~@{Template}Long) dataObj); }
    else if (dataObj instanceof ~@{Template}Short) { retrieveShortInfo(call, (~@{Template}Control) ctl, (~@{Template}Short) dataObj); }
  
  }
  protected void setIndexAuditFields(DbIndex dbIndex, HasUserData call) {
    
    ~@{Template}File ~@{Template}File = (~@{Template}File) dbIndex.dbFile;
    // TODO_JS Implement this method
  
  }
  private void moveLongToFile(~@{Template}Long ~@{Template}Long, ~@{Template}File ~@{Template}File) {
    // TODO_JS Implement this method
  }
  private void moveShortToFile(~@{Template}Short ~@{Template}Short, ~@{Template}File ~@{Template}File) {
    // TODO_JS Implement this method
  }
  private void moveFileToLong(~@{Template}File ~@{Template}File, ~@{Template}Long ~@{Template}Long) {
    // TODO_JS Implement this method
  }
  private void moveFileToShort(~@{Template}File ~@{Template}File, ~@{Template}Short ~@{Template}Sht) {
    // TODO_JS Implement this method
  }
  private void retrieveLongInfo(Call call, ~@{Template}Control ~@{Template}Ctl, ~@{Template}Long ~@{Template}Long) {
    // TODO_JS Implement this method
  }
  private void retrieveShortInfo(Call call, ~@{Template}Control ~@{Template}Ctl, ~@{Template}Short ~@{Template}Sht) {
    // TODO_JS Implement this method
  }
}