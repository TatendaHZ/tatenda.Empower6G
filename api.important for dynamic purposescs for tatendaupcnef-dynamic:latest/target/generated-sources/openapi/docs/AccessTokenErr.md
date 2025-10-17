

# AccessTokenErr

Error returned in the access token response message

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  |
|**errorDescription** | **String** |  |  [optional] |
|**errorUri** | **String** |  |  [optional] |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| INVALID_REQUEST | &quot;invalid_request&quot; |
| INVALID_CLIENT | &quot;invalid_client&quot; |
| INVALID_GRANT | &quot;invalid_grant&quot; |
| UNAUTHORIZED_CLIENT | &quot;unauthorized_client&quot; |
| UNSUPPORTED_GRANT_TYPE | &quot;unsupported_grant_type&quot; |
| INVALID_SCOPE | &quot;invalid_scope&quot; |


## Implemented Interfaces

* Serializable


