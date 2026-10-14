# MDPF_CANON -- round 7 L9 interim adjudication (dell1)

<sweep_watermark>2026-10-14T16:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T16:05:00Z. Packet: 2.0.0_SA_COO~D1 msg 5631, `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/ROUND7_DRAIN_END.md` @238fa48e78 (blob ced4d42147e3, verified).

**L9:** CN-m-1 AC3 MET (D1-C-S72); CN-i-1 AC4 NOT MET (D1-C-S73). CN-h-1 AC4, CN-j-1 AC4 and CN-l-2 AC3 wait on their deploys; no slug yet.
**Rows:** 29 of 29 since v9's watermark: 4 graduated INERT, 25 dismissed. D1-W16-S1 closed on the driven refusal arm.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S72",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T16:05:00Z",
    "one_line": "ROUND 7 L9: JUDGMENT MDPF_CANON.TO-CN-m-1 AC3 MET -- every surface right by the order's definitions; the accrual's output key and never-overwrite reason stand (the schedule passes no --allow-overwrite); a second hop (aum_metrics, non_model_assets) recorded for D1-W16-S5.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-m-1 AC3: is each reader's surface right, and does a PARTNER-FACING-CANDIDATE or PARTNER-FACING reader's output_key and the stated reason stand on the evidence the .md prints?",
    "world_is": "ROUND 7 L9, JUDGMENT MDPF_CANON.TO-CN-m-1 AC3: MET. Packet @238fa48e78 (blob ced4d42147e3, verified), msg 5631. Graded on the record org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~20/CN-m-1_READER_CENSUS.md @6ad2e97350 and this seat's own reads. SURFACES, against the order's section 2 definitions: the accrual bridge (build_portal_gold_accrual.py, schedule mdpf-accrual-bridge-daily) is PARTNER-FACING-CANDIDATE -- this seat read it: DECLARED_TYPES aggregate-aua-timeseries source gold/mdpf_revamp/global/aggregate_aua_timeseries.json, dst portal/gold/mdpf/{scope}/{name}/{as_of}.json, put only when head-object finds no dated key ('R5 SKIP (exists, not clobbering)'). The guard can be turned off by --allow-overwrite; the scheduled command (infra/aws/lambda/mdpf-pipeline/mdpf-accrual-trigger/lambda_function.py:108-110) passes only $DRYFLAG, so the guard is live as the record states. The record's landing evidence stands: the staged key (512,084 B) and the served dated 2026-10-13 key (646,107 B) differ; the served key is written 13 s after the staged one and 9 minutes before the 13:40Z accrual. The INTERNAL and NONE readers are right by the letter of section 2 (their outputs are staging keys or logs). A SECOND HOP the definitions do not classify, recorded for D1-W16-S5's re-point ruling: the same accrual also declares aum-metrics (all scopes) and non-model-assets (global) as sources, i.e. gold/mdpf_revamp/global/aum_metrics.json and non_model_assets.json -- the outputs of the two INTERNAL readers dim_mdpf_aum_metrics.py and dim_mdpf_non_model_assets.py, which read the unfolded staged copy. non_model_assets.json was written today 2026-10-14T13:31:37Z (live); aum_metrics.json last 2026-08-14 (not refreshed). Both reach portal/ under the same R5 guard on a day whose dated key is absent at 13:40Z. The served legacy aum-metrics keys (json/portfolios/aum-metrics.json in opal-data-assets and opal-data-portal-v2, 2026-07-23) are not the staging object's bytes, so the line-40 'repoint' is not live. Row D1-W20-S1 (the face carried the record face): the census's own counts differ from the pre-read, and this seat's reads above do not rest on it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~20/CN-m-1_READER_CENSUS.md @6ad2e97350",
        "data/mdpf/scripts/gold/build_portal_gold_accrual.py DECLARED_TYPES, :227-250, :280-292 (read by this seat)",
        "infra/aws/lambda/mdpf-pipeline/mdpf-accrual-trigger/lambda_function.py:108-110",
        "3.0.0_SA_CVO head-object opal-data-assets gold/mdpf_revamp/global/{aum_metrics,non_model_assets,aggregate_aua_timeseries}.json and the three aum-metrics keys"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record: CN-m-1 AC3 MET."
  },
  {
    "id": "MDPF_CANON-D1-C-S73",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T16:05:00Z",
    "one_line": "ROUND 7 L9: JUDGMENT MDPF_CANON.TO-CN-i-1 AC4 NOT MET -- Client Unsupervised is drawn in the locked Ultra-Short Term hex (#f97316, dE00 0.0); the tooltip has no null filter, so Client rows show on dates C/D; the remainder, -$0, stack-sum and build clauses are not shown.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-i-1 AC4 (judgment): the Global AUA Trend read against PRD FWD-9 (3) and (4) and DESIGN.md, the order's listed clauses.",
    "world_is": "ROUND 7 L9, JUDGMENT MDPF_CANON.TO-CN-i-1 AC4: NOT MET, read against PRD FWD-9 (3)(4) and DESIGN.md on the issuer's walk tmp/ui-walk/20261014T150544Z (shots 003, Global (All), Trend) and on portal cand/dell1/mdpf-canon-aua-trend-groups-and-as-of (34cd12d2). MET in the render: the five canonical series in ladder order; ONE 'Custom Models' (fuchsia500 #d946ef) and no 'Other Models'; 'ETF Strategies' (cyan400 #22d3ee, the Total Assets colour) and 'ALT Strategies' (vermilion500 #ff4f1f, as the order names). NOT MET: (1) COLOUR -- 'Client Unsupervised' resolves through l1ColorOf to L1_COLOR 'Client - Opal Unsupervised' = PALETTE.orange500 = #f97316, the LOCKED Ultra-Short Term hex (DESIGN.md C4, 'the colours MEAN the models'), drawn in the same legend and stack: CIEDE2000 0.0 (this seat's computation; every other trend pair is 10.3 or more, and the estate already moved Alternatives off orange500 to clear 10 from Ultra-Short Term, chartColors.ts IV-e-70). (2) THE TOOLTIP CLAUSE is contradicted by the source: renderTrendTooltip filters only interp_total (`payload.filter((entry) => entry.dataKey !== 'interp_total')`) and formats Number(entry.value), so a mounted Client series that is null on dates C and D yields a Client row of $0 on those dates (row D1-W18-S1); the walk did not hover, so the render does not show otherwise. (3) NOT SHOWN by the render record: the true-remainder 'Other AUA' on date A; no '-$0'; the stack summing to the Total on a sampled date (row D1-W18-S3: exact on 24 of 487 valued dates, the rest classed 'rounding gap' with a worst residual the worker reports in the billions); and which commit the 5174 server carried (the walk stamps none; the issuer states 34cd12d2). Nothing is served: the candidate is not landed, and as a client-facing page it lands only on Andrew's approval.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "tmp/ui-walk/20261014T150544Z/shots/003--portfolios-select-0-Global-All-.png (read by this seat; gitignored, not committed)",
        "portal cand/dell1/mdpf-canon-aua-trend-groups-and-as-of (34cd12d2): src/components/CategoryViewTree.tsx L1_COLOR, src/lib/chartColors.ts :48-60, src/pages/ModelPortfolios.tsx :150-160 and renderTrendTooltip :1146-1190",
        "portal DESIGN.md C4 (the locked duration ladder)",
        "3.0.0_SA_CVO CIEDE2000: #f97316 vs #f97316 0.0; #fbbf24 vs #f59e0b 10.6; #ff4f1f vs #ef4444 10.5; #ff4f1f vs #f97316 10.3; #d946ef vs #ef4444 34.8"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record: CN-i-1 AC4 NOT MET; the defects travel in D1-W18-S1, D1-W18-S3, D1-W18-S7."
  },
  {
    "id": "MDPF_CANON-D1-C-S74",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T16:05:00Z",
    "one_line": "GRADUATED to REMEDIATION_v7, INERT: D1-W18-S7 (colour identity), D1-W18-S1 (null tooltip rows), D1-W18-S3 (stack-sum residual), D1-W17-S2 (unrestored test stub).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W18-S1",
      "MDPF_CANON-D1-W18-S3",
      "MDPF_CANON-D1-W18-S7",
      "MDPF_CANON-D1-W17-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED to REMEDIATION_v7, INERT (nothing served), owner 2.0.0_SA_COO~D1: D1-W18-S7 (Client Unsupervised = Ultra-Short Term #f97316; the Client series take a colour 10 or more dE00 from every ladder rung, or the L1 palette moves). D1-W18-S1 (the Trend tooltip renders a null series as a $0 row; filter null entries before the rows). D1-W18-S3 (the stack meets the total to the cent on 24 of 487 dates; the 'rounding gap' class carries a worst residual the worker reports in billions, which is not rounding: name it before FWD-9 (6) is graded). D1-W17-S2 (test_global_fold_flag2.py replaces the module loader with a stub and never restores it: a test-order leak into the gold suite).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_CANON-D1-W18-S1, MDPF_CANON-D1-W18-S3, MDPF_CANON-D1-W18-S7, MDPF_CANON-D1-W17-S2",
        "row D1-C-S73"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "MDPF_CANON-D1-C-S75",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T16:05:00Z",
    "one_line": "DISMISSED 25 round-7 rows (5 BLOCKING resolved or superseded in the round), each with its own reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W21-S1",
      "MDPF_CANON-D1-W21-S2",
      "MDPF_CANON-D1-W21-S3",
      "MDPF_CANON-D1-W21-S4",
      "MDPF_CANON-D1-W21-S5",
      "MDPF_CANON-D1-W21-S6",
      "MDPF_CANON-D1-W21-S7",
      "MDPF_CANON-D1-W22-S1",
      "MDPF_CANON-D1-W23-S1",
      "MDPF_CANON-D1-W23-S2",
      "MDPF_CANON-D1-W23-S3",
      "MDPF_CANON-D1-W23-S4",
      "MDPF_CANON-D1-W18-S2",
      "MDPF_CANON-D1-W18-S4",
      "MDPF_CANON-D1-W18-S5",
      "MDPF_CANON-D1-W18-S6",
      "MDPF_CANON-D1-W18-S8",
      "MDPF_CANON-D1-W18-S9",
      "MDPF_CANON-D1-W20-S1",
      "MDPF_CANON-D1-W20-S2",
      "MDPF_CANON-D1-W20-S3",
      "MDPF_CANON-D1-W20-S4",
      "MDPF_CANON-D1-W20-S5",
      "MDPF_CANON-D1-W17-S1",
      "MDPF_CANON-D1-W17-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "DISMISSED, 25 rows: D1-W21-S1: BLOCKING ARMED, caused by the QA plant (in-place edits, then a plant inside the builder) and corrected over three amendments; the fourth drive refused Global on the min-firms guard without a raise (run/qa_run.json, this seat's read). The hazard class it names stays with D1-W16-S1's history. D1-W21-S2: Plant note superseded by the corrected plant. D1-W21-S3: Instrument note on a RAISED drive's fallback manifest; the graded drive did not raise. D1-W21-S4: BLOCKING, INERT: the second drive refused on the cross-axis gate, a plant artifact; superseded by the fourth drive. D1-W21-S5: Plant note; superseded. D1-W21-S6: BLOCKING, INERT: the third drive refused on the composition gate, a plant artifact; superseded by the fourth drive. D1-W21-S7: Interpreter shutdown noise after a green exit; no effect on the record. D1-W22-S1: The card tool's AFTER title now prints the resolved date; correct. D1-W23-S1: Row-id prefix note in the face; the worker used its own serial. D1-W23-S2: Real-data arm denominator note; 95 objects read. D1-W23-S3: Expect-string versus timeout prefix; recording note. D1-W23-S4: Naming gate WARN (not REFUSE) on a provenance URI; the commit landed. D1-W18-S2: The order's no-egress bound versus its AC3 data arm; an order-text note, no write. D1-W18-S4: Gradient defs resolve through the same colour map; note. D1-W18-S5: The show-chain fix for the Client series, made in the cell. D1-W18-S6: Other AUA keeps the Non-Model silver; handled in the cell. D1-W18-S8: Carve-out lines read through the paired accessor; handled. D1-W18-S9: The tooltip sort list updated for the relabel; handled. D1-W20-S1: BLOCKING ARMED, ruled by the issuer: the census's counts differ from the pre-read (8,812 files and five code readers against 8,831 and four), and this seat graded AC3 on its own reads of the code, schedule and keys (C-S72). D1-W20-S2: IAM detail recorded in the census. D1-W20-S3: Stale fire-time notes; the live cron is 13:40Z. D1-W20-S4: No server access logging on the sampled buckets; recorded in the census's limits. D1-W20-S5: Scan blind to config-keyed readers; the census added comp-freshness by hand. D1-W17-S1: The served frontier cell is dated 2026-10-13, not 10-09; the freeze finding stands. D1-W17-S3: BLOCKING, INERT, answered: registry row 81453d51cf; CN-h-1 committed with the gate passing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the investigation rows named",
        "deliverables/0.9.0_WK_MDPF_CANON~21/run/qa_run.json, qa_run.log"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "DISMISSED, 25 rows: D1-W21-S1: BLOCKING ARMED, caused by the QA plant (in-place edits, then a plant inside the builder) and corrected over three amendments; the fourth drive refused Global on the min-firms guard without a raise (run/qa_run.json, this seat's read). The hazard class it names stays with D1-W16-S1's history. D1-W21-S2: Plant note superseded by the corrected plant. D1-W21-S3: Instrument note on a RAISED drive's fallback manifest; the graded drive did not raise. D1-W21-S4: BLOCKING, INERT: the second drive refused on the cross-axis gate, a plant artifact; superseded by the fourth drive. D1-W21-S5: Plant note; superseded. D1-W21-S6: BLOCKING, INERT: the third drive refused on the composition gate, a plant artifact; superseded by the fourth drive. D1-W21-S7: Interpreter shutdown noise after a green exit; no effect on the record. D1-W22-S1: The card tool's AFTER title now prints the resolved date; correct. D1-W23-S1: Row-id prefix note in the face; the worker used its own serial. D1-W23-S2: Real-data arm denominator note; 95 objects read. D1-W23-S3: Expect-string versus timeout prefix; recording note. D1-W23-S4: Naming gate WARN (not REFUSE) on a provenance URI; the commit landed. D1-W18-S2: The order's no-egress bound versus its AC3 data arm; an order-text note, no write. D1-W18-S4: Gradient defs resolve through the same colour map; note. D1-W18-S5: The show-chain fix for the Client series, made in the cell. D1-W18-S6: Other AUA keeps the Non-Model silver; handled in the cell. D1-W18-S8: Carve-out lines read through the paired accessor; handled. D1-W18-S9: The tooltip sort list updated for the relabel; handled. D1-W20-S1: BLOCKING ARMED, ruled by the issuer: the census's counts differ from the pre-read (8,812 files and five code readers against 8,831 and four), and this seat graded AC3 on its own reads of the code, schedule and keys (C-S72). D1-W20-S2: IAM detail recorded in the census. D1-W20-S3: Stale fire-time notes; the live cron is 13:40Z. D1-W20-S4: No server access logging on the sampled buckets; recorded in the census's limits. D1-W20-S5: Scan blind to config-keyed readers; the census added comp-freshness by hand. D1-W17-S1: The served frontier cell is dated 2026-10-13, not 10-09; the freeze finding stands. D1-W17-S3: BLOCKING, INERT, answered: registry row 81453d51cf; CN-h-1 committed with the gate passing."
  },
  {
    "id": "MDPF_CANON-D1-C-S76",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T16:05:00Z",
    "one_line": "ROUND 7 INTERIM: 29 of 29 rows since the watermark dispositioned; D1-W16-S1 closed on the driven refusal arm; no slug while three judgments wait on deploys.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W16-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "ROUND 7 INTERIM (no slug: three judgment criteria wait on deploys -- CN-h-1 AC4, CN-j-1 AC4, CN-l-2 AC3). 29 of 29 investigation rows after ADJUDICATION_v9's watermark (2026-10-14T14:05Z) are dispositioned (C-S74 4 graduated, C-S75 25 dismissed). D1-W16-S1's clock closes in REMEDIATION_v6: the CTO's refusal arm was DRIVEN by CN-n-1 (a deliberate act, which the spine prefers to the organic wait my remedy text named): run/qa_run.json reads manifest_errors.global 'SystemExit: GLOBAL MIN-FIRMS FOLD REFUSED: the as-of date 2026-10-13 is held by 1 firm(s) ...', a4_objects_built 12; s3_ops.json calls GetObject 1,370 and ListObjectsV2 1,100, blocked []; served_before.json and served_after.json are canonical-JSON equal, 2,886 entries each (this seat's comparison). D1-W16-S2, D1-W16-S4 (the Other Models carry; deploy owed) and D1-W16-S5 (re-point ruling; C-S72 adds the second hop) stay open in REMEDIATION_v6.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this file's rows C-S72..C-S75",
        "deliverables/0.9.0_WK_MDPF_CANON~21/run/{qa_run.json,s3_ops.json,served_before.json,served_after.json}"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The interim record."
  }
]
```
