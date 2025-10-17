package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import autogen.scef.api.model.FlowDirection;
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
 * Identifies an Ethernet flow
 */

@Schema(name = "EthFlowDescription", description = "Identifies an Ethernet flow")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class EthFlowDescription {

  private String destMacAddr;

  private String ethType;

  private String fDesc;

  private FlowDirection fDir;

  private String sourceMacAddr;

  @Valid
  private List<String> vlanTags;

  private String srcMacAddrEnd;

  private String destMacAddrEnd;

  public EthFlowDescription() {
    super();
  }

  /**
   * Constructor with only required parameters
   */
  public EthFlowDescription(String ethType) {
    this.ethType = ethType;
  }

  public EthFlowDescription destMacAddr(String destMacAddr) {
    this.destMacAddr = destMacAddr;
    return this;
  }

  /**
   * String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042
   * @return destMacAddr
  */
  @Pattern(regexp = "^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$") 
  @Schema(name = "destMacAddr", description = "String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("destMacAddr")
  public String getDestMacAddr() {
    return destMacAddr;
  }

  public void setDestMacAddr(String destMacAddr) {
    this.destMacAddr = destMacAddr;
  }

  public EthFlowDescription ethType(String ethType) {
    this.ethType = ethType;
    return this;
  }

  /**
   * Get ethType
   * @return ethType
  */
  @NotNull 
  @Schema(name = "ethType", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("ethType")
  public String getEthType() {
    return ethType;
  }

  public void setEthType(String ethType) {
    this.ethType = ethType;
  }

  public EthFlowDescription fDesc(String fDesc) {
    this.fDesc = fDesc;
    return this;
  }

  /**
   * Defines a packet filter of an IP flow.
   * @return fDesc
  */
  
  @Schema(name = "fDesc", description = "Defines a packet filter of an IP flow.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("fDesc")
  public String getfDesc() {
    return fDesc;
  }

  public void setfDesc(String fDesc) {
    this.fDesc = fDesc;
  }

  public EthFlowDescription fDir(FlowDirection fDir) {
    this.fDir = fDir;
    return this;
  }

  /**
   * Get fDir
   * @return fDir
  */
  @Valid 
  @Schema(name = "fDir", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("fDir")
  public FlowDirection getfDir() {
    return fDir;
  }

  public void setfDir(FlowDirection fDir) {
    this.fDir = fDir;
  }

  public EthFlowDescription sourceMacAddr(String sourceMacAddr) {
    this.sourceMacAddr = sourceMacAddr;
    return this;
  }

  /**
   * String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042
   * @return sourceMacAddr
  */
  @Pattern(regexp = "^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$") 
  @Schema(name = "sourceMacAddr", description = "String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("sourceMacAddr")
  public String getSourceMacAddr() {
    return sourceMacAddr;
  }

  public void setSourceMacAddr(String sourceMacAddr) {
    this.sourceMacAddr = sourceMacAddr;
  }

  public EthFlowDescription vlanTags(List<String> vlanTags) {
    this.vlanTags = vlanTags;
    return this;
  }

  public EthFlowDescription addVlanTagsItem(String vlanTagsItem) {
    if (this.vlanTags == null) {
      this.vlanTags = new ArrayList<>();
    }
    this.vlanTags.add(vlanTagsItem);
    return this;
  }

  /**
   * Get vlanTags
   * @return vlanTags
  */
  @Size(min = 1, max = 2) 
  @Schema(name = "vlanTags", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("vlanTags")
  public List<String> getVlanTags() {
    return vlanTags;
  }

  public void setVlanTags(List<String> vlanTags) {
    this.vlanTags = vlanTags;
  }

  public EthFlowDescription srcMacAddrEnd(String srcMacAddrEnd) {
    this.srcMacAddrEnd = srcMacAddrEnd;
    return this;
  }

  /**
   * String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042
   * @return srcMacAddrEnd
  */
  @Pattern(regexp = "^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$") 
  @Schema(name = "srcMacAddrEnd", description = "String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("srcMacAddrEnd")
  public String getSrcMacAddrEnd() {
    return srcMacAddrEnd;
  }

  public void setSrcMacAddrEnd(String srcMacAddrEnd) {
    this.srcMacAddrEnd = srcMacAddrEnd;
  }

  public EthFlowDescription destMacAddrEnd(String destMacAddrEnd) {
    this.destMacAddrEnd = destMacAddrEnd;
    return this;
  }

  /**
   * String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042
   * @return destMacAddrEnd
  */
  @Pattern(regexp = "^([0-9a-fA-F]{2})((-[0-9a-fA-F]{2}){5})$") 
  @Schema(name = "destMacAddrEnd", description = "String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("destMacAddrEnd")
  public String getDestMacAddrEnd() {
    return destMacAddrEnd;
  }

  public void setDestMacAddrEnd(String destMacAddrEnd) {
    this.destMacAddrEnd = destMacAddrEnd;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EthFlowDescription ethFlowDescription = (EthFlowDescription) o;
    return Objects.equals(this.destMacAddr, ethFlowDescription.destMacAddr) &&
        Objects.equals(this.ethType, ethFlowDescription.ethType) &&
        Objects.equals(this.fDesc, ethFlowDescription.fDesc) &&
        Objects.equals(this.fDir, ethFlowDescription.fDir) &&
        Objects.equals(this.sourceMacAddr, ethFlowDescription.sourceMacAddr) &&
        Objects.equals(this.vlanTags, ethFlowDescription.vlanTags) &&
        Objects.equals(this.srcMacAddrEnd, ethFlowDescription.srcMacAddrEnd) &&
        Objects.equals(this.destMacAddrEnd, ethFlowDescription.destMacAddrEnd);
  }

  @Override
  public int hashCode() {
    return Objects.hash(destMacAddr, ethType, fDesc, fDir, sourceMacAddr, vlanTags, srcMacAddrEnd, destMacAddrEnd);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EthFlowDescription {\n");
    sb.append("    destMacAddr: ").append(toIndentedString(destMacAddr)).append("\n");
    sb.append("    ethType: ").append(toIndentedString(ethType)).append("\n");
    sb.append("    fDesc: ").append(toIndentedString(fDesc)).append("\n");
    sb.append("    fDir: ").append(toIndentedString(fDir)).append("\n");
    sb.append("    sourceMacAddr: ").append(toIndentedString(sourceMacAddr)).append("\n");
    sb.append("    vlanTags: ").append(toIndentedString(vlanTags)).append("\n");
    sb.append("    srcMacAddrEnd: ").append(toIndentedString(srcMacAddrEnd)).append("\n");
    sb.append("    destMacAddrEnd: ").append(toIndentedString(destMacAddrEnd)).append("\n");
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

