

# MediaComponentRm

This data type is defined in the same way as the MediaComponent data type, but with the OpenAPI nullable property set to true

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afAppId** | **String** | Contains an AF application identifier. |  [optional] |
|**afRoutReq** | [**AfRoutingRequirementRm**](AfRoutingRequirementRm.md) |  |  [optional] |
|**qosReference** | **String** |  |  [optional] |
|**altSerReqs** | **List&lt;String&gt;** |  |  [optional] |
|**disUeNotif** | **Boolean** |  |  [optional] |
|**contVer** | **Integer** | Represents the content version of some content. |  [optional] |
|**codecs** | **List&lt;String&gt;** |  |  [optional] |
|**desMaxLatency** | **Float** | string with format \&quot;float\&quot; as defined in OpenAPI with the OpenAPI defined \&quot;nullable&#x3D;true\&quot; property. |  [optional] |
|**desMaxLoss** | **Float** | string with format \&quot;float\&quot; as defined in OpenAPI with the OpenAPI defined \&quot;nullable&#x3D;true\&quot; property. |  [optional] |
|**flusId** | **String** |  |  [optional] |
|**fStatus** | **FlowStatus** |  |  [optional] |
|**marBwDl** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**marBwUl** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**maxPacketLossRateDl** | **Integer** | This data type is defined in the same way as the \&quot;PacketLossRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property |  [optional] |
|**maxPacketLossRateUl** | **Integer** | This data type is defined in the same way as the \&quot;PacketLossRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property |  [optional] |
|**maxSuppBwDl** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**maxSuppBwUl** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**medCompN** | **Integer** |  |  |
|**medSubComps** | [**Map&lt;String, MediaSubComponentRm&gt;**](MediaSubComponentRm.md) | Contains the requested bitrate and filters for the set of service data flows identified by their common flow identifier. The key of the map is the fNum attribute. |  [optional] |
|**medType** | **MediaType** |  |  [optional] |
|**minDesBwDl** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**minDesBwUl** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**mirBwDl** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**mirBwUl** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**preemptCap** | **PreemptionCapability** |  |  [optional] |
|**preemptVuln** | **PreemptionVulnerability** |  |  [optional] |
|**prioSharingInd** | **PrioritySharingIndicator** |  |  [optional] |
|**resPrio** | **ReservPriority** |  |  [optional] |
|**rrBw** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**rsBw** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**sharingKeyDl** | **Integer** | Integer where the allowed values correspond to the value range of an unsigned 32-bit integer with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**sharingKeyUl** | **Integer** | Integer where the allowed values correspond to the value range of an unsigned 32-bit integer with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**tsnQos** | [**TsnQosContainerRm**](TsnQosContainerRm.md) |  |  [optional] |
|**tscaiInputDl** | [**TscaiInputContainer**](TscaiInputContainer.md) |  |  [optional] |
|**tscaiInputUl** | [**TscaiInputContainer**](TscaiInputContainer.md) |  |  [optional] |
|**tscaiTimeDom** | **Integer** | Unsigned Integer, i.e. only value 0 and integers above 0 are permissible. |  [optional] |


## Implemented Interfaces

* Serializable


