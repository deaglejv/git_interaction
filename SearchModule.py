import requests


def get_number_of_items_on_first_page(per_page):
    """
    Makes a call to GitHub to search the repositories for a passed number of results per page and returns the count.


    :param per_page: How many results should be printed per page
    :return: Number of items that are in the response.
    """
    search_params = {"q": "test", "per_page": per_page}
    resp = requests.get(url="https://api.github.com/search/repositories", params=search_params)
    return len(resp.json()["items"])


def verify_first_five_pages_contain_results_with_stars_greater_than(stargazers):
    """
    This function makes a call with a variation of the search parameters that includes looking at the number
    of stars a repository has.  It looks at several pages to make sure the counts are consistent through
    the first 5 pages.  Pages start at index 1.

    :param stargazers: Number of stars the repository should have at least.
    :return:
    """
    per_page = 25
    for page_num in range(1, 6):
        search_params = {"q": "test+stars:>{}".format(stargazers), "page": page_num, "per_page": per_page}
        resp = requests.get(url="https://api.github.com/search/repositories", params=search_params)
        if len([item for item in resp.json()["items"] if item["stargazers_count"] > stargazers]) != per_page:
            AssertionError("Not all items have greater than {} stars\nItems: {}".format(stargazers, resp.json()))
