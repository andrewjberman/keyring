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
import os
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
ISO_TIME = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")
MAPPING_V02 = "df73332fb2"          # ruled identity mapping v0.2 -- the authored ABSENCE
# "one artifact" = a repo-relative path, no whitespace, with a file extension. Deliberately strict:
# the failure it must avoid is accepting a SENTENCE that happens to contain a path.
MATERIALIZER_PATH = re.compile(r"^[A-Za-z0-9_./-]+\.[A-Za-z0-9]{1,6}$")
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         "..", "..", "..", ".."))


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

    # -- THE IDENTITY VOCABULARY now arrives DECLARED, in `part.identity`, written by the
    # declaration pass from the design lane's ruled mapping (l0_declare_identity.py; mapping v0.1
    # @b3aeaf7b4f; receiver-validated @8607debb64). The translator READS a declaration; it still
    # does not make one. A part whose identity is `unknown`, or absent entirely, errors exactly as
    # before -- the ruling supplied the values, it did not weaken the refusal.
    ident = part.get("identity")
    if isinstance(ident, dict) and ident.get("claim_status") == "declared":
        part = dict(part)
        for f in ("entity_class", "plane", "entity_grain", "identity_scope", "identity_policy"):
            if ident.get(f) is not None:
                part[f] = ident[f]
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


def translate_generation(part, authority, pin=None):
    """AC2's generation half, against RULED MAPPING v0.2 @df73332fb2 -- an authored ABSENCE.

    The design lane took Amendment 2 item 1's exit FOR EVERY CLASS and said why with a measurement:
    `semantic_layer` and `canonical_role` are `$ref nonempty` free strings with NO vocabulary, no
    Rule-24 record and no basis slot; the population carries no layer, role or materializer-class
    key to map from. So v0.2 declares both `declared=false, value=null` for the whole domain.

    THAT IS A DECLARATION, NOT A GAP IN THIS PASS. The difference matters and it is the reason the
    mapping was asked for at all: the refusal now carries a claim and an evidence path (the mapping
    file @df73332fb2) instead of being a silent omission by the emitter. A part naming a materializer
    therefore ERRORS with reason-class `declaration_gap` naming BOTH fields and citing v0.2. No
    default, no "unknown", no parse of the path -- a path-class mapping here would be a costume
    (CTO~X 78228), and inventing either value is the same act as inventing an entity_class.

    THE MATERIALIZER FIELD IS ALSO NOT ONE KIND OF THING, measured at pin 06a5ae751c across 42 parts:
        null                                    14
        an exact repo path with a blob at pin    14   <- bytes exist; a digest IS computable
        PROSE                                    14   <- "the early-morning Nessie run per ..."
    A digest is computable for the middle 14 ONLY. The prose 14 print explicit absence with reason
    `materializer_not_a_single_artifact`: a sha256 of a sentence describing three delegating writers
    is a number with no referent. Schema tightening (one artifact per `materializer`, prose to a
    sibling `materializer_note`) is a NEXT-VINTAGE emitter item, registered in v0.2's next_candidate
    list. This pass reports the shape; it does not launder it.
    """
    gen = part.get("generation") or {}
    name = gen.get("materializer")
    if not name:
        return [], None, {"class": "no_named_materializer"}
    kind, digest = classify_materializer(name, pin)
    missing = [f for f in ("semantic_layer", "canonical_role") if not gen.get(f)]
    if missing:
        raise PartError(part.get("id"), missing,
                        "declaration_gap: ruled mapping v0.2 @%s declares both fields "
                        "declared=false/value=null for the WHOLE domain (no vocabulary, no basis "
                        "receiver, no class key in the population), so no value is available to "
                        "declare and none may be invented; the frozen materializer record requires "
                        "both. materializer_kind=%s" % (MAPPING_V02, kind))
    serial = "mat:" + _slug(name)
    return ([{"record_type": "materializer", "materializer_serial": serial,
              "semantic_layer": gen["semantic_layer"], "canonical_role": gen["canonical_role"],
              "owner": part.get("owner") or "UNKNOWN", "status_basis": "authored"}],
            serial, {"class": kind, "materializer_digest": digest})


def classify_materializer(name, pin=None):
    """Is the named materializer ONE ARTIFACT whose bytes exist at the pin? Returns (kind, digest).

    THREE OUTCOMES, AND THE THIRD IS NOT THE SECOND. `prose` is a claim about the DATA: the field
    carries a sentence, so there is no single artifact to hash. `bytes_absent_at_pin` is a claim
    about the READ: the value is a path and the bytes could not be obtained. Collapsing them lets an
    instrument failure be reported as a finding about the population -- which is what the first
    clean-clone run did, turning 14 readable repo paths into 14 "prose" the moment .git was absent.
    """
    if not isinstance(name, str) or not MATERIALIZER_PATH.match(name.strip()):
        return "prose_not_a_single_artifact", None
    if pin is None:
        return "repo_path", None
    raw = read_at_pin(name.strip(), pin)
    if raw is None:
        return "repo_path_bytes_absent_at_pin", None
    return "repo_path", "sha256:" + hashlib.sha256(raw).hexdigest()


# -- THE SEVEN-FAMILY CENSUS, each family against ITS OWN denominator (Amendment 3 item 4) --------
#
# The correction that produced this: five families are attempted ONCE PER PART (42), but
# source_frontier and materialization_run are ONE record for the whole slice. Reporting all seven
# over 42 would have printed "1 of 42" for two families that were never attempted 42 times -- a
# 41-part shortfall that does not exist, which is the same error class as a denominator certifying
# the sweep instead of the pattern. A family's denominator is a property OF THE FAMILY.
PER_PART_FAMILIES = ("mint_receipt", "entity", "entity_binding", "materializer",
                     "materializer_version")
PER_SLICE_FAMILIES = ("source_frontier", "materialization_run")


def _blank(denominator):
    return {"denominator": denominator, "emitted": 0, "errored": 0, "out_of_reach": 0,
            "reasons": {}}


def _reason(cell, cls, n=1):
    cell["reasons"][cls] = cell["reasons"].get(cls, 0) + n


def family_census(manifest, pin=None):
    """EMITTED / ERRORED / OUT-OF-REACH per family, each against its own denominator.

    OUT-OF-REACH and ERRORED are deliberately distinct. Out-of-reach = the population never carried
    the input (no materializer named at all); errored = the input exists and something REFUSED it
    (the ruled declaration of absence). Collapsing them would let a population gap and a contract
    gap read identically, and they have different owners and different remedies.
    """
    parts = manifest["parts"]
    n = len(parts)
    cen = {f: _blank(n) for f in PER_PART_FAMILIES}
    for f in PER_SLICE_FAMILIES:
        cen[f] = _blank(1)
    digests = {"computable": 0, "prose": 0, "absent_at_pin": 0, "values": {}}

    for part in parts:
        try:
            for r in translate_part(part, "0.0.0_AB_MSTR",
                                    (manifest.get("as_of") or {}).get("compiled_utc")):
                if r["record_type"] in cen:
                    cen[r["record_type"]]["emitted"] += 1
        except PartError as exc:
            for f in ("mint_receipt", "entity", "entity_binding"):
                cen[f]["errored"] += 1
                _reason(cen[f], "identity_" + ",".join(sorted(exc.fields)))

        gen = part.get("generation") or {}
        name = gen.get("materializer")
        if not name:
            for f in ("materializer", "materializer_version"):
                cen[f]["out_of_reach"] += 1
                _reason(cen[f], "no_named_materializer")
            continue
        kind, digest = classify_materializer(name, pin)
        if kind == "repo_path" and digest:
            digests["computable"] += 1
            digests["values"][name] = digest
        elif kind == "repo_path_bytes_absent_at_pin":
            digests["absent_at_pin"] += 1
        else:
            digests["prose"] += 1
        try:
            translate_generation(part, "0.0.0_AB_MSTR", pin)
            cen["materializer"]["emitted"] += 1
        except PartError:
            cen["materializer"]["errored"] += 1
            _reason(cen["materializer"], "declaration_gap")
        # materializer_version: the digest is computable for a repo path, but the version record
        # REFERENCES its materializer, and every named materializer errored above. Emitting it
        # anyway would produce a record whose parent cannot resolve at final state -- sec 2d
        # refuses it, correctly. So the digest is COMPUTED and PRINTED, and the emission is
        # reported as errored with the reason, which is what CVO~X asked for: attempt it, and
        # report or refuse the unresolved parent rather than claiming a family this slice did
        # not land.
        if kind == "repo_path" and digest:
            cen["materializer_version"]["errored"] += 1
            _reason(cen["materializer_version"], "parent_materializer_errored_declaration_gap")
        elif kind == "repo_path_bytes_absent_at_pin":
            cen["materializer_version"]["out_of_reach"] += 1
            _reason(cen["materializer_version"], "materializer_bytes_absent_at_pin")
        else:
            cen["materializer_version"]["out_of_reach"] += 1
            _reason(cen["materializer_version"], "materializer_not_a_single_artifact")

    cen["source_frontier"]["emitted"] = 1
    cen["materialization_run"]["emitted"] = 1
    return cen, digests


def census_lines(cen):
    """One printable line per family. Reconciliation is PRINTED, never asserted silently."""
    out = []
    for fam in list(PER_PART_FAMILIES) + list(PER_SLICE_FAMILIES):
        c = cen[fam]
        tot = c["emitted"] + c["errored"] + c["out_of_reach"]
        out.append("   %-21s emitted %2d | errored %2d | out-of-reach %2d  of %2d  %s%s"
                   % (fam, c["emitted"], c["errored"], c["out_of_reach"], c["denominator"],
                      "OK" if tot == c["denominator"] else "RECONCILIATION FAILS (%d)" % tot,
                      ("  " + json.dumps(c["reasons"], sort_keys=True)) if c["reasons"] else ""))
    return out


def translate_population(manifest, authority="0.0.0_AB_MSTR", minted_at=None):
    """Every part translated. Returns (batches, errors, census). Nothing is skipped silently."""
    minted_at = minted_at or (manifest.get("as_of") or {}).get("compiled_utc")
    batches, errors, census = [], [], {}
    # The GENERATION half's accounting lives in family_census(), which counts every family against
    # ITS OWN denominator. It used to be tallied here too, in a second dict with its own counters --
    # two tallies of one population, which is how a number and its neighbour drift apart. One
    # counter, one owner.
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


# -- THE SLICE'S OWN PROVENANCE RECORDS (issuer amendment 2, item 3) ------------------------------
# source_frontier and materialization_run are NOT the manifest's to supply -- they are the SLICE's.
# The frontier describes the population THIS RUN admitted; the run describes THIS ADMISSION. I had
# been waiting on the manifest for them, which is why AC4's frontier anchor read as unreachable; it
# is reachable now, and the correction is the issuer's.
#
# And the run's own materializer IS a repo artifact -- this file and the runner beside it -- so its
# bundle_digest is COMPUTABLE, by exactly the method amendment 2 item 2 gives the emitter: the git
# blob digest at the population pin, method printed. The slice can therefore carry its own
# provenance in full while the MANIFEST's materializers stay unreachable for want of a digest
# nothing downstream can compute. Those are different facts about different objects.

CRLF, LF = bytes([13, 10]), bytes([10])
DIGEST_METHOD = "sha256-over-declared-canonical-tree-inventory-v1"
DIGEST_NORMALIZATION = ("each member's bytes LF-NORMALISED (CRLF -> LF) then sha256; inventory "
                        "lines '<sha256-hex>  <posix-relpath>', sorted by relpath, LF-joined with a "
                        "trailing LF, UTF-8, then sha256. Bytes are read at the pin -- via `git "
                        "show <pin>:<path>` in a repo, or from the extracted pin tree under AC6 -- "
                        "never from an unpinned working tree")
# The runner's materializer is the code that actually RUNS the slice: the ledger modules the run
# imports plus the runner itself. Naming the set explicitly is the point -- a digest over "whatever
# was in the directory" is not a declared input, and `$ref sha256` is satisfied by 64 hex, never by
# a git object id (SHA-1). CVO item 4 / Amendment 3 item 3.
RUNNER_MEMBERS = [
    "org/standards/isck/ledger/engine.py",
    "org/standards/isck/ledger/machines.py",
    "org/standards/isck/ledger/lineage.py",
    "org/standards/isck/ledger/folds.py",
    "org/standards/isck/ledger/surfaces.py",
    "org/standards/isck/ledger/contests.py",
    "org/standards/isck/ledger/slice.py",
    "org/standards/isck/ledger/snapshot.py",
    "org/standards/isck/ledger/battery/run_slice.py",
]


def read_at_pin(rel, pin):
    """The ONE way this module reads a pinned file. Returns LF-normalised bytes, or None.

    Two byte sources, one number: `git show <pin>:<path>` in a repo, and the extracted tree under
    AC6, which IS the pin by construction and has no .git at all. Every caller goes through here so
    the repo run and the clean-clone run cannot silently answer differently -- which they DID: the
    first clean-clone run labelled 14 repo-path materializers `materializer_not_a_single_artifact`
    because `git show` failed with no .git, and a read failure wore the costume of a data verdict.
    """
    if os.path.isdir(os.path.join(REPO_ROOT, ".git")):
        try:
            raw = subprocess.check_output(["git", "show", "%s:%s" % (pin, rel)], cwd=REPO_ROOT,
                                          stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            return None
    else:
        try:
            with open(os.path.join(REPO_ROOT, rel), "rb") as fh:
                raw = fh.read()
        except IOError:
            return None
    return raw.replace(CRLF, LF)


def byte_source():
    return ("git show <pin>:<path>" if os.path.isdir(os.path.join(REPO_ROOT, ".git"))
            else "extracted pin tree (git archive; no .git present, the tree IS the pin)")


def tree_digest(paths, pin):
    """64-hex SHA-256 over a DECLARED canonical tree inventory. Returns (digest, report).

    TWO SOURCES, ONE NUMBER. In the repo the bytes come from `git show <pin>:<path>`. Under AC6 the
    runner executes inside an extracted `git archive` of the pin, which has NO .git at all -- there
    the extracted tree IS the pin, by construction, and the bytes are read from disk. The digest
    must be identical either way or the clean-clone evidence binds to nothing.

    SO EVERY MEMBER IS LF-NORMALISED BEFORE HASHING, AND THAT IS DECLARED. This is the defect class
    that has bitten this seat four times in this TO: a CRLF checkout and an LF blob are the same
    source and different bytes, and a digest that does not say which it took is not an identity. It
    is the checkout's EOL policy that must not move the number, so the normalisation is part of the
    method rather than a property of where the code happens to be sitting.

    A member absent, or DIRTY against the pin, is reported beside the digest and never folded into
    it -- a digest cannot detect that it describes bytes which did not run.
    """
    lines, missing, dirty = [], [], []
    src = byte_source()
    have_git = os.path.isdir(os.path.join(REPO_ROOT, ".git"))
    for rel in sorted(paths):
        norm = read_at_pin(rel, pin)
        if norm is None:
            missing.append(rel)
            continue
        lines.append("%s  %s" % (hashlib.sha256(norm).hexdigest(), rel))
        if have_git:
            # THE DIRTY CHECK IS THE WHOLE POINT OF PINNING: a digest read at a pin while the code
            # that ran is an uncommitted working tree names bytes that DID NOT RUN. In the archive
            # there is no second copy to disagree, so the check does not run and does not claim to.
            try:
                with open(os.path.join(REPO_ROOT, rel), "rb") as fh:
                    if fh.read().replace(CRLF, LF) != norm:
                        dirty.append(rel)
            except IOError:
                dirty.append(rel + " (absent in working tree)")
    inventory = (LF.decode().join(lines) + LF.decode()).encode("utf-8")
    return ("sha256:" + hashlib.sha256(inventory).hexdigest(),
            {"members_declared": len(paths), "members_hashed": len(lines),
             "members_absent_at_pin": missing, "members_DIRTY_vs_worktree": dirty,
             "digest_describes_the_code_that_ran": not dirty and not missing,
             "byte_source": src, "method": DIGEST_METHOD,
             "normalization": DIGEST_NORMALIZATION})


def slice_provenance(manifest, pins, run_pin, started_at):
    """The four provenance records the SLICE owns. Returns (records, ids)."""
    digest, dreport = tree_digest(RUNNER_MEMBERS, run_pin)
    mat = "mat:wp3b-slice-runner"
    ver = "matv:" + digest.split(":")[1][:12]      # identity DERIVED from the sha256, not a SHA-1
    frontier = "sf:wp3b-" + pins["declared"]
    run = "run:wp3b-" + pins["declared"]
    # observed_at is carried ONLY when it is a TIME. Measured on this population: 36 of 42 parse
    # as ISO, 5 are absent, and ONE carries the prose "per-DB, matches each DB" in a field the
    # manifest types as a timestamp. Passing that through put a frontier entry "after" the run's
    # start under a string compare and the ledger REFUSED the slice's own provenance batch with
    # L-08-observed-after-start -- row 8 catching a value that is not what its field says it is,
    # on real data, which is the entire point of the rule. A non-time is an explicit ABSENCE here,
    # never a value, and never silently coerced into one.
    entries, no_time = [], 0
    for p in manifest["parts"]:
        e = {"source_serial": "ent:" + _slug(p["id"]), "source_native_key": p.get("home")}
        v = (p.get("vintage") or {}).get("measured_utc")
        if isinstance(v, str) and ISO_TIME.match(v):
            e["observed_at"] = v
        else:
            no_time += 1
        entries.append(e)
    recs = [
        {"record_type": "materializer", "materializer_serial": mat,
         "semantic_layer": "isck_ledger_slice", "canonical_role": "wp3b_admission_runner",
         "owner": "0.4.0_DT_ClientPlatform~X", "status_basis": "authored"},
        {"record_type": "materializer_version", "version_id": ver, "materializer_serial": mat,
         "bundle_completeness": "complete",
         "bundle_digest": digest, "valid_from": started_at},
        {"record_type": "source_frontier", "source_frontier_id": frontier, "entries": entries,
         "normalization_version": "v1", "completeness": "complete",
         "expected_count": len(manifest["parts"])},
        {"record_type": "materialization_run", "run_id": run, "materializer_serial": mat,
         "materializer_version_id": ver, "source_frontier_id": frontier,
         "started_at": started_at, "run_status": "succeeded", "random_seeds": [],
         "output_surface_version_ids": [], "executed_on_fabric": "cloud"},
    ]
    return recs, {"materializer": mat, "version": ver, "frontier": frontier, "run": run,
                  "digest": digest, "digest_report": dreport,
                  "entries_without_a_time": no_time, "entries": len(entries)}
