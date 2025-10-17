package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import autogen.scef.api.model.InvalidParam;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.jackson.nullable.JsonNullable;
import java.time.OffsetDateTime;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import jakarta.annotation.Generated;

/**
 * Represents additional information and details on an error response.
 */

@Schema(name = "ProblemDetails", description = "Represents additional information and details on an error response.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class ProblemDetails {

  private String type;

  private String title;

  private Integer status;

  private String detail;

  private String instance;

  private String cause;

  @Valid
  private List<@Valid InvalidParam> invalidParams;

  private String supportedFeatures;

  public ProblemDetails type(String type) {
    this.type = type;
    return this;
  }

  /**
   * string providing an URI formatted according to IETF RFC 3986.
   * @return type
  */
  
  @Schema(name = "type", description = "string providing an URI formatted according to IETF RFC 3986.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("type")
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }

  public ProblemDetails title(String title) {
    this.title = title;
    return this;
  }

  /**
   * A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem.
   * @return title
  */
  
  @Schema(name = "title", description = "A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("title")
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }

  public ProblemDetails status(Integer status) {
    this.status = status;
    return this;
  }

  /**
   * The HTTP status code for this occurrence of the problem.
   * @return status
  */
  
  @Schema(name = "status", description = "The HTTP status code for this occurrence of the problem.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("status")
  public Integer getStatus() {
    return status;
  }

  public void setStatus(Integer status) {
    this.status = status;
  }

  public ProblemDetails detail(String detail) {
    this.detail = detail;
    return this;
  }

  /**
   * A human-readable explanation specific to this occurrence of the problem.
   * @return detail
  */
  
  @Schema(name = "detail", description = "A human-readable explanation specific to this occurrence of the problem.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("detail")
  public String getDetail() {
    return detail;
  }

  public void setDetail(String detail) {
    this.detail = detail;
  }

  public ProblemDetails instance(String instance) {
    this.instance = instance;
    return this;
  }

  /**
   * string providing an URI formatted according to IETF RFC 3986.
   * @return instance
  */
  
  @Schema(name = "instance", description = "string providing an URI formatted according to IETF RFC 3986.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("instance")
  public String getInstance() {
    return instance;
  }

  public void setInstance(String instance) {
    this.instance = instance;
  }

  public ProblemDetails cause(String cause) {
    this.cause = cause;
    return this;
  }

  /**
   * A machine-readable application error cause specific to this occurrence of the problem. This IE should be present and provide application-related error information, if available.
   * @return cause
  */
  
  @Schema(name = "cause", description = "A machine-readable application error cause specific to this occurrence of the problem. This IE should be present and provide application-related error information, if available.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("cause")
  public String getCause() {
    return cause;
  }

  public void setCause(String cause) {
    this.cause = cause;
  }

  public ProblemDetails invalidParams(List<@Valid InvalidParam> invalidParams) {
    this.invalidParams = invalidParams;
    return this;
  }

  public ProblemDetails addInvalidParamsItem(InvalidParam invalidParamsItem) {
    if (this.invalidParams == null) {
      this.invalidParams = new ArrayList<>();
    }
    this.invalidParams.add(invalidParamsItem);
    return this;
  }

  /**
   * Description of invalid parameters, for a request rejected due to invalid parameters.
   * @return invalidParams
  */
  @Valid @Size(min = 1) 
  @Schema(name = "invalidParams", description = "Description of invalid parameters, for a request rejected due to invalid parameters.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("invalidParams")
  public List<@Valid InvalidParam> getInvalidParams() {
    return invalidParams;
  }

  public void setInvalidParams(List<@Valid InvalidParam> invalidParams) {
    this.invalidParams = invalidParams;
  }

  public ProblemDetails supportedFeatures(String supportedFeatures) {
    this.supportedFeatures = supportedFeatures;
    return this;
  }

  /**
   * A string used to indicate the features supported by an API that is used as defined in clause 6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in table 5.2.2-3. The most significant character representing the highest-numbered features shall appear first in the string, and the character representing features 1 to 4 shall appear last in the string. The list of features and their numbering (starting with 1) are defined separately for each API. If the string contains a lower number of characters than there are defined features for an API, all features that would be represented by characters that are not present in the string are not supported
   * @return supportedFeatures
  */
  @Pattern(regexp = "^[A-Fa-f0-9]*$") 
  @Schema(name = "supportedFeatures", description = "A string used to indicate the features supported by an API that is used as defined in clause 6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in table 5.2.2-3. The most significant character representing the highest-numbered features shall appear first in the string, and the character representing features 1 to 4 shall appear last in the string. The list of features and their numbering (starting with 1) are defined separately for each API. If the string contains a lower number of characters than there are defined features for an API, all features that would be represented by characters that are not present in the string are not supported", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("supportedFeatures")
  public String getSupportedFeatures() {
    return supportedFeatures;
  }

  public void setSupportedFeatures(String supportedFeatures) {
    this.supportedFeatures = supportedFeatures;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProblemDetails problemDetails = (ProblemDetails) o;
    return Objects.equals(this.type, problemDetails.type) &&
        Objects.equals(this.title, problemDetails.title) &&
        Objects.equals(this.status, problemDetails.status) &&
        Objects.equals(this.detail, problemDetails.detail) &&
        Objects.equals(this.instance, problemDetails.instance) &&
        Objects.equals(this.cause, problemDetails.cause) &&
        Objects.equals(this.invalidParams, problemDetails.invalidParams) &&
        Objects.equals(this.supportedFeatures, problemDetails.supportedFeatures);
  }

  @Override
  public int hashCode() {
    return Objects.hash(type, title, status, detail, instance, cause, invalidParams, supportedFeatures);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProblemDetails {\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    detail: ").append(toIndentedString(detail)).append("\n");
    sb.append("    instance: ").append(toIndentedString(instance)).append("\n");
    sb.append("    cause: ").append(toIndentedString(cause)).append("\n");
    sb.append("    invalidParams: ").append(toIndentedString(invalidParams)).append("\n");
    sb.append("    supportedFeatures: ").append(toIndentedString(supportedFeatures)).append("\n");
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

