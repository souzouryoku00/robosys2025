#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

from collections import Counter
import string
import json
from collections import OrderedDict

def analyze_text(text: str) -> dict:
    text = text.rstrip("\n")  # 末尾改行を除去

    lines = text.splitlines()
    words = text.split()
    char_count = len(text)
    word_count = len(words)
    line_count = len(lines)
    vocab_size = len(set(words))
    avg_word_len = round(sum(len(w) for w in words)/word_count, 2) if word_count else 0

    counts = Counter(text)
    letters = sum(counts[c] for c in string.ascii_letters)
    digits = sum(counts[c] for c in string.digits)
    spaces = counts[' ']  # 空白の数
    symbols = char_count - letters - digits - spaces

    most_common_words = [w for w, _ in Counter(words).most_common(3)]

    return OrderedDict([
        ("avg_word_len", avg_word_len),
        ("char_count", char_count),
        ("digits", digits),
        ("line_count", line_count),
        ("letters", letters),
        ("spaces", spaces),
        ("symbols", symbols),
        ("top3_words", most_common_words),
        ("vocab_size", vocab_size),
        ("word_count", word_count),
    ])

if __name__ == "__main__":
    import sys
    text = sys.stdin.read()
    result = analyze_text(text)
    print(json.dumps(result, ensure_ascii=False, separators=(',', ':')))
