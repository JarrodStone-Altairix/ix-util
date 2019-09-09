import os
import json
import asyncio
from aiohttp_requests import requests
from ix.google_ext.google_client import Google_Client

dl_fmt = "https://docs.google.com/spreadsheets/d/" \
         "%s/gviz/tq?tqx=out:csv&sheet=%s"


def get_config():
  cfg_fp = open(os.path.join(os.path.dirname(__file__), "update_config.json"))
  cfg = json.load(cfg_fp)
  cfg_fp.close()
  return cfg


def get_sheet_info(srvc_drive, file_id):
  return srvc_drive.files().get(
      fileId=file_id, supportsTeamDrives=True).execute()


async def download_csv(file_id, sheet_name, auth_headers, dst_fp):
  uri = dl_fmt % (file_id, sheet_name)
  # print(uri)
  rsp = await requests.get(uri, headers=auth_headers)
  with open(dst_fp, "wb+") as dst_file:
    dst_file.write(await rsp.content.read())
    dst_file.close()


async def download_config(name, file_id, auth_headers, dst_dir):

  print(f"Starting {name}")
  # Download Question
  await download_csv(file_id, "Questions", auth_headers,
                     os.path.join(dst_dir, f"{name} - Questions.csv"))

  # Download Answers
  await download_csv(file_id, "Answers", auth_headers,
                     os.path.join(dst_dir, f"{name} - Answers.csv"))
  print(f"Update {name} complete")


async def update_config_coroutine(identities):
  # Setup
  cfg = get_config()
  client = Google_Client()
  srvc_drive = client.build_drive_service()
  auth_headers = client.get_auth_headers()
  coroutines = []

  print("Starting Config Update")
  if len(identities) == 1 and identities[0] == "*":
    for iden, (file_id, dst_dir) in cfg.items():
      name = get_sheet_info(srvc_drive, file_id)["name"]
      coroutines.append(download_config(name, file_id, auth_headers, dst_dir))
  else:
    for iden in identities:
      (file_id, dst_dir) = cfg[iden]
      name = get_sheet_info(srvc_drive, file_id)["name"]
      coroutines.append(download_config(name, file_id, auth_headers, dst_dir))

  await asyncio.gather(*coroutines)
  print("Config Update Complete")


if __name__ == "__main__":
  asyncio.run(update_config_coroutine(["*"]))
