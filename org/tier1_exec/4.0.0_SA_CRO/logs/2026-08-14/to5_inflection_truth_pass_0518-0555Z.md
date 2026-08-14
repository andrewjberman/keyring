# 4.0.0_SA_CRO — MDPF_TRGALN.TO-5 Inflection atom_decomp truth-pass (05:18–05:55Z)

**archetype:** DIAGNOSE

## Arc
Fresh spawn 05:18Z → /watcher (Monitor brvc5oavf, confirmed running) → XXX.md startup (A.1–A.3,
B.1 census: exactly one TO, TO-5 pending) → COO filing msg + ACK → pre-GO prep window used to
vintage-pin the pre-refresh served baseline and pre-read every surface → GO 05:39:39Z → truth-pass
completed and committed @98dbaf099a 05:49Z → table reported to COO 05:50Z for TO-6 spawn.

## The finding (full detail in the deliverable)
All 7 served empty Inflection dates are ONE mechanism, none TRUE-ZERO: eclipse
`fact_portfolios_full` missing run-dates {05-21, 06-01, 07-01, 07-13, 07-14, 07-15, 08-06}
(+ orion {08-06}) × RP-W1 vendor label offset (@bf74d031c1, deployed 2026-08-11T08:41:47Z; label D
reads the partition whose run-date normalizes to D) × builder :1050 `non_model = custody − model`
honest-None propagation. Three-way 7/7 agreement (my live census / served nulls / gold
`honest_none` marker). Class A (5 dates) = visibility regression at the offset deploy — pre-flip
values were D-1 closes mislabeled, so offset-revert is not a remedy. Class B (07-13/14) null since
≤07-29 builds. 383 zero-model dates all TRUE-ZERO by exact partition (443 − 60 model-era;
53 + 7 = 60). Eclipse model leg PERMANENTLY UNFILLABLE (3-party @b0cad1965 + empty 07-16 auditlog
attempt + no rawer copy) → Andrew's roll-forward fork is TO-6's live decision. Orion 08-06 custody
is zero-egress surgical (`opal-data-inf/bronze/positions/2026-08-06.parquet` exists; mirror missed it).

## Deliverables
- @98dbaf099a `TO-5_INFLECTION_TRUTH_TABLE.md` + `proof_TO-5.json` (14 claims, PASS; PRD §7 shape;
  COO's 3 instructions folded as dedicated claims). Committed under audited
  GIT_COMMIT_AUTHOR_OVERRIDE=SHARED_CLOUD_OPS (TO's one-proof-home routing; audit line recorded).
- This log + TO `<status>` flip to complete (same commit).

## Method notes (for the record, not the rule)
- The pre-GO window was spent on reads the GO would need: the pre-refresh baseline capture
  (ETag==md5 byte-pin at 05:21:40Z, 18 minutes before AE's refresh started) is the one piece of
  evidence that could ONLY be captured then.
- The 9 surviving gold snapshots are full-series documents → a document-grain bisect localized each
  hole's first appearance without any log archaeology.
- My first partition probe (own-date keys) was the WRONG question under offset semantics — the
  mechanism prediction had to be re-tested at the mapped run-date keys, where it went 7/7. The
  wrong-key read is retained in-session as a worked example of a clean answer to the wrong domain.

## Corrections (mine, in-session)
- Bundled an `rm -rf` into the stray-tree cleanup mv — denied by permission gate, correctly
  (recursive delete needs explicit confirmation); retried as move-only, stray empty tree surfaced
  in the deliverable's residuals instead.

## Residuals surfaced, not chased (also in deliverable §6)
- Gold as-of-08-11 snapshot: S3 write 08-13T14:10:48Z vs meta.generated_at 08-12T15:12:09Z.
- `.tools/aws` shim passed a `/cygdrive/c/...` cp destination through literally → wrote under a
  stray `C:\cygdrive\` tree (file recovered, md5-verified; empty tree left for cleanup).
- audit-archive-invoker startup finding: `org/jq-ban-override-audit.log` audit-shaped, not in
  MANIFEST (owner 0.7.0_AE_CloudOps per the invoker spec).
- Standing at this seat, untouched tonight (fenced): the W-01..W-32 Andrew review walk-list
  (2026-08-12 log) — resumes when Andrew returns.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-to | TO context set | OK (race-free session file) |
| comp-pipescript deployed --pipeline mdpf | builder deployed-vs-repo | MATCH (flagless form correctly rc=2 REFUSED first — the gate worked) |
| comp-find (×4: --name eclipse/orion, content fact_assets producer, asOfDate capability) | localization with denominators | producers + capability probes found; SYSTEMS-CONTEXT rows honored |
| comp-which | via HUD routing | honored (rail nudges on Glob answered by comp-find runs) |
| lib/trading_calendar | all staleness/label math | trading-day frontier, never wall-clock (NEVER#1) |
Raw `aws s3 ls/cp/head-object` reads were operational data-plane on owned buckets (rail carve-out);
no raw inspection-class aws calls were made.
