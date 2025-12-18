#!/usr/bin/bash
# SPDX-FileCopyrightText: 2025 souzouryoku00
# SPDX-License-Identifier: BSD-3-Clause

cd "$(dirname "$0")"

ng(){
    echo "$1 行目のテスト失敗"
    res=1
}

res=0

run_ok_test () {
    local input="$1"
    local expected="$2"
    local out status

    out=$(echo -e "$input" | ./textstats | jq '.top3_words |= sort' | jq -S -c)
    status=$?
    [ "$status" = "0" ] || ng "$3"

    expected=$(echo "$expected" | jq '.top3_words |= sort' | jq -S -c)
    [ "$out" = "$expected" ] || ng "$3"
}

run_ok_test "Hello world\nHello" \
'{"avg_word_len":5.0,"char_count":17,"digits":0,"line_count":2,"letters":15,"spaces":1,"symbols":1,"top3_words":["Hello","world"],"vocab_size":2,"word_count":3}' \
"$LINENO"

run_ok_test "abc 123" \
'{"avg_word_len":3.0,"char_count":7,"digits":3,"line_count":1,"letters":3,"spaces":1,"symbols":0,"top3_words":["123","abc"],"vocab_size":2,"word_count":2}' \
"$LINENO"

run_ok_test "a\nb\nc" \
'{"avg_word_len":1.0,"char_count":5,"digits":0,"line_count":3,"letters":3,"spaces":0,"symbols":2,"top3_words":["a","b","c"],"vocab_size":3,"word_count":3}' \
"$LINENO"

run_ok_test "" \
'{"avg_word_len":0,"char_count":0,"digits":0,"line_count":0,"letters":0,"spaces":0,"symbols":0,"top3_words":[],"vocab_size":0,"word_count":0}' \
"$LINENO"

out=$(./textstats --invalid-option 2>/dev/null)
status=$?
[ "$status" = "1" ] || ng "$LINENO"
[ "$out" = "" ] || ng "$LINENO"

[ "$res" = 0 ] && echo ok
exit $res

