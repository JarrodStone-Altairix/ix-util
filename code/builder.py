import ix.const as const
import ix.code.java as java


# String, Optional String, String[](a,b), String[](a,b,c)
def generate(className, base, reqArgs, optArgs):
  # Write the class
  javaClass = java.Class("public", className)

  if base is not None and len(base) > 0:
    javaClass.setBaseClass(base)

  # Builder static method
  bldrNm = f"{className}Builder"
  javaBuildClass = java.Class("public static", bldrNm)
  javaClass.addNestedClass(javaBuildClass)
  javaBuildCnstr = java.Method("public", None, bldrNm, "")
  javaClassCnstr = java.Method(
      "protected", None, className,
      f"{const.TODO_Impl}\n").addArgument(bldrNm, "builder")

  # Builder required arguments
  for argT, name in reqArgs:
    javaBuildClass.addField(java.Field("private", argT, name))
    javaBuildCnstr.addArgument(argT, name)
    javaBuildCnstr.body += f"this.{name} = {name};"

    javaClass.addField(java.Field("private final", argT, name))
    javaClassCnstr.body += f"    this.{name} = builder.{name};\n"

  javaBuildClass.addMethod(javaBuildCnstr)

  # Builder optional arguments
  for argT, name, defVal in optArgs:
    Name = name[:1].upper() + name[1:]
    javaBuildClass.addField(java.Field("private", argT, name, defVal))
    javaBuildClass.addMethod(
        java.Method(
            "public", bldrNm, f"set{Name}",
            f"""this.{name} = {name};\n    return this;""").addArgument(argT,
                                                                        name))

    javaClass.addField(java.Field("private final", argT, name))
    javaClassCnstr.body += f"    this.{name} = builder.{name};\n"

  javaBuildClass.addMethod(java.Method("public", className, "build",
                                       f"return new {className}(this);"))
  javaClass.addMethod(javaClassCnstr)
  return javaClass
