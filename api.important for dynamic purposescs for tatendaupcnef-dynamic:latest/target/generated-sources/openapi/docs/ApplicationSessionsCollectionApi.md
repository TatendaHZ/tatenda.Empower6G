# ApplicationSessionsCollectionApi

All URIs are relative to *https://example.com/npcf-policyauthorization/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postAppSessions**](ApplicationSessionsCollectionApi.md#postAppSessions) | **POST** /app-sessions | Creates a new Individual Application Session Context resource |


<a id="postAppSessions"></a>
# **postAppSessions**
> AppSessionContext postAppSessions(appSessionContext)

Creates a new Individual Application Session Context resource

### Example
```java
// Import classes:
import autogen.pcf.api.ApiClient;
import autogen.pcf.api.ApiException;
import autogen.pcf.api.Configuration;
import autogen.pcf.api.auth.*;
import autogen.pcf.api.models.*;
import autogen.pcf.api.ApplicationSessionsCollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/npcf-policyauthorization/v1");
    
    // Configure OAuth2 access token for authorization: oAuth2ClientCredentials
    OAuth oAuth2ClientCredentials = (OAuth) defaultClient.getAuthentication("oAuth2ClientCredentials");
    oAuth2ClientCredentials.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationSessionsCollectionApi apiInstance = new ApplicationSessionsCollectionApi(defaultClient);
    AppSessionContext appSessionContext = new AppSessionContext(); // AppSessionContext | Contains the information for the creation the resource
    try {
      AppSessionContext result = apiInstance.postAppSessions(appSessionContext);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationSessionsCollectionApi#postAppSessions");
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
| **appSessionContext** | [**AppSessionContext**](AppSessionContext.md)| Contains the information for the creation the resource | |

### Return type

[**AppSessionContext**](AppSessionContext.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful creation of the resource |  * Location - The URI pointing to the resource located on the redirect target <br>  |
| **303** | See Other. The result of the HTTP POST request would be equivalent to the existing Application Session Context. |  * Location - The URI pointing to the resource located on the redirect target <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  * Retry-After - Indicates the time the AF has to wait before making a new request. It can be a non-negative integer (decimal number) indicating the number of seconds the AF has to wait before making a new request or an HTTP-date after which the AF can retry a new request. <br>  |
| **404** | Not Found |  -  |
| **411** | Length Required |  -  |
| **413** | Payload Too Large |  -  |
| **415** | Unsupported Media Type |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |
| **0** | Generic Error |  -  |

