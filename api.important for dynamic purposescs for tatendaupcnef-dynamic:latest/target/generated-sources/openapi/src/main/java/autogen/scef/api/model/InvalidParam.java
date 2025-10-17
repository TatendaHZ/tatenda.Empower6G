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
 * Represents the description of invalid parameters, for a request rejected due to invalid parameters.
 */

@Schema(name = "InvalidParam", description = "Represents the description of invalid parameters, for a request rejected due to invalid parameters.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class InvalidParam {

  private String param;

  private String reason;

  public InvalidParam() {
    super();
  }

  /**
   * Constructor with only required parameters
   */
  public InvalidParam(String param) {
    this.param = param;
  }

  public InvalidParam param(String param) {
    this.param = param;
    return this;
  }

  /**
   * Attribute's name encoded as a JSON Pointer, or header's name.
   * @return param
  */
  @NotNull 
  @Schema(name = "param", description = "Attribute's name encoded as a JSON Pointer, or header's name.", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("param")
  public String getParam() {
    return param;
  }

  public void setParam(String param) {
    this.param = param;
  }

  public InvalidParam reason(String reason) {
    this.reason = reason;
    return this;
  }

  /**
   * A human-readable reason, e.g. \"must be a positive integer\".
   * @return reason
  */
  
  @Schema(name = "reason", description = "A human-readable reason, e.g. \"must be a positive integer\".", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("reason")
  public String getReason() {
    return reason;
  }

  public void setReason(String reason) {
    this.reason = reason;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InvalidParam invalidParam = (InvalidParam) o;
    return Objects.equals(this.param, invalidParam.param) &&
        Objects.equals(this.reason, invalidParam.reason);
  }

  @Override
  public int hashCode() {
    return Objects.hash(param, reason);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InvalidParam {\n");
    sb.append("    param: ").append(toIndentedString(param)).append("\n");
    sb.append("    reason: ").append(toIndentedString(reason)).append("\n");
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

