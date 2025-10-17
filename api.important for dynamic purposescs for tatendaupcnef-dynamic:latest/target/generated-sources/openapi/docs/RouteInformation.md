

# RouteInformation

At least one of the \"ipv4Addr\" attribute and the \"ipv6Addr\" attribute shall be included in the \"RouteInformation\" data type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipv4Addr** | **String** | String identifying a IPv4 address formatted in the \&quot;dotted decimal\&quot; notation as defined in RFC 1166. |  [optional] |
|**ipv6Addr** | [**Ipv6Addr**](Ipv6Addr.md) |  |  [optional] |
|**portNumber** | **Integer** | Unsigned Integer, i.e. only value 0 and integers above 0 are permissible. |  |


## Implemented Interfaces

* Serializable


