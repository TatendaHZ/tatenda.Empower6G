package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import java.util.Arrays;
import org.openapitools.jackson.nullable.JsonNullable;
import java.util.NoSuchElementException;
import org.openapitools.jackson.nullable.JsonNullable;
import java.time.OffsetDateTime;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import jakarta.annotation.Generated;

/**
 * Represents the same as the UsageThreshold data type but with the nullable:true property.
 */

@Schema(name = "UsageThresholdRm", description = "Represents the same as the UsageThreshold data type but with the nullable:true property.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class UsageThresholdRm {

  private JsonNullable<Integer> duration = JsonNullable.undefined();

  private JsonNullable<Long> totalVolume = JsonNullable.undefined();

  private JsonNullable<Long> downlinkVolume = JsonNullable.undefined();

  private JsonNullable<Long> uplinkVolume = JsonNullable.undefined();

  public UsageThresholdRm duration(Integer duration) {
    this.duration = JsonNullable.of(duration);
    return this;
  }

  /**
   * Unsigned integer identifying a period of time in units of seconds with \"nullable=true\" property.
   * minimum: 0
   * @return duration
  */
  @Min(0) 
  @Schema(name = "duration", description = "Unsigned integer identifying a period of time in units of seconds with \"nullable=true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("duration")
  public JsonNullable<Integer> getDuration() {
    return duration;
  }

  public void setDuration(JsonNullable<Integer> duration) {
    this.duration = duration;
  }

  public UsageThresholdRm totalVolume(Long totalVolume) {
    this.totalVolume = JsonNullable.of(totalVolume);
    return this;
  }

  /**
   * Unsigned integer identifying a volume in units of bytes with \"nullable=true\" property.
   * minimum: 0
   * @return totalVolume
  */
  @Min(0L) 
  @Schema(name = "totalVolume", description = "Unsigned integer identifying a volume in units of bytes with \"nullable=true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("totalVolume")
  public JsonNullable<Long> getTotalVolume() {
    return totalVolume;
  }

  public void setTotalVolume(JsonNullable<Long> totalVolume) {
    this.totalVolume = totalVolume;
  }

  public UsageThresholdRm downlinkVolume(Long downlinkVolume) {
    this.downlinkVolume = JsonNullable.of(downlinkVolume);
    return this;
  }

  /**
   * Unsigned integer identifying a volume in units of bytes with \"nullable=true\" property.
   * minimum: 0
   * @return downlinkVolume
  */
  @Min(0L) 
  @Schema(name = "downlinkVolume", description = "Unsigned integer identifying a volume in units of bytes with \"nullable=true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("downlinkVolume")
  public JsonNullable<Long> getDownlinkVolume() {
    return downlinkVolume;
  }

  public void setDownlinkVolume(JsonNullable<Long> downlinkVolume) {
    this.downlinkVolume = downlinkVolume;
  }

  public UsageThresholdRm uplinkVolume(Long uplinkVolume) {
    this.uplinkVolume = JsonNullable.of(uplinkVolume);
    return this;
  }

  /**
   * Unsigned integer identifying a volume in units of bytes with \"nullable=true\" property.
   * minimum: 0
   * @return uplinkVolume
  */
  @Min(0L) 
  @Schema(name = "uplinkVolume", description = "Unsigned integer identifying a volume in units of bytes with \"nullable=true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("uplinkVolume")
  public JsonNullable<Long> getUplinkVolume() {
    return uplinkVolume;
  }

  public void setUplinkVolume(JsonNullable<Long> uplinkVolume) {
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
    UsageThresholdRm usageThresholdRm = (UsageThresholdRm) o;
    return equalsNullable(this.duration, usageThresholdRm.duration) &&
        equalsNullable(this.totalVolume, usageThresholdRm.totalVolume) &&
        equalsNullable(this.downlinkVolume, usageThresholdRm.downlinkVolume) &&
        equalsNullable(this.uplinkVolume, usageThresholdRm.uplinkVolume);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(hashCodeNullable(duration), hashCodeNullable(totalVolume), hashCodeNullable(downlinkVolume), hashCodeNullable(uplinkVolume));
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UsageThresholdRm {\n");
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

