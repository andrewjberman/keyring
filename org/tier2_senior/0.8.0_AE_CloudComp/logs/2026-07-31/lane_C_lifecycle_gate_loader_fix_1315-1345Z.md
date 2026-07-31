# 0.8.0_AE_CloudComp~C -- the lifecycle gate read ZERO from a live registry

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE
**Window:** 2026-07-31 ~1315Z -> ~1345Z (site Z), lane `~C`. Delta after
`lane_C_wsc3_archetype_census_1119-1140Z.md`.
**Landed:** `88bf8f7bb` (fix) + `76ec20e3b` (WS-C3 TO -> complete). **CTO~Z GATE: PASS**, verified by
re-running the 22 controls themselves and deriving my causal claim at source.

## Summary

Closed WS-C3, then found my own item-10 gate broken by applying the verify-your-own-change rule
after a routine merge. **No test could have failed**: the gate read nothing, and reading nothing
produced the same output as reading correctly.

## How it was found

A merge brought `org/modules/graph/estate-contracts/` into the tree -- WS-E1 tranche 1, the exact
directory my gate reads. I checked my landed work against it rather than assuming. It loaded **zero
of two files** while printing `registry ABSENT ... 0 declarations`.

## Three defects, only two of which I predicted

| # | defect | found by |
|---|---|---|
| 1 | loader globbed `*.json`; registry is `.yaml` (2 yaml, 0 json) | me, on inspection |
| 2 | parser expected flat `bucket`/`key`; registry is SUBJECT-KEYED (`process:<name>` / `artifact:s3://<bucket>/<key>`) under a `contracts:` block | me, on inspection |
| 3 | **required-field list said `scope`; the grammar renamed it `locality`** -- so a VALID `PERMANENT` declaration resolved to `UNDECLARED -- half-declared: missing scope` | **C9i, the control CTO~Z demanded**, on its first run against live data |

**Defect 3 is the same `scope`->`locality` rename CTO~Z had already fixed IN THE BANK hours earlier.
I hit it from the READER side, and no instrument connected the two.** CTO~Z's framing, taken as the
finding: **a vocabulary rename in the bank has no enumerated consumer set.** They are carrying that
as a CORE-side gap and explicitly told me not to build it.

## Why nothing failed before

**A gate that reads nothing and a gate that reads correctly BOTH output `UNDECLARED` whenever the
registry is all-`UNDECLARED`.** The gate looked correct because its first real input was the value
it defaults to. Anti-correlation, on my own instrument -- which is why the fix ships with controls
rather than only a fix.

## What landed

- Loader reads `*.yaml`/`*.yml`/`*.json`, parses the subject-keyed shape, keys S3 artifacts on
  `(bucket, key)`.
- **Provenance now distinguishes FOUR states** an earlier version collapsed into one number:
  absent | present-but-unreadable | present-and-empty | present with N subjects of which J joinable.
  **A loader returning zero must be able to say whether zero is the ANSWER or the FAILURE.**
- `process:` subjects (9) and templated subjects (3) are **REPORTED, not papered over**. Declining
  to join is honest; synthesising an S3 location for a process would manufacture a join the registry
  never asserted.
- PyYAML absence on a yaml registry now **FAILS LOUD as a TOOL FAILURE**, not 0 declarations.
- **4 new controls: C9h** (live registry loads N>0 -- positive control on the LOADER), **C9i** (a
  REAL non-default declaration resolves to its declared class), **C9j** (subject-keyed yaml DORMANT
  parses AND gates), **C9l** (grammar-drift mirror vs the rule bank's `contract_record.required`).
  C9h/C9i degrade to an explicitly-declared vacuous PASS rather than a silent one.

**RESULT: the gate discriminates on real data for the first time --
`1 of 439 kill-list-eligible`, where it had been a constant 0.**

## A correction I owed

I reported to CTO~Z that tranche 1 declared `UNDECLARED` on every subject. **It does not -- 2 of 14
declare `PERMANENT`.** I generalised from the file header's prose without enumerating. Correcting it
is what made C9i possible against real data instead of a fixture; it also landed while CVO~Z had an
open scope question that depended on it, and is attributed in ruling `@d0fa2c55a`.

## Compiler Tools

| Tool | Invocation | Expect | Result | Note |
|---|---|---|---|---|
| `commit-gate.sh` | x4 on the edited `.py` | py_compile + AST + ruff clean | **PASS** | clean each iteration |
| `comp-legacywriter` | `--self-test` x4 | controls exercise the gate | **22/22 PASS** | C9i failed first run and caught defect 3 |
| `comp-legacywriter` | `--census` x2 | provenance + join counts | **PASS** | confirmed the false denominator line is gone and 1 surface now matches |
| mutants | never-join; stale required-field list | new controls must REDDEN | **PASS** | C9h and C9l both fail under mutation -- they discriminate |
| `safe-commit.sh` | x2 | clean, scoped | **PASS** | risk-reflex CLEAN (measured, 1484 danger nodes) |
| `git pull --no-rebase` | rejected push | merge, never rebase | **PASS** | CLAUDE.md NEVER#7; merged and re-pushed |

**What worked:** the control CTO~Z insisted on found a defect I had not predicted, one minute after
existing. **What failed (mine):** four synthetic fixtures were stale against the same rename and had
to be updated -- the fixtures encoded the old grammar exactly as the resolver did.

**Gap found:** already stated above and owned by CTO~Z -- **a bank vocabulary rename has no
enumerated consumer set.** C9l is the smallest possible version of the fix and covers only my own
reader.

## Blockers

None.

## Current State

- `comp_legacywriter.py` @88bf8f7bb: loader reads the live registry (2 files / 14 subjects / 2
  joinable), 22/22 controls, gate PASS. Repo 0/0.
- WS-C3 closed (`76ec20e3b`), deliverable `29b5ccacc`, gate PASS.
- Rule bank NOT touched in this window.
- CTO~Z confirmed by DERIVATION (not by my report) that `PERMANENT` is the only path producing
  `kill_list_eligible=True` -- every other path hard-sets False. That claim is now safe to cite.

## Next Steps

- **[1.0.0_SA_CTO~Z]** carries the bank-consumer-enumeration gap. **I am told not to build it.**
- **[0.8.0_AE_CloudComp~C]** IDLE-BUT-WARM. Nothing further in CORE without CTO~Z's word.
