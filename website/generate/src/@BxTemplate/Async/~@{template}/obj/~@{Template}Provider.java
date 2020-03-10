package com.arrowsmith.async.brainex.~@{template}.obj;

import com.altairix.adf.srvc.ServiceProviderStub;
import com.altairix.comm.adf.fields.ServiceOpCode;
import com.altairix.comm.adf.srvc.SrvcConst;
import com.arrowsmith.comm.acts.student.~@{Template}Const;

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
