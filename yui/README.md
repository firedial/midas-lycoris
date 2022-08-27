# DB

## ユーザ一覧

* root
* midas: アプリケーションはこのユーザを使う
* midas_backup: バックアップに使うユーザ
* midas_analyze: 解析用に使うユーザ

## ユーザの追加

root, midas はコンテナ作成時に自動的に作成される。
midas_backup, midas_analyze は sql 配下にあるシェルスクリプトをコンテナ内で流す(ファイルのマウントはしていないので、コピペで実行する)。

