resource "aws_kms_key" "lambda_key" {
  description             = local.kms_description
  enable_key_rotation     = true
  deletion_window_in_days = 7
}

resource "aws_kms_alias" "lambda_key_alias" {
  name          = local.kms_name
  target_key_id = aws_kms_key.lambda_key.id
}
