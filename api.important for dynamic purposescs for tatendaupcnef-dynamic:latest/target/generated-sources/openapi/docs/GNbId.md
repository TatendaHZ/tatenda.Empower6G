

# GNbId


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bitLength** | **Integer** | Unsigned integer representing the bit length of the gNB ID as defined in clause 9.3.1.6 of 3GPP TS 38.413 [11], within the range 22 to 32. |  |
|**gNBValue** | **String** | This represents the identifier of the gNB. The value of the gNB ID shall be encoded in hexadecimal representation. Each character in the string shall take a value of \&quot;0\&quot; to \&quot;9\&quot;, \&quot;a\&quot; to \&quot;f\&quot; or \&quot;A\&quot; to \&quot;F\&quot; and shall represent 4 bits. The padding 0 shall be added to make multiple nibbles, the most significant character representing the padding 0 if required together with the 4 most significant bits of the gNB ID shall appear first in the string, and the character representing the 4 least significant bit of the gNB ID shall appear last in the string.  |  |


## Implemented Interfaces

* Serializable


