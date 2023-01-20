import requests
import json

# import datetime

BASE_URL = 'http://127.0.0.1:8000/api'


def create_user(registration, channel, user_id, username, first_name, last_name, email, mobile, link, utm_source,
                utm_campaign, utm_medium, utm_term, utm_content, last_visit):
    url = f'{BASE_URL}/bot-user'
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i['user_id'] == user_id:
            user_exist = True
            break
    if not user_exist:
        requests.post(url=url, data={'registration': registration, 'channel': channel, 'user_id': user_id,
                                     'username': username, 'first_name': first_name, 'last_name': last_name,
                                     'email': email, 'mobile': mobile, 'link': link, 'utm_source': utm_source,
                                     'utm_campaign': utm_campaign, 'utm_medium': utm_medium, 'utm_term': utm_term,
                                     'utm_content': utm_content, 'last_visit': last_visit})
        return f'User {username}(id:{user_id}) was added'
    else:
        return f'User {username} exist'


# now = datetime.date.today()
# print(
#     create_user(now, 'chl', 55775, 'us_name', 'f_nm', 'l_nm', 'a@a.com', '333333', 'lnk', 'u_src', 'u_cm', 'u_md', 'u_t',
#                 'u_c', now)
# )
