import os # noqa
import re # noqa
import ix.fs as ixfs # noqa
import ix.code.template as ixtempate # noqa
import ix.config as config # noqa
import ix.regex as ixre # noqa
import ix.code.tcd as ixtcd # noqa
import ix.code.package as ixpkg # noqa
import ix.code.builder as ixbuilder # noqa
import ix.code.service.call as ixsrvc # noqa
import ix.parse.ixjson as ixjson # noqa
import ix.parse.gae as ixgae # noqa

# ixfs.cleanBldDir()

# ixre.findr(r"C:\\", r"\.vrapperrc", None)
# ixre.findr(config.gitRepo(), r"\.vimrc", None)
# ixre.findr(config.gitRepo(), r"\.java", r"hAudio")
ixre.findr(r"C:\Python", r"\.py$", r"subkv\(")

# ixre.subr(config.BxGWT, r"\.java", r"TEMPLATE", r"~@{TEMPLATE}")
# ixre.subfr(config.BxTemplateDir, r"\.java", r"Template", r"~@{Template}")

# ixpkg.createAdfPackage("WebAssess")
# ixpkg.createBxPackage("Contact")

# print(ixpkg.createLoadCommand("QolCompositeQnaireData"))
# print(ixpkg.createPackageData("Qol"))
# ixpkg.createArrayList("Resource", "ResourceEntry")
# ixpkg.createTcd("AdfQSessionStage")

# ixsrvc.createAdfService("Resource", "loadAudio", "AudioSet")
# ixsrvc.createBxService("QQuestion", "loadQuestion", None)


# RoleTcd cleanup
# ixre.findr(config.bxGWT(), r"\.java", r"RoleTcd\s+\w+\s+=", print=None)
# ixre.findr(config.bxGWT(), r"\.java", r"RoleTcd\s+\w+\s*;", print=None)
# ixre.findr(config.bxGWT(), r"\.java", r"RoleTcdField\s+\w+\s*=", print=None)

# ixgae.read_log(r"C:\Users\Jarrod\Downloads\log.json", (""))
