def response(phrase):
    match phrase.strip():
        case "":
            return "Fine. Be that way!"
        case p if p.isupper() and p.endswith("?"):
            return "Calm down, I know what I'm doing!"
        case p if p.isupper():
            return "Whoa, chill out!"
        case p if p.endswith("?"):
            return "Sure."
        case _:
            return "Whatever."
