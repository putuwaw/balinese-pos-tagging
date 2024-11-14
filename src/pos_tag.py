from typing import Optional


def pos_tagger(text: Optional[str]) -> Optional[str]:
    tag = [
        ("Adj", "#1E3A8A"),
        ("Adv", "#B91C1C"),
        ("Noun", "#065F46"),
        ("Verb", "#B45309"),
        ("PropN", "#6B21A8"),
        ("Pronoun", "#134E4A"),
        ("Num", "#4E362A"),
        ("Det", "#3A4F41"),
        ("Part", "#881337"),
        ("Prep", "#2F4F4F"),
    ]
    if text:
        result = []
        counter = 0
        for i in text.split():
            space = " "
            random_tag = tag[counter % 10]
            result.append((i,) + random_tag)
            result.append((space,))
            counter += 1
        return result
    return None


def stanford_formatter(pos_tag: list[tuple[str, str, str]]) -> str:
    if pos_tag:
        str_result = ""
        for item in pos_tag:
            word = item[0]
            if len(item) > 1:
                str_result += f"{item[0]}/{item[1].upper()}"
            else:
                str_result += word
        return str_result
    return None


def list_pos_tag() -> list[dict]:
    return list(
        [
            {
                "Tag": "Adj",
                "Description": "Adjective",
                "Example": "ageng, selem, manis",
            },
            {
                "Tag": "Adv",
                "Description": "Adverb",
                "Example": "teken, olih, lakar",
            },
            {
                "Tag": "Noun",
                "Description": "Noun",
                "Example": "baju, jaler, toko",
            },
            {
                "Tag": "Verb",
                "Description": "Verb",
                "Example": "meli, memunyi, mulih",
            },
            {
                "Tag": "PropN",
                "Description": "Proper noun",
                "Example": "Surabaya, Denpasar, Singaraja",
            },
            {
                "Tag": "Pronoun",
                "Description": "Pronoun",
                "Example": "tiang, ragane, cai, ento, ia, niki",
            },
            {
                "Tag": "Num",
                "Description": "Numeral",
                "Example": "abesik, dadua, seket, karo belah, 7916, 0,255",
            },
            {
                "Tag": "Det",
                "Description": "Determiner",
                "Example": "I, Ni, Ipun",
            },
            {
                "Tag": "Part",
                "Description": "Particle",
                "Example": "ja, ke, teh",
            },
            {
                "Tag": "Prep",
                "Description": "Preposition",
                "Example": "di, ka, uli, ring",
            },
        ],
    )
