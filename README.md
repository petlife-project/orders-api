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
$ python3.7 -m orders.app
```

# Use cases and endpoints #

## Order Placement ##
`POST /client`

*Request body:*
Form data
```
petshop_username: "petshopxusernam123"
petshop_name: "PetX Diadema"
service_id: "5f9d6594448854f39b13d386"
service_name: "Banho"
client_username: "user123"
client_name: "Pedro"
client_pet: (stringified JSON) `{"name":"Tchunay","species":"dog","breed":"labrador","age_years":"10","weight_kilos":"12"}`
schedule_datetime: (UTC) "2020-12-30T08:01:00-03:00"
```

*Responses*

`200 OK`

Returns ok code if everything is correct with the request

```JSON
'Order placed!'
```

## Order Cancellation ##
`DELETE /client?order_id=<exact-match>`

*Responses:*

`200 OK`

Returns ok code if everything is correct with the request

```JSON
'Order cancelled successfully.'
```

`404 Not found`

Returns not found code if the order id sent on the request doesn't match any of the orders in the DB

```JSON
'No orders found with provided id'
```

## Order Confirmation ##
`PUT /shop?order_id=<exact-match>`

*Responses:*

`200 OK`

Returns ok code if everything is correct with the request

```JSON
'Order confirmed successfully.'
```

`404 Not found`

Returns not found code if the order id sent on the request doesn't match any of the orders in the DB

```JSON
'No orders found with provided id'
```

## Order Rejection ##
`DELETE /shop?order_id=<exact-match>`

*Responses:*

`200 OK`

Returns ok code if everything is correct with the request

```JSON
'Order rejected successfully.'
```

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
        "_id": "5fa8a22e11d142b2dbf038a2",
        "client": {
            "name": "Allan",
            "pet": {
                "name": "Tchunay",
                "species": "dog",
                "breed": "labrador",
                "age_years": "10",
                "weight_kilos": "12"   
            },
            "username": "allandlo"
        },
        "petshop": {
            "name": "Pet X",
            "username": "petxusername"
        },
        "schedule": {
            "datetime": "2020-12-30T09:30:00-03:00"
        },
        "service": {
            "id": "5f9d6594448854f39b13d386",
            "name": "Banho"
        },
        "status": {
            "cancelled": false,
            "confirmed": false,
            "rejected": false
        }
    },
    {
        "_id": "5fa8a23311d142b2dbf038a3",
        "client": {
            "name": "Bruno",
            "pet": {
                "name": "Tico",
                "species": "dog",
                "breed": "labrador",
                "age_years": "10",
                "weight_kilos": "12"
            },
            "username": "manobrow"
        },
        "petshop": {
            "name": "Pet X",
            "username": "petxusername"
        },
        "schedule": {
            "datetime": "2020-12-08-08-00"
        },
        "service": {
            "id": "5f9d6594448854f39b13d386",
            "name": "Tosa"
        },
        "status": {
            "cancelled": false,
            "confirmed": false,
            "rejected": false
        }
    }
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
