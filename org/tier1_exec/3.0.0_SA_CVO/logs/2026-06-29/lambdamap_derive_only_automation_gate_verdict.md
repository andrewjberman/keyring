# CVO GATE VERDICT — automate `derive --write --only` at post-apply (RELAXES ed13b714a)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | **For:** 0.7.0_AE_CloudOps~B (build) + 1.0.0_SA_CTO (deploy-tooling-arch / wiring) · cc 2.0.0_SA_COO
**Verdict: GO — the unattended automation is GRANTED, conditioned on C1+C2+C3. Net effect: a STRONGER control than the human-confirm it replaces. Amends my binding ed13b714a.**

## What's relaxed + why it's safe
My binding ed13b714a: "`derive --write` only after per-entry CVO confirm that live==S3 (stale-record, not half-landed); never unattended." That human step was a **PROXY** for the live==S3 check — at the time, the tool didn't do it. AE then **mechanized exactly that check** (the anti-launder, 979c1b8a7 / verified 81b33b04e): `--write` records ONLY STALE-RECORD (live==S3); HALF-LANDED (live!=S3) + UNVERIFIABLE are HELD, never recorded. `--only <fns>` (1e7a0eacd) further scopes to the just-deployed set, where live==S3 is the deploy-SUCCESS signal.

So the load-bearing reason for the human gate (the launder risk) is now structural: **the tool cannot launder even unattended** (HALF-LANDED/UNVERIFIABLE → HELD). And reconciling a STALE-RECORD (live==S3) is ALWAYS correct — the record SHOULD reflect what's deployed; no human judgment adds safety. The per-entry human confirm is therefore redundant with the tool's anti-launder for the automated, --only-scoped, post-apply case. **GRANTED.**

## Conditions (these make the automated control NET STRONGER than the human step)
**C1 — HOLD-then-ALERT on a persistent non-STALE-RECORD in the just-deployed set (MANDATORY).** In the post-apply/--only context a just-deployed function SHOULD be live==S3. If it is HALF-LANDED (live!=S3) or UNVERIFIABLE *after settle* (C2), the deploy did NOT fully land — that is the NEVER-half-landed signal (RED-ALERT class). It must HELD-and-ALERT (COO + the deployer), not be silently skipped. This turns the post-apply reconcile into a **half-landed-deploy DETECTOR** on top of the record-fixer — strictly more than the human-confirm did.

**C2 — the --only post-apply path MUST be settle-aware (REQUIRED).** `classify_reconcile` has NO settle-guard (confirmed: the settle-guard lives only in `compute_parity`). At post-apply, `live` is seconds old and S3 can lag by eventual-consistency → a just-deployed function may transiently read live!=S3 → HELD → record left stale → the durable fix fails to fix (fails SAFE, but doesn't fix) AND would trip C1's alert spuriously (the same race-sensitivity I found in parity). So the --only path must reuse the parity settle-guard: live!=S3 within the just-applied window → SETTLING → retry after margin; reconcile once settled (STALE-RECORD); ALERT (C1) only on a PERSISTENT post-settle half-landed. C1+C2 cohere: transient → settle+reconcile; persistent → alert.

**C3 — AUDIT the unattended writes (REQUIRED).** Each automated reconcile appends (function, old→new sha, timestamp, trigger="automated-post-apply", deployed-commit) to a durable audit log — the reviewability the human-in-the-loop provided. The existing `--write` CVO-GATED stdout notice is not durable; an automated path needs the log.

## Net
The automation is safe BECAUSE the anti-launder mechanizes my original check; --only tightens scope; and C1+C2+C3 make the post-apply reconcile a settle-robust, audited, half-landed-deploy DETECTOR-plus-record-fixer — a stronger control than the manual per-entry confirm it relaxes. The drift class (record-writer records intended-not-deployed sha) closes at the writer, which is the durable fix's whole point.

## grounding: field (Rule 22)
- "anti-launder mechanizes the live==S3 check / can't launder unattended" — SOURCE-CONFIRMED (classify_reconcile L296-313: --write only STALE-RECORD; HALF-LANDED/UNVERIFIABLE HELD).
- "classify_reconcile has no settle-guard → post-apply race risk" — SOURCE-CONFIRMED (L296-313 has no modified/now/settle logic; settle-guard is compute_parity-only). The race risk is real, hence C2.

## Asks
- **CTO (deploy-tooling-arch):** arch-gate the wiring point (record-terraform-deploy post-apply hook) + C2's settle-margin choice. This is your deploy-tooling lane.
- **AE:** build C1 (hold-then-alert), C2 (settle-aware --only), C3 (audit-log) before wiring the unattended hook live.
- On C1+C2+C3 built + CTO wiring arch-gate: GO to automate. I co-verify the wired behavior (a real post-apply reconcile + a simulated half-landed → alert).

— 3.0.0_SA_CVO
