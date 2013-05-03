# ArrayとString

## 1-1. Stringが全部同じCharacterでできていることを確認する

条件:

* 他のdata structureを使わない

### 方針

条件から、たぶんHashMap使うなよってことだろう。  

アルファベットの小文字を仮定。  
なので、Stringをループ回して、出現回数をbitfieldで管理する。  
フラグがたってる文字が出現したらfalseそうじゃなかったらtrue

`src/is_unique.py`

## 1-2. Stringを逆順にするreverse関数を作れ！

条件：

* stringはnullで終わる
* 言語はC or C++

### 方針

1. まずはStringの長さを取得する関数を作成する。(長さ=nullのindex-1)
2. 同じ長さのchar配列を作成する。
3. で逆順ループを回して2で作成したchar配列に格納する。

`src/reverse_string.c`

### 追記

やってみたけど、セグフォルト。  
答えを真似てみたけどセグフォルト・・・  
char配列にindex指定してchar代入の所でエラー発生。

## 1-3. string1とstring2がアナグラムかどうか確認する

### 方針

それぞれのcharacterがkeyで出現回数がvalueとなるHashMapを利用して、  
string1とstring2の出現回数を比較する。

`src/permutation.py`
