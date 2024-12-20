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


def fix_page(page: list[str], rules: list[str]) -> list[str]:
    """Attempt to fix the page to the correct order. It may take multiple fixes!

    Args:
        page (list[str]): page numbers to check.
        rules (list[str]): all the rules to use to check ordering.

    Returns:
        (list[str]): The potentially corrected page.
    """
    for rule in rules:
        start, end = rule.split("|")
        if start in page and end in page:
            if page.index(start) > page.index(end):
                start_idx = page.index(start)
                end_idx = page.index(end)
                page[start_idx], page[end_idx] = page[end_idx], page[start_idx]

    return page


def read_input(filename: str = "input.txt") -> tuple[list[str], list[str]]:
    """Read the input and format to usable lists.

    Returns:
        tuple[list[str], list[str]]: rules and pages.
    """
    with open(filename) as f:
        rules, pages = f.read().split("\n\n")
        rules = rules.split("\n")
        pages = pages.split("\n")

    return rules, pages


def main() -> None:
    rules, pages = read_input()

    total = 0
    for page in pages:
        page = page.split(",")

        if check_page(page, rules) is False:
            fixed_page = fix_page(page, rules)
            fixed = check_page(fixed_page, rules)

            while fixed is False:
                fixed_page = fix_page(page, rules)
                fixed = check_page(page, rules)

            middle_number = len(page) // 2
            total += int(page[middle_number])

    print(f"The result is: {total}")


if __name__ == "__main__":
    main()
