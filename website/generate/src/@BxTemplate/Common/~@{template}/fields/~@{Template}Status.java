package com.arrowsmith.comm.brainex.~@{template}.fields;

import com.altairix.comm.adf.fieldtypes.DataStructure;
import com.altairix.comm.adf.fieldtypes.StringField;
import com.altairix.comm.adf.fieldtypes.TimestampField;
import com.arrowsmith.comm.brainex.fields.~@{Template}UidField;

public class ~@{Template}Status extends DataStructure  {

  public static final String OBJNM = "~@{Template}Status";
  public static final String OBJDESC = "~@{Template} Status Structure";
  public final StringField lastSysId = addField(new StringField("lastSysId", 32));
  public final StringField lastUser = addField(new StringField("lastUser", 32));
  public final TimestampField lastTstp = addField(new TimestampField("lastTstp"));
  public final ~@{Template}UidField ~@{Template}Uid = addField(new ~@{Template}UidField());

  public ~@{Template}Status() {
    super(OBJNM, OBJDESC);
  }
}