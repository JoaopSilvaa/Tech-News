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
def scrape_noticia(html_content):
    new = dict()
    selector = Selector(html_content)
    suffix = ". "
    new["url"] = selector.css("head link::attr(href)").getall()[2]
    title = selector.css(".entry-title::text").get()
    if title.endswith(suffix):
        title = title[:-len(suffix)]
        new["title"] = title
    else:
        new["title"] = title
    new["timestamp"] = selector.css(".meta-date::text").get()
    new["writer"] = selector.css(".author a::text").get()
    new["comments_count"] = selector.css(".comment-list li").getall()
    if not new["comments_count"]:
        new["comments_count"] = 0
    else:
        new["comments_count"] = len(new["comments_count"])
    summary = selector.css(".entry-content p").get()
    if "</a>" not in summary and "<strong>" not in summary and (
            "</em>" not in summary):
        summary = selector.css(".entry-content p::text").get()
    if "</a>" in summary:
        if "</em>" in selector.css(".entry-content p a").get():
            link = selector.css(".entry-content p a").getall()
            text = selector.css(".entry-content p a em::text").getall()
            for i in range(len(text)):
                summary = summary.replace(
                    link[i],
                    text[i])
        else:
            link = selector.css(".entry-content p a").getall()
            text = selector.css(".entry-content p a::text").getall()
            for i in range(len(text)):
                summary = summary.replace(
                    link[i],
                    text[i])
    if "</em>" in summary:
        link = selector.css(".entry-content p em").getall()
        text = selector.css(".entry-content p em::text").getall()
        for i in range(len(text)):
            summary = summary.replace(
                link[i],
                text[i])
    if "<strong>" in summary:
        summary = summary.replace("<strong>", "")
        summary = summary.replace("</strong>", "")
    if "</p>" in summary:
        summary = summary.replace("<p>", "")
        summary = summary.replace("</p>", "")
    print(summary)
    if "\xa0" in summary:
        summary = summary.replace(u'\xa0', u'')
        new["summary"] = summary
    else:
        new["summary"] = summary
    new["tags"] = selector.css(".post-tags ul li a::text").getall()
    new["category"] = selector.css(".label::text").get()
    return new


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
