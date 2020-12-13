import tweepy
auth = tweepy.OAuthHandler("API consumer key here",
                           "API consumer secret key here")
auth.set_access_token("acess token here",
                      "access token secret here")
api = tweepy.API(auth)
tweet = input("")
image = "a path in your computer to any image you want it to tweet"
api.update_with_media(image, tweet)
print("Successfully tweeted your image with caption:", tweet)
