import praw
from database import session, SentimentRecord 

# Replace these with your actual keys
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='MySentimentBot/1.0 by /u/AfraidHunter3837'
)

subreddit = reddit.subreddit('technology')

for submission in subreddit.hot(limit=5):
    new_record = SentimentRecord(raw_text=submission.title)
    session.add(new_record)
    print(f"Added: {submission.title}")

session.commit()
print("Data ingestion complete!")