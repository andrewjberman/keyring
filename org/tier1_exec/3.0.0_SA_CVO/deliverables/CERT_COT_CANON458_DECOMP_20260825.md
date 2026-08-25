# CERT — `COT_CANON458` DECOMP (Andrew's 458M instruction)

**Certifier:** `3.0.0_SA_CVO` · **Ref certified:** `633cfc7c8b`
(`workflows/atom_decomposition/runs/cot-458m-canonical/20260825T032500Z/DECOMP.md`)
**Issued:** 2026-08-25 ~03:4xZ · **Bar:** v2.2, nine checks.

⛔ **I CERTIFIED THE CURRENT REF, NOT THE ONE I WAS HANDED.** COO announced the cut at
`d075e092a5` (126 lines) and re-homed to `633cfc7c8b` (152 lines) six minutes later. I re-ran every
measurement against the later ref. *A cert naming a superseded ref is true of nothing anyone will
read.*

## CERTIFIED on the ENUMERATION — 23 of 23, per-surface symmetric difference EMPTY

Extractor derived the prefix FROM THE DOCUMENT (`COT`, 32 occurrences) rather than assuming one —
my own `STC-`/`STI-` defect earlier tonight returned a clean 0-of-32 against a healthy document.

| | inv | a | b | c | d | e | f | total |
|---|---|---|---|---|---|---|---|---|
| **measured** | 5 | 4 | 3 | 4 | 2 | 3 | 2 | **23** |
| **claimed** | 5 | 4 | 3 | 4 | 2 | 3 | 2 | **23** |

Re-homing arithmetic independently reconciles: surface (c) = **4** = the declared cross-project
count; 23 − 4 = **19** = the claimed in-project count. Cross-project status declared on 9 lines,
`DECLARED DEPENDENCY` on 2. **I certify the enumeration, not the sizing.**

## ⛔ CHECK 9 — THE FIRST DECOMP CERTIFIED UNDER IT, AND IT PASSES **BOTH** LIMBS

Check 9 exists because of the failure this decomp was cut to prevent, so it is the fair test.

- **(a) COVERAGE — passes in the strongest available form.** Andrew's two requirements do not merely
  each map to a cell; they sit on **ONE** criterion (`COT-e-1`) with the trap stated on its face:
  ***"Either alone PASSES a criterion and FAILS the instruction."*** Repointing satisfies CURRENT
  without touching held-away; excluding held-away on stale data emits the number he called wrong.
  **A decomp cannot pass this limb by accident.**
- **(b) DECLARED BOUNDARY — passes, INCLUDING THE OWNERSHIP LIMB.** Surface (c) is not deleted and
  not silently dropped: it is enumerated as a **DECLARED DEPENDENCY of `COT-e-1`** owned by
  `ADVI_COTETL`. **This is the limb `GLDRNS` only partly passed** (`0.4.0_DS_ClientPlatform~H`,
  self-reported): there the boundary named who held the STANDARD, here it names **a project that
  owns the work**. First specimen to close it.

**Rule 24(iv) is DECLARED FAILING and the non-moving value is NAMED** — (a)(b)(d)(e)(f) move on one
remedy, **(c) does not**. That is postulate (iv) used correctly: not a schema defect, a boundary.

## ONE FINDING — CHECK 7 (ORACLE VIABILITY), `COT-e-1`

**`COT-e-1`'s oracle reads *"totalling 458,053,742.19 (+/- the stated tolerance)"* — AND NO TOLERANCE
IS STATED ANYWHERE IN THE DECOMP.** Measured over all 152 lines: the only tolerance-adjacent language
is `COT-e-2`'s **"tie to the cent"**, which is a *different cell's* standard and which `e-1` never
invokes. **The referent is dangling, and a certifier cannot supply it** — supplying it is exactly the
adjudication this seat is forbidden.

**Why it is not pedantry on this particular criterion:** the whole instruction is a *specific number*.
Whether `458,053,742.18` discharges `COT-e-1` is undetermined by the text, and **the cell that carries
BOTH of Andrew's requirements is the one cell where an undetermined pass condition costs the most.**
**REMEDY (issuer's, one line):** state the tolerance in `e-1`, or bind it to `e-2`'s "to the cent"
explicitly. **NOT decomp-invalidating** — an enumerated cell with an underdetermined threshold is the
`PRF-inv-1` precedent: amend in place, no re-cert.

## WHAT I DO NOT CERTIFY

- **Sizing** of any cell, per the standing scope of this seat's certs.
- **Surface (c)'s mechanism.** It is correctly UNDIAGNOSED — an absent partition has several possible
  mechanisms and each is a hypothesis until source-confirmed. The decomp says so; I am not softening it.
- **That the remedy produces 458M.** That is `COT-e-1` at execution, not an enumeration property.

— `3.0.0_SA_CVO`
