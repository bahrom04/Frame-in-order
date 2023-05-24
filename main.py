import os
import dotenv
import tweepy
import sqlite3
import schedule

os.chdir("data")
dotenv.load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
handler = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(handler)
connection = sqlite3.connect("framedata.db")
cursor = connection.cursor()
show_name = "Wednesday"


def post_frames():
    iters = 5
    while iters > 0:
        current_ep = cursor.execute("SELECT current_episode FROM frame_data").fetchone()[0]
        ep_season, ep_num = current_ep.split("x")
        total_frames = cursor.execute(f"SELECT frames FROM show WHERE ep = \"{current_ep}\"").fetchone()[0]
        next_frame = cursor.execute("SELECT last_frame FROM frame_data").fetchone()[0] + 1

        if next_frame > total_frames:
            next_ep = str(int(ep_num) + 1).zfill(2)
            if os.path.isfile(f"./frames/S{ep_season}/{next_ep}x1.jpg"):
                cursor.execute(f'UPDATE frame_data SET current_episode = "{ep_season}x{next_ep}"')
                cursor.execute(f'UPDATE frame_data SET last_frame = 0')
                connection.commit()
                continue
            else:
                next_season = str(int(ep_season) + 1).zfill(2)
                cursor.execute(f'UPDATE frame_data SET current_episode = "{next_season}x01"')
                cursor.execute(f'UPDATE frame_data SET last_frame = 0')
                connection.commit()
                continue

        frame_path = f"./frames/S{ep_season}/{ep_num}x{next_frame}.jpg"
        msg = f"{show_name} - Season {ep_season} Episode {ep_num} - Frame {next_frame} Of {total_frames}"
        media = api.media_upload(frame_path)
        client.create_tweet(text=msg, media_ids=[media.media_id_string])
        cursor.execute(f"UPDATE frame_data SET last_frame = {next_frame}")
        connection.commit()
        iters -= 1


post_frames()
schedule.every(30).minutes.do(post_frames)
while True:
    schedule.run_pending()
