

# AppSessionContextReqData

Identifies the service requirements of an Individual Application Session Context.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afAppId** | **String** | Contains an AF application identifier. |  [optional] |
|**afChargId** | **String** | Application provided charging identifier allowing correlation of charging information. |  [optional] |
|**afReqData** | **AfRequestedData** |  |  [optional] |
|**afRoutReq** | [**AfRoutingRequirement**](AfRoutingRequirement.md) |  |  [optional] |
|**aspId** | **String** | Contains an identity of an application service provider. |  [optional] |
|**bdtRefId** | **String** | string identifying a BDT Reference ID as defined in subclause 5.3.3 of 3GPP TS 29.154. |  [optional] |
|**dnn** | **String** | String representing a Data Network as defined in clause 9A of 3GPP TS 23.003; it shall contain either a DNN Network Identifier, or a full DNN with both the Network Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots (e.g. \&quot;Label1.Label2.Label3\&quot;). |  [optional] |
|**evSubsc** | [**EventsSubscReqData**](EventsSubscReqData.md) |  |  [optional] |
|**mcpttId** | **String** | indication of MCPTT service request |  [optional] |
|**mcVideoId** | **String** | indication of MCVideo service request |  [optional] |
|**medComponents** | [**Map&lt;String, MediaComponent&gt;**](MediaComponent.md) | Contains media component information. The key of the map is the medCompN attribute. |  [optional] |
|**ipDomain** | **String** |  |  [optional] |
|**mpsAction** | **MpsAction** |  |  [optional] |
|**mpsId** | **String** | indication of MPS service request |  [optional] |
|**mcsId** | **String** | indication of MCS service request |  [optional] |
|**preemptControlInfo** | **PreemptionControlInformation** |  |  [optional] |
|**resPrio** | **ReservPriority** |  |  [optional] |
|**servInfStatus** | **ServiceInfoStatus** |  |  [optional] |
|**notifUri** | **String** | String providing an URI formatted according to RFC 3986 |  |
|**servUrn** | **String** | Contains values of the service URN and may include subservices. |  [optional] |
|**sliceInfo** | [**Snssai**](Snssai.md) |  |  [optional] |
|**sponId** | **String** | Contains an identity of a sponsor. |  [optional] |
|**sponStatus** | **SponsoringStatus** |  |  [optional] |
|**supi** | **String** | String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause 2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \&quot;imsi-&lt;imsi&gt;\&quot;, where &lt;imsi&gt; shall be formatted according to clause 2.2 of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \&quot;nai-&lt;nai&gt;, where &lt;nai&gt; shall be formatted according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \&quot;gci-&lt;gci&gt;\&quot;, where &lt;gci&gt; shall be formatted according to clause 28.15.2 of 3GPP TS 23.003.  - for a GLI \&quot;gli-&lt;gli&gt;\&quot;, where &lt;gli&gt; shall be formatted according to clause 28.16.2 of 3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall only contain characters allowed according to the \&quot;lower-with-hyphen\&quot; naming convention defined in 3GPP TS 29.501.  |  [optional] |
|**gpsi** | **String** | String identifying a Gpsi shall contain either an External Id or an MSISDN. It shall be formatted as follows -External Identifier&#x3D; \&quot;extid-&lt;extid&gt;, where &lt;extid&gt; shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an External Identifier. |  [optional] |
|**suppFeat** | **String** | A string used to indicate the features supported by an API that is used as defined in clause 6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in hexadecimal representation Each character in the string shall take a value of \&quot;0\&quot; to \&quot;9\&quot;, \&quot;a\&quot; to \&quot;f\&quot; or \&quot;A\&quot; to \&quot;F\&quot; and shall represent the support of 4 features as described in table 5.2.2-3. The most significant character representing the highest-numbered features shall appear first in the string, and the character representing features 1 to 4 shall appear last in the string. The list of features and their numbering (starting with 1) are defined separately for each API. If the string contains a lower number of characters than there are defined features for an API, all features that would be represented by characters that are not present in the string are not supported |  |
|**ueIpv4** | **String** | String identifying a IPv4 address formatted in the \&quot;dotted decimal\&quot; notation as defined in RFC 1166. |  [optional] |
|**ueIpv6** | [**Ipv6Addr**](Ipv6Addr.md) |  |  [optional] |
|**ueMac** | **String** | String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042 |  [optional] |
|**tsnBridgeManCont** | [**BridgeManagementContainer**](BridgeManagementContainer.md) |  |  [optional] |
|**tsnPortManContDstt** | [**PortManagementContainer**](PortManagementContainer.md) |  |  [optional] |
|**tsnPortManContNwtts** | [**List&lt;PortManagementContainer&gt;**](PortManagementContainer.md) |  |  [optional] |


## Implemented Interfaces

* Serializable


