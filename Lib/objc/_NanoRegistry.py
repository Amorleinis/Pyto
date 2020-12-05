"""
Classes from the 'NanoRegistry' framework.
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


NRLoggingXPCProxy = _Class("NRLoggingXPCProxy")
NRMockXPCProxy = _Class("NRMockXPCProxy")
NRDevicePropertyDiffType = _Class("NRDevicePropertyDiffType")
NRSystemVersionRequest = _Class("NRSystemVersionRequest")
NRBypassQueue = _Class("NRBypassQueue")
NRConnectivitySubscriber = _Class("NRConnectivitySubscriber")
NRClientInfo = _Class("NRClientInfo")
NRTextFormattingUtilities = _Class("NRTextFormattingUtilities")
NRMagicSwitchHelper = _Class("NRMagicSwitchHelper")
NRDevice = _Class("NRDevice")
NRDeviceDiffType = _Class("NRDeviceDiffType")
NRActiveDeviceAssertionMonitor = _Class("NRActiveDeviceAssertionMonitor")
NRActiveDeviceAssertion = _Class("NRActiveDeviceAssertion")
NRSecureDevicePropertyStore = _Class("NRSecureDevicePropertyStore")
NRSecureDevicePropertyID = _Class("NRSecureDevicePropertyID")
NRDataFileHistoryHelpers = _Class("NRDataFileHistoryHelpers")
NRDeviceCollectionHistory = _Class("NRDeviceCollectionHistory")
NRDeviceCollectionHistoryObserverWrapper = _Class(
    "NRDeviceCollectionHistoryObserverWrapper"
)
NRDeviceCollectionHistoryEntry = _Class("NRDeviceCollectionHistoryEntry")
NRServerRequestReporter = _Class("NRServerRequestReporter")
NRWatchPairingExtendedMetadata = _Class("NRWatchPairingExtendedMetadata")
NRMigrator = _Class("NRMigrator")
NRDeviceDiscoveryController = _Class("NRDeviceDiscoveryController")
NRPairingCompatibilityVersionInfo = _Class("NRPairingCompatibilityVersionInfo")
NRBlockQueueWrapper = _Class("NRBlockQueueWrapper")
NRMiniUUIDSet = _Class("NRMiniUUIDSet")
NRUnarchivedObjectVerifier = _Class("NRUnarchivedObjectVerifier")
NRDiffBase = _Class("NRDiffBase")
NRDeviceDiff = _Class("NRDeviceDiff")
NRDevicePropertyDiff = _Class("NRDevicePropertyDiff")
NRDeviceCollectionDiff = _Class("NRDeviceCollectionDiff")
NRMutableStateBase = _Class("NRMutableStateBase")
NRMutableDeviceCollection = _Class("NRMutableDeviceCollection")
NRMutableDeviceProperty = _Class("NRMutableDeviceProperty")
NRMutableDevice = _Class("NRMutableDevice")
NRMutableStateBaseObserverWrapper = _Class("NRMutableStateBaseObserverWrapper")
NRRegistry = _Class("NRRegistry")
NRRegistryHistoryStore = _Class("NRRegistryHistoryStore")
NRRegistryClient = _Class("NRRegistryClient")
NRPairedDeviceRegistry = _Class("NRPairedDeviceRegistry")
NRMockRegistryClient = _Class("NRMockRegistryClient")
NRRegistryQueryCompletionBlockEntry = _Class("NRRegistryQueryCompletionBlockEntry")
NRXPCProxy = _Class("NRXPCProxy")
NRRegistryProxy = _Class("NRRegistryProxy")
NRPairingProxy = _Class("NRPairingProxy")
NRReadWriteConcurrentQueue = _Class("NRReadWriteConcurrentQueue")
NRMockNSXPCListener = _Class("NRMockNSXPCListener")
NRMockServerNSXPCConnection = _Class("NRMockServerNSXPCConnection")
NRMockClientNSXPCConnection = _Class("NRMockClientNSXPCConnection")
NRNSXPCConnection = _Class("NRNSXPCConnection")
NRMockXPCStuff = _Class("NRMockXPCStuff")
NRTermsAcknowledgementRegistry = _Class("NRTermsAcknowledgementRegistry")
NRDataFilePaths = _Class("NRDataFilePaths")
NRPBDevicePropertyDiffType = _Class("NRPBDevicePropertyDiffType")
NRPBMutableDevice = _Class("NRPBMutableDevice")
NRPBDeviceDiff = _Class("NRPBDeviceDiff")
NRPBDevicePropertyDiff = _Class("NRPBDevicePropertyDiff")
NRPBDeviceDiffType = _Class("NRPBDeviceDiffType")
NRPBDeviceCollectionDiff = _Class("NRPBDeviceCollectionDiff")
NRPBCompressedData = _Class("NRPBCompressedData")
NRPBMigrationDeviceInfo = _Class("NRPBMigrationDeviceInfo")
NRPBProperty = _Class("NRPBProperty")
NRPBDeviceCollectionHistoryEntry = _Class("NRPBDeviceCollectionHistoryEntry")
NRPBMigrationDevices = _Class("NRPBMigrationDevices")
NRPBMutableDeviceCollection = _Class("NRPBMutableDeviceCollection")
NRPBMutableDeviceProperty = _Class("NRPBMutableDeviceProperty")
NRPBNumber = _Class("NRPBNumber")
NRPBSize = _Class("NRPBSize")
NRPBSwitchRecord = _Class("NRPBSwitchRecord")
NRSwitchRecord = _Class("NRSwitchRecord")
NRPBPropertyValue = _Class("NRPBPropertyValue")
NRPBSwitchRecordCollection = _Class("NRPBSwitchRecordCollection")
NRSwitchRecordCollection = _Class("NRSwitchRecordCollection")
NRPBDeviceCollectionHistory = _Class("NRPBDeviceCollectionHistory")
NRPBTermsEvent = _Class("NRPBTermsEvent")
NRTermsEvent = _Class("NRTermsEvent")
NRNSXPCListener = _Class("NRNSXPCListener")
NRKeyedUnarchiver = _Class("NRKeyedUnarchiver")
