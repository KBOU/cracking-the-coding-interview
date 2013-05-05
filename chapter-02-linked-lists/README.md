# LinkedList

## テクニック

### Runnerテクニック

進みの違うループを回して該当する位置を探すテクニック。  
例えばLinkedListの真ん中の要素が欲しい時、  
かたっぽはstep=1でループを回して、もう一方はstep=2で回すと、  
step=2で回したほうが終端に達した時にstep=1のほうはちょうど真ん中にいる。

## 2-1. LinkedListの重複する要素を削除する。

条件：

* Listはソートされてない
* bufferを使っちゃダメ

### 方針

bufferを使っちゃダメということは、HashMapとか使っちゃダメということだろう。
二重ループ回して、

1. 1つ目の要素と2つ目の要素を比較
2. 1つ目の要素を3つ目の要素と比較
3. ........

て感じでいこうと思います。

`src/no_dup_list.c`

## 2-2. LinkedListで最後からｋ番目の要素を取得する。

条件：

* 単方向リスト


### 方針

Runnerを2つ回す。

1つめは、step=1で回し、  
2つめは、1つめがk回ループした時にstep=1でスタートする。

`src/kth_to_last.c`

## 2-3. 指定した要素を削除する。

条件：

* 単方向リスト
* 指定した要素にしかアクセス出来ない

### 方針

削除する要素の次の要素のデータ、次の要素の次の要素を要素の次の要素にする。

`src/delete_elem.c`


## 2-4. xの値を境にxより値が小さな要素はx以上の要素より必ず前に来るように配置する

### 方針

1. xより小さいLinkedlistとxより大きなLinkedlistを定義する
2. linkedlistを前からイテレートしていき、xより小さかったら小さいLInkedlistに大きかったら大きいLinkedlistにappend
3. ２つのlinkedlistを合併する

`src/partition.c`

## 2-5. LinkedListに1桁ずつ数字を入れて足し算してみる。

1の位がLinkedListの頭で10の位、100の位がそれに続く場合。  
この場合、単純そう。  
逆の場合をやってみる。(100の位、10の位、1の位と続く場合)

### 方針

1. まずはループを回して最大桁数を取得する。
2. 最大桁数に満たない方のLinkedListはheadに0のLinkedListを足りない分だけ付け加える
3. と同時に繰り上がりLinkedListを同じ桁数+1の長さで作成する。値は0
4. 2つのLinkedListを足し算する。繰り上がりは繰り上がりLinkedListに記憶
5. 繰り上がりLinkedListと足し算済みLinkedListを足し算する。
6. 繰り上がりLinkedListの値が全部0になるまで足し算する。

`src/addition.c`

## 2-6. 循環リストの循環の始点を探せ！

STEP=1のRunnerとSTEP=2のRunnerを回す。  
そうすると、循環していれば必ずRunner1とRunner2は循環リスト上の何処かのノードで出会う。
なぜなら、Runner1とRunner2は1 iterationごとに1つずつ差がでかくなるので。

例えば、ABCDEの5つの要素があり、Cが循環の始点の場合、

<table>
  <tr> <td>ITERATE</td> <td>0</td> <td>1</td> <td>2</td> <td>3</td> <td>4</td> <td>5</td> <td>6</td> <td>7</td> </tr>
  <tr> <td>STEP=1</td> <td>A</td> <td>B</td> <td>C</td> <td>D</td> <td>E</td> <td>C</td> <td>D</td> <td>E</td> </tr>
  <tr> <td>STEP=2</td> <td>A</td> <td>C</td> <td>E</td> <td>D</td> <td>C</td> <td>E</td> <td>D</td> <td>C</td> </tr>
</table>

3回目のiterationと6回目のiterationでであう。  
なので、循環部の長さは3であることがわかる。(2回目に同じ要素にあたった時に判断しないとダメ)

ここまでわかるとありうる可能性はBCD, CDE, DEFのいずれかが循環部分を構成しているということ。  
あとはリスト全体の長さがわかれば循環の始点がわかる。

たとえば、BCDである可能性を調べるためには、STEP=1のRunnerとSTEP=4のRunnerを1回iterateすれば良い。  
これでNode Bで出会えば、循環の始点はBであることがわかる。

### 方針

これを一般化(?)すると、

1. Runnerを2つイテレートする。片方はSTEP=1, もう一方はSTEP=2
2. 2回出会うまでイテレートし、1回目のindex(i1)と2回目のindex(i2)を記録する。
3. Runnerを先頭に戻す。
4. STEP=1とSTEP=i1+1で1回イテレートする。出会えばそこが始点。
5. STEP=1とSTEP=i1+2で1回イテレートする。出会えばそこが始点。。。というのを出会うまでSTEP=i2まで繰り返す。


`src/circular.c`

## 2-7. Linkedlistが回文であることを確認する。

条件：

* 単方向リスト
* データは数値

### 方針

逆順リストをつくって比較

`src/palindrome.c`
