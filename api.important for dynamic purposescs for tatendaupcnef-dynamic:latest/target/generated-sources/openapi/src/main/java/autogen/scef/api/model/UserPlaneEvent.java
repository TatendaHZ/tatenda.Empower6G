package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonValue;
import org.openapitools.jackson.nullable.JsonNullable;
import java.time.OffsetDateTime;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import jakarta.annotation.Generated;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

/**
 * Possible values are - SESSION_TERMINATION: Indicates that Rx session is terminated. - LOSS_OF_BEARER : Indicates a loss of a bearer. - RECOVERY_OF_BEARER: Indicates a recovery of a bearer. - RELEASE_OF_BEARER: Indicates a release of a bearer. - USAGE_REPORT: Indicates the usage report event. - FAILED_RESOURCES_ALLOCATION: Indicates the resource allocation is failed. - QOS_GUARANTEED: The QoS targets of one or more SDFs are guaranteed again. - QOS_NOT_GUARANTEED: The QoS targets of one or more SDFs are not being guaranteed. - QOS_MONITORING: Indicates a QoS monitoring event. - SUCCESSFUL_RESOURCES_ALLOCATION: Indicates the resource allocation is successful. 
 */

@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public enum UserPlaneEvent {
  
  SESSION_TERMINATION("SESSION_TERMINATION"),
  
  LOSS_OF_BEARER("LOSS_OF_BEARER"),
  
  RECOVERY_OF_BEARE("RECOVERY_OF_BEARE"),
  
  RELEASE_OF_BEARER("RELEASE_OF_BEARER"),
  
  USAGE_REPORT("USAGE_REPORT"),
  
  FAILED_RESOURCES_ALLOCATION("FAILED_RESOURCES_ALLOCATION"),
  
  QOS_GUARANTEED("QOS_GUARANTEED"),
  
  QOS_NOT_GUARANTEED("QOS_NOT_GUARANTEED"),
  
  QOS_MONITORING("QOS_MONITORING"),
  
  SUCCESSFUL_RESOURCES_ALLOCATION("SUCCESSFUL_RESOURCES_ALLOCATION");

  private String value;

  UserPlaneEvent(String value) {
    this.value = value;
  }

  @JsonValue
  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  @JsonCreator
  public static UserPlaneEvent fromValue(String value) {
    for (UserPlaneEvent b : UserPlaneEvent.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }
}

