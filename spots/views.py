from django.shortcuts import render


def home(request):
    return render(request, "spots/home.html")


def time(request):
    spot_type = request.GET.get("type")
    return render(request, "spots/time.html", {"spot_type": spot_type})


def budget(request):
    spot_type = request.GET.get("type")
    play_time = request.GET.get("time")

    return render(
        request,
        "spots/budget.html",
        {
            "spot_type": spot_type,
            "play_time": play_time,
        },
    )


def result(request):
    spot_type = request.GET.get("type")
    play_time = request.GET.get("time")

    if spot_type == "friend" and play_time == "night":
        spot = "美浜アメリカンビレッジ"
        image = "spots/images/mihama2.jpg"

    elif spot_type == "couple" and play_time == "night":
        spot = "瀬長島ウミカジテラス"
        image = "spots/images/umikazi.jpg"

    elif spot_type == "family" and play_time == "day":
        spot = "沖縄こどもの国"
        image = "spots/images/kodomo.jpg"

    elif spot_type == "solo" and play_time == "day":
        spot = "首里城"
        image = "spots/images/shuri.jpg"

    else:
        spot = "国際通り"
        image = "spots/images/kokusai.jpg"

    return render(
        request,
        "spots/result.html",
        {
            "spot": spot,
            "image": image,
        },
    )
