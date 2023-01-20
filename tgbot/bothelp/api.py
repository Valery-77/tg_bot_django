import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api'

BOTHELP_TOKEN_URL = 'https://oauth.bothelp.io/oauth2/token'
BOTHELP_API_URL = 'https://api.bothelp.io/v1'
TOKEN_BODY = {'grant_type': 'client_credentials',
              'client_id': '249032:e3078a88587a7ad3b11549dcaf295dbf',
              'client_secret': '249032:33c1fcb51ba54644d6ec29cb3cf9e8f4'}


def get_bothelp_token():
    response = requests.post(url=BOTHELP_TOKEN_URL, data=TOKEN_BODY).text
    token = json.loads(response)
    return token


def get_bothelp_list(token):
    url = f'{BOTHELP_API_URL}/subscribers'
    header = {'Authorization': f'{token["token_type"]} {token["access_token"]}'}
    response = requests.get(url=url, headers=header)
    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        return False


def store_bothelp_todb(users_list):
    url = f'{BASE_URL}/bothelp-user'

    # for i in users_list:
    # print(i['utmCampaign'])
    i = users_list[0]
    # print(i)
    cut_list = {'subscribed': str(i['subscribed']), 'createdAt': str(i['createdAt']),
                'u_id': str(i['id']), 'channelName': i['channelName'],
                'channelType': i['channelType'], 'cuid': str(i['cuid']),
                'utmSource': i['utmSource'], 'utmTerm': i['utmTerm'],
                'utmContent': i['utmContent'], 'utmCampaign': i['utmCampaign'],
                'name': i['name'], 'phone': i['phone'], 'utmMedium': i['utmMedium'],
                'email': i['email']}
    # print(cut_list)
    res = requests.post(url=url, data=cut_list)
    print(res)


tkn = get_bothelp_token()
lst = get_bothelp_list(tkn)
store_bothelp_todb(lst)


# def create_user(registration, channel, user_id, username, first_name, last_name, email, mobile, link, utm_source,
#                 utm_campaign, utm_medium, utm_term, utm_content, last_visit):
#     url = f'{BASE_URL}/bot-user'
#     response = requests.get(url=url).text
#     data = json.loads(response)
#     user_exist = False
#     for i in data:
#         if i['user_id'] == user_id:
#             user_exist = True
#             break
#     if not user_exist:
#         requests.post(url=url, data={'registration': registration, 'channel': channel, 'user_id': user_id,
#                                      'username': username, 'first_name': first_name, 'last_name': last_name,
#                                      'email': email, 'mobile': mobile, 'link': link, 'utm_source': utm_source,
#                                      'utm_campaign': utm_campaign, 'utm_medium': utm_medium, 'utm_term': utm_term,
#                                      'utm_content': utm_content, 'last_visit': last_visit})
#         return f'User {username}(id:{user_id}) was added'
#     else:
#         return f'User {username} exist'

# now = datetime.date.today()
# print(
#     create_user(now, 'chl', 555, 'us_name', 'f_nm', 'l_nm', 'a@a.com', '333333', 'lnk', 'u_src', 'u_cm', 'u_md', 'u_t',
#                 'u_c', now)
# )
