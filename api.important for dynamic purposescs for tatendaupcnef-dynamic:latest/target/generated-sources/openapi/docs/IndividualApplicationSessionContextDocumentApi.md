# IndividualApplicationSessionContextDocumentApi

All URIs are relative to *https://example.com/npcf-policyauthorization/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAppSession**](IndividualApplicationSessionContextDocumentApi.md#deleteAppSession) | **POST** /app-sessions/{appSessionId}/delete | Deletes an existing Individual Application Session Context |
| [**getAppSession**](IndividualApplicationSessionContextDocumentApi.md#getAppSession) | **GET** /app-sessions/{appSessionId} | Reads an existing Individual Application Session Context |
| [**modAppSession**](IndividualApplicationSessionContextDocumentApi.md#modAppSession) | **PATCH** /app-sessions/{appSessionId} | Modifies an existing Individual Application Session Context |


<a id="deleteAppSession"></a>
# **deleteAppSession**
> AppSessionContext deleteAppSession(appSessionId, eventsSubscReqData)

Deletes an existing Individual Application Session Context

### Example
```java
// Import classes:
import autogen.pcf.api.ApiClient;
import autogen.pcf.api.ApiException;
import autogen.pcf.api.Configuration;
import autogen.pcf.api.auth.*;
import autogen.pcf.api.models.*;
import autogen.pcf.api.IndividualApplicationSessionContextDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/npcf-policyauthorization/v1");
    
    // Configure OAuth2 access token for authorization: oAuth2ClientCredentials
    OAuth oAuth2ClientCredentials = (OAuth) defaultClient.getAuthentication("oAuth2ClientCredentials");
    oAuth2ClientCredentials.setAccessToken("YOUR ACCESS TOKEN");

    IndividualApplicationSessionContextDocumentApi apiInstance = new IndividualApplicationSessionContextDocumentApi(defaultClient);
    String appSessionId = "appSessionId_example"; // String | string identifying the Individual Application Session Context resource
    EventsSubscReqData eventsSubscReqData = new EventsSubscReqData(); // EventsSubscReqData | deletion of the Individual Application Session Context resource, req notification
    try {
      AppSessionContext result = apiInstance.deleteAppSession(appSessionId, eventsSubscReqData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualApplicationSessionContextDocumentApi#deleteAppSession");
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
| **appSessionId** | **String**| string identifying the Individual Application Session Context resource | |
| **eventsSubscReqData** | [**EventsSubscReqData**](EventsSubscReqData.md)| deletion of the Individual Application Session Context resource, req notification | [optional] |

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
| **200** | The deletion of the resource is confirmed and a resource is returned |  -  |
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

<a id="getAppSession"></a>
# **getAppSession**
> AppSessionContext getAppSession(appSessionId)

Reads an existing Individual Application Session Context

### Example
```java
// Import classes:
import autogen.pcf.api.ApiClient;
import autogen.pcf.api.ApiException;
import autogen.pcf.api.Configuration;
import autogen.pcf.api.auth.*;
import autogen.pcf.api.models.*;
import autogen.pcf.api.IndividualApplicationSessionContextDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/npcf-policyauthorization/v1");
    
    // Configure OAuth2 access token for authorization: oAuth2ClientCredentials
    OAuth oAuth2ClientCredentials = (OAuth) defaultClient.getAuthentication("oAuth2ClientCredentials");
    oAuth2ClientCredentials.setAccessToken("YOUR ACCESS TOKEN");

    IndividualApplicationSessionContextDocumentApi apiInstance = new IndividualApplicationSessionContextDocumentApi(defaultClient);
    String appSessionId = "appSessionId_example"; // String | string identifying the resource
    try {
      AppSessionContext result = apiInstance.getAppSession(appSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualApplicationSessionContextDocumentApi#getAppSession");
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
| **appSessionId** | **String**| string identifying the resource | |

### Return type

[**AppSessionContext**](AppSessionContext.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A representation of the resource is returned. |  -  |
| **307** | Temporary Redirect |  * Location - The URI pointing to the resource located on the redirect target <br>  * 3gpp-Sbi-Target-Nf-Id - Identifier of target NF (service) instance towards which the request is redirected <br>  |
| **308** | Permanent Redirect |  * Location - The URI pointing to the resource located on the redirect target <br>  * 3gpp-Sbi-Target-Nf-Id - Identifier of target NF (service) instance towards which the request is redirected <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | 406 Not Acceptable |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |
| **0** | Generic Error |  -  |

<a id="modAppSession"></a>
# **modAppSession**
> AppSessionContext modAppSession(appSessionId, appSessionContextUpdateDataPatch)

Modifies an existing Individual Application Session Context

### Example
```java
// Import classes:
import autogen.pcf.api.ApiClient;
import autogen.pcf.api.ApiException;
import autogen.pcf.api.Configuration;
import autogen.pcf.api.auth.*;
import autogen.pcf.api.models.*;
import autogen.pcf.api.IndividualApplicationSessionContextDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/npcf-policyauthorization/v1");
    
    // Configure OAuth2 access token for authorization: oAuth2ClientCredentials
    OAuth oAuth2ClientCredentials = (OAuth) defaultClient.getAuthentication("oAuth2ClientCredentials");
    oAuth2ClientCredentials.setAccessToken("YOUR ACCESS TOKEN");

    IndividualApplicationSessionContextDocumentApi apiInstance = new IndividualApplicationSessionContextDocumentApi(defaultClient);
    String appSessionId = "appSessionId_example"; // String | string identifying the resource
    AppSessionContextUpdateDataPatch appSessionContextUpdateDataPatch = new AppSessionContextUpdateDataPatch(); // AppSessionContextUpdateDataPatch | modification of the resource.
    try {
      AppSessionContext result = apiInstance.modAppSession(appSessionId, appSessionContextUpdateDataPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndividualApplicationSessionContextDocumentApi#modAppSession");
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
| **appSessionId** | **String**| string identifying the resource | |
| **appSessionContextUpdateDataPatch** | [**AppSessionContextUpdateDataPatch**](AppSessionContextUpdateDataPatch.md)| modification of the resource. | |

### Return type

[**AppSessionContext**](AppSessionContext.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful modification of the resource and a representation of that resource is returned |  -  |
| **204** | The successful modification |  -  |
| **307** | Temporary Redirect |  * Location - The URI pointing to the resource located on the redirect target <br>  * 3gpp-Sbi-Target-Nf-Id - Identifier of target NF (service) instance towards which the request is redirected <br>  |
| **308** | Permanent Redirect |  * Location - The URI pointing to the resource located on the redirect target <br>  * 3gpp-Sbi-Target-Nf-Id - Identifier of target NF (service) instance towards which the request is redirected <br>  |
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

