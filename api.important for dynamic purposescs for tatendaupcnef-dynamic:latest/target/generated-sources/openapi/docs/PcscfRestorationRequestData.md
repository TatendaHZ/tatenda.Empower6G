

# PcscfRestorationRequestData

Indicates P-CSCF restoration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnn** | **String** | String representing a Data Network as defined in clause 9A of 3GPP TS 23.003; it shall contain either a DNN Network Identifier, or a full DNN with both the Network Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots (e.g. \&quot;Label1.Label2.Label3\&quot;). |  [optional] |
|**ipDomain** | **String** |  |  [optional] |
|**sliceInfo** | [**Snssai**](Snssai.md) |  |  [optional] |
|**supi** | **String** | String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause 2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \&quot;imsi-&lt;imsi&gt;\&quot;, where &lt;imsi&gt; shall be formatted according to clause 2.2 of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \&quot;nai-&lt;nai&gt;, where &lt;nai&gt; shall be formatted according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \&quot;gci-&lt;gci&gt;\&quot;, where &lt;gci&gt; shall be formatted according to clause 28.15.2 of 3GPP TS 23.003.  - for a GLI \&quot;gli-&lt;gli&gt;\&quot;, where &lt;gli&gt; shall be formatted according to clause 28.16.2 of 3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall only contain characters allowed according to the \&quot;lower-with-hyphen\&quot; naming convention defined in 3GPP TS 29.501.  |  [optional] |
|**ueIpv4** | **String** | String identifying a IPv4 address formatted in the \&quot;dotted decimal\&quot; notation as defined in RFC 1166. |  [optional] |
|**ueIpv6** | [**Ipv6Addr**](Ipv6Addr.md) |  |  [optional] |


## Implemented Interfaces

* Serializable


