package net.i2cat.scef.client;

import java.util.Map;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;
import lombok.Data;

@Component
@ConfigurationProperties(prefix = "pcf.qos")
@Data
public class QoSConfiguration {

    // maps QoS reference string -> profile key (e.g. "video-hd" -> "qosXL")
    private Map<String, String> references;

    // holds all QoS profiles, keyed by profile name (qosE, qosS, qosM, qosXL, etc.)
    private Map<String, Map<String, String>> qos;
}
