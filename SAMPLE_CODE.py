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
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adpreview import AdPreview
from facebookads.api import FacebookAdsApi

access_token = 'EAAg7zM8m1wQBAJOYKZA6bFZC9ZCHxaZCbSNrEne9EeP0MAYvSbWxZCQVqZBGklMiWJczpP4ZBNnCcQWyaCjoXPMBt5QtlhLSwQ6zYOR3V9qG4MZBkmf0qI3AecaHnwekzP2ZBhL4SmrrXrhPPHcdRqJ5BceAPJslz0HwwgCkAtWPAGbElDaH0DcRNssPAYTTneqoZD'
ad_account_id = 'act_306011116959172'
app_secret = '4c1c34b9502793e4837a00f2a7b7f7aa'
page_id = '601550560344776'
app_id = '2317550648481540'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
    'objective': 'PAGE_LIKES',
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
    'image_url': 'http://www.facebookmarketingdevelopers.com/static/images/resource_1.jpg',
    'name': 'My Creative',
    'object_id': page_id,
    'title': 'My Page Like Ad',
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
)
)

