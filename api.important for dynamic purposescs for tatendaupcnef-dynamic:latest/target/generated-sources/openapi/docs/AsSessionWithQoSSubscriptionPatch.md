

# AsSessionWithQoSSubscriptionPatch

Represents parameters to modify an AS session with specific QoS subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exterAppId** | **String** | Identifies the external Application Identifier. |  [optional] |
|**flowInfo** | [**List&lt;FlowInfo&gt;**](FlowInfo.md) | Describe the data flow which requires QoS. |  [optional] |
|**ethFlowInfo** | [**List&lt;EthFlowDescription&gt;**](EthFlowDescription.md) | Identifies Ethernet packet flows. |  [optional] |
|**qosReference** | **String** | Pre-defined QoS reference |  [optional] |
|**altQoSReferences** | **List&lt;String&gt;** | Identifies an ordered list of pre-defined QoS information. The lower the index of the array for a given entry, the higher the priority. |  [optional] |
|**disUeNotif** | **Boolean** |  |  [optional] |
|**usageThreshold** | [**UsageThresholdRm**](UsageThresholdRm.md) |  |  [optional] |
|**qosMonInfo** | [**QosMonitoringInformationRm**](QosMonitoringInformationRm.md) |  |  [optional] |
|**localNotifInd** | **Boolean** |  |  [optional] |
|**notificationDestination** | **String** | string formatted according to IETF RFC 3986 identifying a referenced resource. |  [optional] |
|**tscQosReq** | [**TscQosRequirementRm**](TscQosRequirementRm.md) |  |  [optional] |


## Implemented Interfaces

* Serializable


