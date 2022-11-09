from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    urls = selector.css(".entry-title a::attr(href)").getall()
    if len(urls) == 0:
        return []
    else:
        return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    button_next = selector.css(".next::attr(href)").get()
    if not button_next:
        return None
    else:
        return button_next


# Requisito 4
def title_structure(selector):
    suffix = " "
    title = selector.css(".entry-title::text").get()
    if title.endswith(suffix):
        title = title[:-len(suffix)]
        return title
    if "\xa0" in title:
        title = title.replace(u'\xa0', u'')
        return title
    else:
        return title


def url_structure(selector):
    url = selector.css("head link::attr(href)").getall()[2]
    if "amp" in url:
        url = url[:-len("amp/")]
        return url
    else:
        return url


def comments_structure(selector):
    comments = selector.css(".comment-list li").getall()
    if not comments:
        return 0
    else:
        comments = len(comments)
        return comments


def verify_em(selector, summary):
    link = selector.css(".entry-content p em").getall()
    text = selector.css(".entry-content p em::text").getall()
    for i in range(len(text)):
        summary = summary.replace(
            link[i],
            text[i])
    return summary


def verify_a(selector, summary):
    links = selector.css(".entry-content p a").getall()
    text = selector.css(".entry-content p a::text").getall()
    for i in range(len(text)):
        summary = summary.replace(
            links[i],
            text[i])
    return summary


def verify_a_with_em(selector, summary):
    links = selector.css(".entry-content p a").getall()
    texts = selector.css(".entry-content p a em::text").getall()
    for i in range(len(texts)):
        for j in range(len(links)):
            if texts[i] in links[j]:
                summary = summary.replace(
                        links[j],
                        texts[i])
    return summary


def verify_all_conditions(selector, summary):
    if "</a>" not in summary and "<strong>" not in summary and (
            "</em>" not in summary and "<br>" not in summary):
        summary = selector.css(".entry-content p::text").get()
        return summary
    else:
        return summary


def verify_strong_p_br(summary):
    if "<strong>" in summary:
        summary = summary.replace("<strong>", "")
        summary = summary.replace("</strong>", "")
    if "</p>" in summary:
        summary = summary.replace("<p>", "")
        summary = summary.replace("</p>", "")
    if "<br>" in summary:
        summary = summary.replace("<br>", "")
    return summary


def verify_suffix(summary):
    suffix = " "
    if "\xa0" in summary:
        summary = summary.replace(u'\xa0', u'')
        return summary
    if summary.endswith(suffix):
        summary = summary[:-len(suffix)]
        return summary
    else:
        return summary


def summary_structure(selector):
    summary = selector.css(".entry-content p").get()
    summary = verify_all_conditions(selector, summary)
    if "</em></a>" in summary:
        summary = verify_a_with_em(selector, summary)
    if "</a>" in summary:
        summary = verify_a(selector, summary)
    if "</em>" in summary:
        summary = verify_em(selector, summary)
    summary = verify_strong_p_br(summary)
    summary = verify_suffix(summary)
    return summary


def scrape_noticia(html_content):
    new = dict()
    selector = Selector(html_content)
    new["url"] = url_structure(selector)
    new["title"] = title_structure(selector)
    new["timestamp"] = selector.css(".meta-date::text").get()
    new["writer"] = selector.css(".author a::text").get()
    new["comments_count"] = comments_structure(selector)
    new["summary"] = summary_structure(selector)
    new["tags"] = selector.css(".post-tags ul li a::text").getall()
    new["category"] = selector.css(".label::text").get()
    return new


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
