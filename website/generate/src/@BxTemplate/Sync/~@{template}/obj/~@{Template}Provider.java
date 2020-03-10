package com.arrowsmith.async.brainex.~@{Template}.obj;

public class ~@{Template}Provider extends ServiceProviderStub {

  public final static String OBJNM    = "~@{Template}Provider";
  public final static String OBJDESC  = "~@{Template} Provider";
  
  public final ~@{Template}Control ctl = addPart(new ~@{Template}Control(), ServiceOPCode.REQUEST);

  public ~@{Template}Provider() {
    this(SrvcConst.SRVCROUTE_DEFAULT);
  }

  public ~@{Template}Provider(String srvcRouteId) {
    super(~@{Template}Const.NMSPC, OBJNM, OBJDESC, srvcRouteId);
  }
}
