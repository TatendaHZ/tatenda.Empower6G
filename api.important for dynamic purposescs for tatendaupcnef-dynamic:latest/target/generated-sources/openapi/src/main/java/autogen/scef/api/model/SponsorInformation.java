package autogen.scef.api.model;

import java.net.URI;
import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import org.openapitools.jackson.nullable.JsonNullable;
import java.time.OffsetDateTime;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import jakarta.annotation.Generated;

/**
 * Represents a sponsor information.
 */

@Schema(name = "SponsorInformation", description = "Represents a sponsor information.")
@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2025-09-30T14:53:46.427821530+03:00[Europe/Athens]")
public class SponsorInformation {

  private String sponsorId;

  private String aspId;

  public SponsorInformation() {
    super();
  }

  /**
   * Constructor with only required parameters
   */
  public SponsorInformation(String sponsorId, String aspId) {
    this.sponsorId = sponsorId;
    this.aspId = aspId;
  }

  public SponsorInformation sponsorId(String sponsorId) {
    this.sponsorId = sponsorId;
    return this;
  }

  /**
   * It indicates Sponsor ID.
   * @return sponsorId
  */
  @NotNull 
  @Schema(name = "sponsorId", description = "It indicates Sponsor ID.", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("sponsorId")
  public String getSponsorId() {
    return sponsorId;
  }

  public void setSponsorId(String sponsorId) {
    this.sponsorId = sponsorId;
  }

  public SponsorInformation aspId(String aspId) {
    this.aspId = aspId;
    return this;
  }

  /**
   * It indicates Application Service Provider ID.
   * @return aspId
  */
  @NotNull 
  @Schema(name = "aspId", description = "It indicates Application Service Provider ID.", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("aspId")
  public String getAspId() {
    return aspId;
  }

  public void setAspId(String aspId) {
    this.aspId = aspId;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SponsorInformation sponsorInformation = (SponsorInformation) o;
    return Objects.equals(this.sponsorId, sponsorInformation.sponsorId) &&
        Objects.equals(this.aspId, sponsorInformation.aspId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(sponsorId, aspId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SponsorInformation {\n");
    sb.append("    sponsorId: ").append(toIndentedString(sponsorId)).append("\n");
    sb.append("    aspId: ").append(toIndentedString(aspId)).append("\n");
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

