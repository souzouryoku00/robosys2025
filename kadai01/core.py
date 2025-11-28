#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

import re
from collections import Counter

def analyze_text(text: str) -> dict:
    lines = text.splitlines()
     words = re.findall(r'\S+', text)
     alphabets = sum(c.isalpha() for c in text)
