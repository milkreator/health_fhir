from fhirclient.models.patient import Patient as P, PatientCommunication as PC
from fhirclient.models.codeableconcept import CodeableConcept as CC
from fhirclient.models.identifier import Identifier as ID
from fhirclient.models.attachment import Attachment as AT
from fhirclient.models.coding import Coding as C
from fhirclient.models.fhirreference import FHIRReference as FR
from fhirclient.models.address import Address as AD
from fhirclient.models.fhirdate import FHIRDate as FD
from fhirclient.models.contactpoint import ContactPoint as CP
from fhirclient.models.humanname import HumanName as HN
from fhirclient.models.period import Period as Per
from .common import Resource

class Patient(Resource):
    """Takes a patient adapter instance and provides valid FHIR data.

        Basically a wrapper for the adapter using the fhirclient models.

           E.g., p = Patient(adapter) --> p.fhir_json #valid FHIR json
    """

    def _import_data(self):
        patient = P()

        patient.identifier = []
        # identifier
        for ident in self.adapter.identifier:
            id_ = ID({'use': ident.use,
                    'value': ident.value,
                    'type': {'text': ident.type.text}})
            patient.identifier.append(id_)


        # active
        patient.active = self.adapter.active

        # name
        patient.name = []
        for name in self.adapter.name:
            hn = HN({'given': name.given,
                        'family': name.family,
                        'prefix': name.prefix,
                        'use': name.use})
            hn.period = Per({'start': name.period.start,
                                'end': name.period.end})
            patient.name.append(hn)

        #telecom
        patient.telecom = []
        for telecom in self.adapter.telecom:
            cp = CP({'system': telecom.system,
                        'use': telecom.use,
                        'value': telecom.value
                        })
            patient.telecom.append(cp)

        #gender
        patient.gender = self.adapter.gender

        #date of birth
        patient.birthDate = FD(self.adapter.birthDate)

        #deceased
        patient.deceasedBoolean = self.adapter.deceasedBoolean
        patient.deceasedDateTime = FD(self.adapter.deceasedDateTime)

        #address
        for address in self.adapter.address:
            ad = AD({'city': address.city,
                    'country': address.country,
                    'line': address.line,
                    'type': address.type,
                    'use': address.use,
                    'state': address.state,
                    'postalCode': address.postalCode})

        #generalPractitioner
        gps = []
        for provider in self.adapter.generalPractitioner:
            fr = FR({'display': provider.display,
                        'reference': provider.reference})
            gps.append(fr)
        patient.generalPractitioner = gps

        #communication
        pcs = []
        for lang in self.adapter.communication:
            cc = CC({'coding':
                            {'code': lang.language.coding.code,
                            'display': lang.language.coding.display,
                            'system': lang.language.coding.system
                        }})

            pc = PC({'preferred': lang.preferred,
                        'language': cc})
            pcs.append(pc)
        patient.communication = pcs

        #photo
        photos = []
        for i in self.adapter.photo:
            a = A({'data': i.data})
            photos.append(a)
        patient.photo = photos

        #marital status
        if self.adapter.maritalStatus:
            codings = [{'system': coding.system, 'code': coding.code, 'display': coding.display} \
                    for coding in self.adapter.maritalStatus.coding]
            patient.maritalStatus = CC({'coding': codings})

        self.resource = patient

__all__ = ['Patient']