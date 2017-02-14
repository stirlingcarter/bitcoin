import praw

bot = praw.Reddit(user_agent='bitcoin_analyzer_bot v0.1',
                  client_id='daK9d_j__n9Grg',
                  client_secret='-NHpjhnETc0ey_o-36QdOJrnz00',
                  username='bitcoin_analyzer_bot',
                  password='carterperez')

bitcoin_sub = bot.subreddit('all')

bitcoin_sub_comments = bitcoin_sub.stream.comments()

for comment in bitcoin_sub_comments:
    text = comment.body
    if "right" in text:
            print(text)
            print("\n")
	

                            
