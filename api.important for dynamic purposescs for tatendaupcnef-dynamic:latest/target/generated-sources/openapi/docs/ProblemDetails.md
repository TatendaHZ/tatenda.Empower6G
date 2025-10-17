

# ProblemDetails

Provides additional information in an error response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | String providing an URI formatted according to RFC 3986 |  [optional] |
|**title** | **String** | A short, human-readable summary of the problem type. |  [optional] |
|**status** | **Integer** | The HTTP status code for this occurrence of the problem. |  [optional] |
|**detail** | **String** | A human-readable explanation specific to this occurrence of the problem. |  [optional] |
|**instance** | **String** | String providing an URI formatted according to RFC 3986 |  [optional] |
|**cause** | **String** | A machine-readable application error cause specific to this occurrence of the problem. This IE should be present and provide application-related error information, if available. |  [optional] |
|**invalidParams** | [**List&lt;InvalidParam&gt;**](InvalidParam.md) | Description of invalid parameters, for a request rejected due to invalid parameters. |  [optional] |
|**supportedFeatures** | **String** | A string used to indicate the features supported by an API that is used as defined in clause 6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in hexadecimal representation Each character in the string shall take a value of \&quot;0\&quot; to \&quot;9\&quot;, \&quot;a\&quot; to \&quot;f\&quot; or \&quot;A\&quot; to \&quot;F\&quot; and shall represent the support of 4 features as described in table 5.2.2-3. The most significant character representing the highest-numbered features shall appear first in the string, and the character representing features 1 to 4 shall appear last in the string. The list of features and their numbering (starting with 1) are defined separately for each API. If the string contains a lower number of characters than there are defined features for an API, all features that would be represented by characters that are not present in the string are not supported |  [optional] |
|**accessTokenError** | [**AccessTokenErr**](AccessTokenErr.md) |  |  [optional] |
|**accessTokenRequest** | [**AccessTokenReq**](AccessTokenReq.md) |  |  [optional] |
|**nrfId** | **String** | It contain the Identity (i.e. FQDN) of the NRF that rejected the access token request. |  [optional] |


## Implemented Interfaces

* Serializable


