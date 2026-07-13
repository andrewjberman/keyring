# CVO~B — GATE-2 DETERMINATION #3 = WITHHELD, and FIVE of my own instruments were broken at HEAD

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, SCRIBE
**agent:** `3.0.0_SA_CVO~B` (Andrew-direct dedicated AoR validation lane, LD-0277)
**window:** 2026-07-13 ~10:22Z (respawn) -> ~11:35Z
**commits:** `59c24b46e`, `d3826ceb3`, `294965d79` (all pushed to CLOUD)

---

## Summary

Respawned holding an OPEN gate-2. **Resolved a state conflict first:** MSTR's dispatch said gate-2 was
open and cited round-8 hashes that are **ancestors** of the hash I had already certified — he had
reconstructed my position from a stale MEMORY.md index, because I died before updating it. His top line
was right; his detail was stale. **Grounded against git rather than either summary**, and found the real
position: my determination #2 (`baa2af0f7`, VERIFIED at `8bd1d1b62`) **no longer binds**, because the
chokepoint lib moved under it (`dbab19e4c`, +102/-7).

Re-ran the whole battery at HEAD. **GATE-2 = WITHHELD** (`d3826ceb3`).

## Determination: WITHHELD on three

1. **F2 — the absent-floor closes the NULL and not the LOSS, at 2 of 3 call sites.** `INF_A_00:274`
   RAISES (`:302`); **`INF_A_01:203` and `INF_C_07:280` FLOOR AND CONTINUE.** `absent='unknown'` floors
   `advisor_key` (the field a human SEES) and leaves `rep_bucket` `<NA>` — and `INF_09:193` filters
   `rep_bucket=='individual'` **before** grouping, so the row is **SILENTLY DROPPED**. Exercised on the
   real filter: **$30 of $90 NNA vanishes, no alarm.** Their comments claim the floor protects against
   exactly this. **It does not.** Defect DEMONSTRATED; **harm NOT demonstrated** (reachability at those
   two sites is ungrounded — not claimed).
   **>> AND I GOT THIS WRONG FIRST: I rendered "F2 is CLOSED at HEAD" from a CENSUS OF ONE.** I
   exercised A_00, saw the raise, and generalised to a three-call-site class. **The unit is the CALL
   SITE.** Caught by `1.0.0_SA_CTO~B`'s independent gate-1 (`d9fd3ff2e`), then re-grounded by my own
   source census (both controls scoring correctly).
2. **R2 — the chokepoint asserts the COLUMN and serves the ROW.** Re-exercised base CVO's fixture myself
   rather than take it on report: **one stamped row vouches for 870 UNSTAMPED+FOLDED rows**, RETURNED and
   SERVED on an OFF run. **LATENT, not a blocker — and I withhold anyway.** Both, and they are consistent.
3. **V4 SERVED-VERIFY = `NOT RUN, blocked by the bronze STOP`.** An **EXPLICIT GAP, never a PASS.** Parked
   on an infrastructure control, not on my analysis. **I read the served `advisor_nna_canonical.json` this
   session and it is NOT a V4** — `data_as_of 2026-07-09`, it predates the AoR code and was produced under
   OFF. *A frozen pre-AoR served artifact is a producer-side check wearing a served-side label.*

## GREEN at HEAD (each with a control that can go RED)

8/8 key matrix `(source_digest, fold_mode, code_digest)` — all three inputs discriminate, A5 legit cache
reuse still RETURNS (`--single` not bricked) · round-8 battery **35 PASS / 0 FAIL** (*it had been ABORTING
after 8 — 27 arms had never run at HEAD*) · **served-view arm GREEN and DISCRIMINATING** (RED at
`69219a7db`, the proven-RED control) → **the fold SURVIVES to the served view**; C_07 stays closed ·
OFF-is-a-no-op DELTA-0 · **R5 presence-gating: resolver prepended to ALL EIGHT chains (`:445-452`);
not-deployed branch fails CLOSED (`:433`)**.

## Phantom advisor: RED on the served spine, NOT a gate-2 blocker — EXERCISED, not assumed

My v1 arm **asserted in prose** that the phantom is "switch-independent" and **never tested it**.
Tested now: `INF_C_01:463` floors to the phantom and `:474` runs `apply_resolution_fold` **on those same
rows** — so the switch and the phantom touch the same rows in sequence. The fold re-keys **iff MOVER** →
must be in the resolution → built from `accounts_v2`. **Grounded LIVE** (roster `snapshot_date=2026-07-12`,
**873 rows**; positive control: account 42 IS found): accounts **560/703/1225 are ALL ROSTER-ABSENT** → the
fold cannot reach them → **DELTA-0.** **But switch-dependence IS REACHABLE** — roster-presence and
txn-`rep_id` nullity are facts about **two different sources with nothing coupling them**. **The green is
DATA-dependent, not structural. Armed, not fixed.** Fix BLOCKED by `[STOP] b7bce51bd`.

**And the reconciliation identity is a trap:** `sum(advisors) == firm_total` ties to **0.00 BECAUSE the
phantom is counted as an advisor** — green in the defective state, **and green through the DELETION mode**
(both sides lose the money at once). **It cannot detect this class in either direction.** Ruling (iii)
inherits the blindness: it catches SUPPRESSION and is **blind to DELETION**. The deletion mode needs a
coverage/denominator assertion — **which IS the deleted F7 detector. F7 and the deletion mode are the same
hole.**

## >> FIVE OF MY OWN INSTRUMENTS WERE BROKEN. NOT ONE WAS CAUGHT BY BEING CAREFUL. <<

1. **The served-view arm MISTOOK THE GUARD FOR THE DEFECT.** Any exception → `survived=False` → printed
   *"RED — THE FOLD IS ERASED."* The exception was the **A8 pin-unset guard doing its job** — the guard I
   had personally certified. **A false RED's remedy is DESTRUCTIVE:** it would have had me reopening C_07.
2. **The phantom arm's GREEN condition REWARDED THE FORBIDDEN FIX** (fold the residual into `'Other'`) —
   ruling-(i)-forbidden, and a **false statement on a served field**. v2 asserts the CANONICAL ROSTER.
3. **The F2 arm ENCODED THE DEFECT** (`absent` defaulting to None) — and the "obvious" repair was to
   **re-add the default so my own test would pass: restoring the hazard to green my instrument.**
4. **`aor_r182_key_verify.py` emitted a CONFIDENT FALSE RED** — *"do not ship this key"* — because it
   verifies the 2-input key and the shipped key grew `code_digest`. **Right when written; the ground moved
   under it.** *A stale arm does not go quiet; it goes CONFIDENT.* Now refuses to render.
5. **In the bar I built TO CATCH over-condemnation, I turned the A3 guard into a "RED over-condemnation."**
   `importlib.reload(aor_resolution)` does not reload `inflection_rep_scope`, which reads `AOR_FOLD_ACTIVE`
   **at import time** — so the run was OFF while my fixture stamped ACTIVE, and the chokepoint raised on a
   **mode mismatch**. **Had it shipped, the "fix" would have been to DISARM A3** — the rollback protection
   this entire round exists to build. Mode-sensitive arms must run in their **own process**.

**KNOWING A FAILURE MODE BY NAME DOES NOT IMMUNIZE YOU AGAINST WRITING IT.** #5 is the same class as #1,
written by me, one hour later, in the arm built to catch that class.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-tool HUD` (PreToolUse nudge) | WARN | Fired on an `aws s3 ls` for a gold/platinum artifact; the search was a READ-ONLY grounding of the served spine + roster, which no comp tool answers (comp-freshness answers vintage, not per-advisor CONTENT). Proceeded. |
| `.tools/commit-gate.sh` | PASS (after 3 ruff F541 fixes) | Blocked 3x on f-strings-without-placeholders across my new arms; clean on the 4th. Gate worked. |
| `.tools/safe-commit.sh -F` | PASS x3 | Used `-F` (message-from-file) throughout — every message carried backticks/`$`, and `-m` is an execution vector (CLAUDE.md Git). `-F` passes through the wrapper correctly. |
| `comp-surface-check` (auto in safe-commit) | PASS | `OK: 6 changed file(s) touch no critical surface` — deliverables only, no SEV1 surface. |

**What worked:** the commit gate caught every ruff violation before push; `safe-commit -F` handled a
2KB message with backticks and `$` without shell evaluation.
**What failed:** nothing in the toolchain.
**Gap found:** `python subprocess.run(['aws', ...])` **cannot resolve the `.tools/aws` Git-Bash shim**
from a Windows Python process (`FileNotFoundError WinError 2`). Any comp-tool or arm shelling out to
`aws` from Python hits this. Worked around with **boto3**, which is the correct answer anyway. Worth a
line in the AWS-shim doc: *the shim is a bash artifact; Python must use boto3, not `aws`.*

## MCP traffic

**4 significant messages** (2 in, 4 out of ~5 total):
- **IN** `0.0.0_AB_MSTR` — LD-0277 standing + `[STOP] b7bce51bd`; then a `[STOP]` relay coupling the
  **bronze STOP to my V4** (my final verification step is unrunnable; do not let anyone "kick" it). ACKed
  both; V4 disposition set to an EXPLICIT GAP.
- **IN** `1.0.0_SA_CTO~B` — **gate-1 = SOUND, WITHHELD on 2** (`d9fd3ff2e`). His finding A **corrected my
  census-of-one**; his finding B is my own R2, still live at HEAD.
- **OUT** — gate-2 determination to `2.0.0_SA_COO` + `0.0.0_AB_MSTR`; independent verdict to
  `1.0.0_SA_CTO~B`; the **pre-registered acceptance bar** to `0.4.0_DS_ClientPlatform`.

## Blockers

**None mine.** Gate-2 is WITHHELD on two DS-owned fixes (bar pre-registered at `294965d79`) and on V4,
which is blocked by the **bronze STOP** — an infrastructure control, not my analysis. Neither fix needs a
gold run or a re-derivation.

## Current State

- **GATE-2 = WITHHELD** at `59c24b46e`. Record: `CVO_B_GATE2_DETERMINATION_3_20260713.md` @ `d3826ceb3`.
  **Determination #2 (`baa2af0f7`) NO LONGER BINDS.**
- **Acceptance bar pre-registered:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/aor_gate2_fix_bar.py` @
  `294965d79` — **3/5, RED by construction.** B1 (R2 row-level) and B4 (F2 all-3-call-sites) are the two
  withholds. **B2/B3/B5 are the OVER-CONDEMNATION controls, already GREEN, and they MUST STAY GREEN** — a
  fix that greens B1/B4 by reddening any of them is a fail-closed guard firing on a legitimate run, and I
  will refuse it.
- **Nothing served. Switch OFF. SERVE-HELD.** No prod touch, no gold run, no re-derivation this session;
  every arm is hermetic or READ-ONLY. `[STOP] b7bce51bd` honoured.
- **Surfaced (not adjudicated):** `MEMORY_FULL.md` states a phantom mechanism (**roster departure**) that
  CLAUDE.md's own CTO amendment (`ef923bf10`) **falsifies** (*the mechanism is a NULL `rep_id` in the
  silver feed*). Both facts co-occur, which is what makes the conflation easy. Owner is CTO/DS.

## Next Steps

- **[me]** on DS's fix commit: re-run `aor_gate2_fix_bar.py` at the COMMITTED hash; render determination
  #4 if 5/5 **with the over-condemnation controls still green**. Then (3a)/(3b) delivery exercise, CHANGE-2.
- **[0.4.0_DS_ClientPlatform]** the two fixes (R2 row-level assertion; F2 raise at A_01 + C_07). **Fix the
  CLASS, not the two names I cited.** Run every mode-sensitive arm in its own process.
- **[1.0.0_SA_CTO~B]** gate-1 withholds track mine 1:1; no divergence to resolve.
- **[2.0.0_SA_COO]** CHANGE-2 sequencing + never-widen co-sign remain his; **V4 cannot clear until the
  bronze trigger is disarmed and the nightly returns.**
- **[Andrew]** the GO. Nothing here authorizes go-live.
