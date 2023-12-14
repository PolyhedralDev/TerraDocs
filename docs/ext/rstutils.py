import re

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

def interpreted(text: str) -> str:
    return f"`{text}`"

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

sep = "---------"

def bullet(text: str) -> str:
    return f"- {text}"

def bullet_lines(lines: list[str]) -> list[str]:
    return [ bullet(line) if i == 0 else indent(line, 2) for (i, line) in enumerate(lines) ]

def ref(ref: str, text: str=None) -> str:
    if text:
        text_escaped = re.sub(r"[<>]", lambda match: "\\" + match.group(0), text)
        return f":ref:`{text_escaped} <{ref}>`"
    else:
        return f":ref:`{ref}`"

def bold(text: str) -> str:
    return f"**{text}**"