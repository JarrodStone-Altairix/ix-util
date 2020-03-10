package com.arrowsmith.comm.brainex.~@{Template}.obj;

import com.altairix.comm.adf.fields.ServiceOpCode;
import com.altairix.comm.adf.srvc.obj.DataObjectStub;

public class ~@{Template}Long extends DataObjectStub  {

  public static final String OBJNM = "~@{Template}Long";
  public static final String OBJDESC = "~@{Template}Long";
  public ~@{Template}Body body = addPart(new ~@{Template}Body(), ServiceOpCode.FORCE);
  public ~@{Template}Info info = addPart(new ~@{Template}Info(), ServiceOpCode.RESPONSE);
  public ~@{Template}Status stat = addPart(new ~@{Template}Status(), ServiceOpCode.RESPONSE);

  public ~@{Template}Long() {
    super(~@{Template}Const.NMSPC, OBJNM, OBJDESC);
  }
}