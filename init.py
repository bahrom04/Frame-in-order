import os
import re
import glob
import sqlite3

os.chdir("data")

eps = glob.glob("*.mp4")
fps = 1
os.mkdir("frames")
regx = re.compile(r"(?:.*)(?:s|season|)\s?(\d{1,2})\s?(?:e|x|episode|ep|\n)\s?(\d{1,2})", re.IGNORECASE)

for ep in eps:
    ep_regx = regx.match(ep)
    if ep_regx:
        season, episode = ep_regx.groups()
        out_path = f"./frames/S{season.zfill(2)}"
        if not os.path.isdir(out_path):
            os.mkdir(out_path)
        os.system(f'ffmpeg -i "{ep}" -vf "fps={fps},scale=640:360" {out_path}/{episode}x%d.jpg')

connection = sqlite3.connect("framedata.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE show (ep, frames)")
cursor.execute("CREATE TABLE frame_data (current_episode, last_frame)")
cursor.execute("INSERT INTO frame_data(current_episode, last_frame) VALUES (\"01x01\", 0)")
connection.commit()

total_seasons = int(season)
for n in range(total_seasons):
    current_season = str(n + 1).zfill(2)
    total_eps = len(glob.glob(f"./frames/S{current_season}/*x1.jpg"))
    for i in range(total_eps):
        current_ep = str(i + 1).zfill(2)
        frames = glob.glob(f"./frames/S{current_season}/{current_ep}x*.jpg")
        cursor.execute(f"INSERT INTO show (ep, frames) VALUES (\"{current_season}x{current_ep}\", {len(frames)})")
connection.commit()
