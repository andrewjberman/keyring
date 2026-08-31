# TO-CARD-R-AE closed 7 of 7 — and five distinct control-scope failures, every one in my carrier — 0.7.0_AE_CloudOps~K

**Date:** 2026-08-30
**Task Order:** `NFRA_SUBSTRATECARDING.TO-CARD-R-AE` (issuer `2.0.0_SA_COO~X`, verifier `3.0.0_SA_CVO~X`)
**Status:** COMPLETE — 7 of 7 cards CVO-PASSED, proof instance VALID and CVO-PASSED

---

## Objective

Card the seven `infra/aws/globgrph` subjects this face carries, at SUBSTRATE_CARD v3.1, two of them
(`derive_stitch.py`, `kuzu_nessie_load.py`) FIRST because their cards gate eight other faces. Close
the face with the 7-of-7 line and a validating proof instance.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find "derive_stitch" --all --files`, `"insurance_leg" --all --files` | PASS | The `[HEAD]`/`[DEF]`/`[DOC]` banding located each subject in one hop. **PARTIAL on speed**: two full-corpus content sweeps exceeded 120 s and were backgrounded. |
| comp-which | `comp-which "how do I grep the repo"` | PASS | A.3 EXERCISE limb at load, scored on OUTPUT not rc. |
| substrate-card-check | `python .tools/substrate-card-check.py <card>` | PASS | Routed mid-face by the issuer (04:22Z). 7 of 7 `violations=0 VALID rc=0`, rc read UNPIPED, with a negative control (non-card file → rc=1). |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <instance>` | PASS | `violations=0 VALID rc=0`; alignment 5/5 forward-1, 5/5 forward-2, 5/5 backward. Caught 23 then 3 violations before it passed. |

**What worked:** the two checkers did the job descriptions could not — `substrate-card-check` exists
precisely because a v3.1 rule *"set_by MUST NOT be the carding lane"* had lived only as prose.
**What failed:** `comp-find`'s full-corpus content sweep is too slow for interactive use; native
`Grep` (ungated per Rule 21) carried the scoped searches.
**Gap found:** none in the tools. The gaps were in mine — see below.

---

## Work Completed

### The seven cards

| # | subject | pin | verdict | headline finding |
|---|---|---|---|---|
| 1 | `derive_stitch.py` | `d31070ec0b` | QUALIFIED | nightly leg **20 of 20 FAILED** since 08-10 while the artifact stays fresh — a masked dead schedule |
| 2 | `kuzu_nessie_load.py` | `d7f74b7a59` | QUALIFIED | docstring documents the **retired** mtime pin; node/edge key rules asymmetric |
| 3 | `_canonical.py` | `0950ecb508` | QUALIFIED | #17 liveness + per-unique tmp + tmp GC all ride **one env var** |
| 4 | `_provenance.py` | `92244ab94d` | QUALIFIED | `read_branch_head_marker` collapses **four** causes; `_age_hours` None → verdict `"current"` |
| 5 | `extract_portal_stitch.py` | `1abdfeee95` | QUALIFIED | the shim **discards the denominator its own upstream computes and renders** |
| 6 | `kuzu_incremental_refresh.py` | `9d42cd9910` | QUALIFIED | docstring says "gated OFF pending arch-gate"; the caller records the **GO** and defaults it **ON** |
| 7 | `kuzu_nessie_db.rebuild.tmp.SET` | `f5f5ae2fd2` | QUALIFIED | the reaper's glob reaches **5 of 6** members — not the one the unflagged path creates |

Seven QUALIFIED, zero SOUND, **zero subjects modified**. Two ARMED observations raised and both
DISARMED to `0.7.0_AE_CloudOps` base, OWNED/INERT.

### The proof instance

`fe01478722` — VALID, `violations=0`, `rc=0`. AC1–AC4 PASS. **AC5 `UNCOMPUTABLE-BY-CONSTRUCTION`**:
its oracle is "20 of 20" across the class and this face carries 7. *Face 7 of 7; class 7 of 20.*
Recording PASS on my own seven would have been exactly the "substantially complete" the criterion
forbids.

---

## ⛔ Five control-scope failures, each different from the last

**Fourteen verifier findings across cards 3–7 and the instance. Every one in my CARRIER; none in a
subject.** They are recorded here as five distinct classes, because fixing each did not prevent the
next:

| where | the failure | why the previous fix didn't catch it |
|---|---|---|
| card 3 | census patterns built from the instances **already found** | a member with no verb was invisible to patterns that all required one |
| card 5 | sound instrument, **wrong scope** — per-file census, path-level claim | the instrument was right; the inference crossed a boundary it never measured |
| card 6 | correct detection, **wrong attribution** — `if __name__` is not a `def` | my positive control proved it could FIND handlers, never that it ATTRIBUTED them |
| card 7 | module's **declared intent** voiced as my verified finding | caught by my own credit census before presentation |
| instance | built from the **shape of a similar artifact**, not its contract | the same misroute that opened the face, recurring at its close |

⭐ **The transferable half:** a CREDIT reaches further unnoticed than a defect, because nobody audits
praise as hard — including the author auditing their own draft. My pre-presentation censuses caught
overclaims in findings and repeatedly missed them in credits, until a credit census existed. On
card 6 it caught three on its first run.

⚠ And the pattern *inside* card 5: three rounds, and **every widening flattered the subject.**
"Zero handlers → fails loudly"; "degradation is inherited"; both were a true narrow measurement
widened one step past what was measured, in the direction that praises.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| AC5 recorded UNCOMPUTABLE-BY-CONSTRUCTION, not PASS | Its oracle is the class (20), this face is 7. `PARTIAL` turned out not to be a legal status, and the contract's real vocabulary says something truer than the word I reached for. |
| Never declared the gate open myself | The both-landed report said "LANDED: yes, both. VERIFIED: pending". An author declaring its own gate open is the author grading the author. |
| Refused a D2 deploy mid-face | Rule 27 binds this instance to one project. The base COO withdrew the recall and confirmed the refusal was right. |
| Touched neither the rebuild lock nor the 111 MB of abandoned tmps | Deleting a lock that might belong to a live rebuild is precisely the act the missing discriminator cannot justify. |
| Rebuilt the handler census on the AST mid-face | v1 mis-attributed module-level handlers; card 7 would have inherited the bug. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `deliverables/D11_CARDS/*.card.json` (7) | the seven substrate cards | Yes — `d31070ec0b`, `d7f74b7a59`, `0950ecb508`, `92244ab94d`, `1abdfeee95`, `9d42cd9910`, `f5f5ae2fd2` |
| `deliverables/NFRA_SUBSTRATECARDING.TO-CARD-R-AE_PROOF_OF_SPEC.json` | the proof instance | Yes — `fe01478722` |

**No subject file was modified.** No deploy, no apply, no AWS mutation, no egress.

---

## Blockers

**NONE.** The face is closed and nothing in it waits on anyone.

**Owned elsewhere:** both ARMED observations sit with `0.7.0_AE_CloudOps` base (the
`opal-stitch-produce` nightly; the `_canonical` liveness/GC flag coupling), OWNED/INERT behind that
seat's stated queue. Neither is a monitor — the standing moratorium holds and in both cases the fix
is a schedule or a default.

---

## Current State

`NFRA_SUBSTRATECARDING.TO-CARD-R-AE` is CLOSED: seven cards, each v3.1-valid with three shaped
negatives rejected and `substrate-card-check rc=0`, each independently CVO-PASSED; proof instance
`fe01478722` VALID with alignment 5/5 / 5/5 / 5/5 and a CVO half-PASS. Class denominator 7 of 20 —
the other 13 subjects sit on the eight faces this face's load-bearing gate released at 03:32Z.
**Push state: cards 1–6 on origin; card 7 and the instance LOCAL**, riding the next window as the
verifier instructed.

---

## Next Steps

1. **[`0.7.0_AE_CloudOps~K`] `TO-CARD-R-ETL`** — opens at this seat per its `<sequenced_after>`; four
   `cse_emit_*` subjects. Awaiting the RE-SCOPE line from `2.0.0_SA_COO~X`.
2. **[`2.0.0_SA_COO`] the release clause is at a clean boundary** — face closed, next face not
   started. The cheapest moment to take this seat for D2 if it is wanted.
3. **[`0.7.0_AE_CloudOps` base]** the two OWNED/INERT findings, at that seat's queue position.

---

**Push state:** stated as a MEASURED value in the commit report, never a default.
