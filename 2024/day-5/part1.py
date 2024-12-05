def check_page(page: list[str], rules: list[str]) -> bool:
    """Check if the page is ordered correctly.

    Args:
        page (list[str]): page numbers to check.
        rules (list[str]): all the rules to use to check ordering.

    Returns:
        (bool): True if the page is in order, else False.
    """
    for rule in rules:
        start, end = rule.split("|")
        if start in page and end in page:
            if page.index(start) > page.index(end):
                return False

    return True


with open("input.txt") as f:
    rules, pages = f.read().split("\n\n")
    rules = rules.split("\n")
    pages = pages.split("\n")


total = 0
for page in pages:
    page = page.split(",")

    if check_page(page, rules):
        middle_number = len(page) // 2
        total += int(page[middle_number])

print(f"The result is: {total}")
