package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import autogen.scef.api.model.EthFlowDescription;
import autogen.scef.api.model.FlowInfo;
import autogen.scef.api.model.QosMonitoringInformation;
import autogen.scef.api.model.Snssai;
import autogen.scef.api.model.SponsorInformation;
import autogen.scef.api.model.TscQosRequirement;
import autogen.scef.api.model.UsageThreshold;
import autogen.scef.api.model.WebsockNotifConfig;
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
 * Represents an individual AS session with required QoS subscription resource.
 */

@Schema(name = "AsSessionWithQoSSubscription", description = "Represents an individual AS session with required QoS subscription resource.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class AsSessionWithQoSSubscription {

  private String self;

  private String supportedFeatures;

  private String dnn;

  private Snssai snssai;

  private String notificationDestination;

  private String exterAppId;

  @Valid
  private List<@Valid FlowInfo> flowInfo;

  @Valid
  private List<@Valid EthFlowDescription> ethFlowInfo;

  private String qosReference;

  @Valid
  private List<String> altQoSReferences;

  private Boolean disUeNotif;

  private String ueIpv4Addr;

  private String ipDomain;

  private String ueIpv6Addr;

  private String macAddr;

  private UsageThreshold usageThreshold;

  private SponsorInformation sponsorInfo;

  private QosMonitoringInformation qosMonInfo;

  private Boolean localNotifInd;

  private TscQosRequirement tscQosReq;

  private Boolean requestTestNotification;

  private WebsockNotifConfig websockNotifConfig;

  public AsSessionWithQoSSubscription() {
    super();
  }

  /**
   * Constructor with only required parameters
   */
  public AsSessionWithQoSSubscription(String notificationDestination) {
    this.notificationDestination = notificationDestination;
  }

  public AsSessionWithQoSSubscription self(String self) {
    this.self = self;
    return this;
  }

  /**
   * string formatted according to IETF RFC 3986 identifying a referenced resource.
   * @return self
  */
  
  @Schema(name = "self", description = "string formatted according to IETF RFC 3986 identifying a referenced resource.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("self")
  public String getSelf() {
    return self;
  }

  public void setSelf(String self) {
    this.self = self;
  }

  public AsSessionWithQoSSubscription supportedFeatures(String supportedFeatures) {
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

  public AsSessionWithQoSSubscription dnn(String dnn) {
    this.dnn = dnn;
    return this;
  }

  /**
   * String representing a Data Network as defined in clause 9A of 3GPP TS 23.003; it shall contain either a DNN Network Identifier, or a full DNN with both the Network Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots (e.g. \"Label1.Label2.Label3\").
   * @return dnn
  */
  
  @Schema(name = "dnn", description = "String representing a Data Network as defined in clause 9A of 3GPP TS 23.003; it shall contain either a DNN Network Identifier, or a full DNN with both the Network Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots (e.g. \"Label1.Label2.Label3\").", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("dnn")
  public String getDnn() {
    return dnn;
  }

  public void setDnn(String dnn) {
    this.dnn = dnn;
  }

  public AsSessionWithQoSSubscription snssai(Snssai snssai) {
    this.snssai = snssai;
    return this;
  }

  /**
   * Get snssai
   * @return snssai
  */
  @Valid 
  @Schema(name = "snssai", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("snssai")
  public Snssai getSnssai() {
    return snssai;
  }

  public void setSnssai(Snssai snssai) {
    this.snssai = snssai;
  }

  public AsSessionWithQoSSubscription notificationDestination(String notificationDestination) {
    this.notificationDestination = notificationDestination;
    return this;
  }

  /**
   * string formatted according to IETF RFC 3986 identifying a referenced resource.
   * @return notificationDestination
  */
  @NotNull 
  @Schema(name = "notificationDestination", description = "string formatted according to IETF RFC 3986 identifying a referenced resource.", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("notificationDestination")
  public String getNotificationDestination() {
    return notificationDestination;
  }

  public void setNotificationDestination(String notificationDestination) {
    this.notificationDestination = notificationDestination;
  }

  public AsSessionWithQoSSubscription exterAppId(String exterAppId) {
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

  public AsSessionWithQoSSubscription flowInfo(List<@Valid FlowInfo> flowInfo) {
    this.flowInfo = flowInfo;
    return this;
  }

  public AsSessionWithQoSSubscription addFlowInfoItem(FlowInfo flowInfoItem) {
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

  public AsSessionWithQoSSubscription ethFlowInfo(List<@Valid EthFlowDescription> ethFlowInfo) {
    this.ethFlowInfo = ethFlowInfo;
    return this;
  }

  public AsSessionWithQoSSubscription addEthFlowInfoItem(EthFlowDescription ethFlowInfoItem) {
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

  public AsSessionWithQoSSubscription qosReference(String qosReference) {
    this.qosReference = qosReference;
    return this;
  }

  /**
   * Identifies a pre-defined QoS information
   * @return qosReference
  */
  
  @Schema(name = "qosReference", description = "Identifies a pre-defined QoS information", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("qosReference")
  public String getQosReference() {
    return qosReference;
  }

  public void setQosReference(String qosReference) {
    this.qosReference = qosReference;
  }

  public AsSessionWithQoSSubscription altQoSReferences(List<String> altQoSReferences) {
    this.altQoSReferences = altQoSReferences;
    return this;
  }

  public AsSessionWithQoSSubscription addAltQoSReferencesItem(String altQoSReferencesItem) {
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

  public AsSessionWithQoSSubscription disUeNotif(Boolean disUeNotif) {
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

  public AsSessionWithQoSSubscription ueIpv4Addr(String ueIpv4Addr) {
    this.ueIpv4Addr = ueIpv4Addr;
    return this;
  }

  /**
   * string identifying a Ipv4 address formatted in the \"dotted decimal\" notation as defined in IETF RFC 1166.
   * @return ueIpv4Addr
  */
  
  @Schema(name = "ueIpv4Addr", description = "string identifying a Ipv4 address formatted in the \"dotted decimal\" notation as defined in IETF RFC 1166.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("ueIpv4Addr")
  public String getUeIpv4Addr() {
    return ueIpv4Addr;
  }

  public void setUeIpv4Addr(String ueIpv4Addr) {
    this.ueIpv4Addr = ueIpv4Addr;
  }

  public AsSessionWithQoSSubscription ipDomain(String ipDomain) {
    this.ipDomain = ipDomain;
    return this;
  }

  /**
   * Get ipDomain
   * @return ipDomain
  */
  
  @Schema(name = "ipDomain", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("ipDomain")
  public String getIpDomain() {
    return ipDomain;
  }

  public void setIpDomain(String ipDomain) {
    this.ipDomain = ipDomain;
  }

  public AsSessionWithQoSSubscription ueIpv6Addr(String ueIpv6Addr) {
    this.ueIpv6Addr = ueIpv6Addr;
    return this;
  }

  /**
   * string identifying a Ipv6 address formatted according to clause 4 in IETF RFC 5952. The mixed Ipv4 Ipv6 notation according to clause 5 of IETF RFC 5952 shall not be used.
   * @return ueIpv6Addr
  */
  
  @Schema(name = "ueIpv6Addr", description = "string identifying a Ipv6 address formatted according to clause 4 in IETF RFC 5952. The mixed Ipv4 Ipv6 notation according to clause 5 of IETF RFC 5952 shall not be used.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("ueIpv6Addr")
  public String getUeIpv6Addr() {
    return ueIpv6Addr;
  }

  public void setUeIpv6Addr(String ueIpv6Addr) {
    this.ueIpv6Addr = ueIpv6Addr;
  }

  public AsSessionWithQoSSubscription macAddr(String macAddr) {
    this.macAddr = macAddr;
    return this;
  }

  /**
   * String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042
   * @return macAddr
  */
  @Pattern(regexp = "^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$") 
  @Schema(name = "macAddr", description = "String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("macAddr")
  public String getMacAddr() {
    return macAddr;
  }

  public void setMacAddr(String macAddr) {
    this.macAddr = macAddr;
  }

  public AsSessionWithQoSSubscription usageThreshold(UsageThreshold usageThreshold) {
    this.usageThreshold = usageThreshold;
    return this;
  }

  /**
   * Get usageThreshold
   * @return usageThreshold
  */
  @Valid 
  @Schema(name = "usageThreshold", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("usageThreshold")
  public UsageThreshold getUsageThreshold() {
    return usageThreshold;
  }

  public void setUsageThreshold(UsageThreshold usageThreshold) {
    this.usageThreshold = usageThreshold;
  }

  public AsSessionWithQoSSubscription sponsorInfo(SponsorInformation sponsorInfo) {
    this.sponsorInfo = sponsorInfo;
    return this;
  }

  /**
   * Get sponsorInfo
   * @return sponsorInfo
  */
  @Valid 
  @Schema(name = "sponsorInfo", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("sponsorInfo")
  public SponsorInformation getSponsorInfo() {
    return sponsorInfo;
  }

  public void setSponsorInfo(SponsorInformation sponsorInfo) {
    this.sponsorInfo = sponsorInfo;
  }

  public AsSessionWithQoSSubscription qosMonInfo(QosMonitoringInformation qosMonInfo) {
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
  public QosMonitoringInformation getQosMonInfo() {
    return qosMonInfo;
  }

  public void setQosMonInfo(QosMonitoringInformation qosMonInfo) {
    this.qosMonInfo = qosMonInfo;
  }

  public AsSessionWithQoSSubscription localNotifInd(Boolean localNotifInd) {
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

  public AsSessionWithQoSSubscription tscQosReq(TscQosRequirement tscQosReq) {
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
  public TscQosRequirement getTscQosReq() {
    return tscQosReq;
  }

  public void setTscQosReq(TscQosRequirement tscQosReq) {
    this.tscQosReq = tscQosReq;
  }

  public AsSessionWithQoSSubscription requestTestNotification(Boolean requestTestNotification) {
    this.requestTestNotification = requestTestNotification;
    return this;
  }

  /**
   * Set to true by the SCS/AS to request the SCEF to send a test notification as defined in subclause 5.2.5.3. Set to false or omitted otherwise.
   * @return requestTestNotification
  */
  
  @Schema(name = "requestTestNotification", description = "Set to true by the SCS/AS to request the SCEF to send a test notification as defined in subclause 5.2.5.3. Set to false or omitted otherwise.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("requestTestNotification")
  public Boolean getRequestTestNotification() {
    return requestTestNotification;
  }

  public void setRequestTestNotification(Boolean requestTestNotification) {
    this.requestTestNotification = requestTestNotification;
  }

  public AsSessionWithQoSSubscription websockNotifConfig(WebsockNotifConfig websockNotifConfig) {
    this.websockNotifConfig = websockNotifConfig;
    return this;
  }

  /**
   * Get websockNotifConfig
   * @return websockNotifConfig
  */
  @Valid 
  @Schema(name = "websockNotifConfig", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("websockNotifConfig")
  public WebsockNotifConfig getWebsockNotifConfig() {
    return websockNotifConfig;
  }

  public void setWebsockNotifConfig(WebsockNotifConfig websockNotifConfig) {
    this.websockNotifConfig = websockNotifConfig;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AsSessionWithQoSSubscription asSessionWithQoSSubscription = (AsSessionWithQoSSubscription) o;
    return Objects.equals(this.self, asSessionWithQoSSubscription.self) &&
        Objects.equals(this.supportedFeatures, asSessionWithQoSSubscription.supportedFeatures) &&
        Objects.equals(this.dnn, asSessionWithQoSSubscription.dnn) &&
        Objects.equals(this.snssai, asSessionWithQoSSubscription.snssai) &&
        Objects.equals(this.notificationDestination, asSessionWithQoSSubscription.notificationDestination) &&
        Objects.equals(this.exterAppId, asSessionWithQoSSubscription.exterAppId) &&
        Objects.equals(this.flowInfo, asSessionWithQoSSubscription.flowInfo) &&
        Objects.equals(this.ethFlowInfo, asSessionWithQoSSubscription.ethFlowInfo) &&
        Objects.equals(this.qosReference, asSessionWithQoSSubscription.qosReference) &&
        Objects.equals(this.altQoSReferences, asSessionWithQoSSubscription.altQoSReferences) &&
        Objects.equals(this.disUeNotif, asSessionWithQoSSubscription.disUeNotif) &&
        Objects.equals(this.ueIpv4Addr, asSessionWithQoSSubscription.ueIpv4Addr) &&
        Objects.equals(this.ipDomain, asSessionWithQoSSubscription.ipDomain) &&
        Objects.equals(this.ueIpv6Addr, asSessionWithQoSSubscription.ueIpv6Addr) &&
        Objects.equals(this.macAddr, asSessionWithQoSSubscription.macAddr) &&
        Objects.equals(this.usageThreshold, asSessionWithQoSSubscription.usageThreshold) &&
        Objects.equals(this.sponsorInfo, asSessionWithQoSSubscription.sponsorInfo) &&
        Objects.equals(this.qosMonInfo, asSessionWithQoSSubscription.qosMonInfo) &&
        Objects.equals(this.localNotifInd, asSessionWithQoSSubscription.localNotifInd) &&
        Objects.equals(this.tscQosReq, asSessionWithQoSSubscription.tscQosReq) &&
        Objects.equals(this.requestTestNotification, asSessionWithQoSSubscription.requestTestNotification) &&
        Objects.equals(this.websockNotifConfig, asSessionWithQoSSubscription.websockNotifConfig);
  }

  @Override
  public int hashCode() {
    return Objects.hash(self, supportedFeatures, dnn, snssai, notificationDestination, exterAppId, flowInfo, ethFlowInfo, qosReference, altQoSReferences, disUeNotif, ueIpv4Addr, ipDomain, ueIpv6Addr, macAddr, usageThreshold, sponsorInfo, qosMonInfo, localNotifInd, tscQosReq, requestTestNotification, websockNotifConfig);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AsSessionWithQoSSubscription {\n");
    sb.append("    self: ").append(toIndentedString(self)).append("\n");
    sb.append("    supportedFeatures: ").append(toIndentedString(supportedFeatures)).append("\n");
    sb.append("    dnn: ").append(toIndentedString(dnn)).append("\n");
    sb.append("    snssai: ").append(toIndentedString(snssai)).append("\n");
    sb.append("    notificationDestination: ").append(toIndentedString(notificationDestination)).append("\n");
    sb.append("    exterAppId: ").append(toIndentedString(exterAppId)).append("\n");
    sb.append("    flowInfo: ").append(toIndentedString(flowInfo)).append("\n");
    sb.append("    ethFlowInfo: ").append(toIndentedString(ethFlowInfo)).append("\n");
    sb.append("    qosReference: ").append(toIndentedString(qosReference)).append("\n");
    sb.append("    altQoSReferences: ").append(toIndentedString(altQoSReferences)).append("\n");
    sb.append("    disUeNotif: ").append(toIndentedString(disUeNotif)).append("\n");
    sb.append("    ueIpv4Addr: ").append(toIndentedString(ueIpv4Addr)).append("\n");
    sb.append("    ipDomain: ").append(toIndentedString(ipDomain)).append("\n");
    sb.append("    ueIpv6Addr: ").append(toIndentedString(ueIpv6Addr)).append("\n");
    sb.append("    macAddr: ").append(toIndentedString(macAddr)).append("\n");
    sb.append("    usageThreshold: ").append(toIndentedString(usageThreshold)).append("\n");
    sb.append("    sponsorInfo: ").append(toIndentedString(sponsorInfo)).append("\n");
    sb.append("    qosMonInfo: ").append(toIndentedString(qosMonInfo)).append("\n");
    sb.append("    localNotifInd: ").append(toIndentedString(localNotifInd)).append("\n");
    sb.append("    tscQosReq: ").append(toIndentedString(tscQosReq)).append("\n");
    sb.append("    requestTestNotification: ").append(toIndentedString(requestTestNotification)).append("\n");
    sb.append("    websockNotifConfig: ").append(toIndentedString(websockNotifConfig)).append("\n");
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

