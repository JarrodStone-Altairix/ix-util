import os
import json
from ix.git_ext.core import propagate_changes

_cfg_fd = open(os.path.join(
    os.path.dirname(__file__), "web_assess_config.json"))
_cfg = json.load(_cfg_fd)
_cfg_fd.close()


def resolve_identities(identities):
  if len(identities) == 1 and identities[0] == "*":
      return _cfg.values()
  elif len(identities) == 1 and identities[0] == "qol":
    identities = [
        "anger", "anxiety", "attention", "behaviour", "communication",
        "completion", "depression", "executive", "extremity", "fatigue",
        "general", "grief", "headache", "independence", "intro", "memory",
        "mobility", "pain", "participation", "resilience", "satisfaction",
        "self-esteem", "stigma", "well-being"]

  return [_cfg[iden] for iden in identities]


def propagate_upstream():
  branches = ["webAssess-audio", "webAssess-help", "webAssess-clocks"]

  for src, dst in zip(branches, branches[1:]):
    # print(f"Propagating {src} into {dst}")
    propagate_changes(src, dst, False)
