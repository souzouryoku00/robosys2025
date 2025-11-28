#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

from collections import Counter, OrderedDict
import string
import json

#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

import sys
import json
from collections import Counter, OrderedDict

def analyze_text(text: str) -> dict:
    # 最後の改行を削除（test.bash 仕様）
    if text.endswith("\n"):
        text = text[:-1]

    lines = text.splitlines()
    words = text.split()
    char_count = len(text)
    word_count = len(words)
    line_count = len(lines)
    vocab = set(words)
    vocab_size = len(vocab)
    avg_word_len = sum(len(w) for w in words)/word_count if word_count else 0

    counts = Counter(text)
    letters = sum(counts[c] for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = sum(counts[c] for c in "0123456789")
    spaces = text.count(" ")
    symbols = char_count - letters - digits - spaces

    most_common_words = [w for w, _ in Counter(words).most_common(3)]

    # test.bash の expected に合わせて順序を固定
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
        ("word_count", word_count)
    ])

if __name__ == "__main__":
    text = sys.stdin.read()
    result = analyze_text(text)
    print(json.dumps(result, ensure_ascii=False, separators=(',', ':')))
