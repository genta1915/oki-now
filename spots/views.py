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

    elif spot_type == "couple" and play_time == "night":
        spot = "古宇利島"

    elif spot_type == "family" and play_time == "day":
        spot = "沖縄こどもの国"

    elif spot_type == "solo" and play_time == "day":
        spot = "首里城"

    else:
        spot = "国際通り"

    return render(request, "spots/result.html", {"spot": spot})
