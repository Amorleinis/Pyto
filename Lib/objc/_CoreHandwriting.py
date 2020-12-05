"""
Classes from the 'CoreHandwriting' framework.
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


CHPostprocessingStep = _Class("CHPostprocessingStep")
CHMergeColumnsNoWhiteSpaceStep = _Class("CHMergeColumnsNoWhiteSpaceStep")
CHNumberFieldResultReorderingStep = _Class("CHNumberFieldResultReorderingStep")
CHMultiWordOVSFilteringStep = _Class("CHMultiWordOVSFilteringStep")
CHReorderSCTCConfusionStep = _Class("CHReorderSCTCConfusionStep")
CHTransliterateChineseStep = _Class("CHTransliterateChineseStep")
CHRemoveSpacesFromSpecialFieldsStep = _Class("CHRemoveSpacesFromSpecialFieldsStep")
CHRemoveSpacesFromStrongURLsAndEmailsStep = _Class(
    "CHRemoveSpacesFromStrongURLsAndEmailsStep"
)
CHCandidateRefinementStep = _Class("CHCandidateRefinementStep")
CHDropSpaceBeforePunctuationMarksStep = _Class("CHDropSpaceBeforePunctuationMarksStep")
CHIdentifyLowAlignmentConfidenceColumnsStep = _Class(
    "CHIdentifyLowAlignmentConfidenceColumnsStep"
)
CHSemanticTokenizerStep = _Class("CHSemanticTokenizerStep")
CHTransliterateHalfWidthPunctuationStep = _Class(
    "CHTransliterateHalfWidthPunctuationStep"
)
CHLexiconCorrectionStep = _Class("CHLexiconCorrectionStep")
CHTextFieldTypeSwitchStep = _Class("CHTextFieldTypeSwitchStep")
CHPostProcessingManager = _Class("CHPostProcessingManager")
CHResultWithContext = _Class("CHResultWithContext")
CHPatternNetwork = _Class("CHPatternNetwork")
NetworkCursor = _Class("NetworkCursor")
CHRecognitionSessionIndexableContent = _Class("CHRecognitionSessionIndexableContent")
CHStrokeClassifier = _Class("CHStrokeClassifier")
CHCharacterSetRules = _Class("CHCharacterSetRules")
CHTextCorrectionRecognizer = _Class("CHTextCorrectionRecognizer")
CHRecognitionSession = _Class("CHRecognitionSession")
CHRecognitionSessionVersion = _Class("CHRecognitionSessionVersion")
CHRecognizerConfiguration = _Class("CHRecognizerConfiguration")
CHTextCorrectionResult = _Class("CHTextCorrectionResult")
CHContextualTextResults = _Class("CHContextualTextResults")
CHContextualTextResult = _Class("CHContextualTextResult")
CHVisualizationManager = _Class("CHVisualizationManager")
CHRemoteRecognizer = _Class("CHRemoteRecognizer")
CHPolygon = _Class("CHPolygon")
CHSubstrokePlacement = _Class("CHSubstrokePlacement")
CHSubstroke = _Class("CHSubstroke")
CHDataDetectorQueryItem = _Class("CHDataDetectorQueryItem")
CHTextInputQueryItem = _Class("CHTextInputQueryItem")
CHTopDownStrokeSplit = _Class("CHTopDownStrokeSplit")
CHStrokeClutterFilter = _Class("CHStrokeClutterFilter")
CHSpellChecker = _Class("CHSpellChecker")
CHTokenizedTextResult = _Class("CHTokenizedTextResult")
CHMutableTokenizedTextResult = _Class("CHMutableTokenizedTextResult")
CHRecurrentNeuralNetwork = _Class("CHRecurrentNeuralNetwork")
CHRecurrentNeuralNetworkMontreal = _Class("CHRecurrentNeuralNetworkMontreal")
CHStrokeClassificationModel = _Class("CHStrokeClassificationModel")
CHCutpointModel = _Class("CHCutpointModel")
CHStrokeTransitionModel = _Class("CHStrokeTransitionModel")
CHRecurrentNeuralNetworkCoreML = _Class("CHRecurrentNeuralNetworkCoreML")
CHCTCRecognitionModel = _Class("CHCTCRecognitionModel")
CHTextInputGesture = _Class("CHTextInputGesture")
CHTextInputInsertionCaretGesture = _Class("CHTextInputInsertionCaretGesture")
CHPointFIFO = _Class("CHPointFIFO")
CHQuadCurvePointFIFO = _Class("CHQuadCurvePointFIFO")
CHBoxcarFilterPointFIFO = _Class("CHBoxcarFilterPointFIFO")
CHPointStrokeFIFO = _Class("CHPointStrokeFIFO")
CHSearchQueryItem = _Class("CHSearchQueryItem")
CHRecognitionResult = _Class("CHRecognitionResult")
CHSketchRecognitionResult = _Class("CHSketchRecognitionResult")
CHFreeformRecognitionResult = _Class("CHFreeformRecognitionResult")
CHCloudRecognitionResult = _Class("CHCloudRecognitionResult")
CHHeartRecognitionResult = _Class("CHHeartRecognitionResult")
CHScribbleRecognitionResult = _Class("CHScribbleRecognitionResult")
CHPentagonRecognitionResult = _Class("CHPentagonRecognitionResult")
CHStarRecognitionResult = _Class("CHStarRecognitionResult")
CHEllipseRecognitionResult = _Class("CHEllipseRecognitionResult")
CHChatBubbleRecognitionResult = _Class("CHChatBubbleRecognitionResult")
CHTriangleRecognitionResult = _Class("CHTriangleRecognitionResult")
CHRectangleSketchRecognitionResult = _Class("CHRectangleSketchRecognitionResult")
CHOutlinedArrowSketchRecognitionResult = _Class(
    "CHOutlinedArrowSketchRecognitionResult"
)
CHLineSketchRecognitionResult = _Class("CHLineSketchRecognitionResult")
CHManhattanLineSketchRecognitionResult = _Class(
    "CHManhattanLineSketchRecognitionResult"
)
CHTextRecognitionResult = _Class("CHTextRecognitionResult")
CHTextInputTarget = _Class("CHTextInputTarget")
CHRecognitionSessionTask = _Class("CHRecognitionSessionTask")
CHRecognitionSessionTextInputTask = _Class("CHRecognitionSessionTextInputTask")
CHStrokeGroup = _Class("CHStrokeGroup")
CHTimeWindowStrokeGroup = _Class("CHTimeWindowStrokeGroup")
CHOrderedStrokeGroup = _Class("CHOrderedStrokeGroup")
CHTextLineStrokeGroup = _Class("CHTextLineStrokeGroup")
CHTokenizedTextResultColumn = _Class("CHTokenizedTextResultColumn")
CHMutableTokenizedTextResultColumn = _Class("CHMutableTokenizedTextResultColumn")
CHRemoteRecognitionRequest = _Class("CHRemoteRecognitionRequest")
CHStrokeGroupTextCorrectionResult = _Class("CHStrokeGroupTextCorrectionResult")
CHStrokeGroupRecognitionResult = _Class("CHStrokeGroupRecognitionResult")
CHStrokeClassificationResult = _Class("CHStrokeClassificationResult")
CHMutableStrokeClassificationResult = _Class("CHMutableStrokeClassificationResult")
CHRecognitionSessionResult = _Class("CHRecognitionSessionResult")
CHTextInputProtoSettings = _Class("CHTextInputProtoSettings")
CHStrokeGroupingManager = _Class("CHStrokeGroupingManager")
CHStrokeGroupingResult = _Class("CHStrokeGroupingResult")
CHStrokeFastGroupingResult = _Class("CHStrokeFastGroupingResult")
CHBottomUpStrokeGroupingResult = _Class("CHBottomUpStrokeGroupingResult")
CHMergedStrokeGroupingResults = _Class("CHMergedStrokeGroupingResults")
CHCornerDetector = _Class("CHCornerDetector")
CHNonTextCandidateStroke = _Class("CHNonTextCandidateStroke")
CHMutableNonTextCandidateStroke = _Class("CHMutableNonTextCandidateStroke")
CHTextInputTargetContentInfo = _Class("CHTextInputTargetContentInfo")
CHMutableTextInputTargetContentInfo = _Class("CHMutableTextInputTargetContentInfo")
CHTextInputScriptSpec = _Class("CHTextInputScriptSpec")
CHVisualization = _Class("CHVisualization")
CHStrokeVisualization = _Class("CHStrokeVisualization")
CHStrokePointsVisualization = _Class("CHStrokePointsVisualization")
CHStrokeGroupBasedVisualization = _Class("CHStrokeGroupBasedVisualization")
CHStrokeGroupBaselineLegacyVisualization = _Class(
    "CHStrokeGroupBaselineLegacyVisualization"
)
CHGroupBoundsVisualization = _Class("CHGroupBoundsVisualization")
CHStrokeGroupingVisualization = _Class("CHStrokeGroupingVisualization")
CHStrokeGroupClassificationVisualization = _Class(
    "CHStrokeGroupClassificationVisualization"
)
CHSubstrokeBoundsVisualization = _Class("CHSubstrokeBoundsVisualization")
CHNormalizedDrawingVisualization = _Class("CHNormalizedDrawingVisualization")
CHNormalizedDrawingAllVisualization = _Class("CHNormalizedDrawingAllVisualization")
CHStrokeGroupBaselineVisualization = _Class("CHStrokeGroupBaselineVisualization")
CHDrawingSegmentGroup = _Class("CHDrawingSegmentGroup")
CHSegmentDescriptor = _Class("CHSegmentDescriptor")
CHCutPoint = _Class("CHCutPoint")
CHDrawing = _Class("CHDrawing")
CHRecognitionInsight = _Class("CHRecognitionInsight")
CHRecognitionInsightRequest = _Class("CHRecognitionInsightRequest")
CHStrokeUtilities = _Class("CHStrokeUtilities")
CHDrawingContext = _Class("CHDrawingContext")
CHRecognizer = _Class("CHRecognizer")
CHRecognizerOptions = _Class("CHRecognizerOptions")
CHTokenizedStrokeResult = _Class("CHTokenizedStrokeResult")
CHTokenizedTextResultToken = _Class("CHTokenizedTextResultToken")
CHMutableTokenizedTextResultToken = _Class("CHMutableTokenizedTextResultToken")
CHEncodedStrokeIdentifier = _Class("CHEncodedStrokeIdentifier")
CHStrokeGroupingStrategy = _Class("CHStrokeGroupingStrategy")
CHFastStrokeGroupingStrategy = _Class("CHFastStrokeGroupingStrategy")
CHBottomUpStrokeGroupingStrategy = _Class("CHBottomUpStrokeGroupingStrategy")
CHTimeWindowStrokeGroupingStrategy = _Class("CHTimeWindowStrokeGroupingStrategy")
CHTopDownStrokeGroupingStrategy = _Class("CHTopDownStrokeGroupingStrategy")
CHStrokeGroupQueryItem = _Class("CHStrokeGroupQueryItem")
CHQuery = _Class("CHQuery")
CHIndexableContentQuery = _Class("CHIndexableContentQuery")
CHTranscriptionQuery = _Class("CHTranscriptionQuery")
CHDataDetectorQuery = _Class("CHDataDetectorQuery")
CHTextInputQuery = _Class("CHTextInputQuery")
CHSearchQuery = _Class("CHSearchQuery")
CHTitleQuery = _Class("CHTitleQuery")
CHStrokeGroupQuery = _Class("CHStrokeGroupQuery")
CHLanguageUtilities = _Class("CHLanguageUtilities")
CHClassifiableDrawing = _Class("CHClassifiableDrawing")
CHSpellCheckerErrorModel = _Class("CHSpellCheckerErrorModel")
