"""
Classes from the 'WebKitLegacy' framework.
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


WebMainThreadInvoker = _Class("WebMainThreadInvoker")
WebUserContentURLPattern = _Class("WebUserContentURLPattern")
WebUserContentURLPatternPrivate = _Class("WebUserContentURLPatternPrivate")
WebTextIterator = _Class("WebTextIterator")
WebTextIteratorPrivate = _Class("WebTextIteratorPrivate")
WebStorageManager = _Class("WebStorageManager")
WebSelectionRect = _Class("WebSelectionRect")
WebSecurityOrigin = _Class("WebSecurityOrigin")
WebResourcePrivate = _Class("WebResourcePrivate")
WebPolicyDecisionListenerPrivate = _Class("WebPolicyDecisionListenerPrivate")
WebOpenPanelResultListener = _Class("WebOpenPanelResultListener")
WebNotification = _Class("WebNotification")
WebNotificationPrivate = _Class("WebNotificationPrivate")
WebNodeHighlight = _Class("WebNodeHighlight")
WebNavigationData = _Class("WebNavigationData")
WebNavigationDataPrivate = _Class("WebNavigationDataPrivate")
WebMIMETypeRegistry = _Class("WebMIMETypeRegistry")
WebKitStatistics = _Class("WebKitStatistics")
WebKitFullScreenListener = _Class("WebKitFullScreenListener")
WebInspectorFrontend = _Class("WebInspectorFrontend")
WebHistoryItemPrivate = _Class("WebHistoryItemPrivate")
WebHistory = _Class("WebHistory")
WebHistoryPrivate = _Class("WebHistoryPrivate")
_WebCoreLocationUpdateThreadingProxy = _Class("_WebCoreLocationUpdateThreadingProxy")
WebGeolocationPosition = _Class("WebGeolocationPosition")
WebGeolocationPositionInternal = _Class("WebGeolocationPositionInternal")
WebGeolocationCoreLocationProvider = _Class("WebGeolocationCoreLocationProvider")
WebGeolocationProviderInitializationListener = _Class(
    "WebGeolocationProviderInitializationListener"
)
WebGeolocationPolicyListener = _Class("WebGeolocationPolicyListener")
WebGeolocation = _Class("WebGeolocation")
WebFormDelegate = _Class("WebFormDelegate")
WebUndoStep = _Class("WebUndoStep")
WebDownloadInternal = _Class("WebDownloadInternal")
WebDeviceOrientationProviderMock = _Class("WebDeviceOrientationProviderMock")
WebDeviceOrientationProviderMockInternal = _Class(
    "WebDeviceOrientationProviderMockInternal"
)
WebDeviceOrientation = _Class("WebDeviceOrientation")
WebDeviceOrientationInternal = _Class("WebDeviceOrientationInternal")
WebDefaultUIDelegate = _Class("WebDefaultUIDelegate")
WebDefaultFormDelegate = _Class("WebDefaultFormDelegate")
WebDefaultEditingDelegate = _Class("WebDefaultEditingDelegate")
WebDatabaseQuotaManager = _Class("WebDatabaseQuotaManager")
WebCoreStatistics = _Class("WebCoreStatistics")
WebCache = _Class("WebCache")
WebArchivePrivate = _Class("WebArchivePrivate")
WebProgressItem = _Class("WebProgressItem")
WebUITextIndicatorData = _Class("WebUITextIndicatorData")
WebScriptWorld = _Class("WebScriptWorld")
WebScriptWorldPrivate = _Class("WebScriptWorldPrivate")
WebScriptCallFrame = _Class("WebScriptCallFrame")
WebScriptCallFramePrivate = _Class("WebScriptCallFramePrivate")
WebInspector = _Class("WebInspector")
WebApplicationCacheQuotaManager = _Class("WebApplicationCacheQuotaManager")
WebPluginContainerCheck = _Class("WebPluginContainerCheck")
WebBackForwardList = _Class("WebBackForwardList")
WKQuadObject = _Class("WKQuadObject")
WebDownload = _Class("WebDownload")
WebHTMLRepresentationPrivate = _Class("WebHTMLRepresentationPrivate")
WebHTMLRepresentation = _Class("WebHTMLRepresentation")
WebDefaultResourceLoadDelegate = _Class("WebDefaultResourceLoadDelegate")
WebDefaultFrameLoadDelegate = _Class("WebDefaultFrameLoadDelegate")
WebFramePolicyListener = _Class("WebFramePolicyListener")
WebDefaultPolicyDelegate = _Class("WebDefaultPolicyDelegate")
WebApplicationCache = _Class("WebApplicationCache")
WebPluginDatabase = _Class("WebPluginDatabase")
WebPluginController = _Class("WebPluginController")
WebHTMLViewPrivate = _Class("WebHTMLViewPrivate")
WebFramePrivate = _Class("WebFramePrivate")
_WebSafeAsyncForwarder = _Class("_WebSafeAsyncForwarder")
WebDefaultUIKitDelegate = _Class("WebDefaultUIKitDelegate")
_WebSafeForwarder = _Class("_WebSafeForwarder")
WebFixedPositionContent = _Class("WebFixedPositionContent")
WebNodeHighlighter = _Class("WebNodeHighlighter")
WebEditorUndoTarget = _Class("WebEditorUndoTarget")
WebDatabaseManager = _Class("WebDatabaseManager")
WebFrameViewPrivate = _Class("WebFrameViewPrivate")
WebPreferences = _Class("WebPreferences")
WebGeolocationProviderIOS = _Class("WebGeolocationProviderIOS")
WebViewPrivate = _Class("WebViewPrivate")
WebVisiblePosition = _Class("WebVisiblePosition")
WebPolicyDecisionListener = _Class("WebPolicyDecisionListener")
WebHistoryItem = _Class("WebHistoryItem")
WebFrame = _Class("WebFrame")
WebDataSource = _Class("WebDataSource")
WebBasePluginPackage = _Class("WebBasePluginPackage")
WebPluginPackage = _Class("WebPluginPackage")
WebNodeHighlightView = _Class("WebNodeHighlightView")
WebPDFViewPlaceholder = _Class("WebPDFViewPlaceholder")
WebPDFView = _Class("WebPDFView")
WebFrameView = _Class("WebFrameView")
WebPlainWhiteView = _Class("WebPlainWhiteView")
WebHTMLView = _Class("WebHTMLView")
WebView = _Class("WebView")
DOMObject = _Class("DOMObject")
DOMXPathResult = _Class("DOMXPathResult")
DOMXPathExpression = _Class("DOMXPathExpression")
DOMNativeXPathNSResolver = _Class("DOMNativeXPathNSResolver")
DOMTreeWalker = _Class("DOMTreeWalker")
DOMTokenList = _Class("DOMTokenList")
DOMTimeRanges = _Class("DOMTimeRanges")
DOMStyleSheetList = _Class("DOMStyleSheetList")
DOMRect = _Class("DOMRect")
DOMRange = _Class("DOMRange")
DOMNodeList = _Class("DOMNodeList")
DOMNodeIterator = _Class("DOMNodeIterator")
DOMNamedNodeMap = _Class("DOMNamedNodeMap")
DOMMediaList = _Class("DOMMediaList")
DOMMediaError = _Class("DOMMediaError")
DOMImplementation = _Class("DOMImplementation")
DOMHTMLOptionsCollection = _Class("DOMHTMLOptionsCollection")
DOMHTMLCollection = _Class("DOMHTMLCollection")
DOMFileList = _Class("DOMFileList")
DOMEvent = _Class("DOMEvent")
DOMProgressEvent = _Class("DOMProgressEvent")
DOMOverflowEvent = _Class("DOMOverflowEvent")
DOMMutationEvent = _Class("DOMMutationEvent")
DOMUIEvent = _Class("DOMUIEvent")
DOMTextEvent = _Class("DOMTextEvent")
DOMMouseEvent = _Class("DOMMouseEvent")
DOMWheelEvent = _Class("DOMWheelEvent")
DOMKeyboardEvent = _Class("DOMKeyboardEvent")
DOMCounter = _Class("DOMCounter")
DOMStyleSheet = _Class("DOMStyleSheet")
DOMCSSStyleSheet = _Class("DOMCSSStyleSheet")
DOMCSSRuleList = _Class("DOMCSSRuleList")
DOMCSSRule = _Class("DOMCSSRule")
DOMCSSUnknownRule = _Class("DOMCSSUnknownRule")
DOMCSSStyleRule = _Class("DOMCSSStyleRule")
DOMCSSPageRule = _Class("DOMCSSPageRule")
DOMCSSMediaRule = _Class("DOMCSSMediaRule")
DOMCSSImportRule = _Class("DOMCSSImportRule")
DOMCSSFontFaceRule = _Class("DOMCSSFontFaceRule")
DOMCSSCharsetRule = _Class("DOMCSSCharsetRule")
DOMBlob = _Class("DOMBlob")
DOMFile = _Class("DOMFile")
DOMAbstractView = _Class("DOMAbstractView")
DOMNodeFilter = _Class("DOMNodeFilter")
DOMRGBColor = _Class("DOMRGBColor")
DOMCSSValue = _Class("DOMCSSValue")
DOMCSSValueList = _Class("DOMCSSValueList")
DOMCSSPrimitiveValue = _Class("DOMCSSPrimitiveValue")
DOMCSSStyleDeclaration = _Class("DOMCSSStyleDeclaration")
DOMNode = _Class("DOMNode")
DOMEntityReference = _Class("DOMEntityReference")
DOMEntity = _Class("DOMEntity")
DOMDocumentType = _Class("DOMDocumentType")
DOMDocumentFragment = _Class("DOMDocumentFragment")
DOMAttr = _Class("DOMAttr")
DOMCharacterData = _Class("DOMCharacterData")
DOMProcessingInstruction = _Class("DOMProcessingInstruction")
DOMComment = _Class("DOMComment")
DOMText = _Class("DOMText")
DOMCDATASection = _Class("DOMCDATASection")
DOMDocument = _Class("DOMDocument")
DOMHTMLDocument = _Class("DOMHTMLDocument")
DOMElement = _Class("DOMElement")
DOMHTMLElement = _Class("DOMHTMLElement")
DOMHTMLMediaElement = _Class("DOMHTMLMediaElement")
DOMHTMLVideoElement = _Class("DOMHTMLVideoElement")
DOMHTMLUListElement = _Class("DOMHTMLUListElement")
DOMHTMLTableRowElement = _Class("DOMHTMLTableRowElement")
DOMHTMLTitleElement = _Class("DOMHTMLTitleElement")
DOMHTMLTextAreaElement = _Class("DOMHTMLTextAreaElement")
DOMHTMLTableCellElement = _Class("DOMHTMLTableCellElement")
DOMHTMLTableSectionElement = _Class("DOMHTMLTableSectionElement")
DOMHTMLTableElement = _Class("DOMHTMLTableElement")
DOMHTMLStyleElement = _Class("DOMHTMLStyleElement")
DOMHTMLSelectElement = _Class("DOMHTMLSelectElement")
DOMHTMLScriptElement = _Class("DOMHTMLScriptElement")
DOMHTMLQuoteElement = _Class("DOMHTMLQuoteElement")
DOMHTMLParamElement = _Class("DOMHTMLParamElement")
DOMHTMLParagraphElement = _Class("DOMHTMLParagraphElement")
DOMHTMLOptionElement = _Class("DOMHTMLOptionElement")
DOMHTMLOptGroupElement = _Class("DOMHTMLOptGroupElement")
DOMHTMLOListElement = _Class("DOMHTMLOListElement")
DOMHTMLObjectElement = _Class("DOMHTMLObjectElement")
DOMHTMLMetaElement = _Class("DOMHTMLMetaElement")
DOMHTMLMenuElement = _Class("DOMHTMLMenuElement")
DOMHTMLMarqueeElement = _Class("DOMHTMLMarqueeElement")
DOMHTMLMapElement = _Class("DOMHTMLMapElement")
DOMHTMLPreElement = _Class("DOMHTMLPreElement")
DOMHTMLLinkElement = _Class("DOMHTMLLinkElement")
DOMHTMLLIElement = _Class("DOMHTMLLIElement")
DOMHTMLLegendElement = _Class("DOMHTMLLegendElement")
DOMHTMLLabelElement = _Class("DOMHTMLLabelElement")
DOMHTMLImageElement = _Class("DOMHTMLImageElement")
DOMHTMLIFrameElement = _Class("DOMHTMLIFrameElement")
DOMHTMLHtmlElement = _Class("DOMHTMLHtmlElement")
DOMHTMLHRElement = _Class("DOMHTMLHRElement")
DOMHTMLHeadElement = _Class("DOMHTMLHeadElement")
DOMHTMLHeadingElement = _Class("DOMHTMLHeadingElement")
DOMHTMLFrameSetElement = _Class("DOMHTMLFrameSetElement")
DOMHTMLFrameElement = _Class("DOMHTMLFrameElement")
DOMHTMLFormElement = _Class("DOMHTMLFormElement")
DOMHTMLFontElement = _Class("DOMHTMLFontElement")
DOMHTMLFieldSetElement = _Class("DOMHTMLFieldSetElement")
DOMHTMLEmbedElement = _Class("DOMHTMLEmbedElement")
DOMHTMLDListElement = _Class("DOMHTMLDListElement")
DOMHTMLDivElement = _Class("DOMHTMLDivElement")
DOMHTMLDirectoryElement = _Class("DOMHTMLDirectoryElement")
DOMHTMLModElement = _Class("DOMHTMLModElement")
DOMHTMLTableColElement = _Class("DOMHTMLTableColElement")
DOMHTMLTableCaptionElement = _Class("DOMHTMLTableCaptionElement")
DOMHTMLCanvasElement = _Class("DOMHTMLCanvasElement")
DOMHTMLButtonElement = _Class("DOMHTMLButtonElement")
DOMHTMLBRElement = _Class("DOMHTMLBRElement")
DOMHTMLBodyElement = _Class("DOMHTMLBodyElement")
DOMHTMLBaseFontElement = _Class("DOMHTMLBaseFontElement")
DOMHTMLBaseElement = _Class("DOMHTMLBaseElement")
DOMHTMLAreaElement = _Class("DOMHTMLAreaElement")
DOMHTMLAppletElement = _Class("DOMHTMLAppletElement")
DOMHTMLAnchorElement = _Class("DOMHTMLAnchorElement")
DOMHTMLInputElement = _Class("DOMHTMLInputElement")
WebHighlightLayer = _Class("WebHighlightLayer")
WebIndicateLayer = _Class("WebIndicateLayer")
WebElementDictionary = _Class("WebElementDictionary")
