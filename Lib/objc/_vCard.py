"""
Classes from the 'vCard' framework.
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


CNVCardData = _Class("CNVCardData")
CNVCardUserDefaults = _Class("CNVCardUserDefaults")
CNVCardNameComponentPostProcessor = _Class("CNVCardNameComponentPostProcessor")
CNVCardProdIdString = _Class("CNVCardProdIdString")
CNVCardEncoding = _Class("CNVCardEncoding")
CNVCardValueEncoder = _Class("CNVCardValueEncoder")
CNVCardParameter = _Class("CNVCardParameter")
CNVCardWritingOptions = _Class("CNVCardWritingOptions")
CNVCardOptions = _Class("CNVCardOptions")
CNVCardNameComponents = _Class("CNVCardNameComponents")
CNVCardMutableNameComponents = _Class("CNVCardMutableNameComponents")
CNMECARDParser = _Class("CNMECARDParser")
_CNVCardParsingConcurrentStrategy = _Class("_CNVCardParsingConcurrentStrategy")
_CNVCardParsingSerialStrategy = _Class("_CNVCardParsingSerialStrategy")
CNVCardParsingConcurrencyStrategy = _Class("CNVCardParsingConcurrencyStrategy")
CNVCardNameSerialization = _Class("CNVCardNameSerialization")
CNVCard30PHOTOHelper = _Class("CNVCard30PHOTOHelper")
CNVCardPropertyItem = _Class("CNVCardPropertyItem")
CNVCardParameterEncoder = _Class("CNVCardParameterEncoder")
CNVCardParameterDecoder = _Class("CNVCardParameterDecoder")
CNVCardFilteredPersonScope = _Class("CNVCardFilteredPersonScope")
CNVCardDataStorage = _Class("CNVCardDataStorage")
CNVCardStringStorage = _Class("CNVCardStringStorage")
CNVCardSerializationStorage = _Class("CNVCardSerializationStorage")
CNVCardLineSerializationStrategyImpl = _Class("CNVCardLineSerializationStrategyImpl")
CNVCardLine21SerializationStrategy = _Class("CNVCardLine21SerializationStrategy")
CNVCardLine30SerializationStrategy = _Class("CNVCardLine30SerializationStrategy")
CNVCardLineSerializationStrategy = _Class("CNVCardLineSerializationStrategy")
CNVCardLineGenerator = _Class("CNVCardLineGenerator")
CNVCardActivityAlertLineGenerator = _Class("CNVCardActivityAlertLineGenerator")
CNVCardStreetAddressLineGenerator = _Class("CNVCardStreetAddressLineGenerator")
CNVCardPhoneLineGenerator = _Class("CNVCardPhoneLineGenerator")
CNVCardEmailLineGenerator = _Class("CNVCardEmailLineGenerator")
CNVCardSocialProfileLineGenerator = _Class("CNVCardSocialProfileLineGenerator")
CNVCardLegacyInstantMessagingLineGenerator = _Class(
    "CNVCardLegacyInstantMessagingLineGenerator"
)
CNVCardInstantMessagingLineGenerator = _Class("CNVCardInstantMessagingLineGenerator")
CNVCardAlternateDateComponentsLineGenerator = _Class(
    "CNVCardAlternateDateComponentsLineGenerator"
)
CNVCardDateComponentsLineGenerator = _Class("CNVCardDateComponentsLineGenerator")
CNVCardLineFactory = _Class("CNVCardLineFactory")
CNVCardImage = _Class("CNVCardImage")
CNVCardMutableImage = _Class("CNVCardMutableImage")
CGImageRefWithFormat = _Class("CGImageRefWithFormat")
CNVCardLine = _Class("CNVCardLine")
CNVCardVersionPlaceholderLine = _Class("CNVCardVersionPlaceholderLine")
CNVCardLiteralLine = _Class("CNVCardLiteralLine")
CNVCardPerson = _Class("CNVCardPerson")
CNVCardUnknownPropertyDescription = _Class("CNVCardUnknownPropertyDescription")
CNVCard30CardBuilder = _Class("CNVCard30CardBuilder")
CNVCardFilteredPerson = _Class("CNVCardFilteredPerson")
CNVCardWriting = _Class("CNVCardWriting")
CNVCardParsedDictionaryResultBuilder = _Class("CNVCardParsedDictionaryResultBuilder")
CNVCardLexer = _Class("CNVCardLexer")
CNVCardParsedParameter = _Class("CNVCardParsedParameter")
CNVCardReadingOptions = _Class("CNVCardReadingOptions")
CNVCardParsedLine = _Class("CNVCardParsedLine")
CNVCardXSOCIALPROFILEParser = _Class("CNVCardXSOCIALPROFILEParser")
CNVCardActivityAlertEscapingSerializationStrategy = _Class(
    "CNVCardActivityAlertEscapingSerializationStrategy"
)
CNVCardActivityAlertQuotingSerializationStrategy = _Class(
    "CNVCardActivityAlertQuotingSerializationStrategy"
)
CNVCardActivityAlertSerializer = _Class("CNVCardActivityAlertSerializer")
CNVCardActivityAlertSerialization = _Class("CNVCardActivityAlertSerialization")
CNVCardRangeFinder = _Class("CNVCardRangeFinder")
CNVCardActivityAlertScanner = _Class("CNVCardActivityAlertScanner")
_CNVCardParsedResultBuilderBlockFactory = _Class(
    "_CNVCardParsedResultBuilderBlockFactory"
)
CNVCardParsedResultBuilderFactory = _Class("CNVCardParsedResultBuilderFactory")
CNVCardXACTIVITYALERTParser = _Class("CNVCardXACTIVITYALERTParser")
CNVCardXABPHOTOParser = _Class("CNVCardXABPHOTOParser")
CNVCardURLParser = _Class("CNVCardURLParser")
CNVCardPHOTOParser = _Class("CNVCardPHOTOParser")
CNVCardInstantMessageParser = _Class("CNVCardInstantMessageParser")
CNVCardDateScanner = _Class("CNVCardDateScanner")
CNVCardDateComponentsParser = _Class("CNVCardDateComponentsParser")
CNVCardADRParser = _Class("CNVCardADRParser")
CNVCardSelectorMap = _Class("CNVCardSelectorMap")
CNVCardTesting = _Class("CNVCardTesting")
CNVCardDictionarySerialization = _Class("CNVCardDictionarySerialization")
CNVCardParser = _Class("CNVCardParser")
CNVCardDataAnalyzer = _Class("CNVCardDataAnalyzer")
CNVCardReading = _Class("CNVCardReading")
CNVCardDateComponentsFormatter = _Class("CNVCardDateComponentsFormatter")
