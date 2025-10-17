package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import autogen.scef.api.model.ReportingFrequency;
import autogen.scef.api.model.RequestedQosMonitoringParameter;
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
 * Represents the same as the QosMonitoringInformation data type but with the nullable:true property.
 */

@Schema(name = "QosMonitoringInformationRm", description = "Represents the same as the QosMonitoringInformation data type but with the nullable:true property.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class QosMonitoringInformationRm {

  @Valid
  private List<@Valid RequestedQosMonitoringParameter> reqQosMonParams;

  @Valid
  private List<@Valid ReportingFrequency> repFreqs;

  private JsonNullable<Integer> repThreshDl = JsonNullable.undefined();

  private JsonNullable<Integer> repThreshUl = JsonNullable.undefined();

  private JsonNullable<Integer> repThreshRp = JsonNullable.undefined();

  private JsonNullable<Integer> waitTime = JsonNullable.undefined();

  private JsonNullable<Integer> repPeriod = JsonNullable.undefined();

  public QosMonitoringInformationRm reqQosMonParams(List<@Valid RequestedQosMonitoringParameter> reqQosMonParams) {
    this.reqQosMonParams = reqQosMonParams;
    return this;
  }

  public QosMonitoringInformationRm addReqQosMonParamsItem(RequestedQosMonitoringParameter reqQosMonParamsItem) {
    if (this.reqQosMonParams == null) {
      this.reqQosMonParams = new ArrayList<>();
    }
    this.reqQosMonParams.add(reqQosMonParamsItem);
    return this;
  }

  /**
   * Get reqQosMonParams
   * @return reqQosMonParams
  */
  @Valid @Size(min = 1) 
  @Schema(name = "reqQosMonParams", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("reqQosMonParams")
  public List<@Valid RequestedQosMonitoringParameter> getReqQosMonParams() {
    return reqQosMonParams;
  }

  public void setReqQosMonParams(List<@Valid RequestedQosMonitoringParameter> reqQosMonParams) {
    this.reqQosMonParams = reqQosMonParams;
  }

  public QosMonitoringInformationRm repFreqs(List<@Valid ReportingFrequency> repFreqs) {
    this.repFreqs = repFreqs;
    return this;
  }

  public QosMonitoringInformationRm addRepFreqsItem(ReportingFrequency repFreqsItem) {
    if (this.repFreqs == null) {
      this.repFreqs = new ArrayList<>();
    }
    this.repFreqs.add(repFreqsItem);
    return this;
  }

  /**
   * Get repFreqs
   * @return repFreqs
  */
  @Valid @Size(min = 1) 
  @Schema(name = "repFreqs", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("repFreqs")
  public List<@Valid ReportingFrequency> getRepFreqs() {
    return repFreqs;
  }

  public void setRepFreqs(List<@Valid ReportingFrequency> repFreqs) {
    this.repFreqs = repFreqs;
  }

  public QosMonitoringInformationRm repThreshDl(Integer repThreshDl) {
    this.repThreshDl = JsonNullable.of(repThreshDl);
    return this;
  }

  /**
   * Unsigned Integer, i.e. only value 0 and integers above 0 are permissible with the OpenAPI \"nullable= true\" property.
   * minimum: 0
   * @return repThreshDl
  */
  @Min(0) 
  @Schema(name = "repThreshDl", description = "Unsigned Integer, i.e. only value 0 and integers above 0 are permissible with the OpenAPI \"nullable= true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("repThreshDl")
  public JsonNullable<Integer> getRepThreshDl() {
    return repThreshDl;
  }

  public void setRepThreshDl(JsonNullable<Integer> repThreshDl) {
    this.repThreshDl = repThreshDl;
  }

  public QosMonitoringInformationRm repThreshUl(Integer repThreshUl) {
    this.repThreshUl = JsonNullable.of(repThreshUl);
    return this;
  }

  /**
   * Unsigned Integer, i.e. only value 0 and integers above 0 are permissible with the OpenAPI \"nullable= true\" property.
   * minimum: 0
   * @return repThreshUl
  */
  @Min(0) 
  @Schema(name = "repThreshUl", description = "Unsigned Integer, i.e. only value 0 and integers above 0 are permissible with the OpenAPI \"nullable= true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("repThreshUl")
  public JsonNullable<Integer> getRepThreshUl() {
    return repThreshUl;
  }

  public void setRepThreshUl(JsonNullable<Integer> repThreshUl) {
    this.repThreshUl = repThreshUl;
  }

  public QosMonitoringInformationRm repThreshRp(Integer repThreshRp) {
    this.repThreshRp = JsonNullable.of(repThreshRp);
    return this;
  }

  /**
   * Unsigned Integer, i.e. only value 0 and integers above 0 are permissible with the OpenAPI \"nullable= true\" property.
   * minimum: 0
   * @return repThreshRp
  */
  @Min(0) 
  @Schema(name = "repThreshRp", description = "Unsigned Integer, i.e. only value 0 and integers above 0 are permissible with the OpenAPI \"nullable= true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("repThreshRp")
  public JsonNullable<Integer> getRepThreshRp() {
    return repThreshRp;
  }

  public void setRepThreshRp(JsonNullable<Integer> repThreshRp) {
    this.repThreshRp = repThreshRp;
  }

  public QosMonitoringInformationRm waitTime(Integer waitTime) {
    this.waitTime = JsonNullable.of(waitTime);
    return this;
  }

  /**
   * indicating a time in seconds with OpenAPI defined \"nullable=true\" property.
   * @return waitTime
  */
  
  @Schema(name = "waitTime", description = "indicating a time in seconds with OpenAPI defined \"nullable=true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("waitTime")
  public JsonNullable<Integer> getWaitTime() {
    return waitTime;
  }

  public void setWaitTime(JsonNullable<Integer> waitTime) {
    this.waitTime = waitTime;
  }

  public QosMonitoringInformationRm repPeriod(Integer repPeriod) {
    this.repPeriod = JsonNullable.of(repPeriod);
    return this;
  }

  /**
   * indicating a time in seconds with OpenAPI defined \"nullable=true\" property.
   * @return repPeriod
  */
  
  @Schema(name = "repPeriod", description = "indicating a time in seconds with OpenAPI defined \"nullable=true\" property.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("repPeriod")
  public JsonNullable<Integer> getRepPeriod() {
    return repPeriod;
  }

  public void setRepPeriod(JsonNullable<Integer> repPeriod) {
    this.repPeriod = repPeriod;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    QosMonitoringInformationRm qosMonitoringInformationRm = (QosMonitoringInformationRm) o;
    return Objects.equals(this.reqQosMonParams, qosMonitoringInformationRm.reqQosMonParams) &&
        Objects.equals(this.repFreqs, qosMonitoringInformationRm.repFreqs) &&
        equalsNullable(this.repThreshDl, qosMonitoringInformationRm.repThreshDl) &&
        equalsNullable(this.repThreshUl, qosMonitoringInformationRm.repThreshUl) &&
        equalsNullable(this.repThreshRp, qosMonitoringInformationRm.repThreshRp) &&
        equalsNullable(this.waitTime, qosMonitoringInformationRm.waitTime) &&
        equalsNullable(this.repPeriod, qosMonitoringInformationRm.repPeriod);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(reqQosMonParams, repFreqs, hashCodeNullable(repThreshDl), hashCodeNullable(repThreshUl), hashCodeNullable(repThreshRp), hashCodeNullable(waitTime), hashCodeNullable(repPeriod));
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
    sb.append("class QosMonitoringInformationRm {\n");
    sb.append("    reqQosMonParams: ").append(toIndentedString(reqQosMonParams)).append("\n");
    sb.append("    repFreqs: ").append(toIndentedString(repFreqs)).append("\n");
    sb.append("    repThreshDl: ").append(toIndentedString(repThreshDl)).append("\n");
    sb.append("    repThreshUl: ").append(toIndentedString(repThreshUl)).append("\n");
    sb.append("    repThreshRp: ").append(toIndentedString(repThreshRp)).append("\n");
    sb.append("    waitTime: ").append(toIndentedString(waitTime)).append("\n");
    sb.append("    repPeriod: ").append(toIndentedString(repPeriod)).append("\n");
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

