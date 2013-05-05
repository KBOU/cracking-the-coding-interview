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
