import requests

url =" https://api.vk.com/method/wall.getComments?owner_id=-153041894&post_id=156919&count=10&need_likes=1&preview_length=0&access_token=ab29852fe44a3d1edac474248bacac87f25f2b6e87fe7234762b696aa051b5370dc770270766315e05345&v=5.131"
# print(url)
req = requests.get(url)
src = req.json()
# print(src)
comments = src["response"]["items"]
# print(posts)
for comment in comments:
    print(comment["text"])