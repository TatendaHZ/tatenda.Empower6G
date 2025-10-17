

# MediaSubComponentRm

This data type is defined in the same way as the MediaSubComponent data type, but with the OpenAPI nullable property set to true. Removable attributes marBwDl and marBwUl are defined with the corresponding removable data type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afSigProtocol** | **AfSigProtocol** |  |  [optional] |
|**ethfDescs** | [**List&lt;EthFlowDescription&gt;**](EthFlowDescription.md) |  |  [optional] |
|**fNum** | **Integer** |  |  |
|**fDescs** | **List&lt;String&gt;** |  |  [optional] |
|**fStatus** | **FlowStatus** |  |  [optional] |
|**marBwDl** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**marBwUl** | **String** | This data type is defined in the same way as the \&quot;BitRate\&quot; data type, but with the OpenAPI \&quot;nullable&#x3D; true\&quot; property. |  [optional] |
|**tosTrCl** | **String** | this data type is defined in the same way as the TosTrafficClass data type, but with the OpenAPI nullable property set to true |  [optional] |
|**flowUsage** | **FlowUsage** |  |  [optional] |


## Implemented Interfaces

* Serializable


