package net.i2cat.scef.client;

import java.util.Map;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;
import lombok.Data;

@Component
@ConfigurationProperties(prefix = "pcf.qos")
@Data
public class QoSConfiguration {

    private Map<String, String> references;
    private Map<String, String> qosE;
    private Map<String, String> qosS;
    private Map<String, String> qosM;
    private Map<String, String> qosL;
    private Map<String, String> qosA;
    private Map<String, String> qosB;
    private Map<String, String> qosC;
    private Map<String, String> qosD;
    private Map<String, String> qosF;
    private Map<String, String> qosG;
    private Map<String, String> qosH;
    private Map<String, String> qosI;
    private Map<String, String> qosJ;
    private Map<String, String> qosK;
    private Map<String, String> qosN;
    private Map<String, String> qosO;
    private Map<String, String> qosP;
    private Map<String, String> qosQ;
    private Map<String, String> qosR;
    private Map<String, String> qosT; // Final QoS profile (4K high)
}
