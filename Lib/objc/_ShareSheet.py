"""
Classes from the 'ShareSheet' framework.
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


_UIActivityPlaceholderItemProxy = _Class("_UIActivityPlaceholderItemProxy")
_UIActivityDiscoveryContext = _Class("_UIActivityDiscoveryContext")
_UIOpenInAppActivityDataProvider = _Class("_UIOpenInAppActivityDataProvider")
UIAirDropExtensionItemDataSource = _Class("UIAirDropExtensionItemDataSource")
_UIActivityUserDefaults = _Class("_UIActivityUserDefaults")
_UIActivityMatchingResults = _Class("_UIActivityMatchingResults")
_UIActivityHelper = _Class("_UIActivityHelper")
_UIActivitySortItem = _Class("_UIActivitySortItem")
_UIActivityRecipientManager = _Class("_UIActivityRecipientManager")
UIDocumentInteractionControllerDismissMarkupAction = _Class(
    "UIDocumentInteractionControllerDismissMarkupAction"
)
_UISaveToCameraRollSaveItemsController = _Class(
    "_UISaveToCameraRollSaveItemsController"
)
UISUIActivityConfiguration = _Class("UISUIActivityConfiguration")
UISUIActivityExtensionItemDataRequest = _Class("UISUIActivityExtensionItemDataRequest")
UISUISecurityContext = _Class("UISUISecurityContext")
_UIActivityItemMapping = _Class("_UIActivityItemMapping")
_UIActivityUserDefaultsManager = _Class("_UIActivityUserDefaultsManager")
_UIActivityItemCustomization = _Class("_UIActivityItemCustomization")
_UIActivityItemCustomizationCustom = _Class("_UIActivityItemCustomizationCustom")
_UIActivityItemCustomizationPicker = _Class("_UIActivityItemCustomizationPicker")
_UIActivityItemCustomizationSwitch = _Class("_UIActivityItemCustomizationSwitch")
_UIActivityMatchingContext = _Class("_UIActivityMatchingContext")
_UIShareServiceActivityProxy = _Class("_UIShareServiceActivityProxy")
_UIShareServiceActivityProxy_Share = _Class("_UIShareServiceActivityProxy_Share")
_UIShareServiceActivityProxy_Action = _Class("_UIShareServiceActivityProxy_Action")
UISUIActivityExtensionItemData = _Class("UISUIActivityExtensionItemData")
_UIDICPreviewItem = _Class("_UIDICPreviewItem")
_UIActivityApplicationExtensionDiscovery = _Class(
    "_UIActivityApplicationExtensionDiscovery"
)
UISDActivityItemData = _Class("UISDActivityItemData")
UIAirDropNode = _Class("UIAirDropNode")
SFShareSheetSlotManager = _Class("SFShareSheetSlotManager")
UISUIActivityViewControllerConfiguration = _Class(
    "UISUIActivityViewControllerConfiguration"
)
UISUISecurityScopedResource = _Class("UISUISecurityScopedResource")
UISUIOpenInByCopySecurityScopedResource = _Class(
    "UISUIOpenInByCopySecurityScopedResource"
)
UISUIAirDropSecurityScopedResource = _Class("UISUIAirDropSecurityScopedResource")
_UIHostActivityProxy = _Class("_UIHostActivityProxy")
UISDShareSheetSessionConfiguration = _Class("UISDShareSheetSessionConfiguration")
_UIActivityItemCustomizationGroup = _Class("_UIActivityItemCustomizationGroup")
UICreatePDFActivityItem = _Class("UICreatePDFActivityItem")
_UIActivityResourceLoader = _Class("_UIActivityResourceLoader")
_UIActivityBundleHelper = _Class("_UIActivityBundleHelper")
_UIActivityBundleImageConfiguration = _Class("_UIActivityBundleImageConfiguration")
UIActivityItemImageRep = _Class("UIActivityItemImageRep")
UIActivityItemURLRep = _Class("UIActivityItemURLRep")
_UIActivityApplicationExtensionsCache = _Class("_UIActivityApplicationExtensionsCache")
_UIMatchingExtensionsResult = _Class("_UIMatchingExtensionsResult")
_UIUserDefaultsActivityProxy = _Class("_UIUserDefaultsActivityProxy")
UIActivityItemCustomization = _Class("UIActivityItemCustomization")
_UIActivityUserDefaultsDataSource = _Class("_UIActivityUserDefaultsDataSource")
_UIActivityGroupViewFlowLayout = _Class("_UIActivityGroupViewFlowLayout")
_UIActivityCollectionViewCompositionalLayout = _Class(
    "_UIActivityCollectionViewCompositionalLayout"
)
UICreatePDFActivityPrintPaper = _Class("UICreatePDFActivityPrintPaper")
UIDocumentInteractionController = _Class("UIDocumentInteractionController")
UIActivity = _Class("UIActivity")
_UIPlaceholderActivity = _Class("_UIPlaceholderActivity")
UIAssignToContactActivity = _Class("UIAssignToContactActivity")
UIOpenInIBooksActivity = _Class("UIOpenInIBooksActivity")
UISaveToCameraRollActivity = _Class("UISaveToCameraRollActivity")
UIAddToReadingListActivity = _Class("UIAddToReadingListActivity")
_UIUserDefaultsActivity = _Class("_UIUserDefaultsActivity")
UIPrintActivity = _Class("UIPrintActivity")
UICreatePDFActivity = _Class("UICreatePDFActivity")
_UIDICActionActivity = _Class("_UIDICActionActivity")
UICopyToPasteboardActivity = _Class("UICopyToPasteboardActivity")
UIMessageActivity = _Class("UIMessageActivity")
_UICloudSharingActivity = _Class("_UICloudSharingActivity")
UIMailActivity = _Class("UIMailActivity")
UIApplicationExtensionActivity = _Class("UIApplicationExtensionActivity")
UIShortcutActivity = _Class("UIShortcutActivity")
UISocialActivity = _Class("UISocialActivity")
UIFileProviderApplicationExtensionActivity = _Class(
    "UIFileProviderApplicationExtensionActivity"
)
SUIShareActivity = _Class("SUIShareActivity")
UIAirDropActivity = _Class("UIAirDropActivity")
_UIActivityDragGestureRecognizer = _Class("_UIActivityDragGestureRecognizer")
_UIAirDropProgressLayer = _Class("_UIAirDropProgressLayer")
UIActivityItemProvider = _Class("UIActivityItemProvider")
_UIDICActivityItemProvider = _Class("_UIDICActivityItemProvider")
_UIActivityItemsConfigurationActivityItemProvider = _Class(
    "_UIActivityItemsConfigurationActivityItemProvider"
)
_UIAirDropProgressView = _Class("_UIAirDropProgressView")
_UIActivityContentTitleView = _Class("_UIActivityContentTitleView")
_UIActivityContentCollectionView = _Class("_UIActivityContentCollectionView")
_UIActivityUserDefaultsActivityCell = _Class("_UIActivityUserDefaultsActivityCell")
_UIActivityContentFooterView = _Class("_UIActivityContentFooterView")
UIShareGroupActivityCell = _Class("UIShareGroupActivityCell")
_UIActivityGroupActivityCell = _Class("_UIActivityGroupActivityCell")
UIAirDropGroupActivityCell = _Class("UIAirDropGroupActivityCell")
_UIMagicHeadCollectionViewCell = _Class("_UIMagicHeadCollectionViewCell")
UIActivityActionGroupCell = _Class("UIActivityActionGroupCell")
_UIActivityGroupActivityCellTitleLabel = _Class(
    "_UIActivityGroupActivityCellTitleLabel"
)
_UIActivityActionCellTitleLabel = _Class("_UIActivityActionCellTitleLabel")
_UIActivityContentNavigationBar = _Class("_UIActivityContentNavigationBar")
_UIUserDefaultsActivityPresentableViewController = _Class(
    "_UIUserDefaultsActivityPresentableViewController"
)
UIActivityContentViewController = _Class("UIActivityContentViewController")
ObjectManipulationViewController = _Class("ObjectManipulationViewController")
_UIActivityUserDefaultsViewController = _Class("_UIActivityUserDefaultsViewController")
UIActivityViewController = _Class("UIActivityViewController")
_UIDICActivityViewController = _Class("_UIDICActivityViewController")
UIApplicationExtensionViewControllerHost = _Class(
    "UIApplicationExtensionViewControllerHost"
)
UIActivityGroupViewController = _Class("UIActivityGroupViewController")
UIPrintActivityWrapperNavigationController = _Class(
    "UIPrintActivityWrapperNavigationController"
)
_UIActivityNavigationController = _Class("_UIActivityNavigationController")
_UIUserDefaultsActivityNavigationController = _Class(
    "_UIUserDefaultsActivityNavigationController"
)
