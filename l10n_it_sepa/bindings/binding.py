# flake8: noqa
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8183118d83af50bc8fb8b1036c9d45005c1d60fa
# Generated 2020-02-29 22:07:21.288529 by PyXB version 1.2.6 using Python 3.6.5.final.0
# Namespace urn:CBI:xsd:CBIPaymentRequest.00.04.00

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:79abd046-5b37-11ea-88f3-08606e4492c3')

# Version of PyXB used to generate the bindings
#_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
#if pyxb.__version__ != _PyXBVersion:
    #raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:CBI:xsd:CBIPaymentRequest.00.04.00', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 334, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.INF = STD_ANON._CF_enumeration.addEnumeration(unicode_value='INF', tag='INF')
STD_ANON.SNR = STD_ANON._CF_enumeration.addEnumeration(unicode_value='SNR', tag='SNR')
STD_ANON.CVA = STD_ANON._CF_enumeration.addEnumeration(unicode_value='CVA', tag='CVA')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ActiveOrHistoricCurrencyAndAmount_SimpleType
class ActiveOrHistoricCurrencyAndAmount_SimpleType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveOrHistoricCurrencyAndAmount_SimpleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 522, 1)
    _Documentation = None
ActiveOrHistoricCurrencyAndAmount_SimpleType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ActiveOrHistoricCurrencyAndAmount_SimpleType, value=pyxb.binding.datatypes.decimal('0.0'))
ActiveOrHistoricCurrencyAndAmount_SimpleType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
ActiveOrHistoricCurrencyAndAmount_SimpleType._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(5))
ActiveOrHistoricCurrencyAndAmount_SimpleType._InitializeFacetMap(ActiveOrHistoricCurrencyAndAmount_SimpleType._CF_minInclusive,
   ActiveOrHistoricCurrencyAndAmount_SimpleType._CF_totalDigits,
   ActiveOrHistoricCurrencyAndAmount_SimpleType._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'ActiveOrHistoricCurrencyAndAmount_SimpleType', ActiveOrHistoricCurrencyAndAmount_SimpleType)
_module_typeBindings.ActiveOrHistoricCurrencyAndAmount_SimpleType = ActiveOrHistoricCurrencyAndAmount_SimpleType

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ActiveOrHistoricCurrencyCode
class ActiveOrHistoricCurrencyCode (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveOrHistoricCurrencyCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 529, 1)
    _Documentation = None
ActiveOrHistoricCurrencyCode._CF_pattern = pyxb.binding.facets.CF_pattern()
ActiveOrHistoricCurrencyCode._CF_pattern.addPattern(pattern='[A-Z]{3,3}')
ActiveOrHistoricCurrencyCode._InitializeFacetMap(ActiveOrHistoricCurrencyCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ActiveOrHistoricCurrencyCode', ActiveOrHistoricCurrencyCode)
_module_typeBindings.ActiveOrHistoricCurrencyCode = ActiveOrHistoricCurrencyCode

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}AddressType2Code
class AddressType2Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressType2Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 534, 1)
    _Documentation = None
AddressType2Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AddressType2Code, enum_prefix=None)
AddressType2Code.ADDR = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='ADDR', tag='ADDR')
AddressType2Code.PBOX = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='PBOX', tag='PBOX')
AddressType2Code.HOME = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='HOME', tag='HOME')
AddressType2Code.BIZZ = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='BIZZ', tag='BIZZ')
AddressType2Code.MLTO = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='MLTO', tag='MLTO')
AddressType2Code.DLVY = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='DLVY', tag='DLVY')
AddressType2Code._InitializeFacetMap(AddressType2Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AddressType2Code', AddressType2Code)
_module_typeBindings.AddressType2Code = AddressType2Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}AnyBICIdentifier
class AnyBICIdentifier (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnyBICIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 544, 1)
    _Documentation = None
AnyBICIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
AnyBICIdentifier._CF_pattern.addPattern(pattern='[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}')
AnyBICIdentifier._InitializeFacetMap(AnyBICIdentifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AnyBICIdentifier', AnyBICIdentifier)
_module_typeBindings.AnyBICIdentifier = AnyBICIdentifier

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}BatchBookingIndicator
class BatchBookingIndicator (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BatchBookingIndicator')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 549, 1)
    _Documentation = None
BatchBookingIndicator._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BatchBookingIndicator', BatchBookingIndicator)
_module_typeBindings.BatchBookingIndicator = BatchBookingIndicator

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}BICIdentifier
class BICIdentifier (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BICIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 552, 1)
    _Documentation = None
BICIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
BICIdentifier._CF_pattern.addPattern(pattern='[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}')
BICIdentifier._InitializeFacetMap(BICIdentifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'BICIdentifier', BICIdentifier)
_module_typeBindings.BICIdentifier = BICIdentifier

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIChargeBearerTypeCode
class CBIChargeBearerTypeCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIChargeBearerTypeCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 557, 1)
    _Documentation = None
CBIChargeBearerTypeCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CBIChargeBearerTypeCode, enum_prefix=None)
CBIChargeBearerTypeCode.SLEV = CBIChargeBearerTypeCode._CF_enumeration.addEnumeration(unicode_value='SLEV', tag='SLEV')
CBIChargeBearerTypeCode._InitializeFacetMap(CBIChargeBearerTypeCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBIChargeBearerTypeCode', CBIChargeBearerTypeCode)
_module_typeBindings.CBIChargeBearerTypeCode = CBIChargeBearerTypeCode

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIChequeType1Code
class CBIChequeType1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIChequeType1Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 562, 1)
    _Documentation = None
CBIChequeType1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CBIChequeType1Code, enum_prefix=None)
CBIChequeType1Code.CCCH = CBIChequeType1Code._CF_enumeration.addEnumeration(unicode_value='CCCH', tag='CCCH')
CBIChequeType1Code.BCHQ = CBIChequeType1Code._CF_enumeration.addEnumeration(unicode_value='BCHQ', tag='BCHQ')
CBIChequeType1Code._InitializeFacetMap(CBIChequeType1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBIChequeType1Code', CBIChequeType1Code)
_module_typeBindings.CBIChequeType1Code = CBIChequeType1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIRegulatoryReportingType1Code
class CBIRegulatoryReportingType1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIRegulatoryReportingType1Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 568, 1)
    _Documentation = None
CBIRegulatoryReportingType1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CBIRegulatoryReportingType1Code, enum_prefix=None)
CBIRegulatoryReportingType1Code.DEBT = CBIRegulatoryReportingType1Code._CF_enumeration.addEnumeration(unicode_value='DEBT', tag='DEBT')
CBIRegulatoryReportingType1Code._InitializeFacetMap(CBIRegulatoryReportingType1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBIRegulatoryReportingType1Code', CBIRegulatoryReportingType1Code)
_module_typeBindings.CBIRegulatoryReportingType1Code = CBIRegulatoryReportingType1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIRemittanceLocationMethod1Code
class CBIRemittanceLocationMethod1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIRemittanceLocationMethod1Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 573, 1)
    _Documentation = None
CBIRemittanceLocationMethod1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CBIRemittanceLocationMethod1Code, enum_prefix=None)
CBIRemittanceLocationMethod1Code.FAXI = CBIRemittanceLocationMethod1Code._CF_enumeration.addEnumeration(unicode_value='FAXI', tag='FAXI')
CBIRemittanceLocationMethod1Code.EMAL = CBIRemittanceLocationMethod1Code._CF_enumeration.addEnumeration(unicode_value='EMAL', tag='EMAL')
CBIRemittanceLocationMethod1Code.SMSM = CBIRemittanceLocationMethod1Code._CF_enumeration.addEnumeration(unicode_value='SMSM', tag='SMSM')
CBIRemittanceLocationMethod1Code._InitializeFacetMap(CBIRemittanceLocationMethod1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBIRemittanceLocationMethod1Code', CBIRemittanceLocationMethod1Code)
_module_typeBindings.CBIRemittanceLocationMethod1Code = CBIRemittanceLocationMethod1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIServiceLevel1Code
class CBIServiceLevel1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIServiceLevel1Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 580, 1)
    _Documentation = None
CBIServiceLevel1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CBIServiceLevel1Code, enum_prefix=None)
CBIServiceLevel1Code.SEPA = CBIServiceLevel1Code._CF_enumeration.addEnumeration(unicode_value='SEPA', tag='SEPA')
CBIServiceLevel1Code.URGP = CBIServiceLevel1Code._CF_enumeration.addEnumeration(unicode_value='URGP', tag='URGP')
CBIServiceLevel1Code._InitializeFacetMap(CBIServiceLevel1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBIServiceLevel1Code', CBIServiceLevel1Code)
_module_typeBindings.CBIServiceLevel1Code = CBIServiceLevel1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBISrvInf1
class CBISrvInf1 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBISrvInf1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 586, 1)
    _Documentation = None
CBISrvInf1._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CBISrvInf1, enum_prefix=None)
CBISrvInf1.ESBEN = CBISrvInf1._CF_enumeration.addEnumeration(unicode_value='ESBEN', tag='ESBEN')
CBISrvInf1._InitializeFacetMap(CBISrvInf1._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBISrvInf1', CBISrvInf1)
_module_typeBindings.CBISrvInf1 = CBISrvInf1

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CountryCode
class CountryCode (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountryCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 591, 1)
    _Documentation = None
CountryCode._CF_pattern = pyxb.binding.facets.CF_pattern()
CountryCode._CF_pattern.addPattern(pattern='[A-Z]{2,2}')
CountryCode._InitializeFacetMap(CountryCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CountryCode', CountryCode)
_module_typeBindings.CountryCode = CountryCode

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CreditDebitCode
class CreditDebitCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreditDebitCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 596, 1)
    _Documentation = None
CreditDebitCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CreditDebitCode, enum_prefix=None)
CreditDebitCode.CRDT = CreditDebitCode._CF_enumeration.addEnumeration(unicode_value='CRDT', tag='CRDT')
CreditDebitCode.DBIT = CreditDebitCode._CF_enumeration.addEnumeration(unicode_value='DBIT', tag='DBIT')
CreditDebitCode._InitializeFacetMap(CreditDebitCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CreditDebitCode', CreditDebitCode)
_module_typeBindings.CreditDebitCode = CreditDebitCode

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DecimalNumber
class DecimalNumber (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DecimalNumber')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 602, 1)
    _Documentation = None
DecimalNumber._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
DecimalNumber._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(17))
DecimalNumber._InitializeFacetMap(DecimalNumber._CF_totalDigits,
   DecimalNumber._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'DecimalNumber', DecimalNumber)
_module_typeBindings.DecimalNumber = DecimalNumber

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DocumentType3Code
class DocumentType3Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentType3Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 608, 1)
    _Documentation = None
DocumentType3Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DocumentType3Code, enum_prefix=None)
DocumentType3Code.RADM = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='RADM', tag='RADM')
DocumentType3Code.RPIN = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='RPIN', tag='RPIN')
DocumentType3Code.FXDR = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='FXDR', tag='FXDR')
DocumentType3Code.DISP = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='DISP', tag='DISP')
DocumentType3Code.PUOR = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='PUOR', tag='PUOR')
DocumentType3Code.SCOR = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='SCOR', tag='SCOR')
DocumentType3Code._InitializeFacetMap(DocumentType3Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DocumentType3Code', DocumentType3Code)
_module_typeBindings.DocumentType3Code = DocumentType3Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DocumentType5Code
class DocumentType5Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentType5Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 618, 1)
    _Documentation = None
DocumentType5Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DocumentType5Code, enum_prefix=None)
DocumentType5Code.MSIN = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='MSIN', tag='MSIN')
DocumentType5Code.CNFA = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='CNFA', tag='CNFA')
DocumentType5Code.DNFA = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='DNFA', tag='DNFA')
DocumentType5Code.CINV = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='CINV', tag='CINV')
DocumentType5Code.CREN = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='CREN', tag='CREN')
DocumentType5Code.DEBN = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='DEBN', tag='DEBN')
DocumentType5Code.HIRI = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='HIRI', tag='HIRI')
DocumentType5Code.SBIN = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='SBIN', tag='SBIN')
DocumentType5Code.CMCN = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='CMCN', tag='CMCN')
DocumentType5Code.SOAC = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='SOAC', tag='SOAC')
DocumentType5Code.DISP = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='DISP', tag='DISP')
DocumentType5Code.BOLD = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='BOLD', tag='BOLD')
DocumentType5Code.VCHR = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='VCHR', tag='VCHR')
DocumentType5Code.AROI = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='AROI', tag='AROI')
DocumentType5Code.TSUT = DocumentType5Code._CF_enumeration.addEnumeration(unicode_value='TSUT', tag='TSUT')
DocumentType5Code._InitializeFacetMap(DocumentType5Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DocumentType5Code', DocumentType5Code)
_module_typeBindings.DocumentType5Code = DocumentType5Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ExternalCategoryPurpose1Code
class ExternalCategoryPurpose1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalCategoryPurpose1Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 637, 1)
    _Documentation = None
ExternalCategoryPurpose1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalCategoryPurpose1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalCategoryPurpose1Code._InitializeFacetMap(ExternalCategoryPurpose1Code._CF_minLength,
   ExternalCategoryPurpose1Code._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'ExternalCategoryPurpose1Code', ExternalCategoryPurpose1Code)
_module_typeBindings.ExternalCategoryPurpose1Code = ExternalCategoryPurpose1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ExternalOrganisationIdentification1Code
class ExternalOrganisationIdentification1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalOrganisationIdentification1Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 643, 1)
    _Documentation = None
ExternalOrganisationIdentification1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalOrganisationIdentification1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalOrganisationIdentification1Code._InitializeFacetMap(ExternalOrganisationIdentification1Code._CF_minLength,
   ExternalOrganisationIdentification1Code._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'ExternalOrganisationIdentification1Code', ExternalOrganisationIdentification1Code)
_module_typeBindings.ExternalOrganisationIdentification1Code = ExternalOrganisationIdentification1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ExternalPersonIdentification1Code
class ExternalPersonIdentification1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalPersonIdentification1Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 649, 1)
    _Documentation = None
ExternalPersonIdentification1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalPersonIdentification1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalPersonIdentification1Code._InitializeFacetMap(ExternalPersonIdentification1Code._CF_minLength,
   ExternalPersonIdentification1Code._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'ExternalPersonIdentification1Code', ExternalPersonIdentification1Code)
_module_typeBindings.ExternalPersonIdentification1Code = ExternalPersonIdentification1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ExternalPurpose1Code
class ExternalPurpose1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalPurpose1Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 655, 1)
    _Documentation = None
ExternalPurpose1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalPurpose1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalPurpose1Code._InitializeFacetMap(ExternalPurpose1Code._CF_minLength,
   ExternalPurpose1Code._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'ExternalPurpose1Code', ExternalPurpose1Code)
_module_typeBindings.ExternalPurpose1Code = ExternalPurpose1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}IBAN2007Identifier
class IBAN2007Identifier (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IBAN2007Identifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 661, 1)
    _Documentation = None
IBAN2007Identifier._CF_pattern = pyxb.binding.facets.CF_pattern()
IBAN2007Identifier._CF_pattern.addPattern(pattern='[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}')
IBAN2007Identifier._InitializeFacetMap(IBAN2007Identifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'IBAN2007Identifier', IBAN2007Identifier)
_module_typeBindings.IBAN2007Identifier = IBAN2007Identifier

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ISODate
class ISODate (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISODate')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 666, 1)
    _Documentation = None
ISODate._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ISODate', ISODate)
_module_typeBindings.ISODate = ISODate

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ISODateTime
class ISODateTime (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISODateTime')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 669, 1)
    _Documentation = None
ISODateTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ISODateTime', ISODateTime)
_module_typeBindings.ISODateTime = ISODateTime

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Max4Text
class Max4Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max4Text')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 672, 1)
    _Documentation = None
Max4Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max4Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
Max4Text._InitializeFacetMap(Max4Text._CF_minLength,
   Max4Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max4Text', Max4Text)
_module_typeBindings.Max4Text = Max4Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Max15NumericText
class Max15NumericText (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max15NumericText')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 678, 1)
    _Documentation = None
Max15NumericText._CF_pattern = pyxb.binding.facets.CF_pattern()
Max15NumericText._CF_pattern.addPattern(pattern='[0-9]{1,15}')
Max15NumericText._InitializeFacetMap(Max15NumericText._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'Max15NumericText', Max15NumericText)
_module_typeBindings.Max15NumericText = Max15NumericText

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Max16Text
class Max16Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max16Text')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 683, 1)
    _Documentation = None
Max16Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max16Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
Max16Text._InitializeFacetMap(Max16Text._CF_minLength,
   Max16Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max16Text', Max16Text)
_module_typeBindings.Max16Text = Max16Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Max35Text
class Max35Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max35Text')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 689, 1)
    _Documentation = None
Max35Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max35Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
Max35Text._InitializeFacetMap(Max35Text._CF_minLength,
   Max35Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max35Text', Max35Text)
_module_typeBindings.Max35Text = Max35Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Max70Text
class Max70Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max70Text')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 695, 1)
    _Documentation = None
Max70Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max70Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(70))
Max70Text._InitializeFacetMap(Max70Text._CF_minLength,
   Max70Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max70Text', Max70Text)
_module_typeBindings.Max70Text = Max70Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Max140Text
class Max140Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max140Text')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 701, 1)
    _Documentation = None
Max140Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max140Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(140))
Max140Text._InitializeFacetMap(Max140Text._CF_minLength,
   Max140Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max140Text', Max140Text)
_module_typeBindings.Max140Text = Max140Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Max2048Text
class Max2048Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max2048Text')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 707, 1)
    _Documentation = None
Max2048Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max2048Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2048))
Max2048Text._InitializeFacetMap(Max2048Text._CF_minLength,
   Max2048Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max2048Text', Max2048Text)
_module_typeBindings.Max2048Text = Max2048Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}NamePrefix1Code
class NamePrefix1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NamePrefix1Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 713, 1)
    _Documentation = None
NamePrefix1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NamePrefix1Code, enum_prefix=None)
NamePrefix1Code.DOCT = NamePrefix1Code._CF_enumeration.addEnumeration(unicode_value='DOCT', tag='DOCT')
NamePrefix1Code.MIST = NamePrefix1Code._CF_enumeration.addEnumeration(unicode_value='MIST', tag='MIST')
NamePrefix1Code.MISS = NamePrefix1Code._CF_enumeration.addEnumeration(unicode_value='MISS', tag='MISS')
NamePrefix1Code.MADM = NamePrefix1Code._CF_enumeration.addEnumeration(unicode_value='MADM', tag='MADM')
NamePrefix1Code._InitializeFacetMap(NamePrefix1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NamePrefix1Code', NamePrefix1Code)
_module_typeBindings.NamePrefix1Code = NamePrefix1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PaymentMethod3Code
class PaymentMethod3Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentMethod3Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 721, 1)
    _Documentation = None
PaymentMethod3Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PaymentMethod3Code, enum_prefix=None)
PaymentMethod3Code.CHK = PaymentMethod3Code._CF_enumeration.addEnumeration(unicode_value='CHK', tag='CHK')
PaymentMethod3Code.TRF = PaymentMethod3Code._CF_enumeration.addEnumeration(unicode_value='TRF', tag='TRF')
PaymentMethod3Code.TRA = PaymentMethod3Code._CF_enumeration.addEnumeration(unicode_value='TRA', tag='TRA')
PaymentMethod3Code._InitializeFacetMap(PaymentMethod3Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PaymentMethod3Code', PaymentMethod3Code)
_module_typeBindings.PaymentMethod3Code = PaymentMethod3Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Priority2Code
class Priority2Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Priority2Code')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 728, 1)
    _Documentation = None
Priority2Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Priority2Code, enum_prefix=None)
Priority2Code.HIGH = Priority2Code._CF_enumeration.addEnumeration(unicode_value='HIGH', tag='HIGH')
Priority2Code.NORM = Priority2Code._CF_enumeration.addEnumeration(unicode_value='NORM', tag='NORM')
Priority2Code._InitializeFacetMap(Priority2Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Priority2Code', Priority2Code)
_module_typeBindings.Priority2Code = Priority2Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PhoneNumber
class PhoneNumber (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PhoneNumber')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 734, 1)
    _Documentation = None
PhoneNumber._CF_pattern = pyxb.binding.facets.CF_pattern()
PhoneNumber._CF_pattern.addPattern(pattern='\\+[0-9]{1,3}-[0-9()+\\-]{1,30}')
PhoneNumber._InitializeFacetMap(PhoneNumber._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'PhoneNumber', PhoneNumber)
_module_typeBindings.PhoneNumber = PhoneNumber

# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPaymentRequest.00.04.00 with content type ELEMENT_ONLY
class CBIPaymentRequest_00_04_00 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPaymentRequest.00.04.00 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPaymentRequest.00.04.00')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 6, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}GrpHdr uses Python identifier GrpHdr
    __GrpHdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr'), 'GrpHdr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentRequest_00_04_00_urnCBIxsdCBIPaymentRequest_00_04_00GrpHdr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 8, 3), )

    
    GrpHdr = property(__GrpHdr.value, __GrpHdr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PmtInf uses Python identifier PmtInf
    __PmtInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtInf'), 'PmtInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentRequest_00_04_00_urnCBIxsdCBIPaymentRequest_00_04_00PmtInf', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 9, 3), )

    
    PmtInf = property(__PmtInf.value, __PmtInf.set, None, None)

    _ElementMap.update({
        __GrpHdr.name() : __GrpHdr,
        __PmtInf.name() : __PmtInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPaymentRequest_00_04_00 = CBIPaymentRequest_00_04_00
Namespace.addCategoryObject('typeBinding', 'CBIPaymentRequest.00.04.00', CBIPaymentRequest_00_04_00)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIGroupHeader with content type ELEMENT_ONLY
class CBIGroupHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIGroupHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIGroupHeader')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 14, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}MsgId uses Python identifier MsgId
    __MsgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MsgId'), 'MsgId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_00MsgId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 16, 3), )

    
    MsgId = property(__MsgId.value, __MsgId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CreDtTm uses Python identifier CreDtTm
    __CreDtTm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm'), 'CreDtTm', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_00CreDtTm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 17, 3), )

    
    CreDtTm = property(__CreDtTm.value, __CreDtTm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}NbOfTxs uses Python identifier NbOfTxs
    __NbOfTxs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs'), 'NbOfTxs', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_00NbOfTxs', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 18, 3), )

    
    NbOfTxs = property(__NbOfTxs.value, __NbOfTxs.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CtrlSum uses Python identifier CtrlSum
    __CtrlSum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum'), 'CtrlSum', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_00CtrlSum', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 19, 3), )

    
    CtrlSum = property(__CtrlSum.value, __CtrlSum.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}InitgPty uses Python identifier InitgPty
    __InitgPty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InitgPty'), 'InitgPty', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_00InitgPty', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 20, 3), )

    
    InitgPty = property(__InitgPty.value, __InitgPty.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}FwdgAgt uses Python identifier FwdgAgt
    __FwdgAgt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FwdgAgt'), 'FwdgAgt', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_00FwdgAgt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 21, 3), )

    
    FwdgAgt = property(__FwdgAgt.value, __FwdgAgt.set, None, None)

    _ElementMap.update({
        __MsgId.name() : __MsgId,
        __CreDtTm.name() : __CreDtTm,
        __NbOfTxs.name() : __NbOfTxs,
        __CtrlSum.name() : __CtrlSum,
        __InitgPty.name() : __InitgPty,
        __FwdgAgt.name() : __FwdgAgt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIGroupHeader = CBIGroupHeader
Namespace.addCategoryObject('typeBinding', 'CBIGroupHeader', CBIGroupHeader)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPaymentInstructionInformation with content type ELEMENT_ONLY
class CBIPaymentInstructionInformation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPaymentInstructionInformation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPaymentInstructionInformation')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 31, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PmtInfId uses Python identifier PmtInfId
    __PmtInfId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtInfId'), 'PmtInfId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00PmtInfId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 33, 3), )

    
    PmtInfId = property(__PmtInfId.value, __PmtInfId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PmtMtd uses Python identifier PmtMtd
    __PmtMtd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtMtd'), 'PmtMtd', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00PmtMtd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 34, 3), )

    
    PmtMtd = property(__PmtMtd.value, __PmtMtd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}BtchBookg uses Python identifier BtchBookg
    __BtchBookg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BtchBookg'), 'BtchBookg', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00BtchBookg', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 35, 3), )

    
    BtchBookg = property(__BtchBookg.value, __BtchBookg.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PmtTpInf uses Python identifier PmtTpInf
    __PmtTpInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf'), 'PmtTpInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00PmtTpInf', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 36, 3), )

    
    PmtTpInf = property(__PmtTpInf.value, __PmtTpInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ReqdExctnDt uses Python identifier ReqdExctnDt
    __ReqdExctnDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReqdExctnDt'), 'ReqdExctnDt', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00ReqdExctnDt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 37, 3), )

    
    ReqdExctnDt = property(__ReqdExctnDt.value, __ReqdExctnDt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Dbtr uses Python identifier Dbtr
    __Dbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dbtr'), 'Dbtr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00Dbtr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 38, 3), )

    
    Dbtr = property(__Dbtr.value, __Dbtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DbtrAcct uses Python identifier DbtrAcct
    __DbtrAcct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DbtrAcct'), 'DbtrAcct', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00DbtrAcct', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 39, 3), )

    
    DbtrAcct = property(__DbtrAcct.value, __DbtrAcct.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DbtrAgt uses Python identifier DbtrAgt
    __DbtrAgt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DbtrAgt'), 'DbtrAgt', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00DbtrAgt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 40, 3), )

    
    DbtrAgt = property(__DbtrAgt.value, __DbtrAgt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}UltmtDbtr uses Python identifier UltmtDbtr
    __UltmtDbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), 'UltmtDbtr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00UltmtDbtr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 41, 3), )

    
    UltmtDbtr = property(__UltmtDbtr.value, __UltmtDbtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ChrgBr uses Python identifier ChrgBr
    __ChrgBr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChrgBr'), 'ChrgBr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00ChrgBr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 42, 3), )

    
    ChrgBr = property(__ChrgBr.value, __ChrgBr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ChrgsAcct uses Python identifier ChrgsAcct
    __ChrgsAcct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChrgsAcct'), 'ChrgsAcct', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00ChrgsAcct', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 43, 3), )

    
    ChrgsAcct = property(__ChrgsAcct.value, __ChrgsAcct.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CdtTrfTxInf uses Python identifier CdtTrfTxInf
    __CdtTrfTxInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtTrfTxInf'), 'CdtTrfTxInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_00CdtTrfTxInf', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 44, 3), )

    
    CdtTrfTxInf = property(__CdtTrfTxInf.value, __CdtTrfTxInf.set, None, None)

    _ElementMap.update({
        __PmtInfId.name() : __PmtInfId,
        __PmtMtd.name() : __PmtMtd,
        __BtchBookg.name() : __BtchBookg,
        __PmtTpInf.name() : __PmtTpInf,
        __ReqdExctnDt.name() : __ReqdExctnDt,
        __Dbtr.name() : __Dbtr,
        __DbtrAcct.name() : __DbtrAcct,
        __DbtrAgt.name() : __DbtrAgt,
        __UltmtDbtr.name() : __UltmtDbtr,
        __ChrgBr.name() : __ChrgBr,
        __ChrgsAcct.name() : __ChrgsAcct,
        __CdtTrfTxInf.name() : __CdtTrfTxInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPaymentInstructionInformation = CBIPaymentInstructionInformation
Namespace.addCategoryObject('typeBinding', 'CBIPaymentInstructionInformation', CBIPaymentInstructionInformation)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBICreditTransferTransactionInformation with content type ELEMENT_ONLY
class CBICreditTransferTransactionInformation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBICreditTransferTransactionInformation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBICreditTransferTransactionInformation')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 59, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PmtId uses Python identifier PmtId
    __PmtId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtId'), 'PmtId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00PmtId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 61, 3), )

    
    PmtId = property(__PmtId.value, __PmtId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PmtTpInf uses Python identifier PmtTpInf
    __PmtTpInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf'), 'PmtTpInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00PmtTpInf', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 62, 3), )

    
    PmtTpInf = property(__PmtTpInf.value, __PmtTpInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00Amt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 63, 3), )

    
    Amt = property(__Amt.value, __Amt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ChqInstr uses Python identifier ChqInstr
    __ChqInstr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChqInstr'), 'ChqInstr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00ChqInstr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 64, 3), )

    
    ChqInstr = property(__ChqInstr.value, __ChqInstr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}UltmtDbtr uses Python identifier UltmtDbtr
    __UltmtDbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), 'UltmtDbtr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00UltmtDbtr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 65, 3), )

    
    UltmtDbtr = property(__UltmtDbtr.value, __UltmtDbtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}SrvInf uses Python identifier SrvInf
    __SrvInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SrvInf'), 'SrvInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00SrvInf', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 66, 3), )

    
    SrvInf = property(__SrvInf.value, __SrvInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CdtrAgt uses Python identifier CdtrAgt
    __CdtrAgt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtrAgt'), 'CdtrAgt', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00CdtrAgt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 67, 3), )

    
    CdtrAgt = property(__CdtrAgt.value, __CdtrAgt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Cdtr uses Python identifier Cdtr
    __Cdtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cdtr'), 'Cdtr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00Cdtr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 68, 3), )

    
    Cdtr = property(__Cdtr.value, __Cdtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CdtrAcct uses Python identifier CdtrAcct
    __CdtrAcct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtrAcct'), 'CdtrAcct', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00CdtrAcct', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 69, 3), )

    
    CdtrAcct = property(__CdtrAcct.value, __CdtrAcct.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}UltmtCdtr uses Python identifier UltmtCdtr
    __UltmtCdtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UltmtCdtr'), 'UltmtCdtr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00UltmtCdtr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 70, 3), )

    
    UltmtCdtr = property(__UltmtCdtr.value, __UltmtCdtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DestCdtrRsp uses Python identifier DestCdtrRsp
    __DestCdtrRsp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DestCdtrRsp'), 'DestCdtrRsp', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00DestCdtrRsp', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 71, 3), )

    
    DestCdtrRsp = property(__DestCdtrRsp.value, __DestCdtrRsp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Purp uses Python identifier Purp
    __Purp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Purp'), 'Purp', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00Purp', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 72, 3), )

    
    Purp = property(__Purp.value, __Purp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RgltryRptg uses Python identifier RgltryRptg
    __RgltryRptg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RgltryRptg'), 'RgltryRptg', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00RgltryRptg', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 73, 3), )

    
    RgltryRptg = property(__RgltryRptg.value, __RgltryRptg.set, None, 'Aggiunto blocco per ospitare le comunicazione valutarie sintetiche ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RltdRmtInf uses Python identifier RltdRmtInf
    __RltdRmtInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RltdRmtInf'), 'RltdRmtInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00RltdRmtInf', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 78, 3), )

    
    RltdRmtInf = property(__RltdRmtInf.value, __RltdRmtInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RmtInf uses Python identifier RmtInf
    __RmtInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtInf'), 'RmtInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_00RmtInf', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 79, 3), )

    
    RmtInf = property(__RmtInf.value, __RmtInf.set, None, None)

    _ElementMap.update({
        __PmtId.name() : __PmtId,
        __PmtTpInf.name() : __PmtTpInf,
        __Amt.name() : __Amt,
        __ChqInstr.name() : __ChqInstr,
        __UltmtDbtr.name() : __UltmtDbtr,
        __SrvInf.name() : __SrvInf,
        __CdtrAgt.name() : __CdtrAgt,
        __Cdtr.name() : __Cdtr,
        __CdtrAcct.name() : __CdtrAcct,
        __UltmtCdtr.name() : __UltmtCdtr,
        __DestCdtrRsp.name() : __DestCdtrRsp,
        __Purp.name() : __Purp,
        __RgltryRptg.name() : __RgltryRptg,
        __RltdRmtInf.name() : __RltdRmtInf,
        __RmtInf.name() : __RmtInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBICreditTransferTransactionInformation = CBICreditTransferTransactionInformation
Namespace.addCategoryObject('typeBinding', 'CBICreditTransferTransactionInformation', CBICreditTransferTransactionInformation)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CategoryPurpose1Choice with content type ELEMENT_ONLY
class CategoryPurpose1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CategoryPurpose1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CategoryPurpose1Choice')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 108, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_00_CategoryPurpose1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Cd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 111, 4), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_00_CategoryPurpose1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Prtry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 112, 4), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CategoryPurpose1Choice = CategoryPurpose1Choice
Namespace.addCategoryObject('typeBinding', 'CategoryPurpose1Choice', CategoryPurpose1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIAccountIdentification1 with content type ELEMENT_ONLY
class CBIAccountIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIAccountIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIAccountIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 116, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}IBAN uses Python identifier IBAN
    __IBAN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IBAN'), 'IBAN', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIAccountIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00IBAN', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 118, 3), )

    
    IBAN = property(__IBAN.value, __IBAN.set, None, None)

    _ElementMap.update({
        __IBAN.name() : __IBAN
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIAccountIdentification1 = CBIAccountIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIAccountIdentification1', CBIAccountIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIAmountType1 with content type ELEMENT_ONLY
class CBIAmountType1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIAmountType1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIAmountType1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 121, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}InstdAmt uses Python identifier InstdAmt
    __InstdAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstdAmt'), 'InstdAmt', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIAmountType1_urnCBIxsdCBIPaymentRequest_00_04_00InstdAmt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 123, 3), )

    
    InstdAmt = property(__InstdAmt.value, __InstdAmt.set, None, None)

    _ElementMap.update({
        __InstdAmt.name() : __InstdAmt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIAmountType1 = CBIAmountType1
Namespace.addCategoryObject('typeBinding', 'CBIAmountType1', CBIAmountType1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIBranchAndFinancialInstitutionIdentification1 with content type ELEMENT_ONLY
class CBIBranchAndFinancialInstitutionIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIBranchAndFinancialInstitutionIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIBranchAndFinancialInstitutionIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 126, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}FinInstnId uses Python identifier FinInstnId
    __FinInstnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), 'FinInstnId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIBranchAndFinancialInstitutionIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00FinInstnId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 128, 3), )

    
    FinInstnId = property(__FinInstnId.value, __FinInstnId.set, None, None)

    _ElementMap.update({
        __FinInstnId.name() : __FinInstnId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIBranchAndFinancialInstitutionIdentification1 = CBIBranchAndFinancialInstitutionIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIBranchAndFinancialInstitutionIdentification1', CBIBranchAndFinancialInstitutionIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIBranchAndFinancialInstitutionIdentification2 with content type ELEMENT_ONLY
class CBIBranchAndFinancialInstitutionIdentification2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIBranchAndFinancialInstitutionIdentification2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIBranchAndFinancialInstitutionIdentification2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 131, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}FinInstnId uses Python identifier FinInstnId
    __FinInstnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), 'FinInstnId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIBranchAndFinancialInstitutionIdentification2_urnCBIxsdCBIPaymentRequest_00_04_00FinInstnId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 133, 3), )

    
    FinInstnId = property(__FinInstnId.value, __FinInstnId.set, None, None)

    _ElementMap.update({
        __FinInstnId.name() : __FinInstnId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIBranchAndFinancialInstitutionIdentification2 = CBIBranchAndFinancialInstitutionIdentification2
Namespace.addCategoryObject('typeBinding', 'CBIBranchAndFinancialInstitutionIdentification2', CBIBranchAndFinancialInstitutionIdentification2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIBranchAndFinancialInstitutionIdentification3 with content type ELEMENT_ONLY
class CBIBranchAndFinancialInstitutionIdentification3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIBranchAndFinancialInstitutionIdentification3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIBranchAndFinancialInstitutionIdentification3')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 136, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}FinInstnId uses Python identifier FinInstnId
    __FinInstnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), 'FinInstnId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIBranchAndFinancialInstitutionIdentification3_urnCBIxsdCBIPaymentRequest_00_04_00FinInstnId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 138, 3), )

    
    FinInstnId = property(__FinInstnId.value, __FinInstnId.set, None, None)

    _ElementMap.update({
        __FinInstnId.name() : __FinInstnId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIBranchAndFinancialInstitutionIdentification3 = CBIBranchAndFinancialInstitutionIdentification3
Namespace.addCategoryObject('typeBinding', 'CBIBranchAndFinancialInstitutionIdentification3', CBIBranchAndFinancialInstitutionIdentification3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBICashAccount1 with content type ELEMENT_ONLY
class CBICashAccount1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBICashAccount1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBICashAccount1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 141, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICashAccount1_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 143, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBICashAccount1 = CBICashAccount1
Namespace.addCategoryObject('typeBinding', 'CBICashAccount1', CBICashAccount1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBICashAccount2 with content type ELEMENT_ONLY
class CBICashAccount2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBICashAccount2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBICashAccount2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 146, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICashAccount2_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 148, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBICashAccount2 = CBICashAccount2
Namespace.addCategoryObject('typeBinding', 'CBICashAccount2', CBICashAccount2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBICheque1 with content type ELEMENT_ONLY
class CBICheque1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBICheque1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBICheque1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 151, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ChqTp uses Python identifier ChqTp
    __ChqTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChqTp'), 'ChqTp', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBICheque1_urnCBIxsdCBIPaymentRequest_00_04_00ChqTp', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 153, 3), )

    
    ChqTp = property(__ChqTp.value, __ChqTp.set, None, None)

    _ElementMap.update({
        __ChqTp.name() : __ChqTp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBICheque1 = CBICheque1
Namespace.addCategoryObject('typeBinding', 'CBICheque1', CBICheque1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIClearingSystemMemberIdentification1 with content type ELEMENT_ONLY
class CBIClearingSystemMemberIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIClearingSystemMemberIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIClearingSystemMemberIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 156, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}MmbId uses Python identifier MmbId
    __MmbId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MmbId'), 'MmbId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIClearingSystemMemberIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00MmbId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 158, 3), )

    
    MmbId = property(__MmbId.value, __MmbId.set, None, None)

    _ElementMap.update({
        __MmbId.name() : __MmbId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIClearingSystemMemberIdentification1 = CBIClearingSystemMemberIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIClearingSystemMemberIdentification1', CBIClearingSystemMemberIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIFinancialInstitutionIdentification1 with content type ELEMENT_ONLY
class CBIFinancialInstitutionIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIFinancialInstitutionIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIFinancialInstitutionIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 161, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ClrSysMmbId uses Python identifier ClrSysMmbId
    __ClrSysMmbId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId'), 'ClrSysMmbId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIFinancialInstitutionIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00ClrSysMmbId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 163, 3), )

    
    ClrSysMmbId = property(__ClrSysMmbId.value, __ClrSysMmbId.set, None, None)

    _ElementMap.update({
        __ClrSysMmbId.name() : __ClrSysMmbId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIFinancialInstitutionIdentification1 = CBIFinancialInstitutionIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIFinancialInstitutionIdentification1', CBIFinancialInstitutionIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIFinancialInstitutionIdentification2 with content type ELEMENT_ONLY
class CBIFinancialInstitutionIdentification2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIFinancialInstitutionIdentification2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIFinancialInstitutionIdentification2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 166, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}BIC uses Python identifier BIC
    __BIC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BIC'), 'BIC', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIFinancialInstitutionIdentification2_urnCBIxsdCBIPaymentRequest_00_04_00BIC', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 168, 3), )

    
    BIC = property(__BIC.value, __BIC.set, None, None)

    _ElementMap.update({
        __BIC.name() : __BIC
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIFinancialInstitutionIdentification2 = CBIFinancialInstitutionIdentification2
Namespace.addCategoryObject('typeBinding', 'CBIFinancialInstitutionIdentification2', CBIFinancialInstitutionIdentification2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIFinancialInstitutionIdentification3 with content type ELEMENT_ONLY
class CBIFinancialInstitutionIdentification3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIFinancialInstitutionIdentification3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIFinancialInstitutionIdentification3')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 171, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}BIC uses Python identifier BIC
    __BIC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BIC'), 'BIC', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIFinancialInstitutionIdentification3_urnCBIxsdCBIPaymentRequest_00_04_00BIC', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 173, 3), )

    
    BIC = property(__BIC.value, __BIC.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ClrSysMmbId uses Python identifier ClrSysMmbId
    __ClrSysMmbId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId'), 'ClrSysMmbId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIFinancialInstitutionIdentification3_urnCBIxsdCBIPaymentRequest_00_04_00ClrSysMmbId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 174, 3), )

    
    ClrSysMmbId = property(__ClrSysMmbId.value, __ClrSysMmbId.set, None, None)

    _ElementMap.update({
        __BIC.name() : __BIC,
        __ClrSysMmbId.name() : __ClrSysMmbId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIFinancialInstitutionIdentification3 = CBIFinancialInstitutionIdentification3
Namespace.addCategoryObject('typeBinding', 'CBIFinancialInstitutionIdentification3', CBIFinancialInstitutionIdentification3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIGenericIdentification1 with content type ELEMENT_ONLY
class CBIGenericIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIGenericIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIGenericIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 177, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIGenericIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 179, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIGenericIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00Issr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 180, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIGenericIdentification1 = CBIGenericIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIGenericIdentification1', CBIGenericIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIGenericIdentification2 with content type ELEMENT_ONLY
class CBIGenericIdentification2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIGenericIdentification2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIGenericIdentification2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 183, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIGenericIdentification2_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 185, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIGenericIdentification2_urnCBIxsdCBIPaymentRequest_00_04_00Issr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 186, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIGenericIdentification2 = CBIGenericIdentification2
Namespace.addCategoryObject('typeBinding', 'CBIGenericIdentification2', CBIGenericIdentification2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIIdType1 with content type ELEMENT_ONLY
class CBIIdType1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIIdType1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIIdType1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 189, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIIdType1_urnCBIxsdCBIPaymentRequest_00_04_00OrgId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 191, 3), )

    
    OrgId = property(__OrgId.value, __OrgId.set, None, None)

    _ElementMap.update({
        __OrgId.name() : __OrgId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIIdType1 = CBIIdType1
Namespace.addCategoryObject('typeBinding', 'CBIIdType1', CBIIdType1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIIdType2 with content type ELEMENT_ONLY
class CBIIdType2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIIdType2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIIdType2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 194, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIIdType2_urnCBIxsdCBIPaymentRequest_00_04_00OrgId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 196, 3), )

    
    OrgId = property(__OrgId.value, __OrgId.set, None, None)

    _ElementMap.update({
        __OrgId.name() : __OrgId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIIdType2 = CBIIdType2
Namespace.addCategoryObject('typeBinding', 'CBIIdType2', CBIIdType2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIIdType3 with content type ELEMENT_ONLY
class CBIIdType3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIIdType3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIIdType3')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 199, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIIdType3_urnCBIxsdCBIPaymentRequest_00_04_00OrgId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 201, 3), )

    
    OrgId = property(__OrgId.value, __OrgId.set, None, None)

    _ElementMap.update({
        __OrgId.name() : __OrgId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIIdType3 = CBIIdType3
Namespace.addCategoryObject('typeBinding', 'CBIIdType3', CBIIdType3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBILocalInstrument1 with content type ELEMENT_ONLY
class CBILocalInstrument1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBILocalInstrument1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBILocalInstrument1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 204, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBILocalInstrument1_urnCBIxsdCBIPaymentRequest_00_04_00Prtry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 206, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBILocalInstrument1 = CBILocalInstrument1
Namespace.addCategoryObject('typeBinding', 'CBILocalInstrument1', CBILocalInstrument1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIOrganisationIdentification1 with content type ELEMENT_ONLY
class CBIOrganisationIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIOrganisationIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIOrganisationIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 209, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIOrganisationIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00Othr', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 211, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIOrganisationIdentification1 = CBIOrganisationIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIOrganisationIdentification1', CBIOrganisationIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIOrganisationIdentification2 with content type ELEMENT_ONLY
class CBIOrganisationIdentification2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIOrganisationIdentification2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIOrganisationIdentification2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 214, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}BICOrBEI uses Python identifier BICOrBEI
    __BICOrBEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI'), 'BICOrBEI', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIOrganisationIdentification2_urnCBIxsdCBIPaymentRequest_00_04_00BICOrBEI', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 217, 4), )

    
    BICOrBEI = property(__BICOrBEI.value, __BICOrBEI.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIOrganisationIdentification2_urnCBIxsdCBIPaymentRequest_00_04_00Othr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 218, 4), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __BICOrBEI.name() : __BICOrBEI,
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIOrganisationIdentification2 = CBIOrganisationIdentification2
Namespace.addCategoryObject('typeBinding', 'CBIOrganisationIdentification2', CBIOrganisationIdentification2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIOrganisationIdentification3 with content type ELEMENT_ONLY
class CBIOrganisationIdentification3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIOrganisationIdentification3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIOrganisationIdentification3')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 222, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIOrganisationIdentification3_urnCBIxsdCBIPaymentRequest_00_04_00Othr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 224, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIOrganisationIdentification3 = CBIOrganisationIdentification3
Namespace.addCategoryObject('typeBinding', 'CBIOrganisationIdentification3', CBIOrganisationIdentification3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIOrganisationIdentification4 with content type ELEMENT_ONLY
class CBIOrganisationIdentification4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIOrganisationIdentification4 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIOrganisationIdentification4')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 227, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIOrganisationIdentification4_urnCBIxsdCBIPaymentRequest_00_04_00Othr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 229, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIOrganisationIdentification4 = CBIOrganisationIdentification4
Namespace.addCategoryObject('typeBinding', 'CBIOrganisationIdentification4', CBIOrganisationIdentification4)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIParty1Choice with content type ELEMENT_ONLY
class CBIParty1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIParty1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIParty1Choice')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 232, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIParty1Choice_urnCBIxsdCBIPaymentRequest_00_04_00OrgId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 235, 4), )

    
    OrgId = property(__OrgId.value, __OrgId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PrvtId uses Python identifier PrvtId
    __PrvtId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrvtId'), 'PrvtId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIParty1Choice_urnCBIxsdCBIPaymentRequest_00_04_00PrvtId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 236, 4), )

    
    PrvtId = property(__PrvtId.value, __PrvtId.set, None, None)

    _ElementMap.update({
        __OrgId.name() : __OrgId,
        __PrvtId.name() : __PrvtId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIParty1Choice = CBIParty1Choice
Namespace.addCategoryObject('typeBinding', 'CBIParty1Choice', CBIParty1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPartyIdentification1 with content type ELEMENT_ONLY
class CBIPartyIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPartyIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPartyIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 240, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00Nm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 242, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 243, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPartyIdentification1 = CBIPartyIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIPartyIdentification1', CBIPartyIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPartyIdentification2 with content type ELEMENT_ONLY
class CBIPartyIdentification2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPartyIdentification2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPartyIdentification2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 246, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification2_urnCBIxsdCBIPaymentRequest_00_04_00Nm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 248, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PstlAdr uses Python identifier PstlAdr
    __PstlAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), 'PstlAdr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification2_urnCBIxsdCBIPaymentRequest_00_04_00PstlAdr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 249, 3), )

    
    PstlAdr = property(__PstlAdr.value, __PstlAdr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification2_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 250, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CtryOfRes uses Python identifier CtryOfRes
    __CtryOfRes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), 'CtryOfRes', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification2_urnCBIxsdCBIPaymentRequest_00_04_00CtryOfRes', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 251, 3), )

    
    CtryOfRes = property(__CtryOfRes.value, __CtryOfRes.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __PstlAdr.name() : __PstlAdr,
        __Id.name() : __Id,
        __CtryOfRes.name() : __CtryOfRes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPartyIdentification2 = CBIPartyIdentification2
Namespace.addCategoryObject('typeBinding', 'CBIPartyIdentification2', CBIPartyIdentification2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPartyIdentification3 with content type ELEMENT_ONLY
class CBIPartyIdentification3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPartyIdentification3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPartyIdentification3')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 254, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification3_urnCBIxsdCBIPaymentRequest_00_04_00Nm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 256, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PstlAdr uses Python identifier PstlAdr
    __PstlAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), 'PstlAdr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification3_urnCBIxsdCBIPaymentRequest_00_04_00PstlAdr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 257, 3), )

    
    PstlAdr = property(__PstlAdr.value, __PstlAdr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification3_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 258, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CtryOfRes uses Python identifier CtryOfRes
    __CtryOfRes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), 'CtryOfRes', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification3_urnCBIxsdCBIPaymentRequest_00_04_00CtryOfRes', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 259, 3), )

    
    CtryOfRes = property(__CtryOfRes.value, __CtryOfRes.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __PstlAdr.name() : __PstlAdr,
        __Id.name() : __Id,
        __CtryOfRes.name() : __CtryOfRes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPartyIdentification3 = CBIPartyIdentification3
Namespace.addCategoryObject('typeBinding', 'CBIPartyIdentification3', CBIPartyIdentification3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPartyIdentification4 with content type ELEMENT_ONLY
class CBIPartyIdentification4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPartyIdentification4 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPartyIdentification4')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 262, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification4_urnCBIxsdCBIPaymentRequest_00_04_00Nm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 264, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PstlAdr uses Python identifier PstlAdr
    __PstlAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), 'PstlAdr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification4_urnCBIxsdCBIPaymentRequest_00_04_00PstlAdr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 265, 3), )

    
    PstlAdr = property(__PstlAdr.value, __PstlAdr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification4_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 266, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CtryOfRes uses Python identifier CtryOfRes
    __CtryOfRes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), 'CtryOfRes', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification4_urnCBIxsdCBIPaymentRequest_00_04_00CtryOfRes', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 267, 3), )

    
    CtryOfRes = property(__CtryOfRes.value, __CtryOfRes.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __PstlAdr.name() : __PstlAdr,
        __Id.name() : __Id,
        __CtryOfRes.name() : __CtryOfRes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPartyIdentification4 = CBIPartyIdentification4
Namespace.addCategoryObject('typeBinding', 'CBIPartyIdentification4', CBIPartyIdentification4)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPartyIdentification5 with content type ELEMENT_ONLY
class CBIPartyIdentification5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPartyIdentification5 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPartyIdentification5')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 270, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification5_urnCBIxsdCBIPaymentRequest_00_04_00Nm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 272, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPartyIdentification5_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 273, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPartyIdentification5 = CBIPartyIdentification5
Namespace.addCategoryObject('typeBinding', 'CBIPartyIdentification5', CBIPartyIdentification5)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPaymentTypeInformation1 with content type ELEMENT_ONLY
class CBIPaymentTypeInformation1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPaymentTypeInformation1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPaymentTypeInformation1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 276, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}InstrPrty uses Python identifier InstrPrty
    __InstrPrty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstrPrty'), 'InstrPrty', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentTypeInformation1_urnCBIxsdCBIPaymentRequest_00_04_00InstrPrty', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 278, 3), )

    
    InstrPrty = property(__InstrPrty.value, __InstrPrty.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}SvcLvl uses Python identifier SvcLvl
    __SvcLvl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl'), 'SvcLvl', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentTypeInformation1_urnCBIxsdCBIPaymentRequest_00_04_00SvcLvl', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 279, 3), )

    
    SvcLvl = property(__SvcLvl.value, __SvcLvl.set, None, None)

    _ElementMap.update({
        __InstrPrty.name() : __InstrPrty,
        __SvcLvl.name() : __SvcLvl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPaymentTypeInformation1 = CBIPaymentTypeInformation1
Namespace.addCategoryObject('typeBinding', 'CBIPaymentTypeInformation1', CBIPaymentTypeInformation1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPaymentTypeInformation2 with content type ELEMENT_ONLY
class CBIPaymentTypeInformation2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPaymentTypeInformation2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPaymentTypeInformation2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 282, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}SvcLvl uses Python identifier SvcLvl
    __SvcLvl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl'), 'SvcLvl', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentTypeInformation2_urnCBIxsdCBIPaymentRequest_00_04_00SvcLvl', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 284, 3), )

    
    SvcLvl = property(__SvcLvl.value, __SvcLvl.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}LclInstrm uses Python identifier LclInstrm
    __LclInstrm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LclInstrm'), 'LclInstrm', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentTypeInformation2_urnCBIxsdCBIPaymentRequest_00_04_00LclInstrm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 285, 3), )

    
    LclInstrm = property(__LclInstrm.value, __LclInstrm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CtgyPurp uses Python identifier CtgyPurp
    __CtgyPurp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtgyPurp'), 'CtgyPurp', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPaymentTypeInformation2_urnCBIxsdCBIPaymentRequest_00_04_00CtgyPurp', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 286, 3), )

    
    CtgyPurp = property(__CtgyPurp.value, __CtgyPurp.set, None, None)

    _ElementMap.update({
        __SvcLvl.name() : __SvcLvl,
        __LclInstrm.name() : __LclInstrm,
        __CtgyPurp.name() : __CtgyPurp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPaymentTypeInformation2 = CBIPaymentTypeInformation2
Namespace.addCategoryObject('typeBinding', 'CBIPaymentTypeInformation2', CBIPaymentTypeInformation2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPersonIdentification1 with content type ELEMENT_ONLY
class CBIPersonIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPersonIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPersonIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 289, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPersonIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00Othr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 291, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPersonIdentification1 = CBIPersonIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIPersonIdentification1', CBIPersonIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPostalAddress6 with content type ELEMENT_ONLY
class CBIPostalAddress6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIPostalAddress6 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPostalAddress6')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 294, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}AdrTp uses Python identifier AdrTp
    __AdrTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdrTp'), 'AdrTp', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPostalAddress6_urnCBIxsdCBIPaymentRequest_00_04_00AdrTp', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 296, 3), )

    
    AdrTp = property(__AdrTp.value, __AdrTp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Dept uses Python identifier Dept
    __Dept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dept'), 'Dept', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPostalAddress6_urnCBIxsdCBIPaymentRequest_00_04_00Dept', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 297, 3), )

    
    Dept = property(__Dept.value, __Dept.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}SubDept uses Python identifier SubDept
    __SubDept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubDept'), 'SubDept', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPostalAddress6_urnCBIxsdCBIPaymentRequest_00_04_00SubDept', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 298, 3), )

    
    SubDept = property(__SubDept.value, __SubDept.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}StrtNm uses Python identifier StrtNm
    __StrtNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StrtNm'), 'StrtNm', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPostalAddress6_urnCBIxsdCBIPaymentRequest_00_04_00StrtNm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 299, 3), )

    
    StrtNm = property(__StrtNm.value, __StrtNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}BldgNb uses Python identifier BldgNb
    __BldgNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BldgNb'), 'BldgNb', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPostalAddress6_urnCBIxsdCBIPaymentRequest_00_04_00BldgNb', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 300, 3), )

    
    BldgNb = property(__BldgNb.value, __BldgNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PstCd uses Python identifier PstCd
    __PstCd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstCd'), 'PstCd', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPostalAddress6_urnCBIxsdCBIPaymentRequest_00_04_00PstCd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 301, 3), )

    
    PstCd = property(__PstCd.value, __PstCd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}TwnNm uses Python identifier TwnNm
    __TwnNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TwnNm'), 'TwnNm', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPostalAddress6_urnCBIxsdCBIPaymentRequest_00_04_00TwnNm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 302, 3), )

    
    TwnNm = property(__TwnNm.value, __TwnNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CtrySubDvsn uses Python identifier CtrySubDvsn
    __CtrySubDvsn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtrySubDvsn'), 'CtrySubDvsn', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPostalAddress6_urnCBIxsdCBIPaymentRequest_00_04_00CtrySubDvsn', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 303, 3), )

    
    CtrySubDvsn = property(__CtrySubDvsn.value, __CtrySubDvsn.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Ctry uses Python identifier Ctry
    __Ctry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), 'Ctry', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPostalAddress6_urnCBIxsdCBIPaymentRequest_00_04_00Ctry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 304, 3), )

    
    Ctry = property(__Ctry.value, __Ctry.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}AdrLine uses Python identifier AdrLine
    __AdrLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdrLine'), 'AdrLine', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIPostalAddress6_urnCBIxsdCBIPaymentRequest_00_04_00AdrLine', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 305, 3), )

    
    AdrLine = property(__AdrLine.value, __AdrLine.set, None, None)

    _ElementMap.update({
        __AdrTp.name() : __AdrTp,
        __Dept.name() : __Dept,
        __SubDept.name() : __SubDept,
        __StrtNm.name() : __StrtNm,
        __BldgNb.name() : __BldgNb,
        __PstCd.name() : __PstCd,
        __TwnNm.name() : __TwnNm,
        __CtrySubDvsn.name() : __CtrySubDvsn,
        __Ctry.name() : __Ctry,
        __AdrLine.name() : __AdrLine
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPostalAddress6 = CBIPostalAddress6
Namespace.addCategoryObject('typeBinding', 'CBIPostalAddress6', CBIPostalAddress6)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIRegulatoryReporting1 with content type ELEMENT_ONLY
class CBIRegulatoryReporting1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIRegulatoryReporting1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIRegulatoryReporting1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 308, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DbtCdtRptgInd uses Python identifier DbtCdtRptgInd
    __DbtCdtRptgInd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DbtCdtRptgInd'), 'DbtCdtRptgInd', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIRegulatoryReporting1_urnCBIxsdCBIPaymentRequest_00_04_00DbtCdtRptgInd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 310, 3), )

    
    DbtCdtRptgInd = property(__DbtCdtRptgInd.value, __DbtCdtRptgInd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Dtls uses Python identifier Dtls
    __Dtls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dtls'), 'Dtls', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIRegulatoryReporting1_urnCBIxsdCBIPaymentRequest_00_04_00Dtls', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 311, 3), )

    
    Dtls = property(__Dtls.value, __Dtls.set, None, None)

    _ElementMap.update({
        __DbtCdtRptgInd.name() : __DbtCdtRptgInd,
        __Dtls.name() : __Dtls
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIRegulatoryReporting1 = CBIRegulatoryReporting1
Namespace.addCategoryObject('typeBinding', 'CBIRegulatoryReporting1', CBIRegulatoryReporting1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIRemittanceLocation1 with content type ELEMENT_ONLY
class CBIRemittanceLocation1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIRemittanceLocation1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIRemittanceLocation1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 314, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RmtId uses Python identifier RmtId
    __RmtId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtId'), 'RmtId', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIRemittanceLocation1_urnCBIxsdCBIPaymentRequest_00_04_00RmtId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 316, 3), )

    
    RmtId = property(__RmtId.value, __RmtId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RmtLctnMtd uses Python identifier RmtLctnMtd
    __RmtLctnMtd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtLctnMtd'), 'RmtLctnMtd', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIRemittanceLocation1_urnCBIxsdCBIPaymentRequest_00_04_00RmtLctnMtd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 317, 3), )

    
    RmtLctnMtd = property(__RmtLctnMtd.value, __RmtLctnMtd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RmtLctnElctrncAdr uses Python identifier RmtLctnElctrncAdr
    __RmtLctnElctrncAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtLctnElctrncAdr'), 'RmtLctnElctrncAdr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIRemittanceLocation1_urnCBIxsdCBIPaymentRequest_00_04_00RmtLctnElctrncAdr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 318, 3), )

    
    RmtLctnElctrncAdr = property(__RmtLctnElctrncAdr.value, __RmtLctnElctrncAdr.set, None, None)

    _ElementMap.update({
        __RmtId.name() : __RmtId,
        __RmtLctnMtd.name() : __RmtLctnMtd,
        __RmtLctnElctrncAdr.name() : __RmtLctnElctrncAdr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIRemittanceLocation1 = CBIRemittanceLocation1
Namespace.addCategoryObject('typeBinding', 'CBIRemittanceLocation1', CBIRemittanceLocation1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIServiceLevel1 with content type ELEMENT_ONLY
class CBIServiceLevel1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIServiceLevel1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIServiceLevel1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 321, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIServiceLevel1_urnCBIxsdCBIPaymentRequest_00_04_00Cd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 323, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIServiceLevel1 = CBIServiceLevel1
Namespace.addCategoryObject('typeBinding', 'CBIServiceLevel1', CBIServiceLevel1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIServiceLevel2 with content type ELEMENT_ONLY
class CBIServiceLevel2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIServiceLevel2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIServiceLevel2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 326, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIServiceLevel2_urnCBIxsdCBIPaymentRequest_00_04_00Prtry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 328, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIServiceLevel2 = CBIServiceLevel2
Namespace.addCategoryObject('typeBinding', 'CBIServiceLevel2', CBIServiceLevel2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIStructuredRegulatoryReporting1 with content type ELEMENT_ONLY
class CBIStructuredRegulatoryReporting1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CBIStructuredRegulatoryReporting1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIStructuredRegulatoryReporting1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 331, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIStructuredRegulatoryReporting1_urnCBIxsdCBIPaymentRequest_00_04_00Cd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 333, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIStructuredRegulatoryReporting1_urnCBIxsdCBIPaymentRequest_00_04_00Amt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 342, 3), )

    
    Amt = property(__Amt.value, __Amt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Inf uses Python identifier Inf
    __Inf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Inf'), 'Inf', '__urnCBIxsdCBIPaymentRequest_00_04_00_CBIStructuredRegulatoryReporting1_urnCBIxsdCBIPaymentRequest_00_04_00Inf', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 343, 3), )

    
    Inf = property(__Inf.value, __Inf.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Amt.name() : __Amt,
        __Inf.name() : __Inf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIStructuredRegulatoryReporting1 = CBIStructuredRegulatoryReporting1
Namespace.addCategoryObject('typeBinding', 'CBIStructuredRegulatoryReporting1', CBIStructuredRegulatoryReporting1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ContactDetails2 with content type ELEMENT_ONLY
class ContactDetails2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ContactDetails2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContactDetails2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 346, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}NmPrfx uses Python identifier NmPrfx
    __NmPrfx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NmPrfx'), 'NmPrfx', '__urnCBIxsdCBIPaymentRequest_00_04_00_ContactDetails2_urnCBIxsdCBIPaymentRequest_00_04_00NmPrfx', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 348, 3), )

    
    NmPrfx = property(__NmPrfx.value, __NmPrfx.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_00_ContactDetails2_urnCBIxsdCBIPaymentRequest_00_04_00Nm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 349, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PhneNb uses Python identifier PhneNb
    __PhneNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PhneNb'), 'PhneNb', '__urnCBIxsdCBIPaymentRequest_00_04_00_ContactDetails2_urnCBIxsdCBIPaymentRequest_00_04_00PhneNb', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 350, 3), )

    
    PhneNb = property(__PhneNb.value, __PhneNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}MobNb uses Python identifier MobNb
    __MobNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MobNb'), 'MobNb', '__urnCBIxsdCBIPaymentRequest_00_04_00_ContactDetails2_urnCBIxsdCBIPaymentRequest_00_04_00MobNb', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 351, 3), )

    
    MobNb = property(__MobNb.value, __MobNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}FaxNb uses Python identifier FaxNb
    __FaxNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FaxNb'), 'FaxNb', '__urnCBIxsdCBIPaymentRequest_00_04_00_ContactDetails2_urnCBIxsdCBIPaymentRequest_00_04_00FaxNb', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 352, 3), )

    
    FaxNb = property(__FaxNb.value, __FaxNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}EmailAdr uses Python identifier EmailAdr
    __EmailAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmailAdr'), 'EmailAdr', '__urnCBIxsdCBIPaymentRequest_00_04_00_ContactDetails2_urnCBIxsdCBIPaymentRequest_00_04_00EmailAdr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 353, 3), )

    
    EmailAdr = property(__EmailAdr.value, __EmailAdr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_00_ContactDetails2_urnCBIxsdCBIPaymentRequest_00_04_00Othr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 354, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __NmPrfx.name() : __NmPrfx,
        __Nm.name() : __Nm,
        __PhneNb.name() : __PhneNb,
        __MobNb.name() : __MobNb,
        __FaxNb.name() : __FaxNb,
        __EmailAdr.name() : __EmailAdr,
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ContactDetails2 = ContactDetails2
Namespace.addCategoryObject('typeBinding', 'ContactDetails2', ContactDetails2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CreditorReferenceInformation2 with content type ELEMENT_ONLY
class CreditorReferenceInformation2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CreditorReferenceInformation2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreditorReferenceInformation2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 357, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_00_CreditorReferenceInformation2_urnCBIxsdCBIPaymentRequest_00_04_00Tp', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 359, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Ref uses Python identifier Ref
    __Ref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ref'), 'Ref', '__urnCBIxsdCBIPaymentRequest_00_04_00_CreditorReferenceInformation2_urnCBIxsdCBIPaymentRequest_00_04_00Ref', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 360, 3), )

    
    Ref = property(__Ref.value, __Ref.set, None, None)

    _ElementMap.update({
        __Tp.name() : __Tp,
        __Ref.name() : __Ref
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CreditorReferenceInformation2 = CreditorReferenceInformation2
Namespace.addCategoryObject('typeBinding', 'CreditorReferenceInformation2', CreditorReferenceInformation2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CreditorReferenceType1Choice with content type ELEMENT_ONLY
class CreditorReferenceType1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CreditorReferenceType1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreditorReferenceType1Choice')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 363, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_00_CreditorReferenceType1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Cd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 366, 4), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_00_CreditorReferenceType1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Prtry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 367, 4), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CreditorReferenceType1Choice = CreditorReferenceType1Choice
Namespace.addCategoryObject('typeBinding', 'CreditorReferenceType1Choice', CreditorReferenceType1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CreditorReferenceType2 with content type ELEMENT_ONLY
class CreditorReferenceType2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CreditorReferenceType2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreditorReferenceType2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 371, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CdOrPrtry uses Python identifier CdOrPrtry
    __CdOrPrtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), 'CdOrPrtry', '__urnCBIxsdCBIPaymentRequest_00_04_00_CreditorReferenceType2_urnCBIxsdCBIPaymentRequest_00_04_00CdOrPrtry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 373, 3), )

    
    CdOrPrtry = property(__CdOrPrtry.value, __CdOrPrtry.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_00_CreditorReferenceType2_urnCBIxsdCBIPaymentRequest_00_04_00Issr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 374, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __CdOrPrtry.name() : __CdOrPrtry,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CreditorReferenceType2 = CreditorReferenceType2
Namespace.addCategoryObject('typeBinding', 'CreditorReferenceType2', CreditorReferenceType2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DateAndPlaceOfBirth with content type ELEMENT_ONLY
class DateAndPlaceOfBirth (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DateAndPlaceOfBirth with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateAndPlaceOfBirth')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 377, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}BirthDt uses Python identifier BirthDt
    __BirthDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BirthDt'), 'BirthDt', '__urnCBIxsdCBIPaymentRequest_00_04_00_DateAndPlaceOfBirth_urnCBIxsdCBIPaymentRequest_00_04_00BirthDt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 379, 3), )

    
    BirthDt = property(__BirthDt.value, __BirthDt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PrvcOfBirth uses Python identifier PrvcOfBirth
    __PrvcOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrvcOfBirth'), 'PrvcOfBirth', '__urnCBIxsdCBIPaymentRequest_00_04_00_DateAndPlaceOfBirth_urnCBIxsdCBIPaymentRequest_00_04_00PrvcOfBirth', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 380, 3), )

    
    PrvcOfBirth = property(__PrvcOfBirth.value, __PrvcOfBirth.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CityOfBirth uses Python identifier CityOfBirth
    __CityOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CityOfBirth'), 'CityOfBirth', '__urnCBIxsdCBIPaymentRequest_00_04_00_DateAndPlaceOfBirth_urnCBIxsdCBIPaymentRequest_00_04_00CityOfBirth', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 381, 3), )

    
    CityOfBirth = property(__CityOfBirth.value, __CityOfBirth.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CtryOfBirth uses Python identifier CtryOfBirth
    __CtryOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfBirth'), 'CtryOfBirth', '__urnCBIxsdCBIPaymentRequest_00_04_00_DateAndPlaceOfBirth_urnCBIxsdCBIPaymentRequest_00_04_00CtryOfBirth', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 382, 3), )

    
    CtryOfBirth = property(__CtryOfBirth.value, __CtryOfBirth.set, None, None)

    _ElementMap.update({
        __BirthDt.name() : __BirthDt,
        __PrvcOfBirth.name() : __PrvcOfBirth,
        __CityOfBirth.name() : __CityOfBirth,
        __CtryOfBirth.name() : __CtryOfBirth
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DateAndPlaceOfBirth = DateAndPlaceOfBirth
Namespace.addCategoryObject('typeBinding', 'DateAndPlaceOfBirth', DateAndPlaceOfBirth)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DocumentAdjustment1 with content type ELEMENT_ONLY
class DocumentAdjustment1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DocumentAdjustment1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentAdjustment1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 385, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnCBIxsdCBIPaymentRequest_00_04_00_DocumentAdjustment1_urnCBIxsdCBIPaymentRequest_00_04_00Amt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 387, 3), )

    
    Amt = property(__Amt.value, __Amt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CdtDbtInd uses Python identifier CdtDbtInd
    __CdtDbtInd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtDbtInd'), 'CdtDbtInd', '__urnCBIxsdCBIPaymentRequest_00_04_00_DocumentAdjustment1_urnCBIxsdCBIPaymentRequest_00_04_00CdtDbtInd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 388, 3), )

    
    CdtDbtInd = property(__CdtDbtInd.value, __CdtDbtInd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Rsn uses Python identifier Rsn
    __Rsn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rsn'), 'Rsn', '__urnCBIxsdCBIPaymentRequest_00_04_00_DocumentAdjustment1_urnCBIxsdCBIPaymentRequest_00_04_00Rsn', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 389, 3), )

    
    Rsn = property(__Rsn.value, __Rsn.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}AddtlInf uses Python identifier AddtlInf
    __AddtlInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddtlInf'), 'AddtlInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_DocumentAdjustment1_urnCBIxsdCBIPaymentRequest_00_04_00AddtlInf', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 390, 3), )

    
    AddtlInf = property(__AddtlInf.value, __AddtlInf.set, None, None)

    _ElementMap.update({
        __Amt.name() : __Amt,
        __CdtDbtInd.name() : __CdtDbtInd,
        __Rsn.name() : __Rsn,
        __AddtlInf.name() : __AddtlInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DocumentAdjustment1 = DocumentAdjustment1
Namespace.addCategoryObject('typeBinding', 'DocumentAdjustment1', DocumentAdjustment1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}GenericIdentification3 with content type ELEMENT_ONLY
class GenericIdentification3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}GenericIdentification3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericIdentification3')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 393, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_GenericIdentification3_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 395, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_00_GenericIdentification3_urnCBIxsdCBIPaymentRequest_00_04_00Issr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 396, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericIdentification3 = GenericIdentification3
Namespace.addCategoryObject('typeBinding', 'GenericIdentification3', GenericIdentification3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}GenericOrganisationIdentification1 with content type ELEMENT_ONLY
class GenericOrganisationIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}GenericOrganisationIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericOrganisationIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 399, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_GenericOrganisationIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 401, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}SchmeNm uses Python identifier SchmeNm
    __SchmeNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), 'SchmeNm', '__urnCBIxsdCBIPaymentRequest_00_04_00_GenericOrganisationIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00SchmeNm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 402, 3), )

    
    SchmeNm = property(__SchmeNm.value, __SchmeNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_00_GenericOrganisationIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00Issr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 403, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __SchmeNm.name() : __SchmeNm,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericOrganisationIdentification1 = GenericOrganisationIdentification1
Namespace.addCategoryObject('typeBinding', 'GenericOrganisationIdentification1', GenericOrganisationIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}GenericPersonIdentification1 with content type ELEMENT_ONLY
class GenericPersonIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}GenericPersonIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericPersonIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 406, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_GenericPersonIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 408, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}SchmeNm uses Python identifier SchmeNm
    __SchmeNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), 'SchmeNm', '__urnCBIxsdCBIPaymentRequest_00_04_00_GenericPersonIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00SchmeNm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 409, 3), )

    
    SchmeNm = property(__SchmeNm.value, __SchmeNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_00_GenericPersonIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00Issr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 410, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __SchmeNm.name() : __SchmeNm,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericPersonIdentification1 = GenericPersonIdentification1
Namespace.addCategoryObject('typeBinding', 'GenericPersonIdentification1', GenericPersonIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}OrganisationIdentification4 with content type ELEMENT_ONLY
class OrganisationIdentification4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}OrganisationIdentification4 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrganisationIdentification4')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 413, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}BICOrBEI uses Python identifier BICOrBEI
    __BICOrBEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI'), 'BICOrBEI', '__urnCBIxsdCBIPaymentRequest_00_04_00_OrganisationIdentification4_urnCBIxsdCBIPaymentRequest_00_04_00BICOrBEI', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 415, 3), )

    
    BICOrBEI = property(__BICOrBEI.value, __BICOrBEI.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_00_OrganisationIdentification4_urnCBIxsdCBIPaymentRequest_00_04_00Othr', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 416, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __BICOrBEI.name() : __BICOrBEI,
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrganisationIdentification4 = OrganisationIdentification4
Namespace.addCategoryObject('typeBinding', 'OrganisationIdentification4', OrganisationIdentification4)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}OrganisationIdentificationSchemeName1Choice with content type ELEMENT_ONLY
class OrganisationIdentificationSchemeName1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}OrganisationIdentificationSchemeName1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrganisationIdentificationSchemeName1Choice')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 419, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_00_OrganisationIdentificationSchemeName1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Cd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 422, 4), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_00_OrganisationIdentificationSchemeName1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Prtry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 423, 4), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrganisationIdentificationSchemeName1Choice = OrganisationIdentificationSchemeName1Choice
Namespace.addCategoryObject('typeBinding', 'OrganisationIdentificationSchemeName1Choice', OrganisationIdentificationSchemeName1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PartyIdentification32 with content type ELEMENT_ONLY
class PartyIdentification32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PartyIdentification32 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyIdentification32')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 427, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_00_PartyIdentification32_urnCBIxsdCBIPaymentRequest_00_04_00Nm', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 429, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PstlAdr uses Python identifier PstlAdr
    __PstlAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), 'PstlAdr', '__urnCBIxsdCBIPaymentRequest_00_04_00_PartyIdentification32_urnCBIxsdCBIPaymentRequest_00_04_00PstlAdr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 430, 3), )

    
    PstlAdr = property(__PstlAdr.value, __PstlAdr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_00_PartyIdentification32_urnCBIxsdCBIPaymentRequest_00_04_00Id', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 431, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CtryOfRes uses Python identifier CtryOfRes
    __CtryOfRes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), 'CtryOfRes', '__urnCBIxsdCBIPaymentRequest_00_04_00_PartyIdentification32_urnCBIxsdCBIPaymentRequest_00_04_00CtryOfRes', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 432, 3), )

    
    CtryOfRes = property(__CtryOfRes.value, __CtryOfRes.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CtctDtls uses Python identifier CtctDtls
    __CtctDtls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtctDtls'), 'CtctDtls', '__urnCBIxsdCBIPaymentRequest_00_04_00_PartyIdentification32_urnCBIxsdCBIPaymentRequest_00_04_00CtctDtls', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 433, 3), )

    
    CtctDtls = property(__CtctDtls.value, __CtctDtls.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __PstlAdr.name() : __PstlAdr,
        __Id.name() : __Id,
        __CtryOfRes.name() : __CtryOfRes,
        __CtctDtls.name() : __CtctDtls
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartyIdentification32 = PartyIdentification32
Namespace.addCategoryObject('typeBinding', 'PartyIdentification32', PartyIdentification32)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Party6Choice with content type ELEMENT_ONLY
class Party6Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Party6Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Party6Choice')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 436, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId', '__urnCBIxsdCBIPaymentRequest_00_04_00_Party6Choice_urnCBIxsdCBIPaymentRequest_00_04_00OrgId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 439, 4), )

    
    OrgId = property(__OrgId.value, __OrgId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PrvtId uses Python identifier PrvtId
    __PrvtId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrvtId'), 'PrvtId', '__urnCBIxsdCBIPaymentRequest_00_04_00_Party6Choice_urnCBIxsdCBIPaymentRequest_00_04_00PrvtId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 440, 4), )

    
    PrvtId = property(__PrvtId.value, __PrvtId.set, None, None)

    _ElementMap.update({
        __OrgId.name() : __OrgId,
        __PrvtId.name() : __PrvtId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Party6Choice = Party6Choice
Namespace.addCategoryObject('typeBinding', 'Party6Choice', Party6Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PaymentIdentification1 with content type ELEMENT_ONLY
class PaymentIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PaymentIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 444, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}InstrId uses Python identifier InstrId
    __InstrId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstrId'), 'InstrId', '__urnCBIxsdCBIPaymentRequest_00_04_00_PaymentIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00InstrId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 446, 3), )

    
    InstrId = property(__InstrId.value, __InstrId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}EndToEndId uses Python identifier EndToEndId
    __EndToEndId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndToEndId'), 'EndToEndId', '__urnCBIxsdCBIPaymentRequest_00_04_00_PaymentIdentification1_urnCBIxsdCBIPaymentRequest_00_04_00EndToEndId', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 447, 3), )

    
    EndToEndId = property(__EndToEndId.value, __EndToEndId.set, None, None)

    _ElementMap.update({
        __InstrId.name() : __InstrId,
        __EndToEndId.name() : __EndToEndId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaymentIdentification1 = PaymentIdentification1
Namespace.addCategoryObject('typeBinding', 'PaymentIdentification1', PaymentIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PersonIdentification5 with content type ELEMENT_ONLY
class PersonIdentification5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PersonIdentification5 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonIdentification5')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 450, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DtAndPlcOfBirth uses Python identifier DtAndPlcOfBirth
    __DtAndPlcOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DtAndPlcOfBirth'), 'DtAndPlcOfBirth', '__urnCBIxsdCBIPaymentRequest_00_04_00_PersonIdentification5_urnCBIxsdCBIPaymentRequest_00_04_00DtAndPlcOfBirth', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 452, 3), )

    
    DtAndPlcOfBirth = property(__DtAndPlcOfBirth.value, __DtAndPlcOfBirth.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_00_PersonIdentification5_urnCBIxsdCBIPaymentRequest_00_04_00Othr', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 453, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __DtAndPlcOfBirth.name() : __DtAndPlcOfBirth,
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PersonIdentification5 = PersonIdentification5
Namespace.addCategoryObject('typeBinding', 'PersonIdentification5', PersonIdentification5)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PersonIdentificationSchemeName1Choice with content type ELEMENT_ONLY
class PersonIdentificationSchemeName1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}PersonIdentificationSchemeName1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonIdentificationSchemeName1Choice')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 456, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_00_PersonIdentificationSchemeName1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Cd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 459, 4), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_00_PersonIdentificationSchemeName1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Prtry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 460, 4), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PersonIdentificationSchemeName1Choice = PersonIdentificationSchemeName1Choice
Namespace.addCategoryObject('typeBinding', 'PersonIdentificationSchemeName1Choice', PersonIdentificationSchemeName1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Purpose1Choice with content type ELEMENT_ONLY
class Purpose1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Purpose1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Purpose1Choice')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 464, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_00_Purpose1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Cd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 467, 4), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_00_Purpose1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Prtry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 468, 4), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Purpose1Choice = Purpose1Choice
Namespace.addCategoryObject('typeBinding', 'Purpose1Choice', Purpose1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RemittanceInformation5 with content type ELEMENT_ONLY
class RemittanceInformation5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RemittanceInformation5 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RemittanceInformation5')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 472, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Ustrd uses Python identifier Ustrd
    __Ustrd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ustrd'), 'Ustrd', '__urnCBIxsdCBIPaymentRequest_00_04_00_RemittanceInformation5_urnCBIxsdCBIPaymentRequest_00_04_00Ustrd', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 474, 3), )

    
    Ustrd = property(__Ustrd.value, __Ustrd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Strd uses Python identifier Strd
    __Strd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Strd'), 'Strd', '__urnCBIxsdCBIPaymentRequest_00_04_00_RemittanceInformation5_urnCBIxsdCBIPaymentRequest_00_04_00Strd', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 475, 3), )

    
    Strd = property(__Strd.value, __Strd.set, None, None)

    _ElementMap.update({
        __Ustrd.name() : __Ustrd,
        __Strd.name() : __Strd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RemittanceInformation5 = RemittanceInformation5
Namespace.addCategoryObject('typeBinding', 'RemittanceInformation5', RemittanceInformation5)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ReferredDocumentInformation3 with content type ELEMENT_ONLY
class ReferredDocumentInformation3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ReferredDocumentInformation3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferredDocumentInformation3')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 478, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_00_ReferredDocumentInformation3_urnCBIxsdCBIPaymentRequest_00_04_00Tp', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 480, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Nb uses Python identifier Nb
    __Nb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nb'), 'Nb', '__urnCBIxsdCBIPaymentRequest_00_04_00_ReferredDocumentInformation3_urnCBIxsdCBIPaymentRequest_00_04_00Nb', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 481, 3), )

    
    Nb = property(__Nb.value, __Nb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RltdDt uses Python identifier RltdDt
    __RltdDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RltdDt'), 'RltdDt', '__urnCBIxsdCBIPaymentRequest_00_04_00_ReferredDocumentInformation3_urnCBIxsdCBIPaymentRequest_00_04_00RltdDt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 482, 3), )

    
    RltdDt = property(__RltdDt.value, __RltdDt.set, None, None)

    _ElementMap.update({
        __Tp.name() : __Tp,
        __Nb.name() : __Nb,
        __RltdDt.name() : __RltdDt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferredDocumentInformation3 = ReferredDocumentInformation3
Namespace.addCategoryObject('typeBinding', 'ReferredDocumentInformation3', ReferredDocumentInformation3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ReferredDocumentType1Choice with content type ELEMENT_ONLY
class ReferredDocumentType1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ReferredDocumentType1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferredDocumentType1Choice')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 485, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_00_ReferredDocumentType1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Cd', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 488, 4), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_00_ReferredDocumentType1Choice_urnCBIxsdCBIPaymentRequest_00_04_00Prtry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 489, 4), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferredDocumentType1Choice = ReferredDocumentType1Choice
Namespace.addCategoryObject('typeBinding', 'ReferredDocumentType1Choice', ReferredDocumentType1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ReferredDocumentType2 with content type ELEMENT_ONLY
class ReferredDocumentType2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ReferredDocumentType2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferredDocumentType2')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 493, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CdOrPrtry uses Python identifier CdOrPrtry
    __CdOrPrtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), 'CdOrPrtry', '__urnCBIxsdCBIPaymentRequest_00_04_00_ReferredDocumentType2_urnCBIxsdCBIPaymentRequest_00_04_00CdOrPrtry', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 495, 3), )

    
    CdOrPrtry = property(__CdOrPrtry.value, __CdOrPrtry.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_00_ReferredDocumentType2_urnCBIxsdCBIPaymentRequest_00_04_00Issr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 496, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __CdOrPrtry.name() : __CdOrPrtry,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferredDocumentType2 = ReferredDocumentType2
Namespace.addCategoryObject('typeBinding', 'ReferredDocumentType2', ReferredDocumentType2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RemittanceAmount1 with content type ELEMENT_ONLY
class RemittanceAmount1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RemittanceAmount1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RemittanceAmount1')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 499, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DuePyblAmt uses Python identifier DuePyblAmt
    __DuePyblAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DuePyblAmt'), 'DuePyblAmt', '__urnCBIxsdCBIPaymentRequest_00_04_00_RemittanceAmount1_urnCBIxsdCBIPaymentRequest_00_04_00DuePyblAmt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 501, 3), )

    
    DuePyblAmt = property(__DuePyblAmt.value, __DuePyblAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}DscntApldAmt uses Python identifier DscntApldAmt
    __DscntApldAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DscntApldAmt'), 'DscntApldAmt', '__urnCBIxsdCBIPaymentRequest_00_04_00_RemittanceAmount1_urnCBIxsdCBIPaymentRequest_00_04_00DscntApldAmt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 502, 3), )

    
    DscntApldAmt = property(__DscntApldAmt.value, __DscntApldAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CdtNoteAmt uses Python identifier CdtNoteAmt
    __CdtNoteAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtNoteAmt'), 'CdtNoteAmt', '__urnCBIxsdCBIPaymentRequest_00_04_00_RemittanceAmount1_urnCBIxsdCBIPaymentRequest_00_04_00CdtNoteAmt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 503, 3), )

    
    CdtNoteAmt = property(__CdtNoteAmt.value, __CdtNoteAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}TaxAmt uses Python identifier TaxAmt
    __TaxAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt'), 'TaxAmt', '__urnCBIxsdCBIPaymentRequest_00_04_00_RemittanceAmount1_urnCBIxsdCBIPaymentRequest_00_04_00TaxAmt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 504, 3), )

    
    TaxAmt = property(__TaxAmt.value, __TaxAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}AdjstmntAmtAndRsn uses Python identifier AdjstmntAmtAndRsn
    __AdjstmntAmtAndRsn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdjstmntAmtAndRsn'), 'AdjstmntAmtAndRsn', '__urnCBIxsdCBIPaymentRequest_00_04_00_RemittanceAmount1_urnCBIxsdCBIPaymentRequest_00_04_00AdjstmntAmtAndRsn', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 505, 3), )

    
    AdjstmntAmtAndRsn = property(__AdjstmntAmtAndRsn.value, __AdjstmntAmtAndRsn.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RmtdAmt uses Python identifier RmtdAmt
    __RmtdAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt'), 'RmtdAmt', '__urnCBIxsdCBIPaymentRequest_00_04_00_RemittanceAmount1_urnCBIxsdCBIPaymentRequest_00_04_00RmtdAmt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 506, 3), )

    
    RmtdAmt = property(__RmtdAmt.value, __RmtdAmt.set, None, None)

    _ElementMap.update({
        __DuePyblAmt.name() : __DuePyblAmt,
        __DscntApldAmt.name() : __DscntApldAmt,
        __CdtNoteAmt.name() : __CdtNoteAmt,
        __TaxAmt.name() : __TaxAmt,
        __AdjstmntAmtAndRsn.name() : __AdjstmntAmtAndRsn,
        __RmtdAmt.name() : __RmtdAmt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RemittanceAmount1 = RemittanceAmount1
Namespace.addCategoryObject('typeBinding', 'RemittanceAmount1', RemittanceAmount1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}StructuredRemittanceInformation7 with content type ELEMENT_ONLY
class StructuredRemittanceInformation7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}StructuredRemittanceInformation7 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StructuredRemittanceInformation7')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 509, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RfrdDocInf uses Python identifier RfrdDocInf
    __RfrdDocInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocInf'), 'RfrdDocInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_StructuredRemittanceInformation7_urnCBIxsdCBIPaymentRequest_00_04_00RfrdDocInf', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 511, 3), )

    
    RfrdDocInf = property(__RfrdDocInf.value, __RfrdDocInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}RfrdDocAmt uses Python identifier RfrdDocAmt
    __RfrdDocAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocAmt'), 'RfrdDocAmt', '__urnCBIxsdCBIPaymentRequest_00_04_00_StructuredRemittanceInformation7_urnCBIxsdCBIPaymentRequest_00_04_00RfrdDocAmt', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 512, 3), )

    
    RfrdDocAmt = property(__RfrdDocAmt.value, __RfrdDocAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}CdtrRefInf uses Python identifier CdtrRefInf
    __CdtrRefInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtrRefInf'), 'CdtrRefInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_StructuredRemittanceInformation7_urnCBIxsdCBIPaymentRequest_00_04_00CdtrRefInf', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 513, 3), )

    
    CdtrRefInf = property(__CdtrRefInf.value, __CdtrRefInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Invcr uses Python identifier Invcr
    __Invcr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Invcr'), 'Invcr', '__urnCBIxsdCBIPaymentRequest_00_04_00_StructuredRemittanceInformation7_urnCBIxsdCBIPaymentRequest_00_04_00Invcr', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 514, 3), )

    
    Invcr = property(__Invcr.value, __Invcr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}Invcee uses Python identifier Invcee
    __Invcee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Invcee'), 'Invcee', '__urnCBIxsdCBIPaymentRequest_00_04_00_StructuredRemittanceInformation7_urnCBIxsdCBIPaymentRequest_00_04_00Invcee', False, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 515, 3), )

    
    Invcee = property(__Invcee.value, __Invcee.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.00}AddtlRmtInf uses Python identifier AddtlRmtInf
    __AddtlRmtInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddtlRmtInf'), 'AddtlRmtInf', '__urnCBIxsdCBIPaymentRequest_00_04_00_StructuredRemittanceInformation7_urnCBIxsdCBIPaymentRequest_00_04_00AddtlRmtInf', True, pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 516, 3), )

    
    AddtlRmtInf = property(__AddtlRmtInf.value, __AddtlRmtInf.set, None, None)

    _ElementMap.update({
        __RfrdDocInf.name() : __RfrdDocInf,
        __RfrdDocAmt.name() : __RfrdDocAmt,
        __CdtrRefInf.name() : __CdtrRefInf,
        __Invcr.name() : __Invcr,
        __Invcee.name() : __Invcee,
        __AddtlRmtInf.name() : __AddtlRmtInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StructuredRemittanceInformation7 = StructuredRemittanceInformation7
Namespace.addCategoryObject('typeBinding', 'StructuredRemittanceInformation7', StructuredRemittanceInformation7)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ActiveOrHistoricCurrencyAndAmount with content type SIMPLE
class ActiveOrHistoricCurrencyAndAmount (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.00}ActiveOrHistoricCurrencyAndAmount with content type SIMPLE"""
    _TypeDefinition = ActiveOrHistoricCurrencyAndAmount_SimpleType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveOrHistoricCurrencyAndAmount')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 101, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is ActiveOrHistoricCurrencyAndAmount_SimpleType
    
    # Attribute Ccy uses Python identifier Ccy
    __Ccy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Ccy'), 'Ccy', '__urnCBIxsdCBIPaymentRequest_00_04_00_ActiveOrHistoricCurrencyAndAmount_Ccy', _module_typeBindings.ActiveOrHistoricCurrencyCode, required=True)
    __Ccy._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 104, 4)
    __Ccy._UseLocation = pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 104, 4)
    
    Ccy = property(__Ccy.value, __Ccy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Ccy.name() : __Ccy
    })
_module_typeBindings.ActiveOrHistoricCurrencyAndAmount = ActiveOrHistoricCurrencyAndAmount
Namespace.addCategoryObject('typeBinding', 'ActiveOrHistoricCurrencyAndAmount', ActiveOrHistoricCurrencyAndAmount)


CBIPaymentRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CBIPaymentRequest'), CBIPaymentRequest_00_04_00, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 4, 1))
Namespace.addCategoryObject('elementBinding', CBIPaymentRequest.name().localName(), CBIPaymentRequest)



CBIPaymentRequest_00_04_00._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr'), CBIGroupHeader, scope=CBIPaymentRequest_00_04_00, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 8, 3)))

CBIPaymentRequest_00_04_00._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtInf'), CBIPaymentInstructionInformation, scope=CBIPaymentRequest_00_04_00, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 9, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentRequest_00_04_00._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 8, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPaymentRequest_00_04_00._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 9, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPaymentRequest_00_04_00._Automaton = _BuildAutomaton()




CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MsgId'), Max35Text, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 16, 3)))

CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm'), ISODateTime, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 17, 3)))

CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs'), Max15NumericText, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 18, 3)))

CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum'), DecimalNumber, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 19, 3)))

CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InitgPty'), CBIPartyIdentification1, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 20, 3)))

CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FwdgAgt'), CBIBranchAndFinancialInstitutionIdentification1, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 21, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 21, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MsgId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 16, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 17, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 18, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 19, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InitgPty')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 20, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FwdgAgt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 21, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIGroupHeader._Automaton = _BuildAutomaton_()




CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtInfId'), Max35Text, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 33, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtMtd'), PaymentMethod3Code, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 34, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BtchBookg'), BatchBookingIndicator, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 35, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf'), CBIPaymentTypeInformation1, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 36, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReqdExctnDt'), ISODate, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 37, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dbtr'), CBIPartyIdentification4, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 38, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DbtrAcct'), CBICashAccount1, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 39, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DbtrAgt'), CBIBranchAndFinancialInstitutionIdentification2, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 40, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), CBIPartyIdentification2, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 41, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChrgBr'), CBIChargeBearerTypeCode, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 42, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChrgsAcct'), CBICashAccount1, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 43, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtTrfTxInf'), CBICreditTransferTransactionInformation, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 44, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 35, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 36, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 41, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 42, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 43, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtInfId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 33, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtMtd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 34, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BtchBookg')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 35, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 36, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReqdExctnDt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 37, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dbtr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 38, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DbtrAcct')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 39, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DbtrAgt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 40, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 41, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChrgBr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 42, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChrgsAcct')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 43, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtTrfTxInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 44, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPaymentInstructionInformation._Automaton = _BuildAutomaton_2()




CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtId'), PaymentIdentification1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 61, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf'), CBIPaymentTypeInformation2, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 62, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), CBIAmountType1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 63, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChqInstr'), CBICheque1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 64, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), CBIPartyIdentification2, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 65, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SrvInf'), CBISrvInf1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 66, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtrAgt'), CBIBranchAndFinancialInstitutionIdentification3, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 67, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cdtr'), CBIPartyIdentification3, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 68, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtrAcct'), CBICashAccount2, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 69, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UltmtCdtr'), CBIPartyIdentification3, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 70, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DestCdtrRsp'), CBIPartyIdentification5, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 71, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Purp'), Purpose1Choice, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 72, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RgltryRptg'), CBIRegulatoryReporting1, scope=CBICreditTransferTransactionInformation, documentation='Aggiunto blocco per ospitare le comunicazione valutarie sintetiche ', location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 73, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RltdRmtInf'), CBIRemittanceLocation1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 78, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtInf'), RemittanceInformation5, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 79, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 62, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 64, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 65, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 66, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 67, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 69, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 70, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 71, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 72, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 73, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=10, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 78, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 79, 3))
    counters.add(cc_11)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 61, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 62, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 63, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChqInstr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 64, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 65, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SrvInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 66, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtrAgt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 67, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cdtr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 68, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtrAcct')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 69, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UltmtCdtr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 70, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DestCdtrRsp')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 71, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Purp')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 72, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RgltryRptg')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 73, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RltdRmtInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 78, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 79, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBICreditTransferTransactionInformation._Automaton = _BuildAutomaton_3()




CategoryPurpose1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalCategoryPurpose1Code, scope=CategoryPurpose1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 111, 4)))

CategoryPurpose1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=CategoryPurpose1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 112, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CategoryPurpose1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 111, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CategoryPurpose1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 112, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CategoryPurpose1Choice._Automaton = _BuildAutomaton_4()




CBIAccountIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IBAN'), IBAN2007Identifier, scope=CBIAccountIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 118, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIAccountIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IBAN')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 118, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIAccountIdentification1._Automaton = _BuildAutomaton_5()




CBIAmountType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstdAmt'), ActiveOrHistoricCurrencyAndAmount, scope=CBIAmountType1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 123, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIAmountType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstdAmt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 123, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIAmountType1._Automaton = _BuildAutomaton_6()




CBIBranchAndFinancialInstitutionIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), CBIFinancialInstitutionIdentification1, scope=CBIBranchAndFinancialInstitutionIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 128, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIBranchAndFinancialInstitutionIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 128, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIBranchAndFinancialInstitutionIdentification1._Automaton = _BuildAutomaton_7()




CBIBranchAndFinancialInstitutionIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), CBIFinancialInstitutionIdentification3, scope=CBIBranchAndFinancialInstitutionIdentification2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 133, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIBranchAndFinancialInstitutionIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 133, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIBranchAndFinancialInstitutionIdentification2._Automaton = _BuildAutomaton_8()




CBIBranchAndFinancialInstitutionIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), CBIFinancialInstitutionIdentification2, scope=CBIBranchAndFinancialInstitutionIdentification3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 138, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIBranchAndFinancialInstitutionIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 138, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIBranchAndFinancialInstitutionIdentification3._Automaton = _BuildAutomaton_9()




CBICashAccount1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIAccountIdentification1, scope=CBICashAccount1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 143, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBICashAccount1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 143, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBICashAccount1._Automaton = _BuildAutomaton_10()




CBICashAccount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIAccountIdentification1, scope=CBICashAccount2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 148, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBICashAccount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 148, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBICashAccount2._Automaton = _BuildAutomaton_11()




CBICheque1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChqTp'), CBIChequeType1Code, scope=CBICheque1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 153, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 153, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBICheque1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChqTp')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 153, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBICheque1._Automaton = _BuildAutomaton_12()




CBIClearingSystemMemberIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MmbId'), Max35Text, scope=CBIClearingSystemMemberIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 158, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIClearingSystemMemberIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MmbId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 158, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIClearingSystemMemberIdentification1._Automaton = _BuildAutomaton_13()




CBIFinancialInstitutionIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId'), CBIClearingSystemMemberIdentification1, scope=CBIFinancialInstitutionIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 163, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIFinancialInstitutionIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 163, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIFinancialInstitutionIdentification1._Automaton = _BuildAutomaton_14()




CBIFinancialInstitutionIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BIC'), BICIdentifier, scope=CBIFinancialInstitutionIdentification2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 168, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIFinancialInstitutionIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BIC')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 168, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIFinancialInstitutionIdentification2._Automaton = _BuildAutomaton_15()




CBIFinancialInstitutionIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BIC'), BICIdentifier, scope=CBIFinancialInstitutionIdentification3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 173, 3)))

CBIFinancialInstitutionIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId'), CBIClearingSystemMemberIdentification1, scope=CBIFinancialInstitutionIdentification3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 174, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 173, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIFinancialInstitutionIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BIC')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 173, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIFinancialInstitutionIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 174, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIFinancialInstitutionIdentification3._Automaton = _BuildAutomaton_16()




CBIGenericIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=CBIGenericIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 179, 3)))

CBIGenericIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=CBIGenericIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 180, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 180, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIGenericIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 179, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIGenericIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 180, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIGenericIdentification1._Automaton = _BuildAutomaton_17()




CBIGenericIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=CBIGenericIdentification2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 185, 3)))

CBIGenericIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=CBIGenericIdentification2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 186, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIGenericIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 185, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIGenericIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 186, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIGenericIdentification2._Automaton = _BuildAutomaton_18()




CBIIdType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), CBIOrganisationIdentification1, scope=CBIIdType1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 191, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIIdType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 191, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIIdType1._Automaton = _BuildAutomaton_19()




CBIIdType2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), CBIOrganisationIdentification3, scope=CBIIdType2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 196, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIIdType2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 196, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIIdType2._Automaton = _BuildAutomaton_20()




CBIIdType3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), CBIOrganisationIdentification4, scope=CBIIdType3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 201, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIIdType3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 201, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIIdType3._Automaton = _BuildAutomaton_21()




CBILocalInstrument1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=CBILocalInstrument1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 206, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBILocalInstrument1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 206, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBILocalInstrument1._Automaton = _BuildAutomaton_22()




CBIOrganisationIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), CBIGenericIdentification1, scope=CBIOrganisationIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 211, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 211, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIOrganisationIdentification1._Automaton = _BuildAutomaton_23()




CBIOrganisationIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI'), AnyBICIdentifier, scope=CBIOrganisationIdentification2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 217, 4)))

CBIOrganisationIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), CBIGenericIdentification1, scope=CBIOrganisationIdentification2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 218, 4)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 217, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 218, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIOrganisationIdentification2._Automaton = _BuildAutomaton_24()




CBIOrganisationIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), CBIGenericIdentification1, scope=CBIOrganisationIdentification3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 224, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 224, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIOrganisationIdentification3._Automaton = _BuildAutomaton_25()




CBIOrganisationIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), CBIGenericIdentification2, scope=CBIOrganisationIdentification4, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 229, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 229, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIOrganisationIdentification4._Automaton = _BuildAutomaton_26()




CBIParty1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), CBIOrganisationIdentification2, scope=CBIParty1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 235, 4)))

CBIParty1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrvtId'), CBIPersonIdentification1, scope=CBIParty1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 236, 4)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIParty1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 235, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIParty1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrvtId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 236, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIParty1Choice._Automaton = _BuildAutomaton_27()




CBIPartyIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=CBIPartyIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 242, 3)))

CBIPartyIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIIdType1, scope=CBIPartyIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 243, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 242, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 242, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 243, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPartyIdentification1._Automaton = _BuildAutomaton_28()




CBIPartyIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=CBIPartyIdentification2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 248, 3)))

CBIPartyIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), CBIPostalAddress6, scope=CBIPartyIdentification2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 249, 3)))

CBIPartyIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIIdType2, scope=CBIPartyIdentification2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 250, 3)))

CBIPartyIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), CountryCode, scope=CBIPartyIdentification2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 251, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 248, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 249, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 250, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 251, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 248, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 249, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 250, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 251, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIPartyIdentification2._Automaton = _BuildAutomaton_29()




CBIPartyIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=CBIPartyIdentification3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 256, 3)))

CBIPartyIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), CBIPostalAddress6, scope=CBIPartyIdentification3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 257, 3)))

CBIPartyIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIParty1Choice, scope=CBIPartyIdentification3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 258, 3)))

CBIPartyIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), CountryCode, scope=CBIPartyIdentification3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 259, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 257, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 258, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 259, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 256, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 257, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 258, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 259, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPartyIdentification3._Automaton = _BuildAutomaton_30()




CBIPartyIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=CBIPartyIdentification4, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 264, 3)))

CBIPartyIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), CBIPostalAddress6, scope=CBIPartyIdentification4, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 265, 3)))

CBIPartyIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIIdType2, scope=CBIPartyIdentification4, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 266, 3)))

CBIPartyIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), CountryCode, scope=CBIPartyIdentification4, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 267, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 265, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 266, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 267, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 264, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 265, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 266, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 267, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPartyIdentification4._Automaton = _BuildAutomaton_31()




CBIPartyIdentification5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=CBIPartyIdentification5, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 272, 3)))

CBIPartyIdentification5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIIdType3, scope=CBIPartyIdentification5, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 273, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 273, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 272, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 273, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPartyIdentification5._Automaton = _BuildAutomaton_32()




CBIPaymentTypeInformation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstrPrty'), Priority2Code, scope=CBIPaymentTypeInformation1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 278, 3)))

CBIPaymentTypeInformation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl'), CBIServiceLevel1, scope=CBIPaymentTypeInformation1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 279, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 278, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 279, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstrPrty')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 278, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 279, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIPaymentTypeInformation1._Automaton = _BuildAutomaton_33()




CBIPaymentTypeInformation2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl'), CBIServiceLevel2, scope=CBIPaymentTypeInformation2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 284, 3)))

CBIPaymentTypeInformation2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LclInstrm'), CBILocalInstrument1, scope=CBIPaymentTypeInformation2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 285, 3)))

CBIPaymentTypeInformation2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtgyPurp'), CategoryPurpose1Choice, scope=CBIPaymentTypeInformation2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 286, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 284, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 285, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 286, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 284, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LclInstrm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 285, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtgyPurp')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 286, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIPaymentTypeInformation2._Automaton = _BuildAutomaton_34()




CBIPersonIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), CBIGenericIdentification1, scope=CBIPersonIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 291, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPersonIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 291, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPersonIdentification1._Automaton = _BuildAutomaton_35()




CBIPostalAddress6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdrTp'), AddressType2Code, scope=CBIPostalAddress6, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 296, 3)))

CBIPostalAddress6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dept'), Max70Text, scope=CBIPostalAddress6, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 297, 3)))

CBIPostalAddress6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubDept'), Max70Text, scope=CBIPostalAddress6, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 298, 3)))

CBIPostalAddress6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StrtNm'), Max70Text, scope=CBIPostalAddress6, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 299, 3)))

CBIPostalAddress6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BldgNb'), Max16Text, scope=CBIPostalAddress6, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 300, 3)))

CBIPostalAddress6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstCd'), Max16Text, scope=CBIPostalAddress6, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 301, 3)))

CBIPostalAddress6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TwnNm'), Max35Text, scope=CBIPostalAddress6, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 302, 3)))

CBIPostalAddress6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtrySubDvsn'), Max35Text, scope=CBIPostalAddress6, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 303, 3)))

CBIPostalAddress6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), CountryCode, scope=CBIPostalAddress6, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 304, 3)))

CBIPostalAddress6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdrLine'), Max70Text, scope=CBIPostalAddress6, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 305, 3)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 296, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 297, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 298, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 299, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 300, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 301, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 302, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 303, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 304, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 305, 3))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdrTp')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 296, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dept')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 297, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubDept')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 298, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StrtNm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 299, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BldgNb')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 300, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstCd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 301, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TwnNm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 302, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtrySubDvsn')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 303, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ctry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 304, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdrLine')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 305, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIPostalAddress6._Automaton = _BuildAutomaton_36()




CBIRegulatoryReporting1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DbtCdtRptgInd'), CBIRegulatoryReportingType1Code, scope=CBIRegulatoryReporting1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 310, 3)))

CBIRegulatoryReporting1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dtls'), CBIStructuredRegulatoryReporting1, scope=CBIRegulatoryReporting1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 311, 3)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 311, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIRegulatoryReporting1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DbtCdtRptgInd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 310, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIRegulatoryReporting1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dtls')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 311, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIRegulatoryReporting1._Automaton = _BuildAutomaton_37()




CBIRemittanceLocation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtId'), Max35Text, scope=CBIRemittanceLocation1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 316, 3)))

CBIRemittanceLocation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtLctnMtd'), CBIRemittanceLocationMethod1Code, scope=CBIRemittanceLocation1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 317, 3)))

CBIRemittanceLocation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtLctnElctrncAdr'), Max2048Text, scope=CBIRemittanceLocation1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 318, 3)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 316, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 317, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 318, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIRemittanceLocation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 316, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIRemittanceLocation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtLctnMtd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 317, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIRemittanceLocation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtLctnElctrncAdr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 318, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIRemittanceLocation1._Automaton = _BuildAutomaton_38()




CBIServiceLevel1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), CBIServiceLevel1Code, scope=CBIServiceLevel1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 323, 3)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIServiceLevel1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 323, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIServiceLevel1._Automaton = _BuildAutomaton_39()




CBIServiceLevel2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=CBIServiceLevel2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 328, 3)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIServiceLevel2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 328, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIServiceLevel2._Automaton = _BuildAutomaton_40()




CBIStructuredRegulatoryReporting1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), STD_ANON, scope=CBIStructuredRegulatoryReporting1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 333, 3)))

CBIStructuredRegulatoryReporting1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), ActiveOrHistoricCurrencyAndAmount, scope=CBIStructuredRegulatoryReporting1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 342, 3)))

CBIStructuredRegulatoryReporting1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Inf'), Max35Text, scope=CBIStructuredRegulatoryReporting1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 343, 3)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 342, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 343, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIStructuredRegulatoryReporting1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 333, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIStructuredRegulatoryReporting1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 342, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIStructuredRegulatoryReporting1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Inf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 343, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIStructuredRegulatoryReporting1._Automaton = _BuildAutomaton_41()




ContactDetails2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NmPrfx'), NamePrefix1Code, scope=ContactDetails2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 348, 3)))

ContactDetails2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max140Text, scope=ContactDetails2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 349, 3)))

ContactDetails2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PhneNb'), PhoneNumber, scope=ContactDetails2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 350, 3)))

ContactDetails2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MobNb'), PhoneNumber, scope=ContactDetails2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 351, 3)))

ContactDetails2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FaxNb'), PhoneNumber, scope=ContactDetails2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 352, 3)))

ContactDetails2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmailAdr'), Max2048Text, scope=ContactDetails2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 353, 3)))

ContactDetails2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), Max35Text, scope=ContactDetails2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 354, 3)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 348, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 349, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 350, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 351, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 352, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 353, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 354, 3))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContactDetails2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NmPrfx')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 348, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ContactDetails2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 349, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ContactDetails2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PhneNb')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 350, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ContactDetails2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MobNb')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 351, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ContactDetails2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FaxNb')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 352, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ContactDetails2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmailAdr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 353, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ContactDetails2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 354, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ContactDetails2._Automaton = _BuildAutomaton_42()




CreditorReferenceInformation2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), CreditorReferenceType2, scope=CreditorReferenceInformation2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 359, 3)))

CreditorReferenceInformation2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ref'), Max35Text, scope=CreditorReferenceInformation2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 360, 3)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 359, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 360, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceInformation2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 359, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceInformation2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ref')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 360, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CreditorReferenceInformation2._Automaton = _BuildAutomaton_43()




CreditorReferenceType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), DocumentType3Code, scope=CreditorReferenceType1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 366, 4)))

CreditorReferenceType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=CreditorReferenceType1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 367, 4)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 366, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 367, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CreditorReferenceType1Choice._Automaton = _BuildAutomaton_44()




CreditorReferenceType2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), CreditorReferenceType1Choice, scope=CreditorReferenceType2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 373, 3)))

CreditorReferenceType2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=CreditorReferenceType2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 374, 3)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 374, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceType2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 373, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceType2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 374, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CreditorReferenceType2._Automaton = _BuildAutomaton_45()




DateAndPlaceOfBirth._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BirthDt'), ISODate, scope=DateAndPlaceOfBirth, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 379, 3)))

DateAndPlaceOfBirth._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrvcOfBirth'), Max35Text, scope=DateAndPlaceOfBirth, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 380, 3)))

DateAndPlaceOfBirth._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CityOfBirth'), Max35Text, scope=DateAndPlaceOfBirth, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 381, 3)))

DateAndPlaceOfBirth._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfBirth'), CountryCode, scope=DateAndPlaceOfBirth, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 382, 3)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 380, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DateAndPlaceOfBirth._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BirthDt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 379, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DateAndPlaceOfBirth._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrvcOfBirth')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 380, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DateAndPlaceOfBirth._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CityOfBirth')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 381, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DateAndPlaceOfBirth._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfBirth')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 382, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DateAndPlaceOfBirth._Automaton = _BuildAutomaton_46()




DocumentAdjustment1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), ActiveOrHistoricCurrencyAndAmount, scope=DocumentAdjustment1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 387, 3)))

DocumentAdjustment1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtDbtInd'), CreditDebitCode, scope=DocumentAdjustment1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 388, 3)))

DocumentAdjustment1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rsn'), Max4Text, scope=DocumentAdjustment1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 389, 3)))

DocumentAdjustment1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddtlInf'), Max140Text, scope=DocumentAdjustment1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 390, 3)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 388, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 389, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 390, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DocumentAdjustment1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 387, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DocumentAdjustment1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtDbtInd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 388, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DocumentAdjustment1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rsn')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 389, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DocumentAdjustment1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddtlInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 390, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DocumentAdjustment1._Automaton = _BuildAutomaton_47()




GenericIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericIdentification3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 395, 3)))

GenericIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=GenericIdentification3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 396, 3)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 396, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 395, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenericIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 396, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericIdentification3._Automaton = _BuildAutomaton_48()




GenericOrganisationIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericOrganisationIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 401, 3)))

GenericOrganisationIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), OrganisationIdentificationSchemeName1Choice, scope=GenericOrganisationIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 402, 3)))

GenericOrganisationIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=GenericOrganisationIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 403, 3)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 402, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 403, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 401, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 402, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 403, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericOrganisationIdentification1._Automaton = _BuildAutomaton_49()




GenericPersonIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericPersonIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 408, 3)))

GenericPersonIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), PersonIdentificationSchemeName1Choice, scope=GenericPersonIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 409, 3)))

GenericPersonIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=GenericPersonIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 410, 3)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 409, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 410, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericPersonIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 408, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenericPersonIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 409, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GenericPersonIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 410, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericPersonIdentification1._Automaton = _BuildAutomaton_50()




OrganisationIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI'), AnyBICIdentifier, scope=OrganisationIdentification4, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 415, 3)))

OrganisationIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), GenericOrganisationIdentification1, scope=OrganisationIdentification4, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 416, 3)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 415, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 416, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 415, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 416, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OrganisationIdentification4._Automaton = _BuildAutomaton_51()




OrganisationIdentificationSchemeName1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalOrganisationIdentification1Code, scope=OrganisationIdentificationSchemeName1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 422, 4)))

OrganisationIdentificationSchemeName1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=OrganisationIdentificationSchemeName1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 423, 4)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentificationSchemeName1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 422, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentificationSchemeName1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 423, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrganisationIdentificationSchemeName1Choice._Automaton = _BuildAutomaton_52()




PartyIdentification32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max140Text, scope=PartyIdentification32, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 429, 3)))

PartyIdentification32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), CBIPostalAddress6, scope=PartyIdentification32, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 430, 3)))

PartyIdentification32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Party6Choice, scope=PartyIdentification32, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 431, 3)))

PartyIdentification32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), CountryCode, scope=PartyIdentification32, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 432, 3)))

PartyIdentification32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtctDtls'), ContactDetails2, scope=PartyIdentification32, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 433, 3)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 429, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 430, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 431, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 432, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 433, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 429, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 430, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 431, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 432, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtctDtls')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 433, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PartyIdentification32._Automaton = _BuildAutomaton_53()




Party6Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), OrganisationIdentification4, scope=Party6Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 439, 4)))

Party6Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrvtId'), PersonIdentification5, scope=Party6Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 440, 4)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Party6Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 439, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Party6Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrvtId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 440, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Party6Choice._Automaton = _BuildAutomaton_54()




PaymentIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstrId'), Max35Text, scope=PaymentIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 446, 3)))

PaymentIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndToEndId'), Max35Text, scope=PaymentIdentification1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 447, 3)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PaymentIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstrId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 446, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PaymentIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndToEndId')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 447, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PaymentIdentification1._Automaton = _BuildAutomaton_55()




PersonIdentification5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DtAndPlcOfBirth'), DateAndPlaceOfBirth, scope=PersonIdentification5, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 452, 3)))

PersonIdentification5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), GenericPersonIdentification1, scope=PersonIdentification5, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 453, 3)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 452, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 453, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PersonIdentification5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DtAndPlcOfBirth')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 452, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PersonIdentification5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 453, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PersonIdentification5._Automaton = _BuildAutomaton_56()




PersonIdentificationSchemeName1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalPersonIdentification1Code, scope=PersonIdentificationSchemeName1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 459, 4)))

PersonIdentificationSchemeName1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=PersonIdentificationSchemeName1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 460, 4)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PersonIdentificationSchemeName1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 459, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PersonIdentificationSchemeName1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 460, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PersonIdentificationSchemeName1Choice._Automaton = _BuildAutomaton_57()




Purpose1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalPurpose1Code, scope=Purpose1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 467, 4)))

Purpose1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=Purpose1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 468, 4)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Purpose1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 467, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Purpose1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 468, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Purpose1Choice._Automaton = _BuildAutomaton_58()




RemittanceInformation5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ustrd'), Max140Text, scope=RemittanceInformation5, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 474, 3)))

RemittanceInformation5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Strd'), StructuredRemittanceInformation7, scope=RemittanceInformation5, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 475, 3)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 474, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 475, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceInformation5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ustrd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 474, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceInformation5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Strd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 475, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RemittanceInformation5._Automaton = _BuildAutomaton_59()




ReferredDocumentInformation3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), ReferredDocumentType2, scope=ReferredDocumentInformation3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 480, 3)))

ReferredDocumentInformation3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nb'), Max35Text, scope=ReferredDocumentInformation3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 481, 3)))

ReferredDocumentInformation3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RltdDt'), ISODate, scope=ReferredDocumentInformation3, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 482, 3)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 480, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 481, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 482, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentInformation3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 480, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentInformation3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nb')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 481, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentInformation3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RltdDt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 482, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReferredDocumentInformation3._Automaton = _BuildAutomaton_60()




ReferredDocumentType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), DocumentType5Code, scope=ReferredDocumentType1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 488, 4)))

ReferredDocumentType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=ReferredDocumentType1Choice, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 489, 4)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 488, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 489, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferredDocumentType1Choice._Automaton = _BuildAutomaton_61()




ReferredDocumentType2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), ReferredDocumentType1Choice, scope=ReferredDocumentType2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 495, 3)))

ReferredDocumentType2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=ReferredDocumentType2, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 496, 3)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 496, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentType2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 495, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentType2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 496, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferredDocumentType2._Automaton = _BuildAutomaton_62()




RemittanceAmount1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DuePyblAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 501, 3)))

RemittanceAmount1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DscntApldAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 502, 3)))

RemittanceAmount1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtNoteAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 503, 3)))

RemittanceAmount1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 504, 3)))

RemittanceAmount1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdjstmntAmtAndRsn'), DocumentAdjustment1, scope=RemittanceAmount1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 505, 3)))

RemittanceAmount1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount1, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 506, 3)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 501, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 502, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 503, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 504, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 505, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 506, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DuePyblAmt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 501, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DscntApldAmt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 502, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtNoteAmt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 503, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 504, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdjstmntAmtAndRsn')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 505, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 506, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RemittanceAmount1._Automaton = _BuildAutomaton_63()




StructuredRemittanceInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocInf'), ReferredDocumentInformation3, scope=StructuredRemittanceInformation7, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 511, 3)))

StructuredRemittanceInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocAmt'), RemittanceAmount1, scope=StructuredRemittanceInformation7, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 512, 3)))

StructuredRemittanceInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtrRefInf'), CreditorReferenceInformation2, scope=StructuredRemittanceInformation7, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 513, 3)))

StructuredRemittanceInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Invcr'), PartyIdentification32, scope=StructuredRemittanceInformation7, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 514, 3)))

StructuredRemittanceInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Invcee'), PartyIdentification32, scope=StructuredRemittanceInformation7, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 515, 3)))

StructuredRemittanceInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddtlRmtInf'), Max140Text, scope=StructuredRemittanceInformation7, location=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 516, 3)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 511, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 512, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 513, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 514, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 515, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 516, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 511, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocAmt')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 512, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtrRefInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 513, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Invcr')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 514, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Invcee')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 515, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddtlRmtInf')), pyxb.utils.utility.Location('C:\\Users\\Federico\\Desktop\\xsd bonifici\\CBIPaymentRequest.00.04.00.xsd', 516, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StructuredRemittanceInformation7._Automaton = _BuildAutomaton_64()

