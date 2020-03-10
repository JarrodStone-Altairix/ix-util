package com.altairix.comm.adf.~@{Template}.fields;

public class ~@{Template}UidField extends StringField  {

  public static final int length = 16;

  public ~@{Template}UidField(String fieldNm) {
    super(fieldNm, length);
  }
  public ~@{Template}UidField() {
    this("~@{Template}Uid");
  }
}