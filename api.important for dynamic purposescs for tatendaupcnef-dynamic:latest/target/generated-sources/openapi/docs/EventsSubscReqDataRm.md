

# EventsSubscReqDataRm

this data type is defined in the same way as the EventsSubscReqData data type, but with the OpenAPI nullable property set to true.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**events** | [**List&lt;AfEventSubscription&gt;**](AfEventSubscription.md) |  |  |
|**notifUri** | **String** | String providing an URI formatted according to RFC 3986 |  [optional] |
|**reqQosMonParams** | **List&lt;RequestedQosMonitoringParameter&gt;** |  |  [optional] |
|**qosMon** | [**QosMonitoringInformationRm**](QosMonitoringInformationRm.md) |  |  [optional] |
|**reqAnis** | **List&lt;RequiredAccessInfo&gt;** |  |  [optional] |
|**usgThres** | [**UsageThresholdRm**](UsageThresholdRm.md) |  |  [optional] |
|**notifCorreId** | **String** |  |  [optional] |
|**directNotifInd** | **Boolean** |  |  [optional] |


## Implemented Interfaces

* Serializable


