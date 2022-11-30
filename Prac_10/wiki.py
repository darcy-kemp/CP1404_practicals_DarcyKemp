import wikipedia
search = input("search for:")
while search != '':
    try:
        page = wikipedia.page(search, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.DisambiguationError as results:
        print(results)

    search = input("search for:")
