#!/bin/bash
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "$1 行目のテスト失敗"
    res=1
}

res=0

export PYTHONPATH=$(pwd)

# テスト関数
test_case () {
    local input="$1"
    local expected="$2"
    local out
    out=$(echo -e "$input" | python3 -m kadai01.main | jq '.top3_words |= sort' | jq -S -c)
    expected=$(echo "$expected" | jq '.top3_words |= sort' | jq -S -c)
    if [ "$out" != "$expected" ]; then
        ng "$3"
    fi
}

test_case "Hello world\nHello" \
'{"avg_word_len":5.0,"char_count":17,"digits":0,"line_count":2,"letters":15,"spaces":1,"symbols":1,"top3_words":["Hello","world"],"vocab_size":2,"word_count":3}' \
"$LINENO"

test_case "" \
'{"avg_word_len":0,"char_count":0,"digits":0,"line_count":0,"letters":0,"spaces":0,"symbols":0,"top3_words":[],"vocab_size":0,"word_count":0}' \
"$LINENO"

test_case "abc 123 !@#" \
'{"avg_word_len":3.0,"char_count":10,"digits":3,"line_count":1,"letters":3,"spaces":2,"symbols":2,"top3_words":["abc","123","!@#"],"vocab_size":3,"word_count":3}' \
"$LINENO"

test_case "a\nb\nc" \
'{"avg_word_len":1.0,"char_count":5,"digits":0,"line_count":3,"letters":3,"spaces":0,"symbols":2,"top3_words":["a","b","c"],"vocab_size":3,"word_count":3}' \
"$LINENO"

test_case "foo foo bar baz" \
'{"avg_word_len":3.75,"char_count":15,"digits":0,"line_count":1,"letters":12,"spaces":3,"symbols":0,"top3_words":["bar","baz","foo"],"vocab_size":3,"word_count":4}' \
"$LINENO"

[ "$res" = 0 ] && echo ok
exit $res
