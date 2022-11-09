from tech_news.database import get_collection


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


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
