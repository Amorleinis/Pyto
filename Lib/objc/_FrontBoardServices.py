"""
Classes from the 'FrontBoardServices' framework.
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


FBSDisplayLayoutTransitionContext = _Class("FBSDisplayLayoutTransitionContext")
FBSDisplaySource = _Class("FBSDisplaySource")
FBSApplicationUninstallOptions = _Class("FBSApplicationUninstallOptions")
FBSApplicationTrustFacade = _Class("FBSApplicationTrustFacade")
FBSDisplayMonitor = _Class("FBSDisplayMonitor")
FBSLegacySignatureValidationService = _Class("FBSLegacySignatureValidationService")
FBSApplicationTerminationAssertion = _Class("FBSApplicationTerminationAssertion")
FBSDisplayLayoutPublisherConfiguration = _Class(
    "FBSDisplayLayoutPublisherConfiguration"
)
FBSDisplayLayoutPublisher = _Class("FBSDisplayLayoutPublisher")
FBSSceneClientIdentity = _Class("FBSSceneClientIdentity")
FBSProcessWatchdogPolicy = _Class("FBSProcessWatchdogPolicy")
FBSApplicationLibraryConfiguration = _Class("FBSApplicationLibraryConfiguration")
FBSSceneSnapshotRequestHandle = _Class("FBSSceneSnapshotRequestHandle")
FBSShutdownOptions = _Class("FBSShutdownOptions")
_FBSSnapshotLayer = _Class("_FBSSnapshotLayer")
_FBSSnapshotContext = _Class("_FBSSnapshotContext")
_FBSSnapshot = _Class("_FBSSnapshot")
FBSProcessTerminationRequest = _Class("FBSProcessTerminationRequest")
FBSDisplayConfigurationRequest = _Class("FBSDisplayConfigurationRequest")
FBSMutableDisplayConfigurationRequest = _Class("FBSMutableDisplayConfigurationRequest")
FBSProcess = _Class("FBSProcess")
FBSXPCMessage = _Class("FBSXPCMessage")
FBSApplicationLibrary = _Class("FBSApplicationLibrary")
FBSALOToken = _Class("FBSALOToken")
_FBMapResult = _Class("_FBMapResult")
FBSSceneIdentity = _Class("FBSSceneIdentity")
FBSMutableSceneIdentity = _Class("FBSMutableSceneIdentity")
FBSApplicationPlaceholderProgress = _Class("FBSApplicationPlaceholderProgress")
FBSProfileManager = _Class("FBSProfileManager")
FBSSceneSnapshotContext = _Class("FBSSceneSnapshotContext")
FBSProcessExecutionPolicy = _Class("FBSProcessExecutionPolicy")
FBSProcessExecutionStrategy = _Class("FBSProcessExecutionStrategy")
FBSMutableProcessExecutionStrategy = _Class("FBSMutableProcessExecutionStrategy")
FBSSystemService = _Class("FBSSystemService")
FBSDataResetRequest = _Class("FBSDataResetRequest")
_FBSDisplayLayoutServiceAssertion = _Class("_FBSDisplayLayoutServiceAssertion")
_FBSDisplayLayoutEndpointServices = _Class("_FBSDisplayLayoutEndpointServices")
_FBSDisplayLayoutService = _Class("_FBSDisplayLayoutService")
FBSDisplayLayoutMonitorConfiguration = _Class("FBSDisplayLayoutMonitorConfiguration")
FBSDisplayLayoutMonitor = _Class("FBSDisplayLayoutMonitor")
FBSProcessExecutionProvision = _Class("FBSProcessExecutionProvision")
FBSProcessResourceProvision = _Class("FBSProcessResourceProvision")
FBSApplicationDataStore = _Class("FBSApplicationDataStore")
FBSProcessAssertion = _Class("FBSProcessAssertion")
FBSDisplayLayout = _Class("FBSDisplayLayout")
FBSSceneOcclusion = _Class("FBSSceneOcclusion")
FBSApplicationDataStoreMonitor = _Class("FBSApplicationDataStoreMonitor")
FBSSceneActivitySession = _Class("FBSSceneActivitySession")
FBSOpenApplicationOptions = _Class("FBSOpenApplicationOptions")
FBSLazyApplicationInfoProvider = _Class("FBSLazyApplicationInfoProvider")
FBSProcessWatchdog = _Class("FBSProcessWatchdog")
FBSSceneDefinition = _Class("FBSSceneDefinition")
FBSMutableSceneDefinition = _Class("FBSMutableSceneDefinition")
FBSServiceFacility = _Class("FBSServiceFacility")
FBSDisplayLayoutElement = _Class("FBSDisplayLayoutElement")
FBSOrientationObserver = _Class("FBSOrientationObserver")
FBSOrientationUpdate = _Class("FBSOrientationUpdate")
FBSServiceFacilityClient = _Class("FBSServiceFacilityClient")
FBSSystemAppProxy = _Class("FBSSystemAppProxy")
FBSOrientationObserverClient = _Class("FBSOrientationObserverClient")
FBSApplicationDataStoreRepositoryClient = _Class(
    "FBSApplicationDataStoreRepositoryClient"
)
FBSSystemServiceSpecification = _Class("FBSSystemServiceSpecification")
FBSApplicationDataStoreClientFactory = _Class("FBSApplicationDataStoreClientFactory")
FBSSignatureValidationService = _Class("FBSSignatureValidationService")
_FBSMISInterfaceWrapperImpl = _Class("_FBSMISInterfaceWrapperImpl")
FBSApplicationProvisioningProfile = _Class("FBSApplicationProvisioningProfile")
_FBSCDHashCacheInfo = _Class("_FBSCDHashCacheInfo")
FBSBundleInfo = _Class("FBSBundleInfo")
FBSExtensionInfo = _Class("FBSExtensionInfo")
FBSApplicationPlaceholder = _Class("FBSApplicationPlaceholder")
FBSApplicationInfo = _Class("FBSApplicationInfo")
FBSSceneSnapshotRequest = _Class("FBSSceneSnapshotRequest")
FBSSettingsDiffInspector = _Class("FBSSettingsDiffInspector")
FBSSceneClientSettingsDiffInspector = _Class("FBSSceneClientSettingsDiffInspector")
FBSSceneSettingsDiffInspector = _Class("FBSSceneSettingsDiffInspector")
FBSSceneLayer = _Class("FBSSceneLayer")
FBSExternalSceneLayer = _Class("FBSExternalSceneLayer")
FBSKeyboardProxyLayer = _Class("FBSKeyboardProxyLayer")
FBSKeyboardLayer = _Class("FBSKeyboardLayer")
FBSCAContextSceneLayer = _Class("FBSCAContextSceneLayer")
FBSSceneIdentityToken = _Class("FBSSceneIdentityToken")
FBSBasicSceneAgent = _Class("FBSBasicSceneAgent")
FBSBasicSceneHostAgent = _Class("FBSBasicSceneHostAgent")
FBSBasicSceneClientAgent = _Class("FBSBasicSceneClientAgent")
FBSScene = _Class("FBSScene")
FBSDisplayMode = _Class("FBSDisplayMode")
FBSDisplayIdentity = _Class("FBSDisplayIdentity")
FBSDisplayConfiguration = _Class("FBSDisplayConfiguration")
FBSSceneClientSettings = _Class("FBSSceneClientSettings")
FBSMutableSceneClientSettings = _Class("FBSMutableSceneClientSettings")
FBSSceneSettings = _Class("FBSSceneSettings")
FBSMutableSceneSettings = _Class("FBSMutableSceneSettings")
FBSSceneSpecification = _Class("FBSSceneSpecification")
FBSProcessHandle = _Class("FBSProcessHandle")
FBSSceneParameters = _Class("FBSSceneParameters")
FBSMutableSceneParameters = _Class("FBSMutableSceneParameters")
FBSWorkspaceSceneRequestOptions = _Class("FBSWorkspaceSceneRequestOptions")
FBSWorkspaceSceneRemnant = _Class("FBSWorkspaceSceneRemnant")
_FBSTestExitAction = _Class("_FBSTestExitAction")
FBSSceneAction = _Class("FBSSceneAction")
FBSSceneSnapshotAction = _Class("FBSSceneSnapshotAction")
FBSSceneSnapshotRequestAction = _Class("FBSSceneSnapshotRequestAction")
FBSSceneMessage = _Class("FBSSceneMessage")
FBSSceneEvent = _Class("FBSSceneEvent")
FBSSceneTransitionContext = _Class("FBSSceneTransitionContext")
FBSSettingsDiff = _Class("FBSSettingsDiff")
FBSSceneSettingsDiff = _Class("FBSSceneSettingsDiff")
FBSSceneClientSettingsDiff = _Class("FBSSceneClientSettingsDiff")
FBSWorkspaceResponse = _Class("FBSWorkspaceResponse")
FBSWorkspaceSceneUpdateResponse = _Class("FBSWorkspaceSceneUpdateResponse")
FBSWorkspaceCreateSceneResponse = _Class("FBSWorkspaceCreateSceneResponse")
FBSWorkspaceDestroySceneResponse = _Class("FBSWorkspaceDestroySceneResponse")
FBSUIApplicationLaunchResponse = _Class("FBSUIApplicationLaunchResponse")
FBSWorkspaceFencingImpl = _Class("FBSWorkspaceFencingImpl")
FBSWorkspaceServiceSpecification = _Class("FBSWorkspaceServiceSpecification")
FBSWorkspaceScenesClient = _Class("FBSWorkspaceScenesClient")
FBSWorkspaceInitializationOptions = _Class("FBSWorkspaceInitializationOptions")
FBSUIApplicationWorkspaceShim = _Class("FBSUIApplicationWorkspaceShim")
FBSSerialQueue = _Class("FBSSerialQueue")
FBSWorkspace = _Class("FBSWorkspace")
FBSUIApplicationWorkspace = _Class("FBSUIApplicationWorkspace")
FBSOpenApplicationServiceSpecification = _Class(
    "FBSOpenApplicationServiceSpecification"
)
FBSOpenApplicationService = _Class("FBSOpenApplicationService")
