

import sys
sys.path.append(r'c:\users\one\anaconda3\lib\site-packages') # Replace this with the place you installed facebookads using pip
sys.path.append(r'c:\users\one\anaconda3\lib\site-packages\curlify-2.1.1-py3.6.egg-info') # same as above

import datetime
from facebookads.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adcreative import AdCreative
from facebookads.adobjects.targetingsearch import TargetingSearch
from facebookads.adobjects.targeting import Targeting
from facebookads.adobjects.adimage import AdImage

my_app_id = '2317550648481540'
my_app_secret = '4c1c34b9502793e4837a00f2a7b7f7aa'
my_access_token = 'EAAg7zM8m1wQBAJk5CK770dtAxi4oiudZCNg7Rqj0fn4faKqL8SbSJYTWYfYrhZBctMBlT6A3kTQVJLcLVsWDf69TU0QcnL5vmygdoViZBTQGkC7U029JzOBmPi2YR7Thd46zon0OQHmaVHq01FgHCL2MxTW7SPEUMKMFhcqZBPN7iALMgKnD74lGCTGjGlUZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_306011116959172')
campaigns = my_account.get_campaigns()
print(campaigns)


# 1. 캠페인 만들기
fields = [
]
params = {
  'name': 'My campaign',  # 캠페인 제목
  'objective': 'LINK_CLICKS', # 광고 목표 설정 (링크 클릭)
  'status': 'PAUSED',  # 테스트동안 광고 비용이 청구되지 않도록 캠페인 일시 중단
}
print(AdAccount(id).create_campaign(
  fields=fields,
  params=params,
))

# 2. 타게팅 정의
params = {
    'q': 'baseball',
    'type': 'adinterest',
}

resp = TargetingSearch.search(params=params)
print(resp)

# 생성한 관심사 기반으로 샘플 타게팅 사양 만듦
targeting = {
    Targeting.Field.geo_locations: {
        Targeting.Field.countries: ['KOR'],
    },
    Targeting.Field.interests: 'baseball',
}

# 3. 예산, 청구, 최적화 및 기간 정의
today = datetime.date.today()
start_time = str(today + datetime.timedelta(weeks=1)) # 광고실행기간
end_time = str(today + datetime.timedelta(weeks=2))

adset = AdSet(parent_id='act_306011116959172')
adset.update({
    AdSet.Field.name: 'My Ad Set',
    AdSet.Field.campaign_id: 453840891825593,
    AdSet.Field.daily_budget: 1000,                      # 하루 지출하고자 하는 금액
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,    # 결제 기준
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,  # 광고를 통해 달성하고자 하는 결과
    AdSet.Field.bid_amount: 2,                           # 발생하는 최적화 이번트에 부여할 가치
    # AdSet.Field.targeting: <TARGETING>,
    AdSet.Field.start_time: start_time,
    AdSet.Field.end_time: end_time,
})

adset.remote_create(params={
    'status': AdSet.Status.paused,  # paused : 정지상태로 비용청구 방지
})



