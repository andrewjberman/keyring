#!/usr/bin/env python3
"""Declare-time lint for D3 contract_record instances (NFRA_VELOCITY, CVO~Z Amendment 7 / A7.1).

THE INVARIANT (A7.1): every vocabulary token in a declared contract must RESOLVE against the
ratified rule bank. An unresolvable token is a gap-naming leak and is REJECTED at declare-time.
This is a GATE (it rejects), not notification machinery -- moratorium-clear per CVO~Z 075026Z.

WHAT IT CHECKS
  1. FIELD NAMES  against contract_record.required / .optional  (an added term is REJECTED --
     "CORE fixes the vocabulary; ESTATE WS-E1 declares INSTANCES against it and adds no terms")
  2. REQUIRED FIELDS present
  3. ENUMERATED VALUES against their ratified sets:
       lifecycle_class -> lifecycle.enum
       obligation      -> obligation_types keys
       locality        -> lifecycle.locality_binding.enum, and ONLY IF the bank's
                          `enum_is_lint_checked` says YES (A11 branch (a), ratified by the RAIL
                          AUTHOR @4b9714d5c -- never synthesised here). The marker is READ, so a
                          field ratified free-text under branch (b) cannot be value-checked even
                          if it later grows an enum-shaped key.
     A LEGAL FIELD CARRYING AN ILLEGAL VALUE IS EXACTLY THE CASE THIS CATCHES. It was reported to
     the gate as undetectable-by-any-mechanical-check; it is not, and this is where that is proven.

WHAT IT DOES *NOT* CHECK -- SHIPPED WITH THE FLOOR SO THE FLOOR CANNOT READ AS THE TARGET (A7.2)
  - It catches only the LEXICAL half. A gap can be named entirely in ratified vocabulary
    ("no D3 class for X" uses only legal tokens) and passes cleanly.
    DESCRIBE-THE-SPECIMEN-NEVER-THE-GAP REMAINS THE GOVERNING DISCIPLINE. This is the mechanical
    floor UNDER that discipline, never a replacement for it.
  - A7.3 SEMANTIC DRIFT IS NOT COVERED AND IS NOT RETIRED BY THIS TOOL. A ratified token used in a
    sense D3 never licensed resolves perfectly here. Note the two drifts are DIFFERENT:
        BANK-MOVEMENT drift : bank moves under a stationary declaration -> pin/HEAD DELTA NON-ZERO
                              (this tool reports it)
        A7.3 SEMANTIC drift : declaration drifts under a stationary bank -> pin and HEAD BOTH
                              resolve, DELTA EXACTLY ZERO -> INVISIBLE HERE BY CONSTRUCTION
    Never describe this tool as carrying "a drift signal" unqualified: that sentence retires a
    residual it does not close, and a retired-but-open residual is worse than a named one.

THE PIN IS RESOLVED TWICE, DELIBERATELY
  A pin that nothing re-checks is a frozen map with a version number on it -- the defect that left
  seven SDK artifacts six versions stale. So:
      at PIN  -> "was this declaration VALID WHEN MADE" (immutable; makes the lint reproducible)
      at HEAD -> "is it VALID NOW"
  and the DELTA is the bank-movement signal. Both are always reported.

NO CACHING. Vocabulary is resolved from the rule bank per run and never persisted. A cached
vocabulary IS the frozen enumeration returning with a performance justification instead of a design
one -- the M3 defect (434 contracted verdicts miscounted FAIL; an 8.5%-vs-0.87% error in the
program's own measurement of itself). It will be proposed by someone helpful who has never read M3.
This prohibition carries its own reason so it cannot be optimized away by a reader who lacks it.

Exit: 0 = PASS, 2 = REJECT (a real declare-time refusal), 1 = tool error (never a verdict).
"""
from __future__ import annotations

import subprocess
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: pyyaml required", file=sys.stderr)
    sys.exit(1)

RULE_BANK = "org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml"


def load_bank_at(ref: str | None):
    """Read the rule bank at a git ref, or from the worktree when ref is None.

    NEVER discards stderr on a `git show <ref>:<path>`: an MSYS-mangled ref prints `fatal:` to
    stderr and returns CLEAN EMPTY stdout, which would render "vocabulary absent" out of a broken
    retrieval and reject every token in the file.
    """
    if ref is None:
        with open(RULE_BANK, encoding="utf-8") as fh:
            return yaml.safe_load(fh)
    proc = subprocess.run(
        ["git", "show", "%s:%s" % (ref, RULE_BANK)],
        capture_output=True, text=True,
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        raise RuntimeError(
            "rule bank unreadable at ref %r (rc=%d): %s"
            % (ref, proc.returncode, (proc.stderr or "").strip()[:200])
        )
    return yaml.safe_load(proc.stdout)


def vocab(bank):
    """Extract the ratified vocabulary. Fails LOUD if the shape is not what we expect --
    a silently-empty vocabulary would reject everything and read like a corpus-wide violation."""
    rails = bank.get("dynamic_rails", {}) or {}
    d3 = rails.get("D3_contract_obligation", {}) or {}
    rec = d3.get("contract_record") or {}
    life = d3.get("lifecycle") or {}
    ob = d3.get("obligation_types") or {}

    # UN-LINTABLE FIELDS ARE READ FROM THE BANK, NOT ASSUMED.
    # The bank marks free-text fields "NOT LINT-CHECKED" (CVO~Z A10.2). Until this block existed
    # the lint skipped them only INCIDENTALLY -- because it happened to value-check just two fields
    # -- so the correct behaviour was an ACCIDENT OF SCOPE, and the next value-check added would
    # have silently started linting prose. CVO~Z's own condition names the failure: "a free-text
    # field that is NOT DECLARED un-lintable WILL EVENTUALLY BE LINTED, manufacturing exactly the
    # noise the A9 sequence exists to avoid." Reading the marker makes the exclusion STRUCTURAL:
    # a future value-check cannot reach a field the bank has declared non-vocabulary.
    fields = rec.get("fields") or {}
    unlintable = {
        name for name, desc in fields.items()
        if isinstance(desc, str) and "NOT LINT-CHECKED" in desc.upper()
    }

    # LOCALITY (A11, CTO~Z branch (a) @4b9714d5c) -- value-checked ONLY IF THE BANK SAYS SO.
    # The bank carries `enum_is_lint_checked` beside the enum; we READ it rather than assume, the
    # same way `unlintable` is read. That makes the A11 (a)-vs-(b) branch STRUCTURAL: a field
    # ratified as free-text (branch b) cannot be value-checked here even if it grows an enum-shaped
    # key, and a field ratified as checked (branch a) is checked without anyone editing this file's
    # policy. NOTE this is an ADDITIVE code change -- field NAMES resolve dynamically from the
    # bank, but VALUE enums are extracted by explicit key, so a NEW enum does NOT auto-wire itself.
    # (That distinction was over-generalized in relay as "no code change"; it is true of the rename,
    # false of a new enum.)
    lb = life.get("locality_binding") or {}
    lb_checked = str(lb.get("enum_is_lint_checked") or "").strip().upper().startswith("YES")
    locality_enum = set(lb.get("enum") or []) if lb_checked else set()

    v = {
        "required": set(rec.get("required") or []),
        "optional": set(rec.get("optional") or []),
        "lifecycle_enum": set(life.get("enum") or []),
        "obligation_types": set(ob.keys()),
        "unlintable": unlintable,
        "locality_enum": locality_enum,
    }
    for k, val in v.items():
        # legitimately empty: a bank need not declare free-text fields, and a field ratified
        # NOT-lint-checked (A11 branch b) correctly yields an empty locality oracle.
        if k in ("unlintable", "locality_enum"):
            continue
        if not val:
            raise RuntimeError(
                "vocabulary component %r resolved EMPTY -- refusing to lint against an empty "
                "oracle (that would reject every token and look like a corpus-wide violation)" % k
            )
    return v


def lint_record(rec: dict, key: str, v: dict) -> list[str]:
    out = []
    keys = set(rec.keys())
    for missing in sorted(v["required"] - keys):
        out.append("%s: MISSING REQUIRED FIELD %r" % (key, missing))
    for extra in sorted(keys - v["required"] - v["optional"]):
        out.append(
            "%s: UNRATIFIED TERM %r -- ESTATE declares INSTANCES and ADDS NO TERMS" % (key, extra)
        )
    # STRUCTURAL EXCLUSION: a field the bank declared non-vocabulary is never value-checked.
    # Guarded at each value-check below rather than in a sweep, so the exclusion is impossible to
    # bypass by ADDING a check -- a new value-check that forgets `unlintable` is the failure mode,
    # and the guard has to live where the check lives.
    unlintable = v.get("unlintable", set())

    lc = rec.get("lifecycle_class")
    if "lifecycle_class" not in unlintable and lc is not None and lc not in v["lifecycle_enum"]:
        out.append(
            "%s: lifecycle_class %r DOES NOT RESOLVE (ratified: %s)"
            % (key, lc, sorted(v["lifecycle_enum"]))
        )
    loc = rec.get("locality")
    if v.get("locality_enum") and "locality" not in unlintable             and loc is not None and loc not in v["locality_enum"]:
        out.append(
            "%s: locality %r DOES NOT RESOLVE (ratified: %s)"
            % (key, loc, sorted(v["locality_enum"]))
        )
    ob = None if "obligation" in unlintable else rec.get("obligation")
    if ob is not None:
        for tok in (ob if isinstance(ob, list) else [ob]):
            if tok not in v["obligation_types"]:
                out.append(
                    "%s: obligation %r DOES NOT RESOLVE -- a LEGAL FIELD carrying an ILLEGAL "
                    "VALUE (ratified: %s)" % (key, tok, sorted(v["obligation_types"]))
                )
    return out


def find_records(obj, v, path=""):
    """Yield (path, record) for anything shaped like a contract_record."""
    if isinstance(obj, dict):
        if v["required"] & set(obj.keys()):
            yield (path or "<root>", obj)
            return
        for k, val in obj.items():
            yield from find_records(val, v, "%s/%s" % (path, k))
    elif isinstance(obj, list):
        for i, val in enumerate(obj):
            yield from find_records(val, v, "%s[%d]" % (path, i))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        print("usage: contract_declare_lint.py <declaration.yaml> [--pin <git-ref>]",
              file=sys.stderr)
        return 1
    target = argv[1]
    pin = None
    if "--pin" in argv:
        pin = argv[argv.index("--pin") + 1]

    with open(target, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)

    results = {}
    for label, ref in (("PIN(%s)" % (pin or "none"), pin), ("HEAD", None)):
        v = vocab(load_bank_at(ref))
        findings = []
        n = 0
        for key, rec in find_records(doc, v):
            n += 1
            findings.extend(lint_record(rec, key, v))
        results[label] = (n, findings)
        print("== %s == records=%d findings=%d" % (label, n, len(findings)))
        for f in findings:
            print("   REJECT  %s" % f)

    labels = list(results)
    pin_n, pin_f = results[labels[0]]
    head_n, head_f = results[labels[1]]
    if pin is not None and len(pin_f) != len(head_f):
        print("\n** BANK-MOVEMENT DELTA: pin findings=%d, HEAD findings=%d -- the RULE BANK moved "
              "under a stationary declaration (non-additive change). This is BANK-MOVEMENT drift "
              "ONLY; A7.3 semantic drift has delta EXACTLY ZERO and is NOT covered here."
              % (len(pin_f), len(head_f)))

    # THE VERDICT IS CARRIED IN STDOUT, NOT IN rc.
    # This host has a DOCUMENTED rc-corruption class (MSYS shared-memory mount, not reboot-durable;
    # "score controls on OUTPUT, never rc"). A GATE whose verdict rides only on an exit code FAILS
    # OPEN wherever that code is corrupted -- and a gate that fails open is worse than no gate,
    # because it is believed. Reported live by 0.7.0_AE_CloudOps~D, who saw REJECTED output return
    # rc=0 and correctly scored the OUTPUT instead.
    # CONSUMERS MUST MATCH THE `VERDICT:` LINE. rc is a convenience, never the contract.
    if pin_f or head_f:
        print("\nVERDICT: REJECT")
        print("RESULT: REJECTED at declare-time (A7.1).")
        print("NOTE: this is the LEXICAL floor only. Describe-the-specimen-never-the-gap remains "
              "the governing discipline; a clean run is NOT clearance.")
        return 2
    print("\nVERDICT: PASS")
    print("RESULT: PASS (lexical floor only -- NOT clearance; A7.3 semantic drift is uncovered "
          "and remains a named open residual).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
