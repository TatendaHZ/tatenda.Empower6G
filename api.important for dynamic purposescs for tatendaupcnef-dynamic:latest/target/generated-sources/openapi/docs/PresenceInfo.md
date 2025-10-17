

# PresenceInfo

If the additionalPraId IE is present, this IE shall state the presence information of the UE for the individual PRA identified by the additionalPraId IE; If the additionalPraId IE is not present, this IE shall state the presence information of the UE for the PRA identified by the praId IE.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**praId** | **String** | Represents an identifier of the Presence Reporting Area (see clause 28.10 of 3GPP TS 23.003. This IE shall be present if the Area of Interest subscribed or reported is a Presence Reporting Area or a Set of Core Network predefined Presence Reporting Areas. When present, it shall be encoded as a string representing an integer in the following ranges: 0 to 8 388 607 for UE-dedicated PRA 8 388 608 to 16 777 215 for Core Network predefined PRA Examples: PRA ID 123 is encoded as \&quot;123\&quot; PRA ID 11 238 660 is encoded as \&quot;11238660\&quot;  |  [optional] |
|**additionalPraId** | **String** | This IE may be present if the praId IE is present and if it contains a PRA identifier referring to a set of Core Network predefined Presence Reporting Areas. When present, this IE shall contain a PRA Identifier of an individual PRA within the Set of Core Network predefined Presence Reporting Areas indicated by the praId IE.  |  [optional] |
|**presenceState** | **PresenceState** |  |  [optional] |
|**trackingAreaList** | [**List&lt;Tai&gt;**](Tai.md) | Represents the list of tracking areas that constitutes the area. This IE shall be present if the subscription or the event report is for tracking UE presence in the tracking areas. For non 3GPP access the TAI shall be the N3GPP TAI. |  [optional] |
|**ecgiList** | [**List&lt;Ecgi&gt;**](Ecgi.md) | Represents the list of EUTRAN cell Ids that constitutes the area. This IE shall be present if the Area of Interest subscribed is a list of EUTRAN cell Ids. |  [optional] |
|**ncgiList** | [**List&lt;Ncgi&gt;**](Ncgi.md) | Represents the list of NR cell Ids that constitutes the area. This IE shall be present if the Area of Interest subscribed is a list of NR cell Ids. |  [optional] |
|**globalRanNodeIdList** | [**List&lt;GlobalRanNodeId&gt;**](GlobalRanNodeId.md) | Represents the list of NG RAN node identifiers that constitutes the area. This IE shall be present if the Area of Interest subscribed is a list of NG RAN node identifiers. |  [optional] |
|**globaleNbIdList** | [**List&lt;GlobalRanNodeId&gt;**](GlobalRanNodeId.md) | Represents the list of eNodeB identifiers that constitutes the area. This IE shall be present if the Area of Interest subscribed is a list of eNodeB identifiers. |  [optional] |


## Implemented Interfaces

* Serializable


