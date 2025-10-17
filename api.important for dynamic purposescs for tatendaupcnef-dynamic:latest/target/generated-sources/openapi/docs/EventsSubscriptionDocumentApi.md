# EventsSubscriptionDocumentApi

All URIs are relative to *https://example.com/npcf-policyauthorization/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteEventsSubsc**](EventsSubscriptionDocumentApi.md#deleteEventsSubsc) | **DELETE** /app-sessions/{appSessionId}/events-subscription | deletes the Events Subscription subresource |
| [**updateEventsSubsc**](EventsSubscriptionDocumentApi.md#updateEventsSubsc) | **PUT** /app-sessions/{appSessionId}/events-subscription | creates or modifies an Events Subscription subresource |


<a id="deleteEventsSubsc"></a>
# **deleteEventsSubsc**
> deleteEventsSubsc(appSessionId)

deletes the Events Subscription subresource

### Example
```java
// Import classes:
import autogen.pcf.api.ApiClient;
import autogen.pcf.api.ApiException;
import autogen.pcf.api.Configuration;
import autogen.pcf.api.auth.*;
import autogen.pcf.api.models.*;
import autogen.pcf.api.EventsSubscriptionDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/npcf-policyauthorization/v1");
    
    // Configure OAuth2 access token for authorization: oAuth2ClientCredentials
    OAuth oAuth2ClientCredentials = (OAuth) defaultClient.getAuthentication("oAuth2ClientCredentials");
    oAuth2ClientCredentials.setAccessToken("YOUR ACCESS TOKEN");

    EventsSubscriptionDocumentApi apiInstance = new EventsSubscriptionDocumentApi(defaultClient);
    String appSessionId = "appSessionId_example"; // String | string identifying the Individual Application Session Context resource
    try {
      apiInstance.deleteEventsSubsc(appSessionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsSubscriptionDocumentApi#deleteEventsSubsc");
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

### Return type

null (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The deletion of the of the Events Subscription sub-resource is confirmed without returning additional data. |  -  |
| **307** | Temporary Redirect |  * Location - The URI pointing to the resource located on the redirect target <br>  * 3gpp-Sbi-Target-Nf-Id - Identifier of target NF (service) instance towards which the request is redirected <br>  |
| **308** | Permanent Redirect |  * Location - The URI pointing to the resource located on the redirect target <br>  * 3gpp-Sbi-Target-Nf-Id - Identifier of target NF (service) instance towards which the request is redirected <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |
| **0** | Generic Error |  -  |

<a id="updateEventsSubsc"></a>
# **updateEventsSubsc**
> EventsSubscPutData updateEventsSubsc(appSessionId, eventsSubscReqData)

creates or modifies an Events Subscription subresource

### Example
```java
// Import classes:
import autogen.pcf.api.ApiClient;
import autogen.pcf.api.ApiException;
import autogen.pcf.api.Configuration;
import autogen.pcf.api.auth.*;
import autogen.pcf.api.models.*;
import autogen.pcf.api.EventsSubscriptionDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/npcf-policyauthorization/v1");
    
    // Configure OAuth2 access token for authorization: oAuth2ClientCredentials
    OAuth oAuth2ClientCredentials = (OAuth) defaultClient.getAuthentication("oAuth2ClientCredentials");
    oAuth2ClientCredentials.setAccessToken("YOUR ACCESS TOKEN");

    EventsSubscriptionDocumentApi apiInstance = new EventsSubscriptionDocumentApi(defaultClient);
    String appSessionId = "appSessionId_example"; // String | string identifying the Events Subscription resource
    EventsSubscReqData eventsSubscReqData = new EventsSubscReqData(); // EventsSubscReqData | Creation or modification of an Events Subscription resource.
    try {
      EventsSubscPutData result = apiInstance.updateEventsSubsc(appSessionId, eventsSubscReqData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsSubscriptionDocumentApi#updateEventsSubsc");
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
| **appSessionId** | **String**| string identifying the Events Subscription resource | |
| **eventsSubscReqData** | [**EventsSubscReqData**](EventsSubscReqData.md)| Creation or modification of an Events Subscription resource. | |

### Return type

[**EventsSubscPutData**](EventsSubscPutData.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The creation of the Events Subscription resource is confirmed and its representation is returned. |  * Location - The URI pointing to the resource located on the redirect target <br>  |
| **200** | The modification of the Events Subscription resource is confirmed its representation is returned. |  -  |
| **204** | The modification of the Events Subscription subresource is confirmed without returning additional data. |  -  |
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

