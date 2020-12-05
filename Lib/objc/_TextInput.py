"""
Classes from the 'TextInput' framework.
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


TIUserModelDataStore = _Class("TIUserModelDataStore")
TIUserModelDataStoreEntry = _Class("TIUserModelDataStoreEntry")
TIUserModelDataStoreDurableEntry = _Class("TIUserModelDataStoreDurableEntry")
TIImageCacheItem = _Class("TIImageCacheItem")
TISmartInsertDeleteController = _Class("TISmartInsertDeleteController")
TIFacemarkSorter = _Class("TIFacemarkSorter")
TIAutoshiftController = _Class("TIAutoshiftController")
_TIKeyboardSecureCandidate = _Class("_TIKeyboardSecureCandidate")
TIKeyboardSecureCandidateLayoutTraits = _Class("TIKeyboardSecureCandidateLayoutTraits")
TIUserModel = _Class("TIUserModel")
TIWordTokenizer = _Class("TIWordTokenizer")
TIUserModelValues = _Class("TIUserModelValues")
TIAnalyticsMetricsContext = _Class("TIAnalyticsMetricsContext")
TIUserModelIndexedCounter = _Class("TIUserModelIndexedCounter")
TIUserModelCounter = _Class("TIUserModelCounter")
TIUserDictionaryWord = _Class("TIUserDictionaryWord")
TIUserDictionaryTransaction = _Class("TIUserDictionaryTransaction")
TIUserDictionaryEntryValue = _Class("TIUserDictionaryEntryValue")
TIPreferencesControllerService = _Class("TIPreferencesControllerService")
TIPreferencesControllerServiceHandler = _Class("TIPreferencesControllerServiceHandler")
TIResponseKitTrainer = _Class("TIResponseKitTrainer")
TIInputContextHistory = _Class("TIInputContextHistory")
_TIInputContextEntry = _Class("_TIInputContextEntry")
TIAutofill = _Class("TIAutofill")
TITypologyLog = _Class("TITypologyLog")
TIRollingLog = _Class("TIRollingLog")
TITypologyLogArchiverDelegate = _Class("TITypologyLogArchiverDelegate")
TILinguisticAssetDownloadClientMock = _Class("TILinguisticAssetDownloadClientMock")
TILinguisticAssetDownloadClient = _Class("TILinguisticAssetDownloadClient")
TIInputModeLocaleIdentifierOverrideMapping = _Class(
    "TIInputModeLocaleIdentifierOverrideMapping"
)
TIKeyboardLayoutFactory = _Class("TIKeyboardLayoutFactory")
TITypologyTimer = _Class("TITypologyTimer")
TITypologyStatistic = _Class("TITypologyStatistic")
TITypologyStatisticAutocorrectionListUI = _Class(
    "TITypologyStatisticAutocorrectionListUI"
)
TITypologyStatisticTimeElapsed = _Class("TITypologyStatisticTimeElapsed")
TITypologyStatisticCurrentAutocorrections = _Class(
    "TITypologyStatisticCurrentAutocorrections"
)
TITypologyStatisticRankCandidatesAccepted = _Class(
    "TITypologyStatisticRankCandidatesAccepted"
)
TITypologyStatisticBasicCounts = _Class("TITypologyStatisticBasicCounts")
TITypologyStatisticComposite = _Class("TITypologyStatisticComposite")
TITypologyStatisticTypingSpeed = _Class("TITypologyStatisticTypingSpeed")
TIAssistantSettings = _Class("TIAssistantSettings")
TIKeyboardCandidateResultSetCoder = _Class("TIKeyboardCandidateResultSetCoder")
TIKeyboardCandidateGroup = _Class("TIKeyboardCandidateGroup")
TIKeyboardKeyBehaviors = _Class("TIKeyboardKeyBehaviors")
TIAnalyticsEventDispatcher = _Class("TIAnalyticsEventDispatcher")
TIHandwritingStrokes = _Class("TIHandwritingStrokes")
TIChineseShared = _Class("TIChineseShared")
TILexicon = _Class("TILexicon")
TIRecentInputs = _Class("TIRecentInputs")
TILexiconEntry = _Class("TILexiconEntry")
TIAccessibilityClient = _Class("TIAccessibilityClient")
TITypologyRecord = _Class("TITypologyRecord")
TITypologyRecordGroupMarker = _Class("TITypologyRecordGroupMarker")
TITypologyRecordKeyboardLayout = _Class("TITypologyRecordKeyboardLayout")
TITypologyRecordLastAcceptedCandidateCorrected = _Class(
    "TITypologyRecordLastAcceptedCandidateCorrected"
)
TITypologyRecordCandidateRejected = _Class("TITypologyRecordCandidateRejected")
TITypologyRecordTextAccepted = _Class("TITypologyRecordTextAccepted")
TITypologyRecordSetOriginalInput = _Class("TITypologyRecordSetOriginalInput")
TITypologyRecordPhraseBoundaryAdjustment = _Class(
    "TITypologyRecordPhraseBoundaryAdjustment"
)
TITypologyRecordSkipHitTest = _Class("TITypologyRecordSkipHitTest")
TITypologyRecordHitTest = _Class("TITypologyRecordHitTest")
TITypologyRecordRefinements = _Class("TITypologyRecordRefinements")
TITypologyRecordReplacements = _Class("TITypologyRecordReplacements")
TITypologyRecordAcceptedCandidate = _Class("TITypologyRecordAcceptedCandidate")
TITypologyRecordCandidateResultSet = _Class("TITypologyRecordCandidateResultSet")
TITypologyRecordAutocorrections = _Class("TITypologyRecordAutocorrections")
TITypologyRecordKeyboardInput = _Class("TITypologyRecordKeyboardInput")
TITypologyRecordSync = _Class("TITypologyRecordSync")
TIAdhocEventDispatcher = _Class("TIAdhocEventDispatcher")
TIStatisticChange = _Class("TIStatisticChange")
TIKeyboardIntermediateText = _Class("TIKeyboardIntermediateText")
TIKeyEventMap = _Class("TIKeyEventMap")
TIKeyEventMap_ja = _Class("TIKeyEventMap_ja")
TIKeyEventMap_ja_LiveConversion = _Class("TIKeyEventMap_ja_LiveConversion")
TIKeyEventMapHindiTransliteration = _Class("TIKeyEventMapHindiTransliteration")
TIKeyEventMap_zh = _Class("TIKeyEventMap_zh")
TIKeyEventMap_zh_Hans_Wubixing = _Class("TIKeyEventMap_zh_Hans_Wubixing")
TIKeyEventMap_zh_Hant_Cangjie = _Class("TIKeyEventMap_zh_Hant_Cangjie")
TIKeyEventMap_zh_Stroke = _Class("TIKeyEventMap_zh_Stroke")
TIKeyEventMap_zh_Hant_Stroke = _Class("TIKeyEventMap_zh_Hant_Stroke")
TIKeyEventMap_zh_Hans_Stroke = _Class("TIKeyEventMap_zh_Hans_Stroke")
TIKeyEventMap_zh_Phonetic = _Class("TIKeyEventMap_zh_Phonetic")
TIKeyEventMap_zh_Hant_Zhuyin = _Class("TIKeyEventMap_zh_Hant_Zhuyin")
TIKeyEventMap_zh_Hant_Zhuyin_LiveConversion = _Class(
    "TIKeyEventMap_zh_Hant_Zhuyin_LiveConversion"
)
TIKeyEventMap_zh_Hant_Pinyin = _Class("TIKeyEventMap_zh_Hant_Pinyin")
TIKeyEventMap_zh_Hans_Pinyin = _Class("TIKeyEventMap_zh_Hans_Pinyin")
TIKeyboardBehaviors = _Class("TIKeyboardBehaviors")
TIKeyboardBehaviors_Japanese = _Class("TIKeyboardBehaviors_Japanese")
TIKeyboardBehaviors_Japanese_LiveConversion = _Class(
    "TIKeyboardBehaviors_Japanese_LiveConversion"
)
TIKeyboardBehaviors_Thai = _Class("TIKeyboardBehaviors_Thai")
TIKeyboardBehaviors_Handwriting = _Class("TIKeyboardBehaviors_Handwriting")
TIKeyboardBehaviors_Wubixing = _Class("TIKeyboardBehaviors_Wubixing")
TIKeyboardBehaviors_Cangjie = _Class("TIKeyboardBehaviors_Cangjie")
TIKeyboardBehaviors_ShapeBased = _Class("TIKeyboardBehaviors_ShapeBased")
TIKeyboardBehaviors_Zhuyin_LiveConversion = _Class(
    "TIKeyboardBehaviors_Zhuyin_LiveConversion"
)
TIKeyboardBehaviors_Zhuyin = _Class("TIKeyboardBehaviors_Zhuyin")
TIKeyboardBehaviors_Pinyin = _Class("TIKeyboardBehaviors_Pinyin")
TIKeyboardBehaviors_WaitingForCandidates = _Class(
    "TIKeyboardBehaviors_WaitingForCandidates"
)
TIKeyboardBehaviors_Autocorrect = _Class("TIKeyboardBehaviors_Autocorrect")
TIKeyboardBehaviors_Simple = _Class("TIKeyboardBehaviors_Simple")
TICharacterSetDescription = _Class("TICharacterSetDescription")
TIMutableCharacterSetDescription = _Class("TIMutableCharacterSetDescription")
TIKeyboardInputManagerState = _Class("TIKeyboardInputManagerState")
TIKeyboardInputManagerClientRequest = _Class("TIKeyboardInputManagerClientRequest")
TIStatisticChangeCache = _Class("TIStatisticChangeCache")
TIKeyboardSecureCandidateTextTraits = _Class("TIKeyboardSecureCandidateTextTraits")
TIKeyboardSecureCandidateRGBColor = _Class("TIKeyboardSecureCandidateRGBColor")
TIKeyboardSecureCandidateRenderTraits = _Class("TIKeyboardSecureCandidateRenderTraits")
TIKeyboardLayoutState = _Class("TIKeyboardLayoutState")
TIDocumentState = _Class("TIDocumentState")
TIImageCacheClient = _Class("TIImageCacheClient")
TIAggdReporter = _Class("TIAggdReporter")
TIStatisticKey = _Class("TIStatisticKey")
TIKeyboardBehaviorState = _Class("TIKeyboardBehaviorState")
TISmartPunctuationOptions = _Class("TISmartPunctuationOptions")
TIInputModeParser = _Class("TIInputModeParser")
TIKeyboardLayout = _Class("TIKeyboardLayout")
TIHardwareKeyboardLayout = _Class("TIHardwareKeyboardLayout")
TICandidateRequestToken = _Class("TICandidateRequestToken")
TIKeyboardTouchEvent = _Class("TIKeyboardTouchEvent")
TIKeyboardOutput = _Class("TIKeyboardOutput")
TIKeyboardInput = _Class("TIKeyboardInput")
TIAutocorrectionList = _Class("TIAutocorrectionList")
TIKeyboardCandidateResultSet = _Class("TIKeyboardCandidateResultSet")
TIKeyboardConfiguration = _Class("TIKeyboardConfiguration")
TIKeyboardCandidate = _Class("TIKeyboardCandidate")
TIMecabraCandidate = _Class("TIMecabraCandidate")
TICompositeMecabraCandidate = _Class("TICompositeMecabraCandidate")
TIMecabraFacemarkCandidate = _Class("TIMecabraFacemarkCandidate")
TILiveConversionCandidate = _Class("TILiveConversionCandidate")
TIKeyboardCandidateSingle = _Class("TIKeyboardCandidateSingle")
TIZephyrCandidate = _Class("TIZephyrCandidate")
TILabeledKeyboardCandidate = _Class("TILabeledKeyboardCandidate")
TIShortcutConversionCandidate = _Class("TIShortcutConversionCandidate")
TIPinyinDisambiguationCandidate = _Class("TIPinyinDisambiguationCandidate")
TIHandwritingCandidate = _Class("TIHandwritingCandidate")
TIKeyboardInputManagerStub = _Class("TIKeyboardInputManagerStub")
TIKeyboardInputManagerClient = _Class("TIKeyboardInputManagerClient")
TITextInputTraits = _Class("TITextInputTraits")
TISmartPunctuationController = _Class("TISmartPunctuationController")
TIKeyboardState = _Class("TIKeyboardState")
TIAnalyticsUtil = _Class("TIAnalyticsUtil")
TIAnalyticsServiceProviderImpl = _Class("TIAnalyticsServiceProviderImpl")
TIAnalyticsService = _Class("TIAnalyticsService")
TIAnalyticsEventSpec = _Class("TIAnalyticsEventSpec")
TIAnalyticsFieldSpec = _Class("TIAnalyticsFieldSpec")
TIAnalyticsBooleanFieldSpec = _Class("TIAnalyticsBooleanFieldSpec")
TIAnalyticsNumberFieldSpec = _Class("TIAnalyticsNumberFieldSpec")
TIAnalyticsStringFieldSpec = _Class("TIAnalyticsStringFieldSpec")
TIInputModeController = _Class("TIInputModeController")
_TIPreference = _Class("_TIPreference")
_TIPreferenceDomain = _Class("_TIPreferenceDomain")
TIPreferencesController = _Class("TIPreferencesController")
TIPreferencesControllerClient = _Class("TIPreferencesControllerClient")
