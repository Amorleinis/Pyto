"""
Classes from the 'Sharing' framework.
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


SFWiFiHealthMonitor = _Class("SFWiFiHealthMonitor")
SFTRSession = _Class("SFTRSession")
SFSystemSession = _Class("SFSystemSession")
SFSystemService = _Class("SFSystemService")
SFSiriWordTimingPlayer = _Class("SFSiriWordTimingPlayer")
SFSiriWordTimingInfo = _Class("SFSiriWordTimingInfo")
SFSiriClient = _Class("SFSiriClient")
SFSiriRequest = _Class("SFSiriRequest")
SFSiriDeviceSetupGreetingDetails = _Class("SFSiriDeviceSetupGreetingDetails")
SFShareAudioService = _Class("SFShareAudioService")
SFShareAudioSessionClient = _Class("SFShareAudioSessionClient")
SFSession = _Class("SFSession")
SFServiceSession = _Class("SFServiceSession")
SFService = _Class("SFService")
SFRemoteTextSessionInfo = _Class("SFRemoteTextSessionInfo")
SFRemoteInteractionSession = _Class("SFRemoteInteractionSession")
SFRemoteAutoFillSession = _Class("SFRemoteAutoFillSession")
SFProximityEstimator = _Class("SFProximityEstimator")
SFProximityEstimatorMaxOfMean = _Class("SFProximityEstimatorMaxOfMean")
SFProximityEstimatorChannelMedian = _Class("SFProximityEstimatorChannelMedian")
SFPINPairSession = _Class("SFPINPairSession")
SFPasswordSharingInfo = _Class("SFPasswordSharingInfo")
SFPasswordSharingService = _Class("SFPasswordSharingService")
SFNFCTagReaderUIController = _Class("SFNFCTagReaderUIController")
SFMessage = _Class("SFMessage")
SFResponseMessage = _Class("SFResponseMessage")
SFRequestMessage = _Class("SFRequestMessage")
SFEventMessage = _Class("SFEventMessage")
SFDiagnostics = _Class("SFDiagnostics")
SFDeviceSetupWHASession = _Class("SFDeviceSetupWHASession")
SFDeviceSetupWHAService = _Class("SFDeviceSetupWHAService")
SFDeviceSetupTVLatencySession = _Class("SFDeviceSetupTVLatencySession")
SFDeviceSetupTVLatencyService = _Class("SFDeviceSetupTVLatencyService")
SFDeviceSetupSessioniOS = _Class("SFDeviceSetupSessioniOS")
SFDeviceSetupServiceiOS = _Class("SFDeviceSetupServiceiOS")
SFProxCardSessionServer = _Class("SFProxCardSessionServer")
SFDeviceSetupB238Session = _Class("SFDeviceSetupB238Session")
SFDeviceSetupB238Service = _Class("SFDeviceSetupB238Service")
SFBubbleEstimator = _Class("SFBubbleEstimator")
SFRSSIQueue = _Class("SFRSSIQueue")
SFDeviceAssetRequestConfiguration = _Class("SFDeviceAssetRequestConfiguration")
SFDeviceSetupAppleTVSession = _Class("SFDeviceSetupAppleTVSession")
SFDeviceSetupAppleTVService = _Class("SFDeviceSetupAppleTVService")
SFDeviceRepairSession = _Class("SFDeviceRepairSession")
SFDeviceRepairService = _Class("SFDeviceRepairService")
SFDeviceAssetQuery = _Class("SFDeviceAssetQuery")
SFDeviceOperationHandlerWiFiSetup = _Class("SFDeviceOperationHandlerWiFiSetup")
SFDeviceOperationWiFiSetup = _Class("SFDeviceOperationWiFiSetup")
SFDeviceOperationHomeKitSetup = _Class("SFDeviceOperationHomeKitSetup")
SFDeviceOperationHandlerCDPSetup = _Class("SFDeviceOperationHandlerCDPSetup")
SFDeviceOperationCDPSetup = _Class("SFDeviceOperationCDPSetup")
SFDeviceDiscovery = _Class("SFDeviceDiscovery")
SFDevice = _Class("SFDevice")
SFAccessibilityClient = _Class("SFAccessibilityClient")
SFCoordinatedAlertRequest = _Class("SFCoordinatedAlertRequest")
SFContinuityRemoteSession = _Class("SFContinuityRemoteSession")
SFSessionRequestInfo = _Class("SFSessionRequestInfo")
SFMessageSessionRequestEntry = _Class("SFMessageSessionRequestEntry")
SFBLEData = _Class("SFBLEData")
SFNotificationInfo = _Class("SFNotificationInfo")
SFNotificationError = _Class("SFNotificationError")
SFBatteryInfo = _Class("SFBatteryInfo")
SFClient = _Class("SFClient")
SFPeopleSuggesterResult = _Class("SFPeopleSuggesterResult")
SFPeopleSuggesterParams = _Class("SFPeopleSuggesterParams")
SFContactInfo = _Class("SFContactInfo")
SFClientGetDeviceAssetsResults = _Class("SFClientGetDeviceAssetsResults")
SFClientGetDeviceAssetsParams = _Class("SFClientGetDeviceAssetsParams")
SFClientSubCredentialParams = _Class("SFClientSubCredentialParams")
SFProxHandoffService = _Class("SFProxHandoffService")
SFBluetoothPairingSession = _Class("SFBluetoothPairingSession")
SFBLEScanner = _Class("SFBLEScanner")
SFBLEPipe = _Class("SFBLEPipe")
SFBLEDevice = _Class("SFBLEDevice")
SFBLEConnection = _Class("SFBLEConnection")
SFBLEClient = _Class("SFBLEClient")
SFBLEAdvertiser = _Class("SFBLEAdvertiser")
SFApproveDiscovery = _Class("SFApproveDiscovery")
SFAppleIDPersonInfo = _Class("SFAppleIDPersonInfo")
SFRemoteTextInputClient = _Class("SFRemoteTextInputClient")
SFUserAlert = _Class("SFUserAlert")
SFAppleIDIdentity = _Class("SFAppleIDIdentity")
SFPowerSourceLEDInfo = _Class("SFPowerSourceLEDInfo")
SFPowerSource = _Class("SFPowerSource")
SFPowerSourceMonitor = _Class("SFPowerSourceMonitor")
SFDeviceAssetManager = _Class("SFDeviceAssetManager")
SFDeviceAssetTask = _Class("SFDeviceAssetTask")
SFDeviceQueryParameters = _Class("SFDeviceQueryParameters")
SFAccountManager = _Class("SFAccountManager")
SFCompanionService = _Class("SFCompanionService")
SFUnlockState = _Class("SFUnlockState")
SFAuthenticateAccountsSession = _Class("SFAuthenticateAccountsSession")
SFPasswordSharingSession = _Class("SFPasswordSharingSession")
SFDefaults = _Class("SFDefaults")
SFAirDropAction = _Class("SFAirDropAction")
SFRemoteHotspotInfo = _Class("SFRemoteHotspotInfo")
SFCompanionManager = _Class("SFCompanionManager")
SFAnnounceMessagesEvent = _Class("SFAnnounceMessagesEvent")
SFBLERecorder = _Class("SFBLERecorder")
SFProxCardSessionClient = _Class("SFProxCardSessionClient")
SFCompanionXPCManager = _Class("SFCompanionXPCManager")
SFRemoteAutoFillScanAction = _Class("SFRemoteAutoFillScanAction")
SFRemoteAutoFillService = _Class("SFRemoteAutoFillService")
SFCompanionAdvertiser = _Class("SFCompanionAdvertiser")
SFActivityScanner = _Class("SFActivityScanner")
SFActivityAdvertisement = _Class("SFActivityAdvertisement")
SFAirDropTransferMetaData = _Class("SFAirDropTransferMetaData")
SFAuthenticateAccountInfo = _Class("SFAuthenticateAccountInfo")
SFAuthenticateAccountsService = _Class("SFAuthenticateAccountsService")
SFRemoteHotspotSession = _Class("SFRemoteHotspotSession")
SFRemoteHotspotDevice = _Class("SFRemoteHotspotDevice")
SFAppleIDClient = _Class("SFAppleIDClient")
SFAirDropTransfer = _Class("SFAirDropTransfer")
SFAppleIDContactInfo = _Class("SFAppleIDContactInfo")
SFUnlockManager = _Class("SFUnlockManager")
SFAutoUnlockManager = _Class("SFAutoUnlockManager")
SFRemoteAutoFillSessionHelper = _Class("SFRemoteAutoFillSessionHelper")
SFProximityClient = _Class("SFProximityClient")
SFTokenBucketWithDups = _Class("SFTokenBucketWithDups")
SFTokenBucket = _Class("SFTokenBucket")
SFAppleIDAccount = _Class("SFAppleIDAccount")
SFWirelessSettingsController = _Class("SFWirelessSettingsController")
SFSessionCache = _Class("SFSessionCache")
SFAirDropNode = _Class("SFAirDropNode")
SFAirDropBrowser = _Class("SFAirDropBrowser")
SFAppleIDValidationRecord = _Class("SFAppleIDValidationRecord")
SFPeerDevice = _Class("SFPeerDevice")
SFAutoUnlockDevice = _Class("SFAutoUnlockDevice")
SFAirDropTransferItem = _Class("SFAirDropTransferItem")
SFXPCClient = _Class("SFXPCClient")
SFActivityAdvertiser = _Class("SFActivityAdvertiser")
SFAirDropClassroomTransferManager = _Class("SFAirDropClassroomTransferManager")
SFContinuityScanManager = _Class("SFContinuityScanManager")
SFChargingUICoordinator = _Class("SFChargingUICoordinator")
SFAirDropTransferObserver = _Class("SFAirDropTransferObserver")
SFSettings = _Class("SFSettings")
SFMagicHeadSettings = _Class("SFMagicHeadSettings")
SFSettingsDomain = _Class("SFSettingsDomain")
