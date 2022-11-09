from tech_news.database import get_collection, find_news


# Requisito 10
def top_5_news():
    collection = get_collection()
    news = list(collection.find({}, {"_id": False}).sort(
        "comments_count", -1).limit(5))
    result = []
    if news == []:
        return []
    else:
        for new in news:
            new_tuple = (new["title"], new["url"])
            result.append(new_tuple)
        return result


def sorted_for_value(x, categories):
    new_categories = {}
    for category in sorted(categories, key=categories.get, reverse=True):
        new_categories[category] = categories[category]
    return new_categories


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = {}
    for new in news:
        if new["category"] not in categories:
            categories[new["category"]] = 1
        else:
            categories[new["category"]] += 1
    if len(categories) == 0:
        return []
    else:
        ordened = sorted(
            categories.items(), key=lambda item: item[0],
        )
        ordened.sort(key=lambda item: item[1], reverse=True)
        categories_sorted = []
        for item in ordened:
            categories_sorted.append(item[0])
        return categories_sorted
