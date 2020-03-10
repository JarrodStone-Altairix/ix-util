package com.altairix.comm.adf.~@{Template}.fields;

public class ~@{Template}LsTcdField extends EnumField<~@{Template}LsTcd>  {

  private static final String dftNm = "~@{Template}LsTcdField";
  private static final int length = 2;

  public ~@{Template}LsTcdField() {
    this(dftNm);
  }
  public ~@{Template}LsTcdField(~@{Template}LsTcdField fmEnum) {
    super(fmEnum);
  }
  public ~@{Template}LsTcdField(String fieldNm) {
    super(fieldNm, length, ~@{Template}LsTcd.CALC, ~@{Template}LsTcd.values());
  }
  public ~@{Template}LsTcdField copy() {
    return new ~@{Template}LsTcdField(this);
  }
}