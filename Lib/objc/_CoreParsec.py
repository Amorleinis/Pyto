"""
Classes from the 'CoreParsec' framework.
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


PARReply = _Class("PARReply")
PARRequest = _Class("PARRequest")
PARFlightSearchRequest = _Class("PARFlightSearchRequest")
PARLookupRequest = _Class("PARLookupRequest")
PARZeroKeywordRequest = _Class("PARZeroKeywordRequest")
PARCardRequest = _Class("PARCardRequest")
PARMoreResultsRequest = _Class("PARMoreResultsRequest")
PARSearchRequest = _Class("PARSearchRequest")
PARSearchReplayRequest = _Class("PARSearchReplayRequest")
PARSession = _Class("PARSession")
PARHashtagImagesVisibility = _Class("PARHashtagImagesVisibility")
PARImageLoader = _Class("PARImageLoader")
PARResponse = _Class("PARResponse")
PARFlightResponse = _Class("PARFlightResponse")
PARTask = _Class("PARTask")
PARNewsVisibility = _Class("PARNewsVisibility")
PARSmartSearchV2Parameters = _Class("PARSmartSearchV2Parameters")
PARSmartSearchV1Parameters = _Class("PARSmartSearchV1Parameters")
PARFuture = _Class("PARFuture")
PARPromise = _Class("PARPromise")
FutureValue = _Class("FutureValue")
PARBag = _Class("PARBag")
PARSessionConfiguration = _Class("PARSessionConfiguration")
PARDefaultFactory = _Class("PARDefaultFactory")
PARSearchClient = _Class("PARSearchClient")
WeakSession = _Class("WeakSession")
PAREngagedCompletionCache = _Class("PAREngagedCompletionCache")
PARAsyncMoreResults = _Class("PARAsyncMoreResults")
PARAsyncCard = _Class("PARAsyncCard")
PARSyncCard = _Class("PARSyncCard")
_PARSilhouette_Topic = _Class("_PARSilhouette_Topic")
_PAREntity_Topic = _Class("_PAREntity_Topic")
_PARResult_Template = _Class("_PARResult_Template")
_PARSuggestion = _Class("_PARSuggestion")
_PARSubscriptions = _Class("_PARSubscriptions")
_PARQueryFeatures_Stats = _Class("_PARQueryFeatures_Stats")
_PARSilhouette = _Class("_PARSilhouette")
_PARSearchResponse_Section = _Class("_PARSearchResponse_Section")
_PARSearchResponse = _Class("_PARSearchResponse")
_PARSearchRequest = _Class("_PARSearchRequest")
_PARRevGeoResolution = _Class("_PARRevGeoResolution")
_PARResult = _Class("_PARResult")
_PARRendering = _Class("_PARRendering")
_PARSearchResponse_QuerySuggestion = _Class("_PARSearchResponse_QuerySuggestion")
_PARSearchResponse_QueryFeatures = _Class("_PARSearchResponse_QueryFeatures")
_PARMapsSession = _Class("_PARMapsSession")
_PARLocation = _Class("_PARLocation")
_PARFlightResponse = _Class("_PARFlightResponse")
_PARFlightRequest = _Class("_PARFlightRequest")
_PARSearchResponse_Error = _Class("_PARSearchResponse_Error")
_PAREntity = _Class("_PAREntity")
_PARSearchResponse_Correction = _Class("_PARSearchResponse_Correction")
_PARQueryFeatures_CategoryStats = _Class("_PARQueryFeatures_CategoryStats")
_PARCardResponse = _Class("_PARCardResponse")
_PARCardRequest = _Class("_PARCardRequest")
_PARBagResponse = _Class("_PARBagResponse")
_PARBagRequest = _Class("_PARBagRequest")
_CPVisibleSuggestionsFeedback = _Class("_CPVisibleSuggestionsFeedback")
_CPVisibleSectionHeaderFeedback = _Class("_CPVisibleSectionHeaderFeedback")
_CPVisibleResultsFeedback = _Class("_CPVisibleResultsFeedback")
_CPValue = _Class("_CPValue")
_CPUserReportFeedback = _Class("_CPUserReportFeedback")
_CPUsageSinceLookback = _Class("_CPUsageSinceLookback")
_CPUsageEnvelope = _Class("_CPUsageEnvelope")
_CPTuscanyConnectionInfo = _Class("_CPTuscanyConnectionInfo")
_CPTCPInfo = _Class("_CPTCPInfo")
_CPSuggestionEngagementFeedback = _Class("_CPSuggestionEngagementFeedback")
_CPStruct = _Class("_CPStruct")
_CPStoreCardSectionEngagementFeedback = _Class("_CPStoreCardSectionEngagementFeedback")
_CPStartSearchFeedback = _Class("_CPStartSearchFeedback")
_CPStartNetworkSearchFeedback = _Class("_CPStartNetworkSearchFeedback")
_CPStartLocalSearchFeedback = _Class("_CPStartLocalSearchFeedback")
_CPSpotlightUsagePropensity = _Class("_CPSpotlightUsagePropensity")
_CPSkipSearchFeedback = _Class("_CPSkipSearchFeedback")
_CPSessionMissingSuggestionsFeedback = _Class("_CPSessionMissingSuggestionsFeedback")
_CPSessionMissingResultsFeedback = _Class("_CPSessionMissingResultsFeedback")
_CPSessionEndFeedback = _Class("_CPSessionEndFeedback")
_CPSectionRankingFeedback = _Class("_CPSectionRankingFeedback")
_CPSectionEngagementFeedback = _Class("_CPSectionEngagementFeedback")
_CPSearchViewDisappearFeedback = _Class("_CPSearchViewDisappearFeedback")
_CPSearchViewAppearFeedback = _Class("_CPSearchViewAppearFeedback")
_CPSearchSuggestionForFeedback = _Class("_CPSearchSuggestionForFeedback")
_CPSearchResultForFeedback = _Class("_CPSearchResultForFeedback")
_CPSafariUsagePropensity = _Class("_CPSafariUsagePropensity")
_CPResultsReceivedAfterTimeoutFeedback = _Class(
    "_CPResultsReceivedAfterTimeoutFeedback"
)
_CPResultSectionForFeedback = _Class("_CPResultSectionForFeedback")
_CPResultRankingFeedback = _Class("_CPResultRankingFeedback")
_CPResultGradingFeedback = _Class("_CPResultGradingFeedback")
_CPResultFeedback = _Class("_CPResultFeedback")
_CPResultEngagementFeedback = _Class("_CPResultEngagementFeedback")
_CPRankingFeedback = _Class("_CPRankingFeedback")
_CPRange = _Class("_CPRange")
_CPPunchoutForFeedback = _Class("_CPPunchoutForFeedback")
_CPNewsUsagePropensity = _Class("_CPNewsUsagePropensity")
_CPNetworkTimingData = _Class("_CPNetworkTimingData")
_CPMapsCardSectionEngagementFeedback = _Class("_CPMapsCardSectionEngagementFeedback")
_CPLookupHintRelevancyFeedback = _Class("_CPLookupHintRelevancyFeedback")
_CPListValue = _Class("_CPListValue")
_CPLateSectionsAppendedFeedback = _Class("_CPLateSectionsAppendedFeedback")
_CPImagesUsagePropensity = _Class("_CPImagesUsagePropensity")
_CPFeedbackPayload = _Class("_CPFeedbackPayload")
_CPFeedback = _Class("_CPFeedback")
_CPErrorFeedback = _Class("_CPErrorFeedback")
_CPError = _Class("_CPError")
_CPEngagementTriggerRatio = _Class("_CPEngagementTriggerRatio")
_CPEngagementShareRatio = _Class("_CPEngagementShareRatio")
_CPEndSearchFeedback = _Class("_CPEndSearchFeedback")
_CPEndNetworkSearchFeedback = _Class("_CPEndNetworkSearchFeedback")
_CPEndLocalSearchFeedback = _Class("_CPEndLocalSearchFeedback")
_CPDidGoToSiteFeedback = _Class("_CPDidGoToSiteFeedback")
_CPDidGoToSearchFeedback = _Class("_CPDidGoToSearchFeedback")
_CPDeviceContext = _Class("_CPDeviceContext")
_CPCustomFeedback = _Class("_CPCustomFeedback")
_CPConnectionInvalidatedFeedback = _Class("_CPConnectionInvalidatedFeedback")
_CPClientTimingFeedback = _Class("_CPClientTimingFeedback")
_CPClientSession = _Class("_CPClientSession")
_CPClearInputFeedback = _Class("_CPClearInputFeedback")
_CPCardViewDisappearFeedback = _Class("_CPCardViewDisappearFeedback")
_CPCardViewAppearFeedback = _Class("_CPCardViewAppearFeedback")
_CPCardSectionForFeedback = _Class("_CPCardSectionForFeedback")
_CPCardSectionFeedback = _Class("_CPCardSectionFeedback")
_CPCardSectionEngagementFeedback = _Class("_CPCardSectionEngagementFeedback")
_CPCardForFeedback = _Class("_CPCardForFeedback")
_CPCacheHitFeedback = _Class("_CPCacheHitFeedback")
_CPCBAEngagementFeedback = _Class("_CPCBAEngagementFeedback")
_CPActionItemForFeedback = _Class("_CPActionItemForFeedback")
