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
client_pet: (stringified JSON) `{"pet_name1":{"species":"dog","breed":"labrador","age_years":"10","weight_kilos":"12"}}`
schedule_datetime: (UTC) "2020-12-30T00:09:30-03:00"
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
