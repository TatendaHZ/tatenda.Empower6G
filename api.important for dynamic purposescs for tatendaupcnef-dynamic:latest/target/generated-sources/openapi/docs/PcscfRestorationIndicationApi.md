# PcscfRestorationIndicationApi

All URIs are relative to *https://example.com/npcf-policyauthorization/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pcscfRestoration**](PcscfRestorationIndicationApi.md#pcscfRestoration) | **POST** /app-sessions/pcscf-restoration | Indicates P-CSCF restoration and does not create an Individual Application Session Context |


<a id="pcscfRestoration"></a>
# **pcscfRestoration**
> pcscfRestoration(pcscfRestorationRequestData)

Indicates P-CSCF restoration and does not create an Individual Application Session Context

### Example
```java
// Import classes:
import autogen.pcf.api.ApiClient;
import autogen.pcf.api.ApiException;
import autogen.pcf.api.Configuration;
import autogen.pcf.api.auth.*;
import autogen.pcf.api.models.*;
import autogen.pcf.api.PcscfRestorationIndicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/npcf-policyauthorization/v1");
    
    // Configure OAuth2 access token for authorization: oAuth2ClientCredentials
    OAuth oAuth2ClientCredentials = (OAuth) defaultClient.getAuthentication("oAuth2ClientCredentials");
    oAuth2ClientCredentials.setAccessToken("YOUR ACCESS TOKEN");

    PcscfRestorationIndicationApi apiInstance = new PcscfRestorationIndicationApi(defaultClient);
    PcscfRestorationRequestData pcscfRestorationRequestData = new PcscfRestorationRequestData(); // PcscfRestorationRequestData | PCSCF Restoration Indication
    try {
      apiInstance.pcscfRestoration(pcscfRestorationRequestData);
    } catch (ApiException e) {
      System.err.println("Exception when calling PcscfRestorationIndicationApi#pcscfRestoration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pcscfRestorationRequestData** | [**PcscfRestorationRequestData**](PcscfRestorationRequestData.md)| PCSCF Restoration Indication | |

### Return type

null (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The deletion is confirmed without returning additional data. |  -  |
| **307** | Temporary Redirect |  * Location - The URI pointing to the resource located on the redirect target <br>  * 3gpp-Sbi-Target-Nf-Id - Identifier of target NF (service) instance towards which the request is redirected <br>  |
| **308** | Permanent Redirect |  * Location - The URI pointing to the resource located on the redirect target <br>  * 3gpp-Sbi-Target-Nf-Id - Identifier of target NF (service) instance towards which the request is redirected <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **411** | Length Required |  -  |
| **413** | Payload Too Large |  -  |
| **415** | Unsupported Media Type |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |
| **0** | Generic Error |  -  |

