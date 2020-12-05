"""
Classes from the 'StoreServices' framework.
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


SSVPlayActivityTable = _Class("SSVPlayActivityTable")
SSDoubleLinkedList = _Class("SSDoubleLinkedList")
SSVDirectUpload = _Class("SSVDirectUpload")
SSAuthorizationMetricsController = _Class("SSAuthorizationMetricsController")
SSVMediaSocialPostArtist = _Class("SSVMediaSocialPostArtist")
SSStackShot = _Class("SSStackShot")
SSUpdatableAssetController = _Class("SSUpdatableAssetController")
SSVSubscriptionEntitlementsCoordinator = _Class(
    "SSVSubscriptionEntitlementsCoordinator"
)
SSVStoreDownload = _Class("SSVStoreDownload")
SSDownloadMonitor = _Class("SSDownloadMonitor")
SSDownloadMonitorItem = _Class("SSDownloadMonitorItem")
SSCoalescingQueue = _Class("SSCoalescingQueue")
SSMetricsEventReportingSession = _Class("SSMetricsEventReportingSession")
SSWatchMetricsConfiguration = _Class("SSWatchMetricsConfiguration")
SSWatchMetricsController = _Class("SSWatchMetricsController")
SSPromiseCompletionBlocks = _Class("SSPromiseCompletionBlocks")
SSVGratisRequestBody = _Class("SSVGratisRequestBody")
SSVStoreDownloadQueueResponse = _Class("SSVStoreDownloadQueueResponse")
SSVFairPlaySAPSession = _Class("SSVFairPlaySAPSession")
SSBagKey = _Class("SSBagKey")
SSSimulatedCrash = _Class("SSSimulatedCrash")
asn1ReceiptToken = _Class("asn1ReceiptToken")
SSWishlistDatabaseSchema = _Class("SSWishlistDatabaseSchema")
SSVPlayActivityEventItemIDs = _Class("SSVPlayActivityEventItemIDs")
SSVMutablePlayActivityEventItemIDs = _Class("SSVMutablePlayActivityEventItemIDs")
SSVDialogResponse = _Class("SSVDialogResponse")
SSWishlist = _Class("SSWishlist")
SSPlistCacheObject = _Class("SSPlistCacheObject")
SSPlistCacheObjectFactory = _Class("SSPlistCacheObjectFactory")
SSCacheObjectStore = _Class("SSCacheObjectStore")
SSAppIconDatabaseCache = _Class("SSAppIconDatabaseCache")
SSVMediaSocialAdminStatus = _Class("SSVMediaSocialAdminStatus")
SSVSAPSignatureDataSource = _Class("SSVSAPSignatureDataSource")
SSUpdatableAssetCacheManager = _Class("SSUpdatableAssetCacheManager")
SSAppPurchaseHistoryCache = _Class("SSAppPurchaseHistoryCache")
SSBiometrics = _Class("SSBiometrics")
SSPersistentCache = _Class("SSPersistentCache")
SSObservable = _Class("SSObservable")
SSDatabaseCache = _Class("SSDatabaseCache")
SSVRedeemCodeItem = _Class("SSVRedeemCodeItem")
SSVRedeemCodeMetadata = _Class("SSVRedeemCodeMetadata")
SSPurchasableItem = _Class("SSPurchasableItem")
SSPurchasableAppItem = _Class("SSPurchasableAppItem")
SSAppPurchaseHistoryTransaction = _Class("SSAppPurchaseHistoryTransaction")
SSVPlatformContext = _Class("SSVPlatformContext")
SSAppPurchaseHistoryDatabaseSchema = _Class("SSAppPurchaseHistoryDatabaseSchema")
SSAppPurchaseHistoryDatabase = _Class("SSAppPurchaseHistoryDatabase")
SSVFairPlaySubscriptionController = _Class("SSVFairPlaySubscriptionController")
SSVPlayActivityEventContainerIDs = _Class("SSVPlayActivityEventContainerIDs")
SSVMutablePlayActivityEventContainerIDs = _Class(
    "SSVMutablePlayActivityEventContainerIDs"
)
SSSoftwareUpdate = _Class("SSSoftwareUpdate")
SSVDirectUploadQueue = _Class("SSVDirectUploadQueue")
SSVPlayActivityEnqueuerProperties = _Class("SSVPlayActivityEnqueuerProperties")
SSVMutablePlayActivityEnqueuerProperties = _Class(
    "SSVMutablePlayActivityEnqueuerProperties"
)
SSVPushNotificationParameters = _Class("SSVPushNotificationParameters")
SSFamilyCircleResponse = _Class("SSFamilyCircleResponse")
SSVPlaybackLeaseConfiguration = _Class("SSVPlaybackLeaseConfiguration")
SSSoftwareUpdatesStore = _Class("SSSoftwareUpdatesStore")
SSVMediaSocialAdminPermissionsCoordinator = _Class(
    "SSVMediaSocialAdminPermissionsCoordinator"
)
SSLookupItemOffer = _Class("SSLookupItemOffer")
SSVFairPlaySubscriptionStatus = _Class("SSVFairPlaySubscriptionStatus")
SSURLSessionManager = _Class("SSURLSessionManager")
SSLookupItemArtwork = _Class("SSLookupItemArtwork")
SSPaymentSheetPriceSectionItem = _Class("SSPaymentSheetPriceSectionItem")
SSUpdatableAssetManifestJSONParser = _Class("SSUpdatableAssetManifestJSONParser")
SSVSubscriptionStatus = _Class("SSVSubscriptionStatus")
SSLookupItem = _Class("SSLookupItem")
SSVMediaSocialPostAttachment = _Class("SSVMediaSocialPostAttachment")
SSTermsAndConditions = _Class("SSTermsAndConditions")
SSVSubscriptionEntitlements = _Class("SSVSubscriptionEntitlements")
SSMetricsEventLocation = _Class("SSMetricsEventLocation")
SSPurchaseManager = _Class("SSPurchaseManager")
_SSVPlayActivityFlushSessionInformation = _Class(
    "_SSVPlayActivityFlushSessionInformation"
)
_SSVPlayActivityEndpointRevisionInformation = _Class(
    "_SSVPlayActivityEndpointRevisionInformation"
)
SSVPlayActivityController = _Class("SSVPlayActivityController")
SSHTTPServerRequestHandler = _Class("SSHTTPServerRequestHandler")
SSVServerAuthenticateResponse = _Class("SSVServerAuthenticateResponse")
SSPurchaseResponse = _Class("SSPurchaseResponse")
SSMemoryEntity = _Class("SSMemoryEntity")
SSSQLiteQueryDescriptor = _Class("SSSQLiteQueryDescriptor")
SSSQLiteQuery = _Class("SSSQLiteQuery")
SSSQLitePredicate = _Class("SSSQLitePredicate")
SSSQLiteCompoundPredicate = _Class("SSSQLiteCompoundPredicate")
SSSQLitePropertyPredicate = _Class("SSSQLitePropertyPredicate")
SSSQLiteNullPredicate = _Class("SSSQLiteNullPredicate")
SSSQLiteContainsPredicate = _Class("SSSQLiteContainsPredicate")
SSSQLiteComparisonPredicate = _Class("SSSQLiteComparisonPredicate")
SSVPlayActivityEvent = _Class("SSVPlayActivityEvent")
SSVMutablePlayActivityEvent = _Class("SSVMutablePlayActivityEvent")
SSSQLiteDatabase = _Class("SSSQLiteDatabase")
SSUnitTests = _Class("SSUnitTests")
SSVMediaSocialPostExternalDestination = _Class("SSVMediaSocialPostExternalDestination")
SSMetricsTimingDefaults = _Class("SSMetricsTimingDefaults")
SSUpdatableAsset = _Class("SSUpdatableAsset")
SSKeyValueStoreSession = _Class("SSKeyValueStoreSession")
SSKeyValueStoreTransaction = _Class("SSKeyValueStoreTransaction")
SSKeyValueStoreSchema = _Class("SSKeyValueStoreSchema")
SSKeyValueStoreDatabase = _Class("SSKeyValueStoreDatabase")
SSErrorHandlerSession = _Class("SSErrorHandlerSession")
SSHTTPArchive = _Class("SSHTTPArchive")
SSFeatureEnablerMigrator = _Class("SSFeatureEnablerMigrator")
ISPurchaseReceipt = _Class("ISPurchaseReceipt")
SSErrorHandler = _Class("SSErrorHandler")
SSCircularBuffer = _Class("SSCircularBuffer")
SSDoubleLinkedListNode = _Class("SSDoubleLinkedListNode")
SSLRUCacheItem = _Class("SSLRUCacheItem")
SSLRUCache = _Class("SSLRUCache")
SSKeyValueStore = _Class("SSKeyValueStore")
SSRedeemCodesResponse = _Class("SSRedeemCodesResponse")
asn1Token = _Class("asn1Token")
asn1OSToken = _Class("asn1OSToken")
asn1IntegerToken = _Class("asn1IntegerToken")
asn1SequenceToken = _Class("asn1SequenceToken")
asn1SetToken = _Class("asn1SetToken")
SSVPlaybackLease = _Class("SSVPlaybackLease")
SSVPlaybackLeaseCallback = _Class("SSVPlaybackLeaseCallback")
SSVMediaSocialShareExtension = _Class("SSVMediaSocialShareExtension")
SSSoftwareLibrary = _Class("SSSoftwareLibrary")
SSSoftwareLibraryItem = _Class("SSSoftwareLibraryItem")
SSPaymentSheet = _Class("SSPaymentSheet")
SSDownloadPolicy = _Class("SSDownloadPolicy")
SSDownloadPolicyRule = _Class("SSDownloadPolicyRule")
SSFamilyMember = _Class("SSFamilyMember")
SSFamilyCircle = _Class("SSFamilyCircle")
SSDownloadPolicyApplicationState = _Class("SSDownloadPolicyApplicationState")
SSLogConfig = _Class("SSLogConfig")
SSMutableLogConfig = _Class("SSMutableLogConfig")
SSLookupResponse = _Class("SSLookupResponse")
SSLookupProperties = _Class("SSLookupProperties")
SSWeakReference = _Class("SSWeakReference")
SSVCookieKey = _Class("SSVCookieKey")
SSVMediaContentTasteItem = _Class("SSVMediaContentTasteItem")
SSVMutableMediaContentTasteItem = _Class("SSVMutableMediaContentTasteItem")
SSEventMonitor = _Class("SSEventMonitor")
SSDownloadFileManifest = _Class("SSDownloadFileManifest")
SSVFairPlaySAPContext = _Class("SSVFairPlaySAPContext")
SSRollableLog = _Class("SSRollableLog")
SSDistributedNotificationCenterObserver = _Class(
    "SSDistributedNotificationCenterObserver"
)
SSDistributedNotificationCenter = _Class("SSDistributedNotificationCenter")
SSXPCServerObserver = _Class("SSXPCServerObserver")
SSXPCServer = _Class("SSXPCServer")
SSPurchaseHistoryItem = _Class("SSPurchaseHistoryItem")
SSRestoreContentItem = _Class("SSRestoreContentItem")
SSPreorderManager = _Class("SSPreorderManager")
SSPreorder = _Class("SSPreorder")
SSPersonalizeOffersResponse = _Class("SSPersonalizeOffersResponse")
SSFollowUpController = _Class("SSFollowUpController")
SSDownloadAuthenticationChallengeSender = _Class(
    "SSDownloadAuthenticationChallengeSender"
)
SSDownloadSession = _Class("SSDownloadSession")
SSDownloadAuthenticationSession = _Class("SSDownloadAuthenticationSession")
SSDownloadHandlerSession = _Class("SSDownloadHandlerSession")
SSAuthenticationResponse = _Class("SSAuthenticationResponse")
SSVPlaybackLeaseRequest = _Class("SSVPlaybackLeaseRequest")
SSVPlaybackKDLeaseRequest = _Class("SSVPlaybackKDLeaseRequest")
SSVPlaybackSubscriptionLeaseRequest = _Class("SSVPlaybackSubscriptionLeaseRequest")
SSResponseAction = _Class("SSResponseAction")
SSDictionaryResponse = _Class("SSDictionaryResponse")
SSScriptURLHandler = _Class("SSScriptURLHandler")
SSDownloadHandler = _Class("SSDownloadHandler")
SSConsolidatedDialog = _Class("SSConsolidatedDialog")
SSVTelephonyController = _Class("SSVTelephonyController")
SSSilentEnrollmentContext = _Class("SSSilentEnrollmentContext")
SSDownloadManagerOptions = _Class("SSDownloadManagerOptions")
SSXPCConnection = _Class("SSXPCConnection")
SSBiometricAuthenticationContext = _Class("SSBiometricAuthenticationContext")
SSVPlayActivityFeedSerialization = _Class("SSVPlayActivityFeedSerialization")
SSUpdateAccountResponse = _Class("SSUpdateAccountResponse")
SSItemContentRating = _Class("SSItemContentRating")
SSUpdatableAssetManifest = _Class("SSUpdatableAssetManifest")
SSURLBagContext = _Class("SSURLBagContext")
SSSQLiteEntity = _Class("SSSQLiteEntity")
SSMetricsEventTableEntity = _Class("SSMetricsEventTableEntity")
SSWishlistItemEntity = _Class("SSWishlistItemEntity")
SSDatabaseCacheEntry = _Class("SSDatabaseCacheEntry")
SSAppImageDatabaseCacheEntry = _Class("SSAppImageDatabaseCacheEntry")
SSWatchMetricsEventTableEntity = _Class("SSWatchMetricsEventTableEntity")
SSAppPurchaseHistoryEntry = _Class("SSAppPurchaseHistoryEntry")
SSKeyValueStoreValueEntity = _Class("SSKeyValueStoreValueEntity")
SSAppPurchaseHistoryAccount = _Class("SSAppPurchaseHistoryAccount")
SSURLDataCollection = _Class("SSURLDataCollection")
SSRemoteNotification = _Class("SSRemoteNotification")
SSRemoteNotificationClient = _Class("SSRemoteNotificationClient")
SSItemImageCollection = _Class("SSItemImageCollection")
SSVSAPSignatureComponent = _Class("SSVSAPSignatureComponent")
SSVSAPSignaturePolicy = _Class("SSVSAPSignaturePolicy")
SSItemArtworkImage = _Class("SSItemArtworkImage")
SSPurchaseReceipt = _Class("SSPurchaseReceipt")
SSDialogButton = _Class("SSDialogButton")
SSDialog = _Class("SSDialog")
SSNetworkQualityInquiry = _Class("SSNetworkQualityInquiry")
SSMigrator = _Class("SSMigrator")
SSVPlaybackItem = _Class("SSVPlaybackItem")
SSVPlaybackLeaseItem = _Class("SSVPlaybackLeaseItem")
SSPlayInfoResponse = _Class("SSPlayInfoResponse")
SSPlayInfoRequestContext = _Class("SSPlayInfoRequestContext")
SSURLConnectionResponse = _Class("SSURLConnectionResponse")
SSVSubscriptionResponse = _Class("SSVSubscriptionResponse")
SSURLRequestProperties = _Class("SSURLRequestProperties")
SSMutableURLRequestProperties = _Class("SSMutableURLRequestProperties")
SSVGratisApplication = _Class("SSVGratisApplication")
SSDownloadPolicyUserDefaultState = _Class("SSDownloadPolicyUserDefaultState")
SSLockdown = _Class("SSLockdown")
SSDevice = _Class("SSDevice")
SSProtocolConditionalContext = _Class("SSProtocolConditionalContext")
SSProtocolConditionalEvaluator = _Class("SSProtocolConditionalEvaluator")
SSProtocolCondition = _Class("SSProtocolCondition")
SSSystemVersionCondition = _Class("SSSystemVersionCondition")
SSRestrictionCondition = _Class("SSRestrictionCondition")
SSPlatformCondition = _Class("SSPlatformCondition")
SSItemAvailableCondition = _Class("SSItemAvailableCondition")
SSHasAccountCondition = _Class("SSHasAccountCondition")
SSDocumentCondition = _Class("SSDocumentCondition")
SSCapabilityCondition = _Class("SSCapabilityCondition")
SSApplicationVersionCondition = _Class("SSApplicationVersionCondition")
SSNetworkConstraints = _Class("SSNetworkConstraints")
SSDownloadManager = _Class("SSDownloadManager")
SSDownloadManagerAppShim = _Class("SSDownloadManagerAppShim")
SSDownloadManagerBookShim = _Class("SSDownloadManagerBookShim")
SSDownloadManagerBookShim2 = _Class("SSDownloadManagerBookShim2")
SSItemOfferDeviceError = _Class("SSItemOfferDeviceError")
SSItemOfferDevice = _Class("SSItemOfferDevice")
SSItemOffer = _Class("SSItemOffer")
SSTransactionStore = _Class("SSTransactionStore")
SSBinaryPromise = _Class("SSBinaryPromise")
SSBagProfileConfig = _Class("SSBagProfileConfig")
SSMutableBagProfileConfig = _Class("SSMutableBagProfileConfig")
SSPromise = _Class("SSPromise")
SSLazyPromise = _Class("SSLazyPromise")
SSVCloudServiceAPITokenResponse = _Class("SSVCloudServiceAPITokenResponse")
SSEventsTableBase = _Class("SSEventsTableBase")
SSWatchMetricsEventTable = _Class("SSWatchMetricsEventTable")
SSMetricsEventTable = _Class("SSMetricsEventTable")
SSBag = _Class("SSBag")
SSMetricsController = _Class("SSMetricsController")
SSMetricsEventController = _Class("SSMetricsEventController")
SSSoftwareUpdatesResponse = _Class("SSSoftwareUpdatesResponse")
SSSoftwareUpdatesContext = _Class("SSSoftwareUpdatesContext")
SSMutableSoftwareUpdatesContext = _Class("SSMutableSoftwareUpdatesContext")
SSRestrictions = _Class("SSRestrictions")
SSWatchMetricsEventsController = _Class("SSWatchMetricsEventsController")
SSAuthenticateResponse = _Class("SSAuthenticateResponse")
SSAccountStore = _Class("SSAccountStore")
SSVMediaContentTasteUpdateResponse = _Class("SSVMediaContentTasteUpdateResponse")
SSVMediaSocialPostItem = _Class("SSVMediaSocialPostItem")
SSPromiseResult = _Class("SSPromiseResult")
SSMetricsConfiguration = _Class("SSMetricsConfiguration")
SSSpringBoardUtility = _Class("SSSpringBoardUtility")
SSPaymentSheetRatingImage = _Class("SSPaymentSheetRatingImage")
SSAuthenticationContext = _Class("SSAuthenticationContext")
SSMutableAuthenticationContext = _Class("SSMutableAuthenticationContext")
SSAccount = _Class("SSAccount")
SSAppWakeRequest = _Class("SSAppWakeRequest")
SSWatchMetricsEvent = _Class("SSWatchMetricsEvent")
SSItemMedia = _Class("SSItemMedia")
SSItem = _Class("SSItem")
SSVAppleAccountStore = _Class("SSVAppleAccountStore")
SSPurchase = _Class("SSPurchase")
SSTonePurchase = _Class("SSTonePurchase")
SSRingtonePurchase = _Class("SSRingtonePurchase")
SSObserver = _Class("SSObserver")
SSVURLBagInterpreter = _Class("SSVURLBagInterpreter")
SSVURLDataConsumer = _Class("SSVURLDataConsumer")
SSVURLProtocolConsumer = _Class("SSVURLProtocolConsumer")
SSVURLJSONDataConsumer = _Class("SSVURLJSONDataConsumer")
SSVURLLookupResponseConsumer = _Class("SSVURLLookupResponseConsumer")
SSVURLConnectionConsumer = _Class("SSVURLConnectionConsumer")
SSVMediaContentTasteController = _Class("SSVMediaContentTasteController")
SSVSubscriptionEntitlementsSubscription = _Class(
    "SSVSubscriptionEntitlementsSubscription"
)
SSUniqueExecutionQueue = _Class("SSUniqueExecutionQueue")
SSDownloadManifestResponse = _Class("SSDownloadManifestResponse")
SSVURLCacheConfiguration = _Class("SSVURLCacheConfiguration")
SSVURLCache = _Class("SSVURLCache")
SSVPlaybackResponse = _Class("SSVPlaybackResponse")
SSVPlaybackLeaseResponse = _Class("SSVPlaybackLeaseResponse")
SSLogFileOptions = _Class("SSLogFileOptions")
SSOperationProgress = _Class("SSOperationProgress")
SSDownloadPhase = _Class("SSDownloadPhase")
SSDownloadStatus = _Class("SSDownloadStatus")
SSVMediaContentTasteItemUpdate = _Class("SSVMediaContentTasteItemUpdate")
SSRequest = _Class("SSRequest")
SSImportDownloadToIPodLibraryRequest = _Class("SSImportDownloadToIPodLibraryRequest")
SSPurchaseIntentActionRequest = _Class("SSPurchaseIntentActionRequest")
SSVApplicationCapabilitiesRequest = _Class("SSVApplicationCapabilitiesRequest")
SSPushNotificationTokenRequest = _Class("SSPushNotificationTokenRequest")
SSVShowDialogRequest = _Class("SSVShowDialogRequest")
SSWishlistAddItemsRequest = _Class("SSWishlistAddItemsRequest")
SSVMediaSocialPostRequest = _Class("SSVMediaSocialPostRequest")
SSVClaimApplicationsRequest = _Class("SSVClaimApplicationsRequest")
SSVCloudServiceCapabilitiesRequest = _Class("SSVCloudServiceCapabilitiesRequest")
SSRentalSyncRequest = _Class("SSRentalSyncRequest")
SSFamilyCircleRequest = _Class("SSFamilyCircleRequest")
SSMachineDataRequest = _Class("SSMachineDataRequest")
SSInstallAttributionPingbackRequest = _Class("SSInstallAttributionPingbackRequest")
SSVServerAuthenticateRequest = _Class("SSVServerAuthenticateRequest")
SSVEnableSubscriptionRequest = _Class("SSVEnableSubscriptionRequest")
SSVSubscriptionStatusRequest = _Class("SSVSubscriptionStatusRequest")
SSVKeybagSyncRequest = _Class("SSVKeybagSyncRequest")
SSRedeemCodesRequest = _Class("SSRedeemCodesRequest")
SSKeybagRequest = _Class("SSKeybagRequest")
SSLookupRequest = _Class("SSLookupRequest")
SSVMediaContentTasteUpdateRequest = _Class("SSVMediaContentTasteUpdateRequest")
SSVDisableSubscriptionRequest = _Class("SSVDisableSubscriptionRequest")
SSRentalInformationRequest = _Class("SSRentalInformationRequest")
SSPersonalizeOffersRequest = _Class("SSPersonalizeOffersRequest")
SSVInstallManagedApplicationRequest = _Class("SSVInstallManagedApplicationRequest")
SSRentalCheckinRequest = _Class("SSRentalCheckinRequest")
SSAskPermissionActionRequest = _Class("SSAskPermissionActionRequest")
SSSilentEnrollment = _Class("SSSilentEnrollment")
SSSilentEnrollmentVerification = _Class("SSSilentEnrollmentVerification")
SSSilentEnrollmentPaymentSession = _Class("SSSilentEnrollmentPaymentSession")
SSAuthorizationRequest = _Class("SSAuthorizationRequest")
SSPlayInfoRequest = _Class("SSPlayInfoRequest")
SSVCloudServiceAPITokenRequest = _Class("SSVCloudServiceAPITokenRequest")
SSVPushNotificationRequest = _Class("SSVPushNotificationRequest")
SSSoftwareUpdatesRequest = _Class("SSSoftwareUpdatesRequest")
SSVRepairApplicationRequest = _Class("SSVRepairApplicationRequest")
SSAuthenticateRequest = _Class("SSAuthenticateRequest")
SSRemoteWebViewRequest = _Class("SSRemoteWebViewRequest")
SSRentalCheckoutRequest = _Class("SSRentalCheckoutRequest")
SSItemLookupRequest = _Class("SSItemLookupRequest")
SSURLConnectionRequest = _Class("SSURLConnectionRequest")
SSPurchaseRequest = _Class("SSPurchaseRequest")
SSInstallAttributionParamsRequest = _Class("SSInstallAttributionParamsRequest")
SSDownloadManifestRequest = _Class("SSDownloadManifestRequest")
SSVRefreshSubscriptionRequest = _Class("SSVRefreshSubscriptionRequest")
SSVDownloadQueueRequest = _Class("SSVDownloadQueueRequest")
SSVSubscriptionStatusCoordinator = _Class("SSVSubscriptionStatusCoordinator")
SSVCloudServiceCapabilitiesResponse = _Class("SSVCloudServiceCapabilitiesResponse")
SSDownloadMetadata = _Class("SSDownloadMetadata")
SSVContentLink = _Class("SSVContentLink")
SSEntity = _Class("SSEntity")
SSDownloadAsset = _Class("SSDownloadAsset")
SSDownload = _Class("SSDownload")
SSSoftwareDownload = _Class("SSSoftwareDownload")
SSBookDownload = _Class("SSBookDownload")
SSDivertedDownload = _Class("SSDivertedDownload")
SSVMediaSocialPostDescription = _Class("SSVMediaSocialPostDescription")
SSDownloadQueue = _Class("SSDownloadQueue")
SSVFamilyAccountPair = _Class("SSVFamilyAccountPair")
SSVFamilyContentDeletionEvent = _Class("SSVFamilyContentDeletionEvent")
SSVPlaybackAsset = _Class("SSVPlaybackAsset")
SSVPlaybackLeaseAsset = _Class("SSVPlaybackLeaseAsset")
SSApplicationUtil = _Class("SSApplicationUtil")
SSPrivacyController = _Class("SSPrivacyController")
SSMetricsEvent = _Class("SSMetricsEvent")
SSMetricsMutableEvent = _Class("SSMetricsMutableEvent")
SSMetricsLogEvent = _Class("SSMetricsLogEvent")
SSMetricsAppInstallEvent = _Class("SSMetricsAppInstallEvent")
SSMetricsLoadURLEvent = _Class("SSMetricsLoadURLEvent")
SSPrivacyMetricsEvent = _Class("SSPrivacyMetricsEvent")
SSMetricsCustomEvent = _Class("SSMetricsCustomEvent")
SSMetricsBaseEvent = _Class("SSMetricsBaseEvent")
SSMetricsSearchEvent = _Class("SSMetricsSearchEvent")
SSMetricsMediaEvent = _Class("SSMetricsMediaEvent")
SSMetricsImpressionsEvent = _Class("SSMetricsImpressionsEvent")
SSMetricsExitEvent = _Class("SSMetricsExitEvent")
SSMetricsEnterEvent = _Class("SSMetricsEnterEvent")
SSMetricsClickEvent = _Class("SSMetricsClickEvent")
SSMetricsPurchaseEvent = _Class("SSMetricsPurchaseEvent")
SSMetricsAccountEvent = _Class("SSMetricsAccountEvent")
SSMetricsPageEvent = _Class("SSMetricsPageEvent")
SSMetricsDialogEvent = _Class("SSMetricsDialogEvent")
SSHTTPServerResponse = _Class("SSHTTPServerResponse")
SSHTTPServer = _Class("SSHTTPServer")
SSKeychain = _Class("SSKeychain")
SSVCookieStorage = _Class("SSVCookieStorage")
SSURLBag = _Class("SSURLBag")
SSVPBPlayActivityEvent = _Class("SSVPBPlayActivityEvent")
SSVPBPlayActivityEnqueuerProperties = _Class("SSVPBPlayActivityEnqueuerProperties")
SSVBarrierOperationQueue = _Class("SSVBarrierOperationQueue")
SSVPlatformRequestOperation = _Class("SSVPlatformRequestOperation")
SSVPlayActivityDebugLogOperation = _Class("SSVPlayActivityDebugLogOperation")
SSVLoadNearbyAppsOperation = _Class("SSVLoadNearbyAppsOperation")
SSVOperation = _Class("SSVOperation")
SSVLeaseRequestOperation = _Class("SSVLeaseRequestOperation")
SSVComplexOperation = _Class("SSVComplexOperation")
SSVMediaSocialAdminStatusOperation = _Class("SSVMediaSocialAdminStatusOperation")
SSVAccountLessPlaybackOperation = _Class("SSVAccountLessPlaybackOperation")
SSVLeaseCertificateRequestOperation = _Class("SSVLeaseCertificateRequestOperation")
SSVLoadDownloadQueueOperation = _Class("SSVLoadDownloadQueueOperation")
SSVRefreshStoreQueueDownloadOperation = _Class("SSVRefreshStoreQueueDownloadOperation")
SSVLoadURLOperation = _Class("SSVLoadURLOperation")
SSVSecureKeyDeliveryRequestOperation = _Class("SSVSecureKeyDeliveryRequestOperation")
SSGzipOutputStream = _Class("SSGzipOutputStream")
SSXPCData = _Class("SSXPCData")
