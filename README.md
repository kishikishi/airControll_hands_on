# airControll_hands_on
■概要  
twitterを介して操作できる学習リモコンをハンズオン。
ラズパイ＆簡単な電子回路で作成可能です。
自宅のエアコンを外出時でも操作できるようにするために作りましたが、基本的に赤外線リモコン対応の家電ならなんでも使えると思います。

■機能  
twitterアカウントのタイムラインを定期的に監視し、
書かれているtweetに応じて信号を送信します。

■ディレクトリ説明  
airControll_hands_on/etc/lirc  
→LIRCをインストールすると自動的に生成されます。
 configファイルのみフォーマット参照用として載せています。  
 
airControll_hands_on/etc/systemd  
 →ラズパイ起動後、定期的にシステムを動作するための設定情報が格納されています。
  
airControll_hands_on/python_script/
 →赤外線信号の学習時に必要なプログラムと、システム本体のプログラムが入っています。
