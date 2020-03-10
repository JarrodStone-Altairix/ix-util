import com.altairix.comm.adf.fieldtypes.HasEnumField;
import com.altairix.comm.adf.root.log.Logger;
import com.altairix.comm.adf.root.log.LoggerFactory;

public enum ~@{Template}Tcd implements HasEnumField<~@{Template}Tcd> {

  ALL ("*", "ALL"),
  NULL ("@", "NULL");

  private static final String CLASSNM = ~@{Template}Tcd.class.getName();
  private static final String CLASSNM_SIMPLE = ~@{Template}Tcd.class.getSimpleName();
  private static final Logger logger  = LoggerFactory.getLogger(CLASSNM);

  private final String desc;
  private final String value;

  ~@{Template}Tcd(String value, String desc) {
    this.value = value;
    this.desc  = desc;
  }

  @Override
  public String getDesc() {
    return desc;
  }

  @Override
  public String getString() {
    return value;
  }

  @Override
  public boolean isInstanceOf(Object testValue) {
    return testValue instanceof ~@{Template}Tcd;
  }

  @Override
  public boolean isSelectionValue(~@{Template}Tcd tstEnum) {
    return tstEnum == ALL;
  }

  @Override
  public ~@{Template}Tcd toEnum(String enumString) {

    if (enumString != null) {
      for (~@{Template}Tcd enumVal: ~@{Template}Tcd.values()) {
        if (enumVal.value.equals(enumString)) {
          return enumVal;
        }
      }
    }

    logger.error("Invalid value({}) for {}.toEnum()", enumString, CLASSNM);

    return null;
  }

  @Override
  public String toString() {
    return CLASSNM_SIMPLE + "(" + value + ")";
  }
}