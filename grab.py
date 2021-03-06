from bs4 import BeautifulSoup
import requests

def grab_data():

    headers1 = {
        'authority': 'www.nytimes.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.nytimes.com/crosswords',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'b2b_cig_opt=^%^7B^%^22isCorpUser^%^22^%^3Afalse^%^7D; edu_cig_opt=^%^7B^%^22isEduUser^%^22^%^3Afalse^%^7D; _gcl_au=1.1.818975491.1626793453; nyt-a=p3rg3vhLES2zbogTDKGJ0yii; walley=GA1.2.1735091622.1626793454; walley_gid=GA1.2.86898706.1626793454; LPVID=Q2ZWE1MDJlNjgyMzA1N2Zm; LPSID-17743901=k9y0ZtLrRqOaYbS-ZUhivA; nyt-purr=cfhhcfhhhck; _cb_ls=1; _cb=B0se3tB8lZ6EBf7uS8; purr-cache=^<K0^<r^<C_^<G_^<S0; bluekai_uid_plugin=ora.odc_bluekaiIds_container_id,50134,ora.odc_bluekaiIds_bk_uuid,cCDgB9uB99Ye63jz,ora.odc_bluekaiIds_bk_uuid_noslash,cCDgB9uB99Ye63jz,ora.odc_source,bluekai; FPC=id=cd1968a3-8fd8-4626-a268-5e1b82cbaee1; __gads=ID=7746cfa06cd95a12:T=1626793699:S=ALNI_MZidf4GiUawnnsFSFMBJTrJqTL0tQ; SIDNY=CAgSJQjqzduHBhCmztuHBhoSMS0_3ZVQpBUngq5D2_yuSxJnIPaGqzEaQLa7FOsX5SrDzD82Y65W5OnvRpyXudxeafvu0qqWIVnp0Mp1hhbHX7nsC_wWCAv7v2ajzF0vRNTC4jWKCMEWsgE=; NYT-S=2gIRHKSUgsu0re39yTPEIVlJL6yAaV5uRHDvV8AUpHxGROmqxjDYTApuSWvA17gTRDjOoea6bgYnR8b6Mi.V.zFhzDqKkjEuv.mTGHe33Fxhv4c6RaME2u2pTZxWF35yTzfsw5KtrmFx0UpZZcwOatwmvh8QGEYAzHH0IRlcmR0y.3NLAE9vPXXMPSMHd2Ki2b; nyt-auth-method=sso; nyt-xwd-hashd=false; WTPERSIST=regi_id=103465846; nyt-gdpr=0; _cb_svref=https^%^3A^%^2F^%^2Fwww.nytimes.com^%^2Fcrosswords^%^2Fgame^%^2Fmini; RT=^\\^z=1&dm=nytimes.com&si=523508d1-a917-42ee-bfff-cb8603603bea&ss=krclpm0y&sl=1&tt=1jk&rl=1&ld=1jo&ul=660&hd=664^\\^; mnet_session_depth=5^%^7C1626818509428; nyt-jkidd=uid=103465846&lastRequest=1626818697700&activeDays=^%^5B0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C0^%^2C1^%^5D&adv=1&a7dv=1&a14dv=1&a21dv=1&lastKnownType=sub; _chartbeat2=.1557101001263.1626818696087.0000000000000001.D-qm7XC10NWsCDrqgMBXlEV7D5iM-R.6; iter_id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhaWQiOiI2MGY2ZTVmMTgwOTgxNzAwMDEyYTRiNmUiLCJjb21wYW55X2lkIjoiNWMwOThiM2QxNjU0YzEwMDAxMmM2OGY5IiwiaWF0IjoxNjI2ODE4Njk4fQ.jrgAuFYg1G0L8nilukJ_nf7Q5f96u6soponAAC_njeI; datadome=bFJiCeOQr9Bqi7wHy2F0M_Xo9IDRCkzBJ7q9FonTmkUjALW3T7eQPuwy_ncHwM3ru29uqTbt-I48IOCKWhG-4lLO4MKWxw0xwPwF16Fq2t',
    }

    response = requests.get('https://www.nytimes.com/puzzles/leaderboards', headers=headers1).text
    soup = BeautifulSoup(response, 'lxml')

    return soup


def get_date(soup):
    contents1 = []
    date_ = []

    for clss in soup.find('div', class_='lbd-board__header lbd-type__centered'):
      contents1.append(clss.contents)

    date_.append(contents1[2][0])

    return date_


def get_ranks(soup):

    leaderboard = soup.find('div', class_= 'lbd-board__items')

    ranks = []
    names = []
    times = []

    for rank in leaderboard:
        a = rank.find('p', class_='lbd-score__rank')
        b = rank.find('p', class_='lbd-score__name')
        c = rank.find('p', class_='lbd-score__time')

        ranks.append(a.contents)
        names.append(b.contents)
        times.append(c.contents)

    return ranks, names, times


def create_data(soup):
    date_ = get_date(soup)
    ranks, names, scores = get_ranks(soup)

    return date_, ranks, names, scores