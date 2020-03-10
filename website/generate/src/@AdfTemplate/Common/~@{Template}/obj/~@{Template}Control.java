package com.altairix.comm.adf.~@{Template}.obj;

public class ~@{Template}Control extends ControlStub  {

  public static final String OBJNM = "~@{Template}Control";
  public static final String OBJDESC = "~@{Template}Control";
  private FieldList fldLs = addPart(new FieldList(Serialize.NODE_NMSPC_DEFAULT_PREFIX + OBJNM), ServiceOpCode.REQUEST);
  public ~@{Template}LsTcdField ~@{Template}LsTcd = fldLs.addField(new ~@{Template}LsTcdField());
  public ~@{Template}UidField ~@{Template}Uid = fldLs.addField(new ~@{Template}UidField());

  public ~@{Template}Control() {
    super(~@{Template}Const.NMSPC, OBJNM, OBJDESC);
  }
  public ~@{Template}Control(String nmSpc, String objNm, String objDesc) {
    super(nmSpc, objNm, objDesc);
  }
}