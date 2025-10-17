package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import autogen.scef.api.model.UserPlaneEventReport;
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
 * Represents the parameters to be conveyed in a user plane event(s) notification.
 */

@Schema(name = "UserPlaneNotificationData", description = "Represents the parameters to be conveyed in a user plane event(s) notification.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class UserPlaneNotificationData {

  private String transaction;

  @Valid
  private List<@Valid UserPlaneEventReport> eventReports = new ArrayList<>();

  public UserPlaneNotificationData() {
    super();
  }

  /**
   * Constructor with only required parameters
   */
  public UserPlaneNotificationData(String transaction, List<@Valid UserPlaneEventReport> eventReports) {
    this.transaction = transaction;
    this.eventReports = eventReports;
  }

  public UserPlaneNotificationData transaction(String transaction) {
    this.transaction = transaction;
    return this;
  }

  /**
   * string formatted according to IETF RFC 3986 identifying a referenced resource.
   * @return transaction
  */
  @NotNull 
  @Schema(name = "transaction", description = "string formatted according to IETF RFC 3986 identifying a referenced resource.", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("transaction")
  public String getTransaction() {
    return transaction;
  }

  public void setTransaction(String transaction) {
    this.transaction = transaction;
  }

  public UserPlaneNotificationData eventReports(List<@Valid UserPlaneEventReport> eventReports) {
    this.eventReports = eventReports;
    return this;
  }

  public UserPlaneNotificationData addEventReportsItem(UserPlaneEventReport eventReportsItem) {
    if (this.eventReports == null) {
      this.eventReports = new ArrayList<>();
    }
    this.eventReports.add(eventReportsItem);
    return this;
  }

  /**
   * Contains the reported event and applicable information
   * @return eventReports
  */
  @NotNull @Valid @Size(min = 1) 
  @Schema(name = "eventReports", description = "Contains the reported event and applicable information", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("eventReports")
  public List<@Valid UserPlaneEventReport> getEventReports() {
    return eventReports;
  }

  public void setEventReports(List<@Valid UserPlaneEventReport> eventReports) {
    this.eventReports = eventReports;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserPlaneNotificationData userPlaneNotificationData = (UserPlaneNotificationData) o;
    return Objects.equals(this.transaction, userPlaneNotificationData.transaction) &&
        Objects.equals(this.eventReports, userPlaneNotificationData.eventReports);
  }

  @Override
  public int hashCode() {
    return Objects.hash(transaction, eventReports);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserPlaneNotificationData {\n");
    sb.append("    transaction: ").append(toIndentedString(transaction)).append("\n");
    sb.append("    eventReports: ").append(toIndentedString(eventReports)).append("\n");
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

