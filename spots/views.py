from django.shortcuts import render


def home(request):
    return render(request, "spots/home.html")


def mood(request):
    spot_type = request.GET.get("type")
    return render(request, "spots/mood.html", {"spot_type": spot_type})


def time(request):
    spot_type = request.GET.get("type")
    mood = request.GET.get("mood")
    return render(
        request,
        "spots/time.html",
        {
            "spot_type": spot_type,
            "mood": mood,
        },
    )


def budget(request):
    spot_type = request.GET.get("type")
    play_time = request.GET.get("time")
    mood = request.GET.get("mood")

    return render(
        request,
        "spots/budget.html",
        {
            "spot_type": spot_type,
            "play_time": play_time,
            "mood": mood,
        },
    )


def result(request):
    spot_type = request.GET.get("type")
    play_time = request.GET.get("time")
    mood = request.GET.get("mood")

    if mood == "relax":
        spots = [
            {
                "name": "国際通り",
                "image": "spots/images/kokusai4.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
                "description": "沖縄最大の繁華街！  食べ歩きやショッピングを楽しめます。",
                "reason": "話題のお店や気になるお店を巡りながら、友達とワイワイ過ごせます！",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
                "description": "アメリカ西海岸の街並みが楽しめる人気観光スポットです。",
                "reason": "おしゃれな街並みで写真映えするため、友達との思い出作りにピッタリです！",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
                "description": "海を眺めながらカフェや、ショッピングを楽しめる絶景スポットです。",
                "reason": "海風を感じながらゆったり過ごせるため、沖縄らしい開放感を味わえます！",
            },
        ]

    elif mood == "drive":
        spots = [
            {
                "name": "海中道路",
                "image": "spots/images/kaityuu.jpg",
                "map_url": "https://maps.google.com/?q=海中道路",
                "description": "エメラルドグリーンの海の上を走れる、沖縄を代表する絶景ドライブコースです。",
                "reason": "綺麗な海を眺めながら、海の上を走れて爽快感を感じられます！",
            },
            {
                "name": "果報バンタ",
                "image": "spots/images/kafuubannta.jpg",
                "map_url": "https://maps.google.com/?q=果報バンタ",
                "description": "断崖絶壁の上から広がる絶景を楽しめて、青く輝く海と空を一望でき知る人ぞ知る沖縄屈指のビュースポットです。",
                "reason": "ドライブの途中に立ち寄るだけで、思わず見とれてしまう沖縄ならではの開放感を味わえます！",
            },
            {
                "name": "古宇利大橋",
                "image": "spots/images/kourioohasi.jpg",
                "map_url": "https://maps.google.com/?q=古宇利大橋",
                "description": "古宇利島へ続く絶景の橋で、沖縄らしい満喫できる人気スポットです。",
                "reason": "橋を渡る瞬間から非日常を感じられ、青く透き通る海に囲まれた景色が魅力的！",
            },
        ]

    elif mood == "food":
        spots = [
            {
                "name": "国際通りグルメ",
                "image": "spots/images/kokusaigurume.jpg",
                "map_url": "https://maps.google.com/?q=国際通りグルメ",
                "description": "",
                "reason": "",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
                "description": "",
                "reason": "",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
                "description": "",
                "reason": "",
            },
        ]

    elif mood == "photo":
        spots = [
            {
                "name": "アメリカンビレッジ",
                "image": "spots/images/amerikan.jpg",
                "map_url": "https://maps.google.com/?q=アメリカンビレッジ",
                "description": "",
                "reason": "",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
                "description": "",
                "reson": "",
            },
            {
                "name": "国際通り",
                "image": "spots/images/kokusai.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
                "description": "",
                "reason": "",
            },
        ]

    elif mood == "active":
        spots = [
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
                "description": "",
                "reason": "",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
                "description": "",
                "reason": "",
            },
            {
                "name": "国際通り",
                "image": "spots/images/kokusai2.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
                "description": "",
                "reason": "",
            },
        ]

    elif spot_type == "friend" and play_time == "night":
        spots = [
            {
                "name": "国際通り",
                "image": "spots/imaes/kokusai2.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
                "description": "",
                "reason": "",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
                "description": "",
                "reason": "",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
                "description": "",
                "reason": "",
            },
        ]

    elif spot_type == "couple" and play_time == "night":
        spots = [
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
                "description": "",
                "reson": "",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
                "description": "",
                "reason": "",
            },
            {
                "name": "国際通り",
                "image": "spots/images/kokusai2.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
                "description": "",
                "reason": "",
            },
        ]

    elif spot_type == "family" and play_time == "day":
        spots = [
            {
                "name": "沖縄こどもの国",
                "image": "spots/images/kodomo.jpg",
                "map_url": "https://maps.google.com/?q=沖縄こどもの国",
                "description": "",
                "reason": "",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
                "description": "",
                "reason": "",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
                "description": "",
                "reason": "",
            },
        ]

    elif spot_type == "solo" and play_time == "day":
        spots = [
            {
                "name": "首里城",
                "image": "spots/images/syuri.jpg",
                "map_url": "https://maps.google.com/?q=首里城",
                "description": "",
                "reason": "",
            },
            {
                "name": "国際通り",
                "image": "spots/images/kokusai.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
                "description": "",
                "reason": "",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
                "description": "",
                "reason": "",
            },
        ]

    else:
        spots = [
            {
                "name": "国際通り",
                "image": "spots/images/kokusai.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
                "description": "",
                "reason": "",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
                "description": "",
                "reason": "",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
                "description": "",
                "reason": "",
            },
        ]
    return render(
        request,
        "spots/result.html",
        {
            "spots": spots,
        },
    )
