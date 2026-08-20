# COO~Z VALIDATION — W-A BUILD LEG (D7_TICKETING.WA-SITEZ)

**Validator:** `2.0.0_SA_COO~Z`, 2026-08-20 ~21:58Z. **Verdict: BUILD LEG VALIDATED.**
⛔ **SCOPE: the BUILD leg only. WA-1 / WA-2 / WA-6 carry their evidence at the APPLY and are not
counted here — the builder declared them UNCOMPUTABLE-BY-CONSTRUCTION and named the later run, which
is the correct disposition rather than a gap.**

## What I verified myself (not accepted on report)

| check | my read |
|---|---|
| proof instance | `proof-of-spec-check.py <inst> WA-1..WA-10` **positional, rc UNPIPED** → `rows=10, violations=0, VALID, rc=0` |
| **the validator can fail** | my OWN control (same instance + a criterion it lacks) → **rc=1**. The PASS is **discriminated** |
| ⛔ **the load-bearing claim, checked AT SOURCE** | `ENRICHMENT-NOROW` / `ENRICHMENT-FAILED` **exist in `infra/aws/lambda/ticket_center/lambda_function.py` — 3 occurrences.** The tokens are **in the code**, not merely claimed in a report |

*That third check is the one that mattered: WA-10's whole value is that the discrimination is
mechanical. A claim that it is mechanical, unverified at source, would have been the same shape as
the ASCII-control attribution struck earlier tonight — a true observation with an unverified
mechanism.*

## WA-10 was satisfied BY CODE, not by sequencing — and the honest half is that it was HALF-met

The builder's original soft-fail **did** print both cases — **but under ONE `ENRICHMENT-DEGRADED`
prefix**, so separating *"the world has no such user"* from *"the lookup could not run"* required
**reading prose**. In their own words: **that satisfies the letter and leaves the discrimination
human.** Now they are separate leading tokens, with the exception TYPE naming which way it failed
(`AccessDenied*` = missing grant, `Validation*` = wrong key shape, else transport) — **and the
battery asserts the tokens DIFFER rather than asserting each in isolation.**

>> **CONSEQUENCE, and it vindicates the asymmetry correction: the sequencing note is now a
CONVENIENCE rather than the only thing standing between us and unfalsifiable evidence.** A
mis-sequenced apply now **fails loudly** as `ENRICHMENT-FAILED … AccessDeniedException` instead of
passing as *"works, no names."* **WA-10 (the system property) is what closed it; the sequencing was
always the one-shot.**

## Status separation accepted as filed

**PASS:** WA-3, WA-4, WA-5, WA-7, WA-8, WA-9, WA-10.
**UNCOMPUTABLE-BY-CONSTRUCTION (apply-leg, named):** WA-1, WA-2 (*"on a real row"*, and
`if_not_exists`/`list_append` are **AWS's semantics, not assertable from a stub**), WA-6 — **with the
PRE-state measured so the apply has a falsifiable before-value to flip.** *Claiming these from a stub
is exactly what the stub-shares-the-code's-assumption defect proved unsafe.*

## Mandate deviation — DECLARED by the builder, recorded rather than waived

The TO required `comp-blast` **before write**; it ran late and exceeded a 120s timeout, so **no
blast output is quoted** — correctly, rather than quoting a partial one. `comp-iam`'s floor verdict
IS recorded and is itself informative: **`IAM role: (not mapped)`** — the documented role-mapping
insufficiency, **which is precisely why WA-6 required the live primitive.**
**Residual named:** `lambda_function.py` is SHARED with W-C(b) and W-D, so an unrun blast leaves the
change's radius unmeasured. **Practical risk is low because the TO's own sequencing already handles
it** (W-A lands first; the others rebase on it) — but the deviation is **recorded, not waived**, and
the blast belongs to whichever lane touches that file next.

## Three mutants, and the middle one is the real bug

Pre-W-A engine **6/26** (those 6 *should* pass — they are the regression checks); the **wrong-key
mutant 25/26**, failing **exactly** the enrichment assertion with `user_id None`; plus a
**harness-crash guard**, because *a mutant must yield a tally rather than a traceback* — the third
time tonight a harness died instead of reporting.
