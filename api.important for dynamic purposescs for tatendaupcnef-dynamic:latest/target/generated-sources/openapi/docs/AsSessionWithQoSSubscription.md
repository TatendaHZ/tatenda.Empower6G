

# AsSessionWithQoSSubscription

Represents an individual AS session with required QoS subscription resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**self** | **String** | string formatted according to IETF RFC 3986 identifying a referenced resource. |  [optional] |
|**supportedFeatures** | **String** | A string used to indicate the features supported by an API that is used as defined in clause 6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in hexadecimal representation Each character in the string shall take a value of \&quot;0\&quot; to \&quot;9\&quot;, \&quot;a\&quot; to \&quot;f\&quot; or \&quot;A\&quot; to \&quot;F\&quot; and shall represent the support of 4 features as described in table 5.2.2-3. The most significant character representing the highest-numbered features shall appear first in the string, and the character representing features 1 to 4 shall appear last in the string. The list of features and their numbering (starting with 1) are defined separately for each API. If the string contains a lower number of characters than there are defined features for an API, all features that would be represented by characters that are not present in the string are not supported |  [optional] |
|**dnn** | **String** | String representing a Data Network as defined in clause 9A of 3GPP TS 23.003; it shall contain either a DNN Network Identifier, or a full DNN with both the Network Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots (e.g. \&quot;Label1.Label2.Label3\&quot;). |  [optional] |
|**snssai** | [**Snssai**](Snssai.md) |  |  [optional] |
|**notificationDestination** | **String** | string formatted according to IETF RFC 3986 identifying a referenced resource. |  |
|**exterAppId** | **String** | Identifies the external Application Identifier. |  [optional] |
|**flowInfo** | [**List&lt;FlowInfo&gt;**](FlowInfo.md) | Describe the data flow which requires QoS. |  [optional] |
|**ethFlowInfo** | [**List&lt;EthFlowDescription&gt;**](EthFlowDescription.md) | Identifies Ethernet packet flows. |  [optional] |
|**qosReference** | **String** | Identifies a pre-defined QoS information |  [optional] |
|**altQoSReferences** | **List&lt;String&gt;** | Identifies an ordered list of pre-defined QoS information. The lower the index of the array for a given entry, the higher the priority. |  [optional] |
|**disUeNotif** | **Boolean** |  |  [optional] |
|**ueIpv4Addr** | **String** | string identifying a Ipv4 address formatted in the \&quot;dotted decimal\&quot; notation as defined in IETF RFC 1166. |  [optional] |
|**ipDomain** | **String** |  |  [optional] |
|**ueIpv6Addr** | **String** | string identifying a Ipv6 address formatted according to clause 4 in IETF RFC 5952. The mixed Ipv4 Ipv6 notation according to clause 5 of IETF RFC 5952 shall not be used. |  [optional] |
|**macAddr** | **String** | String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042 |  [optional] |
|**usageThreshold** | [**UsageThreshold**](UsageThreshold.md) |  |  [optional] |
|**sponsorInfo** | [**SponsorInformation**](SponsorInformation.md) |  |  [optional] |
|**qosMonInfo** | [**QosMonitoringInformation**](QosMonitoringInformation.md) |  |  [optional] |
|**localNotifInd** | **Boolean** |  |  [optional] |
|**tscQosReq** | [**TscQosRequirement**](TscQosRequirement.md) |  |  [optional] |
|**requestTestNotification** | **Boolean** | Set to true by the SCS/AS to request the SCEF to send a test notification as defined in subclause 5.2.5.3. Set to false or omitted otherwise. |  [optional] |
|**websockNotifConfig** | [**WebsockNotifConfig**](WebsockNotifConfig.md) |  |  [optional] |


## Implemented Interfaces

* Serializable


