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
 * Represents flow information.
 */

@Schema(name = "FlowInfo", description = "Represents flow information.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class FlowInfo {

  private Integer flowId;

  @Valid
  private List<String> flowDescriptions;

  public FlowInfo() {
    super();
  }

  /**
   * Constructor with only required parameters
   */
  public FlowInfo(Integer flowId) {
    this.flowId = flowId;
  }

  public FlowInfo flowId(Integer flowId) {
    this.flowId = flowId;
    return this;
  }

  /**
   * Indicates the IP flow.
   * @return flowId
  */
  @NotNull 
  @Schema(name = "flowId", description = "Indicates the IP flow.", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("flowId")
  public Integer getFlowId() {
    return flowId;
  }

  public void setFlowId(Integer flowId) {
    this.flowId = flowId;
  }

  public FlowInfo flowDescriptions(List<String> flowDescriptions) {
    this.flowDescriptions = flowDescriptions;
    return this;
  }

  public FlowInfo addFlowDescriptionsItem(String flowDescriptionsItem) {
    if (this.flowDescriptions == null) {
      this.flowDescriptions = new ArrayList<>();
    }
    this.flowDescriptions.add(flowDescriptionsItem);
    return this;
  }

  /**
   * Indicates the packet filters of the IP flow. Refer to subclause 5.3.8 of 3GPP TS 29.214 for encoding. It shall contain UL and/or DL IP flow description.
   * @return flowDescriptions
  */
  @Size(min = 1, max = 2) 
  @Schema(name = "flowDescriptions", description = "Indicates the packet filters of the IP flow. Refer to subclause 5.3.8 of 3GPP TS 29.214 for encoding. It shall contain UL and/or DL IP flow description.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("flowDescriptions")
  public List<String> getFlowDescriptions() {
    return flowDescriptions;
  }

  public void setFlowDescriptions(List<String> flowDescriptions) {
    this.flowDescriptions = flowDescriptions;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FlowInfo flowInfo = (FlowInfo) o;
    return Objects.equals(this.flowId, flowInfo.flowId) &&
        Objects.equals(this.flowDescriptions, flowInfo.flowDescriptions);
  }

  @Override
  public int hashCode() {
    return Objects.hash(flowId, flowDescriptions);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FlowInfo {\n");
    sb.append("    flowId: ").append(toIndentedString(flowId)).append("\n");
    sb.append("    flowDescriptions: ").append(toIndentedString(flowDescriptions)).append("\n");
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

