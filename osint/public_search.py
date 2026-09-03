from urllib.parse import quote


def build_searches(phone, name=None):
    searches = []

    queries = [
        ("Google", f'"{phone}"'),
        ("Bing", f'"{phone}"'),
        ("GitHub Code", f'"{phone}"'),
    ]

    if name:
        queries.extend([
            ("Google Name", f'"{name}"'),
            ("Bing Name", f'"{name}"'),
        ])

    for source, query in queries:
        encoded = quote(query)

        if source.startswith("Google"):
            url = f"https://www.google.com/search?q={encoded}"

        elif source.startswith("Bing"):
            url = f"https://www.bing.com/search?q={encoded}"

        else:
            url = (
                f"https://github.com/search"
                f"?q={encoded}&type=code"
            )

        searches.append({
            "source": source,
            "query": query,
            "url": url
        })

    return searches
