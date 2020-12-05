"""
Classes from the 'AVFCapture' framework.
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


AVMomentCaptureMovie = _Class("AVMomentCaptureMovie")
AVCapturePhotoOutputInternal = _Class("AVCapturePhotoOutputInternal")
AVCaptureSessionInternal = _Class("AVCaptureSessionInternal")
AVFrameRateRange = _Class("AVFrameRateRange")
AVFrameRateRangeInternal = _Class("AVFrameRateRangeInternal")
AVCaptureMetadataOutputInternal = _Class("AVCaptureMetadataOutputInternal")
AVCaptureBracketedStillImageSettings = _Class("AVCaptureBracketedStillImageSettings")
AVCaptureAutoExposureBracketedStillImageSettings = _Class(
    "AVCaptureAutoExposureBracketedStillImageSettings"
)
AVCaptureManualExposureBracketedStillImageSettings = _Class(
    "AVCaptureManualExposureBracketedStillImageSettings"
)
AVCaptureVideoPreviewLayerInternal = _Class("AVCaptureVideoPreviewLayerInternal")
AVCaptureDeviceControlRequestQueue = _Class("AVCaptureDeviceControlRequestQueue")
AVCaptureDeviceControlRequest = _Class("AVCaptureDeviceControlRequest")
AVCaptureDeviceFakeBiasControlRequest = _Class("AVCaptureDeviceFakeBiasControlRequest")
AVCaptureSynchronizedVisionDataInternal = _Class(
    "AVCaptureSynchronizedVisionDataInternal"
)
AVCaptureSynchronizedDepthDataInternal = _Class(
    "AVCaptureSynchronizedDepthDataInternal"
)
AVCaptureSynchronizedMetadataObjectDataInternal = _Class(
    "AVCaptureSynchronizedMetadataObjectDataInternal"
)
AVCaptureSynchronizedSampleBufferDataInternal = _Class(
    "AVCaptureSynchronizedSampleBufferDataInternal"
)
AVCaptureSynchronizedData = _Class("AVCaptureSynchronizedData")
AVCaptureSynchronizedCameraCalibrationData = _Class(
    "AVCaptureSynchronizedCameraCalibrationData"
)
AVCaptureSynchronizedPointCloudData = _Class("AVCaptureSynchronizedPointCloudData")
AVCaptureSynchronizedVisionData = _Class("AVCaptureSynchronizedVisionData")
AVCaptureSynchronizedDepthData = _Class("AVCaptureSynchronizedDepthData")
AVCaptureSynchronizedMetadataObjectData = _Class(
    "AVCaptureSynchronizedMetadataObjectData"
)
AVCaptureSynchronizedSampleBufferData = _Class("AVCaptureSynchronizedSampleBufferData")
AVCaptureSynchronizedDataInternal = _Class("AVCaptureSynchronizedDataInternal")
AVCaptureSessionConfiguration = _Class("AVCaptureSessionConfiguration")
AVCaptureInputInternal = _Class("AVCaptureInputInternal")
AVApplePortraitMetadata = _Class("AVApplePortraitMetadata")
AVApplePortraitMetadataInternal = _Class("AVApplePortraitMetadataInternal")
AVPortraitEffectsMatte = _Class("AVPortraitEffectsMatte")
AVPortraitEffectsMatteInternal = _Class("AVPortraitEffectsMatteInternal")
AVCaptureAudioDataOutputInternal = _Class("AVCaptureAudioDataOutputInternal")
AVCaptureDeferredPhotoProcessor = _Class("AVCaptureDeferredPhotoProcessor")
AVCaptureDeferredPhotoProcessingRequest = _Class(
    "AVCaptureDeferredPhotoProcessingRequest"
)
AVCaptureDataOutputSynchronizer = _Class("AVCaptureDataOutputSynchronizer")
AVCaptureDataOutputSynchronizerInternal = _Class(
    "AVCaptureDataOutputSynchronizerInternal"
)
AVCDOSDataOutputStorage = _Class("AVCDOSDataOutputStorage")
AVCaptureDataOutputDelegateCallbackHelper = _Class(
    "AVCaptureDataOutputDelegateCallbackHelper"
)
AVCaptureInputPort = _Class("AVCaptureInputPort")
AVCaptureInputPortInternal = _Class("AVCaptureInputPortInternal")
AVCaptureSession = _Class("AVCaptureSession")
AVCaptureMultiCamSession = _Class("AVCaptureMultiCamSession")
AVMetadataMachineReadableCodeObjectInternal = _Class(
    "AVMetadataMachineReadableCodeObjectInternal"
)
AVMetadataOfflineVideoStabilizationMotionObjectInternal = _Class(
    "AVMetadataOfflineVideoStabilizationMotionObjectInternal"
)
AVMetadataTrackedFacesObjectInternal = _Class("AVMetadataTrackedFacesObjectInternal")
AVMetadataFaceObjectInternal = _Class("AVMetadataFaceObjectInternal")
AVMetadataObject = _Class("AVMetadataObject")
AVMetadataVideoPreviewHistogramObject = _Class("AVMetadataVideoPreviewHistogramObject")
AVMetadataMachineReadableCodeObject = _Class("AVMetadataMachineReadableCodeObject")
AVMetadataOfflineVideoStabilizationMotionObject = _Class(
    "AVMetadataOfflineVideoStabilizationMotionObject"
)
AVMetadataTrackedFacesObject = _Class("AVMetadataTrackedFacesObject")
AVMetadataFaceObject = _Class("AVMetadataFaceObject")
AVMetadataSaliencyHeatMap = _Class("AVMetadataSaliencyHeatMap")
AVMetadataSalientObject = _Class("AVMetadataSalientObject")
AVMetadataBodyObject = _Class("AVMetadataBodyObject")
AVMetadataDogBodyObject = _Class("AVMetadataDogBodyObject")
AVMetadataCatBodyObject = _Class("AVMetadataCatBodyObject")
AVMetadataHumanBodyObject = _Class("AVMetadataHumanBodyObject")
AVMetadataObjectInternal = _Class("AVMetadataObjectInternal")
AVCaptureMovieFileOutputInternal = _Class("AVCaptureMovieFileOutputInternal")
AVCameraCalibrationData = _Class("AVCameraCalibrationData")
AVCameraCalibrationDataInternal = _Class("AVCameraCalibrationDataInternal")
AVMomentCaptureMovieRecordingResolvedSettings = _Class(
    "AVMomentCaptureMovieRecordingResolvedSettings"
)
AVMomentCaptureMovieRecordingSettings = _Class("AVMomentCaptureMovieRecordingSettings")
AVMomentCaptureMovieRequest = _Class("AVMomentCaptureMovieRequest")
AVCaptureStillImageOutputInternal = _Class("AVCaptureStillImageOutputInternal")
AVCapturePrepareBracketRequest = _Class("AVCapturePrepareBracketRequest")
AVCaptureStillImageRequest = _Class("AVCaptureStillImageRequest")
AVCaptureSynchronizedDataCollectionInternal = _Class(
    "AVCaptureSynchronizedDataCollectionInternal"
)
AVCaptureDevice = _Class("AVCaptureDevice")
AVCaptureFigAudioDevice = _Class("AVCaptureFigAudioDevice")
AVCaptureFigVideoDevice = _Class("AVCaptureFigVideoDevice")
AVCaptureDeviceInternal = _Class("AVCaptureDeviceInternal")
AVCaptureVisionDataOutputInternal = _Class("AVCaptureVisionDataOutputInternal")
AVCapturePhotoRequest = _Class("AVCapturePhotoRequest")
AVCaptureDeviceInputInternal = _Class("AVCaptureDeviceInputInternal")
AVOfflineVideoStabilizer = _Class("AVOfflineVideoStabilizer")
AVCaptureConnection = _Class("AVCaptureConnection")
AVCaptureConnectionInternal = _Class("AVCaptureConnectionInternal")
AVCaptureAudioChannel = _Class("AVCaptureAudioChannel")
AVCaptureAudioChannelInternal = _Class("AVCaptureAudioChannelInternal")
AVCaptureVideoDataOutputInternal = _Class("AVCaptureVideoDataOutputInternal")
AVDepthData = _Class("AVDepthData")
AVDepthDataInternal = _Class("AVDepthDataInternal")
AVMomentCaptureSettings = _Class("AVMomentCaptureSettings")
AVCapturePreparedPhotoSettingsArrayRequest = _Class(
    "AVCapturePreparedPhotoSettingsArrayRequest"
)
AVCapturePhotoInitiationSettings = _Class("AVCapturePhotoInitiationSettings")
AVCapturePhotoInitiationSettingsInternal = _Class(
    "AVCapturePhotoInitiationSettingsInternal"
)
AVCaptureResolvedPhotoSettings = _Class("AVCaptureResolvedPhotoSettings")
AVCaptureResolvedPhotoSettingsInternal = _Class(
    "AVCaptureResolvedPhotoSettingsInternal"
)
AVCapturePhotoBracketSettingsInternal = _Class("AVCapturePhotoBracketSettingsInternal")
AVCapturePhotoSettings = _Class("AVCapturePhotoSettings")
AVCapturePhotoBracketSettings = _Class("AVCapturePhotoBracketSettings")
AVCapturePhotoSettingsInternal = _Class("AVCapturePhotoSettingsInternal")
AVCaptureVideoSettingsValidator = _Class("AVCaptureVideoSettingsValidator")
AVCaptureOutputInternal = _Class("AVCaptureOutputInternal")
AVCaptureDeviceFormat = _Class("AVCaptureDeviceFormat")
AVCaptureDeviceFormatInternal = _Class("AVCaptureDeviceFormatInternal")
AVCapturePhotoPrivateClientMetadata = _Class("AVCapturePhotoPrivateClientMetadata")
AVPointCloudData = _Class("AVPointCloudData")
AVCaptureDeviceDiscoverySession = _Class("AVCaptureDeviceDiscoverySession")
AVCaptureDepthDataOutputInternal = _Class("AVCaptureDepthDataOutputInternal")
AVSemanticSegmentationMatte = _Class("AVSemanticSegmentationMatte")
AVCaptureSystemPressureState = _Class("AVCaptureSystemPressureState")
AVCaptureSystemPressureStateInternal = _Class("AVCaptureSystemPressureStateInternal")
AVCaptureInput = _Class("AVCaptureInput")
AVCaptureDeviceInput = _Class("AVCaptureDeviceInput")
AVCaptureMetadataInput = _Class("AVCaptureMetadataInput")
AVCaptureMetadataInputInternal = _Class("AVCaptureMetadataInputInternal")
AVFlashlight = _Class("AVFlashlight")
AVFlashlightInternal = _Class("AVFlashlightInternal")
AVCapturePhoto = _Class("AVCapturePhoto")
AVCaptureDeferredPhotoProxy = _Class("AVCaptureDeferredPhotoProxy")
AVCapturePhotoInternal = _Class("AVCapturePhotoInternal")
AVCaptureVideoThumbnailOutputInternal = _Class("AVCaptureVideoThumbnailOutputInternal")
AVCaptureOutput = _Class("AVCaptureOutput")
AVCapturePhotoOutput = _Class("AVCapturePhotoOutput")
AVCaptureMetadataOutput = _Class("AVCaptureMetadataOutput")
AVCaptureAudioDataOutput = _Class("AVCaptureAudioDataOutput")
AVCaptureStillImageOutput = _Class("AVCaptureStillImageOutput")
AVCapturePointCloudDataOutput = _Class("AVCapturePointCloudDataOutput")
AVCaptureCameraCalibrationDataOutput = _Class("AVCaptureCameraCalibrationDataOutput")
AVCaptureVisionDataOutput = _Class("AVCaptureVisionDataOutput")
AVCaptureVideoDataOutput = _Class("AVCaptureVideoDataOutput")
AVCaptureDepthDataOutput = _Class("AVCaptureDepthDataOutput")
AVCaptureVideoThumbnailOutput = _Class("AVCaptureVideoThumbnailOutput")
AVCaptureFileOutput = _Class("AVCaptureFileOutput")
AVCaptureMovieFileOutput = _Class("AVCaptureMovieFileOutput")
AVCaptureFileOutputInternal = _Class("AVCaptureFileOutputInternal")
AVCaptureFileOutputDelegateWrapper = _Class("AVCaptureFileOutputDelegateWrapper")
AVMomentCaptureMovieFileOutputDelegateWrapper = _Class(
    "AVMomentCaptureMovieFileOutputDelegateWrapper"
)
AVCaptureSynchronizedDataCollection = _Class("AVCaptureSynchronizedDataCollection")
AVCaptureVideoPreviewLayer = _Class("AVCaptureVideoPreviewLayer")
AVSpatialOverCaptureVideoPreviewLayer = _Class("AVSpatialOverCaptureVideoPreviewLayer")
