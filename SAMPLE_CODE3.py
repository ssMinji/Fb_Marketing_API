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
from facebookads.adobjects.adsinsights import AdsInsights
from facebookads.api import FacebookAdsApi

access_token = 'EAAg7zM8m1wQBAO1qB31k7nrE3YpKZBuzobZA8ebzC2JNriCF5uKK6P8R6zc268N4CnZAdjHF88gUZCRLIyRwEqDZCAWA3GQw5Q8p0eQ4TpliBEsfZBZB1GLDpfXkSnDKZAYYiDXgZACp4IdrK6ZAUl9ieAyCM35pScFJEliEYiH8Q3oSKLqkkIPN1MVB7UE6RoLK8ZD'
ad_account_id = 'act_306011116959172'
app_secret = '4c1c34b9502793e4837a00f2a7b7f7aa'
app_id = '2317550648481540'
FacebookAdsApi.init(access_token=access_token)

fields = [
    'results',
    'result_rate',
    'reach',
    'frequency',
    'impressions',
    'delivery',
    'relevance_score:score',
    'spend',
    'impressions_gross',
    'impressions_auto_refresh',
    'cost_per_result',
    'cpp',
    'cpm',
    'optimization_results',
    'cost_per_optimization_result',
    'last_significant_edit',
]
params = {
    'level': 'campaign',
    'filtering': [],
    'breakdowns': ['gender'],
    'time_range': {'since':'2019-04-13','until':'2019-05-13'},
}
print(AdAccount(ad_account_id).get_insights(
    fields=fields,
    params=params,
))


