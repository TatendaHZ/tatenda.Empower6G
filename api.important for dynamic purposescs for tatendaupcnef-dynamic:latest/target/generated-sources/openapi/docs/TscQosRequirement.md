

# TscQosRequirement

Represents QoS requirements for time sensitive communication.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reqGbrDl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**reqGbrUl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**reqMbrDl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**reqMbrUl** | **String** | String representing a bit rate that shall be formatted as follows. |  [optional] |
|**maxTscBurstSize** | **Integer** | Unsigned integer indicating Maximum Data Burst Volume (see clauses 5.7.3.7 and 5.7.4 of 3GPP TS 23.501), expressed in Bytes. |  [optional] |
|**req5Gsdelay** | **Integer** | Unsigned integer indicating Packet Delay Budget (see clauses 5.7.3.4 and 5.7.4 of 3GPP TS 23.501), expressed in milliseconds. |  [optional] |
|**tscaiTimeDom** | **Integer** | Unsigned Integer, i.e. only value 0 and integers above 0 are permissible. |  [optional] |
|**tscaiInputDl** | [**TscaiInputContainer**](TscaiInputContainer.md) |  |  [optional] |
|**tscaiInputUl** | [**TscaiInputContainer**](TscaiInputContainer.md) |  |  [optional] |


## Implemented Interfaces

* Serializable


