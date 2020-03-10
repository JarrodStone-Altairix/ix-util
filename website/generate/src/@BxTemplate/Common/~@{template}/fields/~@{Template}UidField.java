package com.arrowsmith.comm.brainex.~@{template}.fields;

import com.altairix.comm.adf.fieldtypes.StringField;

public class ~@{Template}UidField extends StringField  {

  public static final int length = 16;

  public ~@{Template}UidField(String fieldNm) {
    super(fieldNm, length);
  }
  public ~@{Template}UidField() {
    this("~@{Template}Uid");
  }
}