import praw

r = praw.Reddit(client_id='LUTuiUV3PF8ZPA', client_secret ='otUptMR7LT1lY990G2P-yNkH-sU', user_agent='RedditScraping', username="merleaux", password = 'hamps567')

#r.login('username', 'password')
subreddit = r.subreddit('pennystocks')

#put = 0
#call = 0

"""for aComment in subreddit.stream.comments():
    if "put" in aComment.body.lower():
        put = put + 1
        print("p: " + str(put)) 
        print("c: " + str(call))
        print('----')
        print(aComment.body)
    elif "call" in aComment.body.lower():
        call = call + 1
        print("p: " + str(put))
        print("c: " + str(call))
        print('----')
        print(aComment.body)

print("Puts" + put)
print("Calls" + call) """
tickers = []
for c in subreddit.stream.comments():
    wordList = c.body.split()
    for aValue in wordList:
        if aValue.isupper() and len(aValue) >=3 and len(aValue) <=4:
            print(aValue)
            tickers.append(aValue)
        #if word in c.body.lower():
            #if c.isupper() and c.len() >=3 and c.len() <= 4:
            #print(c.body)




top_posts = r.subreddit('pennystocks').top(limit=10)
for post in top_posts:
    print(post.title)