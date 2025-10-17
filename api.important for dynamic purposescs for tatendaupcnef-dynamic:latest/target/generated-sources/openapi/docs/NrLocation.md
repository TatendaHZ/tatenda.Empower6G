

# NrLocation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tai** | [**Tai**](Tai.md) |  |  |
|**ncgi** | [**Ncgi**](Ncgi.md) |  |  |
|**ageOfLocationInformation** | **Integer** | The value represents the elapsed time in minutes since the last network contact of the mobile station.  Value \&quot;0\&quot; indicates that the location information was obtained after a successful paging procedure for Active Location Retrieval when the UE is in idle mode or after a successful NG-RAN location reporting procedure with the eNB when the UE is in connected mode. Any other value than \&quot;0\&quot; indicates that the location information is the last known one. See 3GPP TS 29.002 clause 17.7.8.  |  [optional] |
|**ueLocationTimestamp** | **OffsetDateTime** | string with format \&quot;date-time\&quot; as defined in OpenAPI. |  [optional] |
|**geographicalInformation** | **String** | Refer to geographical Information. See 3GPP TS 23.032 clause 7.3.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used. |  [optional] |
|**geodeticInformation** | **String** | Refers to Calling Geodetic Location. See ITU-T Recommendation Q.763 (1999) [24] clause 3.88.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used. |  [optional] |
|**globalGnbId** | [**GlobalRanNodeId**](GlobalRanNodeId.md) |  |  [optional] |


## Implemented Interfaces

* Serializable


