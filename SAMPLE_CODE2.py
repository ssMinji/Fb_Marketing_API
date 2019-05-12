# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.customaudience import CustomAudience
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adpreview import AdPreview
from facebookads.api import FacebookAdsApi

access_token = 'EAAg7zM8m1wQBAJk5CK770dtAxi4oiudZCNg7Rqj0fn4faKqL8SbSJYTWYfYrhZBctMBlT6A3kTQVJLcLVsWDf69TU0QcnL5vmygdoViZBTQGkC7U029JzOBmPi2YR7Thd46zon0OQHmaVHq01FgHCL2MxTW7SPEUMKMFhcqZBPN7iALMgKnD74lGCTGjGlUZD'
app_secret = '4c1c34b9502793e4837a00f2a7b7f7aa'
ad_account_id = 'act_306011116959172'
audience_name = 'myclients'
audience_retention_days = '30'
pixel_id = '568800453628699'
app_id = '2317550648481540'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
    'objective': 'LINK_CLICKS',
    'status': 'PAUSED',
    'buying_type': 'AUCTION',
    'name': 'My Campaign',
}
campaign = AdAccount(ad_account_id).create_campaign(
    fields=fields,
    params=params,
)
print('campaign', campaign)

campaign_id = campaign.get_id()
print('campaign_id:', campaign_id, '\n')

fields = [
]
params = {
    'name': audience_name,
    'pixel_id': pixel_id,
    'prefill': true,
    'rule': {'url':{'i_contains':''}},
    'subtype': 'WEBSITE',
    'retention_days': audience_retention_days,
}
custom_audience = AdAccount(ad_account_id).create_custom_audience(
    fields=fields,
    params=params,
)
print('custom_audience', custom_audience)

custom_audience_id = custom_audience.get_id()
print('custom_audience_id:', custom_audience_id, '\n')

fields = [
]
params = {
    'status': 'PAUSED',
    'targeting': {'custom_audiences':[{'id':custom_audience_id}], 'geo_locations':{'countries':['US']}},
    'name': 'My AdSet',
    'billing_event': 'IMPRESSIONS',
    'bid_amount': '20',
    'campaign_id': campaign_id,
    'optimization_goal': 'REACH',
    'daily_budget': '1000',
}
ad_set = AdAccount(ad_account_id).create_ad_set(
    fields=fields,
    params=params,
)
print('ad_set', ad_set)

ad_set_id = ad_set.get_id()
print('ad_set_id:', ad_set_id, '\n')

fields = [
]
params = {
    'body': 'Like My Page',
    'name': 'My Creative',
    'title': 'My Page Like Ad',
    'object_url': 'www.facebook.com',
    'link_url': 'www.facebook.com',
    'image_url': 'http://www.facebookmarketingdevelopers.com/static/images/resource_1.jpg',
}
creative = AdAccount(ad_account_id).create_ad_creative(
    fields=fields,
    params=params,
)
print('creative', creative)

creative_id = creative.get_id()
print('creative_id:', creative_id, '\n')

fields = [
]
params = {
    'status': 'PAUSED',
    'adset_id': ad_set_id,
    'name': 'My Ad',
    'creative': {'creative_id':creative_id},
}
ad = AdAccount(ad_account_id).create_ad(
    fields=fields,
    params=params,
)
print('ad', ad)

ad_id = ad.get_id()
print('ad_id:', ad_id, '\n')

fields = [
]
params = {
    'ad_format': 'DESKTOP_FEED_STANDARD',
}
print(Ad(ad_id).get_previews(
    fields=fields,
    params=params,
))

