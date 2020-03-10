import com.altairix.comm.adf.fieldtypes.EnumField;

public class ~@{Template}TcdField extends EnumField<~@{Template}Tcd>{

  public static final int            length            = 16;
  public static final String         dftNm             = "~@{template}Tcd";
  public static final boolean        dftAllowNullFg    = false;
  public static final ~@{Template}Tcd dftSelectionValue = ~@{Template}Tcd.ALL;
  public static final ~@{Template}Tcd nullValue         = ~@{Template}Tcd.NULL;

  public ~@{Template}TcdField() {
    this(dftNm);

  }
  public ~@{Template}TcdField(~@{Template}TcdField fmEnum) {
    super(fmEnum);
  }

  public ~@{Template}TcdField(boolean allowSelectionValuesFg) {
    this(allowSelectionValuesFg, dftAllowNullFg);
  }

  public ~@{Template}TcdField(boolean allowSelectionValuesFg, boolean allowNullFg) {
    this(allowSelectionValuesFg, allowNullFg, allowSelectionValuesFg ? dftSelectionValue: nullValue);
  }

  public ~@{Template}TcdField(boolean allowSelectionValuesFg, boolean allowNullFg,
      ~@{Template}Tcd dftVal) {

    this(dftNm, allowSelectionValuesFg, dftVal, allowNullFg);
  }

  public ~@{Template}TcdField(String fieldNm) {
    this(fieldNm, false, nullValue, dftAllowNullFg);
  }

  public ~@{Template}TcdField(String fieldNm, boolean allowSelectionValuesFg, ~@{Template}Tcd dftVal,
      boolean allowNullFg) {

    super(fieldNm, length, dftVal, nullValue, allowNullFg, ~@{Template}Tcd.values(), allowSelectionValuesFg);
  }

  @Override
  public ~@{Template}TcdField copy() { return new ~@{Template}TcdField(this); }
}
