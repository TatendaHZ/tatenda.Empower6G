

# Tai


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**plmnId** | [**PlmnId**](PlmnId.md) |  |  |
|**tac** | **String** | 2 or 3-octet string identifying a tracking area code as specified in clause 9.3.3.10 of 3GPP TS 38.413, in hexadecimal representation. Each character in the string shall take a value of \&quot;0\&quot; to \&quot;9\&quot;, \&quot;a\&quot; to \&quot;f\&quot; or \&quot;A\&quot; to \&quot;F\&quot; and shall represent 4 bits. The most significant character representing the 4 most significant bits of the TAC shall appear first in the string, and the character representing the 4 least significant bit of the TAC shall appear last in the string. |  |
|**nid** | **String** | This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1). |  [optional] |


## Implemented Interfaces

* Serializable


