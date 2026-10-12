# IRPT_BCKEND: remediations, the ~P slug (rounds 117 to 164)

<sweep_watermark>2026-10-12T17:40Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T17:40:00Z. Follows ADJUDICATION_v65. L8 inputs: the held compiles of rounds 117 to 160
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md`, removed in this commit), `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_161_162_P_DRAIN_END_20261012.md` and
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_163_164_P_DRAIN_END_20261012.md` (blob 081cb2b959, msg 6436). No judgment criterion in rounds 161 to 164.
Graduated, round label v165: 28 rows, OPEN; 2 BLOCKING, ARMED 0. Owners: `2.0.0_SA_COO~P2` 8, `1.0.0_SA_CTO~DELL2` 20.
For the CTO's analysis: round 164 counts the claim moves under C-CHAINCLAIM (49F SI 18 as written, 23 if a NON-POSITIVE-BASE day with a
prior position also moves; orion 0 as written, 894); round 163 could not read the stored report (D2-W324-S1), so the S18 count against
the predicted 36 is not established.

```json
[
 {
  "id": "IRPT_BCKEND-D2-S60",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "A signature-closure sweep of the 13 fetchable live irpt-* zips (17 functions; 4 fetch failures) finds keyword splits symbol_closure cannot see: served.py:1006 InteractiveAccess(profile_reader=) in irpt-status and irpt-performance-adapter (packaged interactive_access.py: __init__(read_headers, data_firm, *, ordinary_authorizer)); served.py:1021 guard_prospect(authorize_owner=, resolve_owner=) in irpt-narrative. CloudWatch also shows irpt-performance-adapter raising Enforcer.__init__() unexpected keyword load_report_owner (2 events in 24h), which this check did not catch.",
  "evidence": [
   "investigation row D2-S60",
   "row D2-S102 and this seat's read row D2-S108"
  ],
  "remedy": "DISARMED by this compile (row D2-S108): the three named functions read 0 TypeError over 24 hours on their current code. Residual remediation: run the signature-closure instrument on irpt-49f-reporting-read-lambda, irpt-export-render and irpt-holdings-refresh-lambda (never fetched), and exercise the 4 method-call sites in irpt-ycharts-generate (D2-S102).",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v165"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": "2026-10-12T17:40:00Z"
  }
 },
 {
  "id": "IRPT_BCKEND-D2-S84",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IRPT_BCKEND is named EXPIRY OWNER of a TRANSITIONAL live row in the routed 49 Financial bucket alias: dell1's ADVI_FIRMBKTS lets the IRPT readers and the two gold writers keep reading investor-reporting/directory/ there instead of copying it into the firm's canonical bucket; the row expires at IRPT_BCKEND's RI1 move. Information only; no act was asked of dell2.",
  "evidence": [
   "investigation row D2-S84"
  ],
  "remedy": "IRPT_BCKEND names the date its readers and two gold writers stop reading investor-reporting/directory/ through the routed alias, so the TRANSITIONAL row can expire; the owner records that date on dell1's ADVI_FIRMBKTS row.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W284-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The existing close-anchor instrument keeps ONE price per CUSIP (last row wins), but a CUSIP in the blackdiamond_z09 silver carries different row prices on 50 of 85 graded days; the S252 minority is mostly rows inside securities, not whole securities, so IB-pr-425 grades every row and decides a security-day by a stated precedence. S3 reads went through boto3 (as the existing instrument does), not the .tools/aws CLI shim.",
  "evidence": [
   "investigation row D2-W284-S1"
  ],
  "remedy": "The close-anchor instrument keys a price per (CUSIP, row), or states which row wins, before any grade relies on it.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-S98",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Noted for the vendor producer's NEXT release (CTO msgs 5665 and 5784): a vendor section on the wire carries no title member and no field name for a value; the page now supplies both from a pinned copy of the census. PARKED: the producer cannot be released while the vendor path is stopped.",
  "evidence": [
   "investigation row D2-S98"
  ],
  "remedy": "PARKED for the vendor producer's next release: the wire carries a title member, a field name per value and what each column is (rows D2-S103, D2-W324-S2 fold in). Closed by that release's live read.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-S101",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "IB157-1-AC1 requires the record to carry the ledger's slug and IB157-1-AC3 refuses any bounded eight-digit run in the record; this seat named its ledger slug with a trailing date, so the true slug trips AC3 and the only two ways to pass are to edit the check, which the order forbids, or to record a slug that is not the real one.",
  "evidence": [
   "investigation row D2-S101"
  ],
  "remedy": "A check's bounded-eight-digit refusal limb collides with dated ledger slugs, dated keys and true row counts: 4 instances (D2-W315-S1, D2-S101, D2-W317-S2, and IB155's row count). The issuer scopes the limb to values that can carry an account number before the next cut.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-S104",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The narrow gate refused cottonwood at the 2026-10-12 14:15Z fire (account_lost 9 of 851 candidate accounts), so cottonwood still serves business_date 2026-10-08; the gate did its job and the freshness cost is real.",
  "evidence": [
   "investigation row D2-S104"
  ],
  "remedy": "cottonwood serves business_date 2026-10-08 after the narrow gate refused it at the 2026-10-12 14:15Z fire (account_lost 9 of 851). The owner reads the next fire; if refused again, the 9 accounts go to the CTO.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-S105",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "SSM returns only the first 24000 characters of the holdings command's stdout, which are all \"Classification not found\" lines, so no OK:/REFUSED: verdict line or rc line is retrievable for any of the three firms; the orders' \"output line\" criterion can pass on a statement of absence.",
  "evidence": [
   "investigation row D2-S105"
  ],
  "remedy": "The holdings command's stdout is flooded with 'Classification not found' lines, so SSM's first 24,000 characters carry no verdict line. The command writes its OK:/REFUSED: line and rc to a retrievable place (stderr tail or S3) before an order grades an 'output line'.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W318-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The four authorizer commits after the source map's last_deployed_commit 26ffa22b79 are not unreleased: two CLOSED deploy ledgers record them applied (2026-09-25 and 2026-10-03), and the live package carries them; the map's commit and date fields were not advanced",
  "evidence": [
   "investigation row D2-W318-S2"
  ],
  "remedy": "The source map's last_deployed_commit, last_deployed_at and artifact_sha256 are advanced to the live releases (authorizer; irpt-commentary-draft-store-lambda, row D2-W312-S1, folds in).",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-S72",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "build-and-upload.sh checks pinned members into the shared worktree and restores them from HEAD afterwards; twice in one session that restore failed with 'Unable to create .git/index.lock: File exists' because another seat was committing, and each time it printed only a WARN and exited rc=0, so a tracked file could be left carrying staged content with no error.",
  "evidence": [
   "investigation row D2-S72"
  ],
  "remedy": "build-and-upload.sh stops loud when its restore from HEAD fails on .git/index.lock, and never leaves pinned members checked into a shared worktree.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-S76",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "round-close-check.py without --workstream reads IRPT_BCKEND round 122 as REFUSED: 13 seat-folder orders carry no <round> tag and are counted in every round, and one of them, IRPT_BCKEND.TO-APPLY-Y77 (issued by 2.0.0_SA_COO~Y2, complete), has no proof instance at the name the checker expects. Scoped to --workstream ~P the same round reads MAY-CLOSE (1 order, proof ok).",
  "evidence": [
   "investigation row D2-S76"
  ],
  "remedy": "round-close-check.py without --workstream counts 13 seat-folder orders with no <round> tag in every round. Either the tool scopes them or the orders carry a round tag.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-S83",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "INSTRUMENT: the PRD sign-off gate read the ratified-text half SIGNED and current on text its signer had not seen. The half's hash is taken over the ENDPOINT and CONTRACTS sections; ADDENDUM v0.34 changes the contract in an addendum appended below them, whose own heading says the half re-opens, and the hash did not move. This seat's signature was on v0.33. The review happened because an issuer's packet said so, not because the gate or the notifier asked.",
  "evidence": [
   "investigation row D2-S83"
  ],
  "remedy": "INSTRUMENT: the PRD sign-off hash covers the ENDPOINT and CONTRACTS sections only, so an ADDENDUM appended below them that changes a contract reads SIGNED on text the signer never saw. The hash covers every section that changes a contract (prd_signoff_lib.py).",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W282-S3",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "test_holdings_gold_calendar_gap.py::test_the_fallback_calendar_is_graded_in_its_own_years_and_clipped_outside_them fails because the trading-calendar hardcoded fallback covers 2010-2027 and the test reaches 2028.",
  "evidence": [
   "investigation row D2-W282-S3"
  ],
  "remedy": "lib/trading_calendar.py's hardcoded fallback ends at 2027, and round 162's 125-day count ran on the fallback table (D2-W323-S1). Extend the fallback or make the fallback path print that it ran.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W295-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The portal wire generator cannot render the Opal form's $ref into the v2 report schema (opal://irpt/contracts/v2/...): its ref grammar admits only a v1 sibling document, so the order's 'Opal form by $ref into the v2 schema' throws on the Opal form's provider member.",
  "evidence": [
   "investigation row D2-W295-S2"
  ],
  "remedy": "The portal wire generator's $ref grammar admits a v1 sibling only, so the Opal form cannot be referenced into the v2 report schema. Widen the grammar or re-state the order.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W302-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The capture's probe has no challenge classification: a reply the READ path would call WAF_CHALLENGE (a waf-action header of challenge/captcha/block, or a 202/403/405 with the awswaf marker) is only status-classified as NOT_LIVE, so an accepted sign-in whose probe is challenged ends as failure_class AUTH_FAILED / reason NO_AUTHENTICATED_PROBE, the label of a rejected credential.",
  "evidence": [
   "investigation row D2-W302-S1"
  ],
  "remedy": "The ycharts capture probe has no challenge classification (a WAF challenge reads only NOT_LIVE) while the READ path has one. Classify it the same way.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W302-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The discriminating probe pair is vacuous when the jar holds no aws-waf-token: both arms send the identical token-less request, so 'same status in both arms' (fifth run: 202/202, waf_token_cookie_in_jar false in both) separates nothing about the token.",
  "evidence": [
   "investigation row D2-W302-S2"
  ],
  "remedy": "The discriminating probe pair is vacuous when the jar holds no aws-waf-token (both arms identical). The pair runs only when it can discriminate, or says it could not.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W302-S3",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The persisted receipt keeps the probe's WAF action class and content-type class only for the FIRST probe after the submission (the pair, built once), not per step, and keeps no body marker, probe path or identity-leg record, so the leaf that would settle a header-less interstitial is not persisted.",
  "evidence": [
   "investigation row D2-W302-S3"
  ],
  "remedy": "The persisted receipt keeps the WAF and content-type class for the first probe only, with no body marker, path or identity-leg record. Persist them per step.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-S85",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The capture's full receipt (login_submission, probe_pair, warmup, login_path, screen) is consumed in process by run_capture and written nowhere, so the only surviving host evidence is eight step lines in a per-run-truncated stderr file; and the library's explicit SIGNED_OUT_APP_CHROME diagnosis for exactly the condition those step lines show is gated on `!filled`, so after a submission the same condition degrades to the uninformative NO_AUTHENTICATED_PROBE.",
  "evidence": [
   "investigation row D2-S85"
  ],
  "remedy": "The capture's full receipt is consumed in process and written nowhere; the only host evidence is a per-run-truncated stderr file. Persist the receipt.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W309-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "commentary_ref is set as a sibling attribute of the request item, not inside the immutable record, yet the packager reads record.get('commentary_ref') from DynamoAcceptance.get, which returns only the record attribute.",
  "evidence": [
   "investigation row D2-W309-S2"
  ],
  "remedy": "Read at HEAD whether the packager can see commentary_ref (set as a sibling attribute, read from the record). The finding came from a worktree cut at 0bdd920114 (see D2-S99); if HEAD reads it, close as vintage.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W312-S3",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The resident_worker.py inside the irpt-ycharts-generate zip, live and built, has neither producer_for nor send_ready_if_ticketed, so the Opal-producer branch and the I3 gate AMENDMENT 1 leans on are not in this package; the host's installed package was not read",
  "evidence": [
   "investigation row D2-W312-S3"
  ],
  "remedy": "Read the live irpt-ycharts-generate package (released again 2026-10-12): if resident_worker.py still lacks producer_for and send_ready_if_ticketed, the I3 gate AMENDMENT 1 relies on is not in the package.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W313-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The existing 07:30 and 07:41 America/New_York fires are before the entry's partition usually lands (11:46Z) while daylight time holds; a producer for the entry that reused those times would grade a day before its partition exists",
  "evidence": [
   "investigation row D2-W313-S2"
  ],
  "remedy": "A producer for the 49F entry must fire after its partition lands (~11:46Z), not at the existing 07:30 and 07:41 America/New_York times. State the trigger in the producer's cell.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W315-S3",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The landed prices store was last written 2026-10-09 but its newest yahoo-labelled point is dated 2026-06-05 (newest of any label 2026-06-09), and no schedule for its writer was found",
  "evidence": [
   "investigation row D2-W315-S3"
  ],
  "remedy": "The landed prices store was written 2026-10-09 but its newest yahoo-labelled point is 2026-06-05, and no schedule for its writer was found. Name the writer and its schedule, or retire the store as a source.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W321-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The holdings producer writes the opening and closing value as start_value and end_value; the portal adapter reads beginning_market_value and ending_market_value, so by the code the two value tiles read 'not supplied' for a holdings-basis answer",
  "evidence": [
   "investigation row D2-W321-S1"
  ],
  "remedy": "The holdings producer writes start_value and end_value; the portal adapter reads beginning_market_value and ending_market_value, so both value tiles read 'not supplied' on a holdings-basis answer. One side renames.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W321-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "By the code every holdings-basis performance answer is state PARTIAL, because three absences are added unconditionally, so the only trace of absences the portal shows does not tell a window with a non-OK day from one without",
  "evidence": [
   "investigation row D2-W321-S2"
  ],
  "remedy": "Every holdings-basis answer is PARTIAL because three absences are added unconditionally, so the portal cannot tell a window with a non-OK day from one without. Add an absence only when it holds.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W322-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Interior is 'between two OK days' and last row is the final row; a non-OK run after the last OK row longer than one row is neither, and the reader still skips it.",
  "evidence": [
   "investigation row D2-W322-S2"
  ],
  "remedy": "C-CHAINCLAIM's day rule covers interior and last-row days but not a non-OK run after the last OK row that is not the final row (33,472 days at 49F since inception); the reader still skips them. The contract names their class.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W325-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "NON-POSITIVE-BASE is not one population: the 49F entry's days are almost all no-position-with-a-cash-debit, the orion entry's days are all in accounts with a position row, and the orion share is 575039 of 1430575 gold rows.",
  "evidence": [
   "investigation row D2-W325-S1"
  ],
  "remedy": "NON-POSITIVE-BASE is two populations: 49F's are cash-debit days with no position; orion's are all accounts with a position row, 575,039 of 1,430,575 gold rows. The contract states which population moves the claim (round 164's counts).",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W324-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The stored-report get of the column-meaning read was refused by KMS: the dell2 agent identity may list the analysis_reports prefix but may not decrypt an object in it",
  "evidence": [
   "investigation row D2-W324-S1"
  ],
  "remedy": "The dell2 agent identity is refused kms:Decrypt on the analysis_reports objects, the irpt-requests and irpt-jobs table keys, and iam:SimulatePrincipalPolicy on the firm holdings roles (rows D2-S88, D2-W317-S3, D2-S100 fold in; simulate reads ALLOWED where the key policy refuses). A grant is a cloud permission change: the CTO rules it or names another reader.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W324-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two census sections can carry one field label on one census page, and the extractor locates a label by the first hit with a value on the page: S15 and S16 both list 'Standard Deviation' on page 10",
  "evidence": [
   "investigation row D2-W324-S2"
  ],
  "remedy": "S15 and S16 both list 'Standard Deviation' on census page 10, and the extractor takes the first label hit, so one printed row can yield two section ids (INFERRED). Read one stored report once a reader can decrypt it (D2-W324-S1), then fix the extractor.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W310-S3",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Seven of the 878 tickers asked returned no bar, three of them class-share tickers written with a dot (BF.B, BRK.A, BRK.B); the dash spelling was not tried because nothing is re-asked",
  "evidence": [
   "investigation row D2-W310-S3"
  ],
  "remedy": "Seven of the 878 tickers return no bar, three of them dotted class shares (BF.B, BRK.A, BRK.B). The demand queue's issuer on dell1 is told the dash spelling was never tried.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v165",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v165"
  },
  "closed": false
 }
]
```
