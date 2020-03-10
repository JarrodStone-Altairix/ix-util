package com.altairix.comm.adf.~@{Template}.obj;

public class ~@{Template}Select extends SelectStub  {

  public static final String OBJNM = "~@{Template}Select";
  public static final String OBJDESC = "~@{Template}Select";
  private FieldList fldLs = addPart(new FieldList(Serialize.NODE_NMSPC_DEFAULT_PREFIX + OBJNM), ServiceOpCode.FORCE);
  public ~@{Template}SortSeqCdField ~@{Template}SortSeqCd = fldLs.addField(new ~@{Template}SortSeqCdField("sortSeqCd"));
  public ~@{Template}UidField ~@{Template}Uid = fldLs.addField(new ~@{Template}UidField());

  public ~@{Template}Select() {
    super(~@{Template}Const.NMSPC, OBJNM, OBJDESC);
  }
  public ~@{Template}Select(String nmSpc, String objNm, String objDesc) {
    super(nmSpc, objNm, objDesc);
  }
}