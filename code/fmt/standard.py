import ix.regex as ixre
import ix.config as ixcfg

# Check for appropriate whitespace after method invocation
def checkWhitespaceAfterMethod():
  ixre.findr(ixcfg.GitRepo, r"\.java", r"(?:(?:public|private|protected|final|abstract|static)\s+)+([\w\s\[\]<>]+)\w+\(\s*((?:[\w<>?]+\s+[\w<>?]+),?\s*)*\)\s*{\n.+\n(?!\s+})", \
    lambda m : False)

checkWhitespaceAfterMethod()