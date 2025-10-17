package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import org.openapitools.jackson.nullable.JsonNullable;
import java.time.OffsetDateTime;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import jakarta.annotation.Generated;

/**
 * Represents the configuration information for the delivery of notifications over Websockets.
 */

@Schema(name = "WebsockNotifConfig", description = "Represents the configuration information for the delivery of notifications over Websockets.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class WebsockNotifConfig {

  private String websocketUri;

  private Boolean requestWebsocketUri;

  public WebsockNotifConfig websocketUri(String websocketUri) {
    this.websocketUri = websocketUri;
    return this;
  }

  /**
   * string formatted according to IETF RFC 3986 identifying a referenced resource.
   * @return websocketUri
  */
  
  @Schema(name = "websocketUri", description = "string formatted according to IETF RFC 3986 identifying a referenced resource.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("websocketUri")
  public String getWebsocketUri() {
    return websocketUri;
  }

  public void setWebsocketUri(String websocketUri) {
    this.websocketUri = websocketUri;
  }

  public WebsockNotifConfig requestWebsocketUri(Boolean requestWebsocketUri) {
    this.requestWebsocketUri = requestWebsocketUri;
    return this;
  }

  /**
   * Set by the SCS/AS to indicate that the Websocket delivery is requested.
   * @return requestWebsocketUri
  */
  
  @Schema(name = "requestWebsocketUri", description = "Set by the SCS/AS to indicate that the Websocket delivery is requested.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("requestWebsocketUri")
  public Boolean getRequestWebsocketUri() {
    return requestWebsocketUri;
  }

  public void setRequestWebsocketUri(Boolean requestWebsocketUri) {
    this.requestWebsocketUri = requestWebsocketUri;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WebsockNotifConfig websockNotifConfig = (WebsockNotifConfig) o;
    return Objects.equals(this.websocketUri, websockNotifConfig.websocketUri) &&
        Objects.equals(this.requestWebsocketUri, websockNotifConfig.requestWebsocketUri);
  }

  @Override
  public int hashCode() {
    return Objects.hash(websocketUri, requestWebsocketUri);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WebsockNotifConfig {\n");
    sb.append("    websocketUri: ").append(toIndentedString(websocketUri)).append("\n");
    sb.append("    requestWebsocketUri: ").append(toIndentedString(requestWebsocketUri)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

