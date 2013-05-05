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
