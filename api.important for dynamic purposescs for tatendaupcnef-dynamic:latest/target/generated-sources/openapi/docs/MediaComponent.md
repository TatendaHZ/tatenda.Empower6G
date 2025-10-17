

# MediaComponent

Identifies a media component.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afAppId** | **String** | Contains an AF application identifier. |  [optional] |
|**afRoutReq** | [**AfRoutingRequirement**](AfRoutingRequirement.md) |  |  [optional] |
|**qosReference** | **String** |  |  [optional] |
|**disUeNotif** | **Boolean** |  |  [optional] |
|**altSerReqs** | **List&lt;String&gt;** |  |  [optional] |
|**contVer** | **Integer** | Represents the content version of some content. |  [optional] |
|**codecs** | **List&lt;String&gt;** |  |  [optional] |
|**desMaxLatency** | **Float** | string with format \&quot;float\&quot; as defined in OpenAPI. |  [optional] |
|**desMaxLoss** | **Float** | string with format \&quot;float\&quot; as defined in OpenAPI. |  [optional] |
|**flusId** | **String** |  |  [optional] |
|**fStatus** | **FlowStatus** |  |  [optional] |
|**marBwDl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**marBwUl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**maxPacketLossRateDl** | **Integer** | This data type is defined in the same way as the \&quot;PacketLossRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property |  [optional] |
|**maxPacketLossRateUl** | **Integer** | This data type is defined in the same way as the \&quot;PacketLossRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property |  [optional] |
|**maxSuppBwDl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**maxSuppBwUl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**medCompN** | **Integer** |  |  |
|**medSubComps** | [**Map&lt;String, MediaSubComponent&gt;**](MediaSubComponent.md) | Contains the requested bitrate and filters for the set of service data flows identified by their common flow identifier. The key of the map is the fNum attribute. |  [optional] |
|**medType** | **MediaType** |  |  [optional] |
|**minDesBwDl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**minDesBwUl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**mirBwDl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**mirBwUl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**preemptCap** | **PreemptionCapability** |  |  [optional] |
|**preemptVuln** | **PreemptionVulnerability** |  |  [optional] |
|**prioSharingInd** | **PrioritySharingIndicator** |  |  [optional] |
|**resPrio** | **ReservPriority** |  |  [optional] |
|**rrBw** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**rsBw** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**sharingKeyDl** | **Integer** | Integer where the allowed values correspond to the value range of an unsigned 32-bit integer. |  [optional] |
|**sharingKeyUl** | **Integer** | Integer where the allowed values correspond to the value range of an unsigned 32-bit integer. |  [optional] |
|**tsnQos** | [**TsnQosContainer**](TsnQosContainer.md) |  |  [optional] |
|**tscaiInputDl** | [**TscaiInputContainer**](TscaiInputContainer.md) |  |  [optional] |
|**tscaiInputUl** | [**TscaiInputContainer**](TscaiInputContainer.md) |  |  [optional] |
|**tscaiTimeDom** | **Integer** | Unsigned Integer, i.e. only value 0 and integers above 0 are permissible. |  [optional] |


## Implemented Interfaces

* Serializable


