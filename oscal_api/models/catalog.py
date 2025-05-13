from pydantic import BaseModel, Field
from typing import List, Optional
from typing import Dict

class Property(BaseModel):
    name: str = Field(..., description="Property Name")
    value: str = Field(..., description="Property Value")
    uuid: Optional[str] = Field(None, description="Property Universally Unique Identifier")
    ns: Optional[str] = Field(None, description="Property Namespace")
    class_: Optional[str] = Field(None, alias="class", description="Property Class")
    group: Optional[str] = Field(None, description="Property Group")
    remarks: Optional[str] = Field(None, description="Remarks")


class Link(BaseModel):
    href: str = Field(..., description="Hypertext Reference")
    rel: Optional[str] = Field(None, description="Link Relation Type")
    media_type: Optional[str] = Field(None, description="Media Type")
    resource_fragment: Optional[str] = Field(None, description="Resource Fragment")
    text: Optional[str] = Field(None, description="Link Text")


class Part(BaseModel):
    id: Optional[str] = Field(None, description="Part Identifier")
    name: str = Field(..., description="Part Name")
    ns: Optional[str] = Field(None, description="Part Namespace")
    class_: Optional[str] = Field(None, alias="class", description="Part Class")
    title: Optional[str] = Field(None, description="Part Title")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    prose: Optional[str] = Field(None, description="Part Text")
    parts: Optional[List["Part"]] = Field(None, description="List of Child Parts")
    links: Optional[List[Link]] = Field(None, description="List of Links")


class ParameterConstraintTest(BaseModel):
    expression: str = Field(..., description="Constraint test")
    remarks: Optional[str] = Field(None, description="Remarks")


class ParameterConstraint(BaseModel):
    description: str = Field(..., description="Constraint Description")
    tests: Optional[List[ParameterConstraintTest]] = Field(None, description="List of Constraint Tests")


class ParameterGuideline(BaseModel):
    prose: str = Field(..., description="Guideline Text")


class ParameterSelection(BaseModel):
    how_many: Optional[str] = Field(None, description="Parameter Cardinality")
    choice: List[str] = Field(..., description="List of Choices")


class Parameter(BaseModel):
    id: str = Field(..., description="Parameter Identifier")
    class_: Optional[str] = Field(None, alias="class", description="Parameter Class")
    depends_on: Optional[str] = Field(None, alias="depends-on", description="Depends on")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    links: Optional[List[Link]] = Field(None, description="List of Links")
    label: Optional[str] = Field(None, description="Parameter Label")
    usage: Optional[str] = Field(None, description="Parameter Usage Description")
    constraints: Optional[List[ParameterConstraint]] = Field(None, description="List of Constraints")
    guidelines: Optional[List[ParameterGuideline]] = Field(None, description="List of Guidelines")
    values: Optional[List[str]] = Field(None, description="List of Parameter Values")
    select: Optional[ParameterSelection] = Field(None, description="Parameter Selection")
    remarks: Optional[str] = Field(None, description="Remarks")


class Control(BaseModel):
    id: str = Field(..., description="Control Identifier")
    class_: Optional[str] = Field(None, alias="class", description="Control Class")
    title: str = Field(..., description="Control Title")
    params: Optional[List[Parameter]] = Field(None, description="List of Parameters")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    links: Optional[List[Link]] = Field(None, description="List of Links")
    parts: Optional[List[Part]] = Field(None, description="List of Parts")
    controls: Optional[List["Control"]] = Field(None, description="List of Child Controls")


class Group(BaseModel):
    id: Optional[str] = Field(None, description="Group Identifier")
    class_: Optional[str] = Field(None, alias="class", description="Group Class")
    title: str = Field(..., description="Group Title")
    params: Optional[List[Parameter]] = Field(None, description="List of Parameters")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    links: Optional[List[Link]] = Field(None, description="List of Links")
    parts: Optional[List[Part]] = Field(None, description="List of Parts")
    groups: Optional[List["Group"]] = Field(None, description="List of Child Groups")
    controls: Optional[List[Control]] = Field(None, description="List of Controls")


class DocumentIdentifier(BaseModel):
    scheme: Optional[str] = Field(None, description="Document Identification Scheme")
    identifier: str = Field(..., description="Identifier")


class Role(BaseModel):
    id: str = Field(..., description="Role Identifier")
    title: str = Field(..., description="Role Title")
    short_name: Optional[str] = Field(None, description="Role Short Name")
    description: Optional[str] = Field(None, description="Role Description")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    links: Optional[List[Link]] = Field(None, description="List of Links")
    remarks: Optional[str] = Field(None, description="Remarks")


class Address(BaseModel):
    type: Optional[str] = Field(None, description="Address Type")
    addr_lines: List[str] = Field(..., alias="addr-lines", description="List of Address lines")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State")
    postal_code: Optional[str] = Field(None, alias="postal-code", description="Postal Code")
    country: Optional[str] = Field(None, description="Country Code")


class Location(BaseModel):
    uuid: str = Field(..., description="Location Universally Unique Identifier")
    title: Optional[str] = Field(None, description="Location Title")
    address: Optional[Address] = Field(None, description="Location Address")
    email_addresses: Optional[List[str]] = Field(None, alias="email-addresses", description="List of Email Addresses")
    telephone_numbers: Optional[List[Dict[str, str]]] = Field(None, alias="telephone-numbers", description="List of Telephone Numbers")
    urls: Optional[List[str]] = Field(None, description="List of URLs")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    links: Optional[List[Link]] = Field(None, description="List of Links")
    remarks: Optional[str] = Field(None, description="Remarks")


class Party(BaseModel):
    uuid: str = Field(..., description="Party Universally Unique Identifier")
    type: str = Field(..., description="Party Type")
    name: str = Field(..., description="Party Name")
    short_name: Optional[str] = Field(None, alias="short-name", description="Party Short Name")
    external_ids: Optional[List[Dict[str, str]]] = Field(None, alias="external-ids", description="List of Party External Identifiers")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    links: Optional[List[Link]] = Field(None, description="List of Links")
    email_addresses: Optional[List[str]] = Field(None, alias="email-addresses", description="List of Email Addresses")
    telephone_numbers: Optional[List[Dict[str, str]]] = Field(None, alias="telephone-numbers", description="List of Telephone Numbers")
    addresses: Optional[List[Address]] = Field(None, description="List of Addresses")
    location_uuids: Optional[List[str]] = Field(None, alias="location-uuids", description="List of Location UUIDs")
    member_of_organizations: Optional[List[str]] = Field(None, alias="member-of-organizations", description="List of Organizational Affiliations")
    remarks: Optional[str] = Field(None, description="Remarks")


class ResponsibleParty(BaseModel):
    role_id: str = Field(..., alias="role-id", description="Responsible Role")
    party_uuids: List[str] = Field(..., alias="party-uuids", description="List of Party UUIDs")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    links: Optional[List[Link]] = Field(None, description="List of Links")
    remarks: Optional[str] = Field(None, description="Remarks")


class Action(BaseModel):
    uuid: str = Field(..., description="Action Universally Unique Identifier")
    date: str = Field(..., description="Action Occurrence Date")
    type: str = Field(..., description="Action Type")
    system: str = Field(..., description="Action Type System")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    links: Optional[List[Link]] = Field(None, description="List of Links")
    responsible_parties: Optional[List[ResponsibleParty]] = Field(None, alias="responsible-parties", description="List of Responsible Parties")
    remarks: Optional[str] = Field(None, description="Remarks")


class Metadata(BaseModel):
    title: str = Field(..., description="Document Title")
    published: Optional[str] = Field(None, description="Publication Timestamp")
    last_modified: str = Field(..., alias="last-modified", description="Last Modified Timestamp")
    version: str = Field(..., description="Document Version")
    oscal_version: str = Field(..., alias="oscal-version", description="OSCAL Version")
    revisions: Optional[List[Dict]] = Field(None, description="List of Revision History Entries")
    document_ids: Optional[List[DocumentIdentifier]] = Field(None, alias="document-ids", description="List of Document Identifiers")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    links: Optional[List[Link]] = Field(None, description="List of Links")
    roles: Optional[List[Role]] = Field(None, description="List of Roles")
    locations: Optional[List[Location]] = Field(None, description="List of Locations")
    parties: Optional[List[Party]] = Field(None, description="List of Parties")
    responsible_parties: Optional[List[ResponsibleParty]] = Field(None, alias="responsible-parties", description="List of Responsible Parties")
    actions: Optional[List[Action]] = Field(None, description="List of Actions")
    remarks: Optional[str] = Field(None, description="Remarks")


class Resource(BaseModel):
    uuid: str = Field(..., description="Resource Universally Unique Identifier")
    title: Optional[str] = Field(None, description="Resource Title")
    description: Optional[str] = Field(None, description="Resource Description")
    props: Optional[List[Property]] = Field(None, description="List of Properties")
    document_ids: Optional[List[DocumentIdentifier]] = Field(None, alias="document-ids", description="List of Document Identifiers")
    citation: Optional[Dict] = Field(None, description="Citation")
    rlinks: Optional[List[Link]] = Field(None, description="List of Resource Links")
    base64: Optional[Dict] = Field(None, description="Base64 Encoding")
    remarks: Optional[str] = Field(None, description="Remarks")


class BackMatter(BaseModel):
    resources: Optional[List[Resource]] = Field(None, description="List of Resources")


class Catalog(BaseModel):
    uuid: str = Field(..., description="Catalog Universally Unique Identifier")
    metadata: Metadata
    params: Optional[List[Parameter]] = Field(None, description="List of Parameters")
    controls: Optional[List[Control]] = Field(None, description="List of Controls")
    groups: Optional[List[Group]] = Field(None, description="List of Groups")
    back_matter: Optional[BackMatter] = Field(None, alias="back-matter", description="Back Matter")


class CatalogListItem(BaseModel):
    uuid: str = Field(..., description="Catalog Universally Unique Identifier")
    metadata: Metadata
