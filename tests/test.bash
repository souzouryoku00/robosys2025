#!/bin/bash
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

from textstat import analyze_text

def test_basic():
    text = "Hello world\nHello"
    result = analyze_text(text)
    assert result["word_count"] == 3
    assert result["line_count"] == 2
    assert result["vocab_size"] == 2
