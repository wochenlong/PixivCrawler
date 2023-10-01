import datetime


# NOTE: MODE_CONFIG only applies to ranking crawler
MODE_CONFIG = {
    # start date
    "START_DATE": datetime.date(2022, 9, 20),
    # date range: [start, start + range - 1]
    "RANGE": 1,
    # which ranking list
    "RANKING_MODES": [
        "daily",
        "weekly",
        "monthly",
        "male",
        "female",
        "daily_ai",
        "daily_r18",
        "weekly_r18",
        "male_r18",
        "female_r18",
        "daily_r18_ai",
    ],
    "MODE": "daily",  # choose from the above
    # illustration, manga, or both
    "CONTENT_MODES": ["all", "illust", "manga"],  # download both illustrations & mangas
    "CONTENT_MODE": "illust",  # choose from the above
    # download top x in each ranking
    #   suggested x be a multiple of 50
    "N_ARTWORK": 10,
}

OUTPUT_CONFIG = {
    # verbose / simplified output
    "VERBOSE": False,
    "PRINT_ERROR": False,
}

NETWORK_CONFIG = {
    # proxy setting
    #   you should customize your proxy setting accordingly
    #   default is for clash
    "PROXY": {"https": "127.0.0.1:7890"},
    # common request header
    "HEADER": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    },
}

USER_CONFIG = {
    # user id
    #   access your pixiv user profile to find this
    #   e.g. https://www.pixiv.net/users/xxxx
    "USER_ID": "99073368",
    "COOKIE": "first_visit_datetime_pc=2023-10-02%2000%3A50%3A38; p_ab_id=9; p_ab_id_2=7; p_ab_d_id=679286295; yuid_b=IVNBAhg; __utmc=235335808; __utmz=235335808.1696175441.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gid=GA1.2.2008332939.1696175442; PHPSESSID=99073368_A7jyrOBllgkoigx6XZCzdkx1CD7E4yzx; device_token=dc540340cd6c52b3d3cb05051d14a028; privacy_policy_agreement=6; c_type=24; privacy_policy_notification=0; a_type=0; b_type=1; _ga_MZ1NL4PHH0=GS1.1.1696175443.1.1.1696175479.0.0.0; _fbp=fb.1.1696175481260.1490758754; _im_vid=01HBNYZTZN06YTBZ6VAGKTNR0F; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; login_ever=yes; _gcl_au=1.1.1903931843.1696175488; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=99073368=1^9=p_ab_id=9=1^10=p_ab_id_2=7=1^11=lang=zh=1; __utma=235335808.1712504269.1696175441.1696175441.1696175585.2; cf_clearance=xkLdws3.R1x.IUKBveQL_ncU4p3B0ZjQ.1.dhozm7m0-1696179961-0-1-4f7748a4.c26679ac.18761744-0.2.1696179961; _ga=GA1.2.614556804.1696175442; __cf_bm=usCjj6g4VZDwu2czRkbEeeKzyPP_BXZxmFyaiHPQCU0-1696181285-0-ATd+FMmMUbkoSoT0JJ7hhQPg4JxcADhnqznSG2UdMtuH86lCaKvidZ+j9Z9XQ4B58cMzw5N9EGkOMxjxV2K/jfCNVIBqzfuWEoMr4UBlUA+R; __utmt=1; __utmb=235335808.10.10.1696175585; _ga_75BBYNYN9J=GS1.1.1696179935.2.1.1696182502.0.0.0",
}


DOWNLOAD_CONFIG = {
    # image save path
    #   NOTE: DO NOT miss "/"
    "STORE_PATH": "/root/img/xl/",
    # abort request / download
    #   after 10 unsuccessful attempts
    "N_TIMES": 10,
    # need tag ?
    "WITH_TAG": True,
    # waiting time (s) after failure
    "FAIL_DELAY": 1,
    # max parallel thread number
    "N_THREAD": 12,
    # waiting time (s) after thread start
    "THREAD_DELAY": 1,
}
