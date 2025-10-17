

# EventsNotification

describes the notification of a matched event

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adReports** | [**List&lt;AppDetectionReport&gt;**](AppDetectionReport.md) | includes the detected application report. |  [optional] |
|**accessType** | **AccessType** |  |  [optional] |
|**addAccessInfo** | [**AdditionalAccessInfo**](AdditionalAccessInfo.md) |  |  [optional] |
|**relAccessInfo** | [**AdditionalAccessInfo**](AdditionalAccessInfo.md) |  |  [optional] |
|**anChargAddr** | [**AccNetChargingAddress**](AccNetChargingAddress.md) |  |  [optional] |
|**anChargIds** | [**List&lt;AccessNetChargingIdentifier&gt;**](AccessNetChargingIdentifier.md) |  |  [optional] |
|**anGwAddr** | [**AnGwAddress**](AnGwAddress.md) |  |  [optional] |
|**evSubsUri** | **String** | String providing an URI formatted according to RFC 3986 |  |
|**evNotifs** | [**List&lt;AfEventNotification&gt;**](AfEventNotification.md) |  |  |
|**failedResourcAllocReports** | [**List&lt;ResourcesAllocationInfo&gt;**](ResourcesAllocationInfo.md) |  |  [optional] |
|**succResourcAllocReports** | [**List&lt;ResourcesAllocationInfo&gt;**](ResourcesAllocationInfo.md) |  |  [optional] |
|**noNetLocSupp** | **NetLocAccessSupport** |  |  [optional] |
|**outOfCredReports** | [**List&lt;OutOfCreditInformation&gt;**](OutOfCreditInformation.md) |  |  [optional] |
|**plmnId** | [**PlmnIdNid**](PlmnIdNid.md) |  |  [optional] |
|**qncReports** | [**List&lt;QosNotificationControlInfo&gt;**](QosNotificationControlInfo.md) |  |  [optional] |
|**qosMonReports** | [**List&lt;QosMonitoringReport&gt;**](QosMonitoringReport.md) |  |  [optional] |
|**ranNasRelCauses** | [**List&lt;RanNasRelCause&gt;**](RanNasRelCause.md) | Contains the RAN and/or NAS release cause. |  [optional] |
|**ratType** | **RatType** |  |  [optional] |
|**satBackhaulCategory** | **SatelliteBackhaulCategory** |  |  [optional] |
|**ueLoc** | [**UserLocation**](UserLocation.md) |  |  [optional] |
|**ueTimeZone** | **String** | String with format \&quot;&lt;time-numoffset&gt;\&quot; optionally appended by \&quot;&lt;daylightSavingTime&gt;\&quot;, where -  &lt;time-numoffset&gt; shall represent the time zone adjusted for daylight saving time and be encoded as time-numoffset as defined in clause 5.6 of IETF RFC 3339; - &lt;daylightSavingTime&gt; shall represent the adjustment that has been made and shall be encoded as \&quot;+1\&quot; or \&quot;+2\&quot; for a +1 or +2 hours adjustment. The example is for 8 hours behind UTC, +1 hour adjustment for Daylight Saving Time. |  [optional] |
|**usgRep** | [**AccumulatedUsage**](AccumulatedUsage.md) |  |  [optional] |
|**tsnBridgeManCont** | [**BridgeManagementContainer**](BridgeManagementContainer.md) |  |  [optional] |
|**tsnPortManContDstt** | [**PortManagementContainer**](PortManagementContainer.md) |  |  [optional] |
|**tsnPortManContNwtts** | [**List&lt;PortManagementContainer&gt;**](PortManagementContainer.md) |  |  [optional] |


## Implemented Interfaces

* Serializable


