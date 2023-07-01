from transliterate import translit


def transliterate_from_uk(text: str) -> str:
    return translit(text, "uk", reversed=True).lower().replace(" ", "-")
