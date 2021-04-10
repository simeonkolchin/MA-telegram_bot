import wikipedia

wikipedia.set_lang('ru')

def search_wiki(word):
    print(word)
    try:
        w = wikipedia.search(word)
        if w:
            w2 = wikipedia.page(word).url
            # print(w2)
            w1 = wikipedia.summary(word)
            return w1, "\nСсылка: " + w2
        return "Запрос в википедии не найден", ""  # None
    except:
        return "Запрос в википедии не найден", ""  # None


if __name__ == '__main__':
    w = input()
    print(search_wiki(w))