

# Snssai

When Snssai needs to be converted to string (e.g. when used in maps as key), the string shall be composed of one to three digits \"sst\" optionally followed by \"-\" and 6 hexadecimal digits \"sd\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sst** | **Integer** | Unsigned integer, within the range 0 to 255, representing the Slice/Service Type. It indicates the expected Network Slice behaviour in terms of features and services.  Values 0 to 127 correspond to the standardized SST range. Values 128 to 255 correspond to the Operator-specific range. See clause 28.4.2 of 3GPP TS 23.003.  Standardized values are defined in clause 5.15.2.2 of 3GPP TS 23.501.  |  |
|**sd** | **String** | 3-octet string, representing the Slice Differentiator, in hexadecimal representation. Each character in the string shall take a value of \&quot;0\&quot; to \&quot;9\&quot;, \&quot;a\&quot; to \&quot;f\&quot; or \&quot;A\&quot; to \&quot;F\&quot; and shall represent 4 bits. The most significant character representing the 4 most significant bits of the SD shall appear first in the string, and the character representing the 4 least significant bit of the SD shall appear last in the string.  This is an optional parameter that complements the Slice/Service type(s) to allow to differentiate amongst multiple Network Slices of the same Slice/Service type. This IE shall be absent if no SD value is associated with the SST.  |  [optional] |


## Implemented Interfaces

* Serializable


