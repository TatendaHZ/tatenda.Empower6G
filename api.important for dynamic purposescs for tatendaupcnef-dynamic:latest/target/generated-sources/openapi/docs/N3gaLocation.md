

# N3gaLocation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**n3gppTai** | [**Tai**](Tai.md) |  |  [optional] |
|**n3IwfId** | **String** | This IE shall contain the N3IWF identifier received over NGAP and shall be encoded as a string of hexadecimal characters. Each character in the string shall take a value of \&quot;0\&quot; to \&quot;9\&quot;, \&quot;a\&quot; to \&quot;f\&quot; or \&quot;A\&quot; to \&quot;F\&quot; and shall represent 4 bits. The most significant character representing the 4 most significant bits of the N3IWF ID shall appear first in the string, and the character representing the 4 least significant bit of the N3IWF ID shall appear last in the string. |  [optional] |
|**ueIpv4Addr** | **String** | String identifying a IPv4 address formatted in the \&quot;dotted decimal\&quot; notation as defined in RFC 1166. |  [optional] |
|**ueIpv6Addr** | [**Ipv6Addr**](Ipv6Addr.md) |  |  [optional] |
|**portNumber** | **Integer** | Unsigned Integer, i.e. only value 0 and integers above 0 are permissible. |  [optional] |
|**tnapId** | [**TnapId**](TnapId.md) |  |  [optional] |
|**twapId** | [**TwapId**](TwapId.md) |  |  [optional] |
|**hfcNodeId** | [**HfcNodeId**](HfcNodeId.md) |  |  [optional] |
|**gli** | **byte[]** | string with format \&quot;bytes\&quot; as defined in OpenAPI |  [optional] |
|**w5gbanLineType** | **LineType** |  |  [optional] |
|**gci** | **String** | Global Cable Identifier uniquely identifying the connection between the 5G-CRG or FN-CRG to the 5GS. See clause 28.15.4 of 3GPP TS 23.003. This shall be encoded as a string per clause 28.15.4 of 3GPP TS 23.003, and compliant with the syntax specified in clause 2.2 of IETF RFC 7542 for the username part of a NAI. The GCI value is specified in CableLabs WR-TR-5WWC-ARCH. |  [optional] |


## Implemented Interfaces

* Serializable


