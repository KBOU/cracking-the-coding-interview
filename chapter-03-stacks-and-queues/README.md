# StackとQueue

## 3-1. 一つのArrayで3つのStack

### 方針

3分割する

`src/three_stacks.py`

## 3-2. stackにminメソッドを追加

条件：

* O(1)

### 方針

minもstackにいれる。
popしたときにminと同じ値だったらminスタックもpopする。


## 3-3. StackのSetを仮想的に一つのStackとして扱う

発展： popAt(index)を実装すること(indexで指定されたstackからpopする)

### 方針

* threshold=10としてみる
* init時にStackを一つ作成する。
* Stackはindexで管理
* push時、stackがいっぱいだったら新しいstackを作成し、stackのindexをインクリメントする。
* pop時、stackが空だったら、stackのindexをデクリメントする。
* pop時、stackのindex &lt; stack配列の長さ - 2ならstack配列の最後の要素をdeleteする。

`src/stack_set.py`

## 3-4. ハノイの塔

色々考えたら以下のルールに従えば達成できそう。

* 1個の塔、2個の塔、・・・という小ゴールを達成して最終的にはN個の塔を完成させる
* Diskの個数が奇数なら1個目の塔は右に建てる。偶数なら真ん中。
* 小ゴール達成後は必ず左の塔から空いているスペースに動かす。
* 動かせるDiskのうち最も重いものを動かす
* 最後に動かしたDiskは動かさない
* 動かすDiskのサイズと移動先のDiskのサイズを引いたものが奇数になるところに移動する。

`src/hanoi.py`

### 追記

再帰で簡単にできる。というよりそちらにすべき。

## 3-5. stackを2つ使ってQueueを作る

### 方針

* stack1, stack2を作る
* データ入力のときはstack1にデータを突っ込んでく。この時stack2がからでなければ、stack2の要素をすべてpopしてstack1にpushする
* データ出力のときはstack1からstack2に全部データを突っ込んで、stack2からpopする。

`src/queue_2_stacks.py`

## 3-6. 大きい順にソートされたstackを作る

### 方針

1つ余分にStackを作り、bufferとして使う。  
要素の挿入があった時に毎回stackのtopと比較を行い、    
新しい要素の方が小さかったら、stackをpopしてbufferにpopしたやつを入れる。  
ということを繰り返す。

`src/sorted_stack.py`


## 3-7. 犬猫ハウス

* FIFO
* 犬FIFO
* 猫FIFO

### 方針

LinkedListで犬猫を管理。  
犬FIFOが選択された場合は、
listからinstanceが犬のものを選び、linkedlistから削除

`src/animal_shelter.py`
