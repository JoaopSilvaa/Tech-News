from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    if news == []:
        return []
    else:
        for new in news:
            new_tuple = (new["title"], new["url"])
            result.append(new_tuple)
        return result


# Requisito 7
def search_by_date(date):
    format_date = date[8:] + "/" + date[5:7] + "/" + date[:4]
    try:
        format = "%Y-%m-%d"
        datetime.datetime.strptime(date, format)
        news = search_news({"timestamp": format_date})
        result = []
        if news == []:
            return []
        else:
            for new in news:
                new_tuple = (new["title"], new["url"])
                result.append(new_tuple)
            return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
