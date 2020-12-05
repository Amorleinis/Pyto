"""
Classes from the 'ContactsFoundation' framework.
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


CNWeakProxy = _Class("CNWeakProxy")
CNDispatchSource = _Class("CNDispatchSource")
CNString = _Class("CNString")
_CNForkJoinProgressiveResultObservationStrategy = _Class(
    "_CNForkJoinProgressiveResultObservationStrategy"
)
_CNForkJoinWhenCompleteResultObservationStrategy = _Class(
    "_CNForkJoinWhenCompleteResultObservationStrategy"
)
CNCFPreferencesPrimitiveUserDefaults = _Class("CNCFPreferencesPrimitiveUserDefaults")
CNHandleStringClassifier = _Class("CNHandleStringClassifier")
_CNCombinedBufferingStrategy = _Class("_CNCombinedBufferingStrategy")
_CNTemporalBufferingStrategy = _Class("_CNTemporalBufferingStrategy")
_CNSpatialBufferingStrategy = _Class("_CNSpatialBufferingStrategy")
_CNBufferingStrategy = _Class("_CNBufferingStrategy")
CNDate = _Class("CNDate")
_CNInlineScheduler = _Class("_CNInlineScheduler")
CNFamilyMember = _Class("CNFamilyMember")
CNObserver = _Class("CNObserver")
CNLaunchServices = _Class("CNLaunchServices")
CNDebugHelper = _Class("CNDebugHelper")
_CNAmbObserver = _Class("_CNAmbObserver")
CNURLSessionFactory = _Class("CNURLSessionFactory")
CNDateHelper = _Class("CNDateHelper")
CNLaunchServicesLocalAdapter = _Class("CNLaunchServicesLocalAdapter")
CNHeap = _Class("CNHeap")
CNHeapObject = _Class("CNHeapObject")
CNObjCClass = _Class("CNObjCClass")
CNEqualsBuilder = _Class("CNEqualsBuilder")
CNObjCRuntimeAPI = _Class("CNObjCRuntimeAPI")
_CNRegExHandleStringClassificationStrategy = _Class(
    "_CNRegExHandleStringClassificationStrategy"
)
_CNFlatMapInnerSubscriptionContext = _Class("_CNFlatMapInnerSubscriptionContext")
_CNFlatMapSubscriptionContext = _Class("_CNFlatMapSubscriptionContext")
CNSchedulerProvider = _Class("CNSchedulerProvider")
CNEnvironment = _Class("CNEnvironment")
CNFoundationError = _Class("CNFoundationError")
_CNAssistedDataDetectorsHandleStringClassificationStrategy = _Class(
    "_CNAssistedDataDetectorsHandleStringClassificationStrategy"
)
_CNDataDetectorsHandleStringClassificationStrategy = _Class(
    "_CNDataDetectorsHandleStringClassificationStrategy"
)
_CNJumpToMainRunLoopScheduler = _Class("_CNJumpToMainRunLoopScheduler")
CNDescriptionBuilder = _Class("CNDescriptionBuilder")
CNEmailAddressUtilities = _Class("CNEmailAddressUtilities")
CNProcessSharedLock = _Class("CNProcessSharedLock")
CNBundleIdentifierUtilities = _Class("CNBundleIdentifierUtilities")
CNACAccountProvider = _Class("CNACAccountProvider")
_CNACAccountStaticProvider = _Class("_CNACAccountStaticProvider")
_CNACAccountStoreBasedProvider = _Class("_CNACAccountStoreBasedProvider")
CNNameComponentsStringTokenizer = _Class("CNNameComponentsStringTokenizer")
_CNTimeProfilingTaskOSLogger = _Class("_CNTimeProfilingTaskOSLogger")
CNPostalAddressStringTokenizer = _Class("CNPostalAddressStringTokenizer")
_CNKeyValueObserverHandler = _Class("_CNKeyValueObserverHandler")
CNStringRangeFinder = _Class("CNStringRangeFinder")
CNXPC = _Class("CNXPC")
CNXPCListenerDelegate = _Class("CNXPCListenerDelegate")
_CNBufferedObserver = _Class("_CNBufferedObserver")
CNAtomicUnsignedIntegerGenerator = _Class("CNAtomicUnsignedIntegerGenerator")
CNHandleStringsClassificationBuilder = _Class("CNHandleStringsClassificationBuilder")
CNHandleStringClassification = _Class("CNHandleStringClassification")
CNDictionaryPrimitiveUserDefaults = _Class("CNDictionaryPrimitiveUserDefaults")
CNFutureTask = _Class("CNFutureTask")
CNVirtualReaderWriterScheduler = _Class("CNVirtualReaderWriterScheduler")
CNPromise = _Class("CNPromise")
CNFuture = _Class("CNFuture")
CNArchiver = _Class("CNArchiver")
_CNObservableTakeUntilSignalObserver = _Class("_CNObservableTakeUntilSignalObserver")
CNFamilyCircleAccountSource = _Class("CNFamilyCircleAccountSource")
_CNQueueScheduler = _Class("_CNQueueScheduler")
CNCoalescingSchedulerDecorator = _Class("CNCoalescingSchedulerDecorator")
CNMobileKeyBag = _Class("CNMobileKeyBag")
CNAuditToken = _Class("CNAuditToken")
CNFoundationUserDefaults = _Class("CNFoundationUserDefaults")
_CNObservableEventBufferingStrategy = _Class("_CNObservableEventBufferingStrategy")
_CNObservableEventStaticArrayBufferingStrategy = _Class(
    "_CNObservableEventStaticArrayBufferingStrategy"
)
_CNObservableEventDynamicQueueBufferingStrategy = _Class(
    "_CNObservableEventDynamicQueueBufferingStrategy"
)
CNUnfairLock = _Class("CNUnfairLock")
CNTracedLogger = _Class("CNTracedLogger")
CNUsageReporting = _Class("CNUsageReporting")
_CNSortsByPositionInAuxiliaryArray = _Class("_CNSortsByPositionInAuxiliaryArray")
CNPostalAddressFormats = _Class("CNPostalAddressFormats")
CNChildDelegateAccountsStore = _Class("CNChildDelegateAccountsStore")
CNNameStringTokenizer = _Class("CNNameStringTokenizer")
CNMultiDictionary = _Class("CNMultiDictionary")
CNMutableMultiDictionary = _Class("CNMutableMultiDictionary")
_CNObservableSkipUntilSignalObserver = _Class("_CNObservableSkipUntilSignalObserver")
CNTimeProfilingSchedulerDecorator = _Class("CNTimeProfilingSchedulerDecorator")
CNTimestamped = _Class("CNTimestamped")
CNAbsoluteTimestamped = _Class("CNAbsoluteTimestamped")
CNRelativeTimestamped = _Class("CNRelativeTimestamped")
CNDeviceFirstUnlock = _Class("CNDeviceFirstUnlock")
CNSuspendableSchedulerDecorator = _Class("CNSuspendableSchedulerDecorator")
CNObservableEvent = _Class("CNObservableEvent")
_CNObservableFailureEvent = _Class("_CNObservableFailureEvent")
_CNObservableCompletionEvent = _Class("_CNObservableCompletionEvent")
_CNObservableResultEvent = _Class("_CNObservableResultEvent")
CNTCCFactory = _Class("CNTCCFactory")
CNPropertyListSerialization = _Class("CNPropertyListSerialization")
CNReplaySubjectCacheEntry = _Class("CNReplaySubjectCacheEntry")
CNAsynchronousCacheEntry = _Class("CNAsynchronousCacheEntry")
_CNCacheFixedCapacityBoundingStrategy = _Class("_CNCacheFixedCapacityBoundingStrategy")
CNFileManager = _Class("CNFileManager")
_CNJumpToMainQueueScheduler = _Class("_CNJumpToMainQueueScheduler")
CNTCCVersion2 = _Class("CNTCCVersion2")
CNHashBuilder = _Class("CNHashBuilder")
CNFutureCompletionBlocks = _Class("CNFutureCompletionBlocks")
CNFamilyCircle = _Class("CNFamilyCircle")
CNInhibitor = _Class("CNInhibitor")
_CNSuddenTerminationInhibitor = _Class("_CNSuddenTerminationInhibitor")
_CNOSTransactionInhibitor = _Class("_CNOSTransactionInhibitor")
CNObservableContractTerminationContext = _Class(
    "CNObservableContractTerminationContext"
)
CNObservableContractEnforcementPreferences = _Class(
    "CNObservableContractEnforcementPreferences"
)
CNObservableContractEnforcement = _Class("CNObservableContractEnforcement")
CNStringTokenizer = _Class("CNStringTokenizer")
CNAtomicToggle = _Class("CNAtomicToggle")
CNOrderedDictionary = _Class("CNOrderedDictionary")
CNMutableOrderedDictionary = _Class("CNMutableOrderedDictionary")
_CNBlockFutureImpl = _Class("_CNBlockFutureImpl")
CNStack = _Class("CNStack")
CNLoggingContext = _Class("CNLoggingContext")
CNLogging = _Class("CNLogging")
_CNBlockObserver = _Class("_CNBlockObserver")
CNObservableOperatorConcatenateResultObserver = _Class(
    "CNObservableOperatorConcatenateResultObserver"
)
CNObservableOperatorSwitchResultSequenceObserver = _Class(
    "CNObservableOperatorSwitchResultSequenceObserver"
)
CNObservableOperatorSwitchResultObserver = _Class(
    "CNObservableOperatorSwitchResultObserver"
)
CNAuthorizationContext = _Class("CNAuthorizationContext")
CNWeakReference = _Class("CNWeakReference")
CNAutomaticRetainCountWeakReference = _Class("CNAutomaticRetainCountWeakReference")
_CNOperationQueueScheduler = _Class("_CNOperationQueueScheduler")
CNUserDefaults = _Class("CNUserDefaults")
_CNInMemoryUserDefaults = _Class("_CNInMemoryUserDefaults")
CNPair = _Class("CNPair")
CNObservedResult = _Class("CNObservedResult")
CNObservedFailureResult = _Class("CNObservedFailureResult")
CNObservedCompletionResult = _Class("CNObservedCompletionResult")
CNBinarySemaphoreLock = _Class("CNBinarySemaphoreLock")
CNApplicationProxy = _Class("CNApplicationProxy")
CNTCCVersion1 = _Class("CNTCCVersion1")
_CNImmediateScheduler = _Class("_CNImmediateScheduler")
CNTestableObserver = _Class("CNTestableObserver")
CNCollationLanguage = _Class("CNCollationLanguage")
CNCollationSection = _Class("CNCollationSection")
CNCollationHeaderSection = _Class("CNCollationHeaderSection")
CNCollation = _Class("CNCollation")
CNTask = _Class("CNTask")
_CNAggregateTask = _Class("_CNAggregateTask")
CNEmailAddressSanitizationTask = _Class("CNEmailAddressSanitizationTask")
_CNBlockTask = _Class("_CNBlockTask")
CNFamilyCircleConfigurationUpdateTask = _Class("CNFamilyCircleConfigurationUpdateTask")
_CNTimeProfilingTask = _Class("_CNTimeProfilingTask")
CNEmailAddressScanner = _Class("CNEmailAddressScanner")
CNScheduler = _Class("CNScheduler")
CNFoundationSocialProfile = _Class("CNFoundationSocialProfile")
CNReaderWriterScheduler = _Class("CNReaderWriterScheduler")
CNCallStackRecordingSchedulerDecorator = _Class(
    "CNCallStackRecordingSchedulerDecorator"
)
CNObjCMethod = _Class("CNObjCMethod")
CNQualityOfServiceSchedulerDecorator = _Class("CNQualityOfServiceSchedulerDecorator")
CNEither = _Class("CNEither")
CNFileServices = _Class("CNFileServices")
CNFileUtilities = _Class("CNFileUtilities")
CNInhibitingSchedulerDecorator = _Class("CNInhibitingSchedulerDecorator")
_CNOffMainThreadScheduler = _Class("_CNOffMainThreadScheduler")
CNSocialProfileURLParser = _Class("CNSocialProfileURLParser")
_CNObservableTakeUntilInputObserver = _Class("_CNObservableTakeUntilInputObserver")
CNCoalescingTimer = _Class("CNCoalescingTimer")
CNBlockCountingSchedulerDecorator = _Class("CNBlockCountingSchedulerDecorator")
CNManagedConfiguration = _Class("CNManagedConfiguration")
CNManagedProfileConnection = _Class("CNManagedProfileConnection")
CNManagedAccountsCache = _Class("CNManagedAccountsCache")
CNVirtualScheduler = _Class("CNVirtualScheduler")
CNLocalization = _Class("CNLocalization")
CNCountdownLatch = _Class("CNCountdownLatch")
CNSimulatedCrashReporter = _Class("CNSimulatedCrashReporter")
CNPhoneNumberHelper = _Class("CNPhoneNumberHelper")
CNTCCAppAuthorizationRecord = _Class("CNTCCAppAuthorizationRecord")
_CNDataURLSessionTaskAdapter = _Class("_CNDataURLSessionTaskAdapter")
CNData = _Class("CNData")
CNCache = _Class("CNCache")
_CNMainThreadScheduler = _Class("_CNMainThreadScheduler")
_CNObservableSkipUntilInputObserver = _Class("_CNObservableSkipUntilInputObserver")
CNTimeProvider = _Class("CNTimeProvider")
_CNCacheFixedTTLBoundingStrategy = _Class("_CNCacheFixedTTLBoundingStrategy")
_CNBoundedQueueingStrategy = _Class("_CNBoundedQueueingStrategy")
_CNPriorityQueueingStrategy = _Class("_CNPriorityQueueingStrategy")
_CNDefaultQueueingStrategy = _Class("_CNDefaultQueueingStrategy")
CNQueue = _Class("CNQueue")
_CNConstantFutureImpl = _Class("_CNConstantFutureImpl")
CNFutureResult = _Class("CNFutureResult")
CNEntitlementVerifier = _Class("CNEntitlementVerifier")
_CNSynchronousQueueScheduler = _Class("_CNSynchronousQueueScheduler")
CNCancelationToken = _Class("CNCancelationToken")
CNInlineSchedulerCancelationToken = _Class("CNInlineSchedulerCancelationToken")
_CNDistinctUntilChangedObservableCancelationToken = _Class(
    "_CNDistinctUntilChangedObservableCancelationToken"
)
CNFlatMapSubscribeCancelationToken = _Class("CNFlatMapSubscribeCancelationToken")
CNFlatMapSubscribeInnerObservableCancelationToken = _Class(
    "CNFlatMapSubscribeInnerObservableCancelationToken"
)
_CNEmptyObservableCancelationToken = _Class("_CNEmptyObservableCancelationToken")
CNMainRunLoopSchedulerCancelationToken = _Class(
    "CNMainRunLoopSchedulerCancelationToken"
)
_CNOnEmptyObservableCNCancelationToken = _Class(
    "_CNOnEmptyObservableCNCancelationToken"
)
_CNGeneratorObservableCancelationToken = _Class(
    "_CNGeneratorObservableCancelationToken"
)
CNQueueSchedulerCancelationToken = _Class("CNQueueSchedulerCancelationToken")
_CNCombineLatestObservableCancelationToken = _Class(
    "_CNCombineLatestObservableCancelationToken"
)
CNMainQueueSchedulerCancelationToken = _Class("CNMainQueueSchedulerCancelationToken")
CNWrappingCancelableToken = _Class("CNWrappingCancelableToken")
CNTimeoutAfterDelayCancelationToken = _Class("CNTimeoutAfterDelayCancelationToken")
CNTakeLastCancelationToken = _Class("CNTakeLastCancelationToken")
CNTakeCancelationToken = _Class("CNTakeCancelationToken")
CNSwitchWithSchedulerProviderSwitchedCancelationToken = _Class(
    "CNSwitchWithSchedulerProviderSwitchedCancelationToken"
)
CNSwitchWithSchedulerProviderOuterCancelationToken = _Class(
    "CNSwitchWithSchedulerProviderOuterCancelationToken"
)
CNSwitchWithSchedulerProviderCancelationToken = _Class(
    "CNSwitchWithSchedulerProviderCancelationToken"
)
CNObserveOnCancelationToken = _Class("CNObserveOnCancelationToken")
CNObservableWithFutureCancelationToken = _Class(
    "CNObservableWithFutureCancelationToken"
)
CNObservableWithResultCancelationToken = _Class(
    "CNObservableWithResultCancelationToken"
)
CNObservableWithErrorCancelationToken = _Class("CNObservableWithErrorCancelationToken")
CNEnumerateObjectsUsingBlockCancelationToken = _Class(
    "CNEnumerateObjectsUsingBlockCancelationToken"
)
CNDematerializeCancelationToken = _Class("CNDematerializeCancelationToken")
CNDelaySubscriptionCancelationToken = _Class("CNDelaySubscriptionCancelationToken")
CNDelayCancelationToken = _Class("CNDelayCancelationToken")
CNConcatenateCancelationToken = _Class("CNConcatenateCancelationToken")
CNOperationQueueSchedulerCancelationToken = _Class(
    "CNOperationQueueSchedulerCancelationToken"
)
CNImmediateSchedulerCancelationToken = _Class("CNImmediateSchedulerCancelationToken")
SynchronousQueueSchedulerCancelationToken = _Class(
    "SynchronousQueueSchedulerCancelationToken"
)
_CNFailedFutureImpl = _Class("_CNFailedFutureImpl")
CNDeviceFirstUnlockFuture = _Class("CNDeviceFirstUnlockFuture")
CNCoreDelegateInfo = _Class("CNCoreDelegateInfo")
CNDelegateInfo = _Class("CNDelegateInfo")
CNCoreMutableDelegateInfo = _Class("CNCoreMutableDelegateInfo")
CNObservable = _Class("CNObservable")
_CNForkJoinObservable = _Class("_CNForkJoinObservable")
_CNBufferingObservable = _Class("_CNBufferingObservable")
_CNDistinctUntilChangedObservable = _Class("_CNDistinctUntilChangedObservable")
_CNAmbObservable = _Class("_CNAmbObservable")
CNReplaySubject = _Class("CNReplaySubject")
_CNFlatMapObservable = _Class("_CNFlatMapObservable")
_CNEmptyObservable = _Class("_CNEmptyObservable")
_CNNeverObservable = _Class("_CNNeverObservable")
_CNConcatenatingObservable = _Class("_CNConcatenatingObservable")
CNPublishingSubject = _Class("CNPublishingSubject")
CNManualObservable = _Class("CNManualObservable")
_CNThrottledObservable = _Class("_CNThrottledObservable")
_CNOnEmptyObservable = _Class("_CNOnEmptyObservable")
_CNSamplingObservable = _Class("_CNSamplingObservable")
_CNGeneratorObservable = _Class("_CNGeneratorObservable")
_CNObservableTakeUntilOperator = _Class("_CNObservableTakeUntilOperator")
_CNCombineLatestObservable = _Class("_CNCombineLatestObservable")
_CNObservableSkipUntilOperator = _Class("_CNObservableSkipUntilOperator")
_CNBlockObservable = _Class("_CNBlockObservable")
CNMapObservable = _Class("CNMapObservable")
_CNDistinctObservable = _Class("_CNDistinctObservable")
_CNScheduledObservable = _Class("_CNScheduledObservable")
CNAsynchronousCacheEntryDelegateObservable = _Class(
    "CNAsynchronousCacheEntryDelegateObservable"
)
CNBehaviorSubject = _Class("CNBehaviorSubject")
CNVirtualSchedulerJob = _Class("CNVirtualSchedulerJob")
CNTracedLog = _Class("CNTracedLog")
CNResult = _Class("CNResult")
CNTimeIntervalFormatter = _Class("CNTimeIntervalFormatter")
CNDateComponentsFormatter = _Class("CNDateComponentsFormatter")
CNWrappedDictionary = _Class("CNWrappedDictionary")
