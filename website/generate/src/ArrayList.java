@SuppressWarnings("serial")
public class ~@{Template}ArrayList extends ObjectArrayList<~@{Object}> {

  private static final String CLASSNM = ~@{Template}ArrayList.class.getName();
  private static final String CLASSNM_SIMPLE = ~@{Template}ArrayList.class.getSimpleName();

  private static final Logger logger = LoggerFactory.getLogger(CLASSNM);

  public ~@{Template}ArrayList() {
    this(CLASSNM_SIMPLE);
  }

  public ~@{Template}ArrayList(String listNm) {
    super(listNm, null);
  }

  @Override
  public void copyObjects(ObjectArrayList<?> fmObjectArrayLs) {

    // Check for nulls
    if (fmObjectArrayLs == null) {
      throw new RuntimeException(logger.error(
          "Attempt to copy null ObjectArrayList to {}({})", CLASSNM_SIMPLE, getListName())) ;
    }

    // Check ObjectArrayList type
    if (!(fmObjectArrayLs instanceof ~@{Template}ArrayList)) {
      throw new RuntimeException(logger.error(LogObj.toArray(fmObjectArrayLs),
          "Attempt to copy {} to {}({})", new Object[] {
              fmObjectArrayLs.getListName(), CLASSNM_SIMPLE, getListName() } ));
    }

    clear();

    addAll((~@{Template}ArrayList) fmObjectArrayLs);
  }
}
