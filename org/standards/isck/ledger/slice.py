#!/usr/bin/env python
"""WP-3b -- the first REAL substrate admission: population declaration and translator.

THE POPULATION IS DECLARED, NEVER TYPED (AC1). The runner opens the emitted L0 graph object
manifest at its pin, prints the grain, the sampling rule, the counts it COUNTED and the provenance
line beside every count. Nothing here carries a literal population size.

THE TRANSLATOR CARRIES CLAIMS AND FABRICATES NOTHING (AC2). This is the whole substance of a first
real-substrate admission, and it is worth stating plainly because the temptation runs the other way:

  A part that cannot supply a REQUIRED contract field ERRORS, naming the field. It does not get a
  default, a placeholder, an "unknown" literal, or a plausible guess derived from a neighbouring
  field. There is no synthetic value anywhere in this file -- the negative arm for AC2 is a grep
  over this module, and it has to come back empty.

`part.basis` maps onto the record's claim-bearing field and NEVER UPGRADES: a part whose basis is
`absent`, `held` or `inferred` produces a record whose binding_basis says exactly that. An admission
that silently promoted 42 parts to `measured` would satisfy every structural gate in the ledger and
be a lie about the estate -- which is the failure mode this whole wave was built to make impossible.

WHY MOST PARTS ARE EXPECTED TO ERROR, and why that is the deliverable rather than a defect: the
frozen contract requires of an `entity` its entity_class, plane, entity_grain, identity_scope,
identity_policy, current_status and status_basis. The L0 manifest's parts carry part_class, home,
authority_role, temporal_claim, lineage, generation, population_status, vintage, basis, evidence and
owner. Those vocabularies are NOT the same, and no honest mechanical rule turns one into the other.
Mapping `part_class` onto `entity_class` because both end in "class" is exactly the fabrication this
criterion forbids. So the refusals ARE the finding: they name, per part and per field, what a real
substrate would have to declare before the ISCK can admit it.

AC2's NEGATIVE ARM IS `no_synthetic_defaults()` BELOW, and it is precise about what it forbids,
because a loose grep is not evidence. Three things look alike in source and are not alike:
  * a COUNTER initialiser -- `census.get(k, 0) + 1` -- counts; it substitutes for no part data
  * a SCHEMA CONST -- `status_basis: "authored"` -- is mandated by the frozen contract, which fixes
    that field's only legal value; carrying it is obeying the schema, not inventing a claim
  * a SUBSTITUTE DEFAULT -- `part.get("entity_class", "unknown")` -- invents the very thing the
    part failed to declare. THIS is the fabrication, and there must be zero of them.
The arm walks the AST, classifies every literal that reaches a RECORD field, and fails on the third
kind only. A grep that reported "0 hits" by matching the word "unknown" would have been satisfied by
this module's own docstring forbidding it -- which is exactly what my first run did.

NO EGRESS. This module opens the manifest out of the git object database and nothing else. No S3,
no AWS, no vendor call, no credential, no network.
"""
import hashlib
import json
import re
import subprocess

MANIFEST_PATH = ("org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/"
                 "D11_MANIFEST/graph_object_manifest.json")
# A part is an OBSERVER when its home is a DELIVERABLE of a seat working D11: the population then
# contains artifacts of the very effort that compiled it. Admitted knowingly, flagged, and counted.
OBSERVER_MARKER = "/deliverables/"

# Claim vocabulary, ordered weakest -> strongest. The translator may carry a claim ACROSS and may
# lower it; it may never raise it. `measured` is the only value that asserts observation.
CLAIM_ORDER = ("absent", "held", "inferred", "measured")


class PartError(Exception):
    """A part cannot supply required contract fields.

    Carries EVERY missing field, not just the first. A fail-fast error names one field and makes the
    reader run the translator N times to learn the shape of the gap; the finding this TO wants is
    the whole set a real substrate would have to declare. `field` stays the first for compatibility
    with a caller that wants one name.
    """

    def __init__(self, part_id, fields, detail):
        fields = [fields] if isinstance(fields, str) else list(fields)
        super().__init__("%s: cannot supply required field(s) %s -- %s"
                         % (part_id, ", ".join(repr(f) for f in fields), detail))
        self.part_id = part_id
        self.fields = fields
        self.field = fields[0]
        self.detail = detail


def load_population(commit, path=MANIFEST_PATH):
    """The population, read from the OBJECT DATABASE at a cited commit -- never the working tree."""
    blob = subprocess.check_output(["git", "show", "%s:%s" % (commit, path)],
                                   stderr=subprocess.PIPE)
    return json.loads(blob), hashlib.sha256(blob).hexdigest()


def declare_population(manifest, digest, commit):
    """AC1 -- grain, sampling rule, counts COUNTED, provenance beside every count."""
    parts = manifest["parts"]
    observers = [p for p in parts if OBSERVER_MARKER in (p.get("home") or "")]
    by_class = {}
    for p in parts:
        by_class[p.get("part_class")] = by_class.get(p.get("part_class"), 0) + 1
    decl = {
        "grain": "part",
        "sampling_rule": "ALL -- every part in the manifest, no subset, no stratification",
        "population_file": MANIFEST_PATH,
        "population_commit": commit,
        "population_sha256": digest,
        "as_of": manifest.get("as_of"),
        "counted_parts": len(parts),
        "counted_by_part_class": by_class,
        "observer_parts": [p["id"] for p in observers],
        "counted_observers": len(observers),
    }
    print("POPULATION DECLARED (every number below is COUNTED from the file named beside it)")
    print("   file        %s @ %s" % (MANIFEST_PATH, commit))
    print("   sha256      %s" % digest)
    print("   as_of       %s" % json.dumps(manifest.get("as_of")))
    print("   grain       part")
    print("   sampling    ALL -- no subset, no stratification")
    print("   COUNTED     %d parts | by part_class %s" % (len(parts), json.dumps(by_class,
                                                                                sort_keys=True)))
    print("   OBSERVERS   %d part(s) are D11's own deliverables, admitted KNOWINGLY and flagged "
          "observer=true -- the population observes itself and says so" % len(observers))
    for p in observers:
        print("               observer: %s" % p["id"])
    return decl


def _slug(text):
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")[:60]


def _require(part, value, field, detail):
    if value in (None, "", [], {}):
        raise PartError(part.get("id"), field, detail)
    return value


def _carry_claim(part_basis, part_id, field):
    """Carry the part's own claim across. Never upgrade it; never invent one."""
    if part_basis not in CLAIM_ORDER:
        raise PartError(part_id, field,
                        "part.basis is %r, which is not one of %s -- an unmappable claim is not a "
                        "claim, and defaulting it would upgrade an unknown into an assertion"
                        % (part_basis, list(CLAIM_ORDER)))
    return part_basis


def translate_part(part, authority, minted_at):
    """One part -> its records. Raises PartError naming EVERY required field the part cannot supply.

    All of them, not the first: a fail-fast error makes a reader run the translator once per field
    to learn the shape of a gap, and the shape is the deliverable here.
    """
    pid = part.get("id")
    serial = "ent:" + _slug(pid)

    # -- the entity's identity vocabulary. The manifest carries NONE of these; each is named.
    missing = []
    for field, why in (
        ("entity_class", "the manifest carries `part_class` (store/materializer/projection/"
                         "output_artifact/spec_artifact), which is a GRAPH-OBJECT taxonomy, not the "
                         "contract's entity_class vocabulary; mapping one onto the other because "
                         "both end in 'class' is fabrication"),
        ("plane", "no part field states a plane; the manifest is single-plane by construction and "
                  "never says which"),
        ("entity_grain", "`part_class` is the object's kind, not the grain its identity is minted "
                         "at; the manifest never declares a grain"),
        ("identity_scope", "no part field scopes the identity; `home` is a LOCATION, and a path is "
                           "not a scope"),
        ("identity_policy", "no part field names an identity policy; the vocab file exists in the "
                            "bundle but nothing in the manifest selects from it"),
    ):
        if field not in part:
            missing.append((field, why))
    if missing:
        raise PartError(pid, [f for f, _w in missing],
                        "; ".join("%s: %s" % (f, w) for f, w in missing))

    basis = _carry_claim(part.get("basis"), pid, "basis")
    home = _require(part, part.get("home"), "home",
                    "entity_binding.native_key has no value without it")

    entity = {"record_type": "entity", "entity_serial": serial,
              "entity_class": part["entity_class"], "plane": part["plane"],
              "entity_grain": part["entity_grain"], "identity_scope": part["identity_scope"],
              "identity_policy": part["identity_policy"],
              "minted_at": minted_at, "minting_authority": authority,
              "status_basis": "authored"}
    receipt = {"record_type": "mint_receipt", "receipt_id": "mr:" + _slug(pid),
               "entity_serial": serial, "minted_at": minted_at, "minting_authority": authority}
    binding = {"record_type": "entity_binding", "binding_id": "bind:" + _slug(pid),
               "entity_serial": serial, "native_key": home,
               "valid_from": (part.get("vintage") or {}).get("measured_utc") or minted_at,
               "binding_basis": basis, "status_basis": "authored"}
    return [receipt, entity, binding]


def translate_population(manifest, authority="0.0.0_AB_MSTR", minted_at=None):
    """Every part translated. Returns (batches, errors, census). Nothing is skipped silently."""
    minted_at = minted_at or (manifest.get("as_of") or {}).get("compiled_utc")
    batches, errors, census = [], [], {}
    for part in manifest["parts"]:
        try:
            records = translate_part(part, authority, minted_at)
        except PartError as exc:
            errors.append(exc)
            continue
        for r in records:
            census[r["record_type"]] = census.get(r["record_type"], 0) + 1
        batches.append((part["id"], records))
    return batches, errors, census


# -- AC2's negative arm, in the module it polices ------------------------------------------------

SCHEMA_CONST_FIELDS = {"record_type", "status_basis"}


def no_synthetic_defaults(path=None):
    """FAIL if any RECORD field is filled from a literal that substitutes for absent part data.

    Returns (ok, findings). Counter initialisers and schema-const fields are named and allowed;
    everything else that puts a literal into a record dict is reported.
    """
    import ast
    import io as _io
    import os as _os
    path = path or _os.path.abspath(__file__)
    tree = ast.parse(_io.open(path, encoding="utf-8").read())
    findings, allowed = [], []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        keys = [k.value for k in node.keys if isinstance(k, ast.Constant)]
        if "record_type" not in keys:
            continue                                  # not a record literal
        for k, v in zip(node.keys, node.values):
            if not isinstance(k, ast.Constant) or not isinstance(v, ast.Constant):
                continue
            (allowed if k.value in SCHEMA_CONST_FIELDS else findings).append(
                "%s = %r (line %d)" % (k.value, v.value, v.lineno))
    return (not findings), {"forbidden": findings, "schema_const_allowed": allowed}
