data "archive_file" "function_source" {
  type        = "zip"
  source_dir  = local.lambda_source_dir
  output_path = "archive/${local.lambda_function_name}.zip"
}

resource "aws_lambda_function" "function" {
  function_name = local.lambda_function_name
  handler       = local.lambda_handler
  runtime       = local.lambda_runtime
  role          = aws_iam_role.lambda_role.arn

  filename         = data.archive_file.function_source.output_path
  source_code_hash = data.archive_file.function_source.output_base64sha256

  depends_on = [aws_iam_role_policy_attachment.lambda_policy, aws_cloudwatch_log_group.lambda_log_group]
}
