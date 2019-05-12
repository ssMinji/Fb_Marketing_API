
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi
from facebookads.adobjects.adimage import AdImage

# 4. 광고 크리에이티브 제공 (광고 형식 디자인)
image = AdImage(parent_id='act_306011116959172')
image[AdImage.Field.filename] = './examples/test.png'
image.remote_create()

# Output image Hash
print(image[AdImage.Field.hash])

access_token = 'EAAg7zM8m1wQBAJk5CK770dtAxi4oiudZCNg7Rqj0fn4faKqL8SbSJYTWYfYrhZBctMBlT6A3kTQVJLcLVsWDf69TU0QcnL5vmygdoViZBTQGkC7U029JzOBmPi2YR7Thd46zon0OQHmaVHq01FgHCL2MxTW7SPEUMKMFhcqZBPN7iALMgKnD74lGCTGjGlUZD'
app_secret = '4c1c34b9502793e4837a00f2a7b7f7aa'
app_id = '2317550648481540'
id = 'act_306011116959172'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'Sample Creative',
  'object_story_spec': {'page_id':'<pageID>','link_data':{'image_hash':'<imageHash>','link':'https:\/\/facebook.com\/<pageID>','message':'try it out'}},
}
print(AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
))

