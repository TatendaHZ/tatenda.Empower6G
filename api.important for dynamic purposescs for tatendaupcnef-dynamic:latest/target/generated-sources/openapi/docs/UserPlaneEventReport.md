

# UserPlaneEventReport

Represents an event report for user plane.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**event** | **UserPlaneEvent** |  |  |
|**accumulatedUsage** | [**AccumulatedUsage**](AccumulatedUsage.md) |  |  [optional] |
|**flowIds** | **List&lt;Integer&gt;** | Identifies the IP flows that were sent during event subscription |  [optional] |
|**appliedQosRef** | **String** | The currently applied QoS reference. Applicable for event QOS_NOT_GUARANTEED or SUCCESSFUL_RESOURCES_ALLOCATION. |  [optional] |
|**qosMonReports** | [**List&lt;QosMonitoringReport&gt;**](QosMonitoringReport.md) | Contains the QoS Monitoring Reporting information |  [optional] |


## Implemented Interfaces

* Serializable


