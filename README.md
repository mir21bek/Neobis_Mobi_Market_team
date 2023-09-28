# Neobis_Mobi_Market_team
# API Documentation

This guide describes the user and product management API using the
Django REST framework. The API includes registration, login, updating
the user profile, sending and checking a verification code, as well 
as functionality for managing products and likes.


# Authentication and Authorization Endpoints:


## User Registration
### `POST /register`
Registers a new user and returns user data.

**Request:**
```commandline
Content-Type: application/json

{
  "username": "string",
  "email": "user@example.com",
  "password": "stringst",
  "password_confirm": "stringst"
}
```
**Response:**
```commandline
Content-Type: application/json

{
  "username": "string",
  "email": "user@example.com",
  "password": "stringst",
  "password_confirm": "stringst"
}
```



## User Authorization
### `POST /login`
Authenticates the user and returns an access token and refresh token.

**Request:**
```commandline
Content-Type: application/json

{
  "username": "string",
  "password": "stringst"
}
```
**Response:**
```commandline
Content-Type: application/json

{
  "username": "string",
  "password": "stringst",
  "tokens": "string"
}
```


## Profile Update
### `PUT /profile`
Updates the user's profile.

**Request:**
```commandline
Content-Type: application/json

{
  "avatar": "image",
  "first_name": "string",
  "last_name": "string",
  "date_of_birth": "YYYY-MM-DD"
}
```
**Response:**
```commandline
Content-Type: application/json

{
  "avatar": "http://example.com",
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "date_of_birth": "YYYY-MM-DD"
}
```


## Sending a code to verify phone number
### `PUT /code-send`
Generates and sends a verification code to the specified phone number.

**Request:**
```commandline
Content-Type: application/json

{
  "phone_number": "string"
}
```
**Response:**
```commandline
Content-Type: application/json

{
  "phone_number": "string"
}
```


## Checking a code to verify phone number
### `POST /code-check`
Checks the verification code and confirms the verification of the user's phone number.

**Request:**
```commandline
Content-Type: application/json

{
  "verification_code": "string"
}
```
**Response:**
```commandline
Content-Type: application/json

{
  "verification_code": "string"
}
```


## User Logout
### `POST /logout`
Invalidates the user's refresh token by logging him out.

**Request:**
```commandline
Content-Type: application/json

{
  "refresh": "string"
}
```
**Response:**
```commandline
Content-Type: application/json

{
  "refresh": "string"
}
```


# Product Endpoints:

## Get a list of products
### `GET /products/api/`
Gets a list of all available products.

**Response:**
```commandline
Content-Type: application/json

[
  {
    "name": "string",
    "description": "string",
    "photo": "http://example.com",
    "available": true,
    "price": "string"
  }
]
```


## Receiving Product Details
### `GET /products/api/{product_id}/`
Retrieves details of a specific product by its identifier (product_id).



## Creation of a new product
### `POST /product/api/`
Creates a new product.


**Request:**
```commandline
Content-Type: application/json

{
  "name": "string",
  "description": "string",
  "photo": "image",
  "available": true,
  "price": "string"
}
```
**Response:**
```commandline
Content-Type: application/json

{
  "name": "string",
  "description": "string",
  "photo": "http://example.com",
  "available": true,
  "price": "string"
}
```



## Product Update
### `PUT /products/api/{product_id}/`
Updates product data by its identifier (product_id).

**Request:**
```commandline
Content-Type: application/json

{
  "name": "string",
  "description": "string",
  "photo": "image",
  "available": true,
  "price": "string"
}
```
**Response:**
```commandline
Content-Type: application/json

{
  "name": "string",
  "description": "string",
  "photo": "http://example.com",
  "available": true,
  "price": "string"
}
```



## Product Delete
### `DELETE /products/api/{product_id}/`
Deletes a product by its identifier (product_id).


## Product Like
### `POST /products/like/`
Like a specific product. Returns a message about the result.

## Product Unlike
### `DELETE /products/unlike/{product_id}/`
Remove likes from a product by (product_id). Returns a message about the result.

## Like Counts
### `GET /products/like-counts`
Returns the number of likes for a product.