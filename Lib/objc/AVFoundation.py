"""
Classes from the 'AVFoundation' framework.
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


AVAudioEngine = _Class("AVAudioEngine")
AVVoiceTriggerClient = _Class("AVVoiceTriggerClient")
AVVoiceTriggerNotificationForwarder = _Class("AVVoiceTriggerNotificationForwarder")
AVAudioTime = _Class("AVAudioTime")
AVMusicTrack = _Class("AVMusicTrack")
AVAudioSequencer = _Class("AVAudioSequencer")
AVAudioMixingDestination = _Class("AVAudioMixingDestination")
AVAudioFile = _Class("AVAudioFile")
AVVCSessionManager = _Class("AVVCSessionManager")
AVAudioEnvironmentReverbParameters = _Class("AVAudioEnvironmentReverbParameters")
AVAudioEnvironmentDistanceAttenuationParameters = _Class(
    "AVAudioEnvironmentDistanceAttenuationParameters"
)
AVVCAudioBuffer = _Class("AVVCAudioBuffer")
AVSpeechSynthesisMarker = _Class("AVSpeechSynthesisMarker")
AVSpeechSynthesizer = _Class("AVSpeechSynthesizer")
AVSpeechUtterance = _Class("AVSpeechUtterance")
AVSpeechSynthesisVoice = _Class("AVSpeechSynthesisVoice")
AVAudioDeviceTestProcessingChain = _Class("AVAudioDeviceTestProcessingChain")
AVAudioDeviceTestSequence = _Class("AVAudioDeviceTestSequence")
AVAudioDeviceTestResult = _Class("AVAudioDeviceTestResult")
AVAudioFormat = _Class("AVAudioFormat")
AVAudioUnitEQFilterParameters = _Class("AVAudioUnitEQFilterParameters")
AVAudioBuffer = _Class("AVAudioBuffer")
AVAudioCompressedBuffer = _Class("AVAudioCompressedBuffer")
AVAudioPCMBuffer = _Class("AVAudioPCMBuffer")
AVMIDIPlayer = _Class("AVMIDIPlayer")
AVAudioClock = _Class("AVAudioClock")
AVVCMetricsManager = _Class("AVVCMetricsManager")
AVAudioConverter = _Class("AVAudioConverter")
AVAudioDeviceTest = _Class("AVAudioDeviceTest")
AVSpeechSynthesisProviderRequest = _Class("AVSpeechSynthesisProviderRequest")
AVSpeechSynthesisProviderVoice = _Class("AVSpeechSynthesisProviderVoice")
AVAudioChannelLayout = _Class("AVAudioChannelLayout")
AVAudioRecorder = _Class("AVAudioRecorder")
AVAudioPlayer = _Class("AVAudioPlayer")
AudioPlayerImpl = _Class("AudioPlayerImpl")
VoiceVerificationEndpointer = _Class("VoiceVerificationEndpointer")
AVAudioUnitComponentManager = _Class("AVAudioUnitComponentManager")
SpeexEndpointer = _Class("SpeexEndpointer")
AVAudioUnitComponent = _Class("AVAudioUnitComponent")
AVVCAlertInformation = _Class("AVVCAlertInformation")
AVVCStartRecordSettings = _Class("AVVCStartRecordSettings")
AVVCConfigureAlertBehaviorSettings = _Class("AVVCConfigureAlertBehaviorSettings")
AVVCPrepareRecordSettings = _Class("AVVCPrepareRecordSettings")
AVVCContextSettings = _Class("AVVCContextSettings")
AVVoiceController = _Class("AVVoiceController")
AVVCRecordDeviceInfo = _Class("AVVCRecordDeviceInfo")
AVVCRemoteInputHost = _Class("AVVCRemoteInputHost")
AVAudioConnectionPoint = _Class("AVAudioConnectionPoint")
AVAudioNode = _Class("AVAudioNode")
AVAudioPlayerNode = _Class("AVAudioPlayerNode")
AVAudioEnvironmentNode = _Class("AVAudioEnvironmentNode")
AVAudioSourceNode = _Class("AVAudioSourceNode")
AVAudioMixerNode = _Class("AVAudioMixerNode")
AVAudioSinkNode = _Class("AVAudioSinkNode")
AVAudioUnit = _Class("AVAudioUnit")
AVAudioUnitDSPGraph = _Class("AVAudioUnitDSPGraph")
AVAudioUnitSplitter = _Class("AVAudioUnitSplitter")
AVAudioUnitMIDIInstrument = _Class("AVAudioUnitMIDIInstrument")
AVAudioUnitSampler = _Class("AVAudioUnitSampler")
AVAudioUnitGenerator = _Class("AVAudioUnitGenerator")
AVAudioUnitEffect = _Class("AVAudioUnitEffect")
AVAudioUnitEQ = _Class("AVAudioUnitEQ")
AVAudioUnitDistortion = _Class("AVAudioUnitDistortion")
AVAudioUnitReverb = _Class("AVAudioUnitReverb")
AVAudioUnitDelay = _Class("AVAudioUnitDelay")
AVAudioUnitTimeEffect = _Class("AVAudioUnitTimeEffect")
AVAudioUnitTimePitch = _Class("AVAudioUnitTimePitch")
AVAudioUnitVarispeed = _Class("AVAudioUnitVarispeed")
AVAudioIONode = _Class("AVAudioIONode")
AVAudioInputNode = _Class("AVAudioInputNode")
AVAudioOutputNode = _Class("AVAudioOutputNode")
AVSpeechSynthesisProviderAudioUnit = _Class("AVSpeechSynthesisProviderAudioUnit")
AVStreamDataParserInternal = _Class("AVStreamDataParserInternal")
AVRouteDetector = _Class("AVRouteDetector")
AVRouteDetectorInternal = _Class("AVRouteDetectorInternal")
AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl = _Class(
    "AVFigEndpointUIAgentOutputDeviceAuthorizationRequestImpl"
)
AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl = _Class(
    "AVFigEndpointUIAgentOutputDeviceAuthorizationSessionImpl"
)
AVContentKeyReportGroup = _Class("AVContentKeyReportGroup")
AVContentKeySession = _Class("AVContentKeySession")
AVContentKeySessionInternal = _Class("AVContentKeySessionInternal")
AVContentKeyResponseInternal = _Class("AVContentKeyResponseInternal")
AVContentKeyResponse = _Class("AVContentKeyResponse")
AVContentKeyResponseAuthorizationToken = _Class(
    "AVContentKeyResponseAuthorizationToken"
)
AVContentKeyResponseClearKey = _Class("AVContentKeyResponseClearKey")
AVContentKeyResponseFairPlayStreaming = _Class("AVContentKeyResponseFairPlayStreaming")
AVContentKeyRequest = _Class("AVContentKeyRequest")
AVPersistableContentKeyRequest = _Class("AVPersistableContentKeyRequest")
AVContentKeyRequestInternal = _Class("AVContentKeyRequestInternal")
AVHUDStringGenerator = _Class("AVHUDStringGenerator")
AVMutableMovieInternal = _Class("AVMutableMovieInternal")
AVMovieInternal = _Class("AVMovieInternal")
AVMediaDataStorage = _Class("AVMediaDataStorage")
AVMediaDataStorageInternal = _Class("AVMediaDataStorageInternal")
AVFigEndpointUIAgentOutputContextManagerImpl = _Class(
    "AVFigEndpointUIAgentOutputContextManagerImpl"
)
AVFigCommChannelUUIDOutputContextCommunicationChannelImpl = _Class(
    "AVFigCommChannelUUIDOutputContextCommunicationChannelImpl"
)
AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator = _Class(
    "AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator"
)
AVFigEndpointFigRoutingContextOutputDeviceTranslator = _Class(
    "AVFigEndpointFigRoutingContextOutputDeviceTranslator"
)
AVFigCommChannelUUIDCommunicationChannelManager = _Class(
    "AVFigCommChannelUUIDCommunicationChannelManager"
)
AVFigRoutingContextOutputContextImpl = _Class("AVFigRoutingContextOutputContextImpl")
AVVideoCompositionRenderContext = _Class("AVVideoCompositionRenderContext")
AVVideoCompositionRenderContextInternal = _Class(
    "AVVideoCompositionRenderContextInternal"
)
AVKeyPathFlattenerKVOIntrospectionShim = _Class(
    "AVKeyPathFlattenerKVOIntrospectionShim"
)
AVKeyPathFlattener = _Class("AVKeyPathFlattener")
AVTwoPartKeyPath = _Class("AVTwoPartKeyPath")
AVKeyPathDependency = _Class("AVKeyPathDependency")
AVKeyPathDependencyManager = _Class("AVKeyPathDependencyManager")
AVWeakObservableCallbackCancellationHelper = _Class(
    "AVWeakObservableCallbackCancellationHelper"
)
AVWeaklyObservedObjectClientBlockKVONotifier = _Class(
    "AVWeaklyObservedObjectClientBlockKVONotifier"
)
AVClientBlockKVONotifier = _Class("AVClientBlockKVONotifier")
AVWeakObservationBlockFactory = _Class("AVWeakObservationBlockFactory")
AVObservationBlockFactory = _Class("AVObservationBlockFactory")
AVKVODispatcher = _Class("AVKVODispatcher")
AVAsynchronousVideoCompositionRequest = _Class("AVAsynchronousVideoCompositionRequest")
AVAsynchronousVideoCompositionRequestInternal = _Class(
    "AVAsynchronousVideoCompositionRequestInternal"
)
AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl = _Class(
    "AVFigEndpointOutputDeviceDiscoverySessionAvailableOutputDevicesImpl"
)
AVCustomVideoCompositorSession = _Class("AVCustomVideoCompositorSession")
AVExternalDevice = _Class("AVExternalDevice")
AVExternalDeviceTurnByTurnToken = _Class("AVExternalDeviceTurnByTurnToken")
AVExternalDeviceScreenBorrowToken = _Class("AVExternalDeviceScreenBorrowToken")
AVExternalDeviceInternal = _Class("AVExternalDeviceInternal")
AVExternalDeviceIcon = _Class("AVExternalDeviceIcon")
AVExternalDeviceIconInternal = _Class("AVExternalDeviceIconInternal")
AVExternalDeviceHID = _Class("AVExternalDeviceHID")
AVExternalDeviceHIDInternal = _Class("AVExternalDeviceHIDInternal")
AVMediaSelection = _Class("AVMediaSelection")
AVMutableMediaSelection = _Class("AVMutableMediaSelection")
AVMediaSelectionInternal = _Class("AVMediaSelectionInternal")
AVIOKitOutputSettingsAssistantVideoEncoderCapabilities = _Class(
    "AVIOKitOutputSettingsAssistantVideoEncoderCapabilities"
)
AVExportSettingsOutputSettingsAssistantVideoSettingsAdjuster = _Class(
    "AVExportSettingsOutputSettingsAssistantVideoSettingsAdjuster"
)
AVExportSettingsOutputSettingsAssistantBaseSettings = _Class(
    "AVExportSettingsOutputSettingsAssistantBaseSettings"
)
AVOutputSettingsAssistant = _Class("AVOutputSettingsAssistant")
AVOutputSettingsAssistantInternal = _Class("AVOutputSettingsAssistantInternal")
AVCoreImageFilterCustomVideoCompositor = _Class(
    "AVCoreImageFilterCustomVideoCompositor"
)
AVCoreImageFilterVideoCompositionInstruction = _Class(
    "AVCoreImageFilterVideoCompositionInstruction"
)
AVAsynchronousCIImageFilteringRequest = _Class("AVAsynchronousCIImageFilteringRequest")
AVAsynchronousCIImageFilteringRequestInternal = _Class(
    "AVAsynchronousCIImageFilteringRequestInternal"
)
AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl = _Class(
    "AVFigRouteDescriptorOutputDeviceDiscoverySessionAvailableOutputDevicesImpl"
)
AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl = _Class(
    "AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl"
)
AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory = _Class(
    "AVFigRouteDiscovererOutputDeviceDiscoverySessionFactory"
)
AVPlayerItemLegibleOutputInternal = _Class("AVPlayerItemLegibleOutputInternal")
AVPlayerItemLegibleOutputRealDependencyFactory = _Class(
    "AVPlayerItemLegibleOutputRealDependencyFactory"
)
AVPlayerMediaSelectionCriteria = _Class("AVPlayerMediaSelectionCriteria")
AVTextStyleRule = _Class("AVTextStyleRule")
AVTextStyleRuleInternal = _Class("AVTextStyleRuleInternal")
AVRemoteFigSampleBufferRenderSynchronizerFactory = _Class(
    "AVRemoteFigSampleBufferRenderSynchronizerFactory"
)
AVSampleBufferRenderSynchronizerInternal = _Class(
    "AVSampleBufferRenderSynchronizerInternal"
)
AVAssetResourceLoadingRequestor = _Class("AVAssetResourceLoadingRequestor")
AVAssetResourceLoadingRequestorInternal = _Class(
    "AVAssetResourceLoadingRequestorInternal"
)
AVAssetResourceLoadingRequest = _Class("AVAssetResourceLoadingRequest")
AVAssetResourceRenewalRequest = _Class("AVAssetResourceRenewalRequest")
AVAssetResourceLoadingRequestInternal = _Class("AVAssetResourceLoadingRequestInternal")
AVAssetResourceLoadingDataRequest = _Class("AVAssetResourceLoadingDataRequest")
AVAssetResourceLoadingDataRequestInternal = _Class(
    "AVAssetResourceLoadingDataRequestInternal"
)
AVAssetResourceLoadingContentInformationRequest = _Class(
    "AVAssetResourceLoadingContentInformationRequest"
)
AVAssetResourceLoadingContentInformationRequestInternal = _Class(
    "AVAssetResourceLoadingContentInformationRequestInternal"
)
AVAssetResourceLoader = _Class("AVAssetResourceLoader")
AVAssetResourceLoaderInternal = _Class("AVAssetResourceLoaderInternal")
AVAssetResourceLoaderRemoteHandlerContext = _Class(
    "AVAssetResourceLoaderRemoteHandlerContext"
)
AVPixelBufferAttributeMediator = _Class("AVPixelBufferAttributeMediator")
AVSampleBufferDisplayLayerInternal = _Class("AVSampleBufferDisplayLayerInternal")
AVAPSyncControllerOutputDeviceImpl = _Class("AVAPSyncControllerOutputDeviceImpl")
AVPlayerItemVideoOutputInternal = _Class("AVPlayerItemVideoOutputInternal")
AVPlayerItemOutputInternal = _Class("AVPlayerItemOutputInternal")
AVAssetDownloadSession = _Class("AVAssetDownloadSession")
AVAssetDownloadSessionInternal = _Class("AVAssetDownloadSessionInternal")
AVFloat64Range = _Class("AVFloat64Range")
AVAudioSettingsValueConstrainer = _Class("AVAudioSettingsValueConstrainer")
AVAssetSegmentReport = _Class("AVAssetSegmentReport")
AVAssetSegmentTrackReport = _Class("AVAssetSegmentTrackReport")
AVAssetSegmentReportSampleInformation = _Class("AVAssetSegmentReportSampleInformation")
AVMediaFileOutputSettingsValidator = _Class("AVMediaFileOutputSettingsValidator")
AVGenericMediaFileOutputSettingsValidator = _Class(
    "AVGenericMediaFileOutputSettingsValidator"
)
AVISOOutputSettingsValidator = _Class("AVISOOutputSettingsValidator")
AVAIFCOutputSettingsValidator = _Class("AVAIFCOutputSettingsValidator")
AVAIFFOutputSettingsValidator = _Class("AVAIFFOutputSettingsValidator")
AVWAVEOutputSettingsValidator = _Class("AVWAVEOutputSettingsValidator")
AVMediaFileType = _Class("AVMediaFileType")
AVDisplayCriteria = _Class("AVDisplayCriteria")
AVDisplayCriteriaInternal = _Class("AVDisplayCriteriaInternal")
AVFormatSpecification = _Class("AVFormatSpecification")
AVOutputSettings = _Class("AVOutputSettings")
AVVideoOutputSettings = _Class("AVVideoOutputSettings")
AVAVVideoSettingsVideoOutputSettings = _Class("AVAVVideoSettingsVideoOutputSettings")
AVPixelBufferAttributesVideoOutputSettings = _Class(
    "AVPixelBufferAttributesVideoOutputSettings"
)
AVAudioOutputSettings = _Class("AVAudioOutputSettings")
AVAVAudioSettingsAudioOutputSettings = _Class("AVAVAudioSettingsAudioOutputSettings")
AVMediaSelectionOptionInternal = _Class("AVMediaSelectionOptionInternal")
AVMediaSelectionGroupInternal = _Class("AVMediaSelectionGroupInternal")
AVAudioSessionMediaPlayerOnly = _Class("AVAudioSessionMediaPlayerOnly")
AVAudioSessionMediaPlayerOnlyInternal = _Class("AVAudioSessionMediaPlayerOnlyInternal")
AVPlayerItemErrorLogEvent = _Class("AVPlayerItemErrorLogEvent")
AVPlayerItemErrorLogEventInternal = _Class("AVPlayerItemErrorLogEventInternal")
AVPlayerItemErrorLog = _Class("AVPlayerItemErrorLog")
AVPlayerItemErrorLogInternal = _Class("AVPlayerItemErrorLogInternal")
AVPlayerItemAccessLogEvent = _Class("AVPlayerItemAccessLogEvent")
AVPlayerItemAccessLogEventInternal = _Class("AVPlayerItemAccessLogEventInternal")
AVPlayerItemAccessLog = _Class("AVPlayerItemAccessLog")
AVPlayerItemAccessLogInternal = _Class("AVPlayerItemAccessLogInternal")
AVAssetDownloadCacheInternal = _Class("AVAssetDownloadCacheInternal")
AVManagedAssetCacheInternal = _Class("AVManagedAssetCacheInternal")
AVAssetCache = _Class("AVAssetCache")
AVAssetDownloadCache = _Class("AVAssetDownloadCache")
AVManagedAssetCache = _Class("AVManagedAssetCache")
AVDateRangeMetadataGroupInternal = _Class("AVDateRangeMetadataGroupInternal")
AVTimedMetadataGroupInternal = _Class("AVTimedMetadataGroupInternal")
AVMetadataGroup = _Class("AVMetadataGroup")
AVDateRangeMetadataGroup = _Class("AVDateRangeMetadataGroup")
AVMutableDateRangeMetadataGroup = _Class("AVMutableDateRangeMetadataGroup")
AVTimedMetadataGroup = _Class("AVTimedMetadataGroup")
AVMutableTimedMetadataGroup = _Class("AVMutableTimedMetadataGroup")
AVDispatchOnce = _Class("AVDispatchOnce")
AVEventWaiter = _Class("AVEventWaiter")
AVAPSyncOutputDeviceCommunicationChannelImpl = _Class(
    "AVAPSyncOutputDeviceCommunicationChannelImpl"
)
AVAPSyncOutputDeviceCommunicationChannelManager = _Class(
    "AVAPSyncOutputDeviceCommunicationChannelManager"
)
AVAssetTrackGroup = _Class("AVAssetTrackGroup")
AVAssetTrackGroupInternal = _Class("AVAssetTrackGroupInternal")
AVPlayerItemMediaDataCollectorInternal = _Class(
    "AVPlayerItemMediaDataCollectorInternal"
)
AVCMNotificationDispatcherListenerKey = _Class("AVCMNotificationDispatcherListenerKey")
AVCMNotificationDispatcher = _Class("AVCMNotificationDispatcher")
AVAPSyncControllerRemoteOutputDeviceGroupImpl = _Class(
    "AVAPSyncControllerRemoteOutputDeviceGroupImpl"
)
AVCallbackContextRegistry = _Class("AVCallbackContextRegistry")
AVFigRoutingContextCommandOutputDeviceConfiguration = _Class(
    "AVFigRoutingContextCommandOutputDeviceConfiguration"
)
AVFigRoutingContextCommandOutputDeviceConfigurationModification = _Class(
    "AVFigRoutingContextCommandOutputDeviceConfigurationModification"
)
AVWeakReference = _Class("AVWeakReference")
AVRetainReleaseWeakReference = _Class("AVRetainReleaseWeakReference")
AVResult = _Class("AVResult")
AVAssetInspectorLoader = _Class("AVAssetInspectorLoader")
AVUnreachableAssetInspectorLoader = _Class("AVUnreachableAssetInspectorLoader")
AVFigAssetInspectorLoader = _Class("AVFigAssetInspectorLoader")
AVAssetMakeReadyForInspectionLoader = _Class("AVAssetMakeReadyForInspectionLoader")
AVPlaybackItemInspectorLoader = _Class("AVPlaybackItemInspectorLoader")
AVAssetSynchronousInspectorLoader = _Class("AVAssetSynchronousInspectorLoader")
AVDepartureAnnouncingObjectMonitor = _Class("AVDepartureAnnouncingObjectMonitor")
AVGlobalOperationQueue = _Class("AVGlobalOperationQueue")
AVWeakReferencingDelegateStorage = _Class("AVWeakReferencingDelegateStorage")
AVScheduledAudioParameters = _Class("AVScheduledAudioParameters")
AVMutableScheduledAudioParameters = _Class("AVMutableScheduledAudioParameters")
AVScheduledAudioParametersInternal = _Class("AVScheduledAudioParametersInternal")
AVVideoPerformanceMetrics = _Class("AVVideoPerformanceMetrics")
AVVideoPerformanceMetricsInternal = _Class("AVVideoPerformanceMetricsInternal")
AVMutableMovieTrackInternal = _Class("AVMutableMovieTrackInternal")
AVMovieTrackInternal = _Class("AVMovieTrackInternal")
AVSystemRemotePoolOutputDeviceCommunicationChannelImpl = _Class(
    "AVSystemRemotePoolOutputDeviceCommunicationChannelImpl"
)
AVSystemRemotePoolOutputDeviceCommunicationChannelManager = _Class(
    "AVSystemRemotePoolOutputDeviceCommunicationChannelManager"
)
AVOutputContextManager = _Class("AVOutputContextManager")
AVOutputContextManagerInternal = _Class("AVOutputContextManagerInternal")
AVOutputContextDestinationChange = _Class("AVOutputContextDestinationChange")
AVOutputContextDestinationChangeInternal = _Class(
    "AVOutputContextDestinationChangeInternal"
)
AVOutputContextCommunicationChannel = _Class("AVOutputContextCommunicationChannel")
AVOutputContextCommunicationChannelInternal = _Class(
    "AVOutputContextCommunicationChannelInternal"
)
AVOutputContext = _Class("AVOutputContext")
AVOutputContextInternal = _Class("AVOutputContextInternal")
AVRunLoopConditionRunLoopState = _Class("AVRunLoopConditionRunLoopState")
AVAudioMixInputParametersInternal = _Class("AVAudioMixInputParametersInternal")
AVAudioMixInputParameters = _Class("AVAudioMixInputParameters")
AVMutableAudioMixInputParameters = _Class("AVMutableAudioMixInputParameters")
AVAudioMixInternal = _Class("AVAudioMixInternal")
AVAudioMix = _Class("AVAudioMix")
AVMutableAudioMix = _Class("AVMutableAudioMix")
AVAssetCustomURLAuthentication = _Class("AVAssetCustomURLAuthentication")
AVAssetCustomURLBridgeForNSURLProtocol = _Class(
    "AVAssetCustomURLBridgeForNSURLProtocol"
)
AVAssetCustomURLBridgeForNSURLSession = _Class("AVAssetCustomURLBridgeForNSURLSession")
AVAssetCustomURLRequest = _Class("AVAssetCustomURLRequest")
AVNSURLProtocolRequest = _Class("AVNSURLProtocolRequest")
AVFigEndpointSecondDisplayModeToken = _Class("AVFigEndpointSecondDisplayModeToken")
AVFigEndpointOutputDeviceImpl = _Class("AVFigEndpointOutputDeviceImpl")
AVFigRouteDescriptorOutputDeviceImpl = _Class("AVFigRouteDescriptorOutputDeviceImpl")
AVClusterComponentOutputDeviceDescription = _Class(
    "AVClusterComponentOutputDeviceDescription"
)
AVOutputDeviceCommunicationChannel = _Class("AVOutputDeviceCommunicationChannel")
AVLocalOutputDeviceImpl = _Class("AVLocalOutputDeviceImpl")
AVPairedDevice = _Class("AVPairedDevice")
AVPairedDeviceInternal = _Class("AVPairedDeviceInternal")
AVOutputDeviceAuthorizedPeer = _Class("AVOutputDeviceAuthorizedPeer")
AVOutputDeviceAuthorizedPeerInternal = _Class("AVOutputDeviceAuthorizedPeerInternal")
AVOutputDeviceLegacyFrecentsWriter = _Class("AVOutputDeviceLegacyFrecentsWriter")
AVOutputDeviceLegacyFrecentsReader = _Class("AVOutputDeviceLegacyFrecentsReader")
AVOutputDeviceFrecentsWriter = _Class("AVOutputDeviceFrecentsWriter")
AVOutputDeviceFrecentsReader = _Class("AVOutputDeviceFrecentsReader")
AVOutputDeviceFrecencyManager = _Class("AVOutputDeviceFrecencyManager")
AVOutputDevice = _Class("AVOutputDevice")
AVOutputDeviceInternal = _Class("AVOutputDeviceInternal")
AVMediaDataRequester = _Class("AVMediaDataRequester")
AVSerializedMostlySynchronousReentrantBlockScheduler = _Class(
    "AVSerializedMostlySynchronousReentrantBlockScheduler"
)
AVSynchronousBlockScheduler = _Class("AVSynchronousBlockScheduler")
AVFragmentedMovieTrackInternal = _Class("AVFragmentedMovieTrackInternal")
AVExecutionEnvironment = _Class("AVExecutionEnvironment")
AVSampleBufferVideoOutput = _Class("AVSampleBufferVideoOutput")
AVSampleBufferVideoOutputInternal = _Class("AVSampleBufferVideoOutputInternal")
AVExternalPlaybackMonitor = _Class("AVExternalPlaybackMonitor")
AVExternalPlaybackMonitorInternal = _Class("AVExternalPlaybackMonitorInternal")
AVTimeFormatterInternal = _Class("AVTimeFormatterInternal")
AVOutputDeviceAuthorizationRequest = _Class("AVOutputDeviceAuthorizationRequest")
AVOutputDeviceAuthorizationRequestInternal = _Class(
    "AVOutputDeviceAuthorizationRequestInternal"
)
AVOutputDeviceAuthorizationSession = _Class("AVOutputDeviceAuthorizationSession")
AVOutputDeviceAuthorizationSessionInternal = _Class(
    "AVOutputDeviceAuthorizationSessionInternal"
)
AVVideoCompositionRenderHint = _Class("AVVideoCompositionRenderHint")
AVVideoCompositionRenderHintInternal = _Class("AVVideoCompositionRenderHintInternal")
AVPlayerItemOutput = _Class("AVPlayerItemOutput")
AVPlayerItemLegibleOutput = _Class("AVPlayerItemLegibleOutput")
AVPlayerItemVideoOutput = _Class("AVPlayerItemVideoOutput")
AVPlayerItemMetadataOutput = _Class("AVPlayerItemMetadataOutput")
AVPlayerItemMetadataOutputInternal = _Class("AVPlayerItemMetadataOutputInternal")
AVOutputDeviceGroupMembershipChangeResult = _Class(
    "AVOutputDeviceGroupMembershipChangeResult"
)
AVOutputDeviceGroup = _Class("AVOutputDeviceGroup")
AVExternalProtectionMonitor = _Class("AVExternalProtectionMonitor")
AVExternalProtectionMonitorInternal = _Class("AVExternalProtectionMonitorInternal")
AVFragmentedAssetTrackInternal = _Class("AVFragmentedAssetTrackInternal")
AVFragmentedAssetMinder = _Class("AVFragmentedAssetMinder")
AVFragmentedMovieMinder = _Class("AVFragmentedMovieMinder")
AVFragmentedAssetMinderInternal = _Class("AVFragmentedAssetMinderInternal")
AVFragmentedAssetInternal = _Class("AVFragmentedAssetInternal")
AVSampleBufferAudioRendererInternal = _Class("AVSampleBufferAudioRendererInternal")
AVAssetWriterInputMetadataAdaptor = _Class("AVAssetWriterInputMetadataAdaptor")
AVAssetWriterInputMetadataAdaptorInternal = _Class(
    "AVAssetWriterInputMetadataAdaptorInternal"
)
AVSynchronizedLayerInternal = _Class("AVSynchronizedLayerInternal")
AVAudioMixSweepFilterEffectParametersInternal = _Class(
    "AVAudioMixSweepFilterEffectParametersInternal"
)
AVAudioMixEffectParameters = _Class("AVAudioMixEffectParameters")
AVAudioMixSweepFilterEffectParameters = _Class("AVAudioMixSweepFilterEffectParameters")
AVAssetExportSession = _Class("AVAssetExportSession")
AVAssetExportSessionInternal = _Class("AVAssetExportSessionInternal")
AVAssetProxyInternal = _Class("AVAssetProxyInternal")
AVVideoCompositionCoreAnimationToolInternal = _Class(
    "AVVideoCompositionCoreAnimationToolInternal"
)
AVVideoCompositionCoreAnimationTool = _Class("AVVideoCompositionCoreAnimationTool")
AVVideoComposition = _Class("AVVideoComposition")
AVMutableVideoComposition = _Class("AVMutableVideoComposition")
AVVideoCompositionInternal = _Class("AVVideoCompositionInternal")
AVVideoCompositionLayerInstruction = _Class("AVVideoCompositionLayerInstruction")
AVMutableVideoCompositionLayerInstruction = _Class(
    "AVMutableVideoCompositionLayerInstruction"
)
AVVideoCompositionLayerInstructionInternal = _Class(
    "AVVideoCompositionLayerInstructionInternal"
)
AVVideoCompositionInstruction = _Class("AVVideoCompositionInstruction")
AVMutableVideoCompositionInstruction = _Class("AVMutableVideoCompositionInstruction")
AVVideoCompositionInstructionInternal = _Class("AVVideoCompositionInstructionInternal")
AVAssetWriterInputPassDescription = _Class("AVAssetWriterInputPassDescription")
AVAssetWriterInputPassDescriptionInternal = _Class(
    "AVAssetWriterInputPassDescriptionInternal"
)
AVAssetWriterInputPassDescriptionResponder = _Class(
    "AVAssetWriterInputPassDescriptionResponder"
)
AVAssetWriterInputMediaDataRequester = _Class("AVAssetWriterInputMediaDataRequester")
AVFigAssetWriterTrack = _Class("AVFigAssetWriterTrack")
AVFigAssetWriterGenericTrack = _Class("AVFigAssetWriterGenericTrack")
AVFigAssetWriterVideoTrack = _Class("AVFigAssetWriterVideoTrack")
AVFigAssetWriterAudioTrack = _Class("AVFigAssetWriterAudioTrack")
AVAssetWriterInputPixelBufferAdaptor = _Class("AVAssetWriterInputPixelBufferAdaptor")
AVAssetWriterInputPixelBufferAdaptorInternal = _Class(
    "AVAssetWriterInputPixelBufferAdaptorInternal"
)
AVAssetWriterInputHelper = _Class("AVAssetWriterInputHelper")
AVAssetWriterInputTerminalHelper = _Class("AVAssetWriterInputTerminalHelper")
AVAssetWriterInputNoMorePassesHelper = _Class("AVAssetWriterInputNoMorePassesHelper")
AVAssetWriterInputInterPassAnalysisHelper = _Class(
    "AVAssetWriterInputInterPassAnalysisHelper"
)
AVAssetWriterInputWritingHelper = _Class("AVAssetWriterInputWritingHelper")
AVAssetWriterInputUnknownHelper = _Class("AVAssetWriterInputUnknownHelper")
AVAssetWriterInput = _Class("AVAssetWriterInput")
AVAssetWriterInputInternal = _Class("AVAssetWriterInputInternal")
AVAssetWriterInputConfigurationState = _Class("AVAssetWriterInputConfigurationState")
AVRoutingSessionDestination = _Class("AVRoutingSessionDestination")
AVRoutingSessionDestinationInternal = _Class("AVRoutingSessionDestinationInternal")
AVRoutingSession = _Class("AVRoutingSession")
AVRoutingSessionInternal = _Class("AVRoutingSessionInternal")
AVRoutingSessionManager = _Class("AVRoutingSessionManager")
AVRoutingSessionManagerInternal = _Class("AVRoutingSessionManagerInternal")
AVPlayerItemMediaDataCollector = _Class("AVPlayerItemMediaDataCollector")
AVPlayerItemMetadataCollector = _Class("AVPlayerItemMetadataCollector")
AVPlayerItemMetadataCollectorInternal = _Class("AVPlayerItemMetadataCollectorInternal")
AVTimebaseObserver = _Class("AVTimebaseObserver")
AVOnceTimebaseObserver = _Class("AVOnceTimebaseObserver")
AVOccasionalTimebaseObserver = _Class("AVOccasionalTimebaseObserver")
AVPeriodicTimebaseObserver = _Class("AVPeriodicTimebaseObserver")
AVMediaSelectionOption = _Class("AVMediaSelectionOption")
AVMediaSelectionNilOption = _Class("AVMediaSelectionNilOption")
AVMediaSelectionKeyValueOption = _Class("AVMediaSelectionKeyValueOption")
AVMediaSelectionTrackOption = _Class("AVMediaSelectionTrackOption")
AVAssetWriterInputSelectionOption = _Class("AVAssetWriterInputSelectionOption")
AVMediaSelectionGroup = _Class("AVMediaSelectionGroup")
AVAssetMediaSelectionGroup = _Class("AVAssetMediaSelectionGroup")
AVAssetWriterInputGroup = _Class("AVAssetWriterInputGroup")
AVAssetWriterInputGroupInternal = _Class("AVAssetWriterInputGroupInternal")
AVFragmentedMediaDataReport = _Class("AVFragmentedMediaDataReport")
AVFragmentedMediaDataReportInternal = _Class("AVFragmentedMediaDataReportInternal")
AVAssetWriterFigAssetWriterNotificationHandler = _Class(
    "AVAssetWriterFigAssetWriterNotificationHandler"
)
AVAssetWriterHelper = _Class("AVAssetWriterHelper")
AVAssetWriterTerminalHelper = _Class("AVAssetWriterTerminalHelper")
AVAssetWriterClientInitiatedTerminalHelper = _Class(
    "AVAssetWriterClientInitiatedTerminalHelper"
)
AVAssetWriterFailedTerminalHelper = _Class("AVAssetWriterFailedTerminalHelper")
AVAssetWriterFinishWritingHelper = _Class("AVAssetWriterFinishWritingHelper")
AVAssetWriterWritingHelper = _Class("AVAssetWriterWritingHelper")
AVAssetWriterUnknownHelper = _Class("AVAssetWriterUnknownHelper")
AVAssetWriter = _Class("AVAssetWriter")
AVAssetWriterInternal = _Class("AVAssetWriterInternal")
AVAssetWriterConfigurationState = _Class("AVAssetWriterConfigurationState")
AVAssetReaderSampleReferenceOutputInternal = _Class(
    "AVAssetReaderSampleReferenceOutputInternal"
)
AVAssetReaderVideoCompositionOutputInternal = _Class(
    "AVAssetReaderVideoCompositionOutputInternal"
)
AVAssetReaderAudioMixOutputInternal = _Class("AVAssetReaderAudioMixOutputInternal")
AVAssetReaderTrackOutputInternal = _Class("AVAssetReaderTrackOutputInternal")
AVAssetReaderOutput = _Class("AVAssetReaderOutput")
AVAssetReaderSampleReferenceOutput = _Class("AVAssetReaderSampleReferenceOutput")
AVAssetReaderVideoCompositionOutput = _Class("AVAssetReaderVideoCompositionOutput")
AVAssetReaderAudioMixOutput = _Class("AVAssetReaderAudioMixOutput")
AVAssetReaderTrackOutput = _Class("AVAssetReaderTrackOutput")
AVAssetReaderOutputInternal = _Class("AVAssetReaderOutputInternal")
AVAssetReader = _Class("AVAssetReader")
AVAssetReaderInternal = _Class("AVAssetReaderInternal")
AVAssetTrackSegment = _Class("AVAssetTrackSegment")
AVCompositionTrackSegment = _Class("AVCompositionTrackSegment")
AVCompositionTrackSegmentInternal = _Class("AVCompositionTrackSegmentInternal")
AVMutableCompositionTrackInternal = _Class("AVMutableCompositionTrackInternal")
AVCompositionTrackInternal = _Class("AVCompositionTrackInternal")
AVCompositionTrackFormatDescriptionReplacement = _Class(
    "AVCompositionTrackFormatDescriptionReplacement"
)
AVFigObjectInspector = _Class("AVFigObjectInspector")
AVAssetTrackInspector = _Class("AVAssetTrackInspector")
AVStreamDataAssetTrackInspector = _Class("AVStreamDataAssetTrackInspector")
AVPlaybackItemTrackInspector = _Class("AVPlaybackItemTrackInspector")
AVFigAssetTrackInspector = _Class("AVFigAssetTrackInspector")
AVTrackReaderInspector = _Class("AVTrackReaderInspector")
AVCompositionTrackReaderInspector = _Class("AVCompositionTrackReaderInspector")
AVAssetInspector = _Class("AVAssetInspector")
AVStreamDataAssetInspector = _Class("AVStreamDataAssetInspector")
AVFigAssetInspector = _Class("AVFigAssetInspector")
AVStreamingResourceInspector = _Class("AVStreamingResourceInspector")
AVPlaybackItemInspector = _Class("AVPlaybackItemInspector")
AVFormatReaderInspector = _Class("AVFormatReaderInspector")
AVCompositionFormatReaderInspector = _Class("AVCompositionFormatReaderInspector")
AVMutableCompositionInternal = _Class("AVMutableCompositionInternal")
AVCompositionInternal = _Class("AVCompositionInternal")
AVOutputDeviceDiscoverySessionAvailableOutputDevices = _Class(
    "AVOutputDeviceDiscoverySessionAvailableOutputDevices"
)
AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices = _Class(
    "AVEmptyOutputDeviceDiscoverySessionAvailableOutputDevices"
)
AVOutputDeviceDiscoverySession = _Class("AVOutputDeviceDiscoverySession")
AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal = _Class(
    "AVOutputDeviceDiscoverySessionAvailableOutputDevicesInternal"
)
AVOutputDeviceDiscoverySessionInternal = _Class(
    "AVOutputDeviceDiscoverySessionInternal"
)
AVQueuePlayerInternal = _Class("AVQueuePlayerInternal")
AVAssetDownloadStorageManagementPolicyInternal = _Class(
    "AVAssetDownloadStorageManagementPolicyInternal"
)
AVAssetDownloadStorageManagementPolicy = _Class(
    "AVAssetDownloadStorageManagementPolicy"
)
AVMutableAssetDownloadStorageManagementPolicy = _Class(
    "AVMutableAssetDownloadStorageManagementPolicy"
)
AVAssetDownloadStorageManager = _Class("AVAssetDownloadStorageManager")
AVPlayerItemTrack = _Class("AVPlayerItemTrack")
AVPlayerItemTrackInternal = _Class("AVPlayerItemTrackInternal")
AVPlayerLoggingIdentifier = _Class("AVPlayerLoggingIdentifier")
AVPlayerLoggingIdentifierInternal = _Class("AVPlayerLoggingIdentifierInternal")
AVAssetLoggingIdentifier = _Class("AVAssetLoggingIdentifier")
AVAssetLoggingIdentifierInternal = _Class("AVAssetLoggingIdentifierInternal")
AVSpecifiedLoggingIdentifier = _Class("AVSpecifiedLoggingIdentifier")
AVSpecifiedLoggingIdentifierInternal = _Class("AVSpecifiedLoggingIdentifierInternal")
AVPlayerConnection = _Class("AVPlayerConnection")
AVPlayerItem = _Class("AVPlayerItem")
AVPlayerItemInternal = _Class("AVPlayerItemInternal")
AVOutputContextLocalOutputDeviceGroupImpl = _Class(
    "AVOutputContextLocalOutputDeviceGroupImpl"
)
AVPlayerQueueModificationDescription = _Class("AVPlayerQueueModificationDescription")
AVPlayer = _Class("AVPlayer")
AVQueuePlayer = _Class("AVQueuePlayer")
AVPlayerInternal = _Class("AVPlayerInternal")
AVAssetTrack = _Class("AVAssetTrack")
AVMovieTrack = _Class("AVMovieTrack")
AVMutableMovieTrack = _Class("AVMutableMovieTrack")
AVFragmentedMovieTrack = _Class("AVFragmentedMovieTrack")
AVFragmentedAssetTrack = _Class("AVFragmentedAssetTrack")
AVCompositionTrack = _Class("AVCompositionTrack")
AVMutableCompositionTrack = _Class("AVMutableCompositionTrack")
AVAssetTrackInternal = _Class("AVAssetTrackInternal")
AVAssetReaderOutputMetadataAdaptor = _Class("AVAssetReaderOutputMetadataAdaptor")
AVAssetReaderOutputMetadataAdaptorInternal = _Class(
    "AVAssetReaderOutputMetadataAdaptorInternal"
)
AVAssetImageGenerator = _Class("AVAssetImageGenerator")
AVAssetImageGeneratorInternal = _Class("AVAssetImageGeneratorInternal")
AVURLAssetItemProviderData = _Class("AVURLAssetItemProviderData")
AVAssetClientURLRequestHelper = _Class("AVAssetClientURLRequestHelper")
AVURLAssetInternal = _Class("AVURLAssetInternal")
AVAssetFragment = _Class("AVAssetFragment")
AVAssetFragmentInternal = _Class("AVAssetFragmentInternal")
AVAssetInternal = _Class("AVAssetInternal")
AVMetadataItemFilterInternal = _Class("AVMetadataItemFilterInternal")
AVMetadataItemFilter = _Class("AVMetadataItemFilter")
AVMetadataItemFilterForSharing = _Class("AVMetadataItemFilterForSharing")
AVChapterMetadataItemInternal = _Class("AVChapterMetadataItemInternal")
AVMetadataItemValueRequest = _Class("AVMetadataItemValueRequest")
AVMetadataItemValueRequestInternal = _Class("AVMetadataItemValueRequestInternal")
AVLazyValueLoadingMetadataItemInternal = _Class(
    "AVLazyValueLoadingMetadataItemInternal"
)
AVMetadataItem = _Class("AVMetadataItem")
AVChapterMetadataItem = _Class("AVChapterMetadataItem")
AVLazyValueLoadingMetadataItem = _Class("AVLazyValueLoadingMetadataItem")
AVMutableMetadataItem = _Class("AVMutableMetadataItem")
AVMetadataItemInternal = _Class("AVMetadataItemInternal")
AVPlayerLooper = _Class("AVPlayerLooper")
AVPlayerLooperInternal = _Class("AVPlayerLooperInternal")
AVPlayerLayerInternal = _Class("AVPlayerLayerInternal")
AVFigRemoteRouteDiscovererFactory = _Class("AVFigRemoteRouteDiscovererFactory")
AVAsset = _Class("AVAsset")
AVStreamDataAsset = _Class("AVStreamDataAsset")
AVMovie = _Class("AVMovie")
AVMutableMovie = _Class("AVMutableMovie")
AVFragmentedMovie = _Class("AVFragmentedMovie")
AVAssetProxy = _Class("AVAssetProxy")
AVComposition = _Class("AVComposition")
AVMutableComposition = _Class("AVMutableComposition")
AVDataAsset = _Class("AVDataAsset")
AVURLAsset = _Class("AVURLAsset")
AVStreamDataInspectionOnlyAsset = _Class("AVStreamDataInspectionOnlyAsset")
AVFragmentedAsset = _Class("AVFragmentedAsset")
AVSampleBufferRenderSynchronizer = _Class("AVSampleBufferRenderSynchronizer")
AVSampleBufferAudioRenderer = _Class("AVSampleBufferAudioRenderer")
AVStreamDataParser = _Class("AVStreamDataParser")
AVRunLoopCondition = _Class("AVRunLoopCondition")
AVURLAuthenticationChallenge = _Class("AVURLAuthenticationChallenge")
AVAggregateAssetDownloadTask = _Class("AVAggregateAssetDownloadTask")
AVOperationQueueWithFundamentalDependency = _Class(
    "AVOperationQueueWithFundamentalDependency"
)
AVSampleBufferDisplayLayerContentLayer = _Class(
    "AVSampleBufferDisplayLayerContentLayer"
)
AVSynchronizedLayer = _Class("AVSynchronizedLayer")
AVPlayerLayer = _Class("AVPlayerLayer")
AVPlayerLayerIntermediateLayer = _Class("AVPlayerLayerIntermediateLayer")
AVNetworkPlaybackPerfHUDLayer = _Class("AVNetworkPlaybackPerfHUDLayer")
AVSampleBufferDisplayLayer = _Class("AVSampleBufferDisplayLayer")
AVWaitForNotificationOrDeallocationOperation = _Class(
    "AVWaitForNotificationOrDeallocationOperation"
)
AVOperation = _Class("AVOperation")
AVRouteConfigUpdatedFigRoutingContextRouteChangeOperation = _Class(
    "AVRouteConfigUpdatedFigRoutingContextRouteChangeOperation"
)
AVFigRoutingContextRouteChangeOperation = _Class(
    "AVFigRoutingContextRouteChangeOperation"
)
AVFigRoutingContextSendConfigureDeviceCommandOperation = _Class(
    "AVFigRoutingContextSendConfigureDeviceCommandOperation"
)
AVBlockOperation = _Class("AVBlockOperation")
AVAssetWriterInputFigAssetWriterEndPassOperation = _Class(
    "AVAssetWriterInputFigAssetWriterEndPassOperation"
)
AVFigAssetWriterFinishWritingAsyncOperation = _Class(
    "AVFigAssetWriterFinishWritingAsyncOperation"
)
AVWorkaroundNSBlockOperation = _Class("AVWorkaroundNSBlockOperation")
AVMetadataEnumerator = _Class("AVMetadataEnumerator")
AVAssetTrackEnumerator = _Class("AVAssetTrackEnumerator")
AVTimeFormatter = _Class("AVTimeFormatter")
CMTimeMappingAsValue = _Class("CMTimeMappingAsValue")
CMTimeRangeAsValue = _Class("CMTimeRangeAsValue")
CMTimeAsValue = _Class("CMTimeAsValue")
AVFragmentedAssetsArray = _Class("AVFragmentedAssetsArray")
AVMomentCaptureMovie = _Class("AVMomentCaptureMovie")
AVCapturePhotoOutputInternal = _Class("AVCapturePhotoOutputInternal")
AVCaptureSessionInternal = _Class("AVCaptureSessionInternal")
AVFrameRateRange = _Class("AVFrameRateRange")
AVFrameRateRangeInternal = _Class("AVFrameRateRangeInternal")
AVCaptureMetadataOutputInternal = _Class("AVCaptureMetadataOutputInternal")
AVCaptureBracketedStillImageSettings = _Class("AVCaptureBracketedStillImageSettings")
AVCaptureAutoExposureBracketedStillImageSettings = _Class(
    "AVCaptureAutoExposureBracketedStillImageSettings"
)
AVCaptureManualExposureBracketedStillImageSettings = _Class(
    "AVCaptureManualExposureBracketedStillImageSettings"
)
AVCaptureVideoPreviewLayerInternal = _Class("AVCaptureVideoPreviewLayerInternal")
AVCaptureDeviceControlRequestQueue = _Class("AVCaptureDeviceControlRequestQueue")
AVCaptureDeviceControlRequest = _Class("AVCaptureDeviceControlRequest")
AVCaptureDeviceFakeBiasControlRequest = _Class("AVCaptureDeviceFakeBiasControlRequest")
AVCaptureSynchronizedVisionDataInternal = _Class(
    "AVCaptureSynchronizedVisionDataInternal"
)
AVCaptureSynchronizedDepthDataInternal = _Class(
    "AVCaptureSynchronizedDepthDataInternal"
)
AVCaptureSynchronizedMetadataObjectDataInternal = _Class(
    "AVCaptureSynchronizedMetadataObjectDataInternal"
)
AVCaptureSynchronizedSampleBufferDataInternal = _Class(
    "AVCaptureSynchronizedSampleBufferDataInternal"
)
AVCaptureSynchronizedData = _Class("AVCaptureSynchronizedData")
AVCaptureSynchronizedCameraCalibrationData = _Class(
    "AVCaptureSynchronizedCameraCalibrationData"
)
AVCaptureSynchronizedPointCloudData = _Class("AVCaptureSynchronizedPointCloudData")
AVCaptureSynchronizedVisionData = _Class("AVCaptureSynchronizedVisionData")
AVCaptureSynchronizedDepthData = _Class("AVCaptureSynchronizedDepthData")
AVCaptureSynchronizedMetadataObjectData = _Class(
    "AVCaptureSynchronizedMetadataObjectData"
)
AVCaptureSynchronizedSampleBufferData = _Class("AVCaptureSynchronizedSampleBufferData")
AVCaptureSynchronizedDataInternal = _Class("AVCaptureSynchronizedDataInternal")
AVCaptureSessionConfiguration = _Class("AVCaptureSessionConfiguration")
AVCaptureInputInternal = _Class("AVCaptureInputInternal")
AVApplePortraitMetadata = _Class("AVApplePortraitMetadata")
AVApplePortraitMetadataInternal = _Class("AVApplePortraitMetadataInternal")
AVPortraitEffectsMatte = _Class("AVPortraitEffectsMatte")
AVPortraitEffectsMatteInternal = _Class("AVPortraitEffectsMatteInternal")
AVCaptureAudioDataOutputInternal = _Class("AVCaptureAudioDataOutputInternal")
AVCaptureDeferredPhotoProcessor = _Class("AVCaptureDeferredPhotoProcessor")
AVCaptureDeferredPhotoProcessingRequest = _Class(
    "AVCaptureDeferredPhotoProcessingRequest"
)
AVCaptureDataOutputSynchronizer = _Class("AVCaptureDataOutputSynchronizer")
AVCaptureDataOutputSynchronizerInternal = _Class(
    "AVCaptureDataOutputSynchronizerInternal"
)
AVCDOSDataOutputStorage = _Class("AVCDOSDataOutputStorage")
AVCaptureDataOutputDelegateCallbackHelper = _Class(
    "AVCaptureDataOutputDelegateCallbackHelper"
)
AVCaptureInputPort = _Class("AVCaptureInputPort")
AVCaptureInputPortInternal = _Class("AVCaptureInputPortInternal")
AVCaptureSession = _Class("AVCaptureSession")
AVCaptureMultiCamSession = _Class("AVCaptureMultiCamSession")
AVMetadataMachineReadableCodeObjectInternal = _Class(
    "AVMetadataMachineReadableCodeObjectInternal"
)
AVMetadataOfflineVideoStabilizationMotionObjectInternal = _Class(
    "AVMetadataOfflineVideoStabilizationMotionObjectInternal"
)
AVMetadataTrackedFacesObjectInternal = _Class("AVMetadataTrackedFacesObjectInternal")
AVMetadataFaceObjectInternal = _Class("AVMetadataFaceObjectInternal")
AVMetadataObject = _Class("AVMetadataObject")
AVMetadataVideoPreviewHistogramObject = _Class("AVMetadataVideoPreviewHistogramObject")
AVMetadataMachineReadableCodeObject = _Class("AVMetadataMachineReadableCodeObject")
AVMetadataOfflineVideoStabilizationMotionObject = _Class(
    "AVMetadataOfflineVideoStabilizationMotionObject"
)
AVMetadataTrackedFacesObject = _Class("AVMetadataTrackedFacesObject")
AVMetadataFaceObject = _Class("AVMetadataFaceObject")
AVMetadataSaliencyHeatMap = _Class("AVMetadataSaliencyHeatMap")
AVMetadataSalientObject = _Class("AVMetadataSalientObject")
AVMetadataBodyObject = _Class("AVMetadataBodyObject")
AVMetadataDogBodyObject = _Class("AVMetadataDogBodyObject")
AVMetadataCatBodyObject = _Class("AVMetadataCatBodyObject")
AVMetadataHumanBodyObject = _Class("AVMetadataHumanBodyObject")
AVMetadataObjectInternal = _Class("AVMetadataObjectInternal")
AVCaptureMovieFileOutputInternal = _Class("AVCaptureMovieFileOutputInternal")
AVCameraCalibrationData = _Class("AVCameraCalibrationData")
AVCameraCalibrationDataInternal = _Class("AVCameraCalibrationDataInternal")
AVMomentCaptureMovieRecordingResolvedSettings = _Class(
    "AVMomentCaptureMovieRecordingResolvedSettings"
)
AVMomentCaptureMovieRecordingSettings = _Class("AVMomentCaptureMovieRecordingSettings")
AVMomentCaptureMovieRequest = _Class("AVMomentCaptureMovieRequest")
AVCaptureStillImageOutputInternal = _Class("AVCaptureStillImageOutputInternal")
AVCapturePrepareBracketRequest = _Class("AVCapturePrepareBracketRequest")
AVCaptureStillImageRequest = _Class("AVCaptureStillImageRequest")
AVCaptureSynchronizedDataCollectionInternal = _Class(
    "AVCaptureSynchronizedDataCollectionInternal"
)
AVCaptureDevice = _Class("AVCaptureDevice")
AVCaptureFigAudioDevice = _Class("AVCaptureFigAudioDevice")
AVCaptureFigVideoDevice = _Class("AVCaptureFigVideoDevice")
AVCaptureDeviceInternal = _Class("AVCaptureDeviceInternal")
AVCaptureVisionDataOutputInternal = _Class("AVCaptureVisionDataOutputInternal")
AVCapturePhotoRequest = _Class("AVCapturePhotoRequest")
AVCaptureDeviceInputInternal = _Class("AVCaptureDeviceInputInternal")
AVOfflineVideoStabilizer = _Class("AVOfflineVideoStabilizer")
AVCaptureConnection = _Class("AVCaptureConnection")
AVCaptureConnectionInternal = _Class("AVCaptureConnectionInternal")
AVCaptureAudioChannel = _Class("AVCaptureAudioChannel")
AVCaptureAudioChannelInternal = _Class("AVCaptureAudioChannelInternal")
AVCaptureVideoDataOutputInternal = _Class("AVCaptureVideoDataOutputInternal")
AVDepthData = _Class("AVDepthData")
AVDepthDataInternal = _Class("AVDepthDataInternal")
AVMomentCaptureSettings = _Class("AVMomentCaptureSettings")
AVCapturePreparedPhotoSettingsArrayRequest = _Class(
    "AVCapturePreparedPhotoSettingsArrayRequest"
)
AVCapturePhotoInitiationSettings = _Class("AVCapturePhotoInitiationSettings")
AVCapturePhotoInitiationSettingsInternal = _Class(
    "AVCapturePhotoInitiationSettingsInternal"
)
AVCaptureResolvedPhotoSettings = _Class("AVCaptureResolvedPhotoSettings")
AVCaptureResolvedPhotoSettingsInternal = _Class(
    "AVCaptureResolvedPhotoSettingsInternal"
)
AVCapturePhotoBracketSettingsInternal = _Class("AVCapturePhotoBracketSettingsInternal")
AVCapturePhotoSettings = _Class("AVCapturePhotoSettings")
AVCapturePhotoBracketSettings = _Class("AVCapturePhotoBracketSettings")
AVCapturePhotoSettingsInternal = _Class("AVCapturePhotoSettingsInternal")
AVCaptureVideoSettingsValidator = _Class("AVCaptureVideoSettingsValidator")
AVCaptureOutputInternal = _Class("AVCaptureOutputInternal")
AVCaptureDeviceFormat = _Class("AVCaptureDeviceFormat")
AVCaptureDeviceFormatInternal = _Class("AVCaptureDeviceFormatInternal")
AVCapturePhotoPrivateClientMetadata = _Class("AVCapturePhotoPrivateClientMetadata")
AVPointCloudData = _Class("AVPointCloudData")
AVCaptureDeviceDiscoverySession = _Class("AVCaptureDeviceDiscoverySession")
AVCaptureDepthDataOutputInternal = _Class("AVCaptureDepthDataOutputInternal")
AVSemanticSegmentationMatte = _Class("AVSemanticSegmentationMatte")
AVCaptureSystemPressureState = _Class("AVCaptureSystemPressureState")
AVCaptureSystemPressureStateInternal = _Class("AVCaptureSystemPressureStateInternal")
AVCaptureInput = _Class("AVCaptureInput")
AVCaptureDeviceInput = _Class("AVCaptureDeviceInput")
AVCaptureMetadataInput = _Class("AVCaptureMetadataInput")
AVCaptureMetadataInputInternal = _Class("AVCaptureMetadataInputInternal")
AVFlashlight = _Class("AVFlashlight")
AVFlashlightInternal = _Class("AVFlashlightInternal")
AVCapturePhoto = _Class("AVCapturePhoto")
AVCaptureDeferredPhotoProxy = _Class("AVCaptureDeferredPhotoProxy")
AVCapturePhotoInternal = _Class("AVCapturePhotoInternal")
AVCaptureVideoThumbnailOutputInternal = _Class("AVCaptureVideoThumbnailOutputInternal")
AVCaptureOutput = _Class("AVCaptureOutput")
AVCapturePhotoOutput = _Class("AVCapturePhotoOutput")
AVCaptureMetadataOutput = _Class("AVCaptureMetadataOutput")
AVCaptureAudioDataOutput = _Class("AVCaptureAudioDataOutput")
AVCaptureStillImageOutput = _Class("AVCaptureStillImageOutput")
AVCapturePointCloudDataOutput = _Class("AVCapturePointCloudDataOutput")
AVCaptureCameraCalibrationDataOutput = _Class("AVCaptureCameraCalibrationDataOutput")
AVCaptureVisionDataOutput = _Class("AVCaptureVisionDataOutput")
AVCaptureVideoDataOutput = _Class("AVCaptureVideoDataOutput")
AVCaptureDepthDataOutput = _Class("AVCaptureDepthDataOutput")
AVCaptureVideoThumbnailOutput = _Class("AVCaptureVideoThumbnailOutput")
AVCaptureFileOutput = _Class("AVCaptureFileOutput")
AVCaptureMovieFileOutput = _Class("AVCaptureMovieFileOutput")
AVCaptureFileOutputInternal = _Class("AVCaptureFileOutputInternal")
AVCaptureFileOutputDelegateWrapper = _Class("AVCaptureFileOutputDelegateWrapper")
AVMomentCaptureMovieFileOutputDelegateWrapper = _Class(
    "AVMomentCaptureMovieFileOutputDelegateWrapper"
)
AVCaptureSynchronizedDataCollection = _Class("AVCaptureSynchronizedDataCollection")
AVCaptureVideoPreviewLayer = _Class("AVCaptureVideoPreviewLayer")
AVSpatialOverCaptureVideoPreviewLayer = _Class("AVSpatialOverCaptureVideoPreviewLayer")
