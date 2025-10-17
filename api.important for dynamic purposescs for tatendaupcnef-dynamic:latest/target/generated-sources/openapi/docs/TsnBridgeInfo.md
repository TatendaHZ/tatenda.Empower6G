

# TsnBridgeInfo

Contains parameters that describe and identify the TSC user plane node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bridgeId** | **Integer** | Integer where the allowed values correspond to the value range of an unsigned 64-bit integer. |  [optional] |
|**dsttAddr** | **String** | String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042 |  [optional] |
|**dsttIpv4Addr** | **String** | String identifying a IPv4 address formatted in the \&quot;dotted decimal\&quot; notation as defined in RFC 1166. |  [optional] |
|**dsttIpv6Addr** | [**Ipv6Addr**](Ipv6Addr.md) |  |  [optional] |
|**dsttPortNum** | **Integer** | Unsigned Integer, i.e. only value 0 and integers above 0 are permissible. |  [optional] |
|**dsttResidTime** | **Integer** | Unsigned Integer, i.e. only value 0 and integers above 0 are permissible. |  [optional] |


## Implemented Interfaces

* Serializable


