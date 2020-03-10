package com.arrowsmith.sync.brainex.~@{Template}.obj;

import com.altairix.comm.adf.obj.BaseObject;
import com.altairix.comm.adf.obj.BaseObjectId;
import com.altairix.comm.adf.obj.ObjectFactory;

public class ~@{Template}SyncObjectFactory implements ObjectFactory {

  public BaseObject newBaseObject(BaseObjectId objId) {
    
  if (!objId.getObjectNameSpace().equals(~@{Template}Const.NMSPC)) { return null; }

  String objNm = objId.getObjectName();

	switch (objNm) {
      case ~@{Template}Provider.OBJNM: return new ~@{Template}Provider();
      default: return null;
	}  
  }
}