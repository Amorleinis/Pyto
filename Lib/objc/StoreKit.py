"""
Classes from the 'StoreKit' framework.
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


SKCloudServiceController = _Class("SKCloudServiceController")
SKOverlay = _Class("SKOverlay")
_SKStoreProductActivityAnimationController = _Class(
    "_SKStoreProductActivityAnimationController"
)
SKAccountPageSpecifierProvider = _Class("SKAccountPageSpecifierProvider")
SKPurchaseIntent = _Class("SKPurchaseIntent")
SKPaymentQueueClient = _Class("SKPaymentQueueClient")
SKPaymentDiscount = _Class("SKPaymentDiscount")
SKPaymentDiscountInternal = _Class("SKPaymentDiscountInternal")
SKStorePageRequest = _Class("SKStorePageRequest")
SKStoreReviewController = _Class("SKStoreReviewController")
SKServiceProxy = _Class("SKServiceProxy")
SKInvocationQueueProxy = _Class("SKInvocationQueueProxy")
SKInternalProductStorePromotionController = _Class(
    "SKInternalProductStorePromotionController"
)
SKStorefront = _Class("SKStorefront")
SKCloudServiceSetupExtension = _Class("SKCloudServiceSetupExtension")
SKXPCConnection = _Class("SKXPCConnection")
SKCloudServiceSetupConfiguration = _Class("SKCloudServiceSetupConfiguration")
SKScrollDetector = _Class("SKScrollDetector")
SKWeakContainer = _Class("SKWeakContainer")
SKEntitlementChecker = _Class("SKEntitlementChecker")
SKAdNetwork = _Class("SKAdNetwork")
SKArcadeService = _Class("SKArcadeService")
SKProductStorePromotionController = _Class("SKProductStorePromotionController")
SKPrivacyController = _Class("SKPrivacyController")
SKOverlayConfiguration = _Class("SKOverlayConfiguration")
SKOverlayAppClipConfiguration = _Class("SKOverlayAppClipConfiguration")
SKOverlayAppConfiguration = _Class("SKOverlayAppConfiguration")
SKURLParserBagContract = _Class("SKURLParserBagContract")
SKProductSubscriptionPeriod = _Class("SKProductSubscriptionPeriod")
SKProductSubscriptionPeriodInternal = _Class("SKProductSubscriptionPeriodInternal")
SKPaymentTransactionInternal = _Class("SKPaymentTransactionInternal")
SKPaymentTransaction = _Class("SKPaymentTransaction")
SKRemoteDismissingTransition = _Class("SKRemoteDismissingTransition")
SKInGameAnalytics = _Class("SKInGameAnalytics")
SKOverlayTransitionContext = _Class("SKOverlayTransitionContext")
SKPaymentInternal = _Class("SKPaymentInternal")
SKPayment = _Class("SKPayment")
SKMutablePayment = _Class("SKMutablePayment")
SKCloudServiceSetupReloadContext = _Class("SKCloudServiceSetupReloadContext")
SKDownloadChangeset = _Class("SKDownloadChangeset")
SKDownload = _Class("SKDownload")
SKDownloadInternal = _Class("SKDownloadInternal")
SKProductDiscount = _Class("SKProductDiscount")
SKProductDiscountInternal = _Class("SKProductDiscountInternal")
SKProductInternal = _Class("SKProductInternal")
SKProduct = _Class("SKProduct")
SKProductsResponseInternal = _Class("SKProductsResponseInternal")
SKProductsResponse = _Class("SKProductsResponse")
SKProductsRequestInternal = _Class("SKProductsRequestInternal")
SKRequestInternal = _Class("SKRequestInternal")
SKRequest = _Class("SKRequest")
SKInstallSheetStatusUpdateRequest = _Class("SKInstallSheetStatusUpdateRequest")
SKPromotedIAPGetInfoInternalRequest = _Class("SKPromotedIAPGetInfoInternalRequest")
SKHandleInvalidReceiptRequest = _Class("SKHandleInvalidReceiptRequest")
SKReceiptRefreshRequest = _Class("SKReceiptRefreshRequest")
SKPromotedIAPSetOrderRequest = _Class("SKPromotedIAPSetOrderRequest")
SKPromotedIAPGetVisibilityRequest = _Class("SKPromotedIAPGetVisibilityRequest")
SKPromotedIAPSetVisibilityRequest = _Class("SKPromotedIAPSetVisibilityRequest")
SKPromotedIAPGetOrderRequest = _Class("SKPromotedIAPGetOrderRequest")
SKProductsRequest = _Class("SKProductsRequest")
SKWeakReference = _Class("SKWeakReference")
SKDefaultsManager = _Class("SKDefaultsManager")
SKPaymentQueueInternal = _Class("SKPaymentQueueInternal")
SKPaymentQueue = _Class("SKPaymentQueue")
SKSpecifierWithSubtitleCell = _Class("SKSpecifierWithSubtitleCell")
SKStoreReviewPresentationWindow = _Class("SKStoreReviewPresentationWindow")
SKStarRatingControl = _Class("SKStarRatingControl")
SKStorePageViewController = _Class("SKStorePageViewController")
SKStoreProductActivityViewController = _Class("SKStoreProductActivityViewController")
SKComposeReviewViewController = _Class("SKComposeReviewViewController")
SKCloudServiceSetupViewController = _Class("SKCloudServiceSetupViewController")
SKProductPageExtension = _Class("SKProductPageExtension")
SKStoreProductViewController = _Class("SKStoreProductViewController")
SKTermsPageViewController = _Class("SKTermsPageViewController")
SKAccountPageViewController = _Class("SKAccountPageViewController")
SKStoreReviewViewController = _Class("SKStoreReviewViewController")
SKArcadeSubscribeViewController = _Class("SKArcadeSubscribeViewController")
SKStoreExtension = _Class("SKStoreExtension")
SKRemoteProductActivityViewController = _Class("SKRemoteProductActivityViewController")
SKRemoteStorePageViewController = _Class("SKRemoteStorePageViewController")
SKRemoteComposeReviewViewController = _Class("SKRemoteComposeReviewViewController")
SKRemoteReviewViewController = _Class("SKRemoteReviewViewController")
SKRemoteProductViewController = _Class("SKRemoteProductViewController")
SKStoreRemoteViewController = _Class("SKStoreRemoteViewController")
SKCloudServiceSetupRemoteViewController = _Class(
    "SKCloudServiceSetupRemoteViewController"
)
SKRemoteAccountPageViewController = _Class("SKRemoteAccountPageViewController")
SKStarRatingAlertController = _Class("SKStarRatingAlertController")
