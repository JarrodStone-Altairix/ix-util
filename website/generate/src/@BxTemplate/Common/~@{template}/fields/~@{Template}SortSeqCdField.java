package com.arrowsmith.comm.brainex.~@{template}.fields;

import com.altairix.comm.adf.fieldtypes.EnumField;
import com.altairix.comm.adf.root.log.LoggerFactory;
import com.arrowsmith.comm.brainex.~@{template}.fields.~@{Tempalte}SortSeqCd;

public class ~@{Template}SortSeqCdField extends EnumField<~@{Template}SortSeqCd>  {

  private static final String dftNm = "~@{Template}SortSeqCdField";
  private static final int length = 2;

  public ~@{Template}SortSeqCdField() {
    this(dftNm);
  }
  public ~@{Template}SortSeqCdField(~@{Template}SortSeqCdField fmEnum) {
    super(fmEnum);
  }
  public ~@{Template}SortSeqCdField(String fieldNm) {
    super(fieldNm, length, ~@{Template}SortSeqCd.CALC, ~@{Template}SortSeqCd.values());
  }
  public ~@{Template}SortSeqCdField copy() {
    return new ~@{Template}SortSeqCdField(this);
  }
}