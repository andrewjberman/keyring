# atom_decomp run — INF pipeline stop diagnosis + end-to-end fix — P0 CHARTER

**Run owner:** `4.0.0_SA_CRO~A` · **opened 2026-08-11 ~0445Z** · method: ATOM_DECOMP
`projects/ATOM_DECOMP/skill/atomic-decomposition/` (SKILL.md rules 1–14, workflow P0–P12,
scheduling axes pack 01). **This run is an explicit method test (Andrew's frame).**

## Objective, decision, authority, mode, deadline
- **Objective:** establish WHY the inf-pipeline (`opal-data-inf` + its producers/consumers) is
  stopped, and FIX it end to end.
- **Decision enabled:** release-or-repair — either discharge the 2026-07-13 hold's lift conditions
  and restore the daily cycle, or land the data repair the hold exists to force, then restore.
- **Authority:** Andrew-direct @097ba43959 (verbatim in the record). Confirms/answers the prior
  CTO+DS owner-chain routing question (CTO ACK 044246Z: "it's yours now, cleanly").
- **Mutation mode:** read-only first; mutation EXPLICITLY AUTHORIZED by the sovereign word, but
  sequenced — no mutation before the Phase-0 decisive checks return; all mutation via sanctioned
  mechanisms (safe-commit / safe-apply / Terraform-only / deploy-completion ledger).
- **Deadline:** none stated; drive-now standing law applies.

## Scope: repos, accounts, roots
- Repo: `ajb_workspace` @ CLOUD (`data/inf/scripts/**`, `infra/aws/terraform/inf-pipeline/**` or
  equivalent TF root — exact root pinned in P1).
- AWS: account 313476888478, us-east-1. Data root `s3://opal-data-inf/` (bronze/silver/gold/
  platinum + `code/` + markers). EC2 runner + SSM dispatch surface. Lambda `inf-gold-trigger` (+
  chain Lambdas pinned in P4).
- Consumers: INF platinum dashboard/ADVI surfaces; **mdpf** via completion-marker trigger + the
  inflection feeders (`mdpf/feeds/*/inflection`).

## Invariants (pinned; violating any is a run failure)
1. **The 2026-07-13 HOLD's protected object:** $453,179.39 of served attribution (9 accounts with
   zero silver rows, incl. Peter Lee $368,965.68 + Patrick Scanlan $84,213.71). **No action that
   re-derives gold before the 9-account question is measured.** Lift conditions per
   `org/critical_paths/HOLD_INF_CANONICAL_NNA_REBUILD_20260713.md`: coverage guard LIVE+EXERCISED
   ON THE RUNNER + INF_B_00 selector fix + release word.
2. **W1/W2 consumer contracts (CTO 044246Z):** orion/eclipse `date=D` carries the D-1 settled
   close (no offset reintroduction); firm frontiers stay UNLINKED. Surprise-channel line to CTO
   before any change that could touch either.
3. **Serving path shape unchanged** — no re-homing of served keys (NEVER#3 territory, not in scope).
4. **No alarms/monitors built** (standing moratorium). No shadow paths (standing veto).

## Known questions (the frontier's seeds)
- Q1 What dispatched the gold chain 07-13→08-01 while all three `inf-gold-trigger` rules were
  DISABLED — and why did that path die ~07-31/08-01? (The hold doc's own "direct invoke no
  rule-census can see" warning, live.)
- Q2 The Phase-0 DECISIVE CHECK (predecessor brief §3): (a) deployed `INF_C_01.canonical_nna.py`
  CALLS the coverage guard (call-site, not import) · (b) the 9 at-risk accounts' PRESENCE in
  current silver (by account_id) · (c) single-date scratch dry-run with F7 coverage diff.
- Q3 Why do the 9 accounts have zero silver rows (the upstream mechanism the hold protects
  against) — and is it still true on the current partition?
- Q4 `INF_B_00.canonical_holdings.py` deployed 2026-08-05 17:39Z, AFTER the freeze began — what
  changed, is it the hold's "selector fix," and has it ever run?
- Q5 The inf→mdpf seam: does the completion marker fire on restore, and do the inflection feeders
  resume, without violating W2's unlinked-frontier contract? (Joint with base CRO's decomp.)

## SCOPE-ADD (Andrew-direct via MSTR relay 044428Z, ~0445Z, verbatim in the relay record)
> "yeah that absolutely needs to get fixed and they also need to fix that bullshit residual error by
> taking sum(fee aua) - balance for non fee aua because that is what results in the residual figure
> that freaked out patrick"
- **(a) The fix mandate STANDS through the hold tension** — Phase-0 decisive check folds as
  planned; the check is the safe path to the ordered fix, not a gate against it.
- **(b) NEW IN-SCOPE: the non-fee-AUA residual computation** —
  `data/inf/scripts/gold/INF_D_04.client_portal_summary.py` `_derive_fee_earning_aggregates`
  (predecessor brief located it at `:763`): non-fee AUA is currently `total_aua −
  fee_earning_aua`, a residual that absorbs artifacts. Ground the deployed arithmetic at source
  and fix so non-fee AUA is DERIVED (classification), never a residual. This supersedes the
  exclusion below for the COMPUTATION fix specifically.

## Exclusions (recorded boundaries)
- The ADVI billing ANSWER (predecessor brief §1: the tag, Patrick's true numbers, the
  no-billing-gap verdict): complete, goes to Yang/Joe on its own thread — not re-derived here.
  *(The residual-computation FIX moved IN-scope per the SCOPE-ADD above.)*
- MDPF-side W-waves: CTO's lane; consumer-contract phase only.
- SKILL Rule 14's full SSOT rectangle + multi-agent status-missioned fan-out: ADAPTED to
  sequential single-seat passes (subagent fan-out is fabric-banned) — recorded as a method-test
  deviation, per the SKILL's own focused-run allowance; statuses + evidence classes retained.
- Vendor-side (Orion/Eclipse producer internals beyond our pull boundary): external; egress for
  re-pulls is on the lifted list if needed.

## Evidence freshness
Live AWS reads are current-session; predecessor brief measurements are 2026-08-11 ~0243Z vintage
(re-verified where load-bearing); hold doc is 2026-07-13 vintage (state claims re-verified live,
never trusted as current).
