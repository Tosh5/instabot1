[Eng]
I created instagram auto unfollow bot using python. 
It runs with Firefox and ofcourse you need to download Geckodriver.
Since it is very troublesome to translate everything written in JP, plz use google translate.

  How to use?:
    1. enter your account username and password in the bottom of the code.
     → There are 2 places to enter username and only one place to enter password.
    2. Download Firefox and geckodriver.

[日本語]
初心者ながら、Pythonでインスタのbotを作ってみました。
Firefoxを使う前提で作っているので、Geckodriverをインストールした上で、実行してください。

  [使い方]：
  1. Firefoxと、それをPythonで制御できるようにするためのGeckodriverをインストールしてください。
  2. コードを何かしらのエディタで開いて、コードの最後の方のusername, passwordと書いてあるところに、ご自身のものを書き入れてください。
  （usernameの入力箇所は二箇所あります。）

  [機能]：
  ・自動でフォローを解除していきます。
  
  ・核になっているのは、 control_methods というメソッドです。
  　このメソッドに、どの隠れメソッドを起動させるかを指示するコードを書くことで、プログラムを制御することができます。
      イメージ）
      クラスInstaBotをインスタンス化する-> control_methodsを実行 -> 個々のメソッド（control_methodsに書かれているメソッドが実行される）
      
  ・シャドーバンを制御する機能があります
    フォロー解除をするごとに、今の推定フォロー数とフォロワー数を計算していきます。そして20回ごとにそれがシャドーバンがかかっていないかチェックする仕組みになっています。シャドーバンがかかると、そのひどさに応じて自動で数時間停止します。
    
     
  [フォロー解除の2メソッド]：
  ・有効なフォロー解除方法は2通りあります。
    1：フォローしている人リストの一覧からリムっていく（メソッド名：_remove_following）
    2：タイムラインに流れる投稿をみながら、プロフアイコンをクリックして、そしてリムっていく（メソッド名：_timeline_remove）
    現状のコードでは、2の方のみを利用するように書いてありますが、control_methodsに 1 の方のメソッドを実行するように指示を書けば、1の方でもフォロー解除が可能です。
    

  [注意]：
  1：適宜XPathを更新してください。
  　　インスタはすぐに仕様を変えることがあり、これをご覧になっているときにはすでにコードが動かなくなっていることが考えられます。
  　　特に、XPath（ページ上のオブジェクトを指定するコード？）は頻繁に更新されるため、ご利用前に最新のXPathに書き換え直す必要があるかもしれません。
     ターミナルをみながら、エラーの出た箇所を修正してください。
  
  2：fed, fingとは？
  　　私の脳のスペックの都合上、フォローとフォロワーの意味がこんがらがることがあったため、
        ・こちらから相手にフォローしていることをfing
        ・相手がこちらをフォローしていることをfed
     と勝手に命名しています。
     
     例えば、
     fing_numなどと言ったら、こちらがフォローしているアカウントの数を表します。
     expected_fed_numなどと言ったら、プログラムが想定しているフォロワー数を表します。
     
     
     
     
     
  
  
  
  
