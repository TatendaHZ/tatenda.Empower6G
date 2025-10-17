package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
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
 * Represents a QoS monitoring report.
 */

@Schema(name = "QosMonitoringReport", description = "Represents a QoS monitoring report.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class QosMonitoringReport {

  @Valid
  private List<Integer> ulDelays;

  @Valid
  private List<Integer> dlDelays;

  @Valid
  private List<Integer> rtDelays;

  public QosMonitoringReport ulDelays(List<Integer> ulDelays) {
    this.ulDelays = ulDelays;
    return this;
  }

  public QosMonitoringReport addUlDelaysItem(Integer ulDelaysItem) {
    if (this.ulDelays == null) {
      this.ulDelays = new ArrayList<>();
    }
    this.ulDelays.add(ulDelaysItem);
    return this;
  }

  /**
   * Get ulDelays
   * @return ulDelays
  */
  @Size(min = 1) 
  @Schema(name = "ulDelays", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("ulDelays")
  public List<Integer> getUlDelays() {
    return ulDelays;
  }

  public void setUlDelays(List<Integer> ulDelays) {
    this.ulDelays = ulDelays;
  }

  public QosMonitoringReport dlDelays(List<Integer> dlDelays) {
    this.dlDelays = dlDelays;
    return this;
  }

  public QosMonitoringReport addDlDelaysItem(Integer dlDelaysItem) {
    if (this.dlDelays == null) {
      this.dlDelays = new ArrayList<>();
    }
    this.dlDelays.add(dlDelaysItem);
    return this;
  }

  /**
   * Get dlDelays
   * @return dlDelays
  */
  @Size(min = 1) 
  @Schema(name = "dlDelays", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("dlDelays")
  public List<Integer> getDlDelays() {
    return dlDelays;
  }

  public void setDlDelays(List<Integer> dlDelays) {
    this.dlDelays = dlDelays;
  }

  public QosMonitoringReport rtDelays(List<Integer> rtDelays) {
    this.rtDelays = rtDelays;
    return this;
  }

  public QosMonitoringReport addRtDelaysItem(Integer rtDelaysItem) {
    if (this.rtDelays == null) {
      this.rtDelays = new ArrayList<>();
    }
    this.rtDelays.add(rtDelaysItem);
    return this;
  }

  /**
   * Get rtDelays
   * @return rtDelays
  */
  @Size(min = 1) 
  @Schema(name = "rtDelays", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("rtDelays")
  public List<Integer> getRtDelays() {
    return rtDelays;
  }

  public void setRtDelays(List<Integer> rtDelays) {
    this.rtDelays = rtDelays;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    QosMonitoringReport qosMonitoringReport = (QosMonitoringReport) o;
    return Objects.equals(this.ulDelays, qosMonitoringReport.ulDelays) &&
        Objects.equals(this.dlDelays, qosMonitoringReport.dlDelays) &&
        Objects.equals(this.rtDelays, qosMonitoringReport.rtDelays);
  }

  @Override
  public int hashCode() {
    return Objects.hash(ulDelays, dlDelays, rtDelays);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class QosMonitoringReport {\n");
    sb.append("    ulDelays: ").append(toIndentedString(ulDelays)).append("\n");
    sb.append("    dlDelays: ").append(toIndentedString(dlDelays)).append("\n");
    sb.append("    rtDelays: ").append(toIndentedString(rtDelays)).append("\n");
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

