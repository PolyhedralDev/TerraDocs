def h1(text: str) -> str:
    line = '=' * len(text)
    return '\n'.join([line, text, line])

def h2(text: str) -> str:
    return underline(text, '=')

def h3(text: str) -> str:
    return underline(text, '-')

def h4(text: str) -> str:
    return underline(text, '.')

def underline(text: str, char: str) -> str:
    line = char * len(text)
    return '\n'.join([text, line])

def indent(text: str, spaces: int) -> str:
    return " " * spaces + text

def wrap_in_card(lines: list[str],
                 title: str="",
                 link: str=None,
                 link_type: str=None,

) -> list[str]:
    header = f".. card:: {title}"
    if link:
        header += f"\n    :link: {link}"
    if link_type:
        header += f"\n    :link-type: {link_type}"
    return [header] + [indent(line, 4) for line in lines]

