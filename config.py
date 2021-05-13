"""
配置文件
"""
# ----------全局配置----------
websites = ["csdn"]  # 同时发布到多个网站 csdn、简书、博客园等 目前只支持csdn

# ----------csdn相关配置----------
# 通过浏览器,打开发送博客的页面https://mp.csdn.net/mdeditor
# 然后F12,在network中的第一个页面中复制cookie

# csdn的cookies
cookie_string = """
uuid_tt_dd=10_18753605820-1613561954197-832330; dc_sid=ef7a92977e806f7dda0db91471d17344; c_segment=10; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_18753605820-1613561954197-832330!5744*1*xiligey1; _ga=GA1.2.764957593.1613641286; SESSION=a86ad45b-8ccc-48c5-b3cf-e6f9bd5be574; ssxmod_itna=YuDtBKDK0I4RxiwqBPeeunUjib+qQqi=iPTtGODlOotxA5D8D6DQeGTTupoTqoqepDh3hEjBB5LhoW1EOvqf4ff5KD=xYQDwxYoDUxGtDpxG6QqIDYALDY4DYDm3dDRKqB6XXxDPDgUVIY44DFXx0TDDy7sx0rD0nkDWnHDCKDEZc7fAKDWcckCt9F2lc1p1ypwx0CXx9FDB+NiQPeTnwxTDRWFA0DtWixq=xo44hYtB0x/GjqoC0D5YrK9t14MpecFYD===; ssxmod_itna2=YuDtBKDK0I4RxiwqBPeeunUjib+qQqi=iPTtGD6pFDtD0yio03PPcUXiouD6717KAeXj0L5AOFDZRhXmC3IjvYpP342y4pd3zQdi1NgKuvPRvVOZPNzhkw9yGO+YzlCBnBMzHghRYg5GupvO2cqhV=5+4UBzXQa+i35OO277Fb7HThyaCbIw=87hU2yQUZ5CGG0dfxPe68xhiccNkrGGYRuDtErjy7iUqeeYxPK+yDbXVZwTqr9NpIL2NbcQdy8ba1CFKHkbKuQBgf1UvEOjuYEk4LtnvdBU6TBajMdCyLWlvbIZERs/CTZnyDQPN7KzQviWY6b5W/5SCcMFB2tuqT57QcPp7P1H5xqeMv/j0Dse/QcO3rYw+lzqDLcO9cx74/7+8CwYbv8RytrYVYi3D07exDLxD2bGDD==; UserName=xiligey1; UserInfo=379c177ef8aa455caf408d825481c478; UserToken=379c177ef8aa455caf408d825481c478; UserNick=%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AE%B6%E4%BF%AE%E7%82%BC%E4%B9%8B%E9%81%93; AU=158; UN=xiligey1; BT=1614220136468; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22xiligey1%22%2C%22scope%22%3A1%7D%7D; __gads=ID=3510f0bec80eb447:T=1615345441:S=ALNI_Ma5M3383zt9iPfuD7XwBH9QY7zHQA; pluginUUID=10_29653129180-1615903734647-194638; pluginId=kfkdboecolemdjodhmhmcibjocfopejo; csrfToken=80G9zKifu0RDHSBvdgHguMBu; firstDie=1; aliyun_webUmidToken=T2gANkhUvnGNDhLQQ0b70HfFhiDHYfacm0P1UEynBYhWblM4-AosgCJATEvKuHzu4iA=; _gid=GA1.2.796804702.1618822508; c_first_ref=www.google.com.hk; c_first_page=https%3A//bbs.csdn.net/topics/200027775; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1618822561,1618822784,1618824184,1618824439; dc_session_id=10_1618829963535.413692; announcement-new=%7B%22isLogin%22%3Atrue%2C%22announcementUrl%22%3A%22https%3A%2F%2Fblog.csdn.net%2Fblogdevteam%2Farticle%2Fdetails%2F112280974%3Futm_source%3Dgonggao_0107%22%2C%22announcementCount%22%3A0%2C%22announcementExpire%22%3A3600000%7D; c_page_id=default; log_Id_view=609; log_Id_click=168; c_pref=https%3A//mall.csdn.net/vip%3Fspm%3D1018.2118.3001.4496; c_ref=https%3A//blog.csdn.net/%3Fspm%3D1008.2028.3001.4477; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1618830092; dc_tos=qrt5ak; log_Id_pv=377
"""
url = "https://mp.csdn.net/mdeditor/saveArticle"  # post到csdn的网址
# 默认博客信息
default_data = {
    "title": "Blog Title",  # 文章名
    "content": "<h1>hello, world</h1>",  # 博客内容
    "markdowncontent": '# hello, world~',  # 点击编辑博客后显示的markdown内容
    "categories": "默认分类",  # 分类
    "tags": "",  # 逗号隔开多个标签 如 "python,ml,svm"
    "channel": 28,  # 频道 可选1:移动开发、2:云计算大数据、3:研发管理、6:数据库、12:运维、14:前端、15:架构、16:编程语言、28:人工智能、29:物联网、30:游戏开发、31:后端、32:安全、33:程序人生、34:区块链、35:音视频开发、36:资讯、37:计算机理论与基础
    "articleedittype": "1",
    "type": "orginial",  # orginal原创，report转载，translated翻译
    "private": "0",  # 0公开 1私密
    "status": '0'
}

# ----------简书相关配置----------
