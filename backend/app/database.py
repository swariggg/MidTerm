import boto3

from app.config import AWS_REGION, TABLE_NAME

# Boto3 usa automáticamente las credenciales temporales del rol IAM de EC2.
# No se guardan claves de AWS en el código.
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)


def save_link(item: dict) -> None:
    table.put_item(Item=item)


def get_link(short_code: str) -> dict | None:
    response = table.get_item(Key={"short_code": short_code})
    return response.get("Item")
