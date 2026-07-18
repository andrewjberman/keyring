# 0.8.0_AE_CloudComp~D -- COMPSIMILAR --describe surface ship (Andrew-direct pull-forward)
**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

Window: fresh ~D session start (~0055Z 2026-07-18 UTC) -> ~0215Z. Prior log:
`session_canonical_reg_directive_and_compsimilar_pullforward_2245-0035Z.md`.

## Summary
Executed the Andrew-direct pull-forward (via base 003245Z + COO GO 003449Z): built + shipped the
COMPSIMILAR **`--describe`/comp-describe** tool-surface AHEAD of the KUZUSPLIT-P1 projection. The
"find + describe one AWS resource" capability, servable NOW off the LANDED derive-at-scan engine
(`summary_corpus.py` @3fe0eedf0) over the EXISTING comp-kuzu QUERY path -- decoupled from BOTH gates
(no Kuzu summary-property projection, no `resource_summaries` Iceberg table) by construction.

## What I did
1. **Engine** (`org/modules/graph/debtscan/summary_corpus.py`, +194 lines): new `--describe <arn-or-name>`
   verb. `describe()` = find + describe ONE resource. `load_one()` = 2 targeted comp-kuzu queries (node +
   combined edge neighborhood), NOT the full corpus. `resolve_query()` = LEXICAL ladder (exact ARN ->
   exact name -> substring); ambiguous -> disambiguation list (no silent guess); 0 matches -> comp-kuzu-inc
   refresh hint (broken-retrieval != absent). `_partition_edges()` pure helper (self-loop = both).
   `render_describe()` + `--json`; exit 1 on no-single-resolution. Nearest-BY-PURPOSE similarity stays
   KUZUSPLIT-P1 + table gated (comp-similar Phase-2) -- describe is exact/lexical only.
2. **Self-test** extended to **M5** (offline edge-partition mutant): 5/5 PASS.
3. **Wrapper** `.tools/comp-describe` (on-disk, functional, UNTRACKED -- grantee cannot self-register;
   committing it blocks manifest-check member 5 until COO's tools_index/entries row lands). Added a
   no-arg / --help usage guard (was leaking the internal summary_corpus argparse error).
4. **Registries (AE self-commit):** `comp-tools.yaml` reference entry + `comp-coverage-map.yaml`
   meta_tools row (role graph-describe, **routable: false** -- COO flips to true at land).
5. **Routing SoD handoff for COO:** spec `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/COMPDESCRIBE_ROUTING_SoD_HANDOFF_20260718.md`
   -- ready-to-apply A (graph-call-manifest entries `cloud.describe.resource`) / B (comp-which curated
   vocab) / C (coverage-map routable flip) / D (`git add -f`) + verification + measured collision note.

## Commits (this window)
- `ff21627b0` build: comp-describe surface CODE + registry (3 files: summary_corpus.py, comp-tools.yaml,
  comp-coverage-map.yaml). Pushed CLOUD.
- `381498562` doc: COO routing SoD handoff spec. Pushed CLOUD.
- (both fast-forward-merged clean behind peer commits 7a78bb537/1ba779e0b/080a705e1 -- merge, no rebase.)

## Verification (EXERCISED against the live graph -- Rule 22a, not inferred)
- exact ARN: `bd-49f-fees-runner` -> full summary + producers/consumers/wiring (2 in, 6 out).
- exact name unique: `opal-data-mdpf` bucket -> resolved + described.
- exact name AMBIGUOUS: `opal-cot-value-parity` -> BOTH an IAM_ROLE and a LAMBDA -> disambiguation list,
  NO silent guess (the doctrine working, real name collision).
- substring (ambiguous families), 0-match (refresh hint), `--json`, no-arg usage, exit codes 0/1.
- self-test 5/5 PASS; commit-gate clean; comp-manifest-check registration-invariant PASS (75 tracked
  accounted); comp-coverage-check PASS (inventory complete, no phantom seam).

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| comp-kuzu | pull real ARNs/names to exercise describe against live | PASS (exact queries); one exploratory 4-CONTAINS held-probe timed out (143) -- NOT a comp-describe path |
| comp-describe (built) | exercise all resolution branches end-to-end | PASS (all branches; live graph) |
| comp-manifest-check | confirm member-5 registration-invariant PASS pre-commit | PASS (75 accounted; coverage-map ledgered 79) |
| comp-coverage-check | confirm ledger-ahead-of-disk tolerated | PASS (80 homed, no phantom seam) |
| comp-which | baseline describe-intent routing for the collision note | PASS/measured -- "what is/does this resource" = clean gap; "find an aws resource" -> comp-assets 1.85 (flagged to COO) |
| commit-gate.sh | Rule 14 py gate on summary_corpus.py | PASS (clean) |
| safe-commit.sh + surface-check + risk-reflex | 2 commits, auto gates | PASS (no critical surface; risk-reflex stale-map advisory, clean) |

**What worked:** the KUZUSPLIT-P1 precedent (@5de839ff0 / @7288d1267) gave the exact SoD recipe --
routable:false in the AE ship + wrapper on-disk-untracked passes member 5; COO's land flips routable +
git-add-f's the wrapper. **What failed:** the 4-CONTAINS held-probe timed out (likely triggered a
projection refresh); the held-aware render (`bool(_HELD_RX.search(name))`) is a trivial passthrough
already covered by derive_summary's unit tests -- not re-chased. **Gap:** none new.

## Blockers
NONE (no assumption-blocks). Forward items are at REAL external gates, stated plainly:
- **describe SoD land** -> COO holds the single-manifest-editor baton behind CTO's in-flight
  comp-iam-usage commit (same 2 files); COO lands A/B/C/D + pings on CTO clear. (COO ACK 020512Z.)
- **PH1 apply** (5 resource_summaries_producer TF creates) -> CTO write-path ruling (Nessie-in-VPC vs
  Glue) + rides 0.7.0's derive-image window; NOT addressable now. (0.7.0 released globgrph state 001843Z.)
- **C2 motif-enrich** (next PH2 increment, base design-of-record @72edd1eca) -> CTO arch-gate + COO
  sequence; base explicitly "NOT a GO -- design/feed only". Held.

## Current State
- comp-describe surface: engine + wrapper + AE registries LANDED @ff21627b0 (pushed). Wrapper on-disk
  functional (untracked). Routing SoD spec @381498562 handed to COO, land QUEUED.
- Nice property confirmed with base: C2 enriches derive_summary OUTPUT -> flows into --describe for FREE
  (no surface change), later into --neighbors the same way.
- Monitor `bh9gvom39` LIVE. Registered PID 33232. Session serial file written (LD-0290).

## Next Steps
1. **[2.0.0_SA_COO]** land A/B/C/D from the spec once CTO's comp-iam-usage manifest commit clears; run
   comp-manifest-check + the targeted comp-which route check; ping ~D.
2. **[0.8.0_AE_CloudComp~D]** on COO land ping: verify `comp-which "what does this resource do"` ->
   comp-describe rank-1; iterate the curated vocab immediately if rank-1 needs a tune.
3. **[1.0.0_SA_CTO]** arch-gate C2 (motif-enrich) + the COMPSIMILAR PH1 write-path ruling (Nessie-in-VPC
   vs Glue) for the PH1 apply.
4. **[0.8.0_AE_CloudComp~D]** on CTO C2 GO: build classify_motif (base walks the decomposition/role-map);
   on CTO write-path ruling: re-plan globgrph to absorb 0.7.0's 44 destroys, then the PH1 apply.
