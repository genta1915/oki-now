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
                "image": "spots/images/kokusai2.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
                "description": "沖縄最大の繁華街！  食べ歩きやショッピングを楽しめます。",
                "reason": "友達同士でも気軽に楽しめる沖縄定番スポットだからです。",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
                "description": "アメリカ西海岸の街並みが楽しめる人気観光スポットです。",
                "reason": "おしゃれな街並みで写真映えするため、友達との思い出作りにピッタリです。",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
                "description": "海を眺めながらカフェや、ショッピングを楽しめる絶景スポットです！",
                "reason": "海風を感じながらゆったり過ごせるため、沖縄らしい開放感を味わえるからです。",
            },
        ]

    elif mood == "drive":
        spots = [
            {
                "name": "海中道路",
                "image": "spots/images/kaityuu.jpg",
                "map_url": "https://maps.google.com/?q=海中道路",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
            },
        ]

    elif mood == "food":
        spots = [
            {
                "name": "国際通りグルメ",
                "image": "spots/images/kokusaigurume.jpg",
                "map_url": "https://maps.google.com/?q=国際通りグルメ",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
            },
        ]

    elif mood == "photo":
        spots = [
            {
                "name": "アメリカンビレッジ",
                "image": "spots/images/amerikan.jpg",
                "map_url": "https://maps.google.com/?q=アメリカンビレッジ",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
            },
            {
                "name": "国際通り",
                "image": "spots/images/kokusai.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
            },
        ]

    elif mood == "active":
        spots = [
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
            },
            {
                "name": "国際通り",
                "image": "spots/images/kokusai2.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
            },
        ]

    elif spot_type == "friend" and play_time == "night":
        spots = [
            {
                "name": "国際通り",
                "image": "spots/imaes/kokusai2.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
            },
        ]

    elif spot_type == "couple" and play_time == "night":
        spots = [
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
            },
            {
                "name": "国際通り",
                "image": "spots/images/kokusai2.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
            },
        ]

    elif spot_type == "family" and play_time == "day":
        spots = [
            {
                "name": "沖縄こどもの国",
                "image": "spots/images/kodomo.jpg",
                "map_url": "https://maps.google.com/?q=沖縄こどもの国",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
            },
        ]

    elif spot_type == "solo" and play_time == "day":
        spots = [
            {
                "name": "首里城",
                "image": "spots/images/syuri.jpg",
                "map_url": "https://maps.google.com/?q=首里城",
            },
            {
                "name": "国際通り",
                "image": "spots/images/kokusai.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
            },
        ]

    else:
        spots = [
            {
                "name": "国際通り",
                "image": "spots/images/kokusai.jpg",
                "map_url": "https://maps.google.com/?q=国際通り",
            },
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
                "map_url": "https://maps.google.com/?q=美浜アメリカンビレッジ",
            },
            {
                "name": "瀬長島ウミカジテラス",
                "image": "spots/images/umikazi.jpg",
                "map_url": "https://maps.google.com/?q=瀬長島ウミカジテラス",
            },
        ]
    return render(
        request,
        "spots/result.html",
        {
            "spots": spots,
        },
    )
