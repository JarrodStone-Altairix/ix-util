package com.arrowsmith.comm.brainex.~@{template}.obj;

public class ~@{Template}CommonObjectFactory implements ObjectFactory {

  public BaseObject newBaseObject(BaseObjectId objId) {
    
  if (!objId.getObjectNameSpace().equals(~@{Template}Const.NMSPC)) { return null; }

  BaseObject obj = null;
  String objNm = objId.getObjectName();

  if      (objNm.equals(~@{Template}Select.OBJNM))   obj = new ~@{Template}Select();
  else if (objNm.equals(~@{Template}Control.OBJNM))  obj = new ~@{Template}Control();
  else if (objNm.equals(~@{Template}Long.OBJNM))     obj = new ~@{Template}Long();
  else if (objNm.equals(~@{Template}Short.OBJNM))    obj = new ~@{Template}Short();
  else if (objNm.equals(~@{Template}Prologue.OBJNM)) obj = new ~@{Template}Prologue();

  return obj;
  
  }
}