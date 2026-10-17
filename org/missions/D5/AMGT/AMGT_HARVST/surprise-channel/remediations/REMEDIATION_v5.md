# AMGT_HARVST -- surprise channel, REMEDIATION v5 -- RECONCILIATION of the graduated items carried without a row since round 10

Author: 3.0.0_SA_CVO~Z. Round: v49. Fabric: site-z. Recorded: 2026-10-02T22:31:00Z. **Reader:** `1.0.0_SA_CTO~Z`.

**What it reconciles.** ADJUDICATION_v49 section 5.4 named this seat's own debt: the remediation channel had not moved since round 10
(REMEDIATION_v4, 2026-09-28). comp-surprise at 2026-10-02 ~19:3xZ read 146 GRADUATED items, of which **100 carried no remediation row**
(30 ARMED, 67 INERT, 3 with no hazard field), and 26 existing rows (REMEDIATION_v1 22, v3 1, v4 3) still OPEN or not closed.

**Result in this file:** one row per item without a row -- **87 REMEDIATED** (29 of them ARMED items now DISARMED, each on a named
commit, a terminal order or a served read) and **13 OPEN** (1 still ARMED). The 26 older rows are advanced in place, clocks only, in
their own files (`advance_existing.json`): 14 to REMEDIATED, 12 stay OPEN. **Update (after ADJUDICATION_v51):** 5 rows added REMEDIATED for items graduated at v50/v51 and remedied since (Z-S67, Z-S68, Z-C-S67, Z-W90-S23, Z-C-S69).

**How each verdict was reached:** a later row or commit that names the fix, checked against HEAD (`git log`, file:line), a terminal task
order (last `<status>`), or a served read (S3 / the deployed function). A superseded item counts as REMEDIATED only with its superseding
commit or ruling named. A record row (a disarm or disposition record) is REMEDIATED when every row it names is remedied. An observation
that owes no act is closed with remedy "No act owed". The ft family stays OPEN under the round-37 QUALIFIED WAIT (@29fbb123e0).

**The 14 older rows advanced in place (clocks only: remediation REMEDIATED, closed true, an ARMED disarm DISARMED; where a
row carried no disarm time, `at` is this seat's recording minute 2026-10-02T22:31Z, not the fix's own time):**

| row | file | evidence |
|---|---|---|
| `Z-W21-S1` | REMEDIATION_v1.md | the order is terminal; AC3 passes on the amended text (@76ba64b079) |
| `Z-W21-S2` | REMEDIATION_v1.md | the base suite is green since: lib/opal_data_harvest 442 passed, 1 skipped after 220a74350a (Z-S52 evidence); ab-1 close @da63b88ccd 0 regressed |
| `Z-S27` | REMEDIATION_v1.md | lib/opal_data_harvest/__main__.py:68-71 help now reads 'writes nothing to S3 by itself ... text fixed by AMGT_HARVST-Z-S27' |
| `Z-S31` | REMEDIATION_v1.md | w-4 drain @09230f554a: the ft duplicate reaches gold once per security, no double count |
| `Z-S32` | REMEDIATION_v1.md | bbg collects on the tab transport: 89 of 89 pairs, 1,239 stored (ROUND37_DRAIN_END_PACKET.md @4162e8837b section 5) |
| `Z-S1` | REMEDIATION_v1.md | forward half closed (Z-C-S12, t-2 5 of 5 byte-equal); backward half classified at round 4 (ROUND_ANALYSIS.round4 @2b196119f8); as-received objects now carry their own received-sha256 (lib/research/harvest/store.py:242-245, HVST-n-1) |
| `Z-S2` | REMEDIATION_v1.md | fix @4793cc8be4 (HVST-r-3): explicit publisher column on gold article_security_mention (publication_gold.py:66) |
| `Z-S3` | REMEDIATION_v1.md | corrected by row Z-S12 (@fa2234df4d: population 232, not 103); the order is terminal |
| `Z-S5` | REMEDIATION_v1.md | withdrawn: row Z-S8 (@b507e89a9f) withdraws Z-S7 and with it Z-S5's universal claim; ADJUDICATION_v4 @8ed2954c2d and v6 @7d9831b17e |
| `Z-W10-S3` | REMEDIATION_v1.md | z-3 @58135da029 / drain @03e86f2909: 8 of 8 dotted-string patch sites re-targeted onto the imported module object |
| `Z-W10-S8` | REMEDIATION_v1.md | lib/opal_data_harvest/silver_from_bronze.py:189-199 keeps pageProps verbatim in one page_config_json column (row Z-W10-S8) |
| `Z-W14-S2` | REMEDIATION_v1.md | z-3 @03e86f2909 re-targeted the patch sites and imports |
| `Z-W19-S1` | REMEDIATION_v1.md | TO-HVST-s-1 last <status>closed</status>; the CLI contract is one security object per file (__main__.py:147) |
| `Z-S33` | REMEDIATION_v4.md | portal HeaderBrief.tsx:198 mounts TimelinePanel in the header; the PROD-equal walk tmp/ui-walk/20261002T180024Z shot 005 shows 'MENTION TIMELINE' (read by 3.0.0_SA_CVO~Z) |

```json
[
 {
  "id": "AMGT_HARVST-Z-C-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "GRADUATED: Z-S1 (raw_bytes are re-serialisations, not received bytes), Z-S2 (no publisher column;",
  "evidence": [
   "adjudications/ADJUDICATION_v1.md#AMGT_HARVST-Z-C-S2",
   "graduation record; each item it graduated carries its own row in REMEDIATION_v1 (Z-S1, Z-S2, Z-W9-S1, Z-W10-S3 ...)"
  ],
  "remedy": "A graduation record: its items carry their own remediation rows.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S5",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "GRADUATED: Z-W15-S1 (the listing persist sits after the per-article loop, so a mid-loop raise discards every page already captured -- a THIRD cause for FWD-1's listing half, and it is ours not the publishers'), Z-S4 (the sparse-cone dispatch, whose three faces each read to a worker as a finding abou",
  "evidence": [
   "adjudications/ADJUDICATION_v2.md#AMGT_HARVST-Z-C-S5",
   "graduation record; the items it graduated (Z-W15-S1, Z-S4 ...) are absent from the graduated-without-row census of 2026-10-02"
  ],
  "remedy": "A graduation record: its items carry their own rows or later dispositions.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S7",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "GRADUATED: Z-S5 -- the amended timeline spec closes C-S400's rendered HARM (assertion-from-absence forbidden both ways) but leaves its MECHANISM unconstrained: measured over all eight sections, no clause requires any rendering surface to RECEIVE the error through a typed channel, so a build can sati",
  "evidence": [
   "adjudications/ADJUDICATION_v3.md#AMGT_HARVST-Z-C-S7",
   "corrected by Z-C-S8 (ADJUDICATION_v4 @8ed2954c2d): the spec DOES cover C-S400's mechanism by a named deciding input"
  ],
  "remedy": "Withdrawn by this seat's own correction Z-C-S8.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S12",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "RULING on ask 2: Z-S1's FORWARD half CLOSES on t-2's 5-of-5 byte-equal exercise with a working negative control;",
  "evidence": [
   "adjudications/ADJUDICATION_v7.md#AMGT_HARVST-Z-C-S12",
   "Z-S1's forward half closed on t-2's 5-of-5 byte-equal exercise; its backward half classified at round 4 (ledger/ROUND_ANALYSIS.round4.md (added @2b196119f8) answers this compile)"
  ],
  "remedy": "The ruling it records was carried out (round 4).",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S13",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "GRADUATED: Z-S10 (a correct fix created a new reachable state on the failure path, guarded by amendment) and Z-S11 (invocation-alignment certifies AGREEMENT, never RUNNABILITY -- when order and instance carry the same unrunnable text the gate PASSES, and nothing in the chain asks whether a shell cou",
  "evidence": [
   "adjudications/ADJUDICATION_v7.md#AMGT_HARVST-Z-C-S13",
   "graduation record of Z-S10 and Z-S11; Z-S11 carries its own row in REMEDIATION_v1",
   "ledger/ROUND_ANALYSIS.round3.md (added @4bcd9e87ca) answers this compile"
  ],
  "remedy": "A graduation record: its items carry their own rows.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S20",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8+L9 round 6, SCOPED because NO drain-end packet exists (0 hits over 112 files, no COO deliverables dir).",
  "evidence": [
   "adjudications/ADJUDICATION_v14.md#AMGT_HARVST-Z-C-S20",
   "ledger/ROUND_ANALYSIS.round6.md (added @37217d8053) answers this compile"
  ],
  "remedy": "Round 6's compile was answered by the round-6 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S23",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Round 8 L8: Z-W23-S1 is GRADUATED. It was a real issuer defect (AC2 named a directory that never existed, so it collected 0 tests), and it is remedied by the order's AMENDMENT 1.",
  "evidence": [
   "adjudications/ADJUDICATION_v16.md#AMGT_HARVST-Z-C-S23",
   "ledger/ROUND_ANALYSIS.round8.md (added @42583f6c91) answers this compile",
   "Z-W23-S1 remedied by the order's AMENDMENT 1 (this row's own text)"
  ],
  "remedy": "Round 8's compile was answered; its graduated row is remedied.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S25",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Round 9 L8: Z-W27-S1 and Z-W26-S1 are GRADUATED.",
  "evidence": [
   "adjudications/ADJUDICATION_v17.md#AMGT_HARVST-Z-C-S25",
   "ledger/ROUND_ANALYSIS.round9.md (added @e8d13d58ed) answers this compile",
   "Z-W26-S1 carries its own row (REMEDIATION_v3)"
  ],
  "remedy": "Round 9's compile was answered; its open item carries its own row.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S27",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Round 10 L8: Z-S33, Z-W29-S1 and Z-W30-S1 are GRADUATED.",
  "evidence": [
   "adjudications/ADJUDICATION_v18.md#AMGT_HARVST-Z-C-S27",
   "ledger/ROUND_ANALYSIS.round10.md (added @6710fe6501) answers this compile",
   "Z-S33, Z-W29-S1 and Z-W30-S1 carry their own rows (REMEDIATION_v4)"
  ],
  "remedy": "Round 10's compile was answered; its items carry their own rows.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W31-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The two timeline routes are now handled by scoped_amgt.handler but are NOT mounted at the gateway: infra/aws/terraform/harvest/scoped-amgt-api.tf has 0 occurrences of `timeline`, so a browser call still 404s at API Gateway until a terraform cell adds them.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W31-S1",
   "drain @180989c8a8 (a-1): both timeline routes declared on the gateway, route table 16 -> 18",
   "served: /security/BA_US_Equity/timeline/day/2026-09-08 answers 200 with 6 rows (ADJUDICATION_v49 section 3, 2026-10-02 ~18:2xZ)"
  ],
  "remedy": "Both timeline routes are mounted at the gateway and answer.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-29T00:06Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W31-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The day route takes ~15.8s per call from this box because the headline join scans EVERY source's whole silver `article` table (publication_gold._iter_latest_articles) and the range route ~5.4s;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W31-S2",
   "served 2026-10-02 ~18:2xZ: BA day route 200 x3, cold 18.0 s then 10.5 s and 0.5 s, inside the 29 s gateway (DSGN REMEDIATION_v1 Z-C-S29 @ae0d4e7082)"
  ],
  "remedy": "The day route answers inside the gateway, cold included (memory, deadline and warm-up).",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO~Z",
   "at": "2026-10-02T18:44Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S34",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM RECORD for AMGT_HARVST-Z-W31-S1 and AMGT_HARVST-Z-W31-S2 (both ARMED on this seat by HVST-z-0): neither hazard is reachable today because the gateway mounts no timeline route, so no browser and no ruling-3 pre-push measurement can observe the handler;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S34",
   "disarm record @4dfed2cdc2; both rows it names (Z-W31-S1, Z-W31-S2) are remedied in this file"
  ],
  "remedy": "A disarm record whose rows are remedied.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S35",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The round-11 analysis's cell 1 (mount both timeline routes + ledgered deploy) cannot by itself make either route answer: the deployed opal-amgt-scoped-api package carries NO pyarrow and NO lib.opal_naming, and its only layer (opal-amgt-print-deps:1) carries numpy 2.2.6 but NO pyarrow -- so after a m",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S35",
   "build @36d4ae1ede: the scoped-API build packages what the timeline loaders import",
   "the timeline serves on the deployed API since round 12 (Z-C-S30; ROUND_ANALYSIS.round12 @094cc1f110) and today (BA day 200)"
  ],
  "remedy": "The package carries the loaders' imports; the routes serve.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-29T01:41Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W35-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Mounting the two timeline routes (16->18) turns two tests OUTSIDE HVST-a-1's <paths> red: test_slash_safe_security_route.py::test_route_table_still_has_sixteen_entries and test_generation_and_pool_routes.py::test_19_the_route_set_did_not_move_and_the_retired_table_is_not_named both pin len(scoped_am",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W35-S1",
   "AMENDMENT 1 @15caf6ed3b admits the two RESAPP tests (16 -> 18); complete @e79d28ed1b (256 passed of 256)"
  ],
  "remedy": "The two pinned route-table tests move 16 -> 18 under the amendment.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-28T23:48Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S36",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "HVST-a-2's preflight premise is false on BOTH planes: opal-amgt-scoped-api-role reads NO amgt/harvest/gold/ prefix, live or in Terraform at HEAD, so the timeline loaders (chatter_daily / chatter_event / article_security_mention) would be refused S3 reads after the mount + package deploy -- the 404 b",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S36",
   "AMENDMENT 1 @a60bd1bae5: one read-only gold grant added to the deploy's scope",
   "the timeline loaders serve gold today (BA day 200, 6 rows)"
  ],
  "remedy": "The scoped-API role reads harvest gold.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-28T23:30Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S37",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "safe-merge.sh's --continue foreign-path guard whitelists whatever the INDEX holds when the merge conflicts, not what the MERGE staged: a peer that stages between the pre-merge clean-index check (:208) and the state snapshot (:248) has its files committed under the draining seat's name.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S37",
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S43 (DISARM, resolving commit ccf2a27c6b by 0.0.0_AB_MSTR~Z)",
   "ran live on the j-2 drain with 0 foreign paths (ADJUDICATION_v28 @c3021c76a5)"
  ],
  "remedy": "safe-merge's conflict state records only the paths the merge staged.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-29T22:24Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W37-S3",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "STOP RULE HIT DURING RUNNER DEVELOPMENT, NOT DURING A CAPTURE: a test of a re-authentication guard called the real SessionManager.refresh('sa'), the guard was not loaded, and the producer's credentialed login ran -- headed Chrome, the stored seeking-alpha credential submitted, two press-and-hold att",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W37-S3",
   "AMENDMENT 1 @50a0fd6793: w-2 resumes behind three guards (AC5-AC7)",
   "TO-HVST-w-2 last <status>complete</status>"
  ],
  "remedy": "The capture resumed only behind the three guards; the order is complete.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S38",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "HVST-a-2 cannot build as its halves are written: bound (D) admits no wheel that is not sha256-pinned AND named on the halves, and neither half names a pyarrow version or sha256 -- and at the measured 131.2 MiB headroom the version DECIDES stop limb 2, because the numpy-2 requirement and the 250 MiB ",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S38",
   "@dfc0d15e96: the lib commit routed to and landed by the CTO",
   "the timeline serves (round 12, Z-C-S30; today BA day 200)"
  ],
  "remedy": "The build carries a pinned pyarrow; the routes serve.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO~Z",
   "at": "2026-09-28T10:26Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S39",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The ONE IAM grant a-2's halves name (s3:GetObject on amgt/harvest/gold/*) cannot satisfy a-2.AC1: both timeline loaders reach S3 through paginated list_objects_v2, and the role's only ListBucket statement is conditioned on a prefix set that contains neither the gold prefix nor the silver article pre",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S39",
   "build @36d4ae1ede (a-2 act 1 + row Z-S39)",
   "both loaders list and read gold on the deployed API (round 12 onward; BA day 200 today)"
  ],
  "remedy": "The role's list and read grants cover the loaders' prefixes.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-29T01:41Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W37-S4",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The resumed w-2 capture reached seekingalpha.com ONCE and got HTTP 402 (351 B) on the account check /api/v3/account/1btfwdu/info, where the last sa run (09-26 09:44Z, CALL 1 of ledger ~22) got HTTP 200 (5,149 B).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W37-S4",
   "ac-2 close @097858b1c2: account 200 authorized",
   "round-30 analysis @6adebef352: sa account active; r37 packet section 5: sa 8,570 stored"
  ],
  "remedy": "The sa account check reads 200 and sa collects.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S30",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8/L9 round 12: the timeline serves on the deployed API for the first time -- 18 AMGT routes live incl.",
  "evidence": [
   "adjudications/ADJUDICATION_v20.md#AMGT_HARVST-Z-C-S30",
   "ledger/ROUND_ANALYSIS.round12.md (added @094cc1f110) answers this compile"
  ],
  "remedy": "Answered by the round-12 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W39-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "lib/research/harvest/timeline_api.py get_timeline_event (route 3) keys an event by first_day and recomputes event_id as publication_gold._event_id(security_key, first_day, last_day);",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W39-S1",
   "j-1 @d92bcc0158 / drain @36e8b79f0e: the event route serves the stored event by its stored id",
   "re-run 8 of 8 (ADJUDICATION_v28 @c3021c76a5)"
  ],
  "remedy": "The event route keys on the stored event id.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-29T22:46Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S40",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "HVST-b-1's merged one-story rule would REGRESS a served lead the round-12 L9 graded right: rebuilt in memory at CLOUD 21cea628b4, BA_US_Equity 2026-09-08 leads with 'Everything to Know About the Boeing Jet That Overshot a Miami Runway' again (served today: 'Boeing Delivers 51 Jets in August...'), be",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S40",
   "b-1 AMENDMENT 1 @bb169815a5: BA 2026-09-08 keeps its graded lead",
   "ADJUDICATION_v21 @6ab411d537: the regression did not ship"
  ],
  "remedy": "The one-story rule no longer pulls a third headline into a tight pair.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-29T05:35Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S31",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8/L9 round 13: b-2 AC4 7 of 7 -- every served event is one story about its own company and its lead names it, read against S3 by this seat;",
  "evidence": [
   "adjudications/ADJUDICATION_v21.md#AMGT_HARVST-Z-C-S31",
   "ledger/ROUND_ANALYSIS.round13.md (added @f1de5ca7ce) answers this compile"
  ],
  "remedy": "Answered by the round-13 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W41-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "HVST-d-1 AC2 (d): with the 'Amazon' alias the AMZN crash coverage forms ONE event of 3 articles on 2026-09-07 only, led by barrons 'Scene of Fatal Amazon Plane Crash', not the 6-article, 09-06..09-10 burst the ruling pictures;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W41-S1",
   "ADJUDICATION_v30 @4b4183acd3 (l-2 AC4 MET 3 of 3 on the served events; AMZN led by the first story)",
   "ledger/ROUND_ANALYSIS.round22.md (added @9d7bd0e4f9) answers this compile"
  ],
  "remedy": "The AMZN crash coverage serves as one event led by its first story.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-30T01:00Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W41-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "HVST-d-1 AC2 (a): the 'Amazon' alias moves EXISTING served rows beyond tier: the matcher sums every alias independently, so mention_count of AMZN rows jumps (crash article 2 -> 10), and AMZN joins the co-mention list of 27 existing pairs across 14 securities (BA, COST, HD, 992_HK, NVDA, ...), includ",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W41-S2",
   "ADJUDICATION_v24 @713537d4d0: the crash report serves 8 spans = 8 in the text (double count gone)",
   "ledger/ROUND_ANALYSIS.round16.md (added @f424435829) answers this compile"
  ],
  "remedy": "Each alias span is counted once.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-29T11:53Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W40-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Planted-fixture mechanism test (HVST-c-1 AC2): a 6-article, 3-day, 4-publisher one-story burst that is a security's ONLY coverage forms 0 events, because the rule's security-name step strips the story's own words (quantum, battery, plant) as the name and the paraphrased headlines then share no term.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W40-S1",
   "f-2 drain @35657cd67c: a security's first burst survives name detection",
   "ledger/ROUND_ANALYSIS.round17.md (added @c296f4ba12) answers this compile"
  ],
  "remedy": "Name stems must also be stems of an alias, so a first burst forms its event.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-29T12:39Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S34",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L9 round 16: the double count is gone -- the AMZN crash report serves 8 and its text holds exactly 8 'Amazon' occurrences, and each of the 8 C->D rows counts its one span once (Z-W41-S2 graduates).",
  "evidence": [
   "adjudications/ADJUDICATION_v24.md#AMGT_HARVST-Z-C-S34",
   "ledger/ROUND_ANALYSIS.round16.md (added @f424435829) answers this compile"
  ],
  "remedy": "Answered by the round-16 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S35",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L9 round 17: of 531 sampled hits, tickers are the company 172/240 and short names 61/291.",
  "evidence": [
   "adjudications/ADJUDICATION_v25.md#AMGT_HARVST-Z-C-S35",
   "ledger/ROUND_ANALYSIS.round17.md (added @c296f4ba12) answers this compile"
  ],
  "remedy": "Answered by the round-17 analysis (the alias rule ruled).",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W45-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "HVST-g-1: limb (a) over the pool's 250 names refuses the ruling's own whole-brand entry UBS, because a keyless coverage row named 'UBS' is another of the 250 names.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W45-S1",
   "g-1 complete @ba78c6e75a; TO-HVST-g-2 last <status>complete</status> (the limb (a) population decided at g-2)"
  ],
  "remedy": "Decided by the issuer before g-2; both orders complete.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W45-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "HVST-g-1: the whole-brand alias ASML also enters the listing_hit query identifiers, so 148 chatter_daily cells (74 each for ASML_NA and ASML_US) move data_status/publishers_covered, a movement no mention row explains.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W45-S2",
   "ledger/NEVER_WIDEN_ROUND18_G2_CTO_HALF.md names the 148 cells (2 occurrences of '148')",
   "TO-HVST-g-2 last <status>complete</status>"
  ],
  "remedy": "The g-2 pair names the 148 daily cells that move for a non-mention reason.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S37",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 19: deployed uv0oTSMa... and chatter_daily part 4743eb60 re-read (PARTIAL 148 ['sa'] + 1 ['wsj'], DENIED 51,803);",
  "evidence": [
   "adjudications/ADJUDICATION_v27.md#AMGT_HARVST-Z-C-S37",
   "ledger/ROUND_ANALYSIS.round19.md (added @a251f02116) answers this compile"
  ],
  "remedy": "Answered by the round-19 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S43",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM of AMGT_HARVST-Z-S37 (ARMED, disarm_owner 2.0.0_SA_COO~H): the resolving commit is ccf2a27c6b by 0.0.0_AB_MSTR~Z -- safe-merge.sh's conflict state now records only the paths the MERGE could stage (HEAD..MERGE_HEAD plus unmerged paths);",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S43",
   "disarm record of Z-S37 (ccf2a27c6b); Z-S37 is remedied in this file"
  ],
  "remedy": "A disarm record whose row is remedied.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S38",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 20: j-1's id-keyed route re-run 8 of 8 (Z-W39-S1 graduates);",
  "evidence": [
   "adjudications/ADJUDICATION_v28.md#AMGT_HARVST-Z-C-S38",
   "ledger/ROUND_ANALYSIS.round20.md (added @4b8bd40242) answers this compile"
  ],
  "remedy": "Answered by the round-20 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S39",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 21: k-1 AC2 re-run PASS at the ruled threshold 4 (KEPT 5, CHANGED 3, GONE 0;",
  "evidence": [
   "adjudications/ADJUDICATION_v29.md#AMGT_HARVST-Z-C-S39",
   "ledger/ROUND_ANALYSIS.round21.md (added @63c272600a) answers this compile"
  ],
  "remedy": "Answered by the round-21 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W49-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "BLOCKING: HVST-k-1 AC2 (b) cannot hold as written -- NVDA_US_Equity's served 2026-06-01 event has ONLY guarded members (wsj co_mention_count 3, two sa is_roundup True), so the ruled guard (a guarded member never leads, the span is set by the non-roundup members) leaves it no span and no lead: it is ",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W49-S1",
   "AMENDMENT 1 landed @85fe787f17 (guard threshold 4, ruled msg 26783); k-1 complete @2aee2704b9"
  ],
  "remedy": "The ruled threshold makes AC2 (b) hold; the order is complete.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W49-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "BLOCKING: HVST-k-1 AC2 (c) cannot hold for AMZN_US_Equity -- j-2's candidate (span 2026-09-06..09-08, lead bbg 'Amazon Cargo Plane Overshoots Runway') had no guard, but bbg 09-06 has co_mention_count 3 and barrons 09-08 is is_roundup True, so under the ruled guard neither extends the span and the le",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W49-S2",
   "AMENDMENT 1 landed @85fe787f17 (threshold 4); k-1 complete @2aee2704b9"
  ],
  "remedy": "The ruled threshold makes AC2 (c) hold; the order is complete.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W49-S5",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "OBSERVATION: AMENDMENT 1 (guard threshold 4, RULED by 1.0.0_SA_CTO~Z msg 26783, ROUND_ANALYSIS.round20.md s.2a @168acda05e;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W49-S5",
   "record @7bd5ee8a9d of AMENDMENT 1's landing and the AC2 re-run PASS"
  ],
  "remedy": "A record of the landed amendment.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S40",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L9 round 22: l-2 AC4 MET 3 of 3 -- the served 992_HK, AMZN and HD events (part f57dca9b, 8 rows, read by this seat;",
  "evidence": [
   "adjudications/ADJUDICATION_v30.md#AMGT_HARVST-Z-C-S40",
   "ledger/ROUND_ANALYSIS.round22.md (added @9d7bd0e4f9) answers this compile"
  ],
  "remedy": "Answered by the round-22 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W65-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The signed command runs ONE job per invocation (config.json jobs_per_run=1, no --max-jobs), so 'run 1' touched barrons only;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W65-S1",
   "AMENDMENT 1 @a0134b0467: re-cut with --max-jobs after attempt 1",
   "TO-HVST-o-5 last <status>complete</status>"
  ],
  "remedy": "The signed command was re-cut to cover the four publishers; the order is complete.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-30T04:31Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W65-S3",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The collector's grammar run (bbg, ft, wsj, --max-jobs 3, twice) wrote ZERO S3 objects: it stores fetched articles and listings in the local progress.sqlite3 outbox (status pending) and the S3 put is upload-harvest, the writer the pair marked 'not run';",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W65-S3",
   "AMENDMENT 2 @5facb19f57: the S3 writer is upload-harvest",
   "TO-HVST-o-5 last <status>complete</status>; ADJUDICATION_v34 @190101cb31: 57 objects put"
  ],
  "remedy": "The upload step is named as the S3 writer; the order is complete.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S44",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 25: the served plane reconciles on S3 -- o-5 put 57 objects (27 bronze + 30 silver) under bloomberg/ and wsj/ only, o-4 exactly 3 sa silver parts, nothing under ft/ or barrons/;",
  "evidence": [
   "adjudications/ADJUDICATION_v34.md#AMGT_HARVST-Z-C-S44",
   "ledger/ROUND_ANALYSIS.round25.md (added @300ea99316) answers this compile"
  ],
  "remedy": "Answered by the round-25 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W69-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Barrons' contracted challenge repair cannot run in a job that had to re-authenticate first: the reauth spends the loop's attempt 0 and the repair branch refuses when attempt is truthy, so every logged-out barrons start ends request_rejected (2 of 2 on the ledger).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W69-S2",
   "q-6 drain @75db57b063: barrons B2 -- one contracted repair may follow a same-job reauth",
   "r37 packet section 5: barrons 89 of 89 pairs"
  ],
  "remedy": "A logged-out barrons start may reauth and then repair once.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-30T09:07Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S45",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 26: mention gold 358 rows (0 null mention_count) and chatter_daily 52,143 rows (992_HK 273/273 PARTIAL) re-read on S3;",
  "evidence": [
   "adjudications/ADJUDICATION_v35.md#AMGT_HARVST-Z-C-S45",
   "ledger/ROUND_ANALYSIS.round26.md (added @ff4405d3d5) answers this compile"
  ],
  "remedy": "Answered by the round-26 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W71-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "With the parse fixed, the 11 bbg rows get a NEW article_key (bbg:<story id>) because the empty rows were keyed on a bronze-key hash, so the round-28 silver append adds 11 rows and leaves the 11 empty ones served beside them.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W71-S1",
   "aa-3 complete @ad47adde1f: 11 NEW story-id bbg rows served",
   "the 11 empty bronze-hash rows carry 0 blocks, so they form no mention; gold #5 article_security_mention is titled 23,691 of 23,691 (ROUND37_DRAIN_END_PACKET.md @4162e8837b section 3)"
  ],
  "remedy": "The story-id rows serve; the empty rows reach no gold row.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-30T11:52Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W70-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The wsj job ended no_new_articles (a SUCCESSFUL status) with reached_span null, because its listing pages 1-3 were served from today's held listing bronze (dedupe cache), which records no listing capture and so no reach;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W70-S1",
   "fixed by aa-1 @0df90b1535 (Z-C-S49)"
  ],
  "remedy": "The wsj reach is recorded from the held listing.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S46",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 27: q-1 wrote exactly 1 object (run record, of 3,058 scanned) and no served gold moved;",
  "evidence": [
   "adjudications/ADJUDICATION_v36.md#AMGT_HARVST-Z-C-S46",
   "ledger/ROUND_ANALYSIS.round27.md (added @8c0b34526b) answers this compile"
  ],
  "remedy": "Answered by the round-27 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W79-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A run record carries per-job statuses only, so 'refused for the whole universe' is not readable from it as written: the derivation removes bbg on ONE request_rejected job for ONE name (the Z-S45 case, where o-5 completed bbg the same day), so today's DECLARED SET is [barrons, ft, sa, wsj] and ELIGIB",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W79-S1",
   "aa-4 drain @da4fb630b5: the declared set is derived from concluded universe-scope jobs; complete @ea129cc58c"
  ],
  "remedy": "The declared publisher set is derived, not read off one job.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-30T10:48Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W78-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The signed HVST-aa-3 put cannot serialize: store.silver_append raises pyarrow ArrowNotImplementedError (struct 'data' with no child field) building the parquet for the 11 NEW bbg rows, BEFORE any S3 put;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W78-S1",
   "phase A @379a4cab73: bbg rows prune empty dicts so parquet serializes",
   "aa-3 complete @ad47adde1f"
  ],
  "remedy": "Empty structs are pruned before the silver write.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W78-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Phase A code is built and proven but cannot be committed: the lane gate admits only the order <paths> (deliverables + investigations);",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W78-S2",
   "paths fixed @fcd217c797 (Z-C-S49); phase B served"
  ],
  "remedy": "The amendment's lib paths joined <paths>.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S47",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 28: bbg silver part-114206Z re-read (11 story-id rows, 319,528 B, 0 empty bodies;",
  "evidence": [
   "adjudications/ADJUDICATION_v37.md#AMGT_HARVST-Z-C-S47",
   "ledger/ROUND_ANALYSIS.round28.md (added @c907537920) answers this compile"
  ],
  "remedy": "Answered by the round-28 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S46",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A backfill fetches DATED listing hits published before its floor: 9 of the 11 bbg Lenovo story-id articles (o-5, floor 2026-01-01) were published 2015-01-07..2019-05-23, so they spent fetches and yield mention pairs no page day can show.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S46",
   "lib/opal_data_harvest/worker.py carries skipped_pre_floor (6 occurrences; test_ab1_live_reach_and_seed.py 5)",
   "ab-1 complete @da63b88ccd"
  ],
  "remedy": "A backfill hit dated before the floor is recorded skipped_pre_floor, not fetched.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-30T15:35Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W81-S7",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "For sa, ft and bbg the saved-session file is NEWER than the Secrets session, so 'the Secrets session first' starts a job from the OLDER token and is likely to draw the 401 (and a sign-in) this cell exists to avoid.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W81-S7",
   "ruling @7ac7109140 (ab-1 AMENDMENT 3): the newest stored token is used first",
   "lib/opal_data_harvest/credentials.py:115 reads the secret's LastChangedDate; ab-1 complete @da63b88ccd"
  ],
  "remedy": "The newest of the two stored tokens starts the job.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-09-30T15:05Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S48",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 29: mention part-134616Z re-read (379 rows, 21 new bbg pairs on 11 keys);",
  "evidence": [
   "adjudications/ADJUDICATION_v38.md#AMGT_HARVST-Z-C-S48",
   "ledger/ROUND_ANALYSIS.round29.md (added @d0bc0a79f0) answers this compile"
  ],
  "remedy": "Answered by the round-29 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S49",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Channel hygiene: Z-W70-S1 (fixed by aa-1 at 0df90b1535) and Z-W78-S2 (paths fixed at fcd217c797;",
  "evidence": [
   "adjudications/ADJUDICATION_v39.md#AMGT_HARVST-Z-C-S49",
   "hygiene record: Z-W70-S1 fixed by aa-1 @0df90b1535, Z-W78-S2 paths fixed @fcd217c797"
  ],
  "remedy": "A hygiene record: both rows it names are fixed.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W84-S3",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "AMENDMENT 2 change 5 makes test_q6_barrons_guard_ft_body.py::test_logged_out_barrons_start_reauths_repairs_once_and_replays fail (a base-passing test);",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W84-S3",
   "ruling @bf641ae8af (ac-1 AMENDMENT 3) on the q6 barrons test",
   "TO-HVST-ac-1 last <status>complete</status>"
  ],
  "remedy": "Ruled by the issuer; the order is complete.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W85-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "sa_rest_fetch.check() requests /api/v3/account/1btfwdu/info with the user id hard-coded, not the {user_id} that contracts.json auth_check names from the session.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W85-S2",
   "ad-1 A0 @9e68057327: the sa check reads {user_id} from the session; ad-1 complete @29984dd835"
  ],
  "remedy": "The sa account check reads the session's own user id.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W87-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The stored ft bundle is a flat cookie name->value map with no expiry field, so neither per-cookie expiry nor the earliest login-cookie expiry can be read from it.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W87-S1",
   "ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait)"
  ],
  "remedy": "OPEN: the ft limb is a QUALIFIED WAIT (ROUND_ANALYSIS.round37 @29fbb123e0 ruling 2; addendum @aeb3041e9c: STOP_FT stays); re-check HVST-RECHECK-OCILAR-1 on 2026-11-01. Proof: a working unattended ft sign-in that holds a session.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-C-S50",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 30: chatter_daily part-181745Z re-read (52,143 rows;",
  "evidence": [
   "adjudications/ADJUDICATION_v40.md#AMGT_HARVST-Z-C-S50",
   "ledger/ROUND_ANALYSIS.round30.md (added @6adebef352) answers this compile"
  ],
  "remedy": "Answered by the round-30 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S50",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "test_o1_run_record_reach.py::test_the_persisted_record_is_never_overwritten hardcodes started_at 2026-09-30, so it passes only when run on UTC date 2026-09-30;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S50",
   "ADJUDICATION_v41 @49513b34dc: the repaired test passes on 2026-10-01"
  ],
  "remedy": "The test no longer pins a calendar date.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S51",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 31: the wsj/barrons session secrets exist;",
  "evidence": [
   "adjudications/ADJUDICATION_v41.md#AMGT_HARVST-Z-C-S51",
   "ledger/ROUND_ANALYSIS.round31.md (added @309b2da963) answers this compile"
  ],
  "remedy": "Answered by the round-31 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W90-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Four base tests assert the replaced sa behaviour (an article GET stored as the bronze capture;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S2",
   "AMENDMENT 1 @cec6fb0ba6 and worker @03457e5899; disposition record Z-S52 @eae320125c"
  ],
  "remedy": "The four base tests follow the ruled sa behaviour.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-01T05:52Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W92-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Every sa silver append fails: all 229 rebuilt article rows carry themes={} (an empty struct) and pyarrow refuses to write it to parquet, so upload-harvest returns rc=2 and the 229 raw outbox rows stay pending.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W92-S1",
   "fix @254ea37cf6: sa silver rows prune empty structs"
  ],
  "remedy": "Empty-struct themes no longer block the sa silver append.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-01T07:39Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W92-S4",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Both real sa jobs so far (ASML then ADBE) end status=error from an exception at the end of the job after every article was stored (ASML: Timeout;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W92-S4",
   "fix @3669bd0f0a: a request that got no response is retried at most twice"
  ],
  "remedy": "One dropped connection no longer ends an sa job.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-01T08:44Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W91-S4",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "verification.py's press-and-hold locator fallback (verification_locator.locate) reads secret astn/kimi/api-key and POSTs a page screenshot to api.moonshot.ai;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W91-S4",
   "disarm @220a74350a: no verification path posts a screenshot to an external API; @80f80df619 verification_locator.py out of the release"
  ],
  "remedy": "The vendor-calling locator is gone from the code and the release.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-01T11:06Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W91-S5",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TabSession.seed() can never seed: __init__ already did page.goto(origin), which sets the publisher's own cookies, so seed()'s 'profile holds no cookie for the origin domain' test is always false.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W91-S5",
   "fixes @791616d9b6 and @3cdb41b7e2: TabSession.seed keys on the bundle's own cookie names and adds the ones the profile lacks (Z-S52 evidence)"
  ],
  "remedy": "seed() adds the bundle cookies the profile lacks.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-01T10:54Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W91-S10",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "barrons search returned HTTP 200 with 0 parseable hits once (10:34Z, three browsers running), then 16 hits on every other call;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W91-S10",
   "graduated by Z-C-S63 (ADJUDICATION_v49 @76f4381bce); not cut in round 38 (ROUND_ANALYSIS.round37 @29fbb123e0 section 3)"
  ],
  "remedy": "OPEN: a barrons zero-hit HTTP 200 still reads as 'no articles'. Proof: such a response recorded as a failed retrieval.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO~Z",
   "at": "2026-10-03T01:10Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S52",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Round-32 disposition record (rows are append-only): every round-32 row the file still reads ARMED is disarmed by a landed commit or ruled here -- W90-S2, W92-S1, W92-S4, W91-S4, W91-S5 disarmed;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S52",
   "disposition record @eae320125c; every row it disarms is remedied in this file"
  ],
  "remedy": "A disposition record whose rows are remedied.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S52",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 32: quarantine object holds 33 keys / 35 silver parts;",
  "evidence": [
   "adjudications/ADJUDICATION_v42.md#AMGT_HARVST-Z-C-S52",
   "ledger/ROUND_ANALYSIS.round32.md (added @749ec2c72e) answers this compile"
  ],
  "remedy": "Answered by the round-32 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W90-S4",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "HVST-af-3 AC2 FAILS honestly: 68 of 89 universe rows map to a gold security_key;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S4",
   "AMENDMENT 1 @e11bfe731a: gold universe 212 (rebuilt @e0d3a13ef1); drain @8e5a41ed67"
  ],
  "remedy": "Gold carries the 21 collector-universe names it lacked.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-01T12:37Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W91-S11",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "HVST-af-2 AC2 not met: no challenge was met AND passed under the input-source monitor inside the 10-request-per-publisher cap (bbg met a PerimeterX press-and-hold 403 once, unhandled by the run-1 driver, then none in 4 more attempts;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W91-S11",
   "InputSourceMonitor built @2245350246",
   "bbg limb 2a MET on 13 monitored runs under ruling 8 (ADJUDICATION_v49 @76f4381bce; round 37 closed @29fbb123e0)"
  ],
  "remedy": "A challenge met and passed under the monitor exists (13 runs).",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO~Z",
   "at": "2026-10-02T19:24Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W91-S12",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "verification.solve() against a live bbg page raised 'Locator.count: Frame was detached' once (run 3, 11:58:38Z-11:59:02Z): the control lookup in _press_and_hold_box / _control_visible iterates page.frames and calls count() with no guard against a frame that detaches mid-iteration.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W91-S12",
   "fix @640483677d: solve() re-locates once on 'Frame was detached'"
  ],
  "remedy": "A detached frame no longer aborts the solve.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-01T12:38Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W92-S9",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "af-4: a sitemap listing's reached_span reads stop_bound at the fetch date (2026-10-01..2026-10-01), not the dates the walk reached.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W92-S9",
   "fix @ce17235845: a sitemap-XML listing folds the dates the walk reached into the run record"
  ],
  "remedy": "reached_span reads the walked dates.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-01T12:47Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S53",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Round-33 disposition record (rows are append-only): the four round-33 rows the file still reads ARMED are disarmed by landed commits -- W90-S4, W91-S11, W91-S12, W92-S9.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S53",
   "disposition record @f09e619e57; every row it disarms is remedied in this file"
  ],
  "remedy": "A disposition record whose rows are remedied.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S53",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 33: verification_locator.py is out of the tree and build_release.py (v42's egress disarm now structural);",
  "evidence": [
   "adjudications/ADJUDICATION_v43.md#AMGT_HARVST-Z-C-S53",
   "ledger/ROUND_ANALYSIS.round33.md (added @b25abce8d4) answers this compile"
  ],
  "remedy": "Answered by the round-33 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W90-S6",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "ag-2: neither ft's Security Verification nor sa's PerimeterX press-and-hold was MET in six fresh anonymous profiles, so AC2 (a challenged pass) cannot be earned and no ft solver was built.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S6",
   "ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait)",
   "ROUND_ANALYSIS.round37 ruling 4: (2b) is graded only when a challenge appears"
  ],
  "remedy": "OPEN: the ft limb is a QUALIFIED WAIT (ROUND_ANALYSIS.round37 @29fbb123e0 ruling 2; addendum @aeb3041e9c: STOP_FT stays); re-check HVST-RECHECK-OCILAR-1 on 2026-11-01. Proof: a working unattended ft sign-in that holds a session.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-W90-S7",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "bot_check.signature_of reads a normal sa page as 'perimeterx': the page carries a hidden px-captcha mount, so a page-text signature check on sa is a false positive.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S7",
   "fix @42ea2c30c1: the perimeterx signature needs the challenge (row Z-W90-S8)"
  ],
  "remedy": "sa's hidden px-captcha mount no longer reads as a challenge.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W90-S8",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Z-W90-S7 resolved: bot_check perimeterx signature now needs the challenge;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S8",
   "record @e4939d2e63 of fix @42ea2c30c1"
  ],
  "remedy": "A record of the landed fix.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S54",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 34: window-1 monitor record = packet (hardware 12,795 / injected 204;",
  "evidence": [
   "adjudications/ADJUDICATION_v44.md#AMGT_HARVST-Z-C-S54",
   "ledger/ROUND_ANALYSIS.round34.md (added @6cbef26707) answers this compile"
  ],
  "remedy": "Answered by the round-34 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S55",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Round-35 disposition record (rows are append-only): W92-S11 and W92-S12 (ARMED: a restarted ft driver stalls on a dead session / the ft session dies ~20-30 min after each renewal) are disarmed by state -- the ft backfill driver stays OFF -- and carried to the round-36 proposal.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S55",
   "disposition record @5a6bdc1c07; its two rows were dismissed with ft OFF by Z-C-S65 (ADJUDICATION_v49)"
  ],
  "remedy": "A disposition record; its rows are dispositioned.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S55",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 35: ah-1's planted bbg fixture is a real 16:24Z capture operated ~12 s by the real solve() (proves operation, not server acceptance);",
  "evidence": [
   "adjudications/ADJUDICATION_v45.md#AMGT_HARVST-Z-C-S55",
   "ledger/ROUND_ANALYSIS.round35.md (added @89539ccbc2) answers this compile"
  ],
  "remedy": "Answered by the round-35 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W90-S10",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "ai-1 AC2 cannot grade live data from a worktree: .runtime is untracked, so the grader's runtimes.json is absent there and the grader raises FileNotFoundError.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S10",
   "the grader runs from the main tree's .runtime: close run 18:38Z rc 0 (ROUND37_DRAIN_END_PACKET.md @4162e8837b section 2)"
  ],
  "remedy": "No act owed: the grader is run from the main runtime.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W91-S18",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "HVST-ai-3: ft/sa/barrons captures land under the code's DEFAULT runtime root, not under the per-publisher runtimes.json dir;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W91-S18",
   "the row's own notes: no hazard; recorded for limb-2b readers"
  ],
  "remedy": "No act owed: a location fact recorded for readers.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S56",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "HVST-ai-2 left OPEN: the ft session-death cause is found (no page load in the tab for ~10-40 min) but both keep-alive attempts died and 4 renewals then failed;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S56",
   "ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait)"
  ],
  "remedy": "OPEN: the ft limb is a QUALIFIED WAIT (ROUND_ANALYSIS.round37 @29fbb123e0 ruling 2; addendum @aeb3041e9c: STOP_FT stays); re-check HVST-RECHECK-OCILAR-1 on 2026-11-01. Proof: a working unattended ft sign-in that holds a session.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-W92-S15",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "ai-2: a job run from a worktree used the worktree's own ft profile, not the main runtime's (profile root follows the checkout, not --runtime-root).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W92-S15",
   "lib/opal_data_harvest/tab_transport.py:27 PROFILE_ROOT_ENV = 'OPAL_HARVEST_PROFILE_ROOT' names the profile root explicitly"
  ],
  "remedy": "The profile root can be named, not inferred from the checkout.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W92-S16",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "ai-2 attempt 3: the freshly signed-in ft bundle held a __Host-GAPS cookie that Chrome refuses with a domain;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W92-S16",
   "lib/opal_data_harvest/tab_transport.py:163 falls back when a __Host- cookie is refused; test_ai2_ft_session.py:183 plants it"
  ],
  "remedy": "A refused __Host- cookie no longer fails the whole seed batch.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W92-S17",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "ai-2 attempt 3: the headed ft sign-in met an hCaptcha;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W92-S17",
   "ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait)"
  ],
  "remedy": "OPEN: the ft limb is a QUALIFIED WAIT (ROUND_ANALYSIS.round37 @29fbb123e0 ruling 2; addendum @aeb3041e9c: STOP_FT stays); re-check HVST-RECHECK-OCILAR-1 on 2026-11-01. Proof: a working unattended ft sign-in that holds a session.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-C-S56",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L8 round 36 mid-round compile: 9 rows past the v45 watermark at CLOUD @7463a1fcd4;",
  "evidence": [
   "adjudications/ADJUDICATION_v46.md#AMGT_HARVST-Z-C-S56",
   "ledger/ROUND_ANALYSIS.round36.md (added @e38e50aa55) answers this compile"
  ],
  "remedy": "Answered by the round-36 analysis.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S57",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "ai-5's per-row fallback re-opens Z-S58: any batched bbg pass that contains bbg:TD7VMGKGCTIZ00 (pending SilverRowError, due hourly, next 06:36:56Z) raises SilverRowError and falls back to one silver_append, so one full silver prefix read, per row for all ~266 rows, the same O(n^2) drain;",
  "evidence": [
   "adjudications/ADJUDICATION_v46.md#AMGT_HARVST-Z-C-S57",
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S62 (DISARMED by its owner)",
   "fix @7336e91260 (ai-5: bad rows isolated before the one batched append); close @61ef1fa264 (829 of 830 uploaded in one batched pass)"
  ],
  "remedy": "Bad silver rows are isolated locally before the one batched append; the per-row fallback is refused.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-02T05:50Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W90-S11",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "HVST-ai-5: the sparse cone named for this worktree cannot run the collector suite;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S11",
   "the row's own notes: a later worker cut on this face needs the six paths in its cone"
  ],
  "remedy": "No act owed: a cone-sizing fact for future cuts.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S59",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L9 limb 2a on ruling 28245: bbg MET (9 non-void of 25, 9 passed) only after this seat re-derived presentation times from the 403s, because bbg emits no challenge_presented and the grader anchors the band on the pass;",
  "evidence": [
   "adjudications/ADJUDICATION_v47.md#AMGT_HARVST-Z-C-S59",
   "superseded by Z-C-S64 (ADJUDICATION_v49 @76f4381bce): limb 2a graded per run under ruling 8; round 37 CLOSED on it (ROUND_ANALYSIS.round37 @29fbb123e0)"
  ],
  "remedy": "Superseded by the per-run grade (ruling 8).",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S60",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Limb 2a re-graded over all three windows (ruling 28245): bbg NOT-MET -- a clean, unassisted press-and-hold FAILED at 06:59:52Z in window 3 (run 20261002T065754Z-bbg-4f3bfa12bd, 0 hardware events in the band), 9 of 10 non-void passed;",
  "evidence": [
   "adjudications/ADJUDICATION_v48.md#AMGT_HARVST-Z-C-S60",
   "superseded by Z-C-S64 (ADJUDICATION_v49 @76f4381bce): bbg 2a MET on 13 runs per ruling 8; round 37 CLOSED on it (@29fbb123e0)"
  ],
  "remedy": "Superseded by the per-run grade (ruling 8).",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W90-S14",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "HVST-aj-5: request_kind labels a bbg ARTICLE fetch 'listing' because transport.request_kind matches the substring '/news' and every bbg article path is /news/articles/...",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S14",
   "graduated by Z-C-S63 (ADJUDICATION_v49 @76f4381bce); not cut in round 38 (ROUND_ANALYSIS.round37 @29fbb123e0 section 3)"
  ],
  "remedy": "OPEN: transport.request_kind still labels a bbg article fetch 'listing'. Proof: an article GET recorded as 'article'.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-W92-S18",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "aj-4 step 2: the NopeCHA Token API the ft sign-in uses is DISCONTINUED (error 19);",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W92-S18",
   "ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait)"
  ],
  "remedy": "OPEN: the ft limb is a QUALIFIED WAIT (ROUND_ANALYSIS.round37 @29fbb123e0 ruling 2; addendum @aeb3041e9c: STOP_FT stays); re-check HVST-RECHECK-OCILAR-1 on 2026-11-01. Proof: a working unattended ft sign-in that holds a session.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-W92-S19",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "aj-6: the Ocilar API answered HTTP 503 \"Service 'hcaptcha' is not available yet\" to the one sign-in solve call;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W92-S19",
   "ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait)"
  ],
  "remedy": "OPEN: the ft limb is a QUALIFIED WAIT (ROUND_ANALYSIS.round37 @29fbb123e0 ruling 2; addendum @aeb3041e9c: STOP_FT stays); re-check HVST-RECHECK-OCILAR-1 on 2026-11-01. Proof: a working unattended ft sign-in that holds a session.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-S66",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "NopeCHA no longer offers hCaptcha solving in any measured form, so the approved option A (NopeCHA browser extension for the unattended ft sign-in) is very unlikely to work.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S66",
   "ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait)"
  ],
  "remedy": "OPEN: the ft limb is a QUALIFIED WAIT (ROUND_ANALYSIS.round37 @29fbb123e0 ruling 2; addendum @aeb3041e9c: STOP_FT stays); re-check HVST-RECHECK-OCILAR-1 on 2026-11-01. Proof: a working unattended ft sign-in that holds a session.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-W92-S20",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "aj-4: with the keep-alive firing every ~3.3 min (6 keepalive_page_load events, all logged_in, 200), the hand-solved ft session still died 24 min after sign-in (job ends 401 sign_in_refused), against the 120 min the order needs.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W92-S20",
   "ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait)"
  ],
  "remedy": "OPEN: the ft limb is a QUALIFIED WAIT (ROUND_ANALYSIS.round37 @29fbb123e0 ruling 2; addendum @aeb3041e9c: STOP_FT stays); re-check HVST-RECHECK-OCILAR-1 on 2026-11-01. Proof: a working unattended ft sign-in that holds a session.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-W90-S21",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "aj-6 stage 2: the NopeCHA extension (0.6.1, loaded and running) did NOT clear the ft hCaptcha in 150 s;",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S21",
   "ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait)"
  ],
  "remedy": "OPEN: the ft limb is a QUALIFIED WAIT (ROUND_ANALYSIS.round37 @29fbb123e0 ruling 2; addendum @aeb3041e9c: STOP_FT stays); re-check HVST-RECHECK-OCILAR-1 on 2026-11-01. Proof: a working unattended ft sign-in that holds a session.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-C-S62",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "FWD-11 limb (1) for ft has no working route: NopeCHA Token API discontinued, NopeCHA hCaptcha recognition not offered, the NopeCHA extension did not clear in 150 s, Ocilar answers 503, and hand sessions die at 24-75 min under keep-alive;",
  "evidence": [
   "adjudications/ADJUDICATION_v49.md#AMGT_HARVST-Z-C-S62",
   "ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait)",
   "ROUND_ANALYSIS.round37 addendum @aeb3041e9c: no hCaptcha solver candidate; STOP_FT stays"
  ],
  "remedy": "OPEN: the ft limb is a QUALIFIED WAIT (ROUND_ANALYSIS.round37 @29fbb123e0 ruling 2; addendum @aeb3041e9c: STOP_FT stays); re-check HVST-RECHECK-OCILAR-1 on 2026-11-01. Proof: a working unattended ft sign-in that holds a session.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-C-S63",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two enrichment items graduate to the round-37 analysis: transport.request_kind labels every bbg article fetch 'listing' (substring '/news'), and barrons' search can answer HTTP 200 with 0 parseable hits, which the collector reads as 'no articles' rather than a failure.",
  "evidence": [
   "adjudications/ADJUDICATION_v49.md#AMGT_HARVST-Z-C-S63",
   "ROUND_ANALYSIS.round37 @29fbb123e0 section 3: the round-38 enrichment list (FWD-16, FWD-17, FWD-6 density, ft) does not cut either item"
  ],
  "remedy": "OPEN: not cut for round 38. Proof: a request_kind that labels a bbg article 'article', and a barrons zero-hit 200 recorded as a failed retrieval.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v49",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v49"
  },
  "closed": false
 },
 {
  "id": "AMGT_HARVST-Z-S67",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Silver record_hash hashes run_stamp, so a record_hash-keyed FinBERT store would re-score an unchanged article on every re-silvering.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S67",
   "PRD v0.17 @3da5563fd8 keys FWD-16 to a content hash of the scored text (signed by 3.0.0_SA_CVO~Z @0e85e735c9)",
   "HVST-al-2 @a12f8edbd8 (on HEAD): content_key = sha256 of article_text; AC2 863 rows, 727 keys, 0 mismatches"
  ],
  "remedy": "The scorer keys tone to the scored text's own hash, not record_hash.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v51",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v51"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S68",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "3 tests in test_timeline_day_read_path.py pinned the /timeline/day silver read path that RESAPP am-1 removed by design.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S68",
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S81",
   "repair @949b24cadb (on HEAD); round39/checks/suites_green.py re-run by 3.0.0_SA_CVO~Z 2026-10-03 01:03-01:05Z: 344 + 612 passed, 0 failed"
  ],
  "remedy": "The stale tests were repaired against the gold read path.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v51",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v51"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S67",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Graduation record of Z-S67 and Z-S68 (ADJUDICATION_v50).",
  "evidence": [
   "adjudications/ADJUDICATION_v50.md#AMGT_HARVST-Z-C-S67",
   "both items it graduated carry REMEDIATED rows in this file"
  ],
  "remedy": "A graduation record: both of its items are remedied.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v51",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v51"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W90-S23",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A key-less (ft or no-text) article's null-label marker row in article_sentiment was re-appended on every score run.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W90-S23",
   "HVST-am-1 direct act @d2e915e057 (on HEAD): marker rows keyed to article_key, one per key-less article; round40/am-1.proof.txt plants 3/3, mutant fails 3/3",
   "python -m pytest lib/research/harvest/test_am1_marker_once.py by 3.0.0_SA_CVO~Z 2026-10-03 ~01:3xZ: 3 passed"
  ],
  "remedy": "Each key-less article carries one marker row, written once.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v51",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v51"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S69",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Graduation record of Z-W90-S23's marker re-append residual (ADJUDICATION_v51).",
  "evidence": [
   "adjudications/ADJUDICATION_v51.md#AMGT_HARVST-Z-C-S69",
   "1.0.0_SA_CTO~Z msg 28861 (resolution named: am-1 @d2e915e057)"
  ],
  "remedy": "A graduation record: its item is remedied.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v51",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v51"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S74",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "chatter_window carried rows only for securities present in the mention table, so 6 covered names with 0 mentions had no row and their absence read like a missing build.",
  "evidence": [
   "adjudications/ADJUDICATION_v54.md#AMGT_HARVST-Z-C-S74",
   "HVST-ap-1 @5789ad3487; part-20261004T012303Z: 636 rows on 212 names, 18 explicit zeros, 0 gone, 0 changed (read by 3.0.0_SA_CVO~Z, ADJUDICATION_v55)"
  ],
  "remedy": "Every universe name carries its 30/90/365 rows; a zero-mention name reads 0/0/0/null.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v55",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v55"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-C-S72",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "One company's story is served as an event under each of its listings (78 of 507 events) and composite_figi is null on those rows, so no field groups the listings.",
  "evidence": [
   "adjudications/ADJUDICATION_v53.md#AMGT_HARVST-Z-C-S72"
  ],
  "remedy": "OPEN: a company-level key (populated composite_figi or an issuer id) so cross-security counts collapse listings.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v55",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v55"
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~Z

## Disposition lines (appended, 3.0.0_SA_CVO, dell1, 2026-10-17T12:03:37Z)

From the HVST-cc-6 triage, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json` @341e87e97a, per `ROUND_ANALYSIS.round88.md` section 2 @07264722d8 (a disposition or owner move on an existing row is an appended line on that row's file; no row is edited and none is minted). Each line below supersedes the named row's `owner` and `remediation.owner` from this timestamp. The row's state is unchanged unless the line says DISMISSED.

- `AMGT_HARVST-Z-W87-S1`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the qualified wait and re-checks HVST-RECHECK-OCILAR-1 on 2026-11-01; un-parks on a working unattended ft sign-in that holds a session. Basis: Not met: the stored ft bundle is a flat name-to-value cookie map with no expiry (auth.py:35-36 at fa71ab063e), and the close, a working unattended ft sign-in that holds a session, is not on record; the row is the qualified wait of ROUND_ANALYSIS.round37.
- `AMGT_HARVST-Z-W90-S6`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the qualified wait and re-checks HVST-RECHECK-OCILAR-1 on 2026-11-01; un-parks on a working unattended ft sign-in that holds a session. Basis: Not met: ag-2 found neither ft's Security Verification nor sa's PerimeterX press-and-hold MET in six fresh anonymous profiles, so the challenged-pass clause cannot be earned, and no ft sign-in holding a session is on record.
- `AMGT_HARVST-Z-S56`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the qualified wait and re-checks HVST-RECHECK-OCILAR-1 on 2026-11-01; un-parks on a working unattended ft sign-in that holds a session. Basis: Not met: the ft session-death cause was found in ai-2 (no page load for 10-40 minutes) but both keep-alive attempts died and four renewals failed, and the ft sign-in that holds a session is not on record.
- `AMGT_HARVST-Z-W92-S17`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the qualified wait and re-checks HVST-RECHECK-OCILAR-1 on 2026-11-01; un-parks on a working unattended ft sign-in that holds a session. Basis: Not met: ai-2 attempt 3 met an hCaptcha and the identity cookie appeared 10 s later with no solver call recorded, so whether a person or the widget passed it is unknown and no unattended session that holds is on record.
- `AMGT_HARVST-Z-W90-S14`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 makes request_kind label /news/articles/ paths 'article' under its own pair, with a test that reads one article GET's attempt row; un-parks when that row reads 'article'. Basis: Not met: transport.py:165-175 at HEAD still returns 'listing' for any path containing '/news', and transport.py:503 writes request_kind(url) into the attempt rows, so a Bloomberg article GET is still recorded 'listing'.
- `AMGT_HARVST-Z-W92-S18`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the qualified wait and re-checks HVST-RECHECK-OCILAR-1 on 2026-11-01; un-parks on a working unattended ft sign-in that holds a session. Basis: Not met: the NopeCHA Token API used by the ft sign-in returned error 19 (discontinued) in the aj-4 step-2 read, so the solver path cannot run and no ft sign-in that holds a session is on record.
- `AMGT_HARVST-Z-W92-S19`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the qualified wait and re-checks HVST-RECHECK-OCILAR-1 on 2026-11-01; un-parks on a working unattended ft sign-in that holds a session. Basis: Not met: the Ocilar API answered HTTP 503 'hcaptcha not available yet' to the single aj-6 solve call, so no token was obtained and the ft sign-in did not complete.
- `AMGT_HARVST-Z-S66`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the qualified wait and re-checks HVST-RECHECK-OCILAR-1 on 2026-11-01; un-parks on a working unattended ft sign-in that holds a session. Basis: Not met: the approved option A (NopeCHA extension for the ft hCaptcha) rests on a product that no longer offers hCaptcha solving in any measured form (2026-10-02 reads of the Token API and recognition endpoint), so the close cannot be reached by that route.
- `AMGT_HARVST-Z-W92-S20`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the qualified wait and re-checks HVST-RECHECK-OCILAR-1 on 2026-11-01; un-parks on a working unattended ft sign-in that holds a session. Basis: Not met: the hand-solved ft session with keep-alive every ~3.3 minutes still died 24 minutes after sign-in (job ends 401 sign_in_refused), against the 120 minutes the order needs, so the session-holding clause is not met.
- `AMGT_HARVST-Z-W90-S21`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the qualified wait and re-checks HVST-RECHECK-OCILAR-1 on 2026-11-01; un-parks on a working unattended ft sign-in that holds a session. Basis: Not met: the NopeCHA extension (0.6.1, loaded and running) did not clear the ft hCaptcha in 150 seconds on the aj-6 stage-2 attempt, and no identity cookie was set or saved.
- `AMGT_HARVST-Z-C-S62`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 holds the qualified wait and re-checks HVST-RECHECK-OCILAR-1 on 2026-11-01; un-parks on a working unattended ft sign-in that holds a session. Basis: Not met: ADJUDICATION_v49 graduated the ft limb (FWD-11 limb 1) with no working route at HEAD: NopeCHA discontinued, Ocilar 503, and hand sessions die at 24-75 minutes under keep-alive; the close is a working unattended ft sign-in.
- `AMGT_HARVST-Z-C-S63`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 cuts both halves into the round-N enrichment list (request_kind fix, and barrons zero-hit 200 recorded as a failed retrieval) and reads each at HEAD; un-parks when both tests pass. Basis: Not met: the request_kind half is the same defect as Z-W90-S14 (transport.py:165-175 still labels bbg article paths 'listing'), and the barrons zero-hit-200 half was not read at HEAD by this seat, so the close cannot be shown met.
- `AMGT_HARVST-Z-C-S72`: RE-OWNED to `1.0.0_SA_CTO~DELL1`. Next act: 1.0.0_SA_CTO~DELL1 rules whether a company-level key (populated composite_figi or an issuer id) is built into the served events or the counts; un-parks on the ruling on record. Basis: Not met: ADJUDICATION_v53 measured 78 of 507 events served once per listing with composite_figi null, and no company-level key exists at HEAD; the close is a design decision with no ruling on record, and its owner CTO~Z is not live.

-- 3.0.0_SA_CVO
