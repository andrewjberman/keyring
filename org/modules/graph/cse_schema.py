#!/usr/bin/env python3
"""NFRA_CSE.P1 -- the Canonical Semantic Event contract + versioned semantic algebra (validator).

Built by DS against CTO's authoritative algebra-design v0.1 (docs/architecture/
NFRA_CSE_algebra_schema_v0.1.md, 63b3b9015) -- the shared IR of the Semantic Control Plane.
UNIFY-NOT-BUILD: the four families + the CSE contract + the validator RULES + the mapping approach
are CTO's design (S1-S6); this module is DS's executable form (the enums-as-code + the fail-closed
validator impl + the full CloudNode/CloudEdge mapping table + the parity check + the coverage-sweep
wire). Nothing here invents algebra -- extension is a governed version-bump in CTO's design.

Two gating laws (charter): LAW 1 lexical-certainty-before-inference (reject-not-coerce; untypable ->
Concept(untyped)+low, never a guess); LAW 2 explicit-promotion (full provenance to lexical evidence
so every conclusion decompresses via comp_ladder).

DRAFT for CTO arch-gate (schema-vs-his-design) -> CVO exercise-cert (AC5 fidelity + AC4 parity).
Canonical home on gate = org/modules/graph/cse_schema.py (alongside comp_ladder.py) -- staged here
in the DS lane (org/modules/graph is EXEC-lane); CTO/exec places it canonically on the gate.

Author: 0.4.0_DS_ClientPlatform~B   TO: NFRA_CSE.P1   Date: 2026-07-07
"""
from __future__ import annotations

import enum
import os
import sys
from dataclasses import dataclass, field

# AC5 -- bind the SHARED fidelity gate (comp_ladder.py in the graph module). Path-robust so this
# draft runs from the DS deliverables lane; on canonical placement it is a plain sibling import.
_GRAPH_MOD = os.path.join(os.path.dirname(__file__), "..", "..", "..", "modules", "graph")
if os.path.isdir(_GRAPH_MOD):
    sys.path.insert(0, os.path.abspath(_GRAPH_MOD))
from comp_ladder import Node as LadderNode, fidelity_check  # noqa: E402,F401


# ===========================================================================
# S1/S5  VERSIONED ALGEBRA -- 4 governed-extensible families (CTO design S1)
#   schema_version 0.1. Each family is a CLOSED enum at a version; extension = version-bump +
#   COMPUNIFY coverage-sweep. A recognizer needing an off-enum value emits Concept(untyped)+low +
#   a coverage-gap CSE -- it NEVER invents a value (LAW 1).
# ===========================================================================
SCHEMA_VERSION = "0.5"   # 0.1->0.2: FLOWS_TO EdgeKind + condition. 0.2->0.3 (CTO-ratified 2026-07-07,
# Option A): add Entity.TYPE + Entity.SYMBOL first-class. TypeDecl/symbol: were parked in CONCEPT (the
# honest-degrade target) but are lexically-CERTAIN -- the AC4 full-graph round-trip (NFRA_CSE_P2_ac4_
# fullgraph_parity.py) surfaced the CONCEPT/S3.5 collision (807 nodes + 4269 edges couldn't round-trip
# at honest conf=1.0). CONCEPT stays the PURE honest-degrade target; TypeDecl/symbol now carry a certain type.
# 0.3->0.4 (CTO-arch-gated + CVO-re-signed 2026-07-08, R4 GOV-B): +ProducerKind.PROMOTE (governed 5th-producer
# emission-contract for the promote-materializer's MATERIALIZED/DEMOTED recognizer transition; back-compat additive).
# 0.4->0.5 (CTO-arch-gated + CVO-re-signed 2026-07-18, LD-0311 downstream): +Relationship.OWNS (the governed
# CUSTODY primitive) + OWNED_BY target-typed disambiguation (custody->OWNS / containment-inverse->CONTAINS via
# map_cloudedge); freed by the D3 narrow-governs split (@d16e269bf). Additive enum-extend (back-compat: the
# validator auto-accepts via _REL_VALUES); the OWNED_BY re-map is a CSE-log materializer migration.
MIGRATION_NOTE = (
    "Add a primitive -> version-bump + COMPUNIFY coverage-sweep (which compilers must now handle "
    "it); a gap is a tracked coverage-gap, not a silent skip. Remove/rename -> version-bump + a "
    "CSE-log materializer migration. CTO-arch-gated; a recognizer never forks its own primitive."
)


class Entity(enum.Enum):
    """Nouns (typed). Org (charter) + code/infra reference-compiler vocabulary (CTO S1)."""
    # org-level
    ARTIFACT = "Artifact"
    COMPONENT = "Component"
    CONCEPT = "Concept"                # Concept(untyped) = the LAW-1 honest-degrade target
    REQUIREMENT = "Requirement"
    CONSTRAINT = "Constraint"
    DATASET = "Dataset"
    SERVICE = "Service"
    PERSON = "Person"
    ORGANIZATION = "Organization"
    POLICY = "Policy"
    # code/infra-level (concrete, first-class per CTO S1 + the S4 mapping)
    FUNCTION = "Function"
    MODULE = "Module"
    ENDPOINT = "Endpoint"
    TABLE = "Table"
    LAMBDA = "Lambda"
    S3BUCKET = "S3Bucket"
    IAMROLE = "IAMRole"
    IAMSTATEMENT = "IAMStatement"
    SCHEDULE = "Schedule"
    SECRETREF = "SecretRef"
    FIELD = "Field"
    REACTCOMPONENT = "ReactComponent"
    JSXELEMENT = "JSXElement"
    HOOK = "Hook"
    GRAPHSCOPE = "GraphScope"
    TOOL = "Tool"
    TIER = "Tier"
    TYPE = "Type"                      # 0.3: a type/interface/struct declaration (TypeDecl) -- lexically
    SYMBOL = "Symbol"                  # certain code entities, first-class (were parked in CONCEPT; see
    #                                    the SCHEMA_VERSION note). As concrete as FUNCTION/MODULE/FIELD/HOOK.


class Relationship(enum.Enum):
    """Typed edges (not inferred). Org (charter) + live CloudEdge discriminators (CTO S1)."""
    CONTAINS = "contains"
    REFERENCES = "references"
    DEPENDS_ON = "depends_on"
    PRODUCES = "produces"
    CONSUMES = "consumes"
    IMPLEMENTS = "implements"
    GOVERNS = "governs"
    DERIVES_FROM = "derives_from"
    SUPERSEDES = "supersedes"
    OWNS = "owns"                      # 0.5: the governed CUSTODY/stewardship relation -- "A holds / is-
    #                                    responsible-for B" (an actor OWNS a resource). The C-1 custody sense
    #                                    of OWNED_BY, split out of the NARROWED governs (D3/D6, LD-0311). NOT
    #                                    governance (policy/authority stays GOVERNS); NOT containment (the
    #                                    S3Key sense is CONTAINS). Abstract tier (agnostic).
    # code/infra (CloudEdge discriminators)
    CALLS = "calls"
    IMPORTS = "imports"
    READS = "reads"
    WRITES = "writes"
    RENDERS = "renders"
    FLOWS_TO = "flows_to"
    FETCHES = "fetches"
    SERVED_FROM = "served_from"
    TRIGGERS = "triggers"
    DENIED = "denied"
    ALLOWED = "allowed"
    REQUIRES = "requires"
    AUTHENTICATES = "authenticates"
    AUTHORIZES = "authorizes"


class Transformation(enum.Enum):
    """The semantic delta a CSE records -- CTO S1, closed set."""
    CREATE = "create"
    DELETE = "delete"
    MODIFY = "modify"
    SPLIT = "split"
    MERGE = "merge"
    RENAME = "rename"
    STRENGTHEN = "strengthen"
    WEAKEN = "weaken"
    RECLASSIFY = "reclassify"
    RELOCATE = "relocate"


class Qualifier(enum.Enum):
    """Orthogonal metadata keys on the qualifiers block -- CTO S1. confidence+provenance load-bearing."""
    SCOPE = "scope"
    CONFIDENCE = "confidence"
    PROVENANCE = "provenance"
    TEMPORAL_VALIDITY = "temporal_validity"
    AUTHORITY = "authority"
    VISIBILITY = "visibility"
    STABILITY = "stability"
    OWNERSHIP = "ownership"


class EdgeKind(enum.Enum):
    """GOVERNED edge-KIND discriminator (schema 0.2, CTO-ratified 2026-07-07). The closed TSGRAPH FLOWS_TO
    set -- preserves the field-grain lineage capability (passthrough/rename/recompute-guarded = the spread-
    bug the regex can't see; CTO-parity-signed 961/961). LAW 1: a recognizer emits a governed value or
    Concept(untyped)+low, NEVER an invented string -- so kind is an ENUM (off-enum REJECTS), not a free str.
    Extensible via the same version-governance (a new kind = a version-bump + coverage-sweep)."""
    PASSTHROUGH = "passthrough"
    RENAME = "rename"
    RECOMPUTE_GUARDED = "recompute_guarded"


class ProducerKind(enum.Enum):
    GIT = "git"
    AGENT = "agent"
    DEPLOY = "deploy"
    IDE = "ide"
    TICKET = "ticket"
    DOC = "doc"
    INFRA = "infra"
    API = "api"
    APPROVAL = "approval"
    GRAPH_HEAD = "graph_head"
    PROMOTE = "promote"    # 0.4 (CTO-arch-gated + CVO-re-signed 2026-07-08, R4 GOV-B): the governed 5th-producer
    #                        emission-contract -- the promote-materializer's MATERIALIZED/DEMOTED recognizer
    #                        transition. Subject = Concept(untyped)+LOW (no Entity.RECOGNIZER; the promotion's
    #                        certainty is carried by the event+verb+commission_id, not confidence). See
    #                        org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_PROMOTE_P2_GOVB_R4_promote_emission_contract.py


# confidence is a FLOAT in [0,1] (CTO contract S2: `confidence: float`). The LAW-1 untyped-honest
# rule (S3.5) requires "confidence: low" -> LOW is the band confidence <= LOW_CONFIDENCE_MAX. The
# exact threshold is a CTO reconciliation question (flagged in the RAVC); 0.34 is a documented
# default (thirds: low<=0.34 < medium <=0.67 < high).
LOW_CONFIDENCE_MAX = 0.34

_ENTITY_VALUES = frozenset(e.value for e in Entity)
_REL_VALUES = frozenset(r.value for r in Relationship)
_EDGEKIND_VALUES = frozenset(k.value for k in EdgeKind)   # schema 0.2 -- governed edge-KIND set
_VERB_VALUES = frozenset(t.value for t in Transformation)
_QUAL_VALUES = frozenset(q.value for q in Qualifier)
_PRODUCER_VALUES = frozenset(p.value for p in ProducerKind)


# ===========================================================================
# S2  THE CSE CONTRACT (CTO design S2 -- incl. the head.marker_head field, AC6)
# ===========================================================================
@dataclass
class EntityRef:
    etype: str            # an Entity value
    ref: str              # a stable node id (e.g. 's3:opal-data-bd', 'stmt:DenyCrossFirmBuckets')


@dataclass
class RelationshipDelta:
    rtype: str            # a Relationship value
    target: EntityRef
    verb: str = Transformation.CREATE.value   # create|delete|modify the edge itself
    # schema 0.2 (CTO-ratified 2026-07-07): the FLOWS_TO KIND capability. Both OPTIONAL (most edges set
    # neither). `kind` = a GOVERNED EdgeKind value (off-enum REJECTS, LAW 1); `condition` = an optional
    # captured LEXICAL guard expression (evidence-like, not a type -- it decompresses to the AST node
    # showing the recompute+guard). A kind'd edge still passes comp_ladder fidelity (decompress invariant).
    kind: str = ""        # an EdgeKind value, or "" (no kind -- e.g. compiler #1 code edges)
    condition: str = ""   # optional predicate/guard expression (lexical), or ""


@dataclass
class Provenance:
    """MANDATORY (LAW 2). CTO S2: {source, locus, parser|recognizer, evidence}. Mirrors comp_ladder
    C0 provenance so a CSE decompresses through the fidelity gate. `evidence` non-empty = required."""
    source: str
    locus: str
    recognizer: str        # parser|recognizer
    evidence: str


@dataclass
class CSE:
    """The atomic record of one recognized semantic delta. Every producer emits this exact shape."""
    event_id: str
    schema_version: str
    producer: dict          # {kind, ref}
    compiler: dict          # {id, artifact_class, version}
    transformation: dict    # {verb, subject: EntityRef, edges: [RelationshipDelta]}
    provenance: Provenance  # MANDATORY
    execution_meta: dict    # {timestamp, actor, run_id} -- harness-attached
    head: dict              # {marker_head} -- GLOBGRPH marker-HEAD at emission (AC6)
    qualifiers: dict = field(default_factory=dict)   # {scope, confidence: float, ...}


# ===========================================================================
# S4  CloudNode/CloudEdge -> algebra mapping (AC3 -- the REAL code slice, two vocabularies)
#   (a) node_type STRING discriminators (derive_runner.NODE_TYPE_LAYER, uppercase) and
#   (b) node id PREFIX scheme (CTO S4: 's3:', 'component:', 'endpoint:', 'gold:', 'field:', 'rqk:',
#       'symbol:/type:', 'stmt:', 'lambda:', 'role:'). Both reconcile INTO the same Entity set.
# ===========================================================================
# (a) node_type -> Entity (all 54 NODE_TYPE_LAYER types; concrete infra kept first-class per CTO S1)
CLOUDNODE_TYPE_TO_ENTITY: dict = {
    "LAMBDA": Entity.LAMBDA, "ECS_CLUSTER": Entity.SERVICE, "ECS_TASK_DEFINITION": Entity.SERVICE,
    "EC2_INSTANCE": Entity.SERVICE, "STATE_MACHINE": Entity.SERVICE, "API_GW": Entity.SERVICE,
    "LOAD_BALANCER": Entity.SERVICE, "CLOUDFRONT_DISTRIBUTION": Entity.SERVICE,
    "SERVICE_PRINCIPAL": Entity.SERVICE, "VPC_ENDPOINT": Entity.SERVICE, "EVENT_SOURCE": Entity.SERVICE,
    "S3_BUCKET": Entity.S3BUCKET, "DYNAMODB_TABLE": Entity.TABLE, "SQS_QUEUE": Entity.DATASET,
    "SNS_TOPIC": Entity.SERVICE, "LOG_GROUP": Entity.DATASET, "S3Key": Entity.DATASET,
    "SECRET": Entity.SECRETREF, "KMS_KEY": Entity.SECRETREF,
    "S3_BUCKET_POLICY": Entity.POLICY, "IAM_POLICY": Entity.POLICY, "IAM_ROLE": Entity.IAMROLE,
    "IAM_USER": Entity.PERSON, "INSTANCE_PROFILE": Entity.POLICY,
    "SECURITY_GROUP": Entity.CONSTRAINT, "CW_ALARM": Entity.CONSTRAINT, "EVENT_RULE": Entity.SCHEDULE,
    "API_ROUTE": Entity.ENDPOINT, "ROUTE53_RECORD": Entity.ENDPOINT,
    "Component": Entity.COMPONENT, "ReactComponent": Entity.REACTCOMPONENT, "PanelCluster": Entity.COMPONENT,
    "Module": Entity.MODULE, "Page": Entity.COMPONENT, "Hook": Entity.HOOK, "DataFetch": Entity.FUNCTION,
    "Endpoint": Entity.ENDPOINT, "ServedURL": Entity.ENDPOINT, "ReactQueryKey": Entity.DATASET,
    "Field": Entity.FIELD, "Prop": Entity.FIELD, "TypeDecl": Entity.TYPE,   # 0.3: was CONCEPT (S3.5 collision)
    "JSXElement": Entity.JSXELEMENT, "JSXRender": Entity.JSXELEMENT,
    "MS_SITE": Entity.ORGANIZATION, "MS_LIBRARY": Entity.DATASET, "MS_FOLDER": Entity.DATASET,
    "MS_FILE": Entity.ARTIFACT, "MS_USER": Entity.PERSON, "MS_GROUP": Entity.ORGANIZATION,
    "MS_DRIVE_ONEDRIVE": Entity.DATASET,
    "Pipeline": Entity.SERVICE, "PipelineScript": Entity.MODULE, "PipelineFunction": Entity.FUNCTION,
}

# (b) node id PREFIX -> Entity (CTO S4 nid-prefix scheme)
CLOUDNODE_PREFIX_TO_ENTITY: dict = {
    "s3:": Entity.S3BUCKET, "component:": Entity.REACTCOMPONENT, "endpoint:": Entity.ENDPOINT,
    "gold:": Entity.DATASET, "field:": Entity.FIELD, "rqk:": Entity.DATASET, "symbol:": Entity.SYMBOL,  # 0.3: was CONCEPT
    "type:": Entity.TYPE, "stmt:": Entity.IAMSTATEMENT, "role:": Entity.IAMROLE,   # type:->TYPE (0.3, was
    # COMPONENT -- a type: IS a Type, coherent with symbol:->SYMBOL; CTO fast-follow; masked by node_type precedence)
    "lambda:": Entity.LAMBDA, "bucket:": Entity.S3BUCKET, "hook:": Entity.HOOK, "module:": Entity.MODULE,
    "tool:": Entity.TOOL, "tier:": Entity.TIER, "scope:": Entity.GRAPHSCOPE,
}

# CloudEdge edge_type -> Relationship. TOTAL over the LIVE distinct edge_type inventory (comp-kuzu
# MATCH ()-[e:CloudEdge]->() RETURN DISTINCT e.edge_type, 2026-07-07: 52 types). The algebra
# INTENTIONALLY compresses many concrete edges into fewer governed relationships (C0->C1
# compression); this is a defensible many-to-one reconcile, not an invent. CTO AC4 condition:
# every LIVE edge_type maps -> gap-fail-closed (a new live edge_type is a coverage-gap CSE).
CLOUDEDGE_TO_RELATIONSHIP: dict = {
    # direct algebra-named edges
    "RENDERS": Relationship.RENDERS, "FLOWS_TO": Relationship.FLOWS_TO, "FETCHES": Relationship.FETCHES,
    "SERVED_FROM": Relationship.SERVED_FROM, "CONTAINS": Relationship.CONTAINS,
    "CALLS": Relationship.CALLS, "READS": Relationship.READS, "WRITES": Relationship.WRITES,
    "TRIGGERS": Relationship.TRIGGERS, "REFERENCES": Relationship.REFERENCES,
    # containment / structural
    "CONTAINS_DRILLDOWN": Relationship.CONTAINS, "CLUSTERS": Relationship.CONTAINS,
    "HAS_FIELD": Relationship.CONTAINS, "HAS_PROP": Relationship.CONTAINS, "HAS_ROUTE": Relationship.CONTAINS,
    "HAS_KEY": Relationship.CONTAINS, "DECLARES": Relationship.CONTAINS,
    # reference / typing
    "ALIAS_TO": Relationship.REFERENCES, "HAS_TYPE": Relationship.REFERENCES,
    "HAS_PROPS_TYPE": Relationship.REFERENCES, "REFERENCES_TYPE": Relationship.REFERENCES,
    "SHARES_SOURCE": Relationship.REFERENCES, "MONITORS": Relationship.REFERENCES,
    "IS_ENDPOINT": Relationship.IMPLEMENTS, "HAS_PROFILE": Relationship.REFERENCES,
    # data-flow reads/writes (concrete -> reads/writes/fetches)
    "READS_FIELD": Relationship.READS, "READS_S3": Relationship.READS, "READS_SECRET": Relationship.READS,
    "READS_URL": Relationship.FETCHES, "WRITES_S3": Relationship.WRITES, "LOGS_TO": Relationship.WRITES,
    "PROP_PASSES": Relationship.FLOWS_TO, "ROUTES_TO": Relationship.FLOWS_TO,
    "DEAD_LETTERS_TO": Relationship.FLOWS_TO, "EMITS_TO": Relationship.FLOWS_TO,
    # produce / consume / project
    "PRODUCES": Relationship.PRODUCES, "PUBLISHES_TO": Relationship.PRODUCES,
    "INSTANTIATES": Relationship.PRODUCES, "PROJECTS_TO": Relationship.PRODUCES,
    "RUNS": Relationship.PRODUCES, "CONSUMES": Relationship.CONSUMES, "SUBSCRIBES": Relationship.CONSUMES,
    "NOTIFIES": Relationship.TRIGGERS, "INVOKES": Relationship.CALLS, "ORIGIN": Relationship.SERVED_FROM,
    # governance / auth / requires
    "OWNED_BY": Relationship.OWNS, "HAS_POLICY": Relationship.GOVERNS,
    "ASSUMES": Relationship.AUTHORIZES, "CAN_ASSUME": Relationship.AUTHORIZES, "GRANTS": Relationship.AUTHORIZES,
    "ENCRYPTS_WITH": Relationship.REQUIRES, "USES_OAC": Relationship.REQUIRES,
    "USES_OAI": Relationship.REQUIRES, "USES_SG": Relationship.REQUIRES, "IN_VPC": Relationship.DEPENDS_ON,
    # implements / imports (code)
    "IMPLEMENTS": Relationship.IMPLEMENTS, "IMPORTS": Relationship.IMPORTS,
    "DEPENDS_ON": Relationship.DEPENDS_ON,
    # ms edges + code auth (retained)
    "HAS_ACCESS": Relationship.REFERENCES, "SHARED_WITH": Relationship.REFERENCES,
    "MEMBER_OF": Relationship.CONTAINS, "DENIED": Relationship.DENIED, "ALLOWED": Relationship.ALLOWED,
    "REQUIRES": Relationship.REQUIRES, "AUTHENTICATES": Relationship.AUTHENTICATES,
    "AUTHORIZES": Relationship.AUTHORIZES,
}

# LIVE inventory snapshot (comp-kuzu, 2026-07-07, kuzu_nessie_db 19917 nodes/34948 edges) -- the
# AC4 ground-truth CTO's condition binds against (verify totality vs REALITY, not a hardcoded count).
# CVO re-pulls fresh (assert_live_coverage accepts a freshly-pulled set); this is the P1 snapshot.
LIVE_NODE_TYPES_20260707 = frozenset({
    "API_GW", "API_ROUTE", "CLOUDFRONT_DISTRIBUTION", "CW_ALARM", "Component", "DYNAMODB_TABLE",
    "DataFetch", "EC2_INSTANCE", "ECS_CLUSTER", "ECS_TASK_DEFINITION", "EVENT_RULE", "EVENT_SOURCE",
    "Endpoint", "Field", "Hook", "IAM_POLICY", "IAM_ROLE", "IAM_USER", "INSTANCE_PROFILE", "JSXElement",
    "JSXRender", "KMS_KEY", "LAMBDA", "LOAD_BALANCER", "LOG_GROUP", "MS_FILE", "MS_FOLDER", "MS_LIBRARY",
    "MS_SITE", "MS_USER", "Module", "Page", "PanelCluster", "Pipeline", "PipelineFunction",
    "PipelineScript", "Prop", "ROUTE53_RECORD", "ReactComponent", "ReactQueryKey", "S3Key", "S3_BUCKET",
    "S3_BUCKET_POLICY", "SECRET", "SECURITY_GROUP", "SERVICE_PRINCIPAL", "SNS_TOPIC", "SQS_QUEUE",
    "STATE_MACHINE", "ServedURL", "TypeDecl", "VPC_ENDPOINT",
})
LIVE_EDGE_TYPES_20260707 = frozenset({
    "ALIAS_TO", "ASSUMES", "CALLS", "CAN_ASSUME", "CLUSTERS", "CONTAINS", "CONTAINS_DRILLDOWN",
    "DEAD_LETTERS_TO", "DECLARES", "EMITS_TO", "ENCRYPTS_WITH", "FETCHES", "FLOWS_TO", "GRANTS",
    "HAS_FIELD", "HAS_KEY", "HAS_POLICY", "HAS_PROFILE", "HAS_PROP", "HAS_PROPS_TYPE", "HAS_ROUTE",
    "HAS_TYPE", "INSTANTIATES", "INVOKES", "IN_VPC", "IS_ENDPOINT", "LOGS_TO", "MONITORS", "NOTIFIES",
    "ORIGIN", "OWNED_BY", "PROJECTS_TO", "PROP_PASSES", "PUBLISHES_TO", "READS", "READS_FIELD",
    "READS_S3", "READS_SECRET", "READS_URL", "REFERENCES_TYPE", "RENDERS", "ROUTES_TO", "RUNS",
    "SERVED_FROM", "SHARES_SOURCE", "SUBSCRIBES", "TRIGGERS", "USES_OAC", "USES_OAI", "USES_SG",
    "WRITES", "WRITES_S3",
})


def map_cloudnode(nid: str, node_type: str = "") -> Entity:
    """AC3: resolve a CloudNode to its algebra Entity -- node_type first, else the nid prefix.
    Returns None if neither resolves (a coverage gap -> caller fail-closes)."""
    if node_type and node_type in CLOUDNODE_TYPE_TO_ENTITY:
        return CLOUDNODE_TYPE_TO_ENTITY[node_type]
    for pfx, ent in CLOUDNODE_PREFIX_TO_ENTITY.items():
        if str(nid).startswith(pfx):
            return ent
    return None


# Live-grounded (OWNED_BY object distribution @HEAD): the two OWNED_BY object classes. Extensible via the same
# governed bump if a new object type appears (a coverage-gap, caught by owned_by_object_census, reconciled, not guessed).
_OWNED_BY_CONTAINER_TYPES: frozenset = frozenset({"S3_BUCKET"})   # containment-inverse -> CONTAINS
_OWNED_BY_ACTOR_TYPES: frozenset = frozenset({"MS_USER"})          # custody -> OWNS


def map_cloudedge(edge_type: str, dst_node_type: str = "") -> "Relationship":
    """AC3 (edge): resolve a CloudEdge to its algebra Relationship. TARGET-TYPED for the polysemous OWNED_BY
    (0.5, R3): object is a CONTAINER (S3_BUCKET) -> CONTAINS (containment-inverse, the fine->coarse rollup;
    NO new primitive); else (object is an actor, e.g. MS_USER) -> OWNS (custody). All other edges resolve by
    the flat CLOUDEDGE_TO_RELATIONSHIP map. Returns None on a coverage gap (caller fail-closes).
    THE SANCTIONED EDGE RESOLVER -- a direct CLOUDEDGE_TO_RELATIONSHIP.get('OWNED_BY') returns only the custody
    DEFAULT (it lacks the object type); container disambiguation REQUIRES this function (see Sec 5 co-migration)."""
    if edge_type == "OWNED_BY":
        if dst_node_type in _OWNED_BY_CONTAINER_TYPES:
            return Relationship.CONTAINS   # containment-inverse: the OBJECT (bucket) is the container
        return Relationship.OWNS           # custody (default; actor object -- MS_USER, 5613/5845)
    return CLOUDEDGE_TO_RELATIONSHIP.get(edge_type)


def owned_by_object_census(owned_by_object_types) -> tuple:
    """Forward denominator-guard (semctl contract): given the LIVE OWNED_BY object node_types (one re-derive),
    return (ok, unknown_object_types). An object type in neither _OWNED_BY_ACTOR_TYPES nor
    _OWNED_BY_CONTAINER_TYPES currently DEFAULTS to OWNS via map_cloudedge -- which is WRONG for a new CONTAINER.
    Surface it for a governed whitelist-bump (add to the container set, or affirm custody), NEVER silently
    default. Print the distribution on each re-derive so a new object type is seen, not absorbed."""
    known = _OWNED_BY_ACTOR_TYPES | _OWNED_BY_CONTAINER_TYPES
    unknown = sorted(set(owned_by_object_types) - known)
    return (not unknown, unknown)


# ===========================================================================
# S3  THE FAIL-CLOSED VALIDATOR (CTO S3 rules 1-6, LAW 1 enforced not documented)
# ===========================================================================
class CSEValidationError(Exception):
    """Fail-closed rejection (off-schema / provenance-less / smuggled-guess / non-decompressible)."""


def validate(cse: CSE, *, check_fidelity: bool = True) -> tuple:
    """Fail-closed CSE validator. Returns (ok, errors). Implements CTO S3 rules 1-6."""
    errors: list = []

    # S3.1 schema_version known
    if cse.schema_version != SCHEMA_VERSION:
        errors.append(f"schema_version {cse.schema_version!r} != {SCHEMA_VERSION!r} (unknown algebra version)")

    # S3.2 every verb / entity-type / relationship-type IN the enum (reject, not coerce)
    tr = cse.transformation or {}
    verb = tr.get("verb")
    if verb not in _VERB_VALUES:
        errors.append(f"transformation.verb {verb!r} off-enum (reject-not-coerce)")
    subj = tr.get("subject")
    subj_etype = subj.etype if isinstance(subj, EntityRef) else (subj or {}).get("etype")
    if subj_etype not in _ENTITY_VALUES:
        errors.append(f"transformation.subject.etype {subj_etype!r} off-enum")
    for i, edge in enumerate(tr.get("edges", []) or []):
        rtype = edge.rtype if isinstance(edge, RelationshipDelta) else (edge or {}).get("rtype")
        if rtype not in _REL_VALUES:
            errors.append(f"transformation.edges[{i}].rtype {rtype!r} off-enum")
        # schema 0.2: if a KIND is set it must be a GOVERNED EdgeKind value (off-enum REJECTS, LAW 1).
        # "" = no kind (permitted -- most edges). condition is a free lexical string (evidence-like, no check).
        ekind = edge.kind if isinstance(edge, RelationshipDelta) else (edge or {}).get("kind", "")
        if ekind and ekind not in _EDGEKIND_VALUES:
            errors.append(f"transformation.edges[{i}].kind {ekind!r} off-enum (EdgeKind is governed-closed; "
                          f"a new kind is a version-bump, never an invented string -- LAW 1)")

    # producer.kind on-enum + head.marker_head present (AC6)
    if (cse.producer or {}).get("kind") not in _PRODUCER_VALUES:
        errors.append(f"producer.kind {(cse.producer or {}).get('kind')!r} off-enum")
    if not str((cse.head or {}).get("marker_head", "") or "").strip():
        errors.append("head.marker_head MISSING -- a CSE must pin the GLOBGRPH marker-HEAD at emission (AC6)")

    # S3.3 provenance present AND evidence non-empty
    p = cse.provenance
    if p is None or not str(getattr(p, "evidence", "") or "").strip():
        errors.append("provenance.evidence MISSING/blank -- provenance-less CSE INVALID (LAW 2, fail-closed)")
    if p is not None:
        for fld in ("source", "locus", "recognizer"):
            if not str(getattr(p, fld, "") or "").strip():
                errors.append(f"provenance.{fld} MISSING (full lexical chain required)")

    # S3.4 qualifiers.confidence present + a float in [0,1]
    quals = cse.qualifiers or {}
    for k in quals:
        if k not in _QUAL_VALUES:
            errors.append(f"qualifier key {k!r} off-schema")
    conf = quals.get(Qualifier.CONFIDENCE.value)
    conf_ok = isinstance(conf, (int, float)) and not isinstance(conf, bool) and 0.0 <= float(conf) <= 1.0
    if conf is None:
        errors.append("qualifiers.confidence MISSING (mandatory, CTO S3.4)")
    elif not conf_ok:
        errors.append(f"qualifiers.confidence {conf!r} not a float in [0,1]")

    # S3.5 untypable -> honest-low, never a guess: Concept subject requires confidence in the low band
    if subj_etype == Entity.CONCEPT.value:
        if not (conf_ok and float(conf) <= LOW_CONFIDENCE_MAX):
            errors.append(f"subject.etype=Concept(untyped) requires confidence<={LOW_CONFIDENCE_MAX} "
                          f"(honest-low degrade); an inferred type on a low subject is the GraphRAG "
                          f"failure this validator blocks (LAW 1)")

    # S3.6 fidelity: the CSE must decompress to C0 lexical evidence (comp_ladder), else invalid
    if check_fidelity and (p is not None and str(getattr(p, "evidence", "") or "").strip()):
        fok, ffail = fidelity_check(to_ladder_node(cse))
        if not fok:
            errors.append("fidelity FAIL (non-decompressible / latent): " + "; ".join(ffail))

    return (len(errors) == 0, errors)


def validate_or_raise(cse: CSE) -> None:
    ok, errors = validate(cse)
    if not ok:
        raise CSEValidationError("; ".join(errors))


# ===========================================================================
# AC5  FIDELITY BINDING -- a CSE -> comp_ladder C0 node (decompresses to lexical evidence)
# ===========================================================================
def to_ladder_node(cse: CSE) -> LadderNode:
    p = cse.provenance
    tr = cse.transformation or {}
    subj = tr.get("subject")
    subj_ref = subj.ref if isinstance(subj, EntityRef) else (subj or {}).get("ref", "")
    return LadderNode(
        nid=f"cse:{cse.event_id}", layer="C0", ntype=f"CSE.{tr.get('verb', '?')}",
        label=f"{tr.get('verb', '?')}({subj_ref})",
        provenance={"source": p.source, "locus": p.locus, "evidence": f"[{p.recognizer}] {p.evidence}"},
    )


def cse_fidelity_ok(cse: CSE) -> tuple:
    return fidelity_check(to_ladder_node(cse))


# ===========================================================================
# S5  COMPUNIFY COVERAGE-SWEEP WIRE (AC1) + AC4 PARITY CHECK (scaffold)
# ===========================================================================
def coverage_sweep(observed_node_types: set, observed_edge_types: set) -> tuple:
    """AC1/AC3 coverage: every observed CloudNode/CloudEdge type must reconcile into the algebra
    (fail-closed, mirrors derive_runner NODE_TYPE_LAYER_GAP + reuses COMPUNIFY's one-home coverage
    discipline). Returns (ok, unmapped_node_types, unmapped_edge_types). A gap is a tracked
    coverage-gap CSE candidate (S5), never a silent skip.

    NOTE (RAVC): the live COMPUNIFY coverage-check wire (invoke its machine-checked instrument
    rather than this local set-diff) is the AC1 antecedent -- flagged as the one external wire to
    confirm with CTO/COMPUNIFY owner; this local check is the deterministic fallback.
    """
    un_n = sorted(t for t in observed_node_types if t not in CLOUDNODE_TYPE_TO_ENTITY)
    un_e = sorted(t for t in observed_edge_types if t not in CLOUDEDGE_TO_RELATIONSHIP)
    return (not un_n and not un_e, un_n, un_e)


def assert_live_coverage(live_node_types: set = None, live_edge_types: set = None) -> tuple:
    """AC4 (CTO condition): mapping-totality against the ACTUAL LIVE distinct type inventory (not a
    hardcoded count). Pass freshly-pulled live sets (comp-kuzu DISTINCT node_type/edge_type) or use
    the 2026-07-07 snapshot. Returns (ok, unmapped_node_types, unmapped_edge_types). Fail-closed: a
    live type with no algebra mapping is an AC4 FAIL (a real coverage gap), never silent.

    CVO re-exercise: pull fresh -> comp-kuzu "MATCH (n:CloudNode) RETURN DISTINCT n.node_type" +
    "MATCH ()-[e:CloudEdge]->() RETURN DISTINCT e.edge_type" -> pass here -> assert ok.
    """
    ln = set(live_node_types) if live_node_types is not None else set(LIVE_NODE_TYPES_20260707)
    le = set(live_edge_types) if live_edge_types is not None else set(LIVE_EDGE_TYPES_20260707)
    un_n = sorted(t for t in ln if t not in CLOUDNODE_TYPE_TO_ENTITY)
    un_e = sorted(t for t in le if t not in CLOUDEDGE_TO_RELATIONSHIP)
    return (not un_n and not un_e, un_n, un_e)


def confidence_band(conf) -> str:
    """CTO guidance semantic (non-blocking): in a DETERMINISTIC substrate a TYPED node should be
    HIGH (lexical-certain ~1.0; enrichment-derived ~0.8-0.9). low<=0.34 | mid 0.34-0.67 | high>0.67.
    A TYPED node in the MID band is a soft-inference smell (LAW 1 discourages it) -- allowed in P1
    but the coverage-sweep TRACKS recognizers producing many mid-band typed nodes (a future
    recognizer-honesty signal). Returns 'low'|'mid'|'high'|'invalid'."""
    if not (isinstance(conf, (int, float)) and not isinstance(conf, bool) and 0.0 <= float(conf) <= 1.0):
        return "invalid"
    c = float(conf)
    return "low" if c <= LOW_CONFIDENCE_MAX else ("mid" if c <= 0.67 else "high")


def inference_smell(cse: CSE) -> bool:
    """CTO guidance: a TYPED (non-Concept) subject in the MID confidence band = a soft-inference
    smell (the recognizer is inferring, not lexically matching). Non-blocking; a tracked signal."""
    tr = cse.transformation or {}
    subj = tr.get("subject")
    et = subj.etype if isinstance(subj, EntityRef) else (subj or {}).get("etype")
    conf = (cse.qualifiers or {}).get(Qualifier.CONFIDENCE.value)
    return et != Entity.CONCEPT.value and confidence_band(conf) == "mid"


def parity_check(cloudnodes: list, cloudedges: list) -> tuple:
    """AC4 parity SCAFFOLD: re-materializing the mapped code CSEs must reproduce the current
    CloudNode/CloudEdge graph. Given the live graph's (nid, node_type) + (src, etype, dst) lists,
    map each into the algebra and assert every node/edge reconciles (round-trip coverage). Returns
    (ok, node_gaps, edge_gaps).

    NOTE (RAVC): full AC4 parity = re-materialize mapped CSEs and structurally diff vs the live
    Kuzu graph -- needs a graph EXPORT (consult DS~A/0.8.0 per the TO consult-path). This scaffold
    proves the MAPPING is total over a provided node/edge slice (the necessary precondition);
    the structural round-trip diff is the P2 materializer's cert (CVO AC4 exercise).
    """
    node_gaps = [(nid, nt) for (nid, nt) in cloudnodes if map_cloudnode(nid, nt) is None]
    edge_gaps = [(s, et, d) for (s, et, d) in cloudedges if et not in CLOUDEDGE_TO_RELATIONSHIP]
    return (not node_gaps and not edge_gaps, node_gaps, edge_gaps)


# ===========================================================================
# S6  STORE INTERFACE (AC2/AC6 -- folded from 0.5.0_AE consult 28cf707f9)
# ===========================================================================
CSE_TABLE = "cse"
PARTITION_COLUMNS = ("source", "event_date")   # source=producer.kind, event_date=execution ts date
ONE_MARKER_COMMIT = True     # append CSE + materialize C1 in ONE Nessie commit -> C0/C1 one-marker
FIRM_SCOPE_VIA = Qualifier.SCOPE.value          # firm-scoping is a row qualifier, never bucket-routing
CONTRACT_ID = f"nfra_cse@{SCHEMA_VERSION}"       # register into the existing graph_contracts registry
RETENTION_NOTE = "append-only C0 provenance stream -- retention DECISION open (>13mo SOC2 default?), RAVC CTO"
COMPACTION_ENROLL = "join the 02:00Z Iceberg maintenance (AE constraint #4) -- P2 writer, not write-and-forget"


def partition_key(cse: CSE) -> dict:
    ts = str((cse.execution_meta or {}).get("timestamp", ""))
    return {"source": (cse.producer or {}).get("kind", ""), "event_date": ts[:10]}


# ===========================================================================
# RUNNABLE SELF-TEST (CTO condition a -- re-runnable so CVO can re-exercise the fail-closed gate).
#   `python NFRA_CSE_P1_cse_schema.py`  runs + PRINTS every assertion; exit 0 iff all PASS.
#   `... --live`  ALSO pulls the live distinct type inventory via comp-kuzu for AC4 (else snapshot).
# ===========================================================================
def _mk_cse(prov=True, etype=Entity.REQUIREMENT.value, conf=0.9,
            verb=Transformation.STRENGTHEN.value, head=True):
    return CSE(
        "e1", SCHEMA_VERSION, {"kind": ProducerKind.GIT.value, "ref": "abc123"},
        {"id": "code#1", "artifact_class": "python", "version": "1.0"},
        {"verb": verb, "subject": EntityRef(etype, "CLAUDE.md:rule-22"),
         "edges": [RelationshipDelta(Relationship.GOVERNS.value, EntityRef(Entity.POLICY.value, "gate"))]},
        Provenance("CLAUDE.md", "L42", "rule_recognizer", "Rule 22 grounding") if prov
        else Provenance("", "", "", ""),
        {"timestamp": "2026-07-07T10:00Z", "actor": "ci", "run_id": "r1"},
        {"marker_head": "abc123def"} if head else {},
        {Qualifier.CONFIDENCE.value: conf},
    )


def _self_test(live_nodes=None, live_edges=None) -> bool:
    results = []

    def check(name, cond, detail=""):
        results.append(cond)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  -> {detail}" if (detail and not cond) else ""))

    print("=== NFRA_CSE.P1 self-test (fail-closed validator + AC3/AC4/AC5) ===")
    ok, e = validate(_mk_cse())
    check("1  valid CSE accepted", ok, str(e))
    ok, e = validate(_mk_cse(prov=False))
    check("2  provenance-less REJECTED (LAW 2)", not ok)
    ok, e = validate(_mk_cse(verb="frobnicate"))
    check("3  off-enum verb REJECTED (reject-not-coerce)", not ok)
    ok, e = validate(_mk_cse(head=False))
    check("4  missing head.marker_head REJECTED (AC6)", not ok)
    ok, e = validate(_mk_cse(etype=Entity.CONCEPT.value, conf=0.2))
    check("5  Concept(untyped)+low(0.2) ACCEPTED (honest degrade)", ok, str(e))
    ok, e = validate(_mk_cse(etype=Entity.CONCEPT.value, conf=0.9))
    check("6  Concept+high(0.9) REJECTED (smuggled guess, LAW 1)", not ok)
    ok, e = validate(_mk_cse(conf="high"))
    check("7  non-float confidence REJECTED", not ok)
    fok, ff = cse_fidelity_ok(_mk_cse())
    check("8  fidelity PASS (decompresses to C0 evidence, AC5)", fok, str(ff))
    # AC4 -- mapping totality vs the LIVE distinct type inventory (fresh if --live, else snapshot)
    cok, un, ue = assert_live_coverage(live_nodes, live_edges)
    src = "LIVE-pulled" if live_nodes is not None else "2026-07-07 snapshot"
    check(f"9  AC4 node_type totality vs {src} ({len(live_nodes or LIVE_NODE_TYPES_20260707)} types)",
          not un, f"unmapped: {un}")
    check(f"10 AC4 edge_type totality vs {src} ({len(live_edges or LIVE_EDGE_TYPES_20260707)} types)",
          not ue, f"unmapped: {ue}")
    # schema 0.2 -- the FLOWS_TO edge KIND (governed EdgeKind enum + optional condition)
    def _mk_kinded(kind):
        c = _mk_cse()
        c.transformation["edges"] = [RelationshipDelta(Relationship.FLOWS_TO.value,
                                     EntityRef(Entity.FIELD.value, "field:x"), kind=kind,
                                     condition="if guarded")]
        return c
    ok, e = validate(_mk_kinded(EdgeKind.RECOMPUTE_GUARDED.value))
    check("11 governed edge-kind (RECOMPUTE_GUARDED) ACCEPTED + decompresses (0.2)", ok, str(e))
    ok, e = validate(_mk_kinded("smuggled_kind"))
    check("12 off-enum edge-kind REJECTED (governed-closed, LAW 1)", not ok)
    # OWNS bump (0.5)
    check("OWNS on-enum (validator auto-accepts)", "owns" in _REL_VALUES)
    check("R2: OWNED_BY flat default re-mapped OUT of GOVERNS onto OWNS",
          CLOUDEDGE_TO_RELATIONSHIP["OWNED_BY"] is Relationship.OWNS)
    check("R2: HAS_POLICY stays GOVERNS (governance stays narrow, not swept into OWNS)",
          CLOUDEDGE_TO_RELATIONSHIP["HAS_POLICY"] is Relationship.GOVERNS)
    check("R3: OWNED_BY -> MS_USER (actor) resolves OWNS (custody)",
          map_cloudedge("OWNED_BY", "MS_USER") is Relationship.OWNS)
    check("R3: OWNED_BY -> S3_BUCKET (container) resolves CONTAINS (containment-inverse, no new primitive)",
          map_cloudedge("OWNED_BY", "S3_BUCKET") is Relationship.CONTAINS)
    check("R3: OWNED_BY with no object type falls back to the custody DEFAULT (OWNS)",
          map_cloudedge("OWNED_BY", "") is Relationship.OWNS)
    check("R3: a non-polysemous edge still resolves by the flat map",
          map_cloudedge("HAS_POLICY", "") is Relationship.GOVERNS)
    check("R4: OWNERSHIP Qualifier + OWNS Relationship COEXIST (AUTHORITY:AUTHORIZES precedent)",
          "ownership" in _QUAL_VALUES and "owns" in _REL_VALUES
          and "authority" in _QUAL_VALUES and "authorizes" in _REL_VALUES)
    # forward denominator-guard (Sec 4a)
    check("4a: census FLAGS an unknown OWNED_BY object type (not silently defaulted to OWNS)",
          owned_by_object_census({"MS_USER", "S3_BUCKET", "SOME_NEW_CONTAINER"}) == (False, ["SOME_NEW_CONTAINER"]))
    check("4a: census PASSES the known object set (MS_USER actor + S3_BUCKET container)",
          owned_by_object_census({"MS_USER", "S3_BUCKET"}) == (True, []))
    # CTO guidance: mid-band typed = inference smell (non-blocking, just report)
    smell = inference_smell(_mk_cse(conf=0.5))
    print(f"  [INFO] inference-smell tracker: typed+mid-band(0.5) flagged = {smell} (LAW-1 honesty signal)")
    total = len(results)
    passed = sum(1 for r in results if r)
    print(f"=== {passed}/{total} PASS ===")
    return passed == total


class LivePullError(Exception):
    """A --live inventory pull FAILED. Raised LOUD (CVO hygiene finding): --live must mean 'pull
    live or FAIL', never a silent snapshot fallback -- the honest-missing-never-silent-default
    invariant applied to the validator's own live-check (else a future live-drift goes uncaught)."""


def _pull_live_types():
    """Pull the live distinct node_type/edge_type via comp-kuzu --json (AC4 --live mode). Uses the
    structured --json output + a JSON parse (NOT a fragile stdout heuristic). FAILS LOUD on any
    error (LivePullError) rather than silently returning the snapshot -- so `--live` is honest: it
    verifies against the LIVE graph or it errors, it never quietly degrades to the embedded set."""
    import json
    import subprocess

    # Resolve the workspace root (walk up for .tools/comp-kuzu) so the wrapper is invokable
    # regardless of CWD. comp-kuzu is a bash wrapper (.tools/comp-kuzu) around kuzu_cli.py; invoke
    # it via bash (resolves its venv/env) -- more reliable than spawning the bare PATH name on
    # Windows. Falls back to kuzu_cli.py via the current interpreter if the wrapper path is absent.
    _ws = os.path.abspath(os.path.dirname(__file__))
    for _ in range(8):
        if os.path.isfile(os.path.join(_ws, ".tools", "comp-kuzu")):
            break
        _ws = os.path.dirname(_ws)
    _wrapper = os.path.join(_ws, ".tools", "comp-kuzu")
    _cli = os.path.join(_ws, "infra", "aws", "globgrph", "kuzu_cli.py")

    def _q(cypher):
        cmds = []
        if os.path.isfile(_wrapper):
            cmds.append(["bash", _wrapper, "--json", cypher])
        if os.path.isfile(_cli):
            cmds.append([sys.executable, _cli, "--json", cypher])
        out = None
        last = None
        for cmd in cmds:
            try:
                out = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
                if out.stdout.find("[") >= 0:
                    break
            except Exception as ex:
                last = ex
        if out is None:
            raise LivePullError(f"comp-kuzu invocation failed (no wrapper/cli found or spawnable): {last}")
        # --json prints a provenance preamble then a JSON array; slice from the first '['.
        s = out.stdout
        i = s.find("[")
        if i < 0:
            raise LivePullError(f"comp-kuzu --json returned no JSON array (rc={out.returncode}); "
                                f"stderr={out.stderr[:200]!r}")
        try:
            rows = json.loads(s[i:])
        except Exception as ex:
            raise LivePullError(f"comp-kuzu --json parse failed: {ex}")
        vals = {str(r["t"]) for r in rows if isinstance(r, dict) and r.get("t")}
        if not vals:
            raise LivePullError("comp-kuzu --json returned 0 distinct types (empty live inventory) "
                                "-- refusing a silent snapshot fallback")
        return vals

    n = _q("MATCH (n:CloudNode) RETURN DISTINCT n.node_type AS t ORDER BY t")
    e = _q("MATCH ()-[x:CloudEdge]->() RETURN DISTINCT x.edge_type AS t ORDER BY t")
    return n, e


if __name__ == "__main__":
    if "--live" in sys.argv:
        try:
            _ln, _le = _pull_live_types()
            print(f"[--live] pulled {len(_ln)} node_types + {len(_le)} edge_types from the live graph")
        except LivePullError as _ex:
            print(f"ERROR: --live inventory pull FAILED (no silent snapshot fallback): {_ex}")
            sys.exit(2)
    else:
        _ln, _le = (None, None)
    sys.exit(0 if _self_test(_ln, _le) else 1)
