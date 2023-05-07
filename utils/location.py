import requests
import os
import json

def get_address(lat, lng):
    url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x="+lng+"&y="+lat
    # 'KaKaoAK '는 그대로 두시고 개인키만 지우고 입력해 주세요.
    # ex) KakaoAK 6af8d4826f0e56c54bc794fa8a294
    headers = {'Authorization': f'KakaoAK {os.getenv("KAKAO_KEY")}'}
    api_json = requests.get(url, headers=headers)
    full_address = json.loads(api_json.text)


    return full_address