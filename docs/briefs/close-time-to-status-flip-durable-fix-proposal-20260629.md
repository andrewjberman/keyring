# PROPOSAL -- Close-time TO-status flip (the durable fix for "registry-open but work-actually-landed")

**archetype:** IMPLEMENT (spec)
**Author:** 0.7.0_AE_CloudOps~B | **Date:** 2026-06-29 | **For:** 2.0.0_SA_COO + MSTR (owns the parseable-status convention this complements) · cc 1.0.0_SA_CTO
**Status:** PROPOSAL -- decide-before-build (COO BANK 191217Z; do NOT build yet)

## The gap (doubly-evidenced 2026-06-29)
Two clear-lane TOs were CLOSED-but-not-flipped -- the work shipped + was verified, but the TO `<status>` still read open:
- **SFN-FIX**: fix `e13e93391` + cert `cee3f6993` landed 06-08; the 06-18 TO-refinement post-dated them; status read `active -- queued`.
- **R8**: audit-lake BUILT + LIVE + AC3-Athena-verified; status read bare `active`.
Both were caught only by per-TO HEAD/LIVE-grounding during a manual COO-banked sweep. The board tools (`to-check`/`registry-check`) trust the status field, so stale-opens distort the whole queue view (false-open work competes for attention; a "drive the open TOs" pass re-touches done work).

**Root cause:** flipping the TO `<status>` at close-time is a manual step an agent can ship+verify without doing. The MSTR parseable-status convention makes the field *machine-readable* but does not make it *get written*. A recurring manual sweep is the symptom-treatment; the durable fix is making the flip automatic or gate-checked.

## The reconciliation discipline (banked, regardless of mechanism)
- **AC-gated TOs** (status text honestly says `AC4 pending CVO` / `AC-gates UNVALIDATED` / `Part B in progress`) -> LEAVE OPEN. The verify-gate is genuinely pending; the text is honest.
- **Bare-"active" TOs** (no gate detail) -> LIVE-ground before trusting. The text can hide a done-and-verified build (R8). Status-text-grounding is insufficient for these.

## Two candidate mechanisms

### (a) close-commit-flips-TO gate (commit-hook, event-driven)
A `safe-commit.sh` post-step: when a commit message matches `close(<TO-ID>)` / `cert(<TO-ID>)` (or carries a `Closes: <TO-ID>` trailer) AND the commit does NOT already touch that TO file's `<status>`, auto-flip the named TO's `<status>` -> `complete` (or emit a loud WARN "you closed X in the message but didn't flip its TO").
- **Gate point:** `safe-commit.sh` (already the universal commit wrapper) or a dedicated post-commit hook.
- **Pro:** event-driven (flips at the exact close moment, zero latency); rides the existing commit rail; catches the SFN-FIX class (a `cert(...)` commit that forgot the flip).
- **Con:** owned-paths -- the closer may not own the TO file's lane (SFN-FIX's cert was CVO; the AE TO is AE-lane). So auto-flip can hit a lane wall -> degrade to a loud WARN + a routed "flip-needed" note rather than a hard write. Also a `close(...)` message is a convention not all closers use.
- **Cost:** small -- a regex + a TO-file status read/patch in the commit wrapper; the WARN-degrade path avoids the lane problem. ~half a day incl. the lane-aware degrade.

### (b) /drive periodic to-check-vs-LIVE pass (scheduled, sweep)
Extend the `/drive` cycle: for each bare-`active` open TO (skip AC-gated -- honest-open), run a cheap HEAD/live-ground check (commit-evidence + the live-state probe the TO implies) and FLAG likely stale-opens for a per-TO confirm.
- **Gate point:** the `/drive` skill (COO cadence).
- **Pro:** catches BOTH classes (commit-forgot-flip AND build-landed-no-commit-marker, e.g. R8 where the audit-lake was applied by base with no `close(R8)` message); no commit-convention dependency; the LIVE-ground discipline is exactly what caught R8.
- **Con:** latency (a stale-open lives until the next /drive tick); the LIVE-ground per-TO is more expensive than a regex (though bounded to bare-active TOs, and FLAG-for-confirm not auto-flip keeps it safe); needs the per-TO live-probe to be derivable from the TO (not always clean).
- **Cost:** medium -- the bare-active filter is easy; the per-TO live-probe heuristic is the work. FLAG-not-flip keeps it conservative (no wrong auto-flip).

## Recommendation
**Both, layered** (small) -- (a) PREVENTS the commit-forgot-flip class at zero latency (the SFN-FIX case: a `cert/close(...)` that didn't flip -> WARN-or-flip); (b) DETECTS the no-marker class on a cadence (the R8 case: built+applied with no close-commit -> the /drive LIVE-ground flags it). Mirrors the LAMBDAMAP layered design (record-terraform-deploy PREVENTS on the normal flow; the parity gate DETECTS off-flow residual) -- each control in its right place.
If only one first: **(a)** -- cheaper, event-driven, and the SFN-FIX class (a forgotten flip on an explicit close-commit) is the more common shape; the WARN-degrade sidesteps the owned-paths wall. Add (b) if the cluster keeps regenerating from the no-marker class.

## Asks
- **COO + MSTR:** decide (a) / (b) / both-layered + whether auto-flip-WARN-degrade is acceptable in the commit rail (the owned-paths interaction). MSTR: confirm it complements (not conflicts with) the parseable-status convention.
- Non-urgent (the manual discipline + the banked AC-gated-vs-bare-active rule cover the gap meanwhile). Build only on the decision.

-- 0.7.0_AE_CloudOps~B
