"""
Classes from the 'WebKit' framework.
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


WKObject = _Class("WKObject")
WKNSURLAuthenticationChallenge = _Class("WKNSURLAuthenticationChallenge")
WKNSURL = _Class("WKNSURL")
WKNSString = _Class("WKNSString")
WKNSError = _Class("WKNSError")
WKNSURLRequest = _Class("WKNSURLRequest")
WKShareSheet = _Class("WKShareSheet")
WKDragSessionContext = _Class("WKDragSessionContext")
WKFocusedElementInfo = _Class("WKFocusedElementInfo")
WKFormInputSession = _Class("WKFormInputSession")
WKAnimationDelegate = _Class("WKAnimationDelegate")
WKAccessibilityWebPageObjectBase = _Class("WKAccessibilityWebPageObjectBase")
WKAccessibilityWebPageObject = _Class("WKAccessibilityWebPageObject")
WKWebProcessPlugInBrowserContextController = _Class(
    "WKWebProcessPlugInBrowserContextController"
)
WKWebProcessPlugInController = _Class("WKWebProcessPlugInController")
WKDOMTextIterator = _Class("WKDOMTextIterator")
WKDOMRange = _Class("WKDOMRange")
WKDOMNode = _Class("WKDOMNode")
WKDOMText = _Class("WKDOMText")
WKDOMElement = _Class("WKDOMElement")
WKDOMDocument = _Class("WKDOMDocument")
WKDOMDocumentParserYieldToken = _Class("WKDOMDocumentParserYieldToken")
WKWebProcessPlugInScriptWorld = _Class("WKWebProcessPlugInScriptWorld")
WKWebProcessPlugInRangeHandle = _Class("WKWebProcessPlugInRangeHandle")
WKWebProcessPlugInPageGroup = _Class("WKWebProcessPlugInPageGroup")
WKWebProcessPlugInNodeHandle = _Class("WKWebProcessPlugInNodeHandle")
WKWebProcessPlugInHitTestResult = _Class("WKWebProcessPlugInHitTestResult")
WKWebProcessPlugInFrame = _Class("WKWebProcessPlugInFrame")
WKWebProcessBundleParameters = _Class("WKWebProcessBundleParameters")
WKFullScreenWindowController = _Class("WKFullScreenWindowController")
WKFullScreenInteractiveTransition = _Class("WKFullScreenInteractiveTransition")
WKFullscreenAnimationController = _Class("WKFullscreenAnimationController")
WKColorPicker = _Class("WKColorPicker")
WKRotatingPopover = _Class("WKRotatingPopover")
WKFormRotatingAccessoryPopover = _Class("WKFormRotatingAccessoryPopover")
WKSelectPopover = _Class("WKSelectPopover")
WKColorPopover = _Class("WKColorPopover")
_WKFileUploadItem = _Class("_WKFileUploadItem")
_WKVideoFileUploadItem = _Class("_WKVideoFileUploadItem")
_WKImageFileUploadItem = _Class("_WKImageFileUploadItem")
WKFormPeripheralBase = _Class("WKFormPeripheralBase")
WKFormSelectControl = _Class("WKFormSelectControl")
WKFormColorControl = _Class("WKFormColorControl")
WKDateTimeInputControl = _Class("WKDateTimeInputControl")
WKDateTimePicker = _Class("WKDateTimePicker")
WKAirPlayRoutePicker = _Class("WKAirPlayRoutePicker")
WKDataListSuggestionsControl = _Class("WKDataListSuggestionsControl")
WKDataListSuggestionsPopover = _Class("WKDataListSuggestionsPopover")
WKDataListSuggestionsPicker = _Class("WKDataListSuggestionsPicker")
WKScrollViewDelegateForwarder = _Class("WKScrollViewDelegateForwarder")
WKWebAllowDenyPolicyListener = _Class("WKWebAllowDenyPolicyListener")
WKLegacyCoreLocationProvider = _Class("WKLegacyCoreLocationProvider")
WKGeolocationProviderIOS = _Class("WKGeolocationProviderIOS")
WKSwipeTransitionController = _Class("WKSwipeTransitionController")
WKMockNFTag = _Class("WKMockNFTag")
WKNFReaderSessionDelegate = _Class("WKNFReaderSessionDelegate")
WKScrollingNodeScrollViewDelegate = _Class("WKScrollingNodeScrollViewDelegate")
WKSOSecretDelegate = _Class("WKSOSecretDelegate")
WKReloadFrameErrorRecoveryAttempter = _Class("WKReloadFrameErrorRecoveryAttempter")
WKEditCommand = _Class("WKEditCommand")
_WKPreviewControllerDelegate = _Class("_WKPreviewControllerDelegate")
_WKPreviewControllerDataSource = _Class("_WKPreviewControllerDataSource")
WKCustomProtocolLoader = _Class("WKCustomProtocolLoader")
_WKWebsitePolicies = _Class("_WKWebsitePolicies")
_WKWebsiteDataStore = _Class("_WKWebsiteDataStore")
_WKWebsiteDataSize = _Class("_WKWebsiteDataSize")
_WKWebAuthenticationPanel = _Class("_WKWebAuthenticationPanel")
_WKWebAuthenticationAssertionResponse = _Class("_WKWebAuthenticationAssertionResponse")
_WKUserStyleSheet = _Class("_WKUserStyleSheet")
_WKUserInitiatedAction = _Class("_WKUserInitiatedAction")
_WKUserContentWorld = _Class("_WKUserContentWorld")
_WKUserContentFilter = _Class("_WKUserContentFilter")
_WKUserContentExtensionStore = _Class("_WKUserContentExtensionStore")
_WKTextManipulationToken = _Class("_WKTextManipulationToken")
_WKTextManipulationItem = _Class("_WKTextManipulationItem")
_WKTextManipulationExclusionRule = _Class("_WKTextManipulationExclusionRule")
_WKTextManipulationConfiguration = _Class("_WKTextManipulationConfiguration")
_WKTextInputContext = _Class("_WKTextInputContext")
_WKSessionState = _Class("_WKSessionState")
_WKResourceLoadInfo = _Class("_WKResourceLoadInfo")
_WKLinkIconParameters = _Class("_WKLinkIconParameters")
_WKInternalDebugFeature = _Class("_WKInternalDebugFeature")
_WKInspectorDebuggableInfo = _Class("_WKInspectorDebuggableInfo")
_WKGeolocationPosition = _Class("_WKGeolocationPosition")
_WKExperimentalFeature = _Class("_WKExperimentalFeature")
_WKElementAction = _Class("_WKElementAction")
_WKDownload = _Class("_WKDownload")
_WKContentRuleListAction = _Class("_WKContentRuleListAction")
_WKAutomationSessionConfiguration = _Class("_WKAutomationSessionConfiguration")
_WKAutomationSession = _Class("_WKAutomationSession")
_WKAttachment = _Class("_WKAttachment")
_WKAttachmentInfo = _Class("_WKAttachmentInfo")
_WKAttachmentDisplayOptions = _Class("_WKAttachmentDisplayOptions")
_WKApplicationManifest = _Class("_WKApplicationManifest")
_WKActivatedElementInfo = _Class("_WKActivatedElementInfo")
WKWindowFeatures = _Class("WKWindowFeatures")
WKWebsiteDataRecord = _Class("WKWebsiteDataRecord")
WKURLSchemeTaskImpl = _Class("WKURLSchemeTaskImpl")
WKTypeRefWrapper = _Class("WKTypeRefWrapper")
WKSnapshotConfiguration = _Class("WKSnapshotConfiguration")
WKSecurityOrigin = _Class("WKSecurityOrigin")
WKPreviewElementInfo = _Class("WKPreviewElementInfo")
WKPDFConfiguration = _Class("WKPDFConfiguration")
WKNavigationData = _Class("WKNavigationData")
WKNSURLAuthenticationChallengeSender = _Class("WKNSURLAuthenticationChallengeSender")
WKHTTPCookieStore = _Class("WKHTTPCookieStore")
WKFindResult = _Class("WKFindResult")
WKFindConfiguration = _Class("WKFindConfiguration")
WKContextMenuElementInfo = _Class("WKContextMenuElementInfo")
WKContentRuleListStore = _Class("WKContentRuleListStore")
WKContentRuleList = _Class("WKContentRuleList")
WKBrowsingContextController = _Class("WKBrowsingContextController")
_WKAttributedStringWebViewCache = _Class("_WKAttributedStringWebViewCache")
_WKAttributedStringNavigationDelegate = _Class("_WKAttributedStringNavigationDelegate")
WKObservablePageState = _Class("WKObservablePageState")
_WKRemoteObjectRegistry = _Class("_WKRemoteObjectRegistry")
_WKRemoteObjectInterface = _Class("_WKRemoteObjectInterface")
_WKFrameHandle = _Class("_WKFrameHandle")
WKRemoteObject = _Class("WKRemoteObject")
WKBrowsingContextHandle = _Class("WKBrowsingContextHandle")
WKPaymentAuthorizationDelegate = _Class("WKPaymentAuthorizationDelegate")
WKPaymentAuthorizationControllerDelegate = _Class(
    "WKPaymentAuthorizationControllerDelegate"
)
WKPaymentAuthorizationViewControllerDelegate = _Class(
    "WKPaymentAuthorizationViewControllerDelegate"
)
WKNetworkSessionDelegate = _Class("WKNetworkSessionDelegate")
WKQLThumbnailQueueManager = _Class("WKQLThumbnailQueueManager")
WKProcessTaskStateObserverDelegate = _Class("WKProcessTaskStateObserverDelegate")
_WKTouchEventGenerator = _Class("_WKTouchEventGenerator")
_WKResourceLoadStatisticsThirdParty = _Class("_WKResourceLoadStatisticsThirdParty")
_WKResourceLoadStatisticsFirstParty = _Class("_WKResourceLoadStatisticsFirstParty")
_WKCustomHeaderFields = _Class("_WKCustomHeaderFields")
WKTextPlaceholder = _Class("WKTextPlaceholder")
WKAutocorrectionRects = _Class("WKAutocorrectionRects")
WKAutocorrectionContext = _Class("WKAutocorrectionContext")
WKDataListTextSuggestion = _Class("WKDataListTextSuggestion")
WebResource = _Class("WebResource")
WebArchive = _Class("WebArchive")
WKActionSheetAssistant = _Class("WKActionSheetAssistant")
WKKeyboardScrollingAnimator = _Class("WKKeyboardScrollingAnimator")
WKKeyboardScrollViewAnimator = _Class("WKKeyboardScrollViewAnimator")
WKContentWorld = _Class("WKContentWorld")
WKBackForwardListItem = _Class("WKBackForwardListItem")
WKNavigationResponse = _Class("WKNavigationResponse")
WKOneShotDisplayLinkHandler = _Class("WKOneShotDisplayLinkHandler")
WKNavigationAction = _Class("WKNavigationAction")
WKFrameInfo = _Class("WKFrameInfo")
_WKFrameTreeNode = _Class("_WKFrameTreeNode")
WKNavigation = _Class("WKNavigation")
WKProcessAssertionBackgroundTaskManager = _Class(
    "WKProcessAssertionBackgroundTaskManager"
)
WKConnection = _Class("WKConnection")
WKRBSAssertionDelegate = _Class("WKRBSAssertionDelegate")
_WKInspector = _Class("_WKInspector")
WKBackForwardList = _Class("WKBackForwardList")
WKPreferenceObserver = _Class("WKPreferenceObserver")
WKFullKeyboardAccessWatcher = _Class("WKFullKeyboardAccessWatcher")
WKEditorUndoTarget = _Class("WKEditorUndoTarget")
WKWebViewContentProviderRegistry = _Class("WKWebViewContentProviderRegistry")
WKWebpagePreferences = _Class("WKWebpagePreferences")
WKSOAuthorizationDelegate = _Class("WKSOAuthorizationDelegate")
_WKWebsiteDataStoreConfiguration = _Class("_WKWebsiteDataStoreConfiguration")
_WKVisitedLinkStore = _Class("_WKVisitedLinkStore")
WKPreferences = _Class("WKPreferences")
WKBrowsingContextGroup = _Class("WKBrowsingContextGroup")
_WKProcessPoolConfiguration = _Class("_WKProcessPoolConfiguration")
WKWebViewConfiguration = _Class("WKWebViewConfiguration")
WKWebEvent = _Class("WKWebEvent")
WKSyntheticFlagsChangedWebEvent = _Class("WKSyntheticFlagsChangedWebEvent")
WKTextSelectionRect = _Class("WKTextSelectionRect")
_WKWebViewPrintFormatter = _Class("_WKWebViewPrintFormatter")
WKPreviewAction = _Class("WKPreviewAction")
WKQuirkyNSUndoManager = _Class("WKQuirkyNSUndoManager")
WKTextPosition = _Class("WKTextPosition")
WKTextRange = _Class("WKTextRange")
WKCustomProtocol = _Class("WKCustomProtocol")
WKDownloadProgress = _Class("WKDownloadProgress")
WKInspectorNodeSearchGestureRecognizer = _Class(
    "WKInspectorNodeSearchGestureRecognizer"
)
WKTouchActionGestureRecognizer = _Class("WKTouchActionGestureRecognizer")
WKDeferringGestureRecognizer = _Class("WKDeferringGestureRecognizer")
WKSyntheticTapGestureRecognizer = _Class("WKSyntheticTapGestureRecognizer")
WKHighlightLongPressGestureRecognizer = _Class("WKHighlightLongPressGestureRecognizer")
WKMouseGestureRecognizer = _Class("WKMouseGestureRecognizer")
WKRemoteObjectDecoder = _Class("WKRemoteObjectDecoder")
WKRemoteObjectEncoder = _Class("WKRemoteObjectEncoder")
WKVideoLayerRemote = _Class("WKVideoLayerRemote")
WKPlainRemoteLayer = _Class("WKPlainRemoteLayer")
WKUserDefaults = _Class("WKUserDefaults")
WKQLThumbnailLoadOperation = _Class("WKQLThumbnailLoadOperation")
WKProcessGroup = _Class("WKProcessGroup")
WKProcessPool = _Class("WKProcessPool")
WKScriptMessage = _Class("WKScriptMessage")
WKUserContentController = _Class("WKUserContentController")
WKUserScript = _Class("WKUserScript")
WKWebsiteDataStore = _Class("WKWebsiteDataStore")
WKSafeBrowsingBox = _Class("WKSafeBrowsingBox")
WKSafeBrowsingExclamationPoint = _Class("WKSafeBrowsingExclamationPoint")
WKInspectorIndicationView = _Class("WKInspectorIndicationView")
WKFullScreenPlaceholderView = _Class("WKFullScreenPlaceholderView")
WKColorMatrixView = _Class("WKColorMatrixView")
WKPasswordView = _Class("WKPasswordView")
WKPDFPageNumberIndicator = _Class("WKPDFPageNumberIndicator")
WKInspectorHighlightView = _Class("WKInspectorHighlightView")
WKLayerHostView = _Class("WKLayerHostView")
WKEmbeddedView = _Class("WKEmbeddedView")
WKCompositingView = _Class("WKCompositingView")
WKRemoteView = _Class("WKRemoteView")
WKShapeView = _Class("WKShapeView")
WKSimpleBackdropView = _Class("WKSimpleBackdropView")
WKTransformView = _Class("WKTransformView")
WKApplicationStateTrackingView = _Class("WKApplicationStateTrackingView")
WKSystemPreviewView = _Class("WKSystemPreviewView")
WKContentView = _Class("WKContentView")
WKPDFView = _Class("WKPDFView")
WKBackdropView = _Class("WKBackdropView")
WKUIRemoteView = _Class("WKUIRemoteView")
WKFullscreenStackView = _Class("WKFullscreenStackView")
WKSelectSinglePicker = _Class("WKSelectSinglePicker")
WKMultipleSelectPicker = _Class("WKMultipleSelectPicker")
WKDataListSuggestionsPickerView = _Class("WKDataListSuggestionsPickerView")
WKOptionPickerCell = _Class("WKOptionPickerCell")
WKOptionGroupPickerCell = _Class("WKOptionGroupPickerCell")
WKSafeBrowsingWarning = _Class("WKSafeBrowsingWarning")
WKChildScrollView = _Class("WKChildScrollView")
WKScrollView = _Class("WKScrollView")
WKSafeBrowsingTextView = _Class("WKSafeBrowsingTextView")
_WKExtrinsicButton = _Class("_WKExtrinsicButton")
WKColorButton = _Class("WKColorButton")
WKWebView = _Class("WKWebView")
WKFullScreenViewController = _Class("WKFullScreenViewController")
WKFileUploadPanel = _Class("WKFileUploadPanel")
WKRichFileUploadPanel = _Class("WKRichFileUploadPanel")
WKDateTimeContextMenuViewController = _Class("WKDateTimeContextMenuViewController")
WKVideoFullScreenViewController = _Class("WKVideoFullScreenViewController")
WKImagePreviewViewController = _Class("WKImagePreviewViewController")
WKSelectTableViewController = _Class("WKSelectTableViewController")
WKDataListSuggestionsViewController = _Class("WKDataListSuggestionsViewController")
WKActionSheet = _Class("WKActionSheet")
WKNSData = _Class("WKNSData")
WKNSNumber = _Class("WKNSNumber")
WKNSDictionary = _Class("WKNSDictionary")
WKNSArray = _Class("WKNSArray")
