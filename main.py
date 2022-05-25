from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import random
import logging
import sys
import os
import logging.handlers


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
"""StreamHandler"""
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG) 
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
"""FileHandler"""
rotatingfile_handler = logging.handlers.RotatingFileHandler('main.log', backupCount=5, maxBytes=1073741824)
rotatingfile_handler.setLevel(logging.DEBUG)
rotatingfile_handler.setFormatter(formatter)
logger.addHandler(rotatingfile_handler)

    
logger.info("Main Intro")
try:
    if random.randrange(7) not in [0, 1] :
        logger.info('Choosed work')
        slpt =  random.randrange(60)*30 + random.randrange(60)
        logger.info('Sleeping random :' + str(slpt))
        # time.sleep(slpt)

        logger.info('Strarting')
        # set workspace folder at desired location (default is at your home folder)
        set_workspace(path=r"C:\Users\HP\Documents\repos\Instagram")

        # get an InstaPy session!
        session = InstaPy(username='nikoloztwildie',
                        password='Ej8n3ENTcV4FxPB',
                        browser_profile_path = r"C:\Users\HP\AppData\Roaming\Mozilla\Firefox\Profiles\7kueaqnc.default-release-1625420489216",
                        headless_browser=False)

        with smart_run(session):
            session.set_quota_supervisor(enabled=True,  # sleep_after = [],
                                    sleepyhead=True,
                                    stochastic_flow=True,
                                    notify_me=True,
                                    peak_likes_hourly=11,
                                    peak_likes_daily=55,
                                    peak_comments_hourly=4,
                                    peak_comments_daily=5,
                                    peak_follows_hourly=2,
                                    peak_follows_daily=10,
                                    peak_unfollows_hourly=35,
                                    peak_unfollows_daily=402,
                                    peak_server_calls_daily=422)
            
            session.set_skip_users(skip_private=False,
                            private_percentage=100,
                            skip_no_profile_pic=True,
                            no_profile_pic_percentage=100,
                            skip_business=True,
                            skip_non_business=False,
                            business_percentage=100,
                            skip_business_categories=[],
                            dont_skip_business_categories=[],
                            skip_bio_keyword=['Veriko khinkiladze', 'verro_kh'],
                            mandatory_bio_keywords=[])
            session.set_ignore_users(['verro_kh'])
            session.set_relationship_bounds(enabled=True,
                                        potency_ratio=-1.13,
                                        delimit_by_numbers=False,
                                        max_followers=8500,
                                        max_following=4490,
                                        min_followers=100,
                                        min_following=56,
                                        min_posts=1,
                                        max_posts=1000)


            friend_list = random.choices(session.grab_followers(username="nikoloztwildie", amount=15, live_match=False, store_locally=True), k=random.randint(2, 15))
                
            logger.info("<<<<<<< Friend List: " + str(friend_list) + ">>>>>>>>")
            session.set_user_interact(amount=3, randomize=True, percentage=83)
            crossroad = random.randrange(3)
            if crossroad == 0:
                logger.info("<<<<<<<<follow_user_followers>>>>>>>>")
                session.follow_user_followers(friend_list, amount=random.randrange(1, 20), randomize=True, sleep_delay=random.randrange(1200, 2400), interact=True)
            elif crossroad == 1:
                logger.info("<<<<<<<<follow_user_following>>>>>>>>")
                session.follow_user_following(friend_list, amount=random.randrange(1, 20), randomize=True, sleep_delay=random.randrange(1200, 2400), interact=True)
            
            elif crossroad == 2:
                logger.info("<<<<<<<<follow_likers>>>>>>>>")
                session.follow_likers(friend_list, photos_grab_amount = random.randrange(1,4), follow_likers_per_photo = random.randrange(1, 6), randomize=True, sleep_delay=random.randrange(1200, 2400), interact=True)

    else:
        logger.info('Choosed skip')
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    logger.exception(str(e))
    logger.exception([exc_type, fname, exc_tb.tb_lineno])

    


