package com.altairix.comm.adf.~@{Template}.obj;

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