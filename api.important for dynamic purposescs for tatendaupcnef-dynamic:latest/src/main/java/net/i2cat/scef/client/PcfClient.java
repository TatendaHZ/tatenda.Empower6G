package net.i2cat.scef.client;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import autogen.pcf.api.ApiClient;
import autogen.pcf.api.ApiResponse;
import autogen.pcf.api.ApplicationSessionsCollectionApi;
import autogen.pcf.api.IndividualApplicationSessionContextDocumentApi;
import autogen.pcf.api.model.AppSessionContext;
import autogen.pcf.api.model.AppSessionContextReqData;
import autogen.pcf.api.model.FlowStatus;
import autogen.pcf.api.model.FlowUsage;
import autogen.pcf.api.model.MediaComponent;
import autogen.pcf.api.model.MediaSubComponent;
import autogen.pcf.api.model.MediaType;
import autogen.scef.api.model.AsSessionWithQoSSubscription;
import autogen.scef.api.model.FlowInfo;
import jakarta.annotation.PostConstruct;
import lombok.RequiredArgsConstructor;
import okhttp3.OkHttpClient;
import okhttp3.OkHttpClient.Builder;
import okhttp3.Protocol;

@Service
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
public class PcfClient {

    static final Log log = LogFactory.getLog(PcfClient.class);

    private final QoSConfiguration qoSConfiguration;

    @Value("${pcf.basepath}")
    private String basepath;

    @Value("${pcf.notifuri}")
    private String notifuri;

    @Value("${pcf.suppfeat}")
    private String suppfeat;

    private ApplicationSessionsCollectionApi pcfCreateApi = new ApplicationSessionsCollectionApi();
    private IndividualApplicationSessionContextDocumentApi pcfDeleteApi = new IndividualApplicationSessionContextDocumentApi();

    @PostConstruct
    private void initClient() {
        log.info("************************ Calling initClient ************************");

        ApiClient apiClient = pcfCreateApi.getApiClient();
        apiClient.setBasePath(basepath);
        OkHttpClient.Builder b = new Builder(apiClient.getHttpClient());
        apiClient.setHttpClient(b.protocols(Arrays.asList(Protocol.H2_PRIOR_KNOWLEDGE)).build());

        ApiClient apiClient2 = pcfDeleteApi.getApiClient();
        apiClient2.setBasePath(basepath);
        OkHttpClient.Builder b2 = new Builder(apiClient2.getHttpClient());
        apiClient2.setHttpClient(b2.protocols(Arrays.asList(Protocol.H2_PRIOR_KNOWLEDGE)).build());
    }

    public String postAppSession(AsSessionWithQoSSubscription asSession, String internalSessionId) {
        log.info("*********************** Calling postAppSession ***********************");
        log.info("" + asSession);

        AppSessionContextReqData request = new AppSessionContextReqData();
        request.setUeIpv4(asSession.getUeIpv4Addr());
        request.setNotifUri(notifuri + "/" + internalSessionId);
        request.setSuppFeat(suppfeat);

        Map<String, MediaSubComponent> mscList = new HashMap<>();
        for (FlowInfo fInfo : asSession.getFlowInfo()) {
            MediaSubComponent msc = new MediaSubComponent();
            msc.setfNum(fInfo.getFlowId());
            for (String flowdesc : fInfo.getFlowDescriptions()) {
                msc.addFDescsItem(flowdesc);
            }
            msc.setFlowUsage(FlowUsage.NO_INFO);
            mscList.put(Integer.toString(fInfo.getFlowId()), msc);
        }

        MediaComponent mc = new MediaComponent();
        mc.setMedCompN(1);
        mc.setMedSubComps(mscList);
        mc.setfStatus(FlowStatus.ENABLED);

        // --- Dynamic QoS lookup ---
        String qosKey = qoSConfiguration.getReferences().get(asSession.getQosReference());
        Map<String, String> qosValues = qoSConfiguration.getQos().get(qosKey);

        if (qosValues != null) {
            mc.setMarBwDl(qosValues.get("marBwDl"));
            mc.setMarBwUl(qosValues.get("marBwUl"));
            mc.setMedType(MediaType.fromValue(qosValues.get("mediaType")));
        } else {
            mc.setMedType(MediaType.VIDEO); // fallback
        }

        Map<String, MediaComponent> mcList = new HashMap<>();
        mcList.put("1", mc);
        request.setMedComponents(mcList);

        AppSessionContext context = new AppSessionContext();
        context.setAscReqData(request);

        String sessionId = null;
        try {
            ApiResponse<AppSessionContext> returnedContext = pcfCreateApi.postAppSessionsWithHttpInfo(context);
            if (returnedContext != null) {
                log.info("Returned context: " + returnedContext.getData());
                String location = returnedContext.getHeaders().get("location").get(0);
                if (location != null) {
                    log.info("Location: " + location);
                    sessionId = location.substring(location.lastIndexOf("/") + 1);
                }
            }
        } catch (Exception e) {
            log.info("Error creating AppSession in PCF", e);
            return null;
        }
        return sessionId;
    }

    public void deleteAppSession(String appSessionId) {
        log.info("********************** Calling deleteAppSession **********************");
        try {
            pcfDeleteApi.deleteAppSession(appSessionId, null);
        } catch (Exception e) {
            log.info("Error deleting AppSession in PCF", e);
        }
    }
}
