from typing import Optional
import pickle

with open("best_crf_model.pkl", "rb") as model_file:
    crf_model = pickle.load(model_file)

def prepare_input(text: str) -> list:
    words = text.split()
    return [extract_features(words, i) for i in range(len(words))]

def extract_features(words, index):
    word = words[index]
    features = {
        'word': word,
        'is_first': index == 0,
        'is_last': index == len(words) - 1,
        'is_capitalized': word[0].upper() == word[0],
        'is_all_caps': word.upper() == word,
        'is_all_lower': word.lower() == word,
        'prefix-1': word[0],
        'prefix-2': word[:2],
        'prefix-3': word[:3],
        'suffix-1': word[-1],
        'suffix-2': word[-2:],
        'suffix-3': word[-3:],
        'prev_word': '' if index == 0 else words[index - 1],
        'next_word': '' if index == len(words) - 1 else words[index + 1],
        'has_hyphen': '-' in word,
        'is_numeric': word.isdigit(),
        'capitals_inside': word[1:].lower() != word[1:],
        'word_shape': ''.join(['X' if c.isupper() else 'x' if c.islower() else 'd' if c.isdigit() else '-' for c in word]),
        'prev_word_is_capitalized': '' if index == 0 else words[index - 1][0].isupper(),
    }
    return features


def pos_tagger(text: Optional[str]) -> Optional[str]:
    tag_colors = {
        "Adj": "#1E3A8A",
        "Adv": "#B91C1C",
        "Noun": "#065F46",
        "Verb": "#B45309",
        "PropN": "#6B21A8",
        "Pronoun": "#134E4A",
        "Num": "#4E362A",
        "Det": "#3A4F41",
        "Part": "#881337",
        "Prep": "#2F4F4F",
    }
    if text:
        features = prepare_input(text)
        tags = crf_model.predict([features])[0]
        words = text.split()
        result = [(word, tag, tag_colors.get(tag, "#000000")) for word, tag in zip(words, tags)]
        return result
    return None


def stanford_formatter(pos_tag: list[tuple[str, str, str]]) -> str:
    if pos_tag:
        str_result = ""
        for item in pos_tag:
            word = item[0]
            tag = item[1]
            if word.strip():
                str_result += f"{word}/{tag.upper()} "
        return str_result.strip()
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
