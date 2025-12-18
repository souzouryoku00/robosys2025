# textstatsコマンド
標準入力から受け取ったテキストに対して、文字数・単語数・行数・記号数などの統計情報を解析し、結果を出力するコマンド
文章の簡易的な解析やテキストの特徴量を確認する際に使用できます。

### 使い方
#### 1. リポジトリをクローン
```bash
git clone https://github.com/souzouryoku00/robosys2025
cd robosys2025
```
#### 2. コマンドの実行例
Hello world Helloの所に好きな文章を入れる
```bash
$ echo "Hello world Hello" | ./textstats
{"avg_word_len":5.0,"char_count":17,"digits":0,"line_count":1,"letters":15,"spaces":2,"symbols":0,"top3_words":["Hello","world"],"vocab_size":2,"word_count":3}
```
一応日本語や全角文字でも動きますが、!や?などの記号と同じ判定です
```bash
$ echo -e "あ い う" | ./textstats
{"avg_word_len":1.0,"char_count":5,"digits":0,"line_count":1,"letters":0,"spaces":2,"symbols":3,"top3_words":["あ","い","う"],"vocab_size":3,"word_count":3}
```
##### 3. 集計される項目
|項目名|内容|
|---|---|
|avg_word_len|単語の平均文字数（小数2桁）|
|char_count|全文字数|
|digits|数字文字の個数|
|line_count|行数|
|letters|英字 (A–Z,a–z) の個数|
|spaces|半角スペースの個数|
|symbols|記号の個数（letters digits spaces 以外）|
|top3_words|最頻出上位3単語|
|vocab_size|語彙数（異なる単語の種類）|
|word_count|単語数|

### 必要なソフトウェア
Python(テスト済みバージョン: 3.8〜3.10)

### テスト環境
Ubuntu 24.04 LTS

### ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Rikuto Hoshi 
