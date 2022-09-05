# Anime-Bot

## ビルド・立ち上げ
```sh
docker-compose up -d --build
docker exec -it anime-bot bash
```

## terraformからサービス作成
```sh
cd terraform
bash exec_apply.sh
```

## lambda関数実行テスト
```sh
aws lambda invoke --function-name twitter_anime_bot /dev/null
```
