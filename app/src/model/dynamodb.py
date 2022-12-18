import sys

sys.path.append('lib')
import boto3

# シングルトン
class DynamoDB:
    _TABLE_NAME = 'AnimePostData'

    _unique_instance = None
    _dynamo_table = None

    def __new__(cls):
        raise NotImplementedError('Cannot Generate Instance By Constructor')

    # インスタンス生成
    @classmethod
    def __internal_new__(cls):
        dynamo = boto3.resource('dynamodb')
        cls._dynamo_table = dynamo.Table(cls._TABLE_NAME)

        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        # インスタンス未生成の場合
        if not cls._unique_instance:
            cls._unique_instance = cls.__internal_new__()
        return cls._unique_instance

    @classmethod
    def write_items(cls, items: list[dict]) -> None:
        with cls._dynamo_table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)

    @classmethod
    def get_all_items(cls) -> None:
        response = cls._dynamo_table.scan()
        items = response['Items']
        for item in items:
            print(item)
