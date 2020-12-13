import tweepy
auth = tweepy.OAuthHandler("API CONSUMER KEY HERE",
                           "API CONSUMER SECRET KEY HERE")
auth.set_access_token("ACCESS TOKEN HERE",
                      "ACCESS TOKEN SECRET HERE")
api = tweepy.API(auth)
tweet = input("")
api.update_status(status=(tweet))
print("Successfully tweeted with caption:", tweet)
