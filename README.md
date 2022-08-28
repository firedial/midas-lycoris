# midas-lycolis

家計簿管理システム。

## 初期設定

### 環境変数

環境変数のファイルのコピーと値の修正

```
cp ./yui/.env.example ./yui/.env
cp ./haruhi/.env.example ./haruhi/.env
cp ./rikka/.env.example ./rikka/.env
```

### コンテナ起動

```
docker compose up -d
```

http://localhost:8111/ にアクセスしてページが見れたら大丈夫。

### DB ユーザ作成

root, midas はコンテナ作成時に自動的に作成される。
midas_backup, midas_analyze は yui/sql 配下にあるシェルスクリプトをコンテナ内で流す(ファイルのマウントはしていないので、コピペで実行する)。

#### DB ユーザ一覧

* root
* midas: アプリケーションで使う
* midas_backup: バックアップに使うユーザ
* midas_analyze: 解析用に使うユーザ

### バックアップ設定

#### crontab で定期実行する設定

rikka のコンテナに入って `init/init.sh` を実行する。

#### バックアップボタンの設定

25番に OK のランプ、 24番に NG のランプ、 27番にボタンを接続する。
コンテナに入らず、ホストOS上で下記コマンドを実行する。

```
nohup python backup.py &
```

