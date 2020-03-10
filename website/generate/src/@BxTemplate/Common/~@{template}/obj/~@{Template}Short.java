package com.arrowsmith.comm.brainex.~@{Template}.obj;

public class ~@{Template}Short extends DataObjectStub  {

  public static final String OBJNM = "~@{Template}Short";
  public static final String OBJDESC = "~@{Template}Short";
  private FieldList fldLs = addPart(new FieldList(Serialize.NODE_NMSPC_DEFAULT_PREFIX + OBJNM), ServiceOpCode.RESPONSE);
  public ~@{Template}LsTcdField ~@{Template}LsTcd = fldLs.addField(new ~@{Template}LsTcdField());
  public ~@{Template}UidField ~@{Template}Uid = fldLs.addField(new ~@{Template}UidField());

  public ~@{Template}Short() {
    super(~@{Template}Const.NMSPC, OBJNM, OBJDESC);
  }
}