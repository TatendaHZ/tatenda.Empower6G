

# EventsSubscReqData

Identifies the events the application subscribes to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**events** | [**List&lt;AfEventSubscription&gt;**](AfEventSubscription.md) |  |  |
|**notifUri** | **String** | String providing an URI formatted according to RFC 3986 |  [optional] |
|**reqQosMonParams** | **List&lt;RequestedQosMonitoringParameter&gt;** |  |  [optional] |
|**qosMon** | [**QosMonitoringInformation**](QosMonitoringInformation.md) |  |  [optional] |
|**reqAnis** | **List&lt;RequiredAccessInfo&gt;** |  |  [optional] |
|**usgThres** | [**UsageThreshold**](UsageThreshold.md) |  |  [optional] |
|**notifCorreId** | **String** |  |  [optional] |
|**afAppIds** | **List&lt;String&gt;** |  |  [optional] |
|**directNotifInd** | **Boolean** |  |  [optional] |


## Implemented Interfaces

* Serializable


