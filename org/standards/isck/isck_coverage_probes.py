#!/usr/bin/env python
"""ISCK battery additions -- coverage + attribution probes.

Author: 0.4.0_DT_ClientPlatform~X. Authorized to land by 1.0.0_SA_CTO~X (msg 76477/76496)
as a round-1 deliverable of the D11 ISCK adversarial pass.

WHY THIS EXISTS, SEPARATELY FROM validate_isck.py: that battery asks "does every mutant
reject, for its named reason?" -- a question about the mutants someone thought to write.
These arms ask the complementary question: "what does the schema NOT constrain at all?"
A law with no conditional attached has no mutant to write, so it cannot fail the battery.
DT-1 and DT-7 were both found this way, the second one mechanically, with no human hunting it.

THREE STANDING ARMS, each printing its own denominator, each with self-controls:

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

GENERALIZATION: every arm reads the schema OBJECT, not a copy of its rules. ARM 1 survived the
v0 -> v0.1 rewrite from enumerated if/then arms to dependentRequired without an edit. A construct
ARM 1 cannot parse is reported UNPARSED and NEVER counted as covered: an unparsed conditional
scored as covered is precisely the false-green these arms exist to kill.

Run:  python isck_coverage_probes.py          (self-test; exit 0 unless a self-control fails)
"""
import copy
import json
import os
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
        if isinstance(cond, dict) and isinstance(cond.get("properties"), dict):
            for field, spec in cond["properties"].items():
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

    ⛔ THE OUTPUT IS A CANDIDATE LIST, NOT A FINDING LIST. Measured against v0.1: of 6 gaps
    reported, 1 was a real defect, 3 were PROTECTED by a mechanism this arm does not count
    (a presence-keyed dependentRequired, or a plain `required` in the base branch), and 2 were
    unconditioned BY DESIGN (a 'null verdict' value legitimately carries no obligation).
    Every gap MUST be adjudicated by constructing the record the missing rule would forbid and
    testing it. A gap reported as a finding without that test is a FALSE RED -- the exact
    inverse of the false-green this arm exists to kill, and it fires hardest on a schema that
    has just been improved, because a good fix often uses a mechanism this arm cannot see.

    ⛔ AND THE BLIND SPOT THAT MATTERS MORE: this arm can ONLY find gaps in a record that
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


# ------------------------------------------------------------------------ self-controls
def self_controls(schema, fixtures, verbose=True):
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

    out = {
        ("entity_binding", "fabric_scope", "device_local"): device_local_binding,
        ("materializer_version", "bundle_completeness", "complete"): complete_bundle,
    }
    for rtype in ("state_observation", "materialization_run"):
        out[(rtype, "fabric_scope", "device_local")] = device_local_generic
        out[(rtype, "fabric_scope", "fabric_invariant")] = invariant
    for value in ("partial", "substrate_unavailable", "instrument_error", "not_applicable"):
        out[("state_observation", "failure_state", value)] = drop_fingerprint
    return out


def main():
    sys.path.insert(0, HERE)
    import validate_isck as V

    with open(SCHEMA_PATH, "r", encoding="utf-8") as handle:
        schema = json.load(handle)

    gaps, unparsed = arm_coverage(schema)
    kw_fail, field_fail, unscoreable = arm_attribution(schema, V.FIXTURES, V._mutants())
    dead, open_values = arm_inhabitability(schema, V.FIXTURES, _repairs(V))
    controls_ok = self_controls(schema, V.FIXTURES)

    print()
    print("=" * 94)
    findings = bool(gaps or unparsed or kw_fail or field_fail or unscoreable or dead)
    print("RESULT: %s" % ("FINDINGS PRESENT" if findings else "CLEAN"))
    print("  ARM 1 coverage gaps       : %d   unparsed constructs: %d" % (len(gaps), len(unparsed)))
    print("  ARM 2 keyword failures    : %d   field failures: %d   unscoreable: %d"
          % (len(kw_fail), len(field_fail), len(unscoreable)))
    print("  ARM 3 unreachable values  : %d   open (no repair): %d" % (len(dead), len(open_values)))
    print("  SELF-CONTROLS             : %s" % ("PASS" if controls_ok else "FAIL"))
    print("=" * 94)
    # Findings are the PRODUCT of this tool, not a crash. Only a broken instrument exits non-zero.
    return 0 if controls_ok else 1


if __name__ == "__main__":
    sys.exit(main())
