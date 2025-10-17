package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import autogen.scef.api.model.TscaiInputContainer;
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
 * Represents QoS requirements for time sensitive communication.
 */

@Schema(name = "TscQosRequirement", description = "Represents QoS requirements for time sensitive communication.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class TscQosRequirement {

  private String reqGbrDl;

  private String reqGbrUl;

  private String reqMbrDl;

  private String reqMbrUl;

  private Integer maxTscBurstSize;

  private Integer req5Gsdelay;

  private Integer tscaiTimeDom;

  private JsonNullable<TscaiInputContainer> tscaiInputDl = JsonNullable.undefined();

  private JsonNullable<TscaiInputContainer> tscaiInputUl = JsonNullable.undefined();

  public TscQosRequirement reqGbrDl(String reqGbrDl) {
    this.reqGbrDl = reqGbrDl;
    return this;
  }

  /**
   * String representing a bit rate that shall be formatted as follows.
   * @return reqGbrDl
  */
  @Pattern(regexp = "^\\d+(\\.\\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$") 
  @Schema(name = "reqGbrDl", description = "String representing a bit rate that shall be formatted as follows.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("reqGbrDl")
  public String getReqGbrDl() {
    return reqGbrDl;
  }

  public void setReqGbrDl(String reqGbrDl) {
    this.reqGbrDl = reqGbrDl;
  }

  public TscQosRequirement reqGbrUl(String reqGbrUl) {
    this.reqGbrUl = reqGbrUl;
    return this;
  }

  /**
   * String representing a bit rate that shall be formatted as follows.
   * @return reqGbrUl
  */
  @Pattern(regexp = "^\\d+(\\.\\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$") 
  @Schema(name = "reqGbrUl", description = "String representing a bit rate that shall be formatted as follows.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("reqGbrUl")
  public String getReqGbrUl() {
    return reqGbrUl;
  }

  public void setReqGbrUl(String reqGbrUl) {
    this.reqGbrUl = reqGbrUl;
  }

  public TscQosRequirement reqMbrDl(String reqMbrDl) {
    this.reqMbrDl = reqMbrDl;
    return this;
  }

  /**
   * String representing a bit rate that shall be formatted as follows.
   * @return reqMbrDl
  */
  @Pattern(regexp = "^\\d+(\\.\\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$") 
  @Schema(name = "reqMbrDl", description = "String representing a bit rate that shall be formatted as follows.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("reqMbrDl")
  public String getReqMbrDl() {
    return reqMbrDl;
  }

  public void setReqMbrDl(String reqMbrDl) {
    this.reqMbrDl = reqMbrDl;
  }

  public TscQosRequirement reqMbrUl(String reqMbrUl) {
    this.reqMbrUl = reqMbrUl;
    return this;
  }

  /**
   * String representing a bit rate that shall be formatted as follows.
   * @return reqMbrUl
  */
  @Pattern(regexp = "^\\d+(\\.\\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$") 
  @Schema(name = "reqMbrUl", description = "String representing a bit rate that shall be formatted as follows.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("reqMbrUl")
  public String getReqMbrUl() {
    return reqMbrUl;
  }

  public void setReqMbrUl(String reqMbrUl) {
    this.reqMbrUl = reqMbrUl;
  }

  public TscQosRequirement maxTscBurstSize(Integer maxTscBurstSize) {
    this.maxTscBurstSize = maxTscBurstSize;
    return this;
  }

  /**
   * Unsigned integer indicating Maximum Data Burst Volume (see clauses 5.7.3.7 and 5.7.4 of 3GPP TS 23.501), expressed in Bytes.
   * minimum: 4096
   * maximum: 2000000
   * @return maxTscBurstSize
  */
  @Min(4096) @Max(2000000) 
  @Schema(name = "maxTscBurstSize", description = "Unsigned integer indicating Maximum Data Burst Volume (see clauses 5.7.3.7 and 5.7.4 of 3GPP TS 23.501), expressed in Bytes.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("maxTscBurstSize")
  public Integer getMaxTscBurstSize() {
    return maxTscBurstSize;
  }

  public void setMaxTscBurstSize(Integer maxTscBurstSize) {
    this.maxTscBurstSize = maxTscBurstSize;
  }

  public TscQosRequirement req5Gsdelay(Integer req5Gsdelay) {
    this.req5Gsdelay = req5Gsdelay;
    return this;
  }

  /**
   * Unsigned integer indicating Packet Delay Budget (see clauses 5.7.3.4 and 5.7.4 of 3GPP TS 23.501), expressed in milliseconds.
   * minimum: 1
   * @return req5Gsdelay
  */
  @Min(1) 
  @Schema(name = "req5Gsdelay", description = "Unsigned integer indicating Packet Delay Budget (see clauses 5.7.3.4 and 5.7.4 of 3GPP TS 23.501), expressed in milliseconds.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("req5Gsdelay")
  public Integer getReq5Gsdelay() {
    return req5Gsdelay;
  }

  public void setReq5Gsdelay(Integer req5Gsdelay) {
    this.req5Gsdelay = req5Gsdelay;
  }

  public TscQosRequirement tscaiTimeDom(Integer tscaiTimeDom) {
    this.tscaiTimeDom = tscaiTimeDom;
    return this;
  }

  /**
   * Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.
   * minimum: 0
   * @return tscaiTimeDom
  */
  @Min(0) 
  @Schema(name = "tscaiTimeDom", description = "Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("tscaiTimeDom")
  public Integer getTscaiTimeDom() {
    return tscaiTimeDom;
  }

  public void setTscaiTimeDom(Integer tscaiTimeDom) {
    this.tscaiTimeDom = tscaiTimeDom;
  }

  public TscQosRequirement tscaiInputDl(TscaiInputContainer tscaiInputDl) {
    this.tscaiInputDl = JsonNullable.of(tscaiInputDl);
    return this;
  }

  /**
   * Get tscaiInputDl
   * @return tscaiInputDl
  */
  @Valid 
  @Schema(name = "tscaiInputDl", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("tscaiInputDl")
  public JsonNullable<TscaiInputContainer> getTscaiInputDl() {
    return tscaiInputDl;
  }

  public void setTscaiInputDl(JsonNullable<TscaiInputContainer> tscaiInputDl) {
    this.tscaiInputDl = tscaiInputDl;
  }

  public TscQosRequirement tscaiInputUl(TscaiInputContainer tscaiInputUl) {
    this.tscaiInputUl = JsonNullable.of(tscaiInputUl);
    return this;
  }

  /**
   * Get tscaiInputUl
   * @return tscaiInputUl
  */
  @Valid 
  @Schema(name = "tscaiInputUl", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("tscaiInputUl")
  public JsonNullable<TscaiInputContainer> getTscaiInputUl() {
    return tscaiInputUl;
  }

  public void setTscaiInputUl(JsonNullable<TscaiInputContainer> tscaiInputUl) {
    this.tscaiInputUl = tscaiInputUl;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TscQosRequirement tscQosRequirement = (TscQosRequirement) o;
    return Objects.equals(this.reqGbrDl, tscQosRequirement.reqGbrDl) &&
        Objects.equals(this.reqGbrUl, tscQosRequirement.reqGbrUl) &&
        Objects.equals(this.reqMbrDl, tscQosRequirement.reqMbrDl) &&
        Objects.equals(this.reqMbrUl, tscQosRequirement.reqMbrUl) &&
        Objects.equals(this.maxTscBurstSize, tscQosRequirement.maxTscBurstSize) &&
        Objects.equals(this.req5Gsdelay, tscQosRequirement.req5Gsdelay) &&
        Objects.equals(this.tscaiTimeDom, tscQosRequirement.tscaiTimeDom) &&
        equalsNullable(this.tscaiInputDl, tscQosRequirement.tscaiInputDl) &&
        equalsNullable(this.tscaiInputUl, tscQosRequirement.tscaiInputUl);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(reqGbrDl, reqGbrUl, reqMbrDl, reqMbrUl, maxTscBurstSize, req5Gsdelay, tscaiTimeDom, hashCodeNullable(tscaiInputDl), hashCodeNullable(tscaiInputUl));
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
    sb.append("class TscQosRequirement {\n");
    sb.append("    reqGbrDl: ").append(toIndentedString(reqGbrDl)).append("\n");
    sb.append("    reqGbrUl: ").append(toIndentedString(reqGbrUl)).append("\n");
    sb.append("    reqMbrDl: ").append(toIndentedString(reqMbrDl)).append("\n");
    sb.append("    reqMbrUl: ").append(toIndentedString(reqMbrUl)).append("\n");
    sb.append("    maxTscBurstSize: ").append(toIndentedString(maxTscBurstSize)).append("\n");
    sb.append("    req5Gsdelay: ").append(toIndentedString(req5Gsdelay)).append("\n");
    sb.append("    tscaiTimeDom: ").append(toIndentedString(tscaiTimeDom)).append("\n");
    sb.append("    tscaiInputDl: ").append(toIndentedString(tscaiInputDl)).append("\n");
    sb.append("    tscaiInputUl: ").append(toIndentedString(tscaiInputUl)).append("\n");
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

