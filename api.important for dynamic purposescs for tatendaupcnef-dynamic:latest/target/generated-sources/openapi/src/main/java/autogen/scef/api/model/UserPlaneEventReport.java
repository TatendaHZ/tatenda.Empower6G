package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import autogen.scef.api.model.AccumulatedUsage;
import autogen.scef.api.model.QosMonitoringReport;
import autogen.scef.api.model.UserPlaneEvent;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
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
 * Represents an event report for user plane.
 */

@Schema(name = "UserPlaneEventReport", description = "Represents an event report for user plane.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class UserPlaneEventReport {

  private UserPlaneEvent event;

  private AccumulatedUsage accumulatedUsage;

  @Valid
  private List<Integer> flowIds;

  private String appliedQosRef;

  @Valid
  private List<@Valid QosMonitoringReport> qosMonReports;

  public UserPlaneEventReport() {
    super();
  }

  /**
   * Constructor with only required parameters
   */
  public UserPlaneEventReport(UserPlaneEvent event) {
    this.event = event;
  }

  public UserPlaneEventReport event(UserPlaneEvent event) {
    this.event = event;
    return this;
  }

  /**
   * Get event
   * @return event
  */
  @NotNull @Valid 
  @Schema(name = "event", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("event")
  public UserPlaneEvent getEvent() {
    return event;
  }

  public void setEvent(UserPlaneEvent event) {
    this.event = event;
  }

  public UserPlaneEventReport accumulatedUsage(AccumulatedUsage accumulatedUsage) {
    this.accumulatedUsage = accumulatedUsage;
    return this;
  }

  /**
   * Get accumulatedUsage
   * @return accumulatedUsage
  */
  @Valid 
  @Schema(name = "accumulatedUsage", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("accumulatedUsage")
  public AccumulatedUsage getAccumulatedUsage() {
    return accumulatedUsage;
  }

  public void setAccumulatedUsage(AccumulatedUsage accumulatedUsage) {
    this.accumulatedUsage = accumulatedUsage;
  }

  public UserPlaneEventReport flowIds(List<Integer> flowIds) {
    this.flowIds = flowIds;
    return this;
  }

  public UserPlaneEventReport addFlowIdsItem(Integer flowIdsItem) {
    if (this.flowIds == null) {
      this.flowIds = new ArrayList<>();
    }
    this.flowIds.add(flowIdsItem);
    return this;
  }

  /**
   * Identifies the IP flows that were sent during event subscription
   * @return flowIds
  */
  @Size(min = 1) 
  @Schema(name = "flowIds", description = "Identifies the IP flows that were sent during event subscription", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("flowIds")
  public List<Integer> getFlowIds() {
    return flowIds;
  }

  public void setFlowIds(List<Integer> flowIds) {
    this.flowIds = flowIds;
  }

  public UserPlaneEventReport appliedQosRef(String appliedQosRef) {
    this.appliedQosRef = appliedQosRef;
    return this;
  }

  /**
   * The currently applied QoS reference. Applicable for event QOS_NOT_GUARANTEED or SUCCESSFUL_RESOURCES_ALLOCATION.
   * @return appliedQosRef
  */
  
  @Schema(name = "appliedQosRef", description = "The currently applied QoS reference. Applicable for event QOS_NOT_GUARANTEED or SUCCESSFUL_RESOURCES_ALLOCATION.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("appliedQosRef")
  public String getAppliedQosRef() {
    return appliedQosRef;
  }

  public void setAppliedQosRef(String appliedQosRef) {
    this.appliedQosRef = appliedQosRef;
  }

  public UserPlaneEventReport qosMonReports(List<@Valid QosMonitoringReport> qosMonReports) {
    this.qosMonReports = qosMonReports;
    return this;
  }

  public UserPlaneEventReport addQosMonReportsItem(QosMonitoringReport qosMonReportsItem) {
    if (this.qosMonReports == null) {
      this.qosMonReports = new ArrayList<>();
    }
    this.qosMonReports.add(qosMonReportsItem);
    return this;
  }

  /**
   * Contains the QoS Monitoring Reporting information
   * @return qosMonReports
  */
  @Valid @Size(min = 1) 
  @Schema(name = "qosMonReports", description = "Contains the QoS Monitoring Reporting information", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("qosMonReports")
  public List<@Valid QosMonitoringReport> getQosMonReports() {
    return qosMonReports;
  }

  public void setQosMonReports(List<@Valid QosMonitoringReport> qosMonReports) {
    this.qosMonReports = qosMonReports;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserPlaneEventReport userPlaneEventReport = (UserPlaneEventReport) o;
    return Objects.equals(this.event, userPlaneEventReport.event) &&
        Objects.equals(this.accumulatedUsage, userPlaneEventReport.accumulatedUsage) &&
        Objects.equals(this.flowIds, userPlaneEventReport.flowIds) &&
        Objects.equals(this.appliedQosRef, userPlaneEventReport.appliedQosRef) &&
        Objects.equals(this.qosMonReports, userPlaneEventReport.qosMonReports);
  }

  @Override
  public int hashCode() {
    return Objects.hash(event, accumulatedUsage, flowIds, appliedQosRef, qosMonReports);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserPlaneEventReport {\n");
    sb.append("    event: ").append(toIndentedString(event)).append("\n");
    sb.append("    accumulatedUsage: ").append(toIndentedString(accumulatedUsage)).append("\n");
    sb.append("    flowIds: ").append(toIndentedString(flowIds)).append("\n");
    sb.append("    appliedQosRef: ").append(toIndentedString(appliedQosRef)).append("\n");
    sb.append("    qosMonReports: ").append(toIndentedString(qosMonReports)).append("\n");
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

