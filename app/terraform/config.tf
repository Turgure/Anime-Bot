terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider aws {
  region = "ap-northeast-1"
}

locals {
  ### lambda
  # ソースファイルの場所
  lambda_source_dir    = "../src"
  # 関数名
  lambda_function_name = "twitter_anime_bot"
  # エントリポイント
  lambda_handler       = "lambda_function.lambda_handler"
  # 関数のランタイム
  lambda_runtime       = "python3.9"
  # IAMポリシー名
  lambda_iam_policy    = "anime_bot_iam_policy"
  # IAMロール名
  lambda_iam_role      = "anime_bot_iam_role"

  ### dynamodb
  dynamodb_table_name = "AnimePostData"
}
