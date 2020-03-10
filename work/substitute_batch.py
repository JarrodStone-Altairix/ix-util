import ix.config as config
import ix.regex as ixre
from ix.code.template import substitute_multi_template

OUT_DIR = r"C:\Users\Jarrod\Downloads"
substitute_multi_template(
    "C:\\Users\\Jarrod\\Downloads",
    "ClocksAssess", "MentalMath",
    *ixre.findr(config.gitRepo(), r"ClocksAssess.+\.java"))
