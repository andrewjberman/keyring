#!/usr/bin/env python
"""ISCK battery additions -- coverage + attribution probes.

Author: 0.4.0_DT_ClientPlatform~X. Authorized to land by 1.0.0_SA_CTO~X (msg 76477/76496)
as a round-1 deliverable of the D11 ISCK adversarial pass.

WHY THIS EXISTS, SEPARATELY FROM validate_isck.py: that battery asks "does every mutant
reject, for its named reason?" -- a question about the mutants someone thought to write.
These arms ask the complementary question: "what does the schema NOT constrain at all?"
A law with no conditional attached has no mutant to write, so it cannot fail the battery.
DT-1 and DT-7 were both found this way, the second one mechanically, with no human hunting it.

FOUR STANDING ARMS, each printing its own denominator, each with self-controls:

  ARM 1  conditional-coverage differencing -- for every value-keyed discriminant, which values
         of its domain does a conditional actually reach? An unreached value is a value whose
         law is prose. Rule 24 postulate (iv) binds CONDITIONAL COVERAGE, not only value lists
         (adopted into ISCK doctrine at the round-1 boundary).
  ARM 2  branch-scoped rejection attribution -- two independent questions about the negative arm:
         (2a) does each mutant reject via one of the keywords IT declares, measured through a
              different code path than the validator's own assertion?
         (2b) does the rejecting error land on a field COUPLED to what was actually mutated?
              A mutant can trip the right KEYWORD on the WRONG FIELD; 2b is the axis 2a cannot see.
         Coupling groups are derived FROM THE SCHEMA, so 2b needs no hand-maintained table and
         cannot go stale as the mutant set grows.
  ARM 3  enum-value inhabitability census -- can every enum value appear in a VALID record?
         Carries companion-field repair, and DISTINGUISHES "no repair supplied" from "repair
         tried, still invalid" -- an unrepaired value is an open question, never a verdict.
  ARM 4  paired-arm coverage -- a conditional that binds VALUE -> FIELD REQUIRED without the
         complement FIELD PRESENT -> VALUE CONSTRAINED. Five members of that family were found
         by hand across rounds 1-2 (DT-5, DT-7, DT-R2-1, and two at once in DT-R2-5, which
         landed in the very batch that adopted the paired-arm rule as doctrine). A sentence in
         a doctrine did not survive one batch; this arm is the gate that does.

GENERALIZATION: every arm reads the schema OBJECT, not a copy of its rules. ARM 1 survived the
v0 -> v0.1 rewrite from enumerated if/then arms to dependentRequired without an edit. A construct
ARM 1 cannot parse is reported UNPARSED and NEVER counted as covered: an unparsed conditional
scored as covered is precisely the false-green these arms exist to kill.

Run:  python isck_coverage_probes.py          (self-test; exit 0 unless a self-control fails)
"""
import copy
import hashlib
import json
import os
import subprocess
import sys

import jsonschema

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "ISCK_CONTRACT.v0.schema.json")


# ---------------------------------------------------------------- schema introspection
def _walk_conditionals(node, path, out, unparsed):
    """Collect every conditional construct under a record branch.

    Appends (path, discriminant_field, covered_values_or_None, kind, coupled_fields).
    covered_values is None for presence-keyed constructs (dependentRequired/dependentSchemas),
    which discriminate on a field EXISTING rather than on its value.
    """
    if not isinstance(node, dict):
        return
    if "if" in node:
        cond = node["if"]
        then = node.get("then") or {}
        coupled = _fields_named(then)
        got = False
        # A DISCRIMINANT MAY BE DISJUNCTIVE. `if: {anyOf: [{properties:{a:...}}, ...]}` keys on
        # "a OR b", and reading only the top-level `properties` scored the whole arm UNPARSED --
        # correctly, but it left a real conditional uncounted. Each branch contributes its own
        # (field, values) pair; the arm reaches a value if ANY branch names it.
        branches = [cond] if isinstance(cond, dict) else []
        for key in ("anyOf", "oneOf", "allOf"):
            for sub in (cond.get(key) or []) if isinstance(cond, dict) else []:
                if isinstance(sub, dict):
                    branches.append(sub)
        for br in branches:
            if not isinstance(br.get("properties"), dict):
                continue
            for field, spec in br["properties"].items():
                if "const" in spec:
                    out.append((path, field, {spec["const"]}, "if/const", coupled))
                    got = True
                elif "enum" in spec:
                    out.append((path, field, set(spec["enum"]), "if/enum", coupled))
                    got = True
        if not got:
            unparsed.append((path, "if", json.dumps(cond)[:70]))
    if "dependentRequired" in node:
        for field, req in node["dependentRequired"].items():
            out.append((path, field, None, "dependentRequired", set(req) | {field}))
    if "dependentSchemas" in node:
        for field, sub in node["dependentSchemas"].items():
            out.append((path, field, None, "dependentSchemas", _fields_named(sub) | {field}))
    for key in ("allOf", "anyOf", "oneOf"):
        for i, sub in enumerate(node.get(key, []) or []):
            _walk_conditionals(sub, "%s.%s[%d]" % (path, key, i), out, unparsed)
    for key in ("then", "else"):
        if key in node:
            _walk_conditionals(node[key], "%s.%s" % (path, key), out, unparsed)


def _fields_named(sub):
    """Every property name a subschema mentions -- its coupling surface."""
    names = set()
    if not isinstance(sub, dict):
        return names
    for key in ("required",):
        for f in sub.get(key, []) or []:
            names.add(f)
    if isinstance(sub.get("properties"), dict):
        names |= set(sub["properties"].keys())
    for key in ("not", "then", "else", "if"):
        if key in sub:
            names |= _fields_named(sub[key])
    for key in ("allOf", "anyOf", "oneOf"):
        for item in sub.get(key, []) or []:
            names |= _fields_named(item)
    return names


def _enum_of(schema, branch, field):
    spec = branch.get("properties", {}).get(field)
    if spec is None:
        return None
    if "enum" in spec:
        return list(spec["enum"])
    if "$ref" in spec:
        target = schema.get("$defs", {}).get(spec["$ref"].split("/")[-1], {})
        if "enum" in target:
            return list(target["enum"])
    return None


def _record_defs(schema):
    return {k: v for k, v in schema.get("$defs", {}).items()
            if isinstance(v, dict) and "properties" in v and "record_type" in v.get("properties", {})}


def _branch_validator(schema, record_type):
    sub = schema["$defs"][record_type]
    return jsonschema.Draft202012Validator(dict(sub, **{"$defs": schema["$defs"]}))


def _leaf_errors(validator, inst):
    out = []
    for err in validator.iter_errors(inst):
        stack = [err]
        while stack:
            cur = stack.pop()
            if cur.context:
                stack.extend(cur.context)
            else:
                out.append(cur)
    return out


# ---------------------------------------------------------------------------- ARM 1
def arm_coverage(schema, verbose=True):
    """Report values no VALUE-KEYED conditional reaches.

    WARN: THE OUTPUT IS A CANDIDATE LIST, NOT A FINDING LIST. Measured against v0.1: of 6 gaps
    reported, 1 was a real defect, 3 were PROTECTED by a mechanism this arm does not count
    (a presence-keyed dependentRequired, or a plain `required` in the base branch), and 2 were
    unconditioned BY DESIGN (a 'null verdict' value legitimately carries no obligation).
    Every gap MUST be adjudicated by constructing the record the missing rule would forbid and
    testing it. A gap reported as a finding without that test is a FALSE RED -- the exact
    inverse of the false-green this arm exists to kill, and it fires hardest on a schema that
    has just been improved, because a good fix often uses a mechanism this arm cannot see.

    WARN: AND THE BLIND SPOT THAT MATTERS MORE: this arm can ONLY find gaps in a record that
    ALREADY HAS a discriminant. A record type with ZERO conditionals has zero discriminants,
    therefore zero gaps, and reads IDENTICAL to a fully-covered one. Those records are printed
    below as NOT EXAMINED with their own denominator -- never folded into the clean count.
    """
    if verbose:
        print("=" * 94)
        print("ARM 1 -- CONDITIONAL COVERAGE DIFFERENCING (candidate generator, not a verdict)")
        print("=" * 94)
    gaps = []
    unparsed_all = []
    checked = 0
    unexamined = []
    for rtype, branch in sorted(_record_defs(schema).items()):
        conds = []
        unparsed = []
        _walk_conditionals(branch, rtype, conds, unparsed)
        unparsed_all.extend(unparsed)
        by_field = {}
        presence_coupled = set()
        for _p, field, values, _kind, coupled in conds:
            if values is not None:
                by_field.setdefault(field, set()).update(values)
            else:
                # presence-keyed (dependentRequired/dependentSchemas): couples fields without
                # discriminating on a value. It PROTECTS without 'reaching' any value.
                presence_coupled |= set(coupled)
        if not by_field:
            unexamined.append((rtype, sorted(presence_coupled)))
            continue
        for field, covered in sorted(by_field.items()):
            domain = _enum_of(schema, branch, field)
            if domain is None:
                continue
            checked += 1
            missing = [v for v in domain if v not in covered]
            if verbose:
                mark = "OK:" if not missing else "GAP"
                print("  [%s] %s.%s: %d of %d values reached by a value-keyed conditional"
                      % (mark, rtype, field, len(domain) - len(missing), len(domain)))
            if missing:
                gaps.append((rtype, field, missing, domain))
                if verbose:
                    print("        domain    : %s" % domain)
                    print("        reached   : %s" % sorted(covered))
                    print("        UNREACHED : %s  <- CANDIDATE, adjudicate before reporting"
                          % missing)
                    if presence_coupled:
                        print("        NOTE: this record ALSO has presence-keyed coupling on %s"
                              % presence_coupled)
                        print("              -- a value above may already be protected by it.")
    if verbose:
        print("  DENOMINATOR: %d value-keyed discriminant fields across %d record types"
              % (checked, len(_record_defs(schema))))
        print("  RESULT: %d candidate gap(s) -- each needs the construct-the-lying-record test"
              % len(gaps))
        a1_adj, a1_def, a1_lapse, a1_new = _dispose_arm1(gaps)
        print("  GAPS: %d  (%d adjudicated, %d deferred, %d NEW, %d re-adjudication)"
              % (len(gaps), len(a1_adj), len(a1_def), len(a1_new), len(a1_lapse)))
        for rtype, field, missing, _dom, trigger in a1_def:
            print("    DEFERRED      %-22s %s=%s" % (rtype, field, sorted(missing)))
            print("                  class D: %s NEVER suppressed." % trigger)
        for rtype, field, missing, _dom, prior in a1_lapse:
            print("    RE-ADJUDICATION REQUIRED  %s.%s -- ruled on %s, now %s"
                  % (rtype, field, prior, sorted(missing)))
        for rtype, field, missing, _dom in a1_new:
            print("    NEW           %-22s %s=%s -- UNRULED" % (rtype, field, sorted(missing)))
        if a1_adj:
            print("    %d row(s) suppressed by ARM1_ADJUDICATION.json -- disposed by the record, "
                  "auditable there, not invisible" % len(a1_adj))
        if unexamined:
            print("  NOT EXAMINED: %d of %d record types have NO value-keyed discriminant, so this"
                  % (len(unexamined), len(_record_defs(schema))))
            print("                arm is STRUCTURALLY BLIND to them. Zero gaps here means zero")
            print("                DISCRIMINANTS, never zero defects:")
            for rtype, coupled in unexamined:
                extra = (" (presence-keyed coupling on %s)" % coupled) if coupled else " (no conditional at all)"
                print("        %s%s" % (rtype, extra))
        if unparsed_all:
            print("  WARN: %d conditional construct(s) NOT PARSED -- not counted as covered:"
                  % len(unparsed_all))
            for path, kind, blob in unparsed_all:
                print("        %s [%s] %s" % (path, kind, blob))
        else:
            print("  OK: 0 unparsed conditional constructs")
    return gaps, unparsed_all


# ---------------------------------------------------------------------------- ARM 2
def _coupling_groups(schema, rtype):
    """Fields that a conditional binds together -- the legal blast radius of a mutation."""
    conds = []
    _walk_conditionals(schema["$defs"][rtype], rtype, conds, [])
    groups = []
    for _p, field, _values, _kind, coupled in conds:
        groups.append({field} | set(coupled))
    return groups


def _changed_fields(base, inst):
    changed = set()
    for key in set(base) | set(inst):
        if base.get(key, _MISSING) != inst.get(key, _MISSING):
            changed.add(key)
    return changed


class _Missing(object):
    pass


_MISSING = _Missing()


def arm_attribution(schema, fixtures, mutants, verbose=True):
    if verbose:
        print()
        print("=" * 94)
        print("ARM 2 -- BRANCH-SCOPED REJECTION ATTRIBUTION")
        print("=" * 94)
    kw_fail = []
    field_fail = []
    unscoreable = []
    for entry in mutants:
        if len(entry) == 3:
            name, inst, expected_kw = entry
        else:
            name, inst = entry
            expected_kw = None
        rtype = inst.get("record_type") if isinstance(inst, dict) else None
        if rtype not in schema.get("$defs", {}) or rtype not in fixtures:
            unscoreable.append((name, "record_type %r has no fixture/branch" % rtype))
            continue
        errs = _leaf_errors(_branch_validator(schema, rtype), inst)
        if not errs:
            kw_fail.append((name, "ACCEPTED -- no error at all", expected_kw))
            field_fail.append((name, "ACCEPTED", set()))
            continue
        # 2a -- keyword, through our own path
        if expected_kw:
            got = {e.validator for e in errs}
            if not (got & set(expected_kw)):
                kw_fail.append((name, sorted(got), sorted(expected_kw)))
        else:
            unscoreable.append((name, "mutant declares no expected keywords"))
        # 2b -- field coupling
        changed = _changed_fields(fixtures[rtype], inst)
        legal = set(changed)
        for group in _coupling_groups(schema, rtype):
            if group & changed:
                legal |= group
        hit = set()
        for err in errs:
            path_txt = str(list(err.absolute_path))
            for field in legal:
                if field in path_txt or field in err.message:
                    hit.add(field)
        if not hit:
            field_fail.append((name, sorted(changed), sorted({e.validator for e in errs})))
    total = len(mutants)
    if verbose:
        print("  2a KEYWORD  : %d of %d mutants reject via a keyword they declare"
              % (total - len(kw_fail), total))
        for row in kw_fail:
            print("    ERROR: %s -- got %s, declared %s" % row)
        print("  2b FIELD    : %d of %d mutants reject on a field coupled to what was mutated"
              % (total - len(field_fail), total))
        for row in field_fail:
            print("    ERROR: %s -- mutated %s, rejected via %s, no coupled field named" % row)
        if unscoreable:
            print("  UNSCOREABLE: %d mutant(s) -- reported, NOT counted as passing:" % len(unscoreable))
            for name, why in unscoreable:
                print("    %s: %s" % (name, why))
        else:
            print("  OK: 0 unscoreable mutants")
    return kw_fail, field_fail, unscoreable


# ---------------------------------------------------------------------------- ARM 3
def arm_inhabitability(schema, fixtures, repairs, verbose=True):
    if verbose:
        print()
        print("=" * 94)
        print("ARM 3 -- ENUM-VALUE INHABITABILITY CENSUS")
        print("=" * 94)
    validator = jsonschema.Draft202012Validator(schema)
    total = 0
    inhabitable = 0
    dead = []
    unrepaired = []
    for rtype in sorted(fixtures):
        branch = schema.get("$defs", {}).get(rtype)
        if not branch:
            continue
        for field in sorted(branch.get("properties", {})):
            domain = _enum_of(schema, branch, field)
            if not domain:
                continue
            for value in domain:
                total += 1
                inst = copy.deepcopy(fixtures[rtype])
                inst[field] = value
                if not list(validator.iter_errors(inst)):
                    inhabitable += 1
                    continue
                fixer = repairs.get((rtype, field, value))
                if fixer is None:
                    unrepaired.append("%s.%s=%s" % (rtype, field, value))
                    continue
                repaired = fixer(copy.deepcopy(inst))
                if not list(validator.iter_errors(repaired)):
                    inhabitable += 1
                else:
                    dead.append("%s.%s=%s" % (rtype, field, value))
    if verbose:
        print("  CENSUS: %d of %d enum values inhabitable by a valid record" % (inhabitable, total))
        for row in dead:
            print("    UNREACHABLE (repair supplied and tried, still invalid): %s" % row)
        for row in unrepaired:
            print("    OPEN (no companion repair supplied -- a question, NOT a verdict): %s" % row)
        print("  A value is called UNREACHABLE only after its companion-field repair was tried.")
        print("  Without that distinction a CORRECT conditional reads as a dead value.")
    return dead, unrepaired


# ---------------------------------------------------------------------------- ARM 4
THEN_KNOWN = {"required", "not", "properties", "allOf", "anyOf", "oneOf", "if", "then", "else",
              "minItems", "maxItems", "type", "enum", "const", "$ref", "description",
              "minLength", "format", "items"}


def _then_effects(node, out, unparsed, path):
    """Walk a then-schema for its effects on fields, recursing into nested combinators.

    Three effects count as PAIRING a require arm: REQUIRE (must be present), FORBID (must be
    absent), CONSTRAIN (value restricted). Missing the nested forms is a FALSE-RED generator --
    this arm's own v1 read only the top level and scored four correctly-paired R2-1 arms as
    unpaired, which is why the UNPARSED guard below is not optional.
    """
    if not isinstance(node, dict):
        return
    for field in node.get("required", []) or []:
        out.add(("REQUIRE", field))
    nots = node.get("not")
    if isinstance(nots, dict):
        for field in nots.get("required", []) or []:
            out.add(("FORBID", field))
        for key in ("allOf", "anyOf", "oneOf"):
            for sub in nots.get(key, []) or []:
                _then_effects(sub, out, unparsed, path + ".not." + key)
    if isinstance(node.get("properties"), dict):
        for field in node["properties"]:
            out.add(("CONSTRAIN", field))
    for key in ("allOf", "anyOf", "oneOf"):
        for i, sub in enumerate(node.get(key, []) or []):
            _then_effects(sub, out, unparsed, "%s.%s[%d]" % (path, key, i))
    for key in ("then", "else"):
        if key in node:
            _then_effects(node[key], out, unparsed, path + "." + key)
    unknown = set(node.keys()) - THEN_KNOWN
    if unknown:
        unparsed.append((path, sorted(unknown)))


def _conditional_arms(branch, rtype):
    arms = []
    unparsed = []
    for i, sub in enumerate(branch.get("allOf", []) or []):
        cond = sub.get("if", {})
        then = sub.get("then")
        if then is None or not isinstance(cond.get("properties"), dict):
            continue
        eff = set()
        _then_effects(then, eff, unparsed, "%s.allOf[%d].then" % (rtype, i))
        for disc, spec in cond["properties"].items():
            vals = {spec["const"]} if "const" in spec else set(spec.get("enum", []))
            if vals:
                arms.append((disc, vals, eff))
    return arms, unparsed


ADJUDICATION_PATH = os.path.join(HERE, "ARM4_ADJUDICATION.json")


def _no_dupes(pairs):
    """Refuse a duplicate JSON object key. Same shape as verify_receipt.py:31/:45.

    WARN: I SHIPPED THIS GATE WITHOUT THE GUARD AND THE ESTATE ALREADY HAD IT. Plain `json.load`
    is LAST-WINS, so a sidecar carrying one key twice collapses silently and the survivor is
    whichever was written last. In the direction that matters, an entry ruled class A (SUPPRESSED)
    and one ruled class D (NEVER SUPPRESSED) sharing a key means one ruling ceases to exist -- and
    if the A survives, A DEFERRED ROW IS SUPPRESSED, the precise outcome the class-D control was
    written to make impossible. THAT CONTROL STILL PASSES: it tests the disposition LOGIC while
    the corruption happens in the LOADER upstream of it.
    AND THE GENERATOR CANNOT COVER THIS. Its 20-in/20-out assertion runs at GENERATION; this
    loader runs at CONSUMPTION, and a later hand-edit, merge artifact or concatenation is read
    with no assertion in front of it. GENERATED-TODAY IS NOT TRUSTWORTHY-TOMORROW.
    The guard exists in verify_receipt.py BECAUSE this class bit the receipt contract -- an
    invalid-first/valid-last duplicate collapsed and the verifier returned zero findings on a
    document carrying a forgery. Same defect, in a gate written after that lesson, by the seat
    that banked it.
    """
    seen = set()
    for key, _value in pairs:
        if key in seen:
            raise ValueError("REFUSING TO PARSE -- duplicate JSON object key %r" % key)
        seen.add(key)
    return dict(pairs)


PERMITTED_CLASSES = {"A", "B", "C", "D"}

# R3-CVO-2 (3.0.0_SA_CVO~X's orphan-sidecar exhibit, routed to this seat 77231). A sidecar entry
# used to need only a structurally valid EXACT KEY to suppress a live row -- so an entry that
# corresponds to NO ruling, or to a ruling whose arm has since changed underneath it, suppressed
# exactly as well as a real one. The key proved the SHAPE of a ruling and never its EXISTENCE.
LINK_FIELDS = ("record_ref", "ruled_at", "arm_digest")


def _arm_digest(payload):
    """sha256 over the arm's NORMALIZED content -- what was ruled on, not how it was written.

    Normalized means the PARSED effect set / domain, never the raw JSON text: a reformat, a key
    reorder or a comment must not read as a moved arm, and a real change to what the arm requires
    must. json.dumps(sort_keys) over parsed structures gives exactly that.
    """
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


_RECORD_CACHE = {}


def _repo_root():
    try:
        out = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                      cwd=HERE, stderr=subprocess.PIPE)
        return out.decode("utf-8").strip()
    except (OSError, subprocess.CalledProcessError):
        return None


_RECORD_CACHE = {}


def _repo_root():
    """The trusted repo root: ISCK_REPO_ROOT first, then --show-toplevel, else None.

    R3-CRO-15's CONTRACT (1.0.0_SA_CTO~X 77275). run_gates.sh:24 exports ISCK_REPO_ROOT because
    the canonical gate runs inside an ATOMIC EXTRACT that is not a checkout -- my 8a9ad0644e
    resolved from the extract and turned the gate into a no-op, and my 82efe0bb27 hotfix fixed
    that by open()ing the record out of the extract, which CRO~X correctly names a CONTAMINATION
    path: in a WORKING TREE that reads the dirty file instead of the pinned one. Object database
    only, from a root the RUNNER names.
    """
    env = os.environ.get("ISCK_REPO_ROOT")
    if env and os.path.isdir(env):
        return env
    try:
        return subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                       cwd=HERE, stderr=subprocess.PIPE).decode().strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def _record_blob(ruled_at, path):
    """(text, state) via `git -C <root> show <ruled_at>:<path>`. NEVER open() a working tree.

    state: OK | NO_ROOT | NO_COMMIT | NO_FILE. Stderr is CAPTURED, never discarded -- a swallowed
    git error would make a broken instrument read identically to a real absence, and NO_ROOT
    (nowhere to ask) must never read as NO_COMMIT (asked, and it is not there).
    """
    # R3-DT-6: the RESOLVED ROOT is part of the key. Keyed on (ruled_at, path) alone, a cache
    # populated under one root answered for a DIFFERENT root -- so a control that swapped the root
    # without clearing got the stale verdict and passed vacuously, green. Control (c) was correct
    # only because it happened to call clear() on both sides, a line whose load-bearing role was
    # declared NOWHERE. Keying by root retires that dependency instead of documenting it.
    root = _repo_root()
    key = (root, ruled_at, path)
    if key in _RECORD_CACHE:
        return _RECORD_CACHE[key]
    if root is None:
        out = (None, "NO_ROOT")
    else:
        try:
            subprocess.check_output(["git", "-C", root, "cat-file", "-e",
                                     "%s^{commit}" % ruled_at], stderr=subprocess.PIPE)
        except (OSError, subprocess.CalledProcessError):
            out = (None, "NO_COMMIT")
        else:
            try:
                blob = subprocess.check_output(["git", "-C", root, "show",
                                                "%s:%s" % (ruled_at, path)],
                                               stderr=subprocess.PIPE)
                out = (blob.decode("utf-8", "replace"), "OK")
            except (OSError, subprocess.CalledProcessError):
                out = (None, "NO_FILE")
    _RECORD_CACHE[key] = out
    return out


def _anchor_present(text, anchor):
    """Does the record actually CARRY the ruling this entry points at?

    Two shapes, because the two records ADJUDICATE differently and one shape would be vacuous for
    the other: ARM 1 rules ROW BY ROW (`#rows-4,5` -> those numbered table rows), ARM 4 rules BY
    CLASS and says so in its own heading -- "the reason IS the record" -- so `#class-A` resolves
    to its CLASS A section. No anchor at all is not resolvable.
    """
    if anchor.startswith("rows-"):
        rows = [r for r in anchor[len("rows-"):].split(",") if r]
        return bool(rows) and all(("| %s |" % r) in text for r in rows)
    if anchor.startswith("class-"):
        return ("CLASS %s " % anchor[len("class-"):]) in text
    return False


def _resolve_state(entry):
    """RESOLVED | NO_ANCHOR | UNRESOLVED | NO_COMMIT | NO_FILE | NO_ANCHOR_IN_RECORD.

    Read entirely from the object database at the entry's OWN ruled_at, so what the working tree
    currently says about a record cannot change a verdict at a pin.
    """
    ref = entry.get("record_ref") or ""
    if "#" not in ref:
        return "NO_ANCHOR"
    path, anchor = ref.split("#", 1)
    text, state = _record_blob(entry.get("ruled_at") or "", path)
    if state == "NO_ROOT":
        return "UNRESOLVED"
    if state != "OK":
        return state
    return "RESOLVED" if _anchor_present(text, anchor) else "NO_ANCHOR_IN_RECORD"


def _link_state(entry, computed):
    """LINKED | ORPHAN (a link field missing) | STALE (the arm moved under the ruling).

    ORPHAN fails open to NEW, never to suppressed: an entry that cannot prove it descends from a
    ruling is worth exactly as much as no entry at all, and the row must come back. STALE is the
    value-set lapse generalized -- the ruling was real, its subject moved.
    """
    if any(entry.get(f) in (None, "") for f in LINK_FIELDS):
        return "ORPHAN"
    if computed is not None and entry.get("arm_digest") != computed:
        return "STALE"
    resolved = _resolve_state(entry)
    if resolved == "UNRESOLVED":
        # No trusted root anywhere. UNRESOLVED IS ITS OWN NAMED STATE and never LINKS: the gate
        # declines to suppress and says why, rather than trusting a ruling it cannot open.
        return "UNRESOLVED"
    if resolved != "RESOLVED":
        return "ORPHAN"
    return "LINKED"


def _validate_entries(record):
    """Every entry must be STRUCTURALLY SOUND AT CONSUMPTION, or nothing is suppressed.

    WARN: FOUND BY 4.0.0_SA_CRO~X ATTACKING 6245dc0a3d, AND MY LOADER GUARD HAD CLOSED ONLY HALF
    THE GAP. `_no_dupes` protects KEY UNIQUENESS. It says nothing about whether an entry's PAYLOAD
    agrees with its own key. The sidecar encodes the ruled value set TWICE -- once in the key's
    fourth part, once in `values_at_adjudication` -- and the loader matched on the KEY while never
    reading the payload for agreement. Their exhibit: key `...|evidence_refs|admitted` carrying
    payload `[admitted, candidate]` is accepted and SUPPRESSES, so a reader auditing the record
    sees a ruling covering two values while the gate matched on one.
    THAT IS THE TYPED-BESIDE-DERIVED CLASS INSIDE THE ARTIFACT WHOSE ONLY JOB IS TO BE TRUSTED,
    and the human-readable half is the half that lies. Two representations of one fact with no
    consistency check is exactly what the generator's 20-in/20-out assertion cannot reach: that
    assertion ran at GENERATION, and this is the consumption-time half I said was missing and then
    only half-supplied.
    Fail-open to honest: any mismatch raises, the caller suppresses NOTHING and prints a WARN.
    """
    for key, val in record.items():
        parts = key.split("|")
        if len(parts) != 4:
            raise ValueError("entry key %r has %d parts, expected 4" % (key, len(parts)))
        if not isinstance(val, dict):
            raise ValueError("entry %r payload is not an object" % key)
        cls = val.get("class")
        if cls not in PERMITTED_CLASSES:
            raise ValueError("entry %r class %r not in %s" % (key, cls, sorted(PERMITTED_CLASSES)))
        payload = val.get("values_at_adjudication")
        if not isinstance(payload, list):
            raise ValueError("entry %r values_at_adjudication is not a list" % key)
        if sorted(set(payload)) != sorted(payload):
            raise ValueError("entry %r values_at_adjudication is unsorted or has duplicates" % key)
        if payload != [v for v in parts[3].split(",") if v]:
            raise ValueError("entry %r payload %s DISAGREES with its own key's value set %s"
                             % (key, payload, parts[3]))


def _dispose(unpaired, digests=None):
    """Split ARM 4's rows against the ruled adjudication record.

    THE GATE CONSUMES THE RULING, BUT NEVER BY LABEL. Key = record_type|discriminant|field|values.
    WARN: A (record_type, discriminant, field) TRIPLE IS NOT UNIQUE -- entity_binding.binding_basis
    and identity_relation.claim_origin each carry TWO arms requiring evidence_refs on DIFFERENT
    value sets. A triple key silently collapsed 20 rows to 18, which would have SUPPRESSED AN ARM
    NOBODY RULED ON. The value set is part of the arm's identity. Found by generating the sidecar,
    not by designing it -- which is why the sidecar is DERIVED from ARM 4's own output.

    Four outcomes, and only the first is suppressed:
      ADJUDICATED  exact key present    -> suppressed, counted, auditable in the record
      DEFERRED     class D              -> NEVER suppressed; printed with its reversal trigger
      RE-ADJUDICATE same triple, different value set -> the ruling's premise MOVED. A ruling about
                   a 4-value enum does not survive it becoming 5.
      NEW          no entry at all      -> reported as it always was
    A missing or unreadable record suppresses NOTHING and says so: a gate that silently falls back
    to "suppress none" is honest, but one that silently falls back to "suppress all" is the failure
    this whole arm exists to prevent, and the difference must not be a comment.
    """
    try:
        with open(ADJUDICATION_PATH, "r", encoding="utf-8") as handle:
            record = json.load(handle, object_pairs_hook=_no_dupes).get("entries", {})
        _validate_entries(record)
    except (OSError, ValueError) as exc:
        print("  WARN: ARM4_ADJUDICATION.json UNREADABLE (%s) -- suppressing NOTHING, every row "
              "reported" % str(exc)[:70])
        return [], [], [], list(unpaired)
    by_triple = {}
    for key, val in record.items():
        parts = key.split("|")
        if len(parts) == 4:
            by_triple.setdefault(tuple(parts[:3]), []).append(val)
    adjudicated, deferred, lapsed, fresh = [], [], [], []
    orphans, stale, unresolved = [], [], []
    for rtype, disc, vals, field in unpaired:
        key = "%s|%s|%s|%s" % (rtype, disc, field, ",".join(sorted(vals)))
        entry = record.get(key)
        if entry is None:
            prior = by_triple.get((rtype, disc, field))
            if prior:
                lapsed.append((rtype, disc, vals, field,
                               sorted({v for p in prior for v in p["values_at_adjudication"]})))
            else:
                fresh.append((rtype, disc, vals, field))
            continue
        state = _link_state(entry, (digests or {}).get(key))
        if state in ("ORPHAN", "UNRESOLVED"):
            (orphans if state == "ORPHAN" else unresolved).append(key)
            fresh.append((rtype, disc, vals, field))
        elif state == "STALE":
            stale.append(key)
            lapsed.append((rtype, disc, vals, field, entry.get("values_at_adjudication", [])))
        elif entry.get("class") == "D":
            deferred.append((rtype, disc, vals, field))
        else:
            adjudicated.append((rtype, disc, vals, field))
    for key in orphans:
        print("  WARN: sidecar entry %r is an ORPHAN (missing %s) -- IGNORED, row reported NEW"
              % (key, "/".join(LINK_FIELDS)))
    for key in stale:
        print("  WARN: sidecar entry %r arm_digest MISMATCH -- the arm moved under the ruling; "
              "row reported RE-ADJUDICATION" % key)
    for key in unresolved:
        print("  WARN: sidecar entry %r UNRESOLVED (not a git checkout) -- the ruling could not "
              "be OPENED, so it is not trusted; row reported NEW" % key)
    return adjudicated, deferred, lapsed, fresh


ARM1_ADJUDICATION_PATH = os.path.join(HERE, "ARM1_ADJUDICATION.json")


def _validate_arm1_entries(record):
    """Entry guard for the ARM-1 sidecar. Mirrors ARM 4's, with a THREE-part key.

    ARM 4's key is record_type|discriminant|field|values because a triple was not unique there.
    ARM 1 has no discriminant column -- one field carries one domain -- so the key is
    record_type|field|unreached-values and the guard MUST check 3, not 4. Reusing ARM 4's
    four-part guard here would reject every well-formed ARM-1 entry, and reusing ARM 1's on
    ARM 4 would accept a key that collapses two arms. The arity IS the arm's identity.
    """
    for key, value in sorted(record.items()):
        parts = key.split("|")
        if len(parts) != 3:
            raise ValueError("entry %r key must be record_type|field|value-set (3 parts)" % key)
        if not isinstance(value, dict) or value.get("class") not in PERMITTED_CLASSES:
            raise ValueError("entry %r carries no permitted class" % key)
        payload = value.get("values_at_adjudication")
        if not isinstance(payload, list) or not payload:
            raise ValueError("entry %r has no values_at_adjudication" % key)
        if payload != sorted(set(payload)):
            raise ValueError("entry %r values_at_adjudication is unsorted or has duplicates" % key)
        if payload != [v for v in parts[2].split(",") if v]:
            raise ValueError("entry %r payload %s DISAGREES with its own key's value set %s"
                             % (key, payload, parts[2]))


def _dispose_arm1(gaps):
    """Split ARM 1's gap fields against the ruled adjudication record.

    ARM 1 emits CANDIDATES and says so; ARM1_ADJUDICATION.md disposes all 13 values by id, but
    until this gate existed the runner could not subtract them, so eight adjudicated rows printed
    every run forever. A standing list of rows everyone knows are fine is how a real one stops
    being read -- the same argument that earned ARM 4 its sidecar.

    Four outcomes, and only the first is suppressed:
      ADJUDICATED   exact key present  -> suppressed, counted, auditable in the record
      DEFERRED      class D            -> NEVER suppressed; printed with its reversal trigger
      RE-ADJUDICATE same (record_type, field), DIFFERENT unreached set -> the premise MOVED
      NEW           no entry at all    -> reported as it always was
    A missing or unreadable record suppresses NOTHING and says so.
    """
    try:
        with open(ARM1_ADJUDICATION_PATH, "r", encoding="utf-8") as handle:
            record = json.load(handle, object_pairs_hook=_no_dupes).get("entries", {})
        _validate_arm1_entries(record)
    except (OSError, ValueError) as exc:
        print("  WARN: ARM1_ADJUDICATION.json UNREADABLE (%s) -- suppressing NOTHING, every row "
              "reported" % str(exc)[:70])
        return [], [], [], list(gaps)
    by_pair = {}
    for key, val in record.items():
        parts = key.split("|")
        if len(parts) == 3:
            by_pair.setdefault(tuple(parts[:2]), []).append(val)
    adjudicated, deferred, lapsed, fresh = [], [], [], []
    orphans, stale, unresolved = [], [], []
    for rtype, field, missing, domain in gaps:
        key = "%s|%s|%s" % (rtype, field, ",".join(sorted(missing)))
        entry = record.get(key)
        if entry is None:
            prior = by_pair.get((rtype, field))
            if prior:
                lapsed.append((rtype, field, missing, domain,
                               sorted({v for p in prior for v in p["values_at_adjudication"]})))
            else:
                fresh.append((rtype, field, missing, domain))
            continue
        # ARM 1's arm is the FIELD'S DOMAIN plus the unreached set: a ruling that these values are
        # legitimately free has the domain as its PREMISE, so a domain that grows or shrinks under
        # the ruling must lapse it even when the unreached set happens to be unchanged.
        computed = _arm_digest({"domain": list(domain), "unreached": sorted(missing)})
        state = _link_state(entry, computed)
        if state in ("ORPHAN", "UNRESOLVED"):
            (orphans if state == "ORPHAN" else unresolved).append(key)
            fresh.append((rtype, field, missing, domain))
        elif state == "STALE":
            stale.append(key)
            lapsed.append((rtype, field, missing, domain,
                           entry.get("values_at_adjudication", [])))
        elif entry.get("class") == "D":
            deferred.append((rtype, field, missing, domain, entry.get("reversal_trigger", "")))
        else:
            adjudicated.append((rtype, field, missing, domain))
    for key in orphans:
        print("  WARN: sidecar entry %r is an ORPHAN (missing %s) -- IGNORED, row reported NEW"
              % (key, "/".join(LINK_FIELDS)))
    for key in stale:
        print("  WARN: sidecar entry %r arm_digest MISMATCH -- the domain or unreached set moved "
              "under the ruling; row reported RE-ADJUDICATION" % key)
    for key in unresolved:
        print("  WARN: sidecar entry %r UNRESOLVED (not a git checkout) -- the ruling could not "
              "be OPENED, so it is not trusted; row reported NEW" % key)
    return adjudicated, deferred, lapsed, fresh


def arm_paired(schema, verbose=True):
    """Report REQUIRE arms with no FORBID/CONSTRAIN partner on the same discriminant.

    WARN: CANDIDATE GENERATOR WITH A MANDATORY ADJUDICATION STEP -- raw precision measured at
    roughly 4 of 19. The discriminator is SEMANTIC and no schema-reader can compute it:
      HARMLESS  carrying MORE than required is not a lie. Every evidence_refs row is this --
                a record over-supplying warrant is fine.
      A LIE     the field's PRESENCE CONTRADICTS the value (adjudicated_by on an unadjudicated
                status; a delta_summary on integrity=verified).
    Judging which is which stays with the adjudicating seat. Standing use: run BEFORE landing a
    batch, so a require-only arm is visible in seconds instead of surviving to the next attack.
    """
    if verbose:
        print()
        print("=" * 94)
        print("ARM 4 -- PAIRED-ARM COVERAGE (candidate generator; ~4 of 19 raw are real)")
        print("=" * 94)
    records = _record_defs(schema)
    total = 0
    unpaired = []
    digests = {}
    unparsed_all = []
    for rtype, branch in sorted(records.items()):
        arms, unparsed = _conditional_arms(branch, rtype)
        unparsed_all.extend(unparsed)
        dep = set()
        for key, vals in (branch.get("dependentRequired") or {}).items():
            dep.add(key)
            dep.update(vals)
        by_disc = {}
        for disc, _vals, eff in arms:
            by_disc.setdefault(disc, set()).update(eff)
        for disc, vals, eff in arms:
            for kind, field in sorted(eff):
                if kind != "REQUIRE":
                    continue
                total += 1
                paired = (("FORBID", field) in by_disc.get(disc, set())
                          or ("CONSTRAIN", field) in by_disc.get(disc, set())
                          or field in dep)
                if not paired:
                    unpaired.append((rtype, disc, sorted(vals), field))
                    dkey = "%s|%s|%s|%s" % (rtype, disc, field, ",".join(sorted(vals)))
                    digests[dkey] = _arm_digest(
                        {"values": sorted(vals),
                         "effects": sorted([list(e) for e in eff])})
    adjudicated, deferred, lapsed, fresh = _dispose(unpaired, digests)
    if verbose:
        print("  DENOMINATOR: %d REQUIRE effects across %d record types" % (total, len(records)))
        print("  REQUIRE-ONLY: %d  (%d adjudicated, %d deferred, %d NEW, %d re-adjudication)"
              % (len(unpaired), len(adjudicated), len(deferred), len(fresh), len(lapsed)))
        for rtype, disc, vals, field in fresh:
            print("    NEW           %-22s %s=%s -> requires %r" % (rtype, disc, vals, field))
        for rtype, disc, vals, field, was in lapsed:
            print("    RE-ADJUDICATE %-22s %s=%s -> requires %r" % (rtype, disc, vals, field))
            print("                  ruled at values %s, schema now has %s -- the ruling's premise "
                  "moved" % (was, vals))
        for rtype, disc, vals, field in deferred:
            print("    DEFERRED      %-22s %s=%s -> requires %r" % (rtype, disc, vals, field))
            print("                  class D: reversed at R2-2's landing (corroborated + "
                  "superseded_by becomes the desired expressible state). NEVER suppressed.")
        if adjudicated and not (fresh or lapsed):
            print("    %d row(s) suppressed by ARM4_ADJUDICATION.json -- disposed by the record, "
                  "auditable there, not invisible" % len(adjudicated))
        if unparsed_all:
            print("  WARN: %d then-clause(s) carry UNPARSED keywords -- NOT scored as unpaired:"
                  % len(unparsed_all))
            for path, keys in unparsed_all:
                print("        %s -> %s" % (path, keys))
        else:
            print("  OK: 0 unparsed then-clauses")
        print("  ADJUDICATE each row before reporting it: construct the record the missing")
        print("  partner would forbid and ask whether its presence CONTRADICTS the value.")
    return unpaired, unparsed_all


# ------------------------------------------------------------------------ self-controls
def _battery_contradictions(schema, fixtures, repairs):
    """Values a VALIDATING fixture actually carries that ARM 3 nonetheless calls dead.

    ARM 3 synthesises from ONE base fixture per record type and repairs its way to each
    value; the POSITIVE battery holds VARIANT fixtures that already exhibit those values
    and the synthesis never sees them. When the two disagree the battery wins -- it
    EXHIBITS a real record -- and ARM 3's verdict is a FALSE UNREACHABLE.
    """
    validator = jsonschema.Draft202012Validator(schema)
    dead, _open = arm_inhabitability(schema, fixtures, repairs, verbose=False)
    dead_set = set(dead)
    contradictions = []
    for name, inst in sorted(fixtures.items()):
        if not isinstance(inst, dict):
            continue
        rtype = inst.get("record_type")
        branch = schema.get("$defs", {}).get(rtype)
        if not branch or list(validator.iter_errors(inst)):
            continue
        for field, value in sorted(inst.items()):
            if not isinstance(value, str):
                continue
            domain = _enum_of(schema, branch, field)
            if domain and value in domain:
                row = "%s.%s=%s" % (rtype, field, value)
                if row in dead_set:
                    contradictions.append("%s (exhibited by fixture %s)" % (row, name))
    return contradictions


def self_controls(schema, fixtures, repairs=None, verbose=True):
    """Every arm must be reachable from a DIFFERENT truth -- it must be able to say either thing."""
    if verbose:
        print()
        print("=" * 94)
        print("SELF-CONTROLS")
        print("=" * 94)
    results = []

    # ARM 1 positive: a planted uncovered value must be caught.
    planted = copy.deepcopy(schema)
    branch = planted["$defs"]["state_observation"]
    if "planted_uncovered_value" not in branch["properties"]["failure_state"]["enum"]:
        branch["properties"]["failure_state"]["enum"].append("planted_uncovered_value")
    gaps, _ = arm_coverage(planted, verbose=False)
    caught = any(f == "failure_state" and "planted_uncovered_value" in miss
                 for _rt, f, miss, _dom in gaps)
    results.append(("ARM 1 catches a PLANTED uncovered value", caught, True))

    # ARM 1 negative: on the real schema it must NOT invent a gap in a fully covered field.
    real_gaps, _ = arm_coverage(schema, verbose=False)
    invented = any(f == "bundle_completeness" for _rt, f, _m, _d in real_gaps)
    results.append(("ARM 1 does NOT flag a fully-covered field", not invented, True))

    # ARM 2b positive: a mutant rejecting on an UNCOUPLED field must be caught.
    drifted = copy.deepcopy(fixtures["entity"])
    drifted["minting_authority"] = ""          # trips 'nonempty' on a field nothing couples
    _kw, field_fail, _un = arm_attribution(
        schema, fixtures, [("planted.drifted-mutant", drifted, ["minLength"])], verbose=False)
    results.append(("ARM 2b catches a mutant rejecting on an uncoupled field",
                    len(field_fail) == 0, True))

    # ARM 2a positive: a mutant declaring the WRONG keyword must be caught.
    wrongkw = copy.deepcopy(fixtures["entity"])
    wrongkw["entity_serial"] = "ent:portal/src/App.tsx"
    kw_fail, _ff, _un = arm_attribution(
        schema, fixtures, [("planted.wrong-keyword", wrongkw, ["minItems"])], verbose=False)
    results.append(("ARM 2a catches a mutant declaring the wrong keyword", len(kw_fail) == 1, True))

    # ARM 2a negative: the same mutant declaring the RIGHT keyword must pass.
    kw_ok, _ff2, _un2 = arm_attribution(
        schema, fixtures, [("planted.right-keyword", wrongkw, ["pattern"])], verbose=False)
    results.append(("ARM 2a passes the same mutant with the right keyword", len(kw_ok) == 0, True))

    # ARM 3: a structurally unsatisfiable value must read UNREACHABLE.
    broken = copy.deepcopy(schema)
    ent = broken["$defs"]["entity"]
    ent["properties"]["identity_scope"]["enum"].append("impossible_scope")
    ent.setdefault("allOf", []).append({
        "if": {"properties": {"identity_scope": {"const": "impossible_scope"}}},
        "then": {"required": ["a_field_that_is_not_in_properties"]},
    })
    dead, _open = arm_inhabitability(
        broken, {"entity": fixtures["entity"]},
        {("entity", "identity_scope", "impossible_scope"): lambda i: i}, verbose=False)
    results.append(("ARM 3 sees a structurally UNSATISFIABLE value", len(dead) == 1, True))

    # ARM 3 CROSS-ARM CONTROL. Nothing in this tool compared ARM 3's verdict against the
    # POSITIVE battery, so a repair going stale against a newly-landed conditional made two
    # arms of ONE instrument disagree in the SAME run with no arm to notice. MEASURED at
    # 9869831971: R2-2's `partial -> evidence_refs` cut left the shared drop_fingerprint
    # repair short of the warrant; ARM 3 printed UNREACHABLE for `partial` while fixture
    # state_observation_partial validated in the positive arm 15 of 15.
    if repairs is not None:
        results.append(("ARM 3 agrees with the POSITIVE battery on every exhibited value",
                        len(_battery_contradictions(schema, fixtures, repairs)) == 0, True))
        # ...and it must FIRE on a stale repair, or the arm above is vacuous. Both halves are
        # reachable from a DIFFERENT truth: the schema is fixed, only the repair moves.
        stale = dict(repairs)
        stale[("state_observation", "failure_state", "partial")] = (
            lambda i: dict((k, v) for k, v in i.items()
                           if k not in ("fingerprint", "fingerprint_method",
                                        "normalization_version", "evidence_refs")))
        results.append(("ARM 3 cross-arm control FIRES on a deliberately stale repair",
                        len(_battery_contradictions(schema, fixtures, stale)) > 0, True))

    # ARM 1 REGRESSION CONTROL for the DISJUNCTIVE discriminant. `if: {anyOf: [...]}` was
    # reported UNPARSED until R2-8's bridge_assertion shipped one; the guard did its job (never
    # scored as covered) but a real arm went uncounted. This asserts the shape is now PARSED and,
    # in the other direction, that a genuinely unreadable `if` is STILL reported rather than
    # silently accepted -- a parser that never says UNPARSED has stopped being a guard.
    disj = copy.deepcopy(schema)
    disj["$defs"]["source_frontier"]["allOf"] = [{
        "if": {"anyOf": [{"properties": {"record_type": {"const": "source_frontier"}},
                          "required": ["record_type"]}]},
        "then": {"required": ["entries"]},
    }]
    _g, u_disj = arm_coverage(disj, verbose=False)
    results.append(("ARM 1 PARSES a disjunctive if:{anyOf:[...]} discriminant",
                    len(u_disj) == 0, True))
    opaque = copy.deepcopy(schema)
    opaque["$defs"]["source_frontier"]["allOf"] = [{
        "if": {"not": {"required": ["entries"]}}, "then": {"required": ["entries"]}}]
    _g2, u_op = arm_coverage(opaque, verbose=False)
    results.append(("ARM 1 STILL reports an unreadable if as UNPARSED", len(u_op) == 1, True))

    # ARM 4 positive: a planted require-only arm must be caught.
    planted4 = copy.deepcopy(schema)
    planted4["$defs"]["source_frontier"]["allOf"] = [{
        "if": {"properties": {"record_type": {"const": "source_frontier"}},
               "required": ["record_type"]},
        "then": {"required": ["a_planted_require_only_field"]},
    }]
    p4, _pu = arm_paired(planted4, verbose=False)
    results.append(("ARM 4 catches a PLANTED require-only arm",
                    any(f == "a_planted_require_only_field" for _r, _d, _v, f in p4), True))

    # ARM 4 negative (REGRESSION CONTROL for this arm's own v1 bug): a forbid half expressed
    # NESTED as then.allOf[].not must be SEEN as pairing. v1 read only the top level and scored
    # four correctly-paired R2-1 referent_scope arms as REQUIRE-ONLY.
    nested = copy.deepcopy(schema)
    nested["$defs"]["source_frontier"]["allOf"] = [{
        "if": {"properties": {"record_type": {"const": "source_frontier"}},
               "required": ["record_type"]},
        "then": {"allOf": [{"required": ["nested_pair_field"]},
                           {"not": {"required": ["nested_pair_field"]}}]},
    }]
    n4, _nu = arm_paired(nested, verbose=False)
    results.append(("ARM 4 sees a NESTED then.allOf[].not forbid as pairing",
                    not any(f == "nested_pair_field" for _r, _d, _v, f in n4), True))

    # ---- ARM 4 CONSUME CONTROLS. A suppression mechanism is the one addition that can make this
    # gate LIE, so every path that must NOT suppress gets an arm. Synthetic rows are fed straight
    # to _dispose() -- no schema mutation, no file writes.
    _row = ("bridge_assertion", "verification_standing", ["superseded"], "superseded_by")
    _adj, _def, _lap, _new = _dispose([_row])
    results.append(("ARM 4 NEVER suppresses a class-D deferred row",
                    len(_def) == 1 and not _adj, True))
    _unknown = ("no_such_record", "no_such_field", ["x"], "no_such_target")
    _adj2, _def2, _lap2, _new2 = _dispose([_unknown])
    results.append(("ARM 4 reports an UNRULED row as NEW, never suppressed",
                    len(_new2) == 1 and not _adj2, True))
    # the lapse: a ruled triple whose VALUE SET has moved must return for re-adjudication
    _moved = ("identity_relation", "claim_origin", ["independently_observed", "human_adjudicated"],
              "evidence_refs")
    _adj3, _def3, _lap3, _new3 = _dispose([_moved])
    results.append(("ARM 4 LAPSES a suppression when the discriminant's value set moved",
                    len(_lap3) == 1 and not _adj3, True))
    # and the suppression must still actually FIRE on an exact match, or the arm above is vacuous
    _exact = ("identity_relation", "claim_origin", ["independently_observed"], "evidence_refs")
    _adj4, _def4, _lap4, _new4 = _dispose([_exact])
    results.append(("ARM 4 DOES suppress an exactly-ruled row (else the lapse arm is vacuous)",
                    len(_adj4) == 1 and not _lap4 and not _new4, True))

    # ---- LOADER GUARD, both directions. The duplicate-key vector reaches _dispose UPSTREAM of
    # every disposition control, so it needs its own arm at the loader, not at the logic.
    _dup = '{"entries": {"k|k|k|k": {"class": "A"}, "k|k|k|k": {"class": "D"}}}'
    try:
        json.loads(_dup, object_pairs_hook=_no_dupes)
        _refused = False
    except ValueError:
        _refused = True
    results.append(("LOADER REFUSES a duplicate sidecar key (A+D would collapse last-wins)",
                    _refused, True))
    _clean = '{"entries": {"a|b|c|d": {"class": "A", "values_at_adjudication": ["x"]}}}'
    try:
        _ok_load = json.loads(_clean, object_pairs_hook=_no_dupes)["entries"]["a|b|c|d"]["class"]
    except ValueError:
        _ok_load = None
    results.append(("LOADER still ACCEPTS a clean sidecar (else the refusal arm is vacuous)",
                    _ok_load == "A", True))

    # ---- CONSUMPTION-TIME ENTRY VALIDATION. 4.0.0_SA_CRO~X's superset-values attack: the key and
    # the payload each encode the ruled value set, and the loader matched on one without reading
    # the other. Every arm below must REFUSE; the last must ACCEPT, or they are all vacuous.
    def _rejects(entries):
        try:
            _validate_entries(entries)
            return False
        except ValueError:
            return True

    _good = {"r|d|f|admitted": {"class": "A", "values_at_adjudication": ["admitted"]}}
    results.append(("ENTRY GUARD refuses a SUPERSET payload (CRO~X's exhibit)",
                    _rejects({"r|d|f|admitted":
                              {"class": "A",
                               "values_at_adjudication": ["admitted", "candidate"]}}), True))
    results.append(("ENTRY GUARD refuses a SUBSET payload (the other direction)",
                    _rejects({"r|d|f|admitted,candidate":
                              {"class": "A", "values_at_adjudication": ["admitted"]}}), True))
    results.append(("ENTRY GUARD refuses a key without four parts",
                    _rejects({"r|d|f": {"class": "A", "values_at_adjudication": []}}), True))
    results.append(("ENTRY GUARD refuses an unpermitted class",
                    _rejects({"r|d|f|x": {"class": "Z", "values_at_adjudication": ["x"]}}), True))
    results.append(("ENTRY GUARD refuses an unsorted/duplicated payload",
                    _rejects({"r|d|f|a,a": {"class": "A", "values_at_adjudication": ["a", "a"]}}),
                    True))
    results.append(("ENTRY GUARD ACCEPTS a sound entry (else every arm above is vacuous)",
                    not _rejects(_good), True))

    # ---- ARM-1 SIDECAR (0.4.0_DT_ClientPlatform~X). Same four outcomes as ARM 4, one column
    # narrower, so every arm is re-derived against the 3-part key rather than assumed to carry
    # over. Each disposition arm is paired with the arm that makes it non-vacuous.
    _a1_d = ("entity_binding", "status", ["disputed"], ["open", "closed", "disputed"])
    _adjD, _defD, _lapD, _newD = _dispose_arm1([_a1_d])
    results.append(("ARM 1 NEVER suppresses a class-D deferred row",
                    len(_defD) == 1 and not _adjD, True))
    _a1_exact = ("materializer", "current_status", ["retired"],
                 ["active", "superseded", "retired", "unknown"])
    _adjE, _defE, _lapE, _newE = _dispose_arm1([_a1_exact])
    results.append(("ARM 1 DOES suppress an exactly-ruled row (else every arm here is vacuous)",
                    len(_adjE) == 1 and not _lapE and not _newE, True))
    _a1_moved = ("materializer", "current_status", ["retired", "active"],
                 ["active", "superseded", "retired", "unknown"])
    _adjL, _defL, _lapL, _newL = _dispose_arm1([_a1_moved])
    results.append(("ARM 1 LAPSES a suppression when the UNREACHED set moved",
                    len(_lapL) == 1 and not _adjL, True))
    _a1_new = ("no_such_record", "no_such_field", ["x"], ["x"])
    _adjN, _defN, _lapN, _newN = _dispose_arm1([_a1_new])
    results.append(("ARM 1 reports an UNRULED row as NEW, never suppressed",
                    len(_newN) == 1 and not _adjN, True))

    def _rejects1(entries):
        try:
            _validate_arm1_entries(entries)
            return False
        except ValueError:
            return True

    _good1 = {"r|f|admitted": {"class": "A", "values_at_adjudication": ["admitted"]}}
    results.append(("ARM-1 GUARD refuses a SUPERSET payload",
                    _rejects1({"r|f|admitted":
                               {"class": "A",
                                "values_at_adjudication": ["admitted", "candidate"]}}), True))
    results.append(("ARM-1 GUARD refuses a SUBSET payload",
                    _rejects1({"r|f|admitted,candidate":
                               {"class": "A", "values_at_adjudication": ["admitted"]}}), True))
    results.append(("ARM-1 GUARD refuses an unpermitted class",
                    _rejects1({"r|f|x": {"class": "Z", "values_at_adjudication": ["x"]}}), True))
    results.append(("ARM-1 GUARD refuses an unsorted/duplicated payload",
                    _rejects1({"r|f|a,a": {"class": "A", "values_at_adjudication": ["a", "a"]}}),
                    True))
    results.append(("ARM-1 GUARD ACCEPTS a sound 3-part entry (else every arm above is vacuous)",
                    not _rejects1(_good1), True))
    # ARITY IS THE ARM'S IDENTITY, both directions. A 4-part key in ARM 1's sidecar would silently
    # carry a discriminant column ARM 1 does not have; a 3-part key in ARM 4's would collapse two
    # arms onto one ruling. Neither guard may accept the other's shape.
    results.append(("ARM-1 GUARD refuses an ARM-4 shaped 4-part key",
                    _rejects1({"r|d|f|x": {"class": "A", "values_at_adjudication": ["x"]}}), True))
    results.append(("ARM-4 GUARD refuses an ARM-1 shaped 3-part key",
                    _rejects({"r|f|x": {"class": "A", "values_at_adjudication": ["x"]}}), True))

    # ---- R3-CVO-2 LINK GUARD. EVERY arm is built by mutating ONE FIELD of a REAL, currently
    # LINKED entry, never from a synthetic dict. Synthetic fixtures were the first version and
    # R3-DT-4's resolver broke them: with resolution enforced, an invented entry can no longer be
    # LINKED, so the "missing field -> ORPHAN" arms would have kept passing FOR THE WRONG REASON
    # (unresolvable, not field-missing) and the LINKED arm became unreachable. A control whose
    # baseline cannot reach the state under test measures nothing. The real entry is loaded in the
    # R3-DT-4 block below and reused here, so each arm isolates exactly its own variable.
    # ---- R3-DT-4 / 3.0.0_SA_CVO~X's CLOSURE-FAIL re-attack. The three link fields used to be
    # PRESENCE-checked; record_ref and ruled_at resolved to nothing, so a true digest beside two
    # invented strings suppressed a live row. These arms drive the RESOLVER against the real
    # records. CVO~X's acceptance bar, adopted verbatim: "Refutation must name code that resolves
    # the claimed record/commit; nonempty-field checks do not" -- _resolve_state + _record_blob.
    try:
        with open(ARM1_ADJUDICATION_PATH, "r", encoding="utf-8") as _fh:
            _a1 = json.load(_fh, object_pairs_hook=_no_dupes)["entries"]
        _rk = sorted(k for k in _a1 if _a1[k].get("class") == "A")[0]
        _real = _a1[_rk]
        _dg = _real["arm_digest"]
        # NON-VACUITY FIRST: if a real, current entry stops resolving, every refusal below is
        # meaningless and the gate has simply stopped suppressing.
        results.append(("RESOLVER accepts a REAL entry against the real record (non-vacuity)",
                        _link_state(_real, _dg) == "LINKED", True))
        results.append(("RESOLVER refuses CVO~X's exhibit: true digest, forged ref AND commit",
                        _link_state(dict(_real, record_ref="not-a-record-or-anchor",
                                         ruled_at="not-a-commit"), _dg) == "ORPHAN", True))
        # (b) forged commit. Unconditional now: the runner names a trusted root, so the object
        # database is reachable in the canonical gate too -- no environment-dependent branch and
        # no disclosed hole, which is the whole point of R3-CRO-15's contract.
        results.append(("(b) RESOLVER refuses a ruled_at that is not a commit",
                        _link_state(dict(_real, ruled_at="0" * 40), _dg) == "ORPHAN", True))
        results.append(("RESOLVER refuses a record_ref naming a file absent at ruled_at",
                        _link_state(dict(_real, record_ref="org/standards/isck/NOPE.md#rows-4,5"),
                                    _dg) == "ORPHAN", True))
        results.append(("RESOLVER refuses an anchor ABSENT from the record it names",
                        _link_state(dict(_real,
                                         record_ref="org/standards/isck/ARM1_ADJUDICATION.md"
                                                    "#rows-999"), _dg) == "ORPHAN", True))
        results.append(("RESOLVER refuses a record_ref carrying NO anchor at all",
                        _link_state(dict(_real,
                                         record_ref="org/standards/isck/ARM1_ADJUDICATION.md"),
                                    _dg) == "ORPHAN", True))
        # (a) the REAL sidecars must resolve LINKED -- asserted first, as the non-vacuity arm:
        # if it fails, every refusal below is meaningless and the gate merely stopped suppressing.
        # R3-CRO-15 CONTRACT CONTROLS (a)-(d), 1.0.0_SA_CTO~X 77275.
        # (d) CONTAMINATION -- the sharpest of the four. A path that EXISTS IN THE WORKING TREE
        # but is ABSENT at the entry's own ruled_at must NOT resolve. If this ever passes, the
        # resolver has gone back to reading the tree and every verdict at a pin is contaminated.
        results.append(("(d) CONTAMINATION: a record present in the WORKING TREE but absent at "
                        "ruled_at does NOT resolve",
                        _link_state(dict(_real,
                                         record_ref="org/standards/isck/"
                                                    "ROUND3_CHARTER.md#rows-4,5"),
                                    _dg) == "ORPHAN", True))
        # (e) 3.0.0_SA_CVO~X's ALIAS sub-root (77289). My 82efe0bb27 hotfix resolved the record
        # with os.path.basename(path), so ANY nonexistent declared path ending in the right
        # filename ALIASED the real record and resolved. f98f2d020b removed that whole code path
        # -- the declared path goes to `git show <ruled_at>:<path>` verbatim -- but a fix without
        # a control is one refactor away from returning, and this one reads as a tidy-up.
        for _alias in ("org/standards/isck/NOPE/ARM1_ADJUDICATION.md#rows-4,5",
                       "totally/made/up/ARM1_ADJUDICATION.md#rows-4,5",
                       "ARM1_ADJUDICATION.md#rows-4,5"):
            results.append(("(e) ALIAS: declared path %r absent at ruled_at is ORPHAN even though "
                            "its basename matches" % _alias.split("#")[0],
                            _link_state(dict(_real, record_ref=_alias), _dg) == "ORPHAN", True))

        # (c-bis) R3-DT-6's arm: swap the root WITHOUT clearing the cache and the verdict must
        # STILL be UNRESOLVED. Before the (root, ...) key this returned LINKED off the stale entry
        # -- a control passing on a cached answer to a question it never re-asked. Deliberately
        # populates the cache FIRST so the arm is reachable from the failing state.
        _saved_root_b = _repo_root
        try:
            _RECORD_CACHE.clear()
            _link_state(_real, _dg)                      # populate under the REAL root
            globals()["_repo_root"] = lambda: None       # swap root, DO NOT clear
            results.append(("(c-bis) a swapped root is NOT answered from the cache -- still "
                            "UNRESOLVED without an explicit clear()",
                            _link_state(_real, _dg) == "UNRESOLVED", True))
        finally:
            globals()["_repo_root"] = _saved_root_b
            _RECORD_CACHE.clear()

        # (c) no trusted root at all -> UNRESOLVED, NAMED, never LINKED.
        _saved_root = _repo_root
        try:
            globals()["_repo_root"] = lambda: None
            _RECORD_CACHE.clear()
            results.append(("(c) no ISCK_REPO_ROOT and no checkout -> UNRESOLVED, never LINKED",
                            _link_state(_real, _dg) == "UNRESOLVED", True))
        finally:
            globals()["_repo_root"] = _saved_root
            _RECORD_CACHE.clear()
        # field-presence arms, each ONE mutation of the same real entry that LINKS above
        for _f in LINK_FIELDS:
            _o = dict(_real)
            _o.pop(_f)
            results.append(("LINK GUARD calls a real entry missing %s an ORPHAN" % _f,
                            _link_state(_o, _dg) == "ORPHAN", True))
        results.append(("LINK GUARD treats an EMPTY link field as missing, not as present",
                        _link_state(dict(_real, record_ref=""), _dg) == "ORPHAN", True))
        results.append(("LINK GUARD calls a moved arm STALE (the value-set lapse generalized)",
                        _link_state(_real, "A_DIFFERENT_DIGEST") == "STALE", True))
        results.append(("LINK GUARD cannot call a DEAD-ARM entry LINKED against a real digest",
                        _link_state(dict(_real, arm_digest="ARM_ABSENT"), _dg) == "STALE", True))
        _op = dict(_real)
        _op.pop("ruled_at")
        results.append(("LINK GUARD reports ORPHAN, not STALE, when an entry is both",
                        _link_state(_op, "A_DIFFERENT_DIGEST") == "ORPHAN", True))
    except (OSError, ValueError, IndexError, KeyError) as exc:
        results.append(("RESOLVER arms are RUNNABLE (sidecar readable: %s)" % str(exc)[:40],
                        False, True))

    # And the digest itself must discriminate: same content -> same digest, moved content -> not.
    results.append(("ARM DIGEST is stable on identical normalized content",
                    _arm_digest({"a": [1, 2]}) == _arm_digest({"a": [1, 2]}), True))
    results.append(("ARM DIGEST MOVES when the arm's content moves (else it certifies nothing)",
                    _arm_digest({"a": [1, 2]}) != _arm_digest({"a": [1, 3]}), True))

    ok = True
    for label, got, want in results:
        good = got == want
        ok = ok and good
        if verbose:
            print("  [%s] %s: %s (expect %s)" % ("OK: " if good else "ERROR", label, got, want))
    return ok


# ------------------------------------------------------------------------------- main
def _repairs(V):
    """Companion-field repairs: a value whose conditional demands a partner field."""
    def device_local_binding(inst):
        inst["fabric_id"] = "laptop"
        return inst

    def device_local_generic(inst):
        inst["fabric_id"] = "laptop"
        inst["device_id"] = "some-laptop"
        return inst

    def invariant(inst):
        inst.pop("device_id", None)
        return inst

    def complete_bundle(inst):
        inst.pop("absent_components", None)
        for field in ("source_tree_digest", "dependency_lock_digest",
                      "configuration_digest", "declared_opinions_digest"):
            inst[field] = V.SHA
        inst["normalizer_versions"] = ["none_raw_v0"]
        inst["runtime_contract_version"] = "py39_v0"
        return inst

    def drop_fingerprint(inst):
        for field in ("fingerprint", "fingerprint_method", "normalization_version"):
            inst.pop(field, None)
        return inst

    def mismatch_evaluation(inst):
        inst["evidence_refs"] = ["evidence:content_digest_compare"]
        inst["delta_summary"] = "content_digest differs from target"
        return inst

    def contested_entity(inst):
        inst["adjudicated_by"] = "1.0.0_SA_CTO~X"
        return inst

    def closed_binding(inst):
        inst["valid_to"] = "commit:ffffffffff"
        return inst

    def contradicted_relation(inst):
        inst["evidence_refs"] = ["evidence:counter_observation"]
        inst["adjudicated_by"] = "1.0.0_SA_CTO~X"
        return inst

    def superseded_relation(inst):
        inst["superseded_by"] = "rel:" + ULID_A_OF(V)
        return inst

    def running_run(inst):
        inst.pop("completed_at", None)
        return inst

    def superseded_materializer(inst):
        inst["superseded_by_version"] = "matv:" + ULID_A_OF(V)
        return inst

    out = {
        ("entity_binding", "fabric_scope", "device_local"): device_local_binding,
        ("materializer_version", "bundle_completeness", "complete"): complete_bundle,
        # the seven the census carried as OPEN until this commit; all seven CLOSE,
        # census 66/73 -> 73/73, so the schema has NO structurally dead enum value.
        ("coherence_evaluation", "integrity", "mismatch"): mismatch_evaluation,
        ("entity", "current_status", "contested"): contested_entity,
        ("entity_binding", "status", "closed"): closed_binding,
        ("identity_relation", "verification_standing", "contradicted"): contradicted_relation,
        ("identity_relation", "verification_standing", "superseded"): superseded_relation,
        ("materialization_run", "run_status", "running"): running_run,
        ("materializer", "current_status", "superseded"): superseded_materializer,
    }
    def referent_fabric_local(inst):
        inst["referent_fabric_id"] = "laptop"
        inst.pop("referent_device_id", None)
        return inst

    def referent_device_local(inst):
        inst["referent_fabric_id"] = "laptop"
        inst["referent_device_id"] = "some-laptop"
        return inst

    def bridge_held(inst):
        inst["held_on"] = "ent:" + ULID_A_OF(V)
        inst.pop("store_owner", None)
        return inst

    def bridge_inadmissible(inst):
        inst["store_owner"] = "0.8.0_AE_CloudComp"
        inst.pop("held_on", None)
        return inst

    def bridge_rejected(inst):
        inst["adjudicated_by"] = "1.0.0_SA_CTO~X"
        inst.pop("held_on", None)
        inst.pop("store_owner", None)
        return inst

    def bridge_contradicted(inst):
        inst["evidence_refs"] = ["evidence:counter_observation"]
        inst["adjudicated_by"] = "1.0.0_SA_CTO~X"
        return inst

    def bridge_superseded(inst):
        # br:, not ent: -- a bridge is superseded by another BRIDGE. My first repair used the
        # entity prefix and ARM 3 correctly called the value UNREACHABLE rather than OPEN,
        # which is the distinction that told me the repair had been TRIED and had failed.
        inst["superseded_by"] = "br:" + ULID_A_OF(V)
        return inst

    def observation_absent(inst):
        # observed_absent asserts a MEASURED absence, so it carries its warrant and no fingerprint
        for field in ("fingerprint", "fingerprint_method", "normalization_version"):
            inst.pop(field, None)
        inst["evidence_refs"] = ["evidence:absence_probe"]
        return inst

    def observation_partial(inst):
        # partial asserts "I could not see all of it", so R2-2's cut makes it carry its warrant
        # (evidence_refs) exactly as observed_absent does -- R2-5's cell one step over. Without
        # this the shared drop_fingerprint repair leaves the warrant unsupplied and ARM 3 prints
        # a FALSE UNREACHABLE -- the precise error its own closing note exists to prevent.
        for field in ("fingerprint", "fingerprint_method", "normalization_version"):
            inst.pop(field, None)
        inst["evidence_refs"] = ["evidence:partial_read_warrant"]
        return inst

    def relation_retirement(inst):
        # R2-2's `retirement` is a UNARY relation -- it retires its subject and has no object,
        # so the arm FORBIDS object_serial rather than requiring a partner. The base fixture is
        # a binary candidate_equivalence and carries one; dropping it is the whole repair.
        # evidence_refs stays: claim_origin `rule_derived` still owes its warrant.
        inst.pop("object_serial", None)
        return inst

    out[("identity_relation", "relation_type", "retirement")] = relation_retirement
    def coherence_latest_authority(inst):
        # sec 3.13: latest_authority is the only policy that RESOLVES at read time, so it owes the
        # head it resolved to; the three pinned policies forbid these fields.
        inst["resolved_target_ref"] = "nessie:main"
        inst["resolved_target_version"] = "snapshot:8601547680771488785"
        return inst

    def surface_published(inst):
        # sec 3.26: published is a PROMOTION claim -- it owes where, when, by whom, and evidence.
        inst["published_ref"] = "kuzu:prod/current"
        inst["published_at"] = V.TS2
        inst["promoted_by"] = "0.7.0_AE_CloudOps"
        inst["promotion_evidence_refs"] = ["deploy:kuzu-prod@" + V.TS2]
        return inst

    out[("coherence_evaluation", "target_policy", "latest_authority")] = coherence_latest_authority
    out[("surface_version", "publication_state", "published")] = surface_published
    def contest_lifecycle_target(inst):
        # R4: contest_event's target is a TYPED one-of. The lifecycle_event kind owes
        # target_event_id and FORBIDS the entity/binding targets -- a contest that names two
        # targets names none, so the repair must drop the base fixture's entity target rather
        # than merely add the event one.
        inst["target_event_id"] = "lce:" + ULID_A_OF(V)
        inst.pop("target_entity_serial", None)
        inst.pop("target_binding_id", None)
        return inst

    def lifecycle_decommissioned(inst):
        # R4: a decommission is TERMINAL -- there is no successor version by definition, so
        # superseding_version_id is forbidden. Mirrors materializer.current_status=retired,
        # which carries no successor obligation for the same reason.
        inst.pop("superseding_version_id", None)
        return inst

    def _contest_event_target(prefix):
        # R4-CRO-2 widened target_kind to five values. The three EVENT kinds share one shape --
        # require target_event_id, forbid the entity AND binding targets -- but each constrains
        # the id to its OWN prefix (lce: / bev: / aep:), so a single generic repair would satisfy
        # the require limb and fail the pattern. The prefix is the arm's identity, not decoration.
        def repair(inst):
            inst["target_event_id"] = prefix + ULID_A_OF(V)
            inst.pop("target_entity_serial", None)
            inst.pop("target_binding_id", None)
            return inst
        return repair

    out[("contest_event", "target_kind", "binding_event")] = _contest_event_target("bev:")
    out[("contest_event", "target_kind", "authority_epoch_event")] = _contest_event_target("aep:")
    out[("contest_event", "target_kind", "lifecycle_event")] = contest_lifecycle_target
    out[("lifecycle_event", "event_kind", "materializer_decommissioned")] = lifecycle_decommissioned
    out[("bridge_assertion", "registry_standing", "held")] = bridge_held
    out[("bridge_assertion", "registry_standing", "inadmissible")] = bridge_inadmissible
    out[("bridge_assertion", "registry_standing", "rejected")] = bridge_rejected
    out[("bridge_assertion", "verification_standing", "contradicted")] = bridge_contradicted
    out[("bridge_assertion", "verification_standing", "superseded")] = bridge_superseded
    out[("state_observation", "failure_state", "observed_absent")] = observation_absent
    for rtype in ("entity_binding", "state_observation"):
        out[(rtype, "referent_scope", "fabric_local")] = referent_fabric_local
        out[(rtype, "referent_scope", "device_local")] = referent_device_local
    for rtype in ("state_observation", "materialization_run"):
        out[(rtype, "fabric_scope", "device_local")] = device_local_generic
        out[(rtype, "fabric_scope", "fabric_invariant")] = invariant
    out[("state_observation", "failure_state", "partial")] = observation_partial
    for value in ("substrate_unavailable", "instrument_error", "not_applicable"):
        out[("state_observation", "failure_state", value)] = drop_fingerprint

    # R2-2 (c): contest_event's base fixture is the OPENED half (entity target); every other
    # value is reached by moving to the resolved half or the binding target
    def contest_resolved(inst):
        # setdefault, never assign: ARM 3 has already placed the value under test on `outcome`,
        # and a repair that overwrote it would test `dismissed` three times and call
        # upheld/merged dead -- the cross-arm control above FIRED on exactly that draft
        inst["event_kind"] = "resolved"
        inst.setdefault("outcome", "dismissed")
        inst["adjudicated_by"] = "3.0.0_SA_CVO~X"
        inst.pop("consequence_refs", None)
        return inst

    def contest_with_consequence(inst):
        inst = contest_resolved(inst)
        inst["consequence_refs"] = ["rel:" + ULID_A_OF(V)]
        return inst

    def contest_merged(inst):
        # round-3 REWORK-2: a merge names its SURVIVOR by a typed field, and carries no
        # consequence of its own (the survivor does)
        inst = contest_resolved(inst)
        inst["surviving_contest_id"] = "ct:" + ULID_A_OF(V)
        return inst

    def contest_binding_target(inst):
        inst["target_binding_id"] = "bind:" + ULID_A_OF(V)
        inst.pop("target_entity_serial", None)
        return inst

    out[("contest_event", "event_kind", "resolved")] = contest_resolved
    out[("contest_event", "outcome", "dismissed")] = contest_resolved
    out[("contest_event", "outcome", "upheld")] = contest_with_consequence
    out[("contest_event", "outcome", "merged")] = contest_merged
    out[("contest_event", "target_kind", "binding")] = contest_binding_target
    return out


def ULID_A_OF(V):
    """The battery's canonical test ULID, read from the battery rather than duplicated here."""
    return V.ULID_A


def main():
    sys.path.insert(0, HERE)
    import validate_isck as V

    with open(SCHEMA_PATH, "r", encoding="utf-8") as handle:
        schema = json.load(handle)

    gaps, unparsed = arm_coverage(schema)
    kw_fail, field_fail, unscoreable = arm_attribution(schema, V.FIXTURES, V._mutants())
    dead, open_values = arm_inhabitability(schema, V.FIXTURES, _repairs(V))
    unpaired, unpaired_unparsed = arm_paired(schema)
    controls_ok = self_controls(schema, V.FIXTURES, _repairs(V))

    print()
    print("=" * 94)
    findings = bool(gaps or unparsed or kw_fail or field_fail or unscoreable or dead
                    or unpaired or unpaired_unparsed)
    print("RESULT: %s" % ("FINDINGS PRESENT" if findings else "CLEAN"))
    print("  ARM 1 coverage gaps       : %d   unparsed constructs: %d" % (len(gaps), len(unparsed)))
    print("  ARM 2 keyword failures    : %d   field failures: %d   unscoreable: %d"
          % (len(kw_fail), len(field_fail), len(unscoreable)))
    print("  ARM 3 unreachable values  : %d   open (no repair): %d" % (len(dead), len(open_values)))
    print("  ARM 4 require-only arms   : %d   unparsed then-clauses: %d"
          % (len(unpaired), len(unpaired_unparsed)))
    print("  SELF-CONTROLS             : %s" % ("PASS" if controls_ok else "FAIL"))
    print("  NOTE: ARM 1 and ARM 4 emit CANDIDATES, not findings -- adjudicate before reporting.")
    print("=" * 94)
    # Findings are the PRODUCT of this tool, not a crash. Only a broken instrument exits non-zero.
    return 0 if controls_ok else 1


if __name__ == "__main__":
    sys.exit(main())
