from bot_class import Instagram_bot
from auth_data import username, password

my_bot = Instagram_bot(username,password)
my_bot.login()

my_bot.like_photo_by_hashtag('sketch')



my_bot.browser_close()





