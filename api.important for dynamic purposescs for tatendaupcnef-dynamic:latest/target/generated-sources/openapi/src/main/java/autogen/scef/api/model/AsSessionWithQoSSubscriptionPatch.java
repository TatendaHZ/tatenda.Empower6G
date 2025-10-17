package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import autogen.scef.api.model.EthFlowDescription;
import autogen.scef.api.model.FlowInfo;
import autogen.scef.api.model.QosMonitoringInformationRm;
import autogen.scef.api.model.TscQosRequirementRm;
import autogen.scef.api.model.UsageThresholdRm;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
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
 * Represents parameters to modify an AS session with specific QoS subscription.
 */

@Schema(name = "AsSessionWithQoSSubscriptionPatch", description = "Represents parameters to modify an AS session with specific QoS subscription.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class AsSessionWithQoSSubscriptionPatch {

  private String exterAppId;

  @Valid
  private List<@Valid FlowInfo> flowInfo;

  @Valid
  private List<@Valid EthFlowDescription> ethFlowInfo;

  private String qosReference;

  @Valid
  private List<String> altQoSReferences;

  private Boolean disUeNotif;

  private JsonNullable<UsageThresholdRm> usageThreshold = JsonNullable.undefined();

  private QosMonitoringInformationRm qosMonInfo;

  private Boolean localNotifInd;

  private String notificationDestination;

  private TscQosRequirementRm tscQosReq;

  public AsSessionWithQoSSubscriptionPatch exterAppId(String exterAppId) {
    this.exterAppId = exterAppId;
    return this;
  }

  /**
   * Identifies the external Application Identifier.
   * @return exterAppId
  */
  
  @Schema(name = "exterAppId", description = "Identifies the external Application Identifier.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("exterAppId")
  public String getExterAppId() {
    return exterAppId;
  }

  public void setExterAppId(String exterAppId) {
    this.exterAppId = exterAppId;
  }

  public AsSessionWithQoSSubscriptionPatch flowInfo(List<@Valid FlowInfo> flowInfo) {
    this.flowInfo = flowInfo;
    return this;
  }

  public AsSessionWithQoSSubscriptionPatch addFlowInfoItem(FlowInfo flowInfoItem) {
    if (this.flowInfo == null) {
      this.flowInfo = new ArrayList<>();
    }
    this.flowInfo.add(flowInfoItem);
    return this;
  }

  /**
   * Describe the data flow which requires QoS.
   * @return flowInfo
  */
  @Valid @Size(min = 1) 
  @Schema(name = "flowInfo", description = "Describe the data flow which requires QoS.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("flowInfo")
  public List<@Valid FlowInfo> getFlowInfo() {
    return flowInfo;
  }

  public void setFlowInfo(List<@Valid FlowInfo> flowInfo) {
    this.flowInfo = flowInfo;
  }

  public AsSessionWithQoSSubscriptionPatch ethFlowInfo(List<@Valid EthFlowDescription> ethFlowInfo) {
    this.ethFlowInfo = ethFlowInfo;
    return this;
  }

  public AsSessionWithQoSSubscriptionPatch addEthFlowInfoItem(EthFlowDescription ethFlowInfoItem) {
    if (this.ethFlowInfo == null) {
      this.ethFlowInfo = new ArrayList<>();
    }
    this.ethFlowInfo.add(ethFlowInfoItem);
    return this;
  }

  /**
   * Identifies Ethernet packet flows.
   * @return ethFlowInfo
  */
  @Valid @Size(min = 1) 
  @Schema(name = "ethFlowInfo", description = "Identifies Ethernet packet flows.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("ethFlowInfo")
  public List<@Valid EthFlowDescription> getEthFlowInfo() {
    return ethFlowInfo;
  }

  public void setEthFlowInfo(List<@Valid EthFlowDescription> ethFlowInfo) {
    this.ethFlowInfo = ethFlowInfo;
  }

  public AsSessionWithQoSSubscriptionPatch qosReference(String qosReference) {
    this.qosReference = qosReference;
    return this;
  }

  /**
   * Pre-defined QoS reference
   * @return qosReference
  */
  
  @Schema(name = "qosReference", description = "Pre-defined QoS reference", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("qosReference")
  public String getQosReference() {
    return qosReference;
  }

  public void setQosReference(String qosReference) {
    this.qosReference = qosReference;
  }

  public AsSessionWithQoSSubscriptionPatch altQoSReferences(List<String> altQoSReferences) {
    this.altQoSReferences = altQoSReferences;
    return this;
  }

  public AsSessionWithQoSSubscriptionPatch addAltQoSReferencesItem(String altQoSReferencesItem) {
    if (this.altQoSReferences == null) {
      this.altQoSReferences = new ArrayList<>();
    }
    this.altQoSReferences.add(altQoSReferencesItem);
    return this;
  }

  /**
   * Identifies an ordered list of pre-defined QoS information. The lower the index of the array for a given entry, the higher the priority.
   * @return altQoSReferences
  */
  @Size(min = 1) 
  @Schema(name = "altQoSReferences", description = "Identifies an ordered list of pre-defined QoS information. The lower the index of the array for a given entry, the higher the priority.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("altQoSReferences")
  public List<String> getAltQoSReferences() {
    return altQoSReferences;
  }

  public void setAltQoSReferences(List<String> altQoSReferences) {
    this.altQoSReferences = altQoSReferences;
  }

  public AsSessionWithQoSSubscriptionPatch disUeNotif(Boolean disUeNotif) {
    this.disUeNotif = disUeNotif;
    return this;
  }

  /**
   * Get disUeNotif
   * @return disUeNotif
  */
  
  @Schema(name = "disUeNotif", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("disUeNotif")
  public Boolean getDisUeNotif() {
    return disUeNotif;
  }

  public void setDisUeNotif(Boolean disUeNotif) {
    this.disUeNotif = disUeNotif;
  }

  public AsSessionWithQoSSubscriptionPatch usageThreshold(UsageThresholdRm usageThreshold) {
    this.usageThreshold = JsonNullable.of(usageThreshold);
    return this;
  }

  /**
   * Get usageThreshold
   * @return usageThreshold
  */
  @Valid 
  @Schema(name = "usageThreshold", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("usageThreshold")
  public JsonNullable<UsageThresholdRm> getUsageThreshold() {
    return usageThreshold;
  }

  public void setUsageThreshold(JsonNullable<UsageThresholdRm> usageThreshold) {
    this.usageThreshold = usageThreshold;
  }

  public AsSessionWithQoSSubscriptionPatch qosMonInfo(QosMonitoringInformationRm qosMonInfo) {
    this.qosMonInfo = qosMonInfo;
    return this;
  }

  /**
   * Get qosMonInfo
   * @return qosMonInfo
  */
  @Valid 
  @Schema(name = "qosMonInfo", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("qosMonInfo")
  public QosMonitoringInformationRm getQosMonInfo() {
    return qosMonInfo;
  }

  public void setQosMonInfo(QosMonitoringInformationRm qosMonInfo) {
    this.qosMonInfo = qosMonInfo;
  }

  public AsSessionWithQoSSubscriptionPatch localNotifInd(Boolean localNotifInd) {
    this.localNotifInd = localNotifInd;
    return this;
  }

  /**
   * Get localNotifInd
   * @return localNotifInd
  */
  
  @Schema(name = "localNotifInd", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("localNotifInd")
  public Boolean getLocalNotifInd() {
    return localNotifInd;
  }

  public void setLocalNotifInd(Boolean localNotifInd) {
    this.localNotifInd = localNotifInd;
  }

  public AsSessionWithQoSSubscriptionPatch notificationDestination(String notificationDestination) {
    this.notificationDestination = notificationDestination;
    return this;
  }

  /**
   * string formatted according to IETF RFC 3986 identifying a referenced resource.
   * @return notificationDestination
  */
  
  @Schema(name = "notificationDestination", description = "string formatted according to IETF RFC 3986 identifying a referenced resource.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("notificationDestination")
  public String getNotificationDestination() {
    return notificationDestination;
  }

  public void setNotificationDestination(String notificationDestination) {
    this.notificationDestination = notificationDestination;
  }

  public AsSessionWithQoSSubscriptionPatch tscQosReq(TscQosRequirementRm tscQosReq) {
    this.tscQosReq = tscQosReq;
    return this;
  }

  /**
   * Get tscQosReq
   * @return tscQosReq
  */
  @Valid 
  @Schema(name = "tscQosReq", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("tscQosReq")
  public TscQosRequirementRm getTscQosReq() {
    return tscQosReq;
  }

  public void setTscQosReq(TscQosRequirementRm tscQosReq) {
    this.tscQosReq = tscQosReq;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AsSessionWithQoSSubscriptionPatch asSessionWithQoSSubscriptionPatch = (AsSessionWithQoSSubscriptionPatch) o;
    return Objects.equals(this.exterAppId, asSessionWithQoSSubscriptionPatch.exterAppId) &&
        Objects.equals(this.flowInfo, asSessionWithQoSSubscriptionPatch.flowInfo) &&
        Objects.equals(this.ethFlowInfo, asSessionWithQoSSubscriptionPatch.ethFlowInfo) &&
        Objects.equals(this.qosReference, asSessionWithQoSSubscriptionPatch.qosReference) &&
        Objects.equals(this.altQoSReferences, asSessionWithQoSSubscriptionPatch.altQoSReferences) &&
        Objects.equals(this.disUeNotif, asSessionWithQoSSubscriptionPatch.disUeNotif) &&
        equalsNullable(this.usageThreshold, asSessionWithQoSSubscriptionPatch.usageThreshold) &&
        Objects.equals(this.qosMonInfo, asSessionWithQoSSubscriptionPatch.qosMonInfo) &&
        Objects.equals(this.localNotifInd, asSessionWithQoSSubscriptionPatch.localNotifInd) &&
        Objects.equals(this.notificationDestination, asSessionWithQoSSubscriptionPatch.notificationDestination) &&
        Objects.equals(this.tscQosReq, asSessionWithQoSSubscriptionPatch.tscQosReq);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(exterAppId, flowInfo, ethFlowInfo, qosReference, altQoSReferences, disUeNotif, hashCodeNullable(usageThreshold), qosMonInfo, localNotifInd, notificationDestination, tscQosReq);
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
    sb.append("class AsSessionWithQoSSubscriptionPatch {\n");
    sb.append("    exterAppId: ").append(toIndentedString(exterAppId)).append("\n");
    sb.append("    flowInfo: ").append(toIndentedString(flowInfo)).append("\n");
    sb.append("    ethFlowInfo: ").append(toIndentedString(ethFlowInfo)).append("\n");
    sb.append("    qosReference: ").append(toIndentedString(qosReference)).append("\n");
    sb.append("    altQoSReferences: ").append(toIndentedString(altQoSReferences)).append("\n");
    sb.append("    disUeNotif: ").append(toIndentedString(disUeNotif)).append("\n");
    sb.append("    usageThreshold: ").append(toIndentedString(usageThreshold)).append("\n");
    sb.append("    qosMonInfo: ").append(toIndentedString(qosMonInfo)).append("\n");
    sb.append("    localNotifInd: ").append(toIndentedString(localNotifInd)).append("\n");
    sb.append("    notificationDestination: ").append(toIndentedString(notificationDestination)).append("\n");
    sb.append("    tscQosReq: ").append(toIndentedString(tscQosReq)).append("\n");
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

