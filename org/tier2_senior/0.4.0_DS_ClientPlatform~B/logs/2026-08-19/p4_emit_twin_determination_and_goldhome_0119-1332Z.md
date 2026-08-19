# OPAL_ADVIPOINTERS.P4-EMIT-49F — twin un-collapse determination executed + gold-home absorption
**agent:** 0.4.0_DS_ClientPlatform~B · **date:** 2026-08-19 0119Z–1332Z (event-driven wakes) · **archetype:** IMPLEMENT
**Log ordered:** ANDREW-DIRECT ~13:16Z via CTO 133137Z ("have everyone do a /log and report back") — fleet wind-down follows; **Current State below IS the successor handoff for the publisher lane.**

## What happened (delta since @c0b106d888, yesterday's log)
Overnight COO routed CVO's measured finding: the d12 legacy twin pair serves TWO FE consumers
with DIFFERENT nna domains (windowed 1,091d at ai.ts:409 vs full 2,417d at :300) — the frozen
list's twin collapse would silently change one consumer's rendered chart at flip. Grounded it at
source (the divergence is d12's OWN designed rule, PLATINUM_NNA_TRUNC_DAYS=1091 @ d12:41,
vacuous at CVO's 08-11 grade, live now), proposed the un-collapse; the 4b determination CLOSED
(COO half 012124Z + CTO half & naming word 105824Z + CVO concur) and was EXECUTED same-window.
Also absorbed DS~A's overnight GOLDHOME-REPOINT (@d62b47cc44) after a wrong-bucket clean-empty
near-miss, and re-ran the full fleet fresh: **13 of 15 twins WOULD_PUBLISH.** COO's re-date
@f79760179a (FAM vendor outage, R-anchored) ACKed — nothing at this seat moved.

## Commits (this lane's author line, safe-commit, gate-passed)
- @6211c4f0f4 — the 4b execution package: port pair-conversion (timeseries_chart.json windowed
  + timeseries_chart_full.json full-domain; byte-compare refusal retired WITH its history — it
  fired on the real condition it was built for), GOLDHOME repoint absorbed
  (GOLD_BUCKET/SILVER_BUCKET from runner_common, positive+negative controls), both
  manifest-honesty gaps closed, frozen-list addendum (naming word verbatim incl.
  underscore-stands; per-consumer FE map; EMIT 15 legacy -> 15 twins; freeze @5f1076e9c1
  intact), P4E5_NEVER_WIDEN_DISCLOSURES_49F.md created (both timeseries entries, determination
  verbatim, per-leg vintage note).

## The load-bearing results
1. **4b determination executed end-to-end**: two advi keys, per-consumer DELTA=0 by
   construction (NEVER#3's own no-hold class); all four COO conditions + CVO's leaf nit
   satisfied; CVO folded 15->15 + per-leg vintages + a bucket-scope absence law into their pin
   instrument @c9e60d454f; COO closed the thread at their desk.
2. **13/15 WOULD_PUBLISH** (fresh staging, asof 2026-08-10, zero S3 writes,
   manifest_2026-08-10_a5308b66cbe6.json): a fresh-schema local a01 dim (declared PRE-STAGED
   honestly) cleared the dim-vintage wall for leaderboard / ownership_map / timeseries_overview
   / cumulative_chart + both pair leaves; d13 trio rides role_aua with the declared degrade
   (snap coverage ends 08-06).
3. **The wrong-bucket clean-zero, caught before acting on it**: the gold plane moved overnight
   to s3://opal-data-49financial/gold/advi/; listing the OLD bucket with the NEW prefix
   returned a clean well-formed EMPTY that briefly manufactured a false "inputs vanished"
   reading — falsified on the live listing, durable fix = bucket resolution from
   runner_common's split, recorded as a vintage note on the frozen list's readiness annex.

## Compiler Tools
comp-find --name (D_01 legacy source location, denominator printed); raw aws partition-set
enumerations carried `# rail-checked` markers (partition-SET diffs, not single-artifact
freshness); port listings verified with positive + negative controls per Rule 22a.

## Current State — SUCCESSOR HANDOFF (publisher lane)
- **READY: 13 of 15 advi twins WOULD_PUBLISH** at the 08-10 canonical vintage. Emit mechanism:
  `data/assets/scripts/gold/runners_49f/d_publisher_port.py` — run
  `--asof <D> --staging-root <dir>` (dry-run default; staging auto-declares aliases/pre-staged);
  live write needs `--publish` AND env `OPAL_ADVI_PUBLISH_GRANT=1`, **armed ONLY on AE's
  P4-PUBIAM grant-live MCP (the TO's first-write gate — NOT yet received).** On grant: emit all
  13 same-window, MCP CVO per key (their pre-flip pins), report COO. Per COO re-date
  @f79760179a: 08-10-vintage first emissions are sanctioned (vintage-honest manifests),
  re-emitted on schedule after R (FAM vendor resumption); pins never reference pre-R emissions;
  flip = R+3.
- **BLOCKED-UPSTREAM (2 twins + production dims), all in DS~A's ruled P3-close set
  @7d7e2e19f6, re-anchored R/R+1:** mix_summary (a07 pair has no S3 home), advisor_nna
  (d14 hard-requires the a06 xwalk), and the S3 dim_relationship partitions (07-15, pre-schema
  — production emission of 4 dim-reading keys needs DS~A's scheduled a01).
- **Governing artifacts:** frozen key list P4E1_FROZEN_SERVED_KEY_LIST_49F_20260818.md
  (@5f1076e9c1 = the freeze; addenda @556d40ecb2 + @6211c4f0f4 — 20 members, EMIT 15->15,
  dispositions move only by NAMED release) · P4E5_NEVER_WIDEN_DISCLOSURES_49F.md (per-key
  ledger; a key emits only with its entry — 2 timeseries entries filed; 13 more due AT
  emission) · TO OPAL_ADVIPOINTERS.P4-EMIT-49F @49dd8469d1 amended @7389357 (P4E-1..P4E-8).
- **HELD unchanged:** d04/d05 on the household spine map (PRD §10 hop); two-identity-systems
  (0/201) = PRODUCT question at Andrew; P4E-8(iii) acct_z* dispositions (138) ride the
  d05-row timeline; proof-of-spec instances (P4E-7 grammar) due per group at emission.
- **Do NOT:** write outside platinum/advi/49financial/* · flip any consumer (DE row 4c) ·
  emit d13 on a jd2 basis where a role_aua snap exists (R-1 binds) · read the OLD gold bucket
  (opal-data-assets portal/gold/advi/...) as the plane — it is a copy vintage, the live home is
  opal-data-49financial/gold/advi/ via runner_common's split.

## Next Steps
1. [successor ~B] On AE P4-PUBIAM grant-live MCP: arm env, emit 13, per-key CVO MCPs + P4E-5
   entries + proof instances, report COO (fleet-complete report is the TO's third milestone).
2. [successor ~B] On DS~A scheduled a01/a07/xwalk landings (R/R+1): re-run fleet, emit the
   remaining 2 + production-vintage re-emissions.
3. [DE/DT, not this lane] row 4c flip at R+3 per key after CVO pins/certs.
