resource "aws_dynamodb_table" "anime-post-data" {
  name           = "AnimePostData"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "PostType"
  range_key      = "ContentId"
  table_class    = "STANDARD_INFREQUENT_ACCESS"

  attribute {
    name = "PostType"
    type = "S"
  }
  attribute {
    name = "ContentId"
    type = "S"
  }
  attribute {
    name = "Title"
    type = "S"
  }
  attribute {
    name = "StartDateTime"
    type = "S"
  }

  global_secondary_index {
    name            = "Title-StartDateTime-index"
    hash_key        = "Title"
    range_key       = "StartDateTime"
    write_capacity  = 5
    read_capacity   = 5
    projection_type = "ALL"
  }
  local_secondary_index {
    name            = "ContentId-index"
    range_key       = "ContentId"
    projection_type = "ALL"
  }
}
