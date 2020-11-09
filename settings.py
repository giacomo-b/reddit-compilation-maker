topics = []

topics.append({
    "name":             "first_topic",
    "subreddits":       [ {"name":        "BetterEveryLoop", "sort": "top", "time": "month", "limit": 10},
                          {"name":      "interestingasfuck", "sort": "top", "time": "month", "limit": 10} ],
    "MAX_CLIP_TIME":    10 * 60.0,  # seconds
    "MAX_SUBCLIP_TIME": 10.0,       # seconds
})

topics.append({
    "name":             "second_topic",
    "subreddits":       [ {"name":      "AnimalsBeingJerks", "sort": "top", "time": "month", "limit": 10},
                          {"name":      "AnimalsBeingDerps", "sort": "top", "time": "month", "limit": 10} ],
    "MAX_CLIP_TIME":    10 * 60.0,  # seconds
    "MAX_SUBCLIP_TIME": 10.0,       # seconds
})