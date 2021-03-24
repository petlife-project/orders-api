# orders-api
The REST API responsible for order management, like placing and cancelling an order for the clients and confirming or rejecting for the shops.

## Running locally ##

1 - To run this API locally you should first create a python virtual environment with:

```
$ python3.7 -m venv venv
```

2 - And then enter it:

```
$ source venv/bin/activate
```

3 - Now you can install the project's dependencies:

```
$ pip install -r requirements.txt
```

4 - Fill the .env file with the environment variables and theirs values; the variables you'll need are in the .env-example file; Export them using:

```
$ export $(cat .env | xargs)
```

5 - Finally, start the application:

```
$ python -m orders.app
```

# Use cases and endpoints #

## Order Placement ##
`POST /client`

*Request body:*
JSON
```json
{
    "petshop_username": "string",
    "petshop_name": "string",
    "service_id": "string",
    "service_name": "string",
    "client_username": "string",
    "client_name": "string",
    "client_pet": {
        "name": "string",
        "species": "string",
        "breed": "string",
        "age_years": "integer",
        "weight_kilos": "float"
    },
    "schedule_datetime": (UTC) "datetime"
}
```

*Responses*

`200 OK`

Order places successfully

## Order Cancellation ##
`DELETE /client?order_id=<exact-match>`

*Responses:*

`200 OK`

Order cancelled successfully

`404 Not found`

Returns not found code if the order id sent on the request doesn't match any of the orders in the DB

```JSON
'No orders found with provided id'
```

## Order Confirmation ##
`PUT /shop?order_id=<exact-match>`

*Responses:*

`200 OK`

Order confirmed successfully

`404 Not found`

Returns not found code if the order id sent on the request doesn't match any of the orders in the DB

```JSON
'No orders found with provided id'
```

## Order Rejection ##
`DELETE /shop?order_id=<exact-match>`

*Responses:*

`200 OK`

Order rejected successfully

`404 Not found`

Returns not found code if the order id sent on the request doesn't match any of the orders in the DB

```JSON
'No orders found with provided id'
```

## Polling ##
`GET /shop?username=<exact-match>`

`GET /client?username=<exact-match>`

*Responses:*

`200 OK`

Returns ok code and list of orders if everything is correct with the request and at least one orders is found related to that user

```JSON
[
    {
        "_id": "string",
        "petshop": {
            "username": "string",
            "name": "string"
        },
        "service": {
            "id": "string",
            "name": "string"
        },
        "client": {
            "username": "string",
            "name": "string",
            "pet": {
                "name": "string",
                "species": "string",
                "breed": "string",
                "age_years": "integer",
                "weight_kilos": "float"
            }
        },
        "schedule": {
            "datetime": "datetime"
        },
        "status": {
            "confirmed": "boolean",
            "cancelled": "boolean",
            "rejected": "boolean"
        }
    },
]
```

`404 Not found`

Returns not found code if there aren't any orders related to that user

```JSON
'No orders related to this user'
```

`403 Forbidden`

Returns forbidden code if the provided value contains invalid characters

```JSON
'Invalid username'
```
