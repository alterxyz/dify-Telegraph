from ytelegraph import TelegraphAPI

ph = TelegraphAPI("1467d9f07393dc3f144ae6538d79a2c49214cc1e8bba2856123a30288233")
content = "# Hello, Telegraph!\n\nThis is my first Telegraph page using YTelegraph."
ph_link = ph.create_page_md("My First Page", content)
print(f"Your page is live at: {ph_link}")