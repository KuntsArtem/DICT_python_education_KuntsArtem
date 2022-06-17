import json
import requests
from bs4 import BeautifulSoup
import string
import pickle
import os
import shutil


def url_test_imdb():
    url = input("Enter your URL >")
    if url.startswith('https://www.imdb.com/title/'):
        return url
    print("Your URL must starts with 'https://www.imdb.com/title/'")
    url_test_imdb()


def number_test():
    user_input = input("Please enter a number of pages >")
    while True:
        try:
            number = int(user_input)
            return number
        except ValueError:
            user_input = input(string)
            print("Please input integer number")



def url_test():
   url = input("Enter your URL >")
   if url.startswith('http://') or url.startswith('https://'):
       return url
   print("Your URL must starts with 'http://' or 'https://'")
   url_test()


def content_parse():
   url = url_test()
   res = requests.get(url)
   if res.status_code == 200:
       content = res.json()
       print(content.get('content'))
   else:
       print("Invalid quote resource!")


def movie_parse():
   url = url_test_imdb(string)
   res = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
   if res.ok:
       try:
           html = res.text
           soup = BeautifulSoup(html, 'html.parser')
           title = soup.h1.string
           description = soup.find('meta', {'name': 'description'})
           if not title or not description:
               raise AttributeError()
           film_info = {"title": title, "description": description["content"]}
           print(film_info)
       except AttributeError:
           print("Invalid  IMDB movie page!")
       else:
           print("Invalid quote resource!")


class Parser:

    def __init__(self, page = int, article_type = str):
        self.page_counter = page
        self.article = article_type
        self.take_links()

    def article_parse(self, links_array):
        for a in links_array:
            res = requests.get(a, headers={"Accept-Language": "en-US,en;q=0.5"})
            soup = BeautifulSoup(res.text, "html.parser")
            header = soup.find(class_="c-article-title").text
            header = header.strip().replace(" ", "_")
            text = soup.find("div", class_="c-article-section__content").find_all("p")
            with open(r"Folder_" + str(self.page_counter) + "/" + header + ".txt", "w", encoding="utf-8") as x:
                for i in text:
                    x.write(i.text)

    def preview_parse(self, links_array):
        for a in links_array:
            res = requests.get(a, headers={"Accept-Language": "en-US,en;q=0.5"})
            soup = BeautifulSoup(res.text, "html.parser")
            header = soup.find(class_="c-article-magazine-title").text
            header = header.strip().replace(" ", "_")
            text = soup.find("p", class_="articlepreview_parse")
            with open(r"Folder_" + str(self.page_counter) + "/" + header + ".txt", "w", encoding="utf-8") as x:
                for i in text:
                    x.write(i.text)

    def journal_parse(self, links_array):
        for a in links_array:
            res = requests.get(a, headers={"Accept-Language": "en-US,en;q=0.5"})
            soup = BeautifulSoup(res.text, "html.parser")
            try:
                header = soup.find(class_="c-article-magazine-title").text
                header = header.strip().replace(" ", "_")
            except AttributeError:
                try:
                    header = soup.find(class_="Theme-StoryTitle Theme-textize-small h-align-right").text
                    header = header.strip().replace(" ", "_")
                except AttributeError:
                    header = soup.find(class_="Theme-StoryTitle Theme-textize-xsmall")
            text = (soup.find("div", class_="c-article-body u-clearfix")).find_all("p")
            with open(f"Folder_" + str(self.page_counter) + "/" + header + ".txt", "w", encoding="utf-8") as x:
                for i in text:
                    x.write(i.text)

    def take_links(self):
        res = requests.get("https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=" + str(self.page_counter), headers={"Accept-Language": "en-US,en;q=0.5"})
        soup = BeautifulSoup(res.text, "html.parser")
        href = soup.find_all("a", class_="c-card__link u-link-inherit")
        types = soup.find_all("span", class_="c-meta__type")
        urls = ["https://www.nature.com" + str(j["href"]) for j in href]
        links_array = [urls[i] for i in range(len(urls)) if types[i].string == self.article]
        article_list = ("Article", "Author Correction", "Matters Arising", "Publisher Correction")
        journal_list = ("Career Column", "Career Feature", "Comment", "Editorial", "Futures", "Nature Briefing", "Nature Podcast", "News", "News Feature", "Outlook", "Where I Work", "World View")
        preview_list = ("Correspondence", "News & Views", "Research Briefing")
        if self.article in article_list:
            self.article_parse(links_array)
        if self.article in preview_list:
            self.preview_parse(links_array)
        if self.article in journal_list:
            self.preview_parse(links_array)

while True:
    article = input("Enter article type >")
    try:
        pages = int(input("Enter how many pages to search >"))
        break
    except ValueError:
        print("Please, print NUMBER of pages")
for i in range(1, pages + 1):
    if os.path.exists("Folder_" + str(i)):
        shutil.rmtree("Folder_" + str(i))
        os.mkdir("Folder_" + str(i))
        pars = Parser(i, article)
    else:
        os.mkdir("Folder_" + str(i))
        pars = Parser(i, article)
print("Saved all article")




