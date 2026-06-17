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
            {"name": "国際通り", "image": "spots/images/kokusai2.jpg"},
            {"name": "美浜アメリカンビレッジ", "image": "spots/images/mihama2.jpg"},
            {"name": "瀬長島ウミカジテラス", "image": "spots/images/umikazi.jpg"},
        ]

    elif mood == "drive":
        spots = [
            {"name": "海中道路", "image": "spots/images/kaityuu.jpg"},
            {"name": "瀬長島ウミカジテラス", "image": "spots/images/umikazi.jpg"},
            {"name": "美浜アメリカンビレッジ", "image": "spots/images/mihama2.jpg"},
        ]

    elif mood == "food":
        spots = [
            {"name": "国際通りグルメ", "image": "spots/images/kokusaigurume.jpg"},
            {"name": "瀬長島ウミカジテラス", "image": "spots/images/umikazi.jpg"},
            {
                "name": "美浜アメリカンビレッジ",
                "image": "spots/images/mihama2.jpg",
            },
        ]

    elif mood == "photo":
        spots = [
            {"name": "アメリカンビレッジ", "image": "spots/images/amerikan.jpg"},
            {"name": "瀬長島ウミカジテラス", "image": "spots/images/umikazi.jpg"},
            {"name": "国際通り", "image": "spots/images/kokusai.jpg"},
        ]

    elif mood == "active":
        spots = [
            {"name": "瀬長島ウミカジテラス", "image": "spots/images/umikazi.jpg"},
            {"name": "美浜アメリカンビレッジ", "image": "spots/images/mihama2.jpg"},
            {"name": "国際通り", "image": "spots/images/kokusai2.jpg"},
        ]

    elif spot_type == "friend" and play_time == "night":
        spots = [
            {"name": "国際通り", "image": "spots/imaes/kokusai2.jpg"},
            {"name": "美浜アメリカンビレッジ", "image": "spots/images/mihama2.jpg"},
            {"name": "瀬長島ウミカジテラス", "image": "spots/images/umikazi.jpg"},
        ]

    elif spot_type == "couple" and play_time == "night":
        spots = [
            {"name": "瀬長島ウミカジテラス", "image": "spots/images/umikazi.jpg"},
            {"name": "美浜アメリカンビレッジ", "image": "spots/images/mihama2.jpg"},
            {"name": "国際通り", "image": "spots/images/kokusai2.jpg"},
        ]

    elif spot_type == "family" and play_time == "day":
        spots = [
            {"name": "沖縄こどもの国", "image": "spots/images/kodomo.jpg"},
            {"name": "美浜アメリカンビレッジ", "image": "spots/images/mihama.jpg"},
            {"name": "瀬長島ウミカジテラス", "image": "spots/images/umikazi.jpg"},
        ]

    elif spot_type == "solo" and play_time == "day":
        spots = [
            {"name": "首里城", "image": "spots/images/syuri.jpg"},
            {"name": "国際通り", "image": "spots/images/kokusai.jpg"},
            {"name": "美浜アメリカンビレッジ", "image": "spots/images/mihama.jpg"},
        ]

    else:
        spots = [
            {"name": "国際通り", "image": "spots/images/kokusai.jpg"},
            {"name": "美浜アメリカンビレッジ", "image": "spots*images/mihama2.jpg"},
            {"name": "瀬長島ウミカジテラス", "image": "spots/images/umikazi.jpg"},
        ]
    return render(
        request,
        "spots/result.html",
        {
            "spots": spots,
        },
    )
