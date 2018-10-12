# -*- coding: utf-8 -*-
#
#
import random,requests

def validate(raw_proxy):
    webs = ['http://vip.win0168.com/AsianOdds_n.aspx?id=1631903',
            'http://vip.win0168.com/1x2/oddslist/1630835.htm',
            'http://vip.win0168.com/1x2/oddslist/1631698.htm',
            'http://info.win0168.com/analysis/1630837sb.htm']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    try:
        r = requests.get(random.choice(webs),
                         proxies={'http': 'http://'+raw_proxy}, timeout=2, allow_redirects=False, headers=headers)
    except:
        return False
    if r.status_code == 200:
        return True
    else:
        return False