# AMGT_RESAPP -- surprise channel, REMEDIATION v15 -- PASS 2: every item the instrument still read ARMED after v14

Author: 3.0.0_SA_CVO~Z. Round: v80 (round 67). Fabric: site-z. Recorded: 2026-10-05T02:xxZ. **Reader:** `1.0.0_SA_CTO~Z`.

**What it covers.** After REMEDIATION_v14 (@385d2de981), `comp-surprise --armed AMGT_RESAPP` read 117. Minus the 7 that v14 left ARMED
on purpose, that is 110 items:
- **68** graduated through an adjudication carrier, with no remediation row. The row gate's list did not include them.
- **12** never dispositioned (the instrument read UNDER_INVESTIGATION).
- **30** with an existing remediation row whose disarm was never advanced.

**This file** carries the 80 new rows. Of the 30 stale rows, 26 are advanced IN PLACE, clocks only (disarm DISARMED with `at`,
remediation REMEDIATED, closed true), as the row gate allows. Their new evidence is tabled in ADJUDICATION_v81. 3 stay ARMED (Z-W4-S1,
Z-S6, Z-W31-S2). Z-S11 cannot advance: its row was written INERT with no disarm block. Their files: REMEDIATION_v1 (2), v4 (1), v5 (10), v6 (6), v7 (1), v9 (3), v10 (1),
v11 (1) and v13 (5).

**Result over the 110:** 99 DISARMED and REMEDIATED; **10 still ARMED:** Z-C-S2, Z-W4-S1, Z-C-S3, Z-C-S4, Z-C-S35, Z-S6, Z-W31-S2, Z-C-S46, Z-C-S372, Z-C-S24. One is DISARMED but OPEN (Z-C-S369: disarmed inside
the project, the repo-wide `lib/__init__.py` fix carried to the laptop CTO).

**Method.** As v14: five read-only drafting subagents of this seat. Every row validates against `remediation_row.schema.json`
(0 errors), and every fixing commit cited is an ancestor of HEAD.

**Corrections and notes:**
- `Z-C-S2`'s owner is set to `1.0.0_SA_CTO~Z`, the owner of its one live member (receiving-check grades per file, the gate per set).
- `2.0.0_SA_COO~ZZZ` is kept where a row names it: it is a real early lane serial (ADJUDICATION_v1, v2 and v10).
- v14's `Z-S230` row now cites the CTO's AMENDMENT 1 (@1696185649): rotation is owed, carded to Andrew, and the row stays ARMED until
  the rotated secret passes a daily fire.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "ALL SEVEN GRADUATE AS ONE CLASS, AND IT IS THE MOST EXPENSIVE CLASS IN THIS CHANNEL: A CRITERION WHOSE INVOCATION CANNOT BE SATISFIED BY A CORRECT BUILD IS NOT A WEAK CRITERION, IT IS A NON-CRITERION -- it returns the same verdict on a correct world and a broken one, so nothing about the estate can move it. Three are ALWAYS-FAILS by construction: W7-S1 (AC4's string check cannot match the TO-NAMED tool's own hardcoded Status value), W2-S2 (AC6 greps `comp-routes behaviors`, which prints STATIC hand-authored comments and structurally cannot show a pure-add route; the route IS visible under the `api-routes` subcommand AC6 does not name), W3-S4 (AMGT-s-9's AC2 reads a top-level `figure_ids` key that NONE of AMGT-s-1's three landed files carries, because figures are keyed by a (scope, fiscal_year, mnemonic) tuple there). One is JOINTLY UNSATISFIABLE: W7-S5, where the issuer's instruction and the owned-paths gate cannot both be obeyed, because a TERMINAL order is not a live grant. Two are FACE-VS-GATE disagreements on the same field: W3-S2 and W7-S2, the proof-of-spec filename, where the worker face names a shorter stem than the gate's discovery glob requires. One is an INSTRUMENT GRAIN defect: S2, where receiving-check.py grades one file at a time so an issuance-set coverage limb refuses every member (owns 1 of 16) while the same gate over the set passes 16 of 16.",
    "evidence": [
      "adjudications/ADJUDICATION_v1.md#AMGT_RESAPP-Z-C-S2",
      "W7-S1: org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-6.version-store-opal-data-research.md:145 AC4 amendment 1 reads the ledger tool's own _md_status/_is_terminal_status; last <status> complete",
      "W2-S2: org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-2.on-demand-pull-the-seam-design-then-build.md carries the api-routes substitution (3 hits); last <status> complete",
      "W3-S4 and W7-S5: AMGT-s-9 and AMGT-s-7 last <status> complete -- both criteria sit in terminal orders",
      "W3-S2/W7-S2: e9d19be279 (ancestor of HEAD) check_complete_flip reads the instance the order's <proof_of_spec> block names; REMEDIATION_v14 row Z-W7-S2 REMEDIATED",
      "S2 STILL LIVE: .tools/receiving-check.py:87 routes a task order with argv [p] and :183 runs run_one per path at HEAD 090ba579d3, while .tools/to-pipeline-gate.py:474 _coverage_grade grades the staged SET"
    ],
    "remedy": "Six of seven members are fixed or sit in terminal orders; S2 is still live: receiving-check.py grades task orders one file at a time against a set-level coverage limb. Owner of that member: 1.0.0_SA_CTO~Z (set-level dispatch, or UNCHECKED per file).",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    },
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-C-S278",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, ARMED: FWD-18 has a SPEC-VS-SPEC conflict -- ADDENDUM 4 s.2 ruled the filings producer emit numeric points for the one chart, while the deployed thesis_driver_chart() deliberately reads only an EXACT series-to-mnemonic match and never reads points; rk-7 AC5 and rk-15 AC4 both FAIL on it.",
    "evidence": [
      "adjudications/ADJUDICATION_v12.md#AMGT_RESAPP-Z-C-S278",
      "4c06be3fb1 (ancestor of HEAD, 2026-09-17T07:30Z): ROUND_ANALYSIS.round12 -- FWD-18 conflict RULED option 3",
      "bd299de7e8 (ancestor of HEAD): REMEDIATION_v12 row Z-W23-S5 disarm ARMED -> DISARMED per that ruling",
      "remediations/REMEDIATION_v12.md#AMGT_RESAPP-Z-W23-S5 REMEDIATED, DISARMED, closed true"
    ],
    "remedy": "Disarmed by ruling: the CTO's round-12 analysis ruled the FWD-18 conflict as option 3 (a labelled join from the filing's own points, behind a producer-side verification gate), so the two specs no longer contradict.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-17T07:30Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S359",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED: CAT, a validation name, serves a one-officer roster (its Chief Legal Officer) as complete and RESOLVED, because the parser does not follow its 10-K Item 10 cross-reference to Item 1D -- no CEO on the page.",
    "evidence": [
      "adjudications/ADJUDICATION_v21.md#AMGT_RESAPP-Z-C-S359",
      "a13b0fc140 (ancestor of HEAD, 2026-09-21T21:56Z): rk-79 drain -- CAT served INCOMPLETE-NO-CEO",
      "63d4adf6d1 (ancestor of HEAD): row Z-S206 -- no-CEO census reads 0 of 15 served RESOLVED with no CEO",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-79.jp-president-and-readable-roster-reason.md last <status> complete",
      "remediations/REMEDIATION_v14.md#AMGT_RESAPP-Z-S202 REMEDIATED, DISARMED"
    ],
    "remedy": "Disarmed by rk-79: CAT is served INCOMPLETE-NO-CEO with a readable Item 1D reason, never RESOLVED with no CEO; a full CAT roster from Item 1D stays a named follow-on.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-21T21:56Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S377",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, and it FIRES: the print route runs ~17 s warm against a 29 s timeout, so a cold start times out -- and each timeout tears down the environment, so the next call is cold too. 3 of 5 validation-name prints failed in one sweep.",
    "evidence": [
      "adjudications/ADJUDICATION_v25.md#AMGT_RESAPP-Z-C-S377",
      "88f8589245 (ancestor of HEAD, 2026-09-22T10:00Z): rk-97 apply, memory 512 -> 1769 on opal-amgt-scoped-api",
      "infra/aws/terraform/harvest/scoped-amgt-api.tf:376 memory_size = 1769 at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-97.print-latency.md last <status> complete",
      "remediations/REMEDIATION_v14.md#AMGT_RESAPP-Z-S216 REMEDIATED, DISARMED (ADJUDICATION_v26.md:52: 11 cold starts, 0 timeouts)"
    ],
    "remedy": "Disarmed by rk-97: the function runs at 1769 MB and the print route's cold starts read 0 timeouts on its own logs.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-22T10:00Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S27",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two independently valid Terraform cuts shared singleton configuration",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S27",
      "dc868af89c (ancestor of HEAD): amgt-resapp/dynamodb.tf and security-metrics-table.tf retired",
      "ea6cd450fa (ancestor of HEAD, 2026-09-15T01:29Z): ri-2 git rm amgt-resapp/main.tf; chatter-axis-schedule.tf moved into the harvest root",
      "git ls-files infra/aws/terraform/amgt-resapp/ returns 0 files at HEAD 090ba579d3",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-2.the-producer-consolidated-and-repointed.md last <status> complete"
    ],
    "remedy": "Disarmed: the shared amgt-resapp root no longer exists. Its table files were retired at dc868af89c and its last singleton file (main.tf) removed at ea6cd450fa, so no union of cuts can declare a second backend or provider.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-15T01:29Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S33",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Rename closure must cover live consumers and executable check artifacts",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S33",
      "890b68f914 (ancestor of HEAD): CUTOVER -- the five live modules default to opal-data-harvest",
      "HEAD reads: lib/research/ledger/ledger.py:40, lib/research/freshness/build_view.py:61, infra/aws/lambda/research/pull_enqueue/lambda_function.py:32, integrations/bloomberg/research/model_block_pull.py:88 all default HARVEST_BUCKET to opal-data-harvest",
      "bc577af946 (ancestor of HEAD, 2026-09-15T02:37Z): ri-2 ledger CLOSE -- the scheduled producer repointed and writing again",
      "remediations/REMEDIATION_v5.md#AMGT_RESAPP-Z-S12 REMEDIATED, DISARMED"
    ],
    "remedy": "Disarmed: every live consumer defaults to opal-data-harvest (890b68f914), and the scheduled chatter producer, the residual C-S49 named, was repointed and applied at ri-2 (bc577af946). Pinned worker checks stay historical.",
    "owner": "4.0.0_SA_CRO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "4.0.0_SA_CRO~Z",
      "at": "2026-09-15T02:37Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "4.0.0_SA_CRO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S42",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A worker-local portal object needed preservation before teardown",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S42",
      "remediations/REMEDIATION_v5.md#AMGT_RESAPP-Z-S19 REMEDIATED, DISARMED at 2026-09-11T23:54:40Z (fetch recorded at row Z-S21)",
      "git -C portal cat-file -t e6057f26c57f and c6728146 both return commit at HEAD 090ba579d3; negative control deadbeef1234 returns not a valid object",
      "portal refs/drains/rg-1-portal 83995ea9 and refs/drains/rg-2-portal a845a8be present"
    ],
    "remedy": "Disarmed: the worker-only portal objects were fetched into the main portal object store before teardown and are still present there.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-11T23:54:40Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S56",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Four requested combinations resolve to only two served partitions",
    "evidence": [
      "adjudications/ADJUDICATION_v6.md#AMGT_RESAPP-Z-C-S56",
      "08b2c49923 (ancestor of HEAD, 2026-09-12T21:43Z): rf-1 -- both producers write four crossed partitions",
      "lib/research/metrics/chatter_axis.py:21-23 TRENDING_CHATTER / BREAKOUT_CHATTER and integrations/bloomberg/research/price_axis_pull.py:50,57 TRENDING_PRICE / BREAKOUT_PRICE at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rf-1.the-cross-at-the-producer.md last <status> complete",
      "remediations/REMEDIATION_v6.md#AMGT_RESAPP-Z-W10-S2 REMEDIATED, DISARMED"
    ],
    "remedy": "Disarmed by rf-1: both producers write the four crossed partitions, so each of the four requested combinations has its own served partition.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-12T21:43Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S69",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W12-S1: An unmaterialized portal directory lets Git walk up and successfully answer from the superproject",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S69",
      "remediations/REMEDIATION_v7.md#AMGT_RESAPP-Z-W12-S1 REMEDIATED, DISARMED at 2026-09-13T03:37:45Z",
      "48102a8e9f (ancestor of HEAD, 2026-09-19T03:15Z): rk-60 adds .tools/wk-provision.sh",
      ".tools/wk-provision.sh:107-122 at HEAD: refuses a non-empty portal dir, then git worktree add of the nested repo at the resolved sha",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-60.portal-worktree-provisioning.md last <status> complete"
    ],
    "remedy": "Disarmed: portal-cell worktrees are provisioned by wk-provision.sh, which materialises portal/ as a nested worktree at a resolved ref and refuses a non-empty directory, so git can no longer answer from the parent.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-19T03:15Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S76",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W11-S1: The AC4 portal evidence is at a separately preserved object while the superproject still records e85f6eb84f, which contains zero SecurityAnalysis files",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S76",
      "af6adb7530 (ancestor of HEAD, 2026-09-16T19:44Z): first gitlink carrying c6728146 (portal 2453a7b4)",
      "HEAD gitlink portal = ec65c5d637: 77 files under src/pages/SecurityAnalysis/ against 0 at e85f6eb84f; c6728146 is an ancestor of it"
    ],
    "remedy": "Disarmed: the superproject no longer records e85f6eb84f. The recorded portal gitlink carries the AC4 panel commit c6728146 and the SecurityAnalysis page tree.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-16T19:44Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S88",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W11-S6: The f5461c6884 amendment removes both the empty-key vacuity and the broad PX_LAST substring population",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S88",
      "f5461c6884 (ancestor of HEAD, 2026-09-12T23:19Z): rf-4 amendment 1",
      "8ec7756a49 (ancestor of HEAD): rf-4 AC1 met against amendment 1, order complete",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rf-4.the-corrected-overlay-bypass.md last <status> complete",
      "remediations/REMEDIATION_v7.md#AMGT_RESAPP-Z-W11-S6 REMEDIATED, DISARMED"
    ],
    "remedy": "Disarmed by the criterion repair: rf-4 amendment 1 removed the empty-key vacuity and the broad PX_LAST substring population, and AC1 was met against it.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-12T23:19Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S110",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S51: S52 records each of the twelve candidates required by S51",
    "evidence": [
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S110",
      "5196247fdc (ancestor of HEAD, 2026-09-13T01:28Z): row Z-S52 -- the twelve are READ, which disarms Z-S51",
      "remediations/REMEDIATION_v8.md#AMGT_RESAPP-Z-S51 REMEDIATED, DISARMED"
    ],
    "remedy": "Disarmed: row Z-S52 reads each of the twelve candidates, which meets S51's literal condition; the later omissions are carried by S53/S57.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-13T01:28Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S128",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S61: CTO attributes the PRD's first bar regime to c0b5636ea9 and distinguishes the later per-row expansion at 8019bf6433",
    "evidence": [
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S128",
      "2f66f338da (ancestor of HEAD, 2026-09-13T03:45Z): explanation brief figure corrected",
      "39b6c266a1 (ancestor of HEAD): row Z-S64 -- Z-S61 discharged on its own literal remedy",
      "remediations/REMEDIATION_v8.md#AMGT_RESAPP-Z-S61 REMEDIATED, DISARMED"
    ],
    "remedy": "Disarmed: the brief's body now reads two hours and four minutes, cites both pins, and keeps a correction note.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T03:45Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S146",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT_RESAPP-Z-S70: Both drain refs remain present: rg-1-portal=83995ea977 and rg-2-portal=a845a8be75. The shared gitlink and checkout are e85f6eb84f; the retained worker clone is a845a8be75. Safe object retention is not integration or promotion.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.md#AMGT_RESAPP-Z-C-S146",
      "af6adb7530 (ancestor of HEAD, 2026-09-16T19:44Z): first gitlink containing both rg-1-portal 83995ea977 and rg-2-portal a845a8be75",
      "HEAD gitlink ec65c5d637: 83995ea977 and a845a8be75 are both ancestors (merge-base --is-ancestor true)"
    ],
    "remedy": "Disarmed: the recorded portal gitlink was advanced to a DEV commit that contains both drain refs, so neither project's portal work is outside the pointer.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-16T19:44Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S62",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "I ALMOST TOLD ANDREW THE FRONTEND WAS UNWIRED, ON A ZERO THAT MEANT SOMETHING ELSE. Asked to answer whether the wiring is done, I grepped the SecurityAnalysis page tree for network calls and got ZERO across 20 files with a firing negative control. The page is FULLY WIRED: the calls live one layer out in hooks/useLeadPanelApi.ts, React Query wrappers over portal/src/api/endpoints/amgt-lead-panel.ts, plus PrintExportAction.tsx -- 3 of 21 files import the adapter and the adapter declares BASE = /api/scoped/amgt. A ZERO FROM THE WRONG LAYER READS EXACTLY LIKE A REAL ABSENCE, and this one would have manufactured a round-9 cell to build something that already exists.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S62",
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S129 DISMISSED_WITH_REASON: the hook imports getThesisBundle and getRankTimeSeries from the endpoint adapter",
      "a51f860e36 (ancestor of HEAD, 2026-09-13T03:48Z): ADJUDICATION_v8 lands the dismissal"
    ],
    "remedy": "No act owed: the unwired finding was withdrawn before it was asserted, and the page-to-adapter edge exists. CVO dismissal Z-C-S129 keeps the narrow/wide-layer lesson and creates no cell.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T03:48Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W60-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "AC3's literal invocation (native Windows Python subprocess.run(['./node_modules/.bin/tsc', '--version'], shell=False)) cannot execute the resolved binary: .bin/tsc is an extensionless POSIX shell shim, and Win32 CreateProcess raises OSError WinError 193 rather than running it.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W60-S2",
      "fae9316edb (ancestor of HEAD, 2026-09-19T04:10Z): rk-60 AC3 invokes the tsc shim through bash -c (row W60-S2)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-60.portal-worktree-provisioning.md:218 AC3 runs ['bash', '-c', './node_modules/.bin/tsc --version']; last <status> complete",
      "adjudications/ADJUDICATION_v14.md: W60-S2 dismissed as repaired (fae9316edb, 928352b513), rk-60 AC3 re-run PASS",
      "git grep for the native ['./node_modules/.bin/tsc' argv over org/missions/ finds 0 task orders (the row itself and the rk-60 proof match, as a positive control)"
    ],
    "remedy": "Remediated by acceptance repair: rk-60 AC3 now invokes the tsc shim through bash -c, and the re-run passed.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-19T04:10Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "ALL FOUR GRADUATE, AND THEY SHARE ONE PROPERTY THAT MAKES THEM DANGEROUS: EACH RETURNS A CLEAN, CONFIDENT, WRONG ANSWER ON THIS DEVICE WITH NO ERROR. W2-S4 is the one every seat should read -- the BARE `comp-routes` PATH shim is baked to this device's MAIN checkout, a different directory that never had this branch's commits, so it reported '0' for a route that EXISTS; invoking the worktree's own tracked copy (`bash .tools/comp-routes`) lists it. The issuer's irreproducible '0' was an instrument artifact, not a blind extractor, and the worker re-measured rather than argued. W2-S3 is the same family: an `grep -r` counted a byte-coincidence inside a GITIGNORED terraform provider binary as a loopback violation, reading 1 instead of 0 until the ephemeral .terraform/ cache was removed. W1-S3: the root .gitignore ignores the whole lib/ tree at :47, so any NEW file under lib/research/ is gitignored and `git status`/`git add` report it clean-absent without -f, while already-tracked siblings are unaffected. W1-S4: this worktree's .gitmodules is EMPTY, so the pinned portal gitlink cannot be initialized here at all, and the named READ material was read from the shared main checkout, which carries a DIFFERENT portal commit that also lacks the pin.",
    "evidence": [
      "adjudications/ADJUDICATION_v1.md#AMGT_RESAPP-Z-C-S3",
      "W2-S4 fixed: 13df262a9b (2026-09-10T03:59Z, ancestor of HEAD, NFRA_COMPEFFICACY CE-e-2) makes every ~/bin forwarder exec the CALLER's git toplevel .tools/<name>; ~/bin/comp-routes on this device carries that caller-toplevel resolution and --which",
      "W1-S3 fixed: b750649397 (2026-09-11T09:28Z, ancestor of HEAD) drops the blanket lib/ from the root .gitignore; .gitignore:47-48 at HEAD records the removal and `git check-ignore -v lib/research/newdir_probe/x.py` returns rc=1 (not ignored)",
      "W1-S4 fixed: 69288c8ca0 (2026-09-24T22:27Z, ancestor of HEAD) maps portal in .gitmodules; remediations/REMEDIATION_v14.md W1-S4 row REMEDIATED",
      "W2-S3 STILL LIVE: .tools/_comprail.py:340-341 EPHEMERAL_DIRS at HEAD has no .terraform, and comp-find's default corpus includes gitignored files; remediations/REMEDIATION_v14.md W2-S3 row stays OPEN/ARMED"
    ],
    "remedy": "Open: three of the four instruments are fixed (caller-toplevel shims, lib/ no longer gitignored, .gitmodules maps portal). The fourth, W2-S3, is still live: the comp-find ephemeral floor does not exclude .terraform, so a gitignored provider binary is still searched. Owed: the comp-tool rail owner excludes the ephemeral floor by construction.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    },
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-C-S323",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED: the acceptance sweep drops rk-58's five criteria (unanchored _PROOF_BLOCK_RE binds a prose mention), so round 14 reads 160 over 30 against a true 165 over 31 -- load-bearing for L10 since the R4 ruling.",
    "evidence": [
      "adjudications/ADJUDICATION_v14.md#AMGT_RESAPP-Z-C-S323",
      "01727c89bf (2026-09-21T16:22Z, ancestor of HEAD, AMGT-rk-69): line-anchors _PROOF_BLOCK_RE on both the open and close <proof_of_spec> tags",
      ".tools/surprise-row-gate.py:1307 at HEAD: _PROOF_BLOCK_RE = re.compile(r\"^[ \\t]*<proof_of_spec>[ \\t]*$(.*?)^[ \\t]*</proof_of_spec>\", re.M | re.S)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-69.acceptance-sweep-anchored-proof-block.md last <status> complete",
      "remediations/REMEDIATION_v14.md Z-S176 row REMEDIATED/DISARMED on the same fix"
    ],
    "remedy": "Remediated by rk-69: the acceptance sweep's proof-block regex is line-anchored, so a prose mention of the tag no longer drops an order's criteria from the denominators.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-21T16:22Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S361",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED: two of three validation names served no management under a false ZERO_OFFICERS label; the adapter half is live (rk-77), the page half lands only with rk-78's portal push and the PROD promote.",
    "evidence": [
      "adjudications/ADJUDICATION_v21.md#AMGT_RESAPP-Z-C-S361",
      "3a7afd3316 (2026-09-21T19:13Z, ancestor of HEAD, AMGT-rk-77): read_management serves the Bloomberg fallback roster, labelled (the adapter half)",
      "portal 95d96edb (AMGT-rk-78, the page half) is contained by origin/DEV and origin/PROD and is an ancestor of HEAD's portal gitlink ec65c5d6",
      "portal 6dfc3390 (2026-09-21T23:57Z): merge DEV->PROD v2.1.182 -- Exec Management tab renders the fallback roster's source, status and reason (rk-78), via AMGT-rk-89; ancestor of origin/PROD",
      "6c64d69977 (2026-09-22T00:15Z, ancestor of HEAD): rk-89 complete, portal v2.1.182 on PROD, 7/7 criteria PASS; org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-89.portal-prod-promote.md last <status> complete",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-77.serve-fallback-roster.md and TO-AMGT-rk-78.render-fallback-roster-reason.md last <status> complete"
    ],
    "remedy": "Remediated: the adapter serves the fallback roster (rk-77) and the page that renders it reached portal DEV and PROD (rk-78 promoted by rk-89). This seat did not read the served page back itself.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-22T00:15Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S23",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The current PRD carries an obsolete bucket-absence premise into the next S6 cut although opal-data-research now exists as a declared S3 bucket.",
    "evidence": [
      "adjudications/ADJUDICATION_v4.md#AMGT_RESAPP-Z-C-S23",
      "CTO half: 3e35a50e74 (2026-09-11T15:56Z, ancestor of HEAD) amends PRD s.5 and the S6 measured-by; org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md:1929-1934 at HEAD strikes the absence premise: 'RESOLVED 2026-09-11 -- THE BUCKET EXISTS', with its vintage",
      "COO half: aef0f33605 (2026-09-11T20:46Z, ancestor of HEAD) row Z-S20 + decomposition s.13d remeasure -- identity, access and configuration of the renamed opal-data-harvest bucket read live with an old-name 404 control",
      "adjudications/ADJUDICATION_v5.md (C-S row adjudicating Z-S20): 'support the scoped S5 read obligation after renaming ... no separate bucket remedy is opened'"
    ],
    "remedy": "Remediated: the CTO struck the absent-bucket premise from PRD s.5 and S6 with its measured vintage, and the COO re-read the live bucket (renamed opal-data-harvest) at the cut instead of inheriting a create premise.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-11T20:46Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S28",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Safe-apply required identity state outside the issued write grant",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S28",
      "898fef5268 (2026-09-11T17:57Z, ancestor of HEAD): 'grant org/mcp/sessions/ per row Z-W1-S7', amended BEFORE the spawn into rd-3/rd-5/rd-7",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-5.chatter-axis-scheduled-producer.md:92 lists org/mcp/sessions/ in <paths>, :127 <amended> 'granted org/mcp/sessions/ per row Z-W1-S7'",
      "Later apply cells carry the identity prerequisite and its writer: TO-AMGT-ri-4.the-mount-deployed.md:115 and TO-AMGT-rj-10.the-deploy-and-the-live-read.md:103 list org/mcp/sessions/ in <paths> (issued 59b7b17909, 065fa6070d)"
    ],
    "remedy": "Remediated: the issuer added org/mcp/sessions/ (the safe-apply identity prerequisite) to the apply cells' <paths>, and later apply cells carry it with the printf writer in the criterion.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-11T17:57Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S34",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Tail filtering removed the search denominator required by AC3",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S34",
      "ab85391b24 (2026-09-11T18:49Z): row W7-S6 records the untruncated denominator '12 hit(s) across 67 file(s)'",
      "8b63e78302 (2026-09-11T19:00Z, ancestor of HEAD): rd-7 proof_of_spec instance cites W7-S6 so AC3 is graded on the printed denominator, not on the truncated excerpt",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-7.starred-watchlist-per-firm-pure-marker.md last <status> complete (terminal; the instrument never runs again)",
      "No AMGT_RESAPP order issued after round 6 pipes comp-find through tail (git grep over task-orders: matches only rd-4..rd-7 and re-1, all rounds 5-6)"
    ],
    "remedy": "Remediated for the rd-7 instrument: the full denominator was retained in the row and graded in the proof, and the order is terminal. Not built: no gate refuses a census piped through tail in a future order.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-11T19:00Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S44",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The issued bare npx command selected the wrong compiler package",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S44",
      "4352fe1c47 (2026-09-11T22:24Z, ancestor of HEAD): round-6 issuance fixes the compiler-selection instrument in the criteria",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-re-1.lead-panel-recut.md: 4 uses of 'npx --package typescript' at HEAD, including AC3 at :139",
      "8d6c289dc8 (2026-09-11T23:28Z, ancestor of HEAD): re-1 proof VALID, AC1-AC5 PASS; remediations/REMEDIATION_v5.md W2-S8 row REMEDIATED/DISARMED"
    ],
    "remedy": "Remediated: the recut binds the installed TypeScript package explicitly (npx --package typescript), and the forced build caught an injected type error.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-11T22:24Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S57",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Eleven route declarations and a handler exist in lib/research/api, but the issued paths omit the infrastructure mount",
    "evidence": [
      "adjudications/ADJUDICATION_v6.md#AMGT_RESAPP-Z-C-S57",
      "62d6daf36c (2026-09-15T04:07Z, ancestor of HEAD): 'proof(AMGT_RESAPP ri-4): THE MOUNT IS DEPLOYED -- 8 of 8 PASS-by-output, 19 added 0 changed 0 destroyed'",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-4.the-mount-deployed.md last <status> complete",
      "infra/aws/terraform/harvest/scoped-amgt-api.tf:1 at HEAD: 'THE SCOPED AMGT READ API -- the mount for lib/research/api/scoped_amgt.py', with its own IAM role at :77"
    ],
    "remedy": "Remediated: round 10 granted and deployed the infrastructure mount for the scoped AMGT routes (ri-4), with its own IAM role.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-15T04:07Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S70",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W12-S2: The worker-only object preservation hazard is discharged by the issuer fetch in S32",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S70",
      "120d313474 (2026-09-12T21:52Z, ancestor of HEAD): rows Z-S32/Z-S33 -- the issuer fetch preserving the worker objects, with both controls",
      "portal 83cc87f2 is now contained by origin/DEV and origin/PROD (git branch -r --contains), so remote reachability is also resolved",
      "remediations/REMEDIATION_v7.md W12-S2 row REMEDIATED/DISARMED"
    ],
    "remedy": "No act owed: this row accepts the issuer's local preservation fetch (Z-S32), and the object has since reached portal DEV and PROD.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-12T21:52Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S78",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S36: CVO reproduced six ACTIVE results from to-check against six literal complete record faces and zero actual open orders",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S78",
      "566188587f (2026-09-13T00:57Z, ancestor of HEAD): fix(.tools/to-check.py) masks inline code spans before locating the <status> tag",
      ".tools/to-check.py:76-87 at HEAD: FIX C comment cites rows Z-S36 and Z-S42; :114 the status element is located with inline code spans masked",
      "remediations/REMEDIATION_v7.md Z-S36 row REMEDIATED/DISARMED"
    ],
    "remedy": "Remediated: to-check now locates the status element with inline code spans masked, so prose about the tag is no longer graded as ACTIVE.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-13T00:57Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S90",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S42: directives-check.open_tos consumes to-check ACTIVE/PENDING/BLOCKED/UNKNOWN totals, propagating the same six false ACTIVE counts into D5",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S90",
      "566188587f (2026-09-13T00:57Z, ancestor of HEAD): the to-check status parser fix",
      ".tools/directives-check.py:83-89 at HEAD: open_tos() parses to-check.py --all, so the producer fix reaches the D5 count",
      "remediations/REMEDIATION_v7.md Z-S42 row REMEDIATED/DISARMED"
    ],
    "remedy": "Remediated with Z-S36: directives-check still consumes to-check's totals, and the producer's parser no longer reports false ACTIVE orders.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-13T00:57Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S112",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S53: The reader was blind to multiple fences and to another project's candidates",
    "evidence": [
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S112",
      "25ee0af169 (2026-09-13T03:58Z, ancestor of HEAD): row Z-S65 by 1.0.0_SA_CTO~Z, 'DISARM of Z-S53 and Z-S57' -- the POSN read over both roots and both JSON block shapes",
      "adjudications/ADJUDICATION_v9.md (row adjudicating Z-S65): 'Recovery accepted ... Advance S53/S57 as one completed obligation'",
      "remediations/REMEDIATION_v8.md Z-S53 row REMEDIATED/DISARMED"
    ],
    "remedy": "Remediated: the CTO completed the POSN candidate read over both roots and both block shapes (Z-S65), and the round-9 adjudication accepted it.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-13T03:58Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S142",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT_RESAPP-Z-S66: Fresh-clone absence did not establish estate-wide compiler absence. Round9 AC1 ran the retained 5.9.3 compiler over 2072 files with a firing type-error control. Retained logs agree, and the prepared checkout needs no install. The separate absent-vitest finding remains historically valid.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.md#AMGT_RESAPP-Z-C-S142",
      "1ae76e9c83 (2026-09-14T14:47Z, ancestor of HEAD): round-9 adjudication records the retained 5.9.3 compiler run over 2072 files with a firing type-error control",
      "remediations/REMEDIATION_v9.md Z-S66 row REMEDIATED/DISARMED"
    ],
    "remedy": "No act owed: the row corrects an absence claim. The compiler is present and was run, so no registry egress is needed.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-14T14:47Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S147",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT_RESAPP-Z-S71: The native-path read failure manufactured a full set difference. The final packet records a clean 136-row union (126 base + 4 issuer + 6 worker); the original literal disarm says 134, from the earlier 126+3+5 snapshot. Those are different vintages, not evidence two rows were lost.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.md#AMGT_RESAPP-Z-C-S147",
      "1ae76e9c83 (2026-09-14T14:47Z, ancestor of HEAD): round-9 adjudication records the 136-row union against the earlier 134 snapshot as two vintages",
      "remediations/REMEDIATION_v9.md Z-S71 row REMEDIATED/DISARMED"
    ],
    "remedy": "No act owed: the row records a count-vintage correction (134 vs 136), not a lost row.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-14T14:47Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S63",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "OBLIGATION 4's NUDGE TRIGGER FIRED AND WAS WRONG, FOR THE SECOND MEASURED TIME ON THE SAME SEAT -- and this instance carries the clocks Z-S45 lacked. The L8 packet's receipt read QUEUED with 0 of 1 READ at 23 minutes, which is the literal trigger; at that same moment 3.0.0_SA_CVO~Z had 807,769 bytes of ROUND-8 SUPPLEMENT on disk and wrote its ROUND-8 COMPILE seconds into the probe. THE DELIVERY PLANE AND THE PRODUCTION PLANE DISAGREED AND THE PRODUCTION PLANE WAS RIGHT.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S63",
      "c4705e6ec9 (2026-09-13T03:40Z, ancestor of HEAD): this row read the deliverables plane beside the delivery state in the same sweep, and the nudge was not sent -- the row's own falsifiable disarm condition",
      "adjudications/ADJUDICATION_v8.md row AMGT_RESAPP-Z-C-S139 (a51f860e36) adjudicates Z-S63 DISMISSED_WITH_REASON: 'The owner used the deliverables-plane veto successfully, satisfying the stated same-sweep condition'",
      ".claude/skills/canonical-drive/SKILL.md:30-33 at HEAD: a NUDGE fires only after /canonical-flow's LIVE-PRODUCTION PROBE reports nothing moving"
    ],
    "remedy": "Remediated: the disarm condition was met. The production plane was read beside the receipt and the nudge was withheld. The drive skill gates every nudge behind the live-production probe.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T03:40Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W42-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "After STEP 0's excerpt fix, AC3's literal invocation still cannot run: analyze.py's main() (rk-42's owned surface, not this order's) indexes source_object[\"form\"]/[\"url\"]/[\"filing_date\"]/[\"parser_version\"] unconditionally on the SOURCE print line, and document.py's local CLI object (AC2's own output, .scratch/docs/6861_JP_Equity.source.json) carries none of those four keys -- a second, distinct contract gap from the one this order's amendment named and fixed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W42-S2",
      "2e388452dd (2026-09-19T11:09Z, ancestor of HEAD, rk-40 STEP 0 (v) schema parity): document.py's local source object gains the analyzer's identity keys",
      "lib/research/filings/document.py:981-986 at HEAD: 'AMENDMENT 2 (row AMGT_RESAPP-Z-W42-S2)' sets form, filing_date, url, parser_version in build_local_source_object",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-40.translation-design-a.md last <status> complete",
      "adjudications/ADJUDICATION_v14.md:568 lists Z-W42-S2 under 'Remedied in-project; each fix cited by commit and verified at HEAD'"
    ],
    "remedy": "Remediated (remedy option a): document.py's local source object carries form, filing_date, url and parser_version, so analyze.py main() no longer raises KeyError on the CLI chain.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-19T11:09Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "ALL SEVEN GRADUATE AS SUBSTANTIVE FINDINGS ABOUT THE WORLD RATHER THAN ABOUT AN INSTRUMENT, and two of them are the ones I would not want lost. W1-S2: for the ADR (BABA US, fiscal year end 31 March), Bloomberg NEVER returns a row carrying both a price field and a fundamentals field -- 100% of rows split fiscal-period-end fundamentals from calendar-year-end prices -- so a fiscal-year join keyed on the calendar year of `date` marries each fiscal year's fundamentals to a price observation roughly NINE MONTHS LATER. That is a silently wrong ratio on every non-December fiscal-year-end security, and it is a correctness defect, not a coverage one. W4-S1: AC1's own required action re-runs a PEER's script whose OUTPUT_PATH is derived from `__file__`, so it TRUNCATES that already-completed worker's committed deliverable in place, by construction, on every run -- verified at source. The remaining five: W3-S1 ('the workbook' is not always one file -- 5 of 89 folders carry TWO disagreeing ONE PAGERs), W5-S1 (staleness is list-wide because the schemas name reviewed_at once per LIST, never per entry, so N is 0 or all; plus a `security_key` this project defines nowhere else), S1 (the manifest draws no S1->S6 edge although S1's raw landing needs the store S6 creates, absent at two vintages), W2-S1 (a disclosed deliberate exception to STORE_CONTRACT rule 1), W3-S3 (a ticker set reused from a sibling cell rather than derived independently).",
    "evidence": [
      "adjudications/ADJUDICATION_v1.md#AMGT_RESAPP-Z-C-S4",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/f6_remeasure.py:65 at HEAD still reads OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), \"f6_remeasure.json\") and :232 opens it in \"w\"; file unchanged since 074d0d1ebe (its only commit), so W4-S1's truncation-by-construction stands",
      "W1-S2 remedied: integrations/bloomberg/research/fye_join.py (17f7cba834, AMGT-r-1) pairs price at the fiscal period end; model_block_pull.py:589-597 loads it and :1613 labels the method 'fiscal-period (fye_join)' (34d88231b8, rk-109); both ancestors of HEAD",
      "Child rows Z-W3-S1, Z-W5-S1, Z-S1 read OPEN/ARMED in remediations/REMEDIATION_v1.md; Z-W2-S1 and Z-W3-S3 are closed (REMEDIATION_v1, REMEDIATION_v14); Z-W4-S1 is carried by its own STALE row in this reconciliation"
    ],
    "remedy": "Composite of seven graduated findings; it stays OPEN while any child hazard is live. W4-S1 is unchanged at source: scope f6_remeasure.py's OUTPUT_PATH to the caller (or have criteria read ~3's committed output). W1-S2 is fixed (fye_join). W3-S1, W5-S1 and S1 carry their own OPEN rows in REMEDIATION_v1.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-06T22:04:38Z"
    },
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80",
      "closure": {
        "reason": "CARRIED_BY",
        "pointer": "AMGT_RESAPP-Z-W3-S1 and the other children, per org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/COO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md@fb9ca91ad5 section E"
      }
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S324",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED: a resolved non-EDGAR winner (doc-<sha16>) is not admitted as an accession and beats the UNRESOLVED-SOURCE placeholder only by sort order; the posture batch still bare-sorts and drops a filed name roster resolves.",
    "evidence": [
      "adjudications/ADJUDICATION_v14.md#AMGT_RESAPP-Z-C-S324",
      "90d2de2876 (ancestor of HEAD): rk-65 adds roster.pick_source_key and makes management_posture_batch.filed_status call it; arm e reads UNRESOLVED-SOURCE -> RESOLVED",
      "lib/research/management/roster.py:1065-1082 at HEAD: pick_source_key ranks by class, never bare sorted(keys)[-1]",
      "20f175e4e4 (ancestor of HEAD, rk-91): integrations/bloomberg/research/management_posture_batch.py:108-118 filed_status now reads RESOLVED from filing_source silver rows; no key sort remains"
    ],
    "remedy": "One ranking rule in one place (round 16, rk-65): roster.pick_source_key ranks EDGAR accession over doc-<16hex> over placeholders by explicit class; the posture batch was later moved off key sorting onto filing_source silver (rk-91).",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-21T15:37Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S369",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED: a repo-wide import-identity trap -- lib/ has no __init__.py, so a test file can load a module as a bare top-level package, and two imports of one file become two module objects.",
    "evidence": [
      "adjudications/ADJUDICATION_v23.md#AMGT_RESAPP-Z-C-S369",
      "739eb5f288 (ancestor of HEAD): round-21 analysis disarms W85-S1 for AMGT by a qualified-import cutting rule and raises the repo-wide fix to the estate",
      "org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round21.md:27-33 at HEAD: the cutting rule text and the estate referral",
      "lib/__init__.py absent at HEAD (ls: no such file); child Z-W85-S1 reads DISARMED/REMEDIATED in remediations/REMEDIATION_v14.md"
    ],
    "remedy": "Disarmed for AMGT by the CTO's qualified-import cutting rule binding from round 22 (identity arm in every order). The repo-wide remedy (package marker or single import convention) was raised to the estate and is not built: lib/__init__.py is still absent.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-21T23:29Z"
    },
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80",
      "closure": {
        "reason": "NOT_A_DEFECT",
        "pointer": "org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md@4a89bef967 section E: the namespace-package convention stands"
      }
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S412",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "INCIDENT, not exposure: the deployed opal-amgt-scoped-api SERVES 179 no-span sentences that C-VERBATIM-GATE v0.12 (Andrew-direct) requires to be HELD -- measured by 4.0.0_SA_CRO~Z over 12 of 12 bounded GET /thesis invokes, all HTTP 200 SERVED, 389 sentences, 179 no-span, hash-matched to the historical census. Cause is a PLANE difference: the deployed _validate_drafting_document omits the pipeline no-span HOLD and empty spans pass vacuously, so this seat's earlier repo-probe finding that the pipeline matches the clause does not reach the served artifact.",
    "evidence": [
      "adjudications/ADJUDICATION_v45.md#AMGT_RESAPP-Z-C-S412",
      "4cb1b6b009 (ancestor of HEAD): CVO acceptance, C4 PASSES on deployed bytes -- 210 served / 179 held / zero spanless across all twelve",
      "lib/research/api/scoped_amgt.py:2514-2545 at HEAD: held_no_span_at_read and held_no_span_on_object counted on every served drafting block",
      "65132a45c7 and 0deb8d7318 (ancestors of HEAD): reach measured at five served responses, one security, one client; R-11 rules the eleven untouched securities are not re-opened",
      "bcada3e9ea and 2e9c087db4 (ancestors of HEAD): round 54 AMGT-ad-2, the hold on the object LANDED and ACCEPTED -- 179 no-span sentences held on 12 stored D-1 documents, signed pair 18ac256769 / 04f779ac51",
      "re-read on the CURRENT deployed build (CodeSha256 2rFeF57l) by 3.0.0_SA_CVO~Z, 2026-10-05 ~02:1xZ: GET /thesis on the same twelve securities, 12/12 HTTP 200, 210 served sentences, 0 with empty quoted_spans -- equal to the C4 acceptance"
    ],
    "remedy": "Both halves done. Guard: the deployed validator holds no-span sentences (210 served / 179 held / 0 spanless, 12 of 12). Reach: measured as 5 responses to 1 client, and the CTO ruled untouched securities are not re-opened. Stored objects: the 179 no-span sentences are held on the 12 D-1 documents under the never-widen pair (round 54 ad-2).",
    "owner": "4.0.0_SA_CRO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "4.0.0_SA_CRO~Z",
      "at": "2026-09-23T22:15Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "4.0.0_SA_CRO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S29",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A correct union repair was outside the draining seat grant",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S29",
      "ea6cd450fa (ancestor of HEAD, AMGT-ri-2): git mv chatter-axis-schedule.tf and lambda_src into infra/aws/terraform/harvest/, git rm amgt-resapp/main.tf; 'the amgt-resapp root is now empty and gone'",
      "git ls-files infra/aws/terraform/amgt-resapp at HEAD -> 0 tracked files",
      "infra/aws/terraform/harvest/main.tf:46 and :63 at HEAD: the only terraform {} and provider \"aws\" blocks in the harvest root (git grep over the directory)"
    ],
    "remedy": "The duplicate-backend module no longer exists: ri-2 consolidated all amgt-resapp terraform into the harvest root (Andrew-direct) and removed the amgt-resapp root, so no reconciliation grant is owed.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-15T01:29Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S35",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The socket negative control did not guard the entire test suite",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S35",
      "lib/research/watchlist/tests/test_watchlist.py:80-81 at HEAD: block_all_sockets is a plain (non-autouse) fixture",
      "lib/research/watchlist/tests/test_watchlist.py:104 and :119 at HEAD: the first two tests still do not request it; only :153, :166, :177 do",
      "File unchanged since 61770a9396 (rd-7 build, its only commit); no conftest.py under lib/research/watchlist/tests/ or lib/research/"
    ],
    "remedy": "Apply the socket blocker to every watchlist test (autouse fixture or a package conftest), so no test in the suite can open a real connection.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-10-09T20:19:00Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S45",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The AC2 root no-emit check examined no source files",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S45",
      "8d6c289dc8 (ancestor of HEAD): re-1 proof, AC1-AC5 PASS-by-output, status complete",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-8.lead-panel-and-three-tabs.md: last <status> superseded; :134-135 records AC2 as vacuous",
      "Child Z-W2-S9 reads DISARMED/REMEDIATED in remediations/REMEDIATION_v5.md"
    ],
    "remedy": "The vacuous root no-emit check was replaced in re-1 by a forced referenced-project build with source-file and error-mutant controls; rd-8 is superseded and its historical FAIL is preserved.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-11T23:28Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S51",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The late S22 classification defect has a source repair, with a false kill premise still to correct",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S51",
      "2981c4bd72 (ancestor of HEAD): fix(/canonical-flow SKILL.md:222) -- a kill does NOT destroy on-disk bytes, discharging Z-S22's residual",
      ".claude/skills/canonical-flow/SKILL.md:250-253 at HEAD: 'CORRECTED 2026-09-13 ... THIS LINE USED TO SAY A KILL WOULD HAVE DESTROYED 189 KB OF UNCOMMITTED WORK AND THAT IS FALSE'",
      "Child Z-S22 reads DISARMED/REMEDIATED in remediations/REMEDIATION_v5.md"
    ],
    "remedy": "The CTO corrected the false recovery premise in /canonical-flow: a kill loses in-flight context, not on-disk bytes; the class and output-plane probe stay.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-13T01:30Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S72",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W12-S4: The unsafe only-private-object instruction is retained as issued evidence",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S72",
      "bb9009c924 (ancestor of HEAD): rf-6 drain records gitlink 83cc87f2 after the fetch; row Z-S32 (120d313474) records both controls",
      "git -C portal cat-file -t 83cc87f29d92462ce54ae8b230bb4c9f05a4dc64 -> commit; bogus ...a4dc00 -> could not get object info (read this session)",
      "git -C portal merge-base --is-ancestor 83cc87f2 origin/DEV -> true (read this session)"
    ],
    "remedy": "The issuer fetched portal 83cc87f2 into the shared portal clone under a branch ref before the drain moved the gitlink (Z-S32); the object is now on portal origin/DEV. Future pointer moves still need their own grant.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-12T21:43Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S82",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W11-S2: The amended grant includes the package entrypoint and source map, and comp-iam now names three adapter sites",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S82",
      "62d6daf36c (ancestor of HEAD): ri-4 proof, THE MOUNT IS DEPLOYED -- 8 of 8 PASS-by-output, 19 added 0 changed 0 destroyed",
      "50064d78f5 (ancestor of HEAD): ri-4 drain, opal-amgt-scoped-api Active, 11 routes on 7k3ed8px20 (85 -> 96)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-4.the-mount-deployed.md and TO-AMGT-rf-2.the-mount-and-its-iam.md: last <status> complete; ledger org/critical_paths/change_management/20260915T0345Z_amgt-scoped-api-mount_deploy_completion.md (closed at bd5bad4156)"
    ],
    "remedy": "The packaging, artifact upload and served route were finished by ri-4: opal-amgt-scoped-api deployed with 11 /api/scoped/amgt routes under a closed NEVER-2 entry.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-15T04:07Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S101",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S44: The missing L10.r5/r6 sidecars are independently confirmed by the recorded stamp listing",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S101",
      "00e0813b9d (ancestor of HEAD): adds org/missions/D5/AMGT/AMGT_RESAPP/prd/stamps/L10.r5.json and L10.r6.json",
      "org/missions/D5/AMGT/AMGT_RESAPP/prd/stamps/L10.r5.json at HEAD: note 'Late stamp written now for the round-5 L10 slug committed 2026-09-11 at bd523222a1 ... utc is backfill time'",
      "Child Z-S44 reads DISARMED/REMEDIATED in remediations/REMEDIATION_v7.md"
    ],
    "remedy": "The CVO wrote the two canonical L10 stamps with explicit backfill notes; historical slug pins are preserved.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-13T00:10Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S122",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W13-S7: The old guarded snapshot/unconditional restore could create a wrong-path file from stale scratch bytes",
    "evidence": [
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S122",
      "3981fe738c (ancestor of HEAD): rg-2 amendment converts AC2 and AC4 to judgment; no <invocation> remains on AC4",
      "4d7652ef3f (ancestor of HEAD): row Z-S58 disarms Z-W13-S7 by both limbs, snapshot 10761 bytes removed and re-tested absent",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rg-2.the-incomplete-read-at-the-chart.md: last <status> complete"
    ],
    "remedy": "The issuer retired rg-2 AC4's invocation (now a judgment criterion), and the stale /tmp/rg2.pre snapshot was measured and removed (Z-S58).",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T02:03Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S143",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT_RESAPP-Z-S67: A negative token copied into the order authority ceases to be absent from that corpus. This changes the control, not whether the 15 declared FWDs have cells.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.md#AMGT_RESAPP-Z-C-S143",
      "e9d1c6e6a5 (ancestor of HEAD): round-9 analysis, coverage subtraction with run-time controls",
      "org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round10.md:31 at HEAD: 'NEGATIVE CONTROLS, run time: FWD-99 -> 0 FWD-0 -> 0 FWD-42 -> 0'; :134 records Z-S67 discharged",
      "008ca40b6c (ancestor of HEAD): disarm row for Z-S67 by 1.0.0_SA_CTO~W citing both analyses"
    ],
    "remedy": "The CTO's coverage read now establishes its negative controls at run time (FWD-99, FWD-0, FWD-42 -> 0), from round 9 on.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-14T15:10Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S154",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT_RESAPP-Z-S72: The issuer observed a mounted empty default view, not populated figures or prose. Its explanation that the daily job wrote no row is not established by that screen: CVO renders identical 205-byte output for request failure and successful empty data in the actual LeadPanel/RankedList. See the separate CVO error/empty finding.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.md#AMGT_RESAPP-Z-C-S154",
      "portal 9aef3734 (ancestor of the pinned gitlink ec65c5d6): fix(AMGT-ri-1) a settled read failure is no longer rendered as an empty day",
      "portal ec65c5d6:src/pages/SecurityAnalysis/components/RankedList.tsx:30-36 and :87-88: readError carried separately from rows, citing the round-9 error_equals_empty finding; LeadPanel.tsx:422-425 passes rankingQuery.error",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-1.the-error-empty-boundary.md: last <status> complete"
    ],
    "remedy": "ri-1 split the settled read error from the empty day: RankedList renders LOADING, READ FAILURE and EMPTY as separate states, so a failed request can no longer read as 'no row today'.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-15T01:15Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W58-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AC2's own hardcoded fixture filename ('.fixture-AMGT-rk-58.direct-act.md') cannot pass to-pipeline-gate.py's check_file regardless of what the minter renders: check_project_stage's _project_of() requires the basename to start with an uppercase PROJECT code, and a leading '.' never matches, so the invocation prints gate_violations 1 of 1, not the 0 AC2's own expect names.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W58-S1",
      "7a5c818ff1 (ancestor of HEAD): acceptance repair on rk-58 -- AC2 fixture name in PROJECT.TO-NAME form; row W58-S1",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-58.direct-act-minted-order.md at HEAD: fx = '.../task-orders/AMGT_RESAPP.TO-AMGT-rk-58-fixture.direct-act.md'; last <status> complete; :110 'W58-S1 ... was remedied by the issuer's repair'",
      "adjudications/ADJUDICATION_v14.md:542 and :561: W58-S1 DISMISSED_WITH_REASON, fixture renamed at 7a5c818ff1"
    ],
    "remedy": "The issuer renamed rk-58 AC2's fixture to PROJECT.TO-NAME form, so the gate's filename limb can pass; rk-58 is complete.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-19T02:46Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W39-S5",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two PRE-EXISTING, off-task test failures in lib/research/api/tests/test_generation_and_pool_routes.py (test_13_management_is_M1_with_the_pool_average_at_the_same_as_of, test_13b_the_ceo_profile_reading_separates_the_two_absences) both assert ceo_profile_reading(...)['reading'] == 'NOT_CONFIRMED_NOTHING_FOUND' on a 0-url ABSENT input, but the live function now returns 'NOT_SEARCHED' for that same input -- present at this worktree's HEAD before any AMGT-rk-37 edit, unrelated to this cell's surface.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W39-S5",
      "4f376072d9 (ancestor of HEAD, merged by ec880933eb): rk-63 repairs test_13/test_13b's two orphaned assertions",
      "lib/research/api/tests/test_generation_and_pool_routes.py:528 at HEAD asserts not_searched[\"reading\"] == \"NOT_SEARCHED\"",
      "adjudications/ADJUDICATION_v14.md:541 and :556: W39-S5 DISMISSED_WITH_REASON, re-run 24 passed 0 failed"
    ],
    "remedy": "rk-63 repaired test_13/test_13b's two orphaned assertions to the live NOT_SEARCHED reading.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-21T13:57Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S6",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATES, AND IT IS THE ONE ROW WHOSE DISPOSITION IS NOT THE END OF ITS STORY: W9-S2 is the external TLS block on AMGT-s-b4. astn/brightdata/residential-proxy TLS-intercepts every HTTPS GET with an untrusted 'Bright Data Proxy Root CA' leaf no standard client can verify, so all 9 attempted GETs across 3 tickers failed AT THE HANDSHAKE, before reaching Seeking Alpha, and AC1 honestly reads 0 of 3 landed. STAR: THE GRADE THAT MATTERS HERE IS THE ONE THE ROW ARGUES FOR AND I CONFIRM: THIS IS NOT A DEFECT IN THE ORDER'S OWN WORK. The fetcher, the detectors and the logging are sound and AC2 through AC6 all pass; the deliverable is otherwise complete and the failure is an HONEST TLS FAIL at a layer outside the cell's write surface. An externally-blocked criterion that reports its own blockage accurately is behaving correctly -- it is the one shape of failure that should NOT be re-cut.",
    "evidence": [
      "adjudications/ADJUDICATION_v1.md#AMGT_RESAPP-Z-C-S6",
      "Adjudicates Z-W9-S2, whose row in remediations/REMEDIATION_v1.md is DISARMED/REMEDIATED (closed true): the TLS block was a client-side default, not external",
      "0d02e7ce47 (ancestor of HEAD, 2026-09-11T02:26Z): sa_rest_fetch.py session carries verify False for the SSL-bumping proxy",
      "org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py:111 at HEAD: kwargs = {impersonate chrome, timeout 70, verify False}",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-b4.seeking-alpha-backend-the-measured-route.md last <status>complete</status> (re-run landed 18 objects, 3 of 3 tickers)"
    ],
    "remedy": "Fixed: the client-side proxy default landed in the committed fetcher and s-b4 re-ran to completion; no re-cut of the fetcher is owed.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-11T02:26Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S326",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED: the crosswalk read is unpinned -- _read_pool_latest takes sorted(keys)[-1] over crosswalk/v1/ with no key-shape filter, and the page route reads it.",
    "evidence": [
      "adjudications/ADJUDICATION_v14.md#AMGT_RESAPP-Z-C-S326",
      "Adjudicates Z-W54-S2, whose row in remediations/REMEDIATION_v14.md is DISARMED/REMEDIATED (closed true)",
      "0164b134ac (ancestor of HEAD, 2026-09-21T15:38Z): rk-68 crosswalk pool-vintage key-shape filter, resolved key recorded beside the document",
      "lib/research/identity/crosswalk.py:72 CROSSWALK_KEY_RE and :1176 refusal of any non-dated key inside _read_pool_latest (:1160) at HEAD",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-68.crosswalk-key-shape-filter.md last <status>complete</status>"
    ],
    "remedy": "Fixed per the CTO ruling: rk-68 refuses non-dated keys loudly; newest-dated-wins stays and the resolved key is recorded.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-21T15:38Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S371",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED: the PRINT route serves a 500 for all three validation names (CAT, CSL, 6861) -- render_pack sorts model-block fiscal years stored as a mix of str and int; pre-existing, not caused by M3.",
    "evidence": [
      "adjudications/ADJUDICATION_v24.md#AMGT_RESAPP-Z-C-S371",
      "Adjudicates Z-S215, whose row in remediations/REMEDIATION_v14.md is DISARMED/REMEDIATED (closed true)",
      "5357068676 (ancestor of HEAD): _fiscal_year_sort_key normalises mixed str/int fiscal years in render_pack.py",
      "lib/research/print/render_pack.py:217 _fiscal_year_sort_key; :308 and :968 sorted(by_fy, key=_fiscal_year_sort_key) at HEAD",
      "f16e253426 (ancestor of HEAD, 2026-09-22T08:32Z): opal-amgt-scoped-api redeployed with the fix, deploy ledger opened and closed",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-94.print-pack-fiscal-year-sort.md last <status>complete</status>"
    ],
    "remedy": "Fixed: rk-94 sorts fiscal years on a normalised key and the adapter was redeployed; the print route no longer 500s on mixed year types.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-22T08:32Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S413",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMENDS Z-C-S412's blast radius: the deployed authorizer accepts ORDINARY VERIFIED PORTAL JWT IDENTITIES, not only internal/dev, so the 179 held-but-served sentences reached a served audience rather than an engineering one. Classification stays INCIDENT and the remedy stays double; what grows is the second half -- re-opening what the gap admitted.",
    "evidence": [
      "adjudications/ADJUDICATION_v46.md#AMGT_RESAPP-Z-C-S413",
      "Amends Z-C-S412 (ADJUDICATION_v45): remedy is double -- runtime enforcement, plus re-opening the served documents under the never-widen pair",
      "Half 1, runtime enforcement: dd91fd3126 (ancestor of HEAD) holds unanchored drafted sentences at both API consumers; lib/research/api/scoped_amgt.py:2460-2476 skips every sentence with no non-blank quoted span and counts it in held_no_span_at_read at HEAD",
      "Half 1 on the deployed plane: 4cb1b6b009 (ancestor of HEAD) CVO acceptance -- live CodeSha256 matches the signed candidate; 210 served / 179 held / zero spanless across all twelve documents",
      "Half 2, the stored objects: never-widen pair COO half 18ac256769 and CTO half 04f779ac51; bcada3e9ea (ancestor of HEAD, 2026-09-30T20:39Z) AMGT-ad-2 held 179 no-span sentences on 12 stored D-1 documents; 2e9c087db4 closes ad-2 ACCEPTED"
    ],
    "remedy": "Fixed on both halves: the deployed adapter holds no-span sentences at read, and ad-2 re-opened the 12 stored documents under the signed never-widen pair, so the ordinary-portal audience no longer receives held text.",
    "owner": "1.0.0_SA_CTO",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-30T20:39Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S31",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Per-ticker computation lacked a canonical universe input contract",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S31",
      "fda8d96c0a (ancestor of HEAD, 2026-09-15T09:19Z): AMGT-rj-5 moves the producer onto the pool; the universe source becomes INTERFACE U-1",
      "lib/research/metrics/chatter_axis.py:47-49 and :163 POOL_UNIVERSE_PREFIX universe/v1/ at HEAD: the canonical input is the pool's union universe universe/v1/<as_of>.json",
      "lib/research/metrics/chatter_axis.py:274-293 at HEAD: read_universe_names returns (entries, provenance); the worker-numbered universe.json is only a fallback and the fallback and its reason are carried on the provenance",
      "infra/aws/terraform/harvest/lambda_src/build_zip.py:29-31 at HEAD labels the baked universe_snapshot.json as the producer's FALLBACK, not its source"
    ],
    "remedy": "Fixed: the producer reads a named canonical universe (pool universe/v1, INTERFACE U-1) with provenance; the frozen worker copy is a disclosed fallback only.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-15T09:19Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S37",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Artifact identity cannot be inferred from a recent filesystem timestamp",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S37",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S81: the named holder 1.0.0_SA_CTO~Z ruled the file GENERATED TEST OUTPUT, keyed on the VINTAGEID sentinel, not a deliverable",
      "9d819f151f (ancestor of HEAD, 2026-09-14T08:24Z): the ruling ships with an exact-path .gitignore rule, never a glob",
      ".gitignore:238 at HEAD; git check-ignore -v on the file returns that rule and git status --ignored reads it as ignored (!!), so it no longer surfaces as an untracked peer artifact"
    ],
    "remedy": "Fixed by the holder's classification ruling plus an exact-path ignore rule; a future real model_block_fye_* file is still seen.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-14T08:24Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S46",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A migration message cited a different tree from the worker pin",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S46",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S59 (1.0.0_SA_CTO~Z, 2026-09-13): Z-C-S46 STAYS LIVE -- a handoff must carry path plus commit plus current resource identifier",
      "No later row, commit or skill/doctrine text carries that handoff rule: git log --all --grep for Z-C-S46 returns only the Z-S59 commits (6d30c11bbc, 5495d05415); Grep for 'resource identifier' / 'path plus commit' over .claude/skills, org/ref, docs/doctrine and CLAUDE.md returns 0 files"
    ],
    "remedy": "Still owed: state the handoff rule (path plus commit plus current resource identifier) in a carrier a migrating seat reads; nothing at HEAD shows it.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-10-06T22:04:38Z"
    },
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80",
      "closure": {
        "reason": "NOT_A_DEFECT",
        "pointer": "org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md@4a89bef967 section E: a law proposal, not a RESAPP defect"
      }
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S52",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "rd8 used two insufficient instruments: a references-only no-emit check that examined no source, and a fixture render that did not exercise the page",
    "evidence": [
      "adjudications/ADJUDICATION_v6.md#AMGT_RESAPP-Z-C-S52",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-8.lead-panel-and-three-tabs.md last <status>superseded</status>; AMGT_RESAPP.TO-AMGT-re-1.lead-panel-recut.md last <status>complete</status> (forced compiler build, real route tree)",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rg-1.the-consumer-join.md and AMGT_RESAPP.TO-AMGT-rg-3.the-control-shown-to-fire.md last <status>complete</status>: populated join PRE-REPAIR fiscal 0/183 against REPAIRED 183/183 with a firing control",
      "8f4f4a89fa (ancestor of HEAD, 2026-09-13T05:57Z): TO-AMGT-rh-1 complete -- four real route modules served as distinct transformed bodies against a control that fires",
      "Print consumer: rk-94 fix 5357068676 and redeploy f16e253426 (ancestors of HEAD) serve /print 200 through the real adapter"
    ],
    "remedy": "Fixed: the recut chain (re-1, rg-1, rg-3, rh-1) replaced both substitute instruments with real-route, populated evidence and firing controls; rd-8's AC2/AC4 FAIL stand as history.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T05:57Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S74",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S33: The shared gitlink could serialize otherwise disjoint file work",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S74",
      "Adjudicates Z-S33, whose row in remediations/REMEDIATION_v7.md is DISARMED/REMEDIATED (closed true), landed at 00e0813b9d (ancestor of HEAD, 2026-09-13T00:10Z)",
      "Condition (a) held: rf-1..rf-5 drains moved no portal pointer and the queue read 0 of 43 open"
    ],
    "remedy": "No act owed: the hazard's alternative condition already held and its original's row is closed.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T00:10Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S84",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W11-S4: The exact security key was amended at 5dc02a83d5 and rerun",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S84",
      "Adjudicates Z-W11-S4, whose row in remediations/REMEDIATION_v7.md is DISARMED/REMEDIATED (closed true), landed at 00e0813b9d (ancestor of HEAD, 2026-09-13T00:10Z)",
      "Exact security key amended at 5dc02a83d5; CVO re-read HEADER=13 FISCAL=183 TOTAL=196"
    ],
    "remedy": "No act owed: the criterion repair executed and its original's row is closed.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T00:10Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S104",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S47: The round closes with every portal-dependent result EXERCISED-NOT-REALIZED",
    "evidence": [
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S104",
      "Adjudicates Z-S47, whose row in remediations/REMEDIATION_v8.md is DISARMED/REMEDIATED (closed true), landed at a51f860e36 (ancestor of HEAD, 2026-09-13T03:48Z)",
      "Condition (b) met by the round's object-scoped EXERCISED-NOT-REALIZED grades"
    ],
    "remedy": "No act owed: condition (b) held and its original's row is closed.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-13T03:48Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S123",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S57: S59 reads the seven omitted AMGT carriers, but S57's explicit disarm also requires finishing the POSN standing read",
    "evidence": [
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S123",
      "Adjudicates Z-S57, whose row in remediations/REMEDIATION_v8.md flipped ARMED (at a51f860e36) to DISARMED (at 1ae76e9c83, ancestor of HEAD, 2026-09-14T14:47Z), closed true",
      "adjudications/ADJUDICATION_v9.md:13 and :52-71: the bounded POSN paired read over both roots and both block shapes completed; S53/S57 advanced as one completed obligation"
    ],
    "remedy": "No act owed: the residual POSN standing read was finished and its original's row is closed.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-14T14:47Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S144",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT_RESAPP-Z-S68: The historical 63 armed count names neither a plane nor a grain. Investigation disarm_owner and remediation owner/disarm are different schema fields; no unowned-remediation claim follows from querying the wrong field.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.md#AMGT_RESAPP-Z-C-S144",
      "Adjudicates Z-S68, whose row in remediations/REMEDIATION_v9.md flipped ARMED (at 1ae76e9c83) to DISARMED (at e28f0b546c, ancestor of HEAD, 2026-09-15T05:51Z), closed true"
    ],
    "remedy": "No act owed: the plane/grain/denominator condition was met and its original's row is closed.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-15T05:51Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S164",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT_RESAPP-Z-S82: The shared-home read could attribute a base artifact to a lane. S83 is the named-owner disarm, and current canonical-flow plane(b) now explicitly requires an anchored serial author and says an unscoped home is not lane evidence.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.md#AMGT_RESAPP-Z-C-S164",
      "Adjudicates Z-S82, whose row in remediations/REMEDIATION_v9.md is DISARMED/REMEDIATED (closed true), landed at 1ae76e9c83 (ancestor of HEAD, 2026-09-14T14:47Z)",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S83: named-owner disarm, canonical-drive rung scopes the tier-1 read by anchored author, verified by blob id with a firing negative control"
    ],
    "remedy": "No act owed: the author-scoped reading rule is in the served skill and its original's row is closed.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-14T14:47Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W53-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The chain L CTO half (NEVER_WIDEN_ROUND14_CHAIN_L_CTO_HALVES.md) is absent from this worktree; only the COO half exists.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W53-S1",
      "ce9231d095 (ancestor of HEAD, 2026-09-19T06:53Z): 1.0.0_SA_CTO~Z writes the chain L CTO half for rk-53",
      "org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_L_CTO_HALVES.md:15 at HEAD carries the AMGT-rk-53 section",
      "adjudications/ADJUDICATION_v14.md#AMGT_RESAPP-Z-C-S341: DISMISSED -- absent from one worktree, present in the estate",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-53.no-rank-without-signal.md last <status>complete</status>"
    ],
    "remedy": "No act owed: the missing CTO half existed in the estate before the worker's base caught up; the pair is complete at HEAD.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-19T06:53Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W119-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "TO-AMGT-rk-119's literal AC0 script (section 5) crashes rc=1 before its decisive line: `cw._read_pool_latest()` returns a 2-tuple `(document, key)`, not a document dict, so `.get(\"records\")` raises AttributeError; worked around in the scratch copy only by unpacking the tuple, then AC0 ran clean and refused the run exactly as the order predicted.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W119-S1",
      "adjudications/ADJUDICATION_v35.md#AMGT_RESAPP-Z-C-S398 (c79b5c10fe, ancestor of HEAD, 2026-09-22T22:14Z): DISMISSED -- issuer-text defect caught by the worker at execution, no served value reached, class remedy adopted at L6",
      "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-119.lenovo-seeking-alpha.md last <status>complete</status>: the order is terminal, so its literal AC0 script is not re-run",
      "lib/research/identity/crosswalk.py:1160 _read_pool_latest still returns (document, key) at :1184; every in-module caller unpacks it (:1139 document, key = ...; :1366 and :1489 index [0]), so only a copied private-call script is exposed"
    ],
    "remedy": "No act owed: the defect was in a terminal order's literal text, dispositioned at L9 with its class remedy at L6.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-22T22:14Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S328",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED (EXPOSURE, never fired): model_block_pull._latest_stamp takes the newest raw/bloomberg stamp with no content check, and two writers put non-raw objects in their own stamps -- derive would crash on NoSuchKey instead of reading absent.",
    "evidence": [
      "adjudications/ADJUDICATION_v14.md#AMGT_RESAPP-Z-C-S328",
      "06296daccd (ancestor of HEAD) build(AMGT-rk-70): _latest_stamp requires both refdata.json and histdata.json and raises NoRawStampError instead of NoSuchKey",
      "integrations/bloomberg/research/model_block_pull.py:708-716 at HEAD: _latest_stamp takes qualifying = _stamps_with_raw_pair(...) and raises NoRawStampError when none qualifies",
      "task-orders/AMGT_RESAPP.TO-AMGT-rk-70.latest-stamp-requires-raw-pair.md last <status> complete",
      "remediations/REMEDIATION_v14.md#AMGT_RESAPP-Z-W38-S5 (the adjudicated item) REMEDIATED on the same commit"
    ],
    "remedy": "Remedied by AMGT-rk-70: _latest_stamp only returns a stamp carrying the refdata+histdata pair and reports absence as NoRawStampError.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-21T16:19Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S372",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED: the SERP primitive's records carry no per-page tag, so a multi-page harvest cannot give each silver row its exact page_bronze_key.",
    "evidence": [
      "adjudications/ADJUDICATION_v24.md#AMGT_RESAPP-Z-C-S372",
      "lib/research/harvest/bright_data_serp.py:128-132 at HEAD: every row still takes the last page's bronze key (page_bronze_key = bronze_receipts[-1]); no refusal of max_pages > 1",
      "lib/research/harvest/bright_data_serp.py:81 at HEAD: harvest_serp(..., max_pages=1, ...) accepts any max_pages silently; git grep finds no non-test caller (only lib/research/harvest/tests/test_bright_data_serp.py)",
      "remediations/REMEDIATION_v14.md#AMGT_RESAPP-Z-W88-S1 (the adjudicated item) OPEN, ARMED"
    ],
    "remedy": "Open: the wiring cell that uses max_pages=1 or refuses multi-page fetches does not exist yet; the writer is dormant (no caller) but not disarmed.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-10-09T20:19:00Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S24",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Legacy version fallback can admit changed brief bytes",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S24",
      ".tools/prd_signoff_lib.py:227-232 at HEAD: evaluate() still falls back to `current = str(doc.get('prd_version')) == version` when a record has neither endpoint_hash nor half_hash",
      ".tools/prd_signoff_lib.py:207-208 docstring at HEAD still reads 'CURRENT = half_hash equals the PRD's (or, legacy, prd_version equals)'",
      "110378a08c and 888c678c50 (ancestors of HEAD) changed only the STALE/current detail text, not the legacy branch",
      "org/missions/D5/AMGT/AMGT_RESAPP/prd/signoff/4.0.0_SA_CRO.json at HEAD is still a legacy record (prd_version v0.4, no half, half_hash or signed_at)",
      "remediations/REMEDIATION_v5.md#AMGT_RESAPP-Z-S6 (the adjudicated item) OPEN, ARMED"
    ],
    "remedy": "Open: the sign-off gate owner still owes byte-bound records (retire or re-sign legacy version-bound files) and a red changed-bytes control on the legacy branch.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-10-06T21:23:00Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S32",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Packaging exposed the same singleton-provider grant gap",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S32",
      "ea6cd450fa (ancestor of HEAD) consolidate(ri-2): chatter-axis-schedule.tf and lambda_src moved into infra/aws/terraform/harvest/; the amgt-resapp root is gone",
      "6fdfe5b25e (ancestor of HEAD) deploy(AMGT H03 2a): the function deploys through modules/yang-lambda from a VERSIONED S3 artifact whose content-sha256 metadata is the source_code_hash",
      "infra/aws/terraform/harvest/chatter-axis-schedule.tf:43-55 at HEAD: 'THE ARTIFACT OF RECORD IS AN S3 OBJECT'; build_zip.py builds, build-and-upload-chatter-axis.sh uploads with content-sha256, BUILD AND UPLOAD FIRST, THEN PLAN",
      "f31a81acc6 (ancestor of HEAD) harvest(AMGT-ad-3): one verified upload for every build-and-upload*.sh",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S264 (6e9a09119e): the issuer adjudicates Z-W2-S7; rd-5 complete"
    ],
    "remedy": "The static zip now has a rebuild/hash contract: the deployed bytes are a versioned S3 artifact whose content hash drives source_code_hash (6fdfe5b25e), so a stale manual zip can no longer pass as the current deployment.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-24T05:17Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S39",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The portal artifact carries a promotion-base coupling",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S39",
      "portal: 5b959f63 (the worker base carrying the IRPT chain) and e6057f26 (the Lead Panel) are both ancestors of origin/DEV and origin/PROD (git -C portal merge-base --is-ancestor, read 2026-10-04)",
      "portal 1193bed8 (2026-09-23T04:36Z) is the first origin/DEV first-parent commit containing e6057f26",
      "superproject HEAD gitlink portal = ec65c5d637, which contains both 5b959f63 and e6057f26",
      "remediations/REMEDIATION_v5.md#AMGT_RESAPP-Z-S16 (the adjudicated item) DISARMED, REMEDIATED"
    ],
    "remedy": "The coupled base is integrated: the IRPT chain and the Lead Panel are both on portal DEV and PROD, so no promote decision is left hostage to an unpromoted base.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-23T04:36Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S47",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Object preservation succeeded while portal integration remains held",
    "evidence": [
      "adjudications/ADJUDICATION_v5.md#AMGT_RESAPP-Z-C-S47",
      "bb9009c924 (ancestor of HEAD) drain(AMGT-rf-6): 'portal objects fetched before the gitlink moved'; the first superproject commit whose portal gitlink (83cc87f29d) contains e6057f26 and c67281460a",
      "git -C portal ls-tree -r --name-only 83cc87f29d -- src/pages/SecurityAnalysis | wc -l -> 18; at the HEAD gitlink ec65c5d637 -> 77",
      "portal: e6057f26 is an ancestor of origin/DEV and origin/PROD (read 2026-10-04)",
      "remediations/REMEDIATION_v5.md#AMGT_RESAPP-Z-S21 (the adjudicated item) carries the same hazard"
    ],
    "remedy": "The recorded gitlink moved past the Lead Panel at bb9009c924, so the work is referenced by the superproject and is no longer one branch delete away from loss; it has since reached portal DEV and PROD.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-12T21:43Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S55",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The issued AC3 mutates types.ts then restores from the index, rather than the pre-test working bytes",
    "evidence": [
      "adjudications/ADJUDICATION_v6.md#AMGT_RESAPP-Z-C-S55",
      "e588dc8d05 (ancestor of HEAD) issuance(round 8): every later mutation control snapshots the working tree, restores from the snapshot and proves byte identity with cmp",
      "task-orders/AMGT_RESAPP.TO-AMGT-rg-1.the-consumer-join.md:103-107 at HEAD: 'A MUTATION CONTROL SNAPSHOTS THE WORKING TREE, NEVER THE INDEX ... prove byte identity with cmp'; last <status> complete",
      "task-orders/AMGT_RESAPP.TO-AMGT-rf-2.the-mount-and-its-iam.md:149 (round 7) already restores from a /tmp snapshot instead of git checkout --",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S264 (6e9a09119e): the issuer adjudicates Z-W10-S1 -- no face cut since names a checkout/clean limb",
      "remediations/REMEDIATION_v6.md#AMGT_RESAPP-Z-W10-S1 (the adjudicated item) carries the same hazard"
    ],
    "remedy": "The instrument was recut: mutation controls copy the file to a scratch snapshot, restore from it and prove byte identity, instead of git checkout -- from the index.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T00:42Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S64",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Late S27: a rerun without adapter call-site and role coverage cannot resolve the IAM gap",
    "evidence": [
      "adjudications/ADJUDICATION_v6.md#AMGT_RESAPP-Z-C-S64",
      "271e8f8b43 (ancestor of HEAD) feat(AMGT-rf-2): one infra/aws/lambda/ci/lambda-source-map.json entry makes comp-iam verdict the adapter -- 835 -> 838 calls, the three new lines are scoped_amgt.py:293/:315/:522, positive control steady at 37",
      "the same commit adds the missing grant comp-iam found (Sid ReadTheArticleStoreForTheCoverageTab for read_coverage_set)",
      "88eefbfb5e (ancestor of HEAD) drain(rf-2 + rf-3); task-orders/AMGT_RESAPP.TO-AMGT-rf-2.the-mount-and-its-iam.md last <status> complete",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S264 (6e9a09119e): the issuer adjudicates Z-S27 -- the mount answers the edge's 401 on every AMGT path",
      "remediations/REMEDIATION_v6.md#AMGT_RESAPP-Z-S27 (the adjudicated item) carries the same hazard"
    ],
    "remedy": "The adapter's call sites and role binding were put in comp-iam's denominator through the source map (271e8f8b43); the instrument then verdicted them and the one missing grant was added.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-12T22:48Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S75",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S34: Local fetch repaired object preservation, and the attempted pointer was backed out before the held superproject push",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S75",
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S137 (a51f860e36): 'S34 on the documented bounded remote-plane drain step'",
      "remediations/REMEDIATION_v7.md#AMGT_RESAPP-Z-S34 (the adjudicated item) DISARMED, REMEDIATED",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S264 (6e9a09119e): every drain resolves the gitlink explicitly to the merged portal DEV head, and the one-trunk rule has MSTR push the portal with the workspace",
      "read 2026-10-04: HEAD gitlink portal ec65c5d637 is an ancestor of portal origin/DEV and origin/PROD, so the published pointer resolves on the remote"
    ],
    "remedy": "The remote-plane reachability step was documented in the drain (accepted at C-S137), and drains now point the gitlink at the pushed portal DEV head; the HEAD pointer resolves on origin.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T03:48Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S85",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W11-S5: The amended direct-model control measures POSITIVE=183 WRONG_SCOPE=0, fixing the old absent model_block-key vacuity",
    "evidence": [
      "adjudications/ADJUDICATION_v7.md#AMGT_RESAPP-Z-C-S85",
      "3288378d18 (ancestor of HEAD) feat(AMGT-rg-3): rf-3 AC3's negative arm driven to WRONG_SCOPE=196 by two independent loosenings, then restored",
      "1dea673348 (ancestor of HEAD) drain(AMGT-rg-3); task-orders/AMGT_RESAPP.TO-AMGT-rg-3.the-control-shown-to-fire.md last <status> complete",
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S137 (a51f860e36): 'W11-S5 closes on the measured matcher mutant and restoration'",
      "remediations/REMEDIATION_v7.md#AMGT_RESAPP-Z-W11-S5 (the adjudicated item) DISARMED, REMEDIATED"
    ],
    "remedy": "The named loosened-matcher mutant was executed by rg-3 (196/196 under loosening, back to 183/0 after exact restore) and the CVO accepted it at C-S137.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T01:12Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S106",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S49: A materialized clean portal can make its parent gitlink dirty before worker activity",
    "evidence": [
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S106",
      "remediations/REMEDIATION_v8.md#AMGT_RESAPP-Z-S49 (the adjudicated item) DISARMED, REMEDIATED on the same-sweep nested porcelain probe",
      "a51f860e36 (ancestor of HEAD) adjudicate(round 8): this row's own note accepts the measured owner probe as the literal disarm",
      "No act owed: the row records a measurement obligation that the S60 sweep met"
    ],
    "remedy": "No act owed: the nested-porcelain probe that discriminates issuer dirt from worker movement was measured and accepted as the disarm.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T03:48Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S126",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S60: A reused worktree contains issuer staging and predecessor artifacts",
    "evidence": [
      "adjudications/ADJUDICATION_v8.md#AMGT_RESAPP-Z-C-S126",
      "remediations/REMEDIATION_v8.md#AMGT_RESAPP-Z-S60 (the adjudicated item) DISARMED, REMEDIATED",
      "a51f860e36 (ancestor of HEAD) adjudicate(round 8): the row's own sweep satisfies its named probe condition",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S264 (6e9a09119e): closed by mechanism -- .tools/wk-provision.sh provisions a fresh worktree per slot and remove deletes it at the drain"
    ],
    "remedy": "No act owed for the measurement; worktree reuse is also gone, since wk-provision.sh provisions a fresh worktree per slot and deletes it at the drain.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-13T03:48Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S145",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT_RESAPP-Z-S69: Direct inspection confirms all six W15 rows carry site-z and the Z-W15 infix; none changes fabric to clear the gate. The drain half is met. The condition also requires the next spawn to quote the channel grammar and that future half is not established here.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.md#AMGT_RESAPP-Z-C-S145",
      "e28f0b546c (ancestor of HEAD) round-10 adjudication: Z-S69 advanced to REMEDIATED/DISARMED/closed on the completed evidence in REMEDIATION_v10.md and ADJUDICATION_v10.md",
      "remediations/REMEDIATION_v9.md#AMGT_RESAPP-Z-S69 (the adjudicated item) DISARMED 2026-09-15T05:43:30Z",
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S264 (6e9a09119e): worker prompts quote the channel header's grammar"
    ],
    "remedy": "The future half was met: later spawns quote the channel header grammar, and the round-10 adjudication closed Z-S69 on that evidence.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-15T05:51Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S166",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AMGT_RESAPP-Z-S84: A zero author-filter result alone cannot distinguish a quiet valid lane from a nonexistent one. S85 supplies the controlled-anchor disarm; current canonical-flow plane(a) states both the external-window positive control and INCONCLUSIVE when it fails.",
    "evidence": [
      "adjudications/ADJUDICATION_v9.md#AMGT_RESAPP-Z-C-S166",
      "1ae76e9c83 (ancestor of HEAD) round-9 adjudication: Z-S84 DISARMED/REMEDIATED on the implemented probe correction",
      ".claude/skills/canonical-flow/SKILL.md:165 at HEAD: plane (1) COMMITS -- 'MOVING certifies itself and COLD certifies nothing: a 0 is IN[CONCLUSIVE]'",
      "remediations/REMEDIATION_v9.md#AMGT_RESAPP-Z-S84 (the adjudicated item) DISARMED, REMEDIATED"
    ],
    "remedy": "The probe correction is implemented: canonical-flow treats a zero author-filter read as inconclusive without a positive control.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-14T14:47Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W53-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "This worktree's portal/node_modules was a BROKEN symlink (target mangled to /c/C:/Users/... by MSYS path conversion at spawn-time provisioning), not the working junction the worker face's identity line asserted -- fixed in-session with a Windows junction to the main tree's portal/node_modules, no bun install run.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W53-S2",
      "b01a10ed75 (ancestor of HEAD) drain of rk-60: .tools/wk-provision.sh lands on CLOUD",
      ".tools/wk-provision.sh:132-147 at HEAD: the node_modules link is built with cygpath -w + cmd.exe mklink /J (no MSYS-converted target); :162-164 runs ./node_modules/.bin/tsc --version as a positive control",
      "adjudications/ADJUDICATION_v14.md#AMGT_RESAPP-Z-C-S339 (913a02de36): DISMISSED_WITH_REASON -- 'W53-S2: junction built by wk-provision.sh:129-135 (rk-60 drain b01a10ed75)'"
    ],
    "remedy": "Per-worker provisioning now builds the node_modules junction from a Windows path and checks tsc resolves through it (wk-provision.sh, rk-60), so the doubled-prefix symlink cannot recur.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-19T08:38Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W117-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "AC5's literal `git diff --name-only HEAD~1 HEAD -- integrations lib infra .tools portal` cannot show limb 1's two files at grading time, because this cell's execution spans TWO worker sessions with issuer amendments landing between limb 1's commit (630c3b1e14) and this session's grading pass: HEAD~1 is an amendment commit, not the parent of the limb-1 commit. The predecessor's earlier attempt (proof_of_spec instance AC5) hit the same grain mismatch and recorded it inline without filing a row.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W117-S4",
      "adjudications/ADJUDICATION_v35.md#AMGT_RESAPP-Z-C-S398 (c79b5c10fe): DISMISSED_WITH_REASON -- the class has an adopted L6 cutting practice; every instance was caught by a worker at execution and none reached a served value",
      "task-orders/AMGT_RESAPP.TO-AMGT-rk-117.lenovo-daily-price.md last <status> complete",
      "census 2026-10-04: 6 of 324 AMGT_RESAPP task orders carry HEAD~1, all rounds 12-31 and all complete; 0 of the 137 orders after round 31 do"
    ],
    "remedy": "The issuer's cutting practice adopted at C-S398 retired the HEAD~1 range; no order cut after round 31 uses it.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v80",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-22T22:14Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v80"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~Z
