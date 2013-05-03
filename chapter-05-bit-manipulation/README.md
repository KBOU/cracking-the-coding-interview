# ビット演算

5章の問題を解いてみました。
テストは

`$ mocha --compilers coffee:coffee-script test/`

で実行します。その前に

`$ npm install`

して必要なモジュールをインストールする必要があります。
(ちなみにcoffee, mochaはglobalに入れてます)

## 5-1. 指定した位置にビットを挿入する

`src/bit_insertion.coffee`

## 5-2. doubleをbit配列で表示

`src/double_to_binary.coffee`


## 5-3. 1がたってるbit数が同じで1つ小さな数と大きな数を求める

`src/get_next_prev.coffee`

## 5-4. (n & n-1) == 0が意味するところは

2のべき乗。

n & n-1 == 0ということは各bitが(0, 0)もしくは(0, 1)の組み合わせ。

1を引くと右から見て最初に1が現れるbit以下のbitが反転されるので、
最初に1が現れるところより右側のbitは&をとると0。

しかし左側のbitは変化しないのでnもn-1も上位桁は0である必要がある。

つまり、1つだけbitが立っている数値が答えである。

## 5-5. 数値を変換した時に変化したbitの数を調べる

`src/num_bits.coffee`

## 5-6. intの偶数ビットと奇数ビットを入れ替える

`src/swap_bits.coffee`

## 5-7. 0-nまでの数値で欠損してる数値を調べる(1つのみ欠損)

`src/check_missing.coffee`

## 5-8. 水平線を引く

coffeeにbyteがなさそうなので、Cでやりましたが、
length引数なしでできるのでしょうか・・・

`src/draw_horizontal.c`
