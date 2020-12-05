"""
Classes from the 'VoiceTrigger' framework.
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


VTPhraseSpotter = _Class("VTPhraseSpotter")
VTXPCConnection = _Class("VTXPCConnection")
VTCorruptDetector = _Class("VTCorruptDetector")
VTInvalidSATEntriesCleaner = _Class("VTInvalidSATEntriesCleaner")
VTKeywordAnalyzerNDEAPI = _Class("VTKeywordAnalyzerNDEAPI")
VTVoiceProfileMigration = _Class("VTVoiceProfileMigration")
VTKeywordAnalyzerNDAPI = _Class("VTKeywordAnalyzerNDAPI")
VTKeywordAnalyzerQuasar = _Class("VTKeywordAnalyzerQuasar")
VTAggregator = _Class("VTAggregator")
VTAudioFileReader = _Class("VTAudioFileReader")
VTAudioFileLog = _Class("VTAudioFileLog")
VTAnalyzerNDAPI = _Class("VTAnalyzerNDAPI")
VTPhraseSpotterControlConnection = _Class("VTPhraseSpotterControlConnection")
VTAssetManager = _Class("VTAssetManager")
VTVoiceProfileRetrainer = _Class("VTVoiceProfileRetrainer")
VTSiriNotifications = _Class("VTSiriNotifications")
AudioFileWriter = _Class("AudioFileWriter")
VTStateManager = _Class("VTStateManager")
VTTriggerEventMonitor = _Class("VTTriggerEventMonitor")
VTUtilities = _Class("VTUtilities")
VTNovDetector = _Class("VTNovDetector")
VTNovDetectorResult = _Class("VTNovDetectorResult")
VTPreferences = _Class("VTPreferences")
VTKeywordDetectorResults = _Class("VTKeywordDetectorResults")
VTKeywordDetectorPhraseScore = _Class("VTKeywordDetectorPhraseScore")
VTKeywordAnalyzerResults = _Class("VTKeywordAnalyzerResults")
VTKeywordAnalyzerPhraseScore = _Class("VTKeywordAnalyzerPhraseScore")
VTBlobBuilder = _Class("VTBlobBuilder")
VTKeywordDetectorAssets = _Class("VTKeywordDetectorAssets")
VTPhraseSpotterControlRemote = _Class("VTPhraseSpotterControlRemote")
VTCoreSpeechKeepAliveHandler = _Class("VTCoreSpeechKeepAliveHandler")
VTXPCServiceClient = _Class("VTXPCServiceClient")
VTTranscriber = _Class("VTTranscriber")
VTUtteranceMetadataManager = _Class("VTUtteranceMetadataManager")
VTKeywordDetector = _Class("VTKeywordDetector")
VTKeywordDetectorContext = _Class("VTKeywordDetectorContext")
VTPeerRemoteConnection = _Class("VTPeerRemoteConnection")
VTGestureMonitor = _Class("VTGestureMonitor")
VTGestureMonitorPhone = _Class("VTGestureMonitorPhone")
VTSiriPHash = _Class("VTSiriPHash")
VTSpeakerIdUtilities = _Class("VTSpeakerIdUtilities")
VTXPCServiceServer = _Class("VTXPCServiceServer")
VTEventMonitor = _Class("VTEventMonitor")
VTBiometricMatchMonitor = _Class("VTBiometricMatchMonitor")
VTSoftwareUpdateCheckingMonitor = _Class("VTSoftwareUpdateCheckingMonitor")
VTFirstUnlockMonitor = _Class("VTFirstUnlockMonitor")
VTAudioRouteChangeMonitor = _Class("VTAudioRouteChangeMonitor")
VTVoiceTriggerEnabledMonitor = _Class("VTVoiceTriggerEnabledMonitor")
VTLockScreenMonitor = _Class("VTLockScreenMonitor")
VTBatteryMonitor = _Class("VTBatteryMonitor")
VTSiriAssertionMonitor = _Class("VTSiriAssertionMonitor")
VTSiriRestrictionOnLockScreenMonitor = _Class("VTSiriRestrictionOnLockScreenMonitor")
VTSpringboardStartMonitor = _Class("VTSpringboardStartMonitor")
VTLowPowerModeMonitor = _Class("VTLowPowerModeMonitor")
VTAssetMonitor = _Class("VTAssetMonitor")
VTSiriEnabledMonitor = _Class("VTSiriEnabledMonitor")
VTLanguageCodeUpdateMonitor = _Class("VTLanguageCodeUpdateMonitor")
VTPolicy = _Class("VTPolicy")
VTVoiceTriggerEnabledPolicyAOP = _Class("VTVoiceTriggerEnabledPolicyAOP")
VTVoiceTriggerEnabledPolicyHorseman = _Class("VTVoiceTriggerEnabledPolicyHorseman")
VTVoiceTriggerEnabledPolicyNonAOP = _Class("VTVoiceTriggerEnabledPolicyNonAOP")
VTAssetManagerEnablePolicy = _Class("VTAssetManagerEnablePolicy")
VTVoiceTriggerEnabledPolicyWatch = _Class("VTVoiceTriggerEnabledPolicyWatch")
VTPhraseSpotterEnabledPolicy = _Class("VTPhraseSpotterEnabledPolicy")
VTTextDependentSpeakerRecognizer = _Class("VTTextDependentSpeakerRecognizer")
VTEventTrackerManager = _Class("VTEventTrackerManager")
VTTriggerEventMonitorManager = _Class("VTTriggerEventMonitorManager")
VTBuiltInRTModel = _Class("VTBuiltInRTModel")
VTEvent = _Class("VTEvent")
VTEventPHSReject = _Class("VTEventPHSReject")
VTEventNearTrigger = _Class("VTEventNearTrigger")
VTEventAudioCorrupt = _Class("VTEventAudioCorrupt")
VTEventTrigger = _Class("VTEventTrigger")
VTEventPrepare = _Class("VTEventPrepare")
VTAudioCircularBuffer = _Class("VTAudioCircularBuffer")
