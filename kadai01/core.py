#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

from collections import Counter
import string

def analyze_text(text: str) -> dict:
    lines = text.splitlines()
    words = text.split()
    char_count = len(text)
    word_count = len(words)
    line_count = len(lines)
    vocab = set(words)
    vocab_size = len(vocab)
    avg_word_len = sum(len(w) for w in words)/word_count if word_count else 0

    counts = Counter(text)
    letters = sum(counts[c] for c in string.ascii_letters)
    digits = sum(counts[c] for c in string.digits)
    spaces = sum(counts[c] for c in string.whitespace)
    symbols = char_count - letters - digits - spaces

    most_commonwords = [w for w, _ in Counter(words).most_common(3)]

    return {
        "char_count": char_count,
        "word_count": word_count,
        "line_count": line_count,
        "vocab_size": vocab_size,
        "avg_word_len": avg_word_len,
        "letters": letters,
        "digits": digits,
        "spaces": spaces,
        "symbols": symbols,
        "top3_words": most_common_words
    }

if __name__ == "__main__":
    import sys
    text = sys.stdin.read()
    result = analyze_text(text)
    print(result)
