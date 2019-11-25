import os
import asyncio
from aiohttp_requests import requests
from ix.google_ext.google_client import Google_Client
from ix.web_assess.core import resolve_identities

dl_fmt = "https://docs.google.com/spreadsheets/d/" \
         "%s/export?format=csv&gid=%s"


def get_sheet_info(srvc_drive, file_id):
  return srvc_drive.files().get(
      fileId=file_id, supportsTeamDrives=True).execute()


async def download_csv(file_id, gid, auth_headers, dst_fp):
  uri = dl_fmt % (file_id, gid)
  # print(uri)
  rsp = await requests.get(uri, headers=auth_headers)
  with open(dst_fp, "wb+") as dst_file:
    dst_file.write(await rsp.content.read())
    dst_file.close()


async def download_config(name, file_id, gids, auth_headers, dst_dir):

  print(f"Starting {name}")
  # Download Question
  await download_csv(file_id, gids[0], auth_headers,
                     os.path.join(dst_dir, f"{name} - Questions.csv"))

  # Download Answers
  if gids[1]:
    await download_csv(file_id, gids[1], auth_headers,
                       os.path.join(dst_dir, f"{name} - Answers.csv"))
  print(f"Update {name} complete")


async def update_config_coroutine(identities):
  # Setup
  client = Google_Client()
  srvc_drive = client.build_drive_service()
  auth_headers = client.get_auth_headers()

  print("Starting Config Update")
  await asyncio.gather(*[
      download_config(
          get_sheet_info(srvc_drive, file_id)["name"],
          file_id, gids, auth_headers, dst_dir)
      for file_id, gids, dst_dir in resolve_identities(identities)])
  print("Config Update Complete")


if __name__ == "__main__":
  asyncio.run(update_config_coroutine(["*"]))
