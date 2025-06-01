def domain_name(url):
    if "/" in url:
        url = url.split("/")[2]

    return url
