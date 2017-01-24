import praw
import datetime
import tokens


class RedditBot:
	def __init__(self):
		self.r = praw.Reddit(client_id='1PaRsAq_XZjIkg',
			client_secret=tokens.redditSecret,
			username=tokens.redditUN,
			password=tokens.redditPW,
			user_agent='Reddit access for discord by /u/voice_of_the_machine')

	def test(self):
		print(self.r.user.me())

	def get_top_ten(self):
		new_posts = self.r.subreddit('criticalrole').new(limit=10)
		for new_post in new_posts:
			print(new_post.title)

	def get_rules(self):
		rules = self.r.subreddit('criticalrole').rules()
		print(rules)

	def get_time_till_cr(self, ts):
		# still needs work
		today = datetime.datetime.now()
		next_thurs = today + datetime.timedelta((3-today.weekday())%7)
		next_cr = next_thurs.replace(hour=22, minute=0, second=0, microsecond=0)
		r = next_cr - today
		hours = r.seconds // 3600
		minutes = (r.seconds % 3600) // 60
		seconds = r.seconds % 60
		rt = "Days: {0}. Hours: {1}. Minutes: {2}. Seconds: {3}".format(r.days, hours, minutes, seconds)
		print(rt)

if __name__ == '__main__':
	rb = RedditBot()
	rb.get_time_till_cr()
