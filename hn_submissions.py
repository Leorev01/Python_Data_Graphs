from operator import itemgetter
import plotly.express as px

import requests

#Make an API call and check reponses
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Process information about each submission
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:5]:
	#Make a new API call for each submission
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()

	#Build a dictionary for each article.
	submission_dict = {
	'title':response_dict['title'],
	'hn_link':f"https://news.ycombinator.com/item?id={submission_id}",
	'comments':response_dict['descendants'],
	}
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
							reverse=True)

comments, title, hover_texts = [], [], []
for submission_dict in submission_dicts:
	print(f"\nTitle {submission_dict['title']}")
	print(f"Discussion link: {submission_dict['hn_link']}")
	print(f"Comments: {submission_dict['comments']}")
	comments.append(submission_dict['comments'])

	name = submission_dict['title']
	submission_url = submission_dict['hn_link']
	submission_link = f"<a href='{submission_url}'>{name}</a>"
	title.append(submission_link)

	hover_text = submission_dict['title']
	hover_texts.append(hover_text)

#Make a visualisation
main_title = "Most active discussions on Hacker News"
labels = {'x':'Discussions', 'y':'Number of comments'}
fig = px.bar(x = title, y = comments, title = main_title, labels = labels, hover_name = hover_texts,)
fig.update_layout(title_font_size = 28, xaxis_title_font_size = 20, yaxis_title_font_size = 20)
fig.update_traces(marker_color = 'SteelBlue', marker_opacity = 0.6)
fig.show()