# AMGT_HARVST remediation reconciliation -- TRIAGE (draft, 3.0.0_SA_CVO~Z fork)

A = graduated without a row (100); B = existing rows still OPEN or not closed (26).

| A: REMEDIATED 87, OPEN 13 | B: REMEDIATED 14, OPEN 12 | total 126 |
|---|---|---|

| set | id | class | hazard | verdict | evidence |
|---|---|---|---|---|---|
| A | Z-C-S2 | OBSERVATION | INERT | REMEDIATED | graduation record; each item it graduated carries its own row in REMEDIATION_v1 (Z-S1, Z-S2, Z-W9-S1, Z-W10-S3 ...) |
| A | Z-C-S5 | OBSERVATION | INERT | REMEDIATED | graduation record; the items it graduated (Z-W15-S1, Z-S4 ...) are absent from the graduated-without-row census of 2026-10-02 |
| A | Z-C-S7 | OBSERVATION | INERT | REMEDIATED | corrected by Z-C-S8 (ADJUDICATION_v4 @8ed2954c2d): the spec DOES cover C-S400's mechanism by a named deciding input |
| A | Z-C-S12 | OBSERVATION | INERT | REMEDIATED | Z-S1's forward half closed on t-2's 5-of-5 byte-equal exercise; its backward half classified at round 4 (ledger/ROUND_ANALYSIS.round4.md (added @2b196 |
| A | Z-C-S13 | OBSERVATION | INERT | REMEDIATED | graduation record of Z-S10 and Z-S11; Z-S11 carries its own row in REMEDIATION_v1 |
| A | Z-C-S20 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round6.md (added @37217d8053) answers this compile |
| A | Z-C-S23 | OBSERVATION | None | REMEDIATED | ledger/ROUND_ANALYSIS.round8.md (added @42583f6c91) answers this compile |
| A | Z-C-S25 | OBSERVATION | None | REMEDIATED | ledger/ROUND_ANALYSIS.round9.md (added @e8d13d58ed) answers this compile |
| A | Z-C-S27 | OBSERVATION | None | REMEDIATED | ledger/ROUND_ANALYSIS.round10.md (added @6710fe6501) answers this compile |
| A | Z-W31-S1 | OBSERVATION | ARMED | REMEDIATED | drain @180989c8a8 (a-1): both timeline routes declared on the gateway, route table 16 -> 18 |
| A | Z-W31-S2 | OBSERVATION | ARMED | REMEDIATED | served 2026-10-02 ~18:2xZ: BA day route 200 x3, cold 18.0 s then 10.5 s and 0.5 s, inside the 29 s gateway (DSGN REMEDIATION_v1 Z-C-S29 @ae0d4e7082) |
| A | Z-S34 | OBSERVATION | INERT | REMEDIATED | disarm record @4dfed2cdc2; both rows it names (Z-W31-S1, Z-W31-S2) are remedied in this file |
| A | Z-S35 | OBSERVATION | ARMED | REMEDIATED | build @36d4ae1ede: the scoped-API build packages what the timeline loaders import |
| A | Z-W35-S1 | BLOCKING | ARMED | REMEDIATED | AMENDMENT 1 @15caf6ed3b admits the two RESAPP tests (16 -> 18); complete @e79d28ed1b (256 passed of 256) |
| A | Z-S36 | OBSERVATION | ARMED | REMEDIATED | AMENDMENT 1 @a60bd1bae5: one read-only gold grant added to the deploy's scope |
| A | Z-S37 | OBSERVATION | ARMED | REMEDIATED | investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S43 (DISARM, resolving commit ccf2a27c6b by 0.0.0_AB_MSTR~Z) |
| A | Z-W37-S3 | BLOCKING | INERT | REMEDIATED | AMENDMENT 1 @50a0fd6793: w-2 resumes behind three guards (AC5-AC7) |
| A | Z-S38 | BLOCKING | ARMED | REMEDIATED | @dfc0d15e96: the lib commit routed to and landed by the CTO |
| A | Z-S39 | BLOCKING | ARMED | REMEDIATED | build @36d4ae1ede (a-2 act 1 + row Z-S39) |
| A | Z-W37-S4 | OBSERVATION | INERT | REMEDIATED | ac-2 close @097858b1c2: account 200 authorized |
| A | Z-C-S30 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round12.md (added @094cc1f110) answers this compile |
| A | Z-W39-S1 | OBSERVATION | ARMED | REMEDIATED | j-1 @d92bcc0158 / drain @36e8b79f0e: the event route serves the stored event by its stored id |
| A | Z-S40 | BLOCKING | ARMED | REMEDIATED | b-1 AMENDMENT 1 @bb169815a5: BA 2026-09-08 keeps its graded lead |
| A | Z-C-S31 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round13.md (added @f1de5ca7ce) answers this compile |
| A | Z-W41-S1 | OBSERVATION | ARMED | REMEDIATED | ADJUDICATION_v30 @4b4183acd3 (l-2 AC4 MET 3 of 3 on the served events; AMZN led by the first story) |
| A | Z-W41-S2 | OBSERVATION | ARMED | REMEDIATED | ADJUDICATION_v24 @713537d4d0: the crash report serves 8 spans = 8 in the text (double count gone) |
| A | Z-W40-S1 | OBSERVATION | ARMED | REMEDIATED | f-2 drain @35657cd67c: a security's first burst survives name detection |
| A | Z-C-S34 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round16.md (added @f424435829) answers this compile |
| A | Z-C-S35 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round17.md (added @c296f4ba12) answers this compile |
| A | Z-W45-S1 | OBSERVATION | INERT | REMEDIATED | g-1 complete @ba78c6e75a; TO-HVST-g-2 last <status>complete</status> (the limb (a) population decided at g-2) |
| A | Z-W45-S2 | OBSERVATION | INERT | REMEDIATED | ledger/NEVER_WIDEN_ROUND18_G2_CTO_HALF.md names the 148 cells (2 occurrences of '148') |
| A | Z-C-S37 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round19.md (added @a251f02116) answers this compile |
| A | Z-S43 | OBSERVATION | INERT | REMEDIATED | disarm record of Z-S37 (ccf2a27c6b); Z-S37 is remedied in this file |
| A | Z-C-S38 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round20.md (added @4b8bd40242) answers this compile |
| A | Z-C-S39 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round21.md (added @63c272600a) answers this compile |
| A | Z-W49-S1 | BLOCKING | INERT | REMEDIATED | AMENDMENT 1 landed @85fe787f17 (guard threshold 4, ruled msg 26783); k-1 complete @2aee2704b9 |
| A | Z-W49-S2 | BLOCKING | INERT | REMEDIATED | AMENDMENT 1 landed @85fe787f17 (threshold 4); k-1 complete @2aee2704b9 |
| A | Z-W49-S5 | OBSERVATION | INERT | REMEDIATED | record @7bd5ee8a9d of AMENDMENT 1's landing and the AC2 re-run PASS |
| A | Z-C-S40 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round22.md (added @9d7bd0e4f9) answers this compile |
| A | Z-W65-S1 | BLOCKING | ARMED | REMEDIATED | AMENDMENT 1 @a0134b0467: re-cut with --max-jobs after attempt 1 |
| A | Z-W65-S3 | BLOCKING | INERT | REMEDIATED | AMENDMENT 2 @5facb19f57: the S3 writer is upload-harvest |
| A | Z-C-S44 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round25.md (added @300ea99316) answers this compile |
| A | Z-W69-S2 | OBSERVATION | ARMED | REMEDIATED | q-6 drain @75db57b063: barrons B2 -- one contracted repair may follow a same-job reauth |
| A | Z-C-S45 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round26.md (added @ff4405d3d5) answers this compile |
| A | Z-W71-S1 | OBSERVATION | ARMED | REMEDIATED | aa-3 complete @ad47adde1f: 11 NEW story-id bbg rows served |
| A | Z-W70-S1 | BLOCKING | INERT | REMEDIATED | fixed by aa-1 @0df90b1535 (Z-C-S49) |
| A | Z-C-S46 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round27.md (added @8c0b34526b) answers this compile |
| A | Z-W79-S1 | OBSERVATION | ARMED | REMEDIATED | aa-4 drain @da4fb630b5: the declared set is derived from concluded universe-scope jobs; complete @ea129cc58c |
| A | Z-W78-S1 | BLOCKING | INERT | REMEDIATED | phase A @379a4cab73: bbg rows prune empty dicts so parquet serializes |
| A | Z-W78-S2 | BLOCKING | INERT | REMEDIATED | paths fixed @fcd217c797 (Z-C-S49); phase B served |
| A | Z-C-S47 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round28.md (added @c907537920) answers this compile |
| A | Z-S46 | OBSERVATION | ARMED | REMEDIATED | lib/opal_data_harvest/worker.py carries skipped_pre_floor (6 occurrences; test_ab1_live_reach_and_seed.py 5) |
| A | Z-W81-S7 | OBSERVATION | ARMED | REMEDIATED | ruling @7ac7109140 (ab-1 AMENDMENT 3): the newest stored token is used first |
| A | Z-C-S48 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round29.md (added @d0bc0a79f0) answers this compile |
| A | Z-C-S49 | OBSERVATION | INERT | REMEDIATED | hygiene record: Z-W70-S1 fixed by aa-1 @0df90b1535, Z-W78-S2 paths fixed @fcd217c797 |
| A | Z-W84-S3 | BLOCKING | INERT | REMEDIATED | ruling @bf641ae8af (ac-1 AMENDMENT 3) on the q6 barrons test |
| A | Z-W85-S2 | OBSERVATION | INERT | REMEDIATED | ad-1 A0 @9e68057327: the sa check reads {user_id} from the session; ad-1 complete @29984dd835 |
| A | Z-W87-S1 | BLOCKING | INERT | OPEN | ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait) |
| A | Z-C-S50 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round30.md (added @6adebef352) answers this compile |
| A | Z-S50 | OBSERVATION | INERT | REMEDIATED | ADJUDICATION_v41 @49513b34dc: the repaired test passes on 2026-10-01 |
| A | Z-C-S51 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round31.md (added @309b2da963) answers this compile |
| A | Z-W90-S2 | BLOCKING | ARMED | REMEDIATED | AMENDMENT 1 @cec6fb0ba6 and worker @03457e5899; disposition record Z-S52 @eae320125c |
| A | Z-W92-S1 | BLOCKING | ARMED | REMEDIATED | fix @254ea37cf6: sa silver rows prune empty structs |
| A | Z-W92-S4 | BLOCKING | ARMED | REMEDIATED | fix @3669bd0f0a: a request that got no response is retried at most twice |
| A | Z-W91-S4 | OBSERVATION | ARMED | REMEDIATED | disarm @220a74350a: no verification path posts a screenshot to an external API; @80f80df619 verification_locator.py out of the release |
| A | Z-W91-S5 | OBSERVATION | ARMED | REMEDIATED | fixes @791616d9b6 and @3cdb41b7e2: TabSession.seed keys on the bundle's own cookie names and adds the ones the profile lacks (Z-S52 evidence) |
| A | Z-W91-S10 | OBSERVATION | ARMED | OPEN | graduated by Z-C-S63 (ADJUDICATION_v49 @76f4381bce); not cut in round 38 (ROUND_ANALYSIS.round37 @29fbb123e0 section 3) |
| A | Z-S52 | OBSERVATION | INERT | REMEDIATED | disposition record @eae320125c; every row it disarms is remedied in this file |
| A | Z-C-S52 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round32.md (added @749ec2c72e) answers this compile |
| A | Z-W90-S4 | BLOCKING | ARMED | REMEDIATED | AMENDMENT 1 @e11bfe731a: gold universe 212 (rebuilt @e0d3a13ef1); drain @8e5a41ed67 |
| A | Z-W91-S11 | BLOCKING | ARMED | REMEDIATED | InputSourceMonitor built @2245350246 |
| A | Z-W91-S12 | OBSERVATION | ARMED | REMEDIATED | fix @640483677d: solve() re-locates once on 'Frame was detached' |
| A | Z-W92-S9 | OBSERVATION | ARMED | REMEDIATED | fix @ce17235845: a sitemap-XML listing folds the dates the walk reached into the run record |
| A | Z-S53 | OBSERVATION | INERT | REMEDIATED | disposition record @f09e619e57; every row it disarms is remedied in this file |
| A | Z-C-S53 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round33.md (added @b25abce8d4) answers this compile |
| A | Z-W90-S6 | BLOCKING | INERT | OPEN | ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait) |
| A | Z-W90-S7 | OBSERVATION | INERT | REMEDIATED | fix @42ea2c30c1: the perimeterx signature needs the challenge (row Z-W90-S8) |
| A | Z-W90-S8 | OBSERVATION | INERT | REMEDIATED | record @e4939d2e63 of fix @42ea2c30c1 |
| A | Z-C-S54 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round34.md (added @6cbef26707) answers this compile |
| A | Z-S55 | OBSERVATION | INERT | REMEDIATED | disposition record @5a6bdc1c07; its two rows were dismissed with ft OFF by Z-C-S65 (ADJUDICATION_v49) |
| A | Z-C-S55 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round35.md (added @89539ccbc2) answers this compile |
| A | Z-W90-S10 | OBSERVATION | INERT | REMEDIATED | the grader runs from the main tree's .runtime: close run 18:38Z rc 0 (ROUND37_DRAIN_END_PACKET.md @4162e8837b section 2) |
| A | Z-W91-S18 | OBSERVATION | INERT | REMEDIATED | the row's own notes: no hazard; recorded for limb-2b readers |
| A | Z-S56 | OBSERVATION | INERT | OPEN | ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait) |
| A | Z-W92-S15 | OBSERVATION | INERT | REMEDIATED | lib/opal_data_harvest/tab_transport.py:27 PROFILE_ROOT_ENV = 'OPAL_HARVEST_PROFILE_ROOT' names the profile root explicitly |
| A | Z-W92-S16 | BLOCKING | INERT | REMEDIATED | lib/opal_data_harvest/tab_transport.py:163 falls back when a __Host- cookie is refused; test_ai2_ft_session.py:183 plants it |
| A | Z-W92-S17 | OBSERVATION | INERT | OPEN | ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait) |
| A | Z-C-S56 | OBSERVATION | INERT | REMEDIATED | ledger/ROUND_ANALYSIS.round36.md (added @e38e50aa55) answers this compile |
| A | Z-C-S57 | BLOCKING | ARMED | REMEDIATED | investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S62 (DISARMED by its owner) |
| A | Z-W90-S11 | OBSERVATION | INERT | REMEDIATED | the row's own notes: a later worker cut on this face needs the six paths in its cone |
| A | Z-C-S59 | OBSERVATION | INERT | REMEDIATED | superseded by Z-C-S64 (ADJUDICATION_v49 @76f4381bce): limb 2a graded per run under ruling 8; round 37 CLOSED on it (ROUND_ANALYSIS.round37 @29fbb123e0 |
| A | Z-C-S60 | OBSERVATION | INERT | REMEDIATED | superseded by Z-C-S64 (ADJUDICATION_v49 @76f4381bce): bbg 2a MET on 13 runs per ruling 8; round 37 CLOSED on it (@29fbb123e0) |
| A | Z-W90-S14 | OBSERVATION | INERT | OPEN | graduated by Z-C-S63 (ADJUDICATION_v49 @76f4381bce); not cut in round 38 (ROUND_ANALYSIS.round37 @29fbb123e0 section 3) |
| A | Z-W92-S18 | BLOCKING | INERT | OPEN | ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait) |
| A | Z-W92-S19 | BLOCKING | INERT | OPEN | ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait) |
| A | Z-S66 | BLOCKING | INERT | OPEN | ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait) |
| A | Z-W92-S20 | BLOCKING | INERT | OPEN | ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait) |
| A | Z-W90-S21 | BLOCKING | INERT | OPEN | ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait) |
| A | Z-C-S62 | BLOCKING | INERT | OPEN | ROUND_ANALYSIS.round37.md @29fbb123e0 rulings 1-2 (option (c) rejected, (a) adopted as the qualified wait) |
| A | Z-C-S63 | OBSERVATION | INERT | OPEN | ROUND_ANALYSIS.round37 @29fbb123e0 section 3: the round-38 enrichment list (FWD-16, FWD-17, FWD-6 density, ft) does not cut either item |
| B | Z-W21-S1 | OBSERVATION | ARMED | REMEDIATED | the order is terminal; AC3 passes on the amended text (@76ba64b079) |
| B | Z-W21-S2 | OBSERVATION | ARMED | REMEDIATED | the base suite is green since: lib/opal_data_harvest 442 passed, 1 skipped after 220a74350a (Z-S52 evidence); ab-1 close @da63b88ccd 0 regressed |
| B | Z-W22-S2 | OBSERVATION | ARMED | OPEN | mitigated only: @3669bd0f0a retries a no-response request twice, but a thrice-failing body still cools the whole publisher |
| B | Z-S27 | OBSERVATION | ARMED | REMEDIATED | lib/opal_data_harvest/__main__.py:68-71 help now reads 'writes nothing to S3 by itself ... text fixed by AMGT_HARVST-Z-S27' |
| B | Z-S31 | OBSERVATION | ARMED | REMEDIATED | w-4 drain @09230f554a: the ft duplicate reaches gold once per security, no double count |
| B | Z-S32 | OBSERVATION | ARMED | REMEDIATED | bbg collects on the tab transport: 89 of 89 pairs, 1,239 stored (ROUND37_DRAIN_END_PACKET.md @4162e8837b section 5) |
| B | Z-S1 | OBSERVATION | INERT | REMEDIATED | forward half closed (Z-C-S12, t-2 5 of 5 byte-equal); backward half classified at round 4 (ROUND_ANALYSIS.round4 @2b196119f8); as-received objects now |
| B | Z-S11 | OBSERVATION | ARMED | OPEN | proof-of-spec-check.py still has no runnability check (0 hits for 'runnab' at HEAD) |
| B | Z-S19 | OBSERVATION | INERT | OPEN | still live: s3://opal-data-harvest/universe/v1/2026-09-16.json (newest of 2) names HAL_US_Equity 'Haliburton HAL' |
| B | Z-S2 | OBSERVATION | INERT | REMEDIATED | fix @4793cc8be4 (HVST-r-3): explicit publisher column on gold article_security_mention (publication_gold.py:66) |
| B | Z-S20 | OBSERVATION | INERT | OPEN | still live: the newest universe object carries the folder-name spelling 'Haliburton HAL' |
| B | Z-S21 | OBSERVATION | INERT | OPEN | unproven: gold identity now comes from the crosswalk and the 212-key gold universe (@e0d3a13ef1), but no record shows R-75's EDGAR arm retired as an i |
| B | Z-S23 | OBSERVATION | ARMED | OPEN | no fix named: a census that reads the channel can still count its own written result |
| B | Z-S3 | OBSERVATION | ARMED | REMEDIATED | corrected by row Z-S12 (@fa2234df4d: population 232, not 103); the order is terminal |
| B | Z-S5 | OBSERVATION | ARMED | REMEDIATED | withdrawn: row Z-S8 (@b507e89a9f) withdraws Z-S7 and with it Z-S5's universal claim; ADJUDICATION_v4 @8ed2954c2d and v6 @7d9831b17e |
| B | Z-W10-S3 | OBSERVATION | ARMED | REMEDIATED | z-3 @58135da029 / drain @03e86f2909: 8 of 8 dotted-string patch sites re-targeted onto the imported module object |
| B | Z-W10-S8 | OBSERVATION | ARMED | REMEDIATED | lib/opal_data_harvest/silver_from_bronze.py:189-199 keeps pageProps verbatim in one page_config_json column (row Z-W10-S8) |
| B | Z-W11-S1 | OBSERVATION | ARMED | OPEN | still live: .tools/missions-tree-index.py:162-171 walks org/missions with iterdir (physical tree) |
| B | Z-W14-S2 | OBSERVATION | ARMED | REMEDIATED | z-3 @03e86f2909 re-targeted the patch sites and imports |
| B | Z-W19-S1 | OBSERVATION | INERT | REMEDIATED | TO-HVST-s-1 last <status>closed</status>; the CLI contract is one security object per file (__main__.py:147) |
| B | Z-W8-S2 | OBSERVATION | ARMED | OPEN | unproven: no proof-of-spec-check commit since 09-20 names the coverage-frame fix; later instances grade VALID, which is not a fix |
| B | Z-W9-S1 | OBSERVATION | ARMED | OPEN | still live on the listings half: store.silver_append keys part-<run_stamp>.parquet with IfNoneMatch='*' (store.py:463-471) |
| B | Z-W26-S1 | OBSERVATION | ARMED | OPEN | the class stays: no lib/__init__.py at HEAD; z-3 re-targeted sites, it added no guard |
| B | Z-S33 | BLOCKING | ARMED | REMEDIATED | portal HeaderBrief.tsx:198 mounts TimelinePanel in the header; the PROD-equal walk tmp/ui-walk/20261002T180024Z shot 005 shows 'MENTION TIMELINE' (rea |
| B | Z-W29-S1 | OBSERVATION | ARMED | OPEN | no standing identity-source clause in AMGT_HARVST_DECOMP.md (0 hits) |
| B | Z-W30-S1 | OBSERVATION | ARMED | OPEN | no standing 'git -C portal' clause in AMGT_HARVST_DECOMP.md (0 hits) |
