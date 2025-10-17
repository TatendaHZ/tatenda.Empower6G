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
 * Represents the same as the TscQosRequirement data type but with the nullable:true property.
 */

@Schema(name = "TscQosRequirementRm", description = "Represents the same as the TscQosRequirement data type but with the nullable:true property.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class TscQosRequirementRm {

  private JsonNullable<String> reqGbrDl = JsonNullable.undefined();

  private JsonNullable<String> reqGbrUl = JsonNullable.undefined();

  private JsonNullable<String> reqMbrDl = JsonNullable.undefined();

  private JsonNullable<String> reqMbrUl = JsonNullable.undefined();

  private JsonNullable<Integer> maxTscBurstSize = JsonNullable.undefined();

  private JsonNullable<Integer> req5Gsdelay = JsonNullable.undefined();

  private Integer tscaiTimeDom;

  private JsonNullable<TscaiInputContainer> tscaiInputDl = JsonNullable.undefined();

  private JsonNullable<TscaiInputContainer> tscaiInputUl = JsonNullable.undefined();

  public TscQosRequirementRm reqGbrDl(String reqGbrDl) {
    this.reqGbrDl = JsonNullable.of(reqGbrDl);
    return this;
  }

  /**
   * This data type is defined in the same way as the \"BitRate\" data type, but with the OpenAPI \"nullable= true\" property.
   * @return reqGbrDl
  */
  @Pattern(regexp = "^\\d+(\\.\\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$") 
  @Schema(name = "reqGbrDl", description = "This data type is defined in the same way as the \"BitRate\" data type, but with the OpenAPI \"nullable= true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("reqGbrDl")
  public JsonNullable<String> getReqGbrDl() {
    return reqGbrDl;
  }

  public void setReqGbrDl(JsonNullable<String> reqGbrDl) {
    this.reqGbrDl = reqGbrDl;
  }

  public TscQosRequirementRm reqGbrUl(String reqGbrUl) {
    this.reqGbrUl = JsonNullable.of(reqGbrUl);
    return this;
  }

  /**
   * This data type is defined in the same way as the \"BitRate\" data type, but with the OpenAPI \"nullable= true\" property.
   * @return reqGbrUl
  */
  @Pattern(regexp = "^\\d+(\\.\\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$") 
  @Schema(name = "reqGbrUl", description = "This data type is defined in the same way as the \"BitRate\" data type, but with the OpenAPI \"nullable= true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("reqGbrUl")
  public JsonNullable<String> getReqGbrUl() {
    return reqGbrUl;
  }

  public void setReqGbrUl(JsonNullable<String> reqGbrUl) {
    this.reqGbrUl = reqGbrUl;
  }

  public TscQosRequirementRm reqMbrDl(String reqMbrDl) {
    this.reqMbrDl = JsonNullable.of(reqMbrDl);
    return this;
  }

  /**
   * This data type is defined in the same way as the \"BitRate\" data type, but with the OpenAPI \"nullable= true\" property.
   * @return reqMbrDl
  */
  @Pattern(regexp = "^\\d+(\\.\\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$") 
  @Schema(name = "reqMbrDl", description = "This data type is defined in the same way as the \"BitRate\" data type, but with the OpenAPI \"nullable= true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("reqMbrDl")
  public JsonNullable<String> getReqMbrDl() {
    return reqMbrDl;
  }

  public void setReqMbrDl(JsonNullable<String> reqMbrDl) {
    this.reqMbrDl = reqMbrDl;
  }

  public TscQosRequirementRm reqMbrUl(String reqMbrUl) {
    this.reqMbrUl = JsonNullable.of(reqMbrUl);
    return this;
  }

  /**
   * This data type is defined in the same way as the \"BitRate\" data type, but with the OpenAPI \"nullable= true\" property.
   * @return reqMbrUl
  */
  @Pattern(regexp = "^\\d+(\\.\\d+)? (bps|Kbps|Mbps|Gbps|Tbps)$") 
  @Schema(name = "reqMbrUl", description = "This data type is defined in the same way as the \"BitRate\" data type, but with the OpenAPI \"nullable= true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("reqMbrUl")
  public JsonNullable<String> getReqMbrUl() {
    return reqMbrUl;
  }

  public void setReqMbrUl(JsonNullable<String> reqMbrUl) {
    this.reqMbrUl = reqMbrUl;
  }

  public TscQosRequirementRm maxTscBurstSize(Integer maxTscBurstSize) {
    this.maxTscBurstSize = JsonNullable.of(maxTscBurstSize);
    return this;
  }

  /**
   * This data type is defined in the same way as the \"ExtMaxDataBurstVol\" data type, but with the OpenAPI \"nullable= true\" property.
   * minimum: 4096
   * maximum: 2000000
   * @return maxTscBurstSize
  */
  @Min(4096) @Max(2000000) 
  @Schema(name = "maxTscBurstSize", description = "This data type is defined in the same way as the \"ExtMaxDataBurstVol\" data type, but with the OpenAPI \"nullable= true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("maxTscBurstSize")
  public JsonNullable<Integer> getMaxTscBurstSize() {
    return maxTscBurstSize;
  }

  public void setMaxTscBurstSize(JsonNullable<Integer> maxTscBurstSize) {
    this.maxTscBurstSize = maxTscBurstSize;
  }

  public TscQosRequirementRm req5Gsdelay(Integer req5Gsdelay) {
    this.req5Gsdelay = JsonNullable.of(req5Gsdelay);
    return this;
  }

  /**
   * This data type is defined in the same way as the \"PacketDelBudget\" data type, but with the OpenAPI \"nullable= true\" property
   * minimum: 1
   * @return req5Gsdelay
  */
  @Min(1) 
  @Schema(name = "req5Gsdelay", description = "This data type is defined in the same way as the \"PacketDelBudget\" data type, but with the OpenAPI \"nullable= true\" property", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("req5Gsdelay")
  public JsonNullable<Integer> getReq5Gsdelay() {
    return req5Gsdelay;
  }

  public void setReq5Gsdelay(JsonNullable<Integer> req5Gsdelay) {
    this.req5Gsdelay = req5Gsdelay;
  }

  public TscQosRequirementRm tscaiTimeDom(Integer tscaiTimeDom) {
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

  public TscQosRequirementRm tscaiInputDl(TscaiInputContainer tscaiInputDl) {
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

  public TscQosRequirementRm tscaiInputUl(TscaiInputContainer tscaiInputUl) {
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
    TscQosRequirementRm tscQosRequirementRm = (TscQosRequirementRm) o;
    return equalsNullable(this.reqGbrDl, tscQosRequirementRm.reqGbrDl) &&
        equalsNullable(this.reqGbrUl, tscQosRequirementRm.reqGbrUl) &&
        equalsNullable(this.reqMbrDl, tscQosRequirementRm.reqMbrDl) &&
        equalsNullable(this.reqMbrUl, tscQosRequirementRm.reqMbrUl) &&
        equalsNullable(this.maxTscBurstSize, tscQosRequirementRm.maxTscBurstSize) &&
        equalsNullable(this.req5Gsdelay, tscQosRequirementRm.req5Gsdelay) &&
        Objects.equals(this.tscaiTimeDom, tscQosRequirementRm.tscaiTimeDom) &&
        equalsNullable(this.tscaiInputDl, tscQosRequirementRm.tscaiInputDl) &&
        equalsNullable(this.tscaiInputUl, tscQosRequirementRm.tscaiInputUl);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(hashCodeNullable(reqGbrDl), hashCodeNullable(reqGbrUl), hashCodeNullable(reqMbrDl), hashCodeNullable(reqMbrUl), hashCodeNullable(maxTscBurstSize), hashCodeNullable(req5Gsdelay), tscaiTimeDom, hashCodeNullable(tscaiInputDl), hashCodeNullable(tscaiInputUl));
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
    sb.append("class TscQosRequirementRm {\n");
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

