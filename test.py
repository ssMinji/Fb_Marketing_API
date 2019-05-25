import sys
sys.path.append(r'C:\Anaconda3\Lib\site-packages') # Replace this with the place you installed facebookads using pip
sys.path.append(r'C:\Anaconda3\Lib\site-packages\facebook_business-3.0.0-py2.7.egg-info') # same as above

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adimage import AdImage

my_app_id = '2317550648481540'
my_app_secret = '4c1c34b9502793e4837a00f2a7b7f7aa'
page_id = '601550560344776'
my_access_token = 'EAAg7zM8m1wQBAO1qB31k7nrE3YpKZBuzobZA8ebzC2JNriCF5uKK6P8R6zc268N4CnZAdjHF88gUZCRLIyRwEqDZCAWA3GQw5Q8p0eQ4TpliBEsfZBZB1GLDpfXkSnDKZAYYiDXgZACp4IdrK6ZAUl9ieAyCM35pScFJEliEYiH8Q3oSKLqkkIPN1MVB7UE6RoLK8ZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_306011116959172')


fields = [
]
params = {
    'objective': 'PAGE_LIKES',
    'status': 'PAUSED',
    'buying_type': 'AUCTION',
    'name': 'My Campaign',
}
campaign = my_account.create_campaign(
    fields=fields,
    params=params,
)
print ('campaign', campaign)

campaign_id = campaign.get_id()
print ('campaign_id:', campaign_id, '\n')

fields = [
]
params = {
    'status': 'PAUSED',
    'targeting': {'geo_locations':{'countries':['US']}},
    'daily_budget': '1000',
    'billing_event': 'IMPRESSIONS',
    'bid_amount': '20',
    'campaign_id': campaign_id,
    'optimization_goal': 'PAGE_LIKES',
    'promoted_object': {'page_id': page_id},
    'name': 'My AdSet',
}
ad_set = my_account.create_ad_set(
    fields=fields,
    params=params,
)
print ('ad_set', ad_set)

ad_set_id = ad_set.get_id()
print ('ad_set_id:', ad_set_id, '\n')

# fields = [
# ]
# params = {
#     'body': 'Like My Page',
#     'image_url': 'https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-1/p32x32/13010641_580724558761933_1572200345389822918_n.jpg?_nc_cat=108&_nc_ht=scontent-icn1-1.xx&oh=05a6349127fbb53ecf18aa72292a06e5&oe=5D570D6C',
#     'name': 'My Creative',
#     'object_id': page_id,
#     'title': 'My Page Like Ad',
# }
# creative = my_account.create_ad_creative(
#     fields=fields,
#     params=params,
# )
# print ('creative', creative)

# creative_id = creative.get_id()
# print ('creative_id:', creative_id, '\n')





image = AdImage(parent_id='act_306011116959172')
image[AdImage.Field.filename] = 'sample.gif'
image.remote_create()

image_hash = image[AdImage.Field.hash]
# print(image)

fields = [
]
params = {
  'name': 'Like My Page',
  'object_story_spec': {'page_id':page_id,'link_data':{'image_hash':image_hash,'link':'https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-1/p32x32/13010641_580724558761933_1572200345389822918_n.jpg?_nc_cat=108&_nc_ht=scontent-icn1-1.xx&oh=05a6349127fbb53ecf18aa72292a06e5&oe=5D570D6C','message':'ENTER AD MESSAGE HERE'}},
}
adcreative = my_account.create_ad_creative(fields=fields, params=params)
print(adcreative)

# fields = [
# ]
# params = {
#   'name': 'ENTER AD NAME HERE',
#   'adset_id': adset['id'],
#   'creative': {'creative_id': adcreative['creative_id']},
#   'status': 'ACTIVE'
# }
# print(AdAccount(ad_account_id).create_ad(fields=fields, params=params))