# AsSessionWithQoSApiSubscriptionEventsNotificationCallbackApi

All URIs are relative to *https://example.com/3gpp-as-session-with-qos/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notificationsPost**](AsSessionWithQoSApiSubscriptionEventsNotificationCallbackApi.md#notificationsPost) | **POST** /notifications | notify bearer level event(s) from the SCEF to the SCS/AS |


<a id="notificationsPost"></a>
# **notificationsPost**
> notificationsPost(userPlaneNotificationData)

notify bearer level event(s) from the SCEF to the SCS/AS

### Example
```java
// Import classes:
import autogen.scef.notification.api.ApiClient;
import autogen.scef.notification.api.ApiException;
import autogen.scef.notification.api.Configuration;
import autogen.scef.notification.api.auth.*;
import autogen.scef.notification.api.models.*;
import autogen.scef.notification.api.AsSessionWithQoSApiSubscriptionEventsNotificationCallbackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/3gpp-as-session-with-qos/v1");
    
    // Configure OAuth2 access token for authorization: oAuth2ClientCredentials
    OAuth oAuth2ClientCredentials = (OAuth) defaultClient.getAuthentication("oAuth2ClientCredentials");
    oAuth2ClientCredentials.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AsSessionWithQoSApiSubscriptionEventsNotificationCallbackApi apiInstance = new AsSessionWithQoSApiSubscriptionEventsNotificationCallbackApi(defaultClient);
    UserPlaneNotificationData userPlaneNotificationData = new UserPlaneNotificationData(); // UserPlaneNotificationData | 
    try {
      apiInstance.notificationsPost(userPlaneNotificationData);
    } catch (ApiException e) {
      System.err.println("Exception when calling AsSessionWithQoSApiSubscriptionEventsNotificationCallbackApi#notificationsPost");
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
| **userPlaneNotificationData** | [**UserPlaneNotificationData**](UserPlaneNotificationData.md)|  | |

### Return type

null (empty response body)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content (successful notification) |  -  |
| **307** | Temporary Redirect |  * Location - An alternative URI of the resource. <br>  |
| **308** | Permanent Redirect |  * Location - An alternative URI of the resource. <br>  |
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

