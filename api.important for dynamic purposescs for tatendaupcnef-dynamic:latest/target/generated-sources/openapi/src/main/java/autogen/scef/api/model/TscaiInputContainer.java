package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import java.time.OffsetDateTime;
import org.springframework.format.annotation.DateTimeFormat;
import org.openapitools.jackson.nullable.JsonNullable;
import java.time.OffsetDateTime;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import jakarta.annotation.Generated;

/**
 * Indicates TSC Traffic pattern.
 */

@Schema(name = "TscaiInputContainer", description = "Indicates TSC Traffic pattern.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class TscaiInputContainer {

  private Integer periodicity;

  @DateTimeFormat(iso = DateTimeFormat.ISO.DATE_TIME)
  private OffsetDateTime burstArrivalTime;

  private Integer surTimeInNumMsg;

  private Integer surTimeInTime;

  public TscaiInputContainer periodicity(Integer periodicity) {
    this.periodicity = periodicity;
    return this;
  }

  /**
   * Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.
   * minimum: 0
   * @return periodicity
  */
  @Min(0) 
  @Schema(name = "periodicity", description = "Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("periodicity")
  public Integer getPeriodicity() {
    return periodicity;
  }

  public void setPeriodicity(Integer periodicity) {
    this.periodicity = periodicity;
  }

  public TscaiInputContainer burstArrivalTime(OffsetDateTime burstArrivalTime) {
    this.burstArrivalTime = burstArrivalTime;
    return this;
  }

  /**
   * string with format \"date-time\" as defined in OpenAPI.
   * @return burstArrivalTime
  */
  @Valid 
  @Schema(name = "burstArrivalTime", description = "string with format \"date-time\" as defined in OpenAPI.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("burstArrivalTime")
  public OffsetDateTime getBurstArrivalTime() {
    return burstArrivalTime;
  }

  public void setBurstArrivalTime(OffsetDateTime burstArrivalTime) {
    this.burstArrivalTime = burstArrivalTime;
  }

  public TscaiInputContainer surTimeInNumMsg(Integer surTimeInNumMsg) {
    this.surTimeInNumMsg = surTimeInNumMsg;
    return this;
  }

  /**
   * Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.
   * minimum: 0
   * @return surTimeInNumMsg
  */
  @Min(0) 
  @Schema(name = "surTimeInNumMsg", description = "Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("surTimeInNumMsg")
  public Integer getSurTimeInNumMsg() {
    return surTimeInNumMsg;
  }

  public void setSurTimeInNumMsg(Integer surTimeInNumMsg) {
    this.surTimeInNumMsg = surTimeInNumMsg;
  }

  public TscaiInputContainer surTimeInTime(Integer surTimeInTime) {
    this.surTimeInTime = surTimeInTime;
    return this;
  }

  /**
   * Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.
   * minimum: 0
   * @return surTimeInTime
  */
  @Min(0) 
  @Schema(name = "surTimeInTime", description = "Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("surTimeInTime")
  public Integer getSurTimeInTime() {
    return surTimeInTime;
  }

  public void setSurTimeInTime(Integer surTimeInTime) {
    this.surTimeInTime = surTimeInTime;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TscaiInputContainer tscaiInputContainer = (TscaiInputContainer) o;
    return Objects.equals(this.periodicity, tscaiInputContainer.periodicity) &&
        Objects.equals(this.burstArrivalTime, tscaiInputContainer.burstArrivalTime) &&
        Objects.equals(this.surTimeInNumMsg, tscaiInputContainer.surTimeInNumMsg) &&
        Objects.equals(this.surTimeInTime, tscaiInputContainer.surTimeInTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(periodicity, burstArrivalTime, surTimeInNumMsg, surTimeInTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TscaiInputContainer {\n");
    sb.append("    periodicity: ").append(toIndentedString(periodicity)).append("\n");
    sb.append("    burstArrivalTime: ").append(toIndentedString(burstArrivalTime)).append("\n");
    sb.append("    surTimeInNumMsg: ").append(toIndentedString(surTimeInNumMsg)).append("\n");
    sb.append("    surTimeInTime: ").append(toIndentedString(surTimeInTime)).append("\n");
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

