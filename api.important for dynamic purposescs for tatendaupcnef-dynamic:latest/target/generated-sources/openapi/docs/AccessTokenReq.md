

# AccessTokenReq

Contains information related to the access token request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**grantType** | [**GrantTypeEnum**](#GrantTypeEnum) |  |  |
|**nfInstanceId** | **UUID** | String uniquely identifying a NF instance. The format of the NF Instance ID shall be a Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122. |  |
|**nfType** | **NFType** |  |  [optional] |
|**targetNfType** | **NFType** |  |  [optional] |
|**scope** | **String** |  |  |
|**targetNfInstanceId** | **UUID** | String uniquely identifying a NF instance. The format of the NF Instance ID shall be a Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122. |  [optional] |
|**requesterPlmn** | [**PlmnId**](PlmnId.md) |  |  [optional] |
|**requesterPlmnList** | [**List&lt;PlmnId&gt;**](PlmnId.md) |  |  [optional] |
|**requesterSnssaiList** | [**List&lt;Snssai&gt;**](Snssai.md) |  |  [optional] |
|**requesterFqdn** | **String** | Fully Qualified Domain Name |  [optional] |
|**requesterSnpnList** | [**List&lt;PlmnIdNid&gt;**](PlmnIdNid.md) |  |  [optional] |
|**targetPlmn** | [**PlmnId**](PlmnId.md) |  |  [optional] |
|**targetSnssaiList** | [**List&lt;Snssai&gt;**](Snssai.md) |  |  [optional] |
|**targetNsiList** | **List&lt;String&gt;** |  |  [optional] |
|**targetNfSetId** | **String** | NF Set Identifier (see clause 28.12 of 3GPP TS 23.003), formatted as the following string \&quot; set&lt;Set ID&gt;.&lt;nftype&gt;set.5gc.mnc&lt;MNC&gt;.mcc&lt;MCC&gt;\&quot;, or \&quot;set&lt;SetID&gt;. &lt;NFType&gt;set.5gc.nid&lt;NID&gt;.mnc&lt;MNC&gt;.mcc&lt;MCC&gt;\&quot; with &lt;MCC&gt; encoded as defined in clause 5.4.2 (\&quot;Mcc\&quot; data type definition) &lt;MNC&gt; encoded as defined in clause 5.4.2 (\&quot;Mnc\&quot; data type definition) &lt;NFType&gt; encoded as a value defined in Table 6.1.6.3.3-1 of 3GPP TS 29.510 but with lower case characters &lt;Set ID&gt; encoded as a string of characters consisting of alphabetic characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that shall end with either an alphabetic character or a digit. |  [optional] |
|**targetNfServiceSetId** | **String** | NF Service Set Identifier (see clause 28.12 of 3GPP TS 23.003) formatted as the following string  \&quot; set&lt;Set ID&gt;.sn&lt;Service Name&gt;.nfi&lt;NF Instance ID&gt;.5gc.mnc&lt;MNC&gt;.mcc&lt;MCC&gt;\&quot;&gt;\&quot;, or \&quot;set&lt;SetID&gt;.sn&lt;ServiceName&gt;.nfi&lt;NFInstanceID&gt;.5gc.nid&lt;NID&gt;.mnc&lt;MNC&gt;.mcc&lt;MCC&gt;\&quot; with &lt;MCC&gt; encoded as defined in clause 5.4.2 (\&quot;Mcc\&quot; data type definition)  &lt;MNC&gt; encoded as defined in clause 5.4.2 (\&quot;Mnc\&quot; data type definition)  &lt;NID&gt; encoded as defined in clause 5.4.2 (\&quot;Nid\&quot; data type definition) &lt;NFInstanceId&gt; encoded as defined in clause 5.3.2 &lt;ServiceName&gt; encoded as defined in 3GPP TS 29.510 &lt;Set ID&gt; encoded as a string of characters consisting of alphabetic characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that shall end with either an alphabetic character or a digit. |  [optional] |
|**hnrfAccessTokenUri** | **String** | String providing an URI formatted according to RFC 3986 |  [optional] |



## Enum: GrantTypeEnum

| Name | Value |
|---- | -----|
| CLIENT_CREDENTIALS | &quot;client_credentials&quot; |


## Implemented Interfaces

* Serializable


