import json
from pyqldb.driver.qldb_driver import QldbDriver
qldb_driver = QldbDriver(ledger_name='kosansyoumei-registration')


def lambda_handler(event, context):
    # TODO implement

    # return {
    #     'statusCode': 200,
    #     'body': event
    # }

    device = event['queryStringParameters']['device']

    certificate_list = []
    from_name_list = []
    to_name_list = []
    dob_list = []
    memo_list = []
    def read_documents(transaction_executor):
    
        cursor = transaction_executor.execute_statement("SELECT * FROM Certificate WHERE DeviceId IN ('" + device + "')")
        for doc in cursor:
            print(device)
            print(doc["FromName"])
            print(doc["ToName"])
            print(doc["MEMO"])
            certificate_list.append(doc["ToName"])
            from_name_list.append(doc["FromName"])
            to_name_list.append(doc["ToName"])
            dob_list.append(doc["DOB"])
            memo_list.append(doc["MEMO"])
    qldb_driver.execute_lambda(lambda executor: read_documents(executor))

    msg = {
        "person_list": certificate_list,
        "from_name_list": from_name_list,
        "to_name_list": to_name_list,
        "dob_list": dob_list,
        "memo_list": memo_list
    }

    return {
        'statusCode': 200,
        'body': json.dumps(msg)
    }

