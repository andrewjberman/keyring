# Deploy completion — MDPF G7 cottonwood value_date re-key + compose migration

- **Opened:** 2026-07-29T05:05Z (deploy-start) — **Closed:** 2026-07-29T05:10Z (all legs landed + verified; nothing stranded)
- **Owner:** 0.4.0_DS_ClientPlatform (Rule-13 lane). **Gate:** 1.0.0_SA_CTO (three conditions 234639Z; pulled forward Andrew-direct ~0337Z).
- **Commits (origin/CLOUD confirmed, carried via merge 3920cab0f6):**
  - `0d653d4aa3` — slice value_date re-key + W-2b base + compose moved to producer + global splice removed + loader fail-closed/scope-consistency + tests (25/25)
  - `0bf39cc8d4` — pair UNION merge (repo basis correction + deployed tolerance recal, both provenances)
- **Deploy legs (all `aws s3 cp` from HEAD blobs; head-object ETag == local md5, single-part):**
  1. `s3://opal-data-mdpf/code/scripts/assets_gold/build_cottonwood_mdpf_slice.py` — md5 `68539df870f6039f54445da35436bd30` (37,992 B) ✔
  2. `s3://opal-data-mdpf/code/scripts/assets_gold/build_cottonwood_mdpf_pair.py` — md5 `3c6496d869b670acd774a20cff1c093a` (25,300 B) ✔
  3. `s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` — md5 `374c8ba7a6b588318fd2f01039a5d364` (138,523 B) ✔
- **No activation step:** the 15:00Z scheduled chain (mdpf-daily-dispatch 6d) syncs `code/scripts/` and runs dim → pair → slice → global; the fire is the production emit (D2 evidence untouched — trigger path unmodified).
- **Ordering note (fail-closed by design):** the deployed spine now REFUSES the current live (pre-migration, daily-only) cottonwood slice artifact as UN-COMPOSED. The dispatch writes the composed slice BEFORE the spine runs, so the refusal can only fire if the slice producer itself failed — the refusal IS the outage signal, never a shrunken fold.
- **Follow-on (routed, not mine):** AE dim backfill 07-23..07-27 (CTO condition 3, production-before-consumption — signal sent 2026-07-29 ~05:1xZ; backfill landing before 15:00Z closes the interim 07-21/22/23 cottonwood-absent window entirely).
- **QA evidence (read-only, no ad-hoc production writes):** slice dry-run GATES PASS (covered {07-20, 07-24}, W-2b 38 dates, composed 2+44); fold acceptance harness ALL ROWS PASS (frontier carried_at_declared_cadence(as_of=2026-07-24), headline $1,951,276,008.15 = +$756,202.29 true-vintage delta; 07-20 measured supersedes interp +$1,723,230.36); pair identity PASS on matched vintage, LOUD on mismatched (delta $7,662.24 = real 07-24→07-27 market movement, the gate discriminating).
