from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

table = dynamodb.Table('pageranks')

pageid = "1234"

# response = table.put_item(
#    Item={
#         'PageId': pageid,
#         'Info': {
#             'pagerank': "35818.1408379591"
#         }
#     }
# )
#
# print("PutItem succeeded:")
# print(json.dumps(response, indent=4, cls=DecimalEncoder))


try:
    response = table.get_item(
        Key={
            'PageId': pageid,
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response['Item']
    print("GetItem succeeded:")
    print(json.dumps(item, indent=4, cls=DecimalEncoder))
