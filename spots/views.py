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
                "name": "知念岬公園",
                "image": "spots/images/tinen.jpg",
                "map_url": "https://maps.google.com/?q=知念岬公園",
                "description": "海風を感じながら、のんびり散歩や絶景を楽しめます。",
                "reason": "開放感あふれる景色で気分もリフレッシュ！ドライブの途中に立ち寄るのにもピッタリです。",
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
                "name": "エスティネート ラウンジ 那覇",
                "image": "spots/images/raunzi.jpg",
                "map_url": "https://maps.google.com/?q=エスティネート ラウンジ 那覇",
                "description": "沖縄の食材を使った「琉球メキシカン」かコンセプトのカフェ&レストランです。",
                "reason": "おしゃれな雰囲気で会話を楽しみながら、美味しい沖縄グルメを味わえるデートにもピッタリ！",
            },
            {
                "name": "カフェ サンフランシスコ",
                "image": "spots/images/sanfuransisuko.jpg",
                "map_url": "https://maps.google.com/?q=カフェサンフランシスコ",
                "description": "北カルフォルニアの雰囲気とオーシャンビューの絶景を楽しめる人気のカフェ&バーです。",
                "reason": "ビル最上階のテラス席から、アメリカンビレッジと沖縄の海を一望できます！",
            },
            {
                "name": "トランジット カフェ",
                "image": "spots/images/toranziltuto.jpg",
                "map_url": "https://maps.google.com/?q=トランジット カフェ",
                "description": "店内やテラス席からは、時間の移り変わりとともに変化する美しい海と空を眺めながら食事を楽しめます。",
                "reason": "海風を感じられるテラス席は、リゾート気分を味わえる人気スポットです！",
            },
        ]

    elif mood == "photo":
        spots = [
            {
                "name": "果報バンタ",
                "image": "spots/images/kafuubanta.jpg",
                "map_url": "https://maps.google.com/?q=果報バンタ",
                "description": "断崖絶壁の上から広がる絶景を楽しめて、青く輝く海と空を一望でき知る人ぞ知る沖縄屈指のビュースポットです。",
                "reason": "どこを切り取っても写真映え抜群！思い出に残る一枚を取りたい人にピッタリです。",
            },
            {
                "name": "伊計島",
                "image": "spots/images/ikei.jpg",
                "map_url": "https://maps.google.com/?q=伊計島",
                "description": "透明度抜群の海と自然に囲まれた、癒しの絶景スポット。のんびり過ごしたい日に最適です！",
                "reason": "海をバックに写真を撮れば映えること間違えなし！ドライブにもおすすめです。",
            },
            {
                "name": "浜辺の茶屋",
                "image": "spots/images/hamabe.jpg",
                "map_url": "https://maps.google.com/?q=浜辺の茶屋",
                "description": "海のすぐそばでゆっくり過ごせる人気カフェ。窓から見える青い海が、写真映えする癒し空間です。",
                "reason": "海を眺めながらカフェ時間を楽しめるのが魅力！沖縄らしい景色を満喫できます。",
            },
        ]

    elif mood == "active":
        spots = [
            {
                "name": "チームラボ学ぶ！未来の遊園地 沖縄",
                "image": "spots/images/rabo2.jpg",
                "map_url": "https://maps.google.com/?q=チームラボ学ぶ！未来の遊園地 沖縄",
                "description": "光と映像が広がる幻想的な空間で、体を動かしながら楽しめる体験型スポット。",
                "reason": "作品に触れて遊べる不思議な世界は、思わず夢中に！写真映えも抜群。",
            },
            {
                "name": "ケイブ オキナワ",
                "image": "spots/images/keibu.jpg",
                "map_url": "https://maps.google.com/?q=ケイブ オキナワ",
                "description": "足を踏み入れた瞬間から幻想的な世界が広がる、沖縄屈指の鍾乳洞スポット。",
                "reason": "まるで別世界に迷い込んだような空間で、ワクワクする探検気分を味わえる！",
            },
            {
                "name": "東南植物楽園",
                "image": "spots/images/tounan.jpg",
                "map_url": "https://maps.google.com/?q=東南植物楽園",
                "description": "南国ならではの植物や美しい景色が広がる、自然を満喫できる人気スポットです。",
                "reason": "昼は自然に癒され、夜は幻想的なイルミネーションで特別な時間を楽しめる！",
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
