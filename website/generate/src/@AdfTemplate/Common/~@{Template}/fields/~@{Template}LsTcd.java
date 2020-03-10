package com.altairix.comm.adf.~@{Template}.fields

public enum ~@{Template}LsTcd implements HasEnumField<~@{Template}LsTcd> {

  LONG ("01", "Long"),
  SHORT ("02", "Short");
  private static final String CLASSNM = ~@{Template}LsTcd.class.getName();;
  private static final String CLASSNM_SIMPLE = ~@{Template}LsTcd.class.getSimpleName();;
  private static final Logger logger = LoggerFactory.getLogger(CLASSNM);;
  private final String desc;
  private final String value;

   ~@{Template}LsTcd(String value, String desc) {
    this.value = value;
    this.desc = desc;

  }
  public String getDesc() {
    return desc;
  }
  public String getString() {
    return value;
  }
  public ~@{Template}LsTcd toEnum(String enumString) {
    
    if (enumString == null) { 
      logger.error("Invalid value({}) for {}.toEnum()", enumString, CLASSNM);
      return null;
    }

    for (~@{Template}LsTcd enumVal : ~@{Template}LsTcd.values()) {
      if (enumVal.value.equals(enumString)) {
        return enumVal;
      }
    }

    return null;
  }
  public boolean isInstanceOf(Object testObj) {
    return testObj instanceof ~@{Template}LsTcd;
  }
  public boolean isSelectionValue(~@{Template}LsTcd tstEnum) {
    return false;
  }
  public String toString() {
    return CLASSNM_SIMPLE + "(" + value + ")";
  }
}