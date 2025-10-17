

# AfRoutingRequirementRm

this data type is defined in the same way as the AfRoutingRequirement data type, but with the OpenAPI nullable property set to true and the spVal and tempVals attributes defined as removable.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appReloc** | **Boolean** |  |  [optional] |
|**routeToLocs** | [**List&lt;RouteToLocation&gt;**](RouteToLocation.md) |  |  [optional] |
|**spVal** | [**SpatialValidityRm**](SpatialValidityRm.md) |  |  [optional] |
|**tempVals** | [**List&lt;TemporalValidity&gt;**](TemporalValidity.md) |  |  [optional] |
|**upPathChgSub** | [**UpPathChgEvent**](UpPathChgEvent.md) |  |  [optional] |
|**addrPreserInd** | **Boolean** |  |  [optional] |


## Implemented Interfaces

* Serializable


