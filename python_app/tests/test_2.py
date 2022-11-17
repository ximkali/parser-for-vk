import configparser 

param = config = configparser.ConfigParser()


src = {
    "response": [
        {
            "id": 1,
            "city": {
                "id": 2,
                "title": "Санкт-Петербург"
            },
            "country": {
                "id": 1,
                "title": "Россия"
            },
            "name": "ВКонтакте API",
                    "screen_name": "apiclub",
                    "is_closed": 0,
                    "type": "group",
                    "photo_50": "https://sun7-8.userapi.com/s/v1/if1/04SDm6iX9Lb6SbdbdrfonC3AYNYcmeITh7qA2hWfqZHsm8Vzg1eAgFgEXj5r9hnX4tJGjxxh.jpg?size=50x50&quality=96&crop=20,20,560,560&ava=1",
                    "photo_100": "https://sun7-8.userapi.com/s/v1/if1/-KtBexxCseHjbF2KHkGe39sIKDnFws1s2jZGoSyu6VVi60svhEBzHdFpxtSTMVnSjHhc_x0h.jpg?size=100x100&quality=96&crop=20,20,560,560&ava=1",
                    "photo_200": "https://sun7-8.userapi.com/s/v1/if1/VzUDrhCC83ylOGINHBFS2Cy3ctu2s6mXr4KwuS_sEXNN0AJwoyrxRwHtFomuX6h9NALKDx0F.jpg?size=200x200&quality=96&crop=20,20,560,560&ava=1"
        },
        {
            "id": 55293029,
            "name": "moment of",
                    "screen_name": "mntof",
                    "is_closed": 0,
                    "type": "page",
                    "photo_50": "https://sun7-6.userapi.com/s/v1/if2/GWnbhXc4icRkSrQsTYaCF8h552qJpNdzDa-YLFqR5xB2b4whiO2VbVVYTLERFAvs0JViW2fEFVmbrNakAb0QzGxv.jpg?size=50x50&quality=96&crop=0,57,786,786&ava=1",
                    "photo_100": "https://sun7-6.userapi.com/s/v1/if2/xwX2Nh1Jot73-Xj5lawzd5ceqHcnyWeAsuwfgleAmd3Z5jQgXHM9AY_G60xKAoR4RxBeBwMIb6zuQPWwxCiE0Qqb.jpg?size=100x100&quality=96&crop=0,57,786,786&ava=1",
                    "photo_200": "https://sun7-6.userapi.com/s/v1/if2/nsE6ukOkD-fz3gNKwyLqIJ2KUscoCDk0435eS9N3zcbenXkyk0x4l3vjO44czQYNez13l7jqWV3r4-u_jNeEMBva.jpg?size=200x200&quality=96&crop=0,57,786,786&ava=1"
        },
        {
            "id": 1192207,
            "city": {
                "id": 125,
                "title": "Саратов"
            },
            "country": {
                "id": 1,
                "title": "Россия"
            },
            "name": "ЮрФак СГУ",
                    "screen_name": "urfak_sgu",
                    "is_closed": 0,
                    "type": "group",
                    "photo_50": "https://sun7-9.userapi.com/s/v1/if2/BGQIJPaOYbl4xlOovT0lkkH6BqPbFbRtYmXcUD5yf3jTzMFHero1Usf_tlhPsoxuj9fdNCa4FdSUmQuk9G63et-P.jpg?size=50x50&quality=96&crop=0,0,591,591&ava=1",
                    "photo_100": "https://sun7-9.userapi.com/s/v1/if2/TQbpXMMQJRV99vtON-yFC4G5wph4o1Fpge8BUzkuZDDp1lgEDZExeMQmYAbP3_Sz7tmqpShgpFQcZIINFkcl_-Fo.jpg?size=100x100&quality=96&crop=0,0,591,591&ava=1",
                    "photo_200": "https://sun7-9.userapi.com/s/v1/if2/Nn_zVxB1meHKVzcSD1RJsEBMvofKba66Ny25t2vDF8vkR5PnfY-exYVpfUKLfcBQc3i4Q5aZ7rF0-3avViLRy9Yk.jpg?size=200x200&quality=96&crop=0,0,591,591&ava=1"
        }
    ]
}


for x in src["response"]:
    try:
        print(x['id'], x['name'], x["screen_name"],x['city']["title"],x['country']["title"])
    except:
        print(x['id'], x['name'], x["screen_name"])
        continue



while True:
    config.read('conf/config.ini')
    filds = ''
    fild = input()    
    match fild:
        case'ac':
            param = config.get('sub_info','activity')
            filds = ''
            filds.join(param)
        case'ad':
            param = config.get('sub_info','addresses')
            filds = ''
            filds.join(param)
        case'ag':
            param = config.get('sub_info','age_limits')
            filds.join(param)
        case'ci':
            param = config.get('sub_info','city')
            filds.join(param)
        case'con':
            param = config.get('sub_info','contacts')
            filds.join(param)
        case'cou':
            param = config.get('sub_info','country')
            filds.join(param)
        case'des':
            param = config.get('sub_info','description')
            filds.join(param)
        case'mem':
            param = config.get('sub_info','members_count')
            filds.join(param)
        case'exit':
            break 
print(filds)


