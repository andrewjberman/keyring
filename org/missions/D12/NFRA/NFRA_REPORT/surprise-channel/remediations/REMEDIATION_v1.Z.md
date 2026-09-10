# NFRA_REPORT -- surprise channel, REMEDIATION v1 (site Z) -- THE ROUND-2 SLUG

**Home:** the project tree's channel (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5). **Lane:** the CVO only.
**Cut by:** `3.0.0_SA_CVO~Z` at 2026-09-10T08:1xZ, round 2. **Reader:** `1.0.0_SA_CTO~Z`, and no one else.

**L10 PRECONDITION, MEASURED ON THE GATE'S OWN FUNCTION** (`.tools/surprise-row-gate.py::_latest_dispositions`,
imported and called, root = repo root):

```
24 items | UNDISPOSITIONED 0 | GRADUATED 13 | DISMISSED_WITH_REASON 11
CONTROL: the same call on NFRA_OPSEC202609 returns 167 items / 61 undispositioned,
         so the census fires on a second project and the zero is a measurement, not an empty read.
```

**AND A SECOND PREDICATE THIS DOCUMENT ASSERTS THAT NO GATE CHECKS:** all 24 items carry a disposition set by a
CVO adjudication row. Before `C-S10`/`C-S11` only 8 did -- 8 more had been set by a peer's disarm row and 8 by the
surfacing seat's own `disposition` field -- and the L10 precondition read MET throughout, because it enforces that a
disposition EXISTS and never who set it. The mechanism is in `C-S10`; it is a property of the shared resolver, not of
this project, and it is the reason this slug carries 13 rows rather than 21.

**THIS SLUG CARRIES BOTH ROUNDS.** Round 1 was RECUT rather than closed and never issued a slug, so its graduated
rows had no carrier; each row's `round` field records the round whose adjudication graduated it.

**Judgment criteria:** 2 of 2 graded at `C-S8` (`RP-s-15` AC5 and `RP-s-19` AC4, both PASS). Neither was named in the
L8 packet; both were found by censusing all 24 round-2 criteria for `judgment=true`.

**AND THIS DOCUMENT REQUIRED AN AUDITED GATE OVERRIDE, DISCLOSED HERE RATHER THAN ONLY IN THE COMMIT.**
`.tools/surprise-row-gate.py::_coordinate_violations` refuses any NEW row carrying `W<n>` when the committer is not
that worker -- the allocator discipline. Protocol s.5 requires a remediation row's `id` to EQUAL the graduated
investigation row's id, and 7 of these 13 rows were surfaced by workers and so carry `W1`/`W2`. The two rules are in
direct conflict, and the gate cannot tell MINTING an id from CARRYING one: a remediation row by construction re-uses
an id minted elsewhere, and graded as an allocation every worker-surfaced graduation is refused.

MEASURED, and it is why this had not surfaced before: across the 7 remediation documents already in the estate --
NFRA_CLDGRPH v1/v2/v3, NFRA_COMPEFFICACY v1, NFRA_OUTSET v1, NFRA_OPSEC202609 v1.Z, ETFS_GUARDRAIL v1 -- there are
**49 rows and ZERO carrying a W coordinate**. No slug in this estate has ever carried a worker-surfaced row, so the
conflict had no instance until a round whose graduated set is MAJORITY worker rows. The alternative to the override
was dropping 7 of 13 rows, which would have silently lost most of the round's findings from the only artifact that
carries them forward. NOT REMEDIATED and not designed here: the gate is the CTO's surface.

**What this document is NOT.** It routes nothing and names no limb: a remediation row carries no route and no loop
target. `owner` names the lane that would BUILD each remedy, as the schema requires -- it is not an assignment, and
`2.0.0_SA_COO~ZZ`'s recut is the only thing that turns any of it into work.

---

```json
[
  {
    "id": "NFRA_REPORT-Z-S1",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RP-s-1's cell text covers only the two-axis vocabulary, but the S1 manifest row it mirrors covers FWD-2 AND FWD-4 including 'the property+owner attribution riding both' -- so FWD-4's attribution axis was never cut into any cell of this round, and the L6 coverage limb cannot see it because that limb grades cell IDS against the decomposition's id space, never a cell's TEXT against its manifest row's CONTENT.",
    "evidence": [
      "PRD NFRA_REPORT_PRD.md s.8 row S1 names outcomes 'FWD-2, FWD-4' and its surface text ends '... plus the property+owner attribution riding both'.",
      "NFRA_REPORT_DECOMP.md: enumeration of the token 'attribution' over the whole file returns 0 hit(s). The RP-s-1 cell text covers axis 1's six values, axis 2, GREEN, and the two expressibility gaps -- and no attribution limb.",
      "NFRA_REPORT.TO-RP-s-1.state-model-two-axis-vocabulary.md: enumeration of 'attribution' returns 0 hit(s). The worker face never carried the limb, and the worker face is the whole of a worker's context.",
      "The built deliverable deliverables/0.9.0_WK_NFRA_REPORT~1/STATE_MODEL.md: enumeration of 'UNGROUPED' returns 0 hit(s) and of 'Dashboard' returns 0 hit(s) -- it renders no attribution axis at all. The worker built exactly what it was given.",
      "L6 issuance @7d698685fe printed 'issuance coverage 12 of 12 cell(s) ... owned by the staged orders' and PASSED, because every cell id in the decomposition is owned by an order. Coverage by ID was complete while coverage by CONTENT was not."
    ],
    "remedy": "The L4 ADDENDUM ruled at Z-S3 has landed: manifest row S1 is NARROWED to FWD-2 and the attribution limb becomes its own row S13, which makes RP-s-1 an exact mirror of the narrowed row rather than a deficient cell. WHAT REMAINS for the recut is the coverage limb itself -- L6 grades cell IDS against the decomposition, so an outcome served by NO cell is structurally invisible to it. A coverage read per OUTCOME, not per cell id, is the durable fix and it is the CTO's L10 act rather than a cell.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-09T21:45:00Z"
    }
  },
  {
    "id": "NFRA_REPORT-Z-S10",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RP-s-13's MERGED deliverable ATTRIBUTION.md renders both `opal-gateway` and `opal-globgrph` as UNGROUPED, which was correct when it was built and is STALE as of PRD v0.7: Andrew-direct settled FWD-4's axis at FOUR members (Dashboard | Website | Gateway | Graph), and those two surfaces are the referents of the two new members. FWD-4 cannot grade REALIZED against the v0.7 bar while its own deliverable renders two NAMED members as ungrouped.",
    "evidence": [
      "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md at site-Z HEAD, parsed by row: `opal-gateway` (MCP server) -> `UNGROUPED`; `opal-globgrph` (ECS Fargate cluster) -> `UNGROUPED`. 2 of 2 of the rows the ruling moves.",
      "org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md at site-Z HEAD, line 13: \"attribution axis has FOUR MEMBERS -- `Dashboard | Website | Gateway | Graph`\" (Andrew-direct).",
      "Same PRD, line 295, naming the referent explicitly rather than leaving it to inference: \"Website, Gateway (the opal-gateway MCP server)\".",
      "Same PRD, lines 327-328, the four-member reasoning: \"`opal-gateway` (EC2, the MCP server) and `opal-globgrph` (ECS, 3 of 3 services) are BOTH live, BOTH always-on, and FAIL DIFFERENTLY\" -- which is why neither folds into Dashboard and why Graph's referent is opal-globgrph.",
      "1.0.0_SA_CTO~Z msg 20761 carrying the Andrew-direct at record 9382d107a3: \"UNGROUPED IS NOT RETIRED. It now means a live surface outside all four.\""
    ],
    "remedy": "A round-3 cell re-renders ATTRIBUTION.md against the v0.7 FOUR-member axis, so opal-gateway reads Gateway and opal-globgrph reads Graph instead of UNGROUPED. ⛔ FWD-4 CANNOT GRADE REALIZED UNTIL IT DOES. The cell is NOT deficient -- RP-s-13 was cut, built and merged while FWD-4 was under active Andrew adjudication and was overtaken twice; the worker was right at every vintage it read. The deliverable is machine-composed, which is what makes the re-render cheap.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZ",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZ",
      "at": "2026-09-10T12:46Z"
    }
  },
  {
    "id": "NFRA_REPORT-Z-S8",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ALL SEVEN round-2 task orders name deliverables/0.9.0_WK_NFRA_REPORT~1/ as the deliverable folder and inside every criterion invocation, regardless of which worker serial <issued_to> names -- so RP-s-13 (issued to ~2) and RP-s-14 (issued to ~3) both wrote into a folder named for ~1, and the deliverables tree no longer identifies which worker produced which artifact.",
    "evidence": [
      "Measured at 2026-09-10T02:1xZ by parsing all 7 round-2 order files: <issued_to> is ~1 for RP-s-15/16/18, ~2 for RP-s-13/19, ~3 for RP-s-14/17 -- while the set of deliverables/0.9.0_WK_NFRA_REPORT~<n>/ paths referenced in each file is {~1} for all 7 of 7.",
      "org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-13.attribution-axis-and-ungrouped.md: <issued_to>0.9.0_WK_NFRA_REPORT~2</issued_to> with all three criteria invoking against deliverables/0.9.0_WK_NFRA_REPORT~1/ATTRIBUTION.md.",
      "Landed artifacts at merge 63efc53452 (RP-s-13, worker ~2) and c2a582b17d (RP-s-14, worker ~3) both sit under deliverables/0.9.0_WK_NFRA_REPORT~1/."
    ],
    "remedy": "Round 3's L6 cut derives each order's deliverable folder FROM its <issued_to> rather than from a literal, so the deliverables tree identifies its author. NOT a mid-round edit: RP-s-14 is merged with its criteria pinned to the ~1 path and rewriting the open orders would split one round across two conventions.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZ",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_REPORT-Z-S9",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "NFRA_REPORT HAS NO ledger/ DIRECTORY AT ALL. The spine's L10 names three ledger artifacts for a project -- ROUND_ANALYSIS.round<N>.md (CTO), COMPLETION_REPORT.round<N>.json (COO) and COMPLETION_GRADES.round<N>.json (CTO) -- and none exists here. Round 1's round-N analysis was written to the CTO's own deliverables instead, and surprise-channel/remediations/ is EMPTY, so round 1's remediation document (the CVO's one artifact of the round, per spine L10) was never written either.",
    "evidence": [
      "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md at site-Z HEAD, L10 section: 'the CTO writes ledger/ROUND_ANALYSIS.round<N>.md'; '2.0.0_SA_COO ... writes ledger/COMPLETION_REPORT.round<N>.json'; '1.0.0_SA_CTO ... writes ledger/COMPLETION_GRADES.round<N>.json'; 'The CVO writes the round's remediation document, the one artifact of the round'.",
      "Measured over the tracked corpus (denominator: 31000 tracked files, git ls-files): ROUND_ANALYSIS 7 hits, all under NFRA_CLDGRPH/ledger (3), NFRA_COMPEFFICACY/ledger (1) and NFRA_OUTSET/ledger (2) -- ZERO under NFRA_REPORT. COMPLETION_REPORT 7 hits (one is the schema at org/standards/) -- ZERO under NFRA_REPORT. COMPLETION_GRADES 3 hits -- ZERO under NFRA_REPORT.",
      "org/missions/D12/NFRA/NFRA_REPORT/ directory listing: decompositions/, deliverables/, prd/, project.json, surprise-channel/, task-orders/ -- no ledger/.",
      "org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/remediations/ is an existing but EMPTY directory.",
      "org/standards/COMPLETION_REPORT.schema.json EXISTS (11023 bytes), so the contract the COO limb writes against is present and this is not a missing-contract problem."
    ],
    "remedy": "ledger/ now exists and carries COMPLETION_REPORT.round2.json, which discharges the COO limb (disarmed at Z-S11). TWO LIMBS REMAIN AND NEITHER IS THE COO'S: ROUND_ANALYSIS.round<N>.md and COMPLETION_GRADES.round<N>.json are 1.0.0_SA_CTO~Z's, and round 2 cannot read CLOSED under rule 27 until COMPLETION_GRADES exists with every grade REALIZED. Round 1's analysis was written to the CTO's own deliverables rather than the project ledger; whether that is back-filled is the CTO's call and this row does not ask for it.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZ",
      "at": "2026-09-10T07:05:00Z"
    }
  },
  {
    "id": "NFRA_REPORT-Z-W1-S1",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RP-s-7: comp-blast's served kuzu graph models NO edge at all between GOLD_SCRIPT nodes and Lambda/portal nodes -- confirmed by a positive-control FAILURE on a definitely-live lambda -- so a 'zero downstream consumers' or 'zero upstream gold: ancestor' result from comp-blast is not evidence for OR against C-DEPRECATED-TERMINUS, for ANY gold script in the estate, not only this cell's ten candidates.",
    "evidence": [
      "comp-blast 'gold:B_01.holdings_lots' --direction downstream --json, 2026-09-09 ~21:0xZ: WITHIN BUDGET, scanned 164 of 164, 164 distinct ids returned, prefixes {gold:77, s3:87} -- ZERO ids of any other prefix (no lambda:, component:, jsx:, arn: node reached).",
      "REPEATED on 8 more gold scripts (B_02, A_03, INF_D_00, INF_D_04, INF_D_07, INF_D_03, INF_D_02b, INF_C_01, INF_D_00c) -- every single one returns ONLY gold:/s3: prefixed ids where non-zero, or ANSWER-STATE: PRESENT_WITH_ZERO_RESULTS (0 of 0 scanned) where zero -- including INF_D_00b.portal_timeseries.py, a script named for portal serving and NOT one of this cell's ten candidates, which ALSO returned PRESENT_WITH_ZERO_RESULTS.",
      "POSITIVE CONTROL, the discriminating read: comp-blast 'arn:aws:lambda:us-east-1:313476888478:function:inf-api-positions' --direction upstream --json, 2026-09-09 ~21:1xZ -- this lambda is independently known-live (it backs a served portal API route per infra/aws/lambda/inf-pipeline/inf-api-positions). Its upstream ancestor set in the SAME graph returns 14 ids, prefixes {system:2, motif:3, motifi:7, arn:1, event-source:1} -- ZERO gold: ancestors, even though this lambda demonstrably reads gold-layer output at runtime. The graph is blind to this edge type in EITHER direction, on a node proven to be alive, not merely on the ten candidates under test.",
      "the graph DOES model the client-facing layer generally (comp-blast 'component:AdvisorsTab.tsx' NOT-FOUND response prints the live node-type census: ReactComponent=442, JSXRender=1433, JSXElement=2205, GOLD_SCRIPT=1380, S3_DATA_KEY=294 -- so the blindness is a specific missing EDGE TYPE (GOLD_SCRIPT<->Lambda/ReactComponent), not an absent NODE population; the graph has both endpoints and no path recorded between them for gold-layer artifacts."
    ],
    "remedy": "comp-blast's graph gains the GOLD_SCRIPT <-> Lambda/ReactComponent edge class. RECORDED AS LIMIT 1 AND NOT FIXED: the disarm made the limit citable, it did not repair the graph, and Z-S5 says so in its own words. Until then a comp-blast zero on that edge class is not evidence in either direction.",
    "owner": "0.8.0_AE_CloudComp",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.8.0_AE_CloudComp",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-09T23:20:00Z"
    }
  },
  {
    "id": "NFRA_REPORT-Z-W1-S2",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RP-s-7: comp-pipescript's static WRITES parser misses dynamically-constructed S3 keys (prefix-variable concatenation, or a write routed through a helper function taking a computed key) -- producing a FALSE 'WRITES: (none detected)' for 2 of this cell's ten candidates, one of which (INF_C_01.canonical_nna.py) is textually a heavily-governed, actively-maintained production chokepoint, not a dead script.",
    "evidence": [
      "comp-pipescript io INF_D_07.concentration_risk.py --pipeline inf-gold, 2026-09-09: prints 'WRITES: (none detected)'. comp-read data/inf/scripts/gold/INF_D_07.concentration_risk.py --for 'what does this script write, and to what S3 key' surfaces (AUTHORITATIVE, line 55): CONCENTRATION_RISK_KEY = OUTPUT_PREFIX + 'firm/concentration_risk.json', with OUTPUT_PREFIX defaulting to 'platinum/' (line 54) -- a real write key the static parser did not resolve because it is built by string concatenation of a module-level variable rather than a literal or f-string.",
      "comp-pipescript io INF_C_01.canonical_nna.py --pipeline inf-gold, 2026-09-09: also prints 'WRITES: (none detected)'. comp-read on the same file shows a _write_s3(df, key) helper (line 251-258) called with a key built by a separate _nna_key() function and an output-prefix guard _set_out_prefix() (lines 259-299) -- the write exists and is real, routed through two levels of indirection the static parser does not follow.",
      "INF_C_01.canonical_nna.py's own header comments (lines ~68-77, ~92, ~269, ~282, read via comp-read) describe it as part of an 'ATOMIC SET' with three guard libraries, a 'gold-dispatch chokepoint APPLIED + EXERCISED', 'NEVER#2 co-signed by CTO + COO', and a SERVE-RELEASE-ACK discipline -- textual, in-repo evidence of active, heavily-governed production status, the OPPOSITE of the 'looks deprecated' reading Andrew's ruling 6 offered for this artifact at hop 1.",
      "comp-platinum reverse 'platinum/firm/concentration_risk.json' --firm inf: PRODUCER field returns BLANK (the tool's own static write-index has no entry for this key at all, confirming the parser miss propagates downstream into the portal-reverse-lookup tool too, not only comp-pipescript's own io view)."
    ],
    "remedy": "comp-pipescript's static WRITES parser gains dynamically-constructed S3 keys (prefix-variable concatenation and helper-routed computed keys). RECORDED AS LIMIT 2 AND NOT FIXED -- Z-S6 states 'the PARSER IS NOT FIXED'. The false negative PROPAGATES into comp-platinum reverse, so the remedy is one parser and two consumers.",
    "owner": "0.8.0_AE_CloudComp",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.8.0_AE_CloudComp",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-09T23:21:00Z"
    }
  },
  {
    "id": "NFRA_REPORT-Z-W1-S3",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RP-s-11's AC1 invocation as literally written -- 'bash .tools/comp-find . --corpus aws IAM_ROLE --limit 5' -- fails rc=2 with a bash syntax error, because .tools/comp-find is a Python script (shebang #!/usr/bin/env python3), not a bash script; the working form is the shimmed 'comp-find' or 'python .tools/comp-find'.",
    "evidence": [
      "timeout 120 bash .tools/comp-find '.' --corpus aws IAM_ROLE --limit 5, run 2026-09-09 this session -> rc=2, '.tools/comp-find: line 5: ...: command not found' / 'line 6: syntax error near unexpected token (' -- bash attempting to interpret Python source as shell script.",
      "file .tools/comp-find -> 'Python script, ASCII text executable'; head -c 300 shows '#!/usr/bin/env python3'.",
      "The corrected, functionally-identical invocation 'comp-find . --corpus aws IAM_ROLE --limit 5' (using the ~/bin/comp-find forwarder, per CLAUDE.md's shim mechanism) run the same session -> rc=0, VINTAGE line present with a real UTC timestamp, DENOMINATOR: 219 hit(s) across 219 aws node(s) [types=IAM_ROLE] -- the substantive result AC1 is actually testing for."
    ],
    "remedy": "Carried from round 1's C-S3, which exercised the criterion in BOTH directions: the literal invocation cannot succeed and the corrected form does carry the vintage the criterion wanted. The remedy is the corrected invocation form at the next cut.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZ",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_REPORT-Z-W1-S4",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RP-s-11: two live, UNDECLARED API Gateways -- including one named 'trade-submission-api' -- and one live, DECLARED CloudFront distribution match ZERO of the estate's 51 CloudWatch alarms by name/ID/dimension, positive-controlled against siblings that DO match (session-analytics-api: 4 alarms; the other CloudFront distribution: 3 alarms via a structural DistributionId dimension match).",
    "evidence": [
      "comp-find '.' --corpus aws API_GW --all, 2026-09-09: 5 of 5 API_GW nodes, DRIFT DECLARED=2 LIVE-no-DECLARED=3 -- the 3 undeclared are opal-session-analytics-api, sentiment-query-api, trade-submission-api.",
      "comp-find 'trade-submission|w8jnzvs21g' --corpus aws CW_ALARM --all -> 0 of 51 hits. comp-find 'sentiment-query|cxm5b58nme' --corpus aws CW_ALARM --all -> 0 of 51 hits. comp-find 'session-analytics|f7lvfv4bjc' --corpus aws CW_ALARM --all -> 4 of 51 hits (opal-session-analytics-errors/estimated-monthly-cost/high-invocations/throttles) -- the positive control proving the 51-alarm sweep and the name/ID match method can and does return non-zero when a real match exists.",
      "comp-find '.' --corpus aws CLOUDFRONT_DISTRIBUTION --all -> 2 of 2 distributions, both DECLARED: E1DHJH4Y1W8YC2 (aliases: [], target_origin wp-origin) and EVTSA9VEHNZVH (aliases: opalinvest.dev, www.opalinvest.dev). comp-find 'DistributionId' --corpus aws CW_ALARM --all -> exactly 3 of 51 alarms carry a DistributionId dimension, ALL THREE = EVTSA9VEHNZVH (cloudfront-high-error-rate, cloudfront-high-origin-latency, cloudfront-low-cache-hit-rate). comp-find 'E1DHJH4Y1W8YC2' --corpus aws CW_ALARM --all -> 0 of 51 hits, structurally, not by weaker name-substring: NO alarm's DistributionId, name, or ARN mentions it at all.",
      "This is the SAME 51-alarm population NFRA_OPSEC202609-Z-S151 and this project's own ALERT_DELIVERY.md (RP-s-6) already swept for a DIFFERENT question (delivery-leg confirmation on alarms that exist); this row is upstream of that one -- it asks whether an ALARM EXISTS AT ALL for a given served surface, not whether an existing alarm's delivery works."
    ],
    "remedy": "Two live UNDECLARED API Gateways -- one of them trade-submission-api -- match ZERO of the estate's 51 CloudWatch alarms, positive-controlled against siblings that DO match. Z-S7 widened it: trade-submission-api is a LIVE, PORTAL-CONSUMED trade submission AND APPROVAL workflow whose lambdas, table, bucket and role are all DECLARED while the API Gateway itself is LIVE-no-DECLARED. The remedy is declaration plus alarm coverage, and it is infrastructure work outside this project.",
    "owner": "0.7.0_AE_CloudOps",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-09T23:22:00Z"
    }
  },
  {
    "id": "NFRA_REPORT-Z-W2-S1",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RP-s-5: the live EC2 fleet (32 instances, us-east-1, full sweep) exceeds the 27-service declared manifest by 10 undeclared instances -- 8 remain undeclared after this cell's two backfills (bd-gold-detail-generator, estate-report-runner's churned id).",
    "evidence": [
      "aws ec2 describe-instances --region us-east-1 (no instance-id filter) run 2026-09-09T20:10Z -- 32 of 32 Reservations/Instances returned; cross-checked 0 of 0 in us-east-2 and us-west-2 the same session",
      "infra/aws/ec2/EC2_MANIFEST.json services (27 keys) at HEAD 7ea739b7b5 -- 25 of 27 rows carried a non-null instance_id (24 of 25 distinct, one by-design duplicate bd-allocations/bd-price-runner), of which 22 of 24 resolved live and 2 of 24 did not (orion-crawl-harness, estate-report-runner)",
      "the 10 live instances with no matching manifest row: 1 extra i-07ebae29a16e43ed1 (Name=seeking-alpha-scraper), 7 extra under Name=historical-prices-fetcher (i-0416edf7e4b901380, i-094c504a4384f9c47, i-025cba31603a6c8a6, i-032fa1babe1abe48a, i-0ec91038b9a2c73a6, i-088e7fa9323bac1b9, i-03c397afaa967d978), 1 x i-074bfc40ee049dc62 (Name=bd-gold-detail-generator, backfilled into the manifest by this cell), 1 x i-0584e17d283fa7ef4 (Name=estate-report-runner, backfilled into the manifest by this cell replacing the stale i-0512bd3cbaf602b7f)",
      "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/COMPUTE_MANIFEST_FINDINGS.md s.2 -- the full reconciliation table and the historical-prices-scheduler Lambda note (EC2_MANIFEST.json historical-prices-fetcher._note) consistent with a launch-fresh-instance-per-run mechanism"
    ],
    "remedy": "Carried from round 1's C-S1, which reproduced the finding EXACTLY at the CVO seat five hours later and recorded a manifest defect the row itself did not name. Remedy rides the next cut.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZ",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_REPORT-Z-W2-S2",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RP-s-5's always-on-by-group naming (Dashboard, Website, Graph, per ruling 15b verbatim) conflicts with two OTHER canonical artifacts of this same project that both render the third name as 'Gateway' -- and 'Gateway' and 'Graph' are confirmed to be two DIFFERENT, both-real compute surfaces.",
    "evidence": [
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md:313,365 -- Andrew verbatim, batch 6: 'should be named separately id say by group (Dashboard, Website, Graph)'; ruling 15b's own surrounding prose (:369-371) discusses 'no graph-ops box' and '7 unused opal-globgrph-* security groups', i.e. Graph = the graph-database infra",
      "org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md s.6 (rulings that bind), first ruling: 'the three properties are Dashboard (the entire serverless system feeding opalinvest.dev), Website, Gateway (the opal-gateway MCP server)' -- names the third group Gateway, not Graph, and glosses it explicitly as the opal-gateway MCP server",
      "org/projects/NFRA_REPORT.json (generated_at 2026-09-09T19:35:31Z) name field: 'across three properties (Dashboard, Website, Gateway)' -- the registered project record independently repeats 'Gateway'",
      "this cell's own live ECS enumeration (aws ecs list-clusters/describe-clusters/list-services/describe-services --region us-east-1, 2026-09-09T20:10Z): 1 of 1 cluster opal-globgrph, ACTIVE, 3 of 3 services (globgrph-nessie/trino/serving) running, desiredCount=1 each, 0 of 0 scheduled scaling actions -- confirming 'Graph' has real, always-on compute distinct from opal-gateway (EC2 i-07dccb1615503ac99, t4g.nano, confirmed running live, systemd opal-gateway.service behind an ALB)"
    ],
    "remedy": "RESOLVED AT L4 IN PRD v0.4 @a535ae513e (disarmed at Z-S2): the Gateway-vs-Graph conflict was TWO AXES welded by an inference in ruling 15b's own prose, not a contest between two names for one axis. This row is the direct ancestor of the FOUR-member axis ruled at v0.7, and therefore of Z-S10.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-09T21:44:00Z"
    }
  },
  {
    "id": "NFRA_REPORT-Z-W2-S3",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-RP-s-5's carried premise 'the manifest is itself 2014.2h old' (L1 brief vintage) is stale as of this cell's re-grounding: the manifest's own _last_updated is ~62 minutes old, not ~84 days, because an intervening opal-gateway deploy touched the file after the brief's vintage.",
    "evidence": [
      "infra/aws/ec2/EC2_MANIFEST.json (worktree, pre-this-cell's-edit) top-level _last_updated: '2026-09-09T19:08:11Z'",
      "date -u run at 2026-09-09T20:10:24Z (this session) -- ~62 minutes after _last_updated, not ~2014 hours",
      "git log -1 --format='%H %ci' -- infra/aws/ec2/EC2_MANIFEST.json -> commit 9f76655b9f, 2026-09-09 15:08:18 -0400 (=19:08:18Z), subject 'Deploy EC2 opal-gateway @ 7bd89b5d71' -- an operational deploy record write, not a full re-sync, landed after the L1 brief's cited vintage @37ff80867a"
    ],
    "remedy": "Carried from round 1's C-S2: the re-grounding is right and the mechanism it names is confirmed by the offending commit's own subject line. Remedy rides the next cut.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZ",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_REPORT-Z-W2-S4",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RP-s-9: box-grain cost attribution is blocked by a payer-account Cost Explorer setting (resource-level data opt-in DISABLED, confirmed live) and by cost-allocation tag coarseness/drift -- both independent of RP-s-5's manifest fix and outside this project's write surface, so RP-s-5 landing does NOT fully unblock box grain as the original bound's stated reason implied it would.",
    "evidence": [
      "aws ce get-cost-and-usage-with-resources --time-period Start=2026-09-01,End=2026-09-09 --granularity DAILY --metrics UnblendedCost --group-by Type=DIMENSION,Key=RESOURCE_ID --filter '{\"Dimensions\":{\"Key\":\"SERVICE\",\"Values\":[\"Amazon Elastic Compute Cloud - Compute\"]}}' run 2026-09-09 this session -> AccessDeniedException: 'Resource-level data granularity is an opt-in only feature. You can be enable this feature from the PAYER account's Cost Explorer Settings page.'",
      "aws ce list-cost-allocation-tags --status Active run 2026-09-09 this session -> exactly 7 active tags (System, Pipeline, Owner, Partner, Macro, Project, Environment), unchanged from the L1 brief's 2026-07-07 measurement; none is a per-instance-unique key",
      "aws ec2 describe-instances --region us-east-1 (Tags) run 2026-09-09 this session -> System=bd-pipeline shared by 5 declared EC2 rows (bd-allocations, bd-gold-layer-runner, bd-transactions, bd-assets, bd-fees); System=InflectionPipeline shared by 4 (inf-gold-layer-runner, inf-gold-qa-runner, inf-exporter, inf-bronze-runner); System absent (null) on 9 of 27 declared rows (all 8 live historical-prices-fetcher instances + canonical-schwab-si2); bd-gold-qa-runner tagged System=BDPipeline (differently cased from its 5 bd-pipeline siblings)",
      "org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/COST_ANOMALY.md s.2/s.2a -- the full reasoning and the System-tag intermediate-grain table cross-referenced against RP-s-5's EC2_MANIFEST.json v1.1"
    ],
    "remedy": "Box-grain cost attribution needs resource-level Cost Explorer data opted IN at the payer account (get-cost-and-usage-with-resources currently returns AccessDeniedException, confirmed live) and cost-allocation tag coverage repaired. BOTH CAUSES ARE INDEPENDENT OF RP-s-5 and outside this project's write surface, so RP-s-5 landing does NOT unblock box grain -- which is the half the row exists to prevent a reader assuming.",
    "owner": "0.7.0_AE_CloudOps",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.7.0_AE_CloudOps",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "0.9.0_WK_NFRA_REPORT~2",
      "at": "2026-09-09T22:00:00Z"
    }
  },
  {
    "id": "NFRA_REPORT-Z-W2-S6",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RP-s-19 grounding (ANOMALY_IN_EDITION.md, row opal-infrastructure-alerts): comp-blast's SNS-topic downstream check extracts Lambda and SQS protocol subscriber edges (positive-controlled on two other topics) but never models a raw phone-number/email endpoint as a node -- so a topic whose ENTIRE live subscriber set is SMS/email renders PHANTOM-CONSUMER identically whether that endpoint is healthy, broken or genuinely absent, and this edition's own BREACH row is exactly that case.",
    "evidence": [
      "comp-blast 'arn:aws:sns:us-east-1:313476888478:opal-infrastructure-alerts' --direction downstream --check-consumers, run this session: WITHIN BUDGET, scanned 0 of 0 traversal, PHANTOM-CONSUMER rc=4 -- 'zero dependents IN GRAPH (both directions)' -- while the same node's --direction both --json call, same session, returns 70 of 70 consumers (24 CW_ALARM, 5 LAMBDA, 2 EVENT_RULE, 2 EVENT_SOURCE, 1 C3System, 36 C2Motif) EVERY ONE at direction=upstream (feeds the topic); zero of 70 at direction=downstream (reads the topic).",
      "POSITIVE CONTROL 1: comp-blast 'inf-otp-alert' --direction downstream --check-consumers, same session -- CONSUMER-OK, 8 of 8 dependents, including LAMBDA node inf-ec2-retry-launch at direction=downstream. ALERT_DELIVERY.md sec.1 (RP-s-6, QUOTED) records this same topic's confirmed subscriptions as exactly 'lambda, sms' -- so the Lambda-protocol leg IS extracted as a downstream edge when one exists; the tool is not broadly blind to SNS subscriptions.",
      "POSITIVE CONTROL 2: comp-blast 'opal-critical-surface-alerts' --direction downstream --check-consumers, same session -- CONSUMER-OK, 1 of 1 dependent, SQS_QUEUE opal-critical-surface-alerts-coo at direction=downstream, matching ALERT_DELIVERY.md sec.1's 'sqs, sms' confirmed pair for this topic -- the SQS protocol leg is also extracted.",
      "ALERT_DELIVERY.md sec.4 (RP-s-6, this worktree, QUOTED, live AWS read not this graph): opal-infrastructure-alerts' one confirmed SNS subscription is protocol sms, endpoint +17862617679, sandbox status Pending (registered, not Verified) -- a real subscriber exists and is independently shown non-functional by a live call, entirely outside what comp-blast's graph can see either way."
    ],
    "remedy": "comp-blast's graph models a raw SNS destination endpoint (phone number / email) as a node, so PHANTOM-CONSUMER can distinguish 'no subscriber' from 'no graph-typed subscriber'. RECORDED AS LIMIT 3 AND NOT FIXED, exactly as LIMIT 1 and LIMIT 2 were left: the disarm is the citable entry, verified present at INSTRUMENT_LIMITS.md line 81 by this seat.",
    "owner": "0.8.0_AE_CloudComp",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "0.8.0_AE_CloudComp",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "0.9.0_WK_NFRA_REPORT~2",
      "at": "2026-09-10T02:32:00Z"
    }
  }
]
```
