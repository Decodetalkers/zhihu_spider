'''
Get the message from zhihu
'''

import time
# import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
# import parsel
from scrapy.selector import Selector


def get_message(url: str, times: int, wordsa: str, wordsb: str, wordsc: str, wordsd: str):
    '''
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1;WOW64;rv:23.0)Gecko/20100101 Firefox/23.0'
    }
    '''
    CHAPTER_URL = url
    # req = urllib.request.Request(url=CHAPTER_URL, headers=headers)

    driver = webdriver.Firefox()
    driver.get(CHAPTER_URL)
    # time.sleep(30)
    driver.find_element(
            By.XPATH,
            '//button[@class="Button Modal-closeButton Button--plain"]'
            ).click()

    driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight+20);"
            )

    def execute_times(times):
        '''
        get the <p>
        '''
        for _ in range(times + 1):
            driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight+10);"
                    )
            time.sleep(5)

    execute_times(times)
    html = driver.page_source
    # html = urllib.request.urlopen(req).read().decode("utf8")
    # with open("./test.html", "r") as f:
    #     html = f.read()
    # print(html)
    # html = parsel.Selector(html)
    # print(html)
    selector = Selector(text=html)
    pages = selector.xpath('//div[@class="List"]')
    pages = pages.xpath('./div')[1].xpath('./div')[0].xpath(
        './div[@class="List-item"]'
    )
    COUT: int = 0
    content = []
    # HELP: int = 0
    # print(len((pages)))
    for each in pages[:-1]:
        # HELP = HELP+1
        # print(HELP)
        page = each.xpath(
                './div/div'
                )[1].xpath(
                    './div'
                    )[0].xpath(
                        './span/p'
                        ).extract()
        PAGE = str(page).replace(
                '\'<p>', ''
                ).replace(
                '</p>\',', '\n'
                ).replace(
                '\'', ''
                ).replace(
                '</p>', ''
                )
        if (wordsa in PAGE) or (wordsb in PAGE) or (wordsc in PAGE) or (wordsd in PAGE):
            COUT = COUT + 1
            # print(PAGE+'\n')
            content.append(PAGE+'\n\n')
    print("test")
    # print(str(COUT)+":"+str(len(pages)))
    return (content, str(COUT)+":"+str(len(pages)))
