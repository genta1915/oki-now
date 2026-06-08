from django.shortcuts import render


def home(request):
    return render(request, "spots/home.html")


def result(request):
    spot_type = request.GET.get("type")

    if spot_type == "friend":
        spot = "美浜アメリカンビレッジ"

    elif spot_type == "couple":
        spot = "古宇利島"

    elif spot_type == "family":
        spot = "沖縄こどもの国"

    elif spot_type == "solo":
        spot = "首里城"

    else:
        spot = "国際通り"

    return render(request, "spots/result.html", {"spot": spot})
