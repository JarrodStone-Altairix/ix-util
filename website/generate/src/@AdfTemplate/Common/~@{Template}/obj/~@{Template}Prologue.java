package com.altairix.comm.adf.~@{Template}.obj;

public class ~@{Template}Prologue extends Prologue  {

  public static final String OBJNM = "~@{Template}Prologue";
  public static final String OBJDESC = "~@{Template}Prologue";
  private FieldList fldLs = addPart(new FieldList(Serialize.NODE_NMSPC_DEFAULT_PREFIX + OBJNM), ServiceOpCode.FORCE);
  public ~@{Template}UidField ~@{Template}Uid = fldLs.addField(new ~@{Template}UidField());

  public ~@{Template}Prologue() {
    super(~@{Template}Const.NMSPC, OBJNM, OBJDESC);
  }
  public ~@{Template}Prologue(String nmSpc, String objNm, String objDesc) {
    super(nmSpc, objNm, objDesc);
  }
}