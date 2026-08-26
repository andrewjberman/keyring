# CERT -- `ADVI_STITCH.TO-A1-DS` proof instance

**Certifier:** `3.0.0_SA_CVO` · **Date:** 2026-08-26T03:1xZ · **Verdict: CERTIFIED**
**Subject:** ONE task order's proof instance from ONE lane --
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_STITCH.TO-A1-DS_PROOF_OF_SPEC.json`
**Assignee:** `0.4.0_DS_ClientPlatform~Q` · closed @`2c7b221027`

---

## 1. RUN AT MY OWN SEAT

```
proof-of-spec-check | acceptance rows=13 | violations=0
  alignment-forward-1  (criterion -> cell):        13/13 criteria carry >=1 cell_ref
  alignment-forward-2  (cell_ref -> decomp):       22/22 distinct cell_refs resolve
  alignment-backward   (declared cell -> criterion): 22/22 declared cells reachable
  WARN lines: 0
VALID   rc=0
```

⚠ **THE `WARN: 0` IS LOAD-BEARING AND IS NEW AS OF TONIGHT.** This instance was re-run AFTER
`e89469a25c`, which annotates alignment figures computed on a structurally invalid instance --
because the alignment lines are **byte-identical** between a VALID and an INVALID run. **Quoting
"13/13, 22/22, 22/22" is only meaningful beside the verdict**, and on this instance the verdict is
VALID with the annotation absent. *(That defect was surfaced by this same assignee, against my tool,
in the course of this very TO.)*

---

## 2. LAYER 5 -- THE JUDGMENT THE CHECKER DECLINES TO MAKE

**Method: the D1 method, not the general one.** The grammar is hardcoded for this project and a
positive control is run -- because my attempt at a *general* cross-project cell extractor failed its
own validation tonight (0 against a known 31 on one decomp, 2.6x over-capture on another).

```
  decomp id space                                    32
  claimed by >=1 ADVI_STITCH TO                      23
  UNCLAIMED                                           9
  POSITIVE CONTROL  STI-b-4    9 mentions across the 2 TOs
                    STI-inv-1 10 mentions           -> the scan CAN return non-zero
```

**8 of the 9 are correctly out of Phase A**, and the decomp says so on their own lines:
`STI-g-1` `g-2` `g-3` `g-4` are **explicitly labelled PHASE B**; `g-5` `g-6` are Phase-B-shaped by
content (out-of-territory recording; re-deriving BD's calculated performance, where BD stays the
parity ORACLE); `STI-e-1` is a **cross-project consumer edge** (`ADVI_PERFRP` reads the seam, so it
belongs to that project's cells, not this TO); `STI-e-2` is the Fidelity sequencing edge, gated on
Phase B's re-adjudication.

### ⛔ THE NINTH IS `STI-inv-6`, IT IS A **CVO-CLASS CONTROL**, AND NO TO CARRIED IT

> **`STI-inv-6` -- FIRM + ACCOUNT-SET SEPARATION: 49F only; 08242234 rows are EVIDENCE, NEVER A
> SUBSTITUTE for 08335338** (PRD s.3, standing NEVER-SUM / NEVER-SUBSTITUTE).
> Oracle: *"CVO-class control - no 08242234 key in any landed path or census input; the two account
> sets never summed."*

**The decomp assigned this control to MY class and it was never cut into a task order.** Not the
assignee's gap -- **an uncarried cell is invisible to every downstream check, because every check
joins on the criteria** (the join-hole family, and this is a live instance of it).

**SO I EXECUTED IT RATHER THAN NOTING IT.** Read 2026-08-26T03:14:17Z:

```
  bronze_legacy    08242234 keys: 0  of   931
  silver_legacy    08242234 keys: 0  of 7,921
  gold/advi/reference  ..... : 0  of 7,283
  POSITIVE CONTROL  s3://opal-data-assets/schwab/08242234/  ->  17,378 keys
```
**The token is emphatically findable, so the three zeros are MEASURED ABSENCES, not dead filters.**
**`STI-inv-6`'s PATH arm HOLDS across all three landed planes -- 16,125 objects, zero crossings.**

**WHAT I DID *NOT* VERIFY, stated so this is not read wider:** the oracle's second half -- *"the two
account sets never summed"* -- is a claim about COMPUTATION, not paths. **Nothing above tests it.**
It needs a read of the census inputs and the summation sites, and **it remains uncarried.**

⚠ **AND IT IS LIVE RIGHT NOW:** `STI-inv-6` is the invariant governing the open
`08335338`/`08242234` composition question -- whether the account-number path segment is a scope
boundary at all. **If that segment is ruled NOT a boundary, this invariant loses its mechanical
carrier and is enforced by prose alone.** The two questions are the same question and should not be
settled separately.

---

## 3. WHAT THIS CERT DOES **NOT** SAY

1. **It does not certify Phase A as complete** -- it certifies ONE instance from ONE lane.
2. **It does not discharge `STI-inv-6`.** Its path arm is measured and holds; its summation arm is
   **UNMEASURED and UNOWNED.**
3. **It does not adjudicate the `AC10` UNCOMPUTABLE row** -- scored at its weakest layer per the
   issuer's own 70416 law, with `STI-d-3` discharged and `STI-d-4` blocked, named rather than averaged.
4. **It does not assert the MIGRATED class** for the 541 renumbered accounts. The old->new pairs are
   emitted as EVIDENCE; the class is Phase B and the assignee correctly declined to assert it.

---

## 4. NOTED IN THE ASSIGNEE'S FAVOUR

They **modelled their first instance on a peer's file instead of on the schema**, got 14 violations
including eleven missing required properties, rebuilt against the schema -- and then reported the
part nobody would have asked for: **the alignment layers had passed on the broken attempt too,
identically.** That produced a real fix to my instrument.
They also **took the sanctioned path over the audited override** when the system gate blocked their
commit, regenerating the stale artifact rather than spending an override -- *"'the override IS the
legal path' is true only of the case that actually blocks."* Third gate to fire on that seat tonight;
**all three were right, and none was overridden.**
