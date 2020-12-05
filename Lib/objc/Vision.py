"""
Classes from the 'Vision' framework.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


VNImageRequestHandler = _Class("VNImageRequestHandler")
VNCircle = _Class("VNCircle")
VNPersonsModelData = _Class("VNPersonsModelData")
VNImageRegistration = _Class("VNImageRegistration")
VNANFDDetectorCompoundRequestConfigurationGroups = _Class(
    "VNANFDDetectorCompoundRequestConfigurationGroups"
)
VNRequestPerformingContext = _Class("VNRequestPerformingContext")
VNBrightnessMeasure = _Class("VNBrightnessMeasure")
ShotflowNetwork = _Class("ShotflowNetwork")
ShotflowNetworkANODBase = _Class("ShotflowNetworkANODBase")
ShotflowNetworkANODv3 = _Class("ShotflowNetworkANODv3")
ShotflowNetworkANFDv2 = _Class("ShotflowNetworkANFDv2")
ShotflowNetworkANFDv1 = _Class("ShotflowNetworkANFDv1")
VNMPContext = _Class("VNMPContext")
VNClustererBuilder = _Class("VNClustererBuilder")
VNClustererQuery = _Class("VNClustererQuery")
VNClustererOptions = _Class("VNClustererOptions")
VNClustererBuilderOptions = _Class("VNClustererBuilderOptions")
VNClustererQueryOptions = _Class("VNClustererQueryOptions")
VNClassificationCustomHierarchy = _Class("VNClassificationCustomHierarchy")
_VNImageAnalyzerMultiDetectorClassificationCustomHierarchy = _Class(
    "_VNImageAnalyzerMultiDetectorClassificationCustomHierarchy"
)
_VNSceneClassifierClassificationCustomHierarchy = _Class(
    "_VNSceneClassifierClassificationCustomHierarchy"
)
VNANFDMultiDetectorOriginalRequestInfo = _Class(
    "VNANFDMultiDetectorOriginalRequestInfo"
)
VNRequestPerformer = _Class("VNRequestPerformer")
ShotflowDetection = _Class("ShotflowDetection")
VNContour = _Class("VNContour")
VNRecognizedText = _Class("VNRecognizedText")
VNObservationsCache = _Class("VNObservationsCache")
CCTextDetector = _Class("CCTextDetector")
CCCharBoxContext = _Class("CCCharBoxContext")
_VNImageAnalyzerMultiDetectorSceneOperationPointsProvider = _Class(
    "_VNImageAnalyzerMultiDetectorSceneOperationPointsProvider"
)
_VNImageAnalyzerMultiDetectorSceneOperationPointsCache = _Class(
    "_VNImageAnalyzerMultiDetectorSceneOperationPointsCache"
)
VNVector = _Class("VNVector")
VNBurstContext = _Class("VNBurstContext")
VNMPImageDescriptor = _Class("VNMPImageDescriptor")
VNContourPerimeterAlgorithm = _Class("VNContourPerimeterAlgorithm")
VNContourAreaCalculationAlgorithm = _Class("VNContourAreaCalculationAlgorithm")
VNBoundingCircleAlgorithm = _Class("VNBoundingCircleAlgorithm")
VNGeometryUtils = _Class("VNGeometryUtils")
VNWeakSessionWrapper = _Class("VNWeakSessionWrapper")
VNSession = _Class("VNSession")
_VNGlobalSession = _Class("_VNGlobalSession")
VNModelFilesCache = _Class("VNModelFilesCache")
VNModelFileImpl = _Class("VNModelFileImpl")
BurstThumbnailCluster = _Class("BurstThumbnailCluster")
VNFaceSegments = _Class("VNFaceSegments")
ParabolaDetetction = _Class("ParabolaDetetction")
VNImageClassifier = _Class("VNImageClassifier")
VNFaceLegacyFaceCore = _Class("VNFaceLegacyFaceCore")
VNCoreMLModel = _Class("VNCoreMLModel")
VNMLFeatureProvider = _Class("VNMLFeatureProvider")
MPImageDescriptor_LegacySupportDoNotChange = _Class(
    "MPImageDescriptor_LegacySupportDoNotChange"
)
CVMLObservation_LegacySupportDoNotChange = _Class(
    "CVMLObservation_LegacySupportDoNotChange"
)
CVMLImageprintObservation_LegacySupportDoNotChange = _Class(
    "CVMLImageprintObservation_LegacySupportDoNotChange"
)
CVMLFaceprint_LegacySupportDoNotChange = _Class(
    "CVMLFaceprint_LegacySupportDoNotChange"
)
VNBlacklist = _Class("VNBlacklist")
VNValidationUtilities = _Class("VNValidationUtilities")
VNFaceLandmarks = _Class("VNFaceLandmarks")
VNFaceLandmarks3D = _Class("VNFaceLandmarks3D")
VNFaceLandmarks2D = _Class("VNFaceLandmarks2D")
VNFaceLandmarkRegion = _Class("VNFaceLandmarkRegion")
VNFaceLandmarkRegion3D = _Class("VNFaceLandmarkRegion3D")
VNFaceLandmarkRegion2D = _Class("VNFaceLandmarkRegion2D")
MetalInterface = _Class("MetalInterface")
VNDetectionprint = _Class("VNDetectionprint")
VNEspressoHelpers = _Class("VNEspressoHelpers")
VNEspressoResources = _Class("VNEspressoResources")
VNMPImageGrouping = _Class("VNMPImageGrouping")
BurstImageSetInternal = _Class("BurstImageSetInternal")
VNPersonsModelFaceModel = _Class("VNPersonsModelFaceModel")
VNSequenceRequestHandler = _Class("VNSequenceRequestHandler")
VNCVPixelBufferConversionHelpers = _Class("VNCVPixelBufferConversionHelpers")
VNImageGrouper = _Class("VNImageGrouper")
VNDetectorCache = _Class("VNDetectorCache")
VNHeatMapUtilities = _Class("VNHeatMapUtilities")
VNHeatMapExtrema = _Class("VNHeatMapExtrema")
VNVersionParser = _Class("VNVersionParser")
VNCluster = _Class("VNCluster")
VNTrajectoryProcessor = _Class("VNTrajectoryProcessor")
VNImageprint = _Class("VNImageprint")
LKTOpticalFlow = _Class("LKTOpticalFlow")
LKTOpticalFlowCPU = _Class("LKTOpticalFlowCPU")
LKTOpticalFlowGPU = _Class("LKTOpticalFlowGPU")
VNOperationPoints = _Class("VNOperationPoints")
VNSceneTaxonomyOperationPoints = _Class("VNSceneTaxonomyOperationPoints")
_VNUnspecifiedOperationPoints = _Class("_VNUnspecifiedOperationPoints")
VNMPImageData = _Class("VNMPImageData")
VNTrackerManager = _Class("VNTrackerManager")
ShotflowDetector = _Class("ShotflowDetector")
ShotflowDetectorANODBase = _Class("ShotflowDetectorANODBase")
ShotflowDetectorANODv3 = _Class("ShotflowDetectorANODv3")
ShotflowDetectorANFDv2 = _Class("ShotflowDetectorANFDv2")
ShotflowDetectorANFDv1 = _Class("ShotflowDetectorANFDv1")
VNVideoProcessor = _Class("VNVideoProcessor")
VNVideoProcessorRequestProcessingOptions = _Class(
    "VNVideoProcessorRequestProcessingOptions"
)
VNVideoProcessorCadence = _Class("VNVideoProcessorCadence")
VNVideoProcessorTimeIntervalCadence = _Class("VNVideoProcessorTimeIntervalCadence")
VNVideoProcessorFrameRateCadence = _Class("VNVideoProcessorFrameRateCadence")
VNOperationPointsProvider = _Class("VNOperationPointsProvider")
VNMPUtils = _Class("VNMPUtils")
VNImageSignature = _Class("VNImageSignature")
VNImageRegistrationSignature = _Class("VNImageRegistrationSignature")
VNWarningRecorder = _Class("VNWarningRecorder")
VNMTLDeviceWisdomParameters = _Class("VNMTLDeviceWisdomParameters")
VNFaceAttributes = _Class("VNFaceAttributes")
VNFaceAttributeCategory = _Class("VNFaceAttributeCategory")
VNPersonsModelWriteOptions = _Class("VNPersonsModelWriteOptions")
VNPersonsModelReadOptions = _Class("VNPersonsModelReadOptions")
VNPersonsModelPrediction = _Class("VNPersonsModelPrediction")
VNPersonsModelConfiguration = _Class("VNPersonsModelConfiguration")
VNPersonsModelInformation = _Class("VNPersonsModelInformation")
_VNPersonsModelDataSourceBasedDataProvider = _Class(
    "_VNPersonsModelDataSourceBasedDataProvider"
)
BurstClusterDivider = _Class("BurstClusterDivider")
VNObservation = _Class("VNObservation")
VNTrajectoryObservation = _Class("VNTrajectoryObservation")
VNBurstObservation = _Class("VNBurstObservation")
VNSmartCamObservation = _Class("VNSmartCamObservation")
VNFeaturePrintObservation = _Class("VNFeaturePrintObservation")
VNSceneObservation = _Class("VNSceneObservation")
VNClusterObservation = _Class("VNClusterObservation")
VNHorizonObservation = _Class("VNHorizonObservation")
VNCoreMLFeatureValueObservation = _Class("VNCoreMLFeatureValueObservation")
VNClassificationObservation = _Class("VNClassificationObservation")
VNImageprintObservation = _Class("VNImageprintObservation")
VNImageScoreObservation = _Class("VNImageScoreObservation")
VNImageBrightnessObservation = _Class("VNImageBrightnessObservation")
VNImageBlurObservation = _Class("VNImageBlurObservation")
VNImageAlignmentObservation = _Class("VNImageAlignmentObservation")
VNImageHomographicAlignmentObservation = _Class(
    "VNImageHomographicAlignmentObservation"
)
VNImageTranslationAlignmentObservation = _Class(
    "VNImageTranslationAlignmentObservation"
)
VNContoursObservation = _Class("VNContoursObservation")
VNImageAestheticsObservation = _Class("VNImageAestheticsObservation")
VNDetectedObjectObservation = _Class("VNDetectedObjectObservation")
VNRecognizedObjectObservation = _Class("VNRecognizedObjectObservation")
VNFaceObservation = _Class("VNFaceObservation")
VNRectangleObservation = _Class("VNRectangleObservation")
VNTextObservation = _Class("VNTextObservation")
_VNTextObservationCharacterBox = _Class("_VNTextObservationCharacterBox")
VNRecognizedTextObservation = _Class("VNRecognizedTextObservation")
VNBarcodeObservation = _Class("VNBarcodeObservation")
VNRecognizedPointsObservation = _Class("VNRecognizedPointsObservation")
VNHumanBodyPoseObservation = _Class("VNHumanBodyPoseObservation")
VNHumanHandPoseObservation = _Class("VNHumanHandPoseObservation")
VNDetectionprintObservation = _Class("VNDetectionprintObservation")
VNPixelBufferObservation = _Class("VNPixelBufferObservation")
VNOpticalFlowObservation = _Class("VNOpticalFlowObservation")
VNSaliencyImageObservation = _Class("VNSaliencyImageObservation")
VNImageSaliencyObservation = _Class("VNImageSaliencyObservation")
SaliencyExtrema = _Class("SaliencyExtrema")
VNEspressoDetectedObject = _Class("VNEspressoDetectedObject")
ANFDDetectedObject = _Class("ANFDDetectedObject")
VNMPClusteringTreeNodeWrapper = _Class("VNMPClusteringTreeNodeWrapper")
VNMomentProcessor = _Class("VNMomentProcessor")
VNEspressoModelImageprint = _Class("VNEspressoModelImageprint")
VNTorsoprint = _Class("VNTorsoprint")
VNDetectionprintTensor = _Class("VNDetectionprintTensor")
VNSmartCamprint = _Class("VNSmartCamprint")
VNSceneprint = _Class("VNSceneprint")
VNSceneFeaturePrint = _Class("VNSceneFeaturePrint")
VNFaceprint = _Class("VNFaceprint")
VNFaceTorsoprint = _Class("VNFaceTorsoprint")
VNSupportedImageSize = _Class("VNSupportedImageSize")
VNSizeRange = _Class("VNSizeRange")
VNPoint = _Class("VNPoint")
VNDetectedPoint = _Class("VNDetectedPoint")
VNRecognizedPoint = _Class("VNRecognizedPoint")
VNPersonsModel = _Class("VNPersonsModel")
VNReadOnlyPersonsModel = _Class("VNReadOnlyPersonsModel")
VNMutablePersonsModel = _Class("VNMutablePersonsModel")
VNRPNTrackerEspressoModelCacheManager = _Class("VNRPNTrackerEspressoModelCacheManager")
VNFrameworkManager = _Class("VNFrameworkManager")
_VNWeakSessionsCollection = _Class("_VNWeakSessionsCollection")
VNImageBuffer = _Class("VNImageBuffer")
VNImageSourceManager = _Class("VNImageSourceManager")
VNImageBufferManager = _Class("VNImageBufferManager")
VNFaceAnalyzerFaceObservationGrouping = _Class("VNFaceAnalyzerFaceObservationGrouping")
VNFaceAnalyzerCompoundRequestConfigurationGroups = _Class(
    "VNFaceAnalyzerCompoundRequestConfigurationGroups"
)
VNCanceller = _Class("VNCanceller")
VNRuntimeUtilities = _Class("VNRuntimeUtilities")
VNProcessingDevice = _Class("VNProcessingDevice")
VNCPUProcessingDevice = _Class("VNCPUProcessingDevice")
VNMetalProcessingDevice = _Class("VNMetalProcessingDevice")
VNANEProcessingDevice = _Class("VNANEProcessingDevice")
VNANERuntimeProcessingDevice = _Class("VNANERuntimeProcessingDevice")
VNANERuntimeDirectProcessingDevice = _Class("VNANERuntimeDirectProcessingDevice")
VNFaceRegionMap = _Class("VNFaceRegionMap")
VNImageAnalyzerCompoundRequestGroupingConfigurations = _Class(
    "VNImageAnalyzerCompoundRequestGroupingConfigurations"
)
VNImageAnalyzerCompoundRequestGroupingConfiguration = _Class(
    "VNImageAnalyzerCompoundRequestGroupingConfiguration"
)
VNMetalContext = _Class("VNMetalContext")
VNBlurMeasure = _Class("VNBlurMeasure")
VNBlurSignature = _Class("VNBlurSignature")
VNPhotosRequestHandler = _Class("VNPhotosRequestHandler")
VNTracker = _Class("VNTracker")
VNRectangleTracker = _Class("VNRectangleTracker")
VNObjectTracker = _Class("VNObjectTracker")
VNObjectTrackerRevision1 = _Class("VNObjectTrackerRevision1")
VNObjectTrackerRevision2 = _Class("VNObjectTrackerRevision2")
VNObjectTrackerLegacyFaceCore = _Class("VNObjectTrackerLegacyFaceCore")
BurstImageStat = _Class("BurstImageStat")
BurstFaceStat = _Class("BurstFaceStat")
VNRequestConfiguration = _Class("VNRequestConfiguration")
VNANFDDetectorCompoundRequestConfiguration = _Class(
    "VNANFDDetectorCompoundRequestConfiguration"
)
VNAlignFaceRectangleRequestConfiguration = _Class(
    "VNAlignFaceRectangleRequestConfiguration"
)
VNFaceAnalyzerCompoundRequestConfiguration = _Class(
    "VNFaceAnalyzerCompoundRequestConfiguration"
)
VNImageAnalyzerCompoundRequestConfiguration = _Class(
    "VNImageAnalyzerCompoundRequestConfiguration"
)
VNImageBasedRequestConfiguration = _Class("VNImageBasedRequestConfiguration")
VNGenerateObjectnessBasedSaliencyImageRequestConfiguration = _Class(
    "VNGenerateObjectnessBasedSaliencyImageRequestConfiguration"
)
VNCreateFaceprintRequestConfiguration = _Class("VNCreateFaceprintRequestConfiguration")
VNCoreMLRequestConfiguration = _Class("VNCoreMLRequestConfiguration")
VNCreateSceneprintRequestConfiguration = _Class(
    "VNCreateSceneprintRequestConfiguration"
)
VNDetectRectanglesRequestConfiguration = _Class(
    "VNDetectRectanglesRequestConfiguration"
)
VNRecognizeTextRequestConfiguration = _Class("VNRecognizeTextRequestConfiguration")
VNDetectContoursRequestConfiguration = _Class("VNDetectContoursRequestConfiguration")
VNCreateSmartCamprintRequestConfiguration = _Class(
    "VNCreateSmartCamprintRequestConfiguration"
)
VNDetectFaceCaptureQualityRequestConfiguration = _Class(
    "VNDetectFaceCaptureQualityRequestConfiguration"
)
VNDetectFaceRectanglesRequestConfiguration = _Class(
    "VNDetectFaceRectanglesRequestConfiguration"
)
VNGenerateFaceSegmentsRequestConfiguration = _Class(
    "VNGenerateFaceSegmentsRequestConfiguration"
)
VNDetectHumanBodyPoseRequestConfiguration = _Class(
    "VNDetectHumanBodyPoseRequestConfiguration"
)
VNCreateImageprintRequestConfiguration = _Class(
    "VNCreateImageprintRequestConfiguration"
)
VNImageBlurScoreRequestConfiguration = _Class("VNImageBlurScoreRequestConfiguration")
VNdGg5skzXHSAENO6T3enHEConfiguration = _Class("VNdGg5skzXHSAENO6T3enHEConfiguration")
VNGenerateImageSaliencyRequestConfiguration = _Class(
    "VNGenerateImageSaliencyRequestConfiguration"
)
VNDetectFaceLandmarksRequestConfiguration = _Class(
    "VNDetectFaceLandmarksRequestConfiguration"
)
VNNOPRequestConfiguration = _Class("VNNOPRequestConfiguration")
VNDetectHumanHandPoseRequestConfiguration = _Class(
    "VNDetectHumanHandPoseRequestConfiguration"
)
VNGenerateImageFeaturePrintRequestConfiguration = _Class(
    "VNGenerateImageFeaturePrintRequestConfiguration"
)
VNDetectBarcodesRequestConfiguration = _Class("VNDetectBarcodesRequestConfiguration")
VNCreateDetectionprintRequestConfiguration = _Class(
    "VNCreateDetectionprintRequestConfiguration"
)
VNClassifyImageRequestConfiguration = _Class("VNClassifyImageRequestConfiguration")
VNDetectTextRectanglesRequestConfiguration = _Class(
    "VNDetectTextRectanglesRequestConfiguration"
)
VNRecognizeObjectsRequestConfiguration = _Class(
    "VNRecognizeObjectsRequestConfiguration"
)
VNClassifyImageAestheticsRequestConfiguration = _Class(
    "VNClassifyImageAestheticsRequestConfiguration"
)
VNVYvzEtX1JlUdu8xx5qhDIConfiguration = _Class("VNVYvzEtX1JlUdu8xx5qhDIConfiguration")
VNGenerateAttentionBasedSaliencyImageRequestConfiguration = _Class(
    "VNGenerateAttentionBasedSaliencyImageRequestConfiguration"
)
VN5kJNH3eYuyaLxNpZr5Z7ziConfiguration = _Class("VN5kJNH3eYuyaLxNpZr5Z7ziConfiguration")
VNClassifyPotentialLandmarkRequestConfiguration = _Class(
    "VNClassifyPotentialLandmarkRequestConfiguration"
)
VNStatefulRequestConfiguration = _Class("VNStatefulRequestConfiguration")
VNDetectTrajectoriesRequestConfiguration = _Class(
    "VNDetectTrajectoriesRequestConfiguration"
)
VNSceneClassificationRequestConfiguration = _Class(
    "VNSceneClassificationRequestConfiguration"
)
VNClassifyJunkImageRequestConfiguration = _Class(
    "VNClassifyJunkImageRequestConfiguration"
)
VNError = _Class("VNError")
LKTMetalContext = _Class("LKTMetalContext")
VNRequestForensics = _Class("VNRequestForensics")
_VNRequestForensicsParentChildRequests = _Class(
    "_VNRequestForensicsParentChildRequests"
)
_VNRequestForensicsRequestAndObservationsCacheKeyTuple = _Class(
    "_VNRequestForensicsRequestAndObservationsCacheKeyTuple"
)
_VNRequestForensicsRequestAndErrorTuple = _Class(
    "_VNRequestForensicsRequestAndErrorTuple"
)
VNClustererContextBase = _Class("VNClustererContextBase")
VNClustererReadWriteContext = _Class("VNClustererReadWriteContext")
VNClustererReadOnlyContext = _Class("VNClustererReadOnlyContext")
BurstActionClassifier = _Class("BurstActionClassifier")
BurstImageFaceAnalysisContext = _Class("BurstImageFaceAnalysisContext")
BurstFaceInfo = _Class("BurstFaceInfo")
BurstFaceScoreEntry = _Class("BurstFaceScoreEntry")
BurstFaceConfigEntry = _Class("BurstFaceConfigEntry")
VNGreedyClusteringReadOnly = _Class("VNGreedyClusteringReadOnly")
VNGreedyClusteringReadWrite = _Class("VNGreedyClusteringReadWrite")
VNClusteringLogger = _Class("VNClusteringLogger")
VNSuggestionsLogger = _Class("VNSuggestionsLogger")
CVML_Error = _Class("CVML_Error")
VNRequest = _Class("VNRequest")
VNAlignFaceRectangleRequest = _Class("VNAlignFaceRectangleRequest")
VNGroupImagesByTimeAndContentRequest = _Class("VNGroupImagesByTimeAndContentRequest")
VNCompoundRequest = _Class("VNCompoundRequest")
VNANFDDetectorCompoundRequest = _Class("VNANFDDetectorCompoundRequest")
VNUniqueObservationClassCompoundRequest = _Class(
    "VNUniqueObservationClassCompoundRequest"
)
VNHomologousObservationClassCompoundRequest = _Class(
    "VNHomologousObservationClassCompoundRequest"
)
VNFaceAnalyzerCompoundRequest = _Class("VNFaceAnalyzerCompoundRequest")
VNImageAnalyzerCompoundRequest = _Class("VNImageAnalyzerCompoundRequest")
VNImageBasedRequest = _Class("VNImageBasedRequest")
VNDetectHorizonRequest = _Class("VNDetectHorizonRequest")
VNGenerateObjectnessBasedSaliencyImageRequest = _Class(
    "VNGenerateObjectnessBasedSaliencyImageRequest"
)
VNImageExposureScoreRequest = _Class("VNImageExposureScoreRequest")
VNCreateFaceprintRequest = _Class("VNCreateFaceprintRequest")
VNCreateFaceTorsoprintRequest = _Class("VNCreateFaceTorsoprintRequest")
VNDetectFaceExpressionsRequest = _Class("VNDetectFaceExpressionsRequest")
VNCoreMLRequest = _Class("VNCoreMLRequest")
VNIdentifyJunkRequest = _Class("VNIdentifyJunkRequest")
VNCreateSceneprintRequest = _Class("VNCreateSceneprintRequest")
VNDetectRectanglesRequest = _Class("VNDetectRectanglesRequest")
VNRecognizeTextRequest = _Class("VNRecognizeTextRequest")
VNCreateFaceRegionMapRequest = _Class("VNCreateFaceRegionMapRequest")
VNDetectContoursRequest = _Class("VNDetectContoursRequest")
VNCreateSmartCamprintRequest = _Class("VNCreateSmartCamprintRequest")
VNDetectFaceCaptureQualityRequest = _Class("VNDetectFaceCaptureQualityRequest")
VNDetectFaceRectanglesRequest = _Class("VNDetectFaceRectanglesRequest")
VNRecognizeFoodAndDrinkRequest = _Class("VNRecognizeFoodAndDrinkRequest")
VNGenerateFaceSegmentsRequest = _Class("VNGenerateFaceSegmentsRequest")
VNDetectHumanBodyPoseRequest = _Class("VNDetectHumanBodyPoseRequest")
VNCreateImageprintRequest = _Class("VNCreateImageprintRequest")
VNImageBlurScoreRequest = _Class("VNImageBlurScoreRequest")
VN6Mb1ME89lyW3HpahkEygIG = _Class("VN6Mb1ME89lyW3HpahkEygIG")
VNDetectFace3DLandmarksRequest = _Class("VNDetectFace3DLandmarksRequest")
VNDetectHumanRectanglesRequest = _Class("VNDetectHumanRectanglesRequest")
VNClassifyFaceAttributesRequest = _Class("VNClassifyFaceAttributesRequest")
VNRecognizeAnimalsRequest = _Class("VNRecognizeAnimalsRequest")
VNGenerateImageSaliencyRequest = _Class("VNGenerateImageSaliencyRequest")
VNDetectFacePoseRequest = _Class("VNDetectFacePoseRequest")
VNDetectFaceLandmarksRequest = _Class("VNDetectFaceLandmarksRequest")
VNNOPRequest = _Class("VNNOPRequest")
VNDetectHumanHandPoseRequest = _Class("VNDetectHumanHandPoseRequest")
VNGenerateImageFeaturePrintRequest = _Class("VNGenerateImageFeaturePrintRequest")
VNDetectBarcodesRequest = _Class("VNDetectBarcodesRequest")
VNCreateDetectionprintRequest = _Class("VNCreateDetectionprintRequest")
VNClassifyImageRequest = _Class("VNClassifyImageRequest")
VNDetectTextRectanglesRequest = _Class("VNDetectTextRectanglesRequest")
VNRecognizeObjectsRequest = _Class("VNRecognizeObjectsRequest")
VNClassifyImageAestheticsRequest = _Class("VNClassifyImageAestheticsRequest")
VNVYvzEtX1JlUdu8xx5qhDI = _Class("VNVYvzEtX1JlUdu8xx5qhDI")
VNGenerateAttentionBasedSaliencyImageRequest = _Class(
    "VNGenerateAttentionBasedSaliencyImageRequest"
)
VN5kJNH3eYuyaLxNpZr5Z7zi = _Class("VN5kJNH3eYuyaLxNpZr5Z7zi")
VNCreateTorsoprintRequest = _Class("VNCreateTorsoprintRequest")
VNClassifyPotentialLandmarkRequest = _Class("VNClassifyPotentialLandmarkRequest")
VNStatefulRequest = _Class("VNStatefulRequest")
VNDetectTrajectoriesRequest = _Class("VNDetectTrajectoriesRequest")
VNTrackingRequest = _Class("VNTrackingRequest")
VNTrackRectangleRequest = _Class("VNTrackRectangleRequest")
VNTrackObjectRequest = _Class("VNTrackObjectRequest")
VNTrackLegacyFaceCoreObjectRequest = _Class("VNTrackLegacyFaceCoreObjectRequest")
VNSceneClassificationRequest = _Class("VNSceneClassificationRequest")
VNClassifyJunkImageRequest = _Class("VNClassifyJunkImageRequest")
VNTargetedImageRequest = _Class("VNTargetedImageRequest")
VNGenerateOpticalFlowRequest = _Class("VNGenerateOpticalFlowRequest")
VNImageRegistrationRequest = _Class("VNImageRegistrationRequest")
VNTranslationalImageRegistrationRequest = _Class(
    "VNTranslationalImageRegistrationRequest"
)
VNHomographicImageRegistrationRequest = _Class("VNHomographicImageRegistrationRequest")
VNAppendBurstSequenceFrameRequest = _Class("VNAppendBurstSequenceFrameRequest")
VNDetectHumanHeadRectanglesRequest = _Class("VNDetectHumanHeadRectanglesRequest")
VNDetector = _Class("VNDetector")
VNImageprintGenerator = _Class("VNImageprintGenerator")
VNFaceBBoxAligner = _Class("VNFaceBBoxAligner")
VNImageAnalyzerMultiDetector = _Class("VNImageAnalyzerMultiDetector")
VNOpticalFlowGenerator = _Class("VNOpticalFlowGenerator")
VNCoreMLTransformer = _Class("VNCoreMLTransformer")
VNRectangleDetector = _Class("VNRectangleDetector")
VNJunkIdentifier = _Class("VNJunkIdentifier")
VNContoursDetector = _Class("VNContoursDetector")
VNHorizonDetector = _Class("VNHorizonDetector")
VNFaceRegionMapGenerator = _Class("VNFaceRegionMapGenerator")
VNFaceGeometryEstimator = _Class("VNFaceGeometryEstimator")
VNHumanPoseDetector = _Class("VNHumanPoseDetector")
VNHumanHandPoseDetector = _Class("VNHumanHandPoseDetector")
VNHumanBodyPoseDetector = _Class("VNHumanBodyPoseDetector")
VNFaceExpressionDetector = _Class("VNFaceExpressionDetector")
VNFaceprintGenerator = _Class("VNFaceprintGenerator")
VNFaceprintGeneratorRevision1 = _Class("VNFaceprintGeneratorRevision1")
VNFaceDetector = _Class("VNFaceDetector")
VNFaceDetectorPrivateRevisionLegacyFaceCore = _Class(
    "VNFaceDetectorPrivateRevisionLegacyFaceCore"
)
VNFaceDetectorRevision1 = _Class("VNFaceDetectorRevision1")
VNFaceDetectorRevision2 = _Class("VNFaceDetectorRevision2")
VNEspressoModelClassifier = _Class("VNEspressoModelClassifier")
VNSmartCamClassifier = _Class("VNSmartCamClassifier")
VNSceneClassifier = _Class("VNSceneClassifier")
VNEspressoModelFileBasedDetector = _Class("VNEspressoModelFileBasedDetector")
VNDetectionprintGenerator = _Class("VNDetectionprintGenerator")
VNGenerateObjectnessBasedSaliencyDetector = _Class(
    "VNGenerateObjectnessBasedSaliencyDetector"
)
VNGenerateObjectnessBasedSaliency544x544Detector = _Class(
    "VNGenerateObjectnessBasedSaliency544x544Detector"
)
VNSmartCamCombinedAestheticsAndSaliencyDetector = _Class(
    "VNSmartCamCombinedAestheticsAndSaliencyDetector"
)
VNTorsoprintGenerator = _Class("VNTorsoprintGenerator")
VNANFDMultiDetector = _Class("VNANFDMultiDetector")
VNANFDMultiDetectorANFDv2 = _Class("VNANFDMultiDetectorANFDv2")
VNANFDMultiDetectorANODv3 = _Class("VNANFDMultiDetectorANODv3")
VNSingleHeadSceneprintGenerator = _Class("VNSingleHeadSceneprintGenerator")
VNFaceSegmentGenerator = _Class("VNFaceSegmentGenerator")
VNFaceLandmarkDetector = _Class("VNFaceLandmarkDetector")
VNFaceLandmarkDetectorDNN = _Class("VNFaceLandmarkDetectorDNN")
VNFaceLandmarkDetectorRevision2 = _Class("VNFaceLandmarkDetectorRevision2")
VNFaceLandmarkDetectorRevision3 = _Class("VNFaceLandmarkDetectorRevision3")
VNFaceLandmarkDetectorRevision1 = _Class("VNFaceLandmarkDetectorRevision1")
VNFaceAnalyzerMultiDetectorBase = _Class("VNFaceAnalyzerMultiDetectorBase")
VNHomeAppFaceAnalyzerMultiDetector = _Class("VNHomeAppFaceAnalyzerMultiDetector")
VNFaceAnalyzerMultiDetector = _Class("VNFaceAnalyzerMultiDetector")
VNFaceAnalyzerMultiDetectorFPrev2FArev1 = _Class(
    "VNFaceAnalyzerMultiDetectorFPrev2FArev1"
)
VNFaceAnalyzerMultiDetectorFPrev3FArev2 = _Class(
    "VNFaceAnalyzerMultiDetectorFPrev3FArev2"
)
VNFaceQualityGenerator = _Class("VNFaceQualityGenerator")
VNSaliencyHeatmapBoundingBoxGenerator = _Class("VNSaliencyHeatmapBoundingBoxGenerator")
VNSaliencyOHeatmapBoundingBoxGenerator = _Class(
    "VNSaliencyOHeatmapBoundingBoxGenerator"
)
VNSaliencyAHeatmapBoundingBoxGenerator = _Class(
    "VNSaliencyAHeatmapBoundingBoxGenerator"
)
VNRecognizedPointsSpecifier = _Class("VNRecognizedPointsSpecifier")
VNRecognizedHandPointsSpecifier = _Class("VNRecognizedHandPointsSpecifier")
VNRecognizedBodyPointsSpecifier = _Class("VNRecognizedBodyPointsSpecifier")
FaceCoreExceptionUtils = _Class("FaceCoreExceptionUtils")
FaceCoreImage = _Class("FaceCoreImage")
FaceCoreDetector = _Class("FaceCoreDetector")
FaceCoreLandmark = _Class("FaceCoreLandmark")
FaceCoreFace = _Class("FaceCoreFace")
