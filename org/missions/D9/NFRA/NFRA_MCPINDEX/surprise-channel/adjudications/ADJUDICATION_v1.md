# NFRA_MCPINDEX -- round 1 adjudication

Author: 3.0.0_SA_CVO~O. Round: v1. Fabric: site-z (the project was re-seated to the ~O fabric @23bbeff325; round 1
was issued on the laptop fabric). Recorded: 2026-09-25T06:10:00Z.

Input snapshot: workspace `fec99f11cd`. Investigation: `surprise-channel/investigations/INVESTIGATION_v1.md@1a651aecfc`
(blob `a0489bf854`), 11 rows: W1-S1, W1-S2, W4-S1, W3-S1, W1-S3, W4-S2, W1-S4, W3-S2, W1-S5, W1-S6, Z-S1. 11 of 11 items
are dispositioned below.

Terminality: 38 of 38 orders, read from the LAST `<status>` tag of each file. 9 are complete (MX-a-1..a-7, MX-c-1,
MX-c-2) and 29 superseded (28 at 366b7f1113, MX-c-4 at 1a651aecfc under CTO ruling R-1 @9c70622d13). 9 of 9
proof-of-spec instances read VALID (rc=0) on this seat's own run.

Judgment criteria: **8**, all graded here (C-S14, C-S15). The trigger message named one, MXC1-AC7. The other seven
are the analysis cells' AC10s, found by enumerating the criteria of every complete order.

Two findings the round's issuer reported in prose only (`POSITION_20260921_WIND_DOWN.md` item 6) are raised as rows
here (C-S12, C-S13), so they reach the slug. Review record:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_MCPINDEX_ROUND1_L8_L9_REVIEW_20260925.md` (same commit).

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "W1-S1 GRADUATED and closed: MXC1-AC4's grant conflict was a cut defect, amended by the issuer, and AC4 was re-run and PASSED under the amended grant (worktree wk-mcpindex-1c, 2026-09-21T08:02:41Z).",
    "class": "OBSERVATION",
    "spec_asserts": "W1-S1: AC4 demands running the writer against the served file, but the order's <paths> grants neither the served file nor a runs/ input.",
    "world_is": "catalog-writer.result.md 'MXC1-AC4 (re-run 2026-09-21T08:02:41Z) -- PASS, under the AMENDMENT' (:79). The served file changed by exactly one planted row, returned to baseline on revert, and nothing was committed. MX-c-1's instance is VALID rc=0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W1-S1",
        "deliverables/0.9.0_WK_NFRA_MCPINDEX~1/catalog-writer.result.md:54-121",
        "POSITION_20260921_WIND_DOWN.md item 3 (cut defects: W1-S1 amended under ruling)"
      ]
    },
    "adjudicates": ["NFRA_MCPINDEX-W1-S1"],
    "disposition": "GRADUATED",
    "notes": "Remediation row W1-S1: REMEDIATED, closed. What carries forward: a criterion that exercises a served file must name that file in <paths> at the cut."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "W1-S2 DISMISSED: the orders named firm NFRA, which the proof-of-spec enum lacks; the issuer ruled FABRIC, the field is optional, and no criterion reads it.",
    "class": "OBSERVATION",
    "spec_asserts": "W1-S2: the order says firm NFRA; the schema's firm enum is {49F, INF, COT, MDPF, FABRIC}.",
    "world_is": "The worker omitted the optional field rather than write an invalid value. The issuer's position records the ruling as FABRIC. Three instances written before the ruling carry no firm; all 9 read VALID.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W1-S2", "POSITION_20260921_WIND_DOWN.md items 3-4"]
    },
    "adjudicates": ["NFRA_MCPINDEX-W1-S2"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Ruled FABRIC by the issuer, and the field is schema-optional and unread by any criterion. The re-cut faces should say FABRIC; that is a wording act at the cut, not a remedy."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S3",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "W4-S1 GRADUATED OPEN: opal-data-bd, read as Black Diamond's bucket, also holds live schwab/ (~12.1 GB), smartx/, platinum/ and canonical/ data, and neither the PRD nor the decomposition discloses it as shared; the read fences the tool cells cut must be exact-prefix per property.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Decomposition s.3's per-property notes and PRD C7's isolation contract describe per-property reads; they name no bucket shared between properties.",
    "world_is": "The worker's live census (2026-09-21) found schwab/ 4,622 objects (~12.1 GB) and smartx/ 2,967 objects in opal-data-bd. MX-a-3's own AC8 fence excludes them by exact prefix, so round 1 is unaffected. A tool cell that fences by BUCKET rather than prefix would read three properties and a served tier.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W4-S1", "data/black_diamond/scripts/silver/merge-daily-incremental.py:53 (S3_BUCKET opal-data-bd)"]
    },
    "adjudicates": ["NFRA_MCPINDEX-W4-S1"],
    "disposition": "GRADUATED",
    "notes": "Not re-measured by this seat; the counts are the worker's, 4 days old."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S4",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "W3-S1 DISMISSED: the empty portal gitlink left the advisor-intelligence page uncited, and AC11 was met on its letter with the gap disclosed; NFRA_OPALAI C2's checkout-path init is the structural remedy.",
    "class": "OBSERVATION",
    "spec_asserts": "MXA1-AC11: each surface's portal page is named with the precomputed key it reads.",
    "world_is": "3 of 4 surfaces are cited from checked-out text; the fourth names its key and discloses the missing page path. W1-S4 is the same environment gap met another way.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W3-S1", "NFRA_OPALAI PRD C2 ('Every checkout path initialises submodules ... An uninitialised submodule is refused loudly')"]
    },
    "adjudicates": ["NFRA_MCPINDEX-W3-S1"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The criterion was honestly met with the gap disclosed, and the environment defect has an owner and a contract elsewhere (NFRA_OPALAI C2)."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S5",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "W1-S3 GRADUATED OPEN: running validate_catalog_v02.py writes a tracked report outside MX-c-2's grant, and the worker reverted it with `git checkout --` after each run; a bound was crossed and repaired by hand, which the next cell should not have to repeat.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MXC2-AC5 requires running the validator; the order's <paths> omits catalog_v02/validation_report.json.",
    "world_is": "The validator writes the tracked file as designed output. The worker restored it each time and committed nothing outside the grant. The issuer's position calls it 'a bound crossed'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W1-S3", "POSITION_20260921_WIND_DOWN.md item 3"]
    },
    "adjudicates": ["NFRA_MCPINDEX-W1-S3"],
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S6",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "W4-S2 GRADUATED and closed: the MX-a-3 drain that lost 5 of 6 files was repaired at 155533ea00, and at HEAD the four deliverables are present, the order's last status is complete and its instance is VALID.",
    "class": "OBSERVATION",
    "spec_asserts": "W4-S2 (ARMED, disarm owner 2.0.0_SA_COO~M): the drain's tree lacked MX-a-3's deliverables and status flip.",
    "world_is": "deliverables/0.9.0_WK_NFRA_MCPINDEX~4/ holds analysis-blackdiamond.result.md and the MX-a-3 instance (last touched 18f48e87d4), read VALID rc=0 by this seat. Row Z-S1 (2.0.0_SA_COO~O) records the disarm.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W4-S2, #NFRA_MCPINDEX-Z-S1", "POSITION_20260921_WIND_DOWN.md item 5 (repaired 155533ea00)", "proof-of-spec-check on the MX-a-3 instance: VALID rc=0 (this seat, 2026-09-25)"]
    },
    "adjudicates": ["NFRA_MCPINDEX-W4-S2"],
    "disposition": "GRADUATED",
    "notes": "Remediation row W4-S2: REMEDIATED, DISARMED, closed. The issuer's method (compare each drained file's blob against the branch, not a count) is what caught it."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S7",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "W1-S4 DISMISSED: the worker provisioned the empty portal gitlink with a read-only `git -C portal worktree add` at the pinned SHA and changed no tracked byte; the same environment gap as W3-S1.",
    "class": "OBSERVATION",
    "spec_asserts": "W1-S4: MXC1-AC4's exercise needs portal/src/api readable; portal is empty in a fresh worktree and not in the grant.",
    "world_is": "The worker recorded `git status --porcelain -- portal` clean before and after. The provisioning is local environment state, not a committed object.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W1-S4"]
    },
    "adjudicates": ["NFRA_MCPINDEX-W1-S4"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved in-cell without crossing the grant. The structural remedy is NFRA_OPALAI C2's submodule init, as for W3-S1."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S8",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "W3-S2 GRADUATED OPEN and still ARMED, RE-MEASURED LIVE TODAY: trueshares DIVZ and IDVZ silver fact_holdings hold 0 objects against 32 bronze deliveries each (up from 28 on 09-21), while the silver guard still reads PASS because it never counts the holdings feed.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.4.0_DS_ClientPlatform",
    "spec_asserts": "trueshares/{DIVZ,IDVZ}/meta/backfill-status.json: silver backfill_complete true, verdict PASS, holes [].",
    "world_is": "This seat's reads, 2026-09-25 ~06:0xZ, bucket opal-data-assets, with auto-paginated counts: DIVZ silver/fact_holdings 0, DIVZ bronze/holdings 32; IDVZ silver/fact_holdings 0, IDVZ bronze/holdings 32. Positive control: trueshares/DIVZ/silver/ holds 72 objects, so the read sees silver. The gap has grown by 4 deliveries per fund since the row. The converter exists (etf_conversion.py:279-347) and is wired (:231-232), so the fault is upstream of the code, in invocation or trigger.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W3-S2",
        ".tools/aws s3api list-objects-v2 --bucket opal-data-assets --prefix trueshares/{DIVZ,IDVZ}/{silver/fact_holdings,bronze/holdings}/ (this seat, 2026-09-25)",
        "data/assets/scripts/silver/etf_conversion.py:231-232, :279-347"
      ]
    },
    "adjudicates": ["NFRA_MCPINDEX-W3-S2"],
    "disposition": "GRADUATED",
    "notes": "The disarm owner is outside this fabric. Per CLAUDE.md, a queued-if-not-live delivery is a wish, so the slug PARKS the item with its owner and the condition that un-parks it, and 1.0.0_SA_CTO~O routes it. Two defects travel together: the unconverted feed, and a completeness guard whose 'expected' set omits a feed it claims to cover."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S9",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "W1-S5 GRADUATED OPEN, disarmed: AC11's unsatisfiable catalog limb was ruled out of MX-c-4 (@5f3b4a20c6) and MX-c-4 was superseded (R-1 @9c70622d13); the re-cut cell grades 49 as 44 classified plus 5 HELD, and each tool cell (MX-t-*) owns its catalog reference.",
    "class": "OBSERVATION",
    "spec_asserts": "W1-S5 (ARMED, disarm owner 2.0.0_SA_COO~M): AC11 fails for all 49 tools on every re-run until the catalog carries tool references or AC11 is narrowed.",
    "world_is": "AC11 was narrowed to its two registry limbs; the catalog limb moved to MX-t-1..t-7. R-1 splits the 14 unclassified tools: 9 to the re-cut cell, and the 5 schwab tools HELD behind G-OPLGTW (registered, not enabled, so unreachable). Row Z-S1 records the disarm. The held branch wk-nfra_mcpindex-1-1d is the re-cut's base.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W1-S5, #NFRA_MCPINDEX-Z-S1", "deliverables/1.0.0_SA_CTO~O/ROUND1_RULINGS.md@9c70622d13 R-1", "POSITION_20260921_WIND_DOWN.md 'AC11 RULED'"]
    },
    "adjudicates": ["NFRA_MCPINDEX-W1-S5"],
    "disposition": "GRADUATED",
    "notes": "MX-c-4's AC8 (read_teams_attachment becomes SAFE) is a judgment criterion this seat has NOT graded. R-1 moves it to the re-cut cell's L9. It must be graded before that branch drains, because the change alters live Gateway behaviour."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S10",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "W1-S6 GRADUATED OPEN: every MCPINDEX invocation pins `py -3.12`, which site Z does not register, so the re-cut faces must name a device-neutral interpreter, and so must any re-run of the 9 COMPLETE orders' probes on this box.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "W1-S6: MX-c-4's invocations name `py -3.12`; site Z registers only 3.11 (rc=103).",
    "world_is": "R-1 item 4 fixes the pin in the re-cut face. The complete orders carry the same pin; MXA1-AC11's invocation, for one, reads `timeout 120 py -3.12 .../mx_a_1.py AC11`. Their instances stand VALID as recorded on the laptop fabric, but no seat can re-run them here as written. This seat did not re-run the probes: L10 grades the instances, and they are VALID.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-W1-S6", "task-orders/NFRA_MCPINDEX.TO-MX-a-1.analysis-portal.md (MXA1-AC11 invocation)", "ROUND1_RULINGS.md@9c70622d13 R-1 item 4"]
    },
    "adjudicates": ["NFRA_MCPINDEX-W1-S6"],
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S11",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "Z-S1 DISMISSED: the re-seated issuer's answer record for W4-S2, W1-S5 and W1-S6; its substance is carried at C-S6, C-S9 and C-S10.",
    "class": "OBSERVATION",
    "spec_asserts": "Z-S1: disarms W4-S2; answers W1-S5 and W1-S6.",
    "world_is": "Each answer holds as measured at C-S6, C-S9 and C-S10. W3-S2 was left to this seat, and C-S8 carries it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": ["INVESTIGATION_v1.md@1a651aecfc#NFRA_MCPINDEX-Z-S1"]
    },
    "adjudicates": ["NFRA_MCPINDEX-Z-S1"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A record whose three substances are dispositioned at C-S6, C-S9 and C-S10."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S12",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "RAISED FROM PROSE (issuer position item 6): the Eclipse silver converter calls filter_to_inflection() 0 times, the INFGRD allowlist the Orion tables use, so Eclipse's firm scope rests on an unverified single-tenant vendor connection; a tool serving Eclipse data would inherit that assumption.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "spec_asserts": "PRD C7 (isolation); CLAUDE.md hard stop: NEVER reference another firm's data from a pipeline tree. MX-a-5 AC3 names the scope token `inflection` for all 4 Eclipse tables.",
    "world_is": "analysis-eclipse.result.md:66-75: convert_eclipse_portfolios_to_silver.py imports only coerce_silver_ids (dtype coercion) and makes 0 calls to filter_to_inflection() (_orion_api_silver_lib.py:301-311). No key carries a firm segment. The indirect evidence for single tenancy (a docstring saying 'all firm portfolios'; one scope under monolith_scopes.eclipse) was not verified by the worker, and this seat did not verify it either.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPINDEX~4/analysis-eclipse.result.md:59-75",
        "deliverables/2.0.0_SA_COO~M/POSITION_20260921_WIND_DOWN.md item 6 ('a C7 firm-scope question', reported in prose only)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "ARMED because the MX-t tool for Eclipse would serve whatever the connection returns. Disarm: one read that settles tenancy, such as the distinct firm or rep identifiers across the live Eclipse silver rows against the INFGRD allowlist, before any Eclipse tool cell is cut."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S13",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "RAISED FROM PROSE (issuer position item 6), RE-MEASURED LIVE: Black Diamond's asset_id->cusip bridge silver/bd_assets_dim.parquet was last written 2026-04-14T20:44:16Z and no scheduler builds it, so every asset first seen after that date enters silver transactions, realized and unrealized with a null cusip.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "spec_asserts": "merge-daily-incremental.py:57 names silver/bd_assets_dim.parquet as the asset_id -> cusip bridge, joined at ingestion by enrich_with_cusip() (:292-334).",
    "world_is": "This seat's read, 2026-09-25 ~06:0xZ (s3api, UTC): opal-data-bd silver/bd_assets_dim.parquet LastModified 2026-04-14T20:44:16+00:00. The worker found no scheduler or Lambda trigger for build_bd_assets_dim.py; bd-daily-trigger starts export, silver merge and gold only (README.md:322-338). How many served rows carry a null cusip today was NOT measured.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPINDEX~4/analysis-blackdiamond.result.md:35, :40-47",
        "data/black_diamond/scripts/silver/merge-daily-incremental.py:57, :267, :294",
        ".tools/aws s3api list-objects-v2 --bucket opal-data-bd --prefix silver/bd_assets_dim (this seat, 2026-09-25)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Outside MCPINDEX's write surface. It lives in the Black Diamond pipeline, whose silver scripts DS owns (CLAUDE.md rule 13). The disarm owner is the issuer, who routes it. A Black Diamond tool cell must not be cut to serve cusip-keyed answers until the null rate is measured."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S14",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "L9 grades, the seven analysis AC10s: all PASS. Each list is what staff would plausibly ask, and each typed-query assignment carries a stated reason. Four lists leave out one obvious question, and one routing reason is a registry gap rather than fit; these are carried to the tool cells.",
    "class": "OBSERVATION",
    "spec_asserts": "MXA{1..7}-AC10: 'the question list is what a staff member would plausibly ask of this property, and no common question is left to the typed query without a stated reason'.",
    "world_is": "Read by this seat: the AC5 and AC6 sections of analysis-portal (:257-317), analysis-schwab (:162-227) and analysis-etfs (:197-263); the QUESTIONS blocks of probes mx_a_3..mx_a_6; and the AC5/AC6 prose of analysis-blackdiamond (:73-90), -orion (:102-110), -eclipse (:99-109) and -smartx (:116-125). Every list states that it is NOT measured demand, which is honest. The lists cover holdings, balances, AUA, flows, NNA, gains, fees, advisor of record, model composition and crosswalks.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPINDEX~3/analysis-{portal,schwab,etfs}.result.md (sections cited above)",
        "deliverables/0.9.0_WK_NFRA_MCPINDEX~4/analysis-{blackdiamond,orion,eclipse,smartx}.result.md and probes/mx_a_{3,4,5,6}.py QUESTIONS"
      ]
    },
    "disposition": "GRADUATED",
    "grades": [
      {"criterion": "MXA1-AC10", "instance": "deliverables/0.9.0_WK_NFRA_MCPINDEX~3/NFRA_MCPINDEX.TO-MX-a-1.analysis-portal.proof_of_spec.json@25033c8a6f", "verdict": "PASS", "reason": "18 questions sourced from producer contracts and page briefs; 3 typed-query routings, each with a reason. Limits: (a) Q15 (correlations) and Q16 (factor tilts) are small, fixed, named objects, which by the cell's own rule take a purpose-built tool; they went to the typed query only because systems.json has no key for the domain, so the reason is a registry gap, not fit; (b) 'what does model X hold' (composition and weights) is absent although category-views is not a substitute; (c) Q9 and Q10 are sourced from file names alone."},
      {"criterion": "MXA2-AC10", "instance": "deliverables/0.9.0_WK_NFRA_MCPINDEX~3/NFRA_MCPINDEX.TO-MX-a-2.analysis-schwab.proof_of_spec.json@b6d9d22b68", "verdict": "PASS", "reason": "8 questions tied to the engine's declared schemas and the research record's Rung-2 text; 6 typed-query routings, each reasoned per table, with the dim_transaction routing cited to the decomposition, not re-decided. Limit: Rung-2 asks 'how did it change since date X' of POSITIONS; Q6 carries only the transaction half, and a holdings diff between two dates is absent."},
      {"criterion": "MXA3-AC10", "instance": "deliverables/0.9.0_WK_NFRA_MCPINDEX~4/NFRA_MCPINDEX.TO-MX-a-3.analysis-blackdiamond.proof_of_spec.json@18f48e87d4", "verdict": "PASS", "reason": "10 questions covering AUA, flows, NNA, gains, price, advisor leaderboard, fees, classification and freshness. The one tool (stateful NNA classification) is well reasoned. Limit: no return or performance question for a relationship, though Orion (MX-a-4) carries TWR for the same firm class."},
      {"criterion": "MXA4-AC10", "instance": "deliverables/0.9.0_WK_NFRA_MCPINDEX~4/NFRA_MCPINDEX.TO-MX-a-4.analysis-orion.proof_of_spec.json@2433831f8c", "verdict": "PASS", "reason": "10 questions covering holdings, AUA, transactions, TWR, tax lots, billing, advisor of record, roster, reps and price. The one tool (advisor of record, a two-table join with fallback and disclosed provenance) is well reasoned."},
      {"criterion": "MXA5-AC10", "instance": "deliverables/0.9.0_WK_NFRA_MCPINDEX~4/NFRA_MCPINDEX.TO-MX-a-5.analysis-eclipse.proof_of_spec.json@ea53762c32", "verdict": "PASS", "reason": "10 questions covering model assignment, composition, cash, rebalance and trade-block, roster, counts and the Orion crosswalk. The one tool (AUM variance across two tables, a pattern already at gold) is well reasoned. The scope caveat is carried at C-S12, not here."},
      {"criterion": "MXA6-AC10", "instance": "deliverables/0.9.0_WK_NFRA_MCPINDEX~4/NFRA_MCPINDEX.TO-MX-a-6.analysis-smartx.proof_of_spec.json@88aa89f582", "verdict": "PASS", "reason": "10 questions covering the equity series, AUM on Andrew's ruled GROSS basis, the allocation/account map, positions, valuation, change requests, custody, cash sleeves and the 49F crosswalk. The one tool (filtered join and sum on the ruled basis) is well reasoned."},
      {"criterion": "MXA7-AC10", "instance": "deliverables/0.9.0_WK_NFRA_MCPINDEX~3/NFRA_MCPINDEX.TO-MX-a-7.analysis-etfs.proof_of_spec.json@e2b13a348d", "verdict": "PASS", "reason": "8 questions tied to the vendor schemas and MX-t-7's title; the two typed-query routings (top-N, cross-fund lookup) are reasoned; missing fields are named absent per fund rather than fabricated. Limit: 'how has fund X performed' (period returns), the most common question about an ETF, is neither listed nor named absent."}
    ],
    "notes": "The limits are not failures of AC10's letter. They are the questions the MX-t tool cells should carry, in remediation row C-S14."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S15",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-25T06:10:00Z",
    "one_line": "L9 grade, MXC1-AC7: PASS. A reader holding only the catalog header, the emitter and the cell's record can tell that emit_catalog_v02.py is the one writer of the live catalog, but the emitter's opening docstring line still names the staged file as its output, and only the next paragraph corrects it.",
    "class": "OBSERVATION",
    "spec_asserts": "MXC1-AC7: 'the cell's writer finding is sufficient for a reader who has only the catalog's header, the emitter and this cell's record to know who writes the live catalog'.",
    "world_is": "Read by this seat with only those three inputs. DATA_CATALOG.yaml:3 reads 'BUILT BY: workflows/atom_decomposition/emit_catalog_v02.py at git HEAD 41da358d45'. The emitter's :2-3 read '... -> catalog_v02/DATA_CATALOG.v0.2.staged.yaml (the STAGED port artifact)', and :5 reads 'THIS SCRIPT WRITES THE LIVE refs/DATA_CATALOG.yaml DIRECTLY'. catalog-writer.result.md :39-53 shows 1 writer found, with its resolved OUT equal to the live path. The three agree on the answer; the emitter contradicts itself between its first two lines and its fifth.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml:1-3 at fec99f11cd",
        "workflows/atom_decomposition/emit_catalog_v02.py:1-10 at fec99f11cd",
        "deliverables/0.9.0_WK_NFRA_MCPINDEX~1/catalog-writer.result.md:39-53"
      ]
    },
    "disposition": "GRADUATED",
    "grades": [
      {"criterion": "MXC1-AC7", "instance": "deliverables/0.9.0_WK_NFRA_MCPINDEX~1/NFRA_MCPINDEX.TO-MX-c-1.catalog-writer.proof_of_spec.json@a1329af6d5", "verdict": "PASS", "reason": "The answer (one writer, emit_catalog_v02.py, writing the live path) is recoverable from the three named inputs and they agree. Limit: MXC1-AC5 corrected the disclaimer line but left the docstring's summary line naming the staged output, so a reader of line 2 alone is misled. This is also distinct from WHO OWNS the writer, MCPINDEX's open C1 question, which AC7 does not ask."}
    ],
    "notes": "Remediation row C-S15: a one-line docstring fix, cut into the round's batch cell."
  }
]
```

-- 3.0.0_SA_CVO~O
