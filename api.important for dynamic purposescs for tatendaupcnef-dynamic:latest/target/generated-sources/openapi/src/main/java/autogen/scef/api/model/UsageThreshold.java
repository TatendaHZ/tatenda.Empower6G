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
 * Represents a usage threshold.
 */

@Schema(name = "UsageThreshold", description = "Represents a usage threshold.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class UsageThreshold {

  private Integer duration;

  private Long totalVolume;

  private Long downlinkVolume;

  private Long uplinkVolume;

  public UsageThreshold duration(Integer duration) {
    this.duration = duration;
    return this;
  }

  /**
   * Unsigned integer identifying a period of time in units of seconds.
   * minimum: 0
   * @return duration
  */
  @Min(0) 
  @Schema(name = "duration", description = "Unsigned integer identifying a period of time in units of seconds.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("duration")
  public Integer getDuration() {
    return duration;
  }

  public void setDuration(Integer duration) {
    this.duration = duration;
  }

  public UsageThreshold totalVolume(Long totalVolume) {
    this.totalVolume = totalVolume;
    return this;
  }

  /**
   * Unsigned integer identifying a volume in units of bytes.
   * minimum: 0
   * @return totalVolume
  */
  @Min(0L) 
  @Schema(name = "totalVolume", description = "Unsigned integer identifying a volume in units of bytes.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("totalVolume")
  public Long getTotalVolume() {
    return totalVolume;
  }

  public void setTotalVolume(Long totalVolume) {
    this.totalVolume = totalVolume;
  }

  public UsageThreshold downlinkVolume(Long downlinkVolume) {
    this.downlinkVolume = downlinkVolume;
    return this;
  }

  /**
   * Unsigned integer identifying a volume in units of bytes.
   * minimum: 0
   * @return downlinkVolume
  */
  @Min(0L) 
  @Schema(name = "downlinkVolume", description = "Unsigned integer identifying a volume in units of bytes.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("downlinkVolume")
  public Long getDownlinkVolume() {
    return downlinkVolume;
  }

  public void setDownlinkVolume(Long downlinkVolume) {
    this.downlinkVolume = downlinkVolume;
  }

  public UsageThreshold uplinkVolume(Long uplinkVolume) {
    this.uplinkVolume = uplinkVolume;
    return this;
  }

  /**
   * Unsigned integer identifying a volume in units of bytes.
   * minimum: 0
   * @return uplinkVolume
  */
  @Min(0L) 
  @Schema(name = "uplinkVolume", description = "Unsigned integer identifying a volume in units of bytes.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("uplinkVolume")
  public Long getUplinkVolume() {
    return uplinkVolume;
  }

  public void setUplinkVolume(Long uplinkVolume) {
    this.uplinkVolume = uplinkVolume;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UsageThreshold usageThreshold = (UsageThreshold) o;
    return Objects.equals(this.duration, usageThreshold.duration) &&
        Objects.equals(this.totalVolume, usageThreshold.totalVolume) &&
        Objects.equals(this.downlinkVolume, usageThreshold.downlinkVolume) &&
        Objects.equals(this.uplinkVolume, usageThreshold.uplinkVolume);
  }

  @Override
  public int hashCode() {
    return Objects.hash(duration, totalVolume, downlinkVolume, uplinkVolume);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UsageThreshold {\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    totalVolume: ").append(toIndentedString(totalVolume)).append("\n");
    sb.append("    downlinkVolume: ").append(toIndentedString(downlinkVolume)).append("\n");
    sb.append("    uplinkVolume: ").append(toIndentedString(uplinkVolume)).append("\n");
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

