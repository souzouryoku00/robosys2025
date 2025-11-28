#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

import re
from collections import Counter

def analyze_text(text: str) -> dict:
    lines = text.splitlines()
    words = re.findall(r'\S+', text)
    alphabets = sum(c.isalpha() for c in text)
    digits = sum(c.isdigit() for c in text)
    spaces = sum(c.isspace() for c in text)
    symbols = len(text) - alphabets - digits - spaces
    word_lengths = [len(w) for w in words]
    counter = Counter(w.lower() for w in words)
    top_words = counter.most_common(3)

    return {
        "char_count": len(text),
        "word_count": len(words),
        "line_count": len(lines),
        "top_words": top_words,
        "avg_word_length": sum(word_lengths) / len(word_lengths) if word_lengths else 0,
        "alphabet_count": alphabets,
        "digit_count": digits,
        "space_count": spaces,
        "symbol_count": symbols,
        "vocab_size": len(counter),
    }
