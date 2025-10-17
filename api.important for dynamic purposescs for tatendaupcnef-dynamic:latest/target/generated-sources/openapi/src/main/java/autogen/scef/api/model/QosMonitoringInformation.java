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
import java.time.OffsetDateTime;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import jakarta.annotation.Generated;

/**
 * Represents QoS monitoring information.
 */

@Schema(name = "QosMonitoringInformation", description = "Represents QoS monitoring information.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class QosMonitoringInformation {

  @Valid
  private List<@Valid RequestedQosMonitoringParameter> reqQosMonParams = new ArrayList<>();

  @Valid
  private List<@Valid ReportingFrequency> repFreqs = new ArrayList<>();

  private Integer repThreshDl;

  private Integer repThreshUl;

  private Integer repThreshRp;

  private Integer waitTime;

  private Integer repPeriod;

  public QosMonitoringInformation() {
    super();
  }

  /**
   * Constructor with only required parameters
   */
  public QosMonitoringInformation(List<@Valid RequestedQosMonitoringParameter> reqQosMonParams, List<@Valid ReportingFrequency> repFreqs) {
    this.reqQosMonParams = reqQosMonParams;
    this.repFreqs = repFreqs;
  }

  public QosMonitoringInformation reqQosMonParams(List<@Valid RequestedQosMonitoringParameter> reqQosMonParams) {
    this.reqQosMonParams = reqQosMonParams;
    return this;
  }

  public QosMonitoringInformation addReqQosMonParamsItem(RequestedQosMonitoringParameter reqQosMonParamsItem) {
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
  @NotNull @Valid @Size(min = 1) 
  @Schema(name = "reqQosMonParams", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("reqQosMonParams")
  public List<@Valid RequestedQosMonitoringParameter> getReqQosMonParams() {
    return reqQosMonParams;
  }

  public void setReqQosMonParams(List<@Valid RequestedQosMonitoringParameter> reqQosMonParams) {
    this.reqQosMonParams = reqQosMonParams;
  }

  public QosMonitoringInformation repFreqs(List<@Valid ReportingFrequency> repFreqs) {
    this.repFreqs = repFreqs;
    return this;
  }

  public QosMonitoringInformation addRepFreqsItem(ReportingFrequency repFreqsItem) {
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
  @NotNull @Valid @Size(min = 1) 
  @Schema(name = "repFreqs", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("repFreqs")
  public List<@Valid ReportingFrequency> getRepFreqs() {
    return repFreqs;
  }

  public void setRepFreqs(List<@Valid ReportingFrequency> repFreqs) {
    this.repFreqs = repFreqs;
  }

  public QosMonitoringInformation repThreshDl(Integer repThreshDl) {
    this.repThreshDl = repThreshDl;
    return this;
  }

  /**
   * Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.
   * minimum: 0
   * @return repThreshDl
  */
  @Min(0) 
  @Schema(name = "repThreshDl", description = "Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("repThreshDl")
  public Integer getRepThreshDl() {
    return repThreshDl;
  }

  public void setRepThreshDl(Integer repThreshDl) {
    this.repThreshDl = repThreshDl;
  }

  public QosMonitoringInformation repThreshUl(Integer repThreshUl) {
    this.repThreshUl = repThreshUl;
    return this;
  }

  /**
   * Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.
   * minimum: 0
   * @return repThreshUl
  */
  @Min(0) 
  @Schema(name = "repThreshUl", description = "Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("repThreshUl")
  public Integer getRepThreshUl() {
    return repThreshUl;
  }

  public void setRepThreshUl(Integer repThreshUl) {
    this.repThreshUl = repThreshUl;
  }

  public QosMonitoringInformation repThreshRp(Integer repThreshRp) {
    this.repThreshRp = repThreshRp;
    return this;
  }

  /**
   * Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.
   * minimum: 0
   * @return repThreshRp
  */
  @Min(0) 
  @Schema(name = "repThreshRp", description = "Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("repThreshRp")
  public Integer getRepThreshRp() {
    return repThreshRp;
  }

  public void setRepThreshRp(Integer repThreshRp) {
    this.repThreshRp = repThreshRp;
  }

  public QosMonitoringInformation waitTime(Integer waitTime) {
    this.waitTime = waitTime;
    return this;
  }

  /**
   * indicating a time in seconds.
   * @return waitTime
  */
  
  @Schema(name = "waitTime", description = "indicating a time in seconds.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("waitTime")
  public Integer getWaitTime() {
    return waitTime;
  }

  public void setWaitTime(Integer waitTime) {
    this.waitTime = waitTime;
  }

  public QosMonitoringInformation repPeriod(Integer repPeriod) {
    this.repPeriod = repPeriod;
    return this;
  }

  /**
   * indicating a time in seconds.
   * @return repPeriod
  */
  
  @Schema(name = "repPeriod", description = "indicating a time in seconds.", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("repPeriod")
  public Integer getRepPeriod() {
    return repPeriod;
  }

  public void setRepPeriod(Integer repPeriod) {
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
    QosMonitoringInformation qosMonitoringInformation = (QosMonitoringInformation) o;
    return Objects.equals(this.reqQosMonParams, qosMonitoringInformation.reqQosMonParams) &&
        Objects.equals(this.repFreqs, qosMonitoringInformation.repFreqs) &&
        Objects.equals(this.repThreshDl, qosMonitoringInformation.repThreshDl) &&
        Objects.equals(this.repThreshUl, qosMonitoringInformation.repThreshUl) &&
        Objects.equals(this.repThreshRp, qosMonitoringInformation.repThreshRp) &&
        Objects.equals(this.waitTime, qosMonitoringInformation.waitTime) &&
        Objects.equals(this.repPeriod, qosMonitoringInformation.repPeriod);
  }

  @Override
  public int hashCode() {
    return Objects.hash(reqQosMonParams, repFreqs, repThreshDl, repThreshUl, repThreshRp, waitTime, repPeriod);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class QosMonitoringInformation {\n");
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

