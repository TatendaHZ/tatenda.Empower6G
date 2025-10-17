

# AppSessionContextUpdateData

Identifies the modifications to the \"ascReqData\" property of an Individual Application Session Context which may include the modifications to the sub-resource Events Subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afAppId** | **String** | Contains an AF application identifier. |  [optional] |
|**afRoutReq** | [**AfRoutingRequirementRm**](AfRoutingRequirementRm.md) |  |  [optional] |
|**aspId** | **String** | Contains an identity of an application service provider. |  [optional] |
|**bdtRefId** | **String** | string identifying a BDT Reference ID as defined in subclause 5.3.3 of 3GPP TS 29.154. |  [optional] |
|**evSubsc** | [**EventsSubscReqDataRm**](EventsSubscReqDataRm.md) |  |  [optional] |
|**mcpttId** | **String** | indication of MCPTT service request |  [optional] |
|**mcVideoId** | **String** | indication of modification of MCVideo service |  [optional] |
|**medComponents** | [**Map&lt;String, MediaComponentRm&gt;**](MediaComponentRm.md) | Contains media component information. The key of the map is the medCompN attribute. |  [optional] |
|**mpsAction** | **MpsAction** |  |  [optional] |
|**mpsId** | **String** | indication of MPS service request |  [optional] |
|**mcsId** | **String** | indication of MCS service request |  [optional] |
|**preemptControlInfo** | **PreemptionControlInformation** |  |  [optional] |
|**resPrio** | **ReservPriority** |  |  [optional] |
|**servInfStatus** | **ServiceInfoStatus** |  |  [optional] |
|**sipForkInd** | **SipForkingIndication** |  |  [optional] |
|**sponId** | **String** | Contains an identity of a sponsor. |  [optional] |
|**sponStatus** | **SponsoringStatus** |  |  [optional] |
|**tsnBridgeManCont** | [**BridgeManagementContainer**](BridgeManagementContainer.md) |  |  [optional] |
|**tsnPortManContDstt** | [**PortManagementContainer**](PortManagementContainer.md) |  |  [optional] |
|**tsnPortManContNwtts** | [**List&lt;PortManagementContainer&gt;**](PortManagementContainer.md) |  |  [optional] |


## Implemented Interfaces

* Serializable


