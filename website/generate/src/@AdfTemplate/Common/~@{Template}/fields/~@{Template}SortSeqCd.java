package com.altairix.comm.adf.~@{Template}.fields

public enum ~@{Template}SortSeqCd implements HasEnumField<~@{Template}SortSeqCd> {

  CALC ("00", "Calculate Sort Sequence");
  private static final String CLASSNM = ~@{Template}SortSeqCd.class.getName();;
  private static final String CLASSNM_SIMPLE = ~@{Template}SortSeqCd.class.getSimpleName();;
  private static final Logger logger = LoggerFactory.getLogger(CLASSNM);;
  private final String desc;
  private final String value;

   ~@{Template}SortSeqCd(String value, String desc) {
    this.value = value;
    this.desc = desc;

  }
  public String getDesc() {
    return desc;
  }
  public String getString() {
    return value;
  }
  public ~@{Template}SortSeqCd toEnum(String enumString) {
    
    if (enumString == null) { 
      logger.error("Invalid value({}) for {}.toEnum()", enumString, CLASSNM);
      return null;
    }

    for (~@{Template}SortSeqCd enumVal : ~@{Template}SortSeqCd.values()) {
      if (enumVal.value.equals(enumString)) {
        return enumVal;
      }
    }

    return null;
  }
  public boolean isInstanceOf(Object testObj) {
    return testObj instanceof ~@{Template}SortSeqCd;
  }
  public boolean isSelectionValue(~@{Template}SortSeqCd tstEnum) {
    return false;
  }
  public String toString() {
    return CLASSNM_SIMPLE + "(" + value + ")";
  }
}