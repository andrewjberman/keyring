# IRPT_BCKEND -- project sweep 9 remediations

<sweep_watermark>2026-10-07T08:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07. Graduated at sweep 9's L9 (ADJUDICATION_v24.md), round label v61 (the round after
IRPT_BCKEND round 60). 20 rows: 5 REMEDIATED and closed on a served or committed read (S322, S324, S326, W121-S1, W123-S1); 1 REMEDIATED
and not closed, its disarm owed by its owner (S335); 14 OPEN (S320, S334, S337, S338, S339, S340, S341, S342, S343, S344, S345, S346,
S347, W127-S1). ARMED after this compile: S334, S335 (BLOCKING), S339, S347 (BLOCKING), W127-S1. Owners are the dell2 successor lanes where the predecessor's
session is closed (`2.0.0_SA_COO~P2`, `2.0.0_SA_COO~Y2`); a disarm already filed keeps the serial that filed it.

S340, S341, S342, S345 and S346 are one owed exercise: a single export-render, which waits on Andrew's per-use word.

Clocks advanced in place at this compile (state fields only: remediation.state, closed, and disarm where it read ARMED):
- From W116-S2..S14 (2.0.0_SA_COO~P via worker ~116, 2026-10-04T23:19Z; ADJUDICATION_v24 C-S288): REMEDIATED and closed --
  S147 (v10; disarm DISARMED at 23:19Z), S214, S216 (v13), W86-S1, W86-S2 (v14; W86-S2 disarm DISARMED at 23:19Z), S238 (v15; disarm DISARMED by its owner 1.0.0_SA_CTO at
  2026-10-01T07:18:15Z, row S248, which W116-S5 cites), S245, S257, W99-S3 (v16; S257 and W99-S3 disarm DISARMED), W101-S15, W101-S6, W104-S1, W104-S2, W104-S3, W104-S4, W105-S1,
  W105-S2 (v18).
- From the disarm records (C-S289): S318 (v19; DISARMED by 2.0.0_SA_COO~Y at 2026-10-05T00:20Z, row S325), S284 (v18; DISARMED by
  ~Y at 03:58Z, S327), W69-S1 (v11; DISARMED by ~P at 04:38Z, S328), W100-S2 (v16; DISARMED by ~P at 04:58Z, S331), S218 (v13;
  DISARMED by ~P at 05:55Z, S333), W80-S1 (v13; DISARMED by ~P at 14:25Z, S336): each REMEDIATED and closed. S204 (v12; disarm already
  DISARMED 2026-09-29): closed as moot, its failing path retired for 49F by B3 (S332); the remediation state reads REMEDIATED because
  the retirement is the remedy.
Not moved: S252 (v16, parked by its own declaration).

```json
[
  {
    "id": "IRPT_BCKEND-S320",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The close leg of ledger irpt-y5d did not run the recorder with --function, so lambda-source-map.json records irpt-ycharts-generate at a hash the function no longer runs (CTO batch 234's class remedy).",
    "evidence": [
      "investigation row IRPT_BCKEND-S320",
      "lambda-source-map.json at dell2 CLOUD c2bc15f427: irpt-ycharts-generate deployed_code_sha256 FgZcBjJuwuBD.., last_deployed_at 2026-10-04T21:19:06Z; lambda get-function-configuration: live CodeSha256 uFTONal/RhfoETes.., LastModified 2026-10-04T01:57:24Z (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)",
      "the record was re-written at 21:19Z on 10-04, after this row, still at the old hash"
    ],
    "remedy": "Run the recorder for irpt-ycharts-generate with --function at the live hash; add the step to the ~Y close-leg checklist.",
    "owner": "2.0.0_SA_COO~Y2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y2",
      "round": "v61"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S322",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Three source-map rows keyed irpt-reporting-{gold,publish,read}-lambda named no live function; the live functions are builder-named irpt-49f-reporting-*.",
    "evidence": [
      "investigation row IRPT_BCKEND-S322",
      "IB-pr-316 drained @f9d6238f11 (source map rows keyed by live names; S322, S178)",
      "lambda-source-map.json at c2bc15f427: irpt-49f-reporting-gold-lambda Mex71Y5gk9RY.., -publish-lambda AH5r60vpxR/G.., -read-lambda cou/Td9ydDrn..; lambda get-function-configuration of the three: equal (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)"
    ],
    "remedy": "Done: the rows are keyed by the live names and record the live hashes. The artifact S3 key of these rows still carries the old name; that is S343's.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S324",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A PATH B export bundle carried neither narrative_packet.json nor an analysis-report reference, which ADDENDUM v0.24 refuses.",
    "evidence": [
      "investigation row IRPT_BCKEND-S324",
      "CTO RULINGS batch 247 item 2: PRD v0.27 ruling 28 adds narrative_state NOT_ATTACHED with its reason; FWD-8 stays NOT REALIZED until a branded export carries its narrative page",
      "IB-pr-317 drained @82ff1bf64a; served in r58 (IRPT_BCKEND_ROUNDS_52_60_P_DRAIN_END_20261007.md)",
      "live irpt-export-render CodeSha256 exDoi/uo5e.., LastModified 2026-10-06T01:35:28Z: the zip's bundle.py and irpt_contracts/ExportBundle.schema.json carry NOT_ATTACHED (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)"
    ],
    "remedy": "Done in the running bytes: a PATH B export now declares narrative_state NOT_ATTACHED with its reason. No export has run on these bytes yet; that exercise is S340's family. FWD-8 is unchanged by this row.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S326",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "GET /analysis/requests paged in request-id order, not newest first, so a just-submitted request could stay off the list.",
    "evidence": [
      "investigation row IRPT_BCKEND-S326",
      "investigation row IRPT_BCKEND-S329 (2.0.0_SA_COO~Y, 04:48Z): the disarm; fix 44cc631396, CTO half batch 253 @4bbe1bd830; ledger irpt-s326-history-20261005 CLOSED (U1, D1, V1)",
      "V1 route read IRPT_MVP_Y/S326/V1_HISTORY_READ_COTTONWOOD.json @202da5f5dc (REQ-c1b53772 first, 30 rows newest first); V1 page: 2.0.0_SA_COO~D msg 105156"
    ],
    "remedy": "Done and served: irpt-status reads the history whole (bounded at 2,000), newest first, with the cursor contract unchanged.",
    "owner": "2.0.0_SA_COO~Y2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y2",
      "round": "v61"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-05T04:48:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W121-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The 49F perfrp_performance_account leaf, still carrying the inflated 2025-01-10 day, had a live reader: the PROD Advisor Intelligence page through shared-advisor-router.",
    "evidence": [
      "investigation row IRPT_BCKEND-W121-S1",
      "investigation row IRPT_BCKEND-S331 (2.0.0_SA_COO~P, 04:58Z): the disarm; CTO batches 251, 254 and 256; Andrew card 1 @c9c8e0c191; CTO half @4a63c9b600, COO half @48fa2860ab",
      "ledger irpt-w100s2-perfrp-leaf-withdrawal-20261005 CLOSED @752ffa138a: delete marker current, head 404, prior version kept for rollback"
    ],
    "remedy": "Done: the leaf is withdrawn and the route answers as for a never-served key (403/403/200).",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-05T04:58:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W123-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "S297's fix made _days_to_compute return [] on a landed target, and lambda_handler (results[-1]) and _target_day (days[-1]) indexed the empty list, so a re-fire raised IndexError.",
    "evidence": [
      "investigation row IRPT_BCKEND-W123-S1",
      "IB-pr-320 drained @f9e1c4ab96 under amendment 1 @37e246c6df (W123-S1 empty-plan no-op); released in r54 @9bb0ab46b7 (holdings-performance, 49F and INF)",
      "infra/aws/lambda/investor-reporting/holdings-performance/handler.py at c2bc15f427: 'return days[-1] if days else None' and 'if not days: ... TARGET_ALREADY_LANDED' (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)",
      "live irpt-inf-holdings-performance-lambda CodeSha256 DaDtnTCq.., LastModified 2026-10-05T14:21:07Z: handler.py in the zip carries TARGET_ALREADY_LANDED (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)",
      "not read: the 49F function's zip"
    ],
    "remedy": "Done and served: an empty plan answers a no-op (rc 0, reason TARGET_ALREADY_LANDED).",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-10-05T14:21:07Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S334",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "safe-apply's comp-tagauthz pre-apply gate calls aws iam get-account-authorization-details, which makes no progress, so the gate fails closed on every tree that sets default_tags.",
    "evidence": [
      "investigation row IRPT_BCKEND-S334",
      "CTO RULINGS batch 259 (TAGAUTHZ_OVERRIDE authorized for the one r54 code-hash apply; the gate's hang filed to the gate's owner)",
      "git log .tools/comp-tagauthz*: newest commit 65ec0e0f5a (2026-07-09); no change since this row (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)"
    ],
    "remedy": "The gate evaluates a default_tags tree in bounded time: a timeout on the IAM read, or a narrower read than the account-wide authorization details.",
    "owner": "the comp-tagauthz gate's owner, via 1.0.0_SA_CTO",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "the comp-tagauthz gate's owner, via 1.0.0_SA_CTO",
      "round": "v61"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "the comp-tagauthz gate's owner via 1.0.0_SA_CTO",
      "at": "2026-10-08T18:04:52Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S335",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The directory refresh dispatcher starts the runner EC2 and hands the build over before its SSM agent is Online, so a start-then-dispatch fails by construction (HAND_OVER_RUNNER_OFFLINE).",
    "evidence": [
      "investigation row IRPT_BCKEND-S335",
      "IB-pr-325 drained @45ac71f1c7 under amendment 1; applied @fb8f047e40 (1 add); CTO batches 264 and 265 (the half signed with four outcomes); ledger irpt-s335-retry-schedule-20261005 CLOSED",
      "s3 latest.json at opal-data-bd, opal-data-inf and opal-data-cot: generated 2026-10-06T13:40:46Z / 13:40:51Z / 13:40:46Z, as-of 2026-10-05 / 2026-10-06 / 2026-10-05 (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)",
      "the 10-06 refresh manifests do not read READY at any firm: 49F and INF stop at RUNNING, REFRESH_DISPATCHED, revision pending (last written 13:40:39Z and 13:40:45Z); COT has no _refresh/2026-10-06/ manifest and wrote its fire's result under _refresh/2026-09-22/ (row S348) (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)"
    ],
    "remedy": "Done in effect: the 13:40Z retry fire moved the served directory at all three firms on 10-06. The disarm is the owner's, and the row's own condition reads 'lands READY at all three firms'; the pointers say yes and the manifests say no. Its disarm row should state which it reads, with S348.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": "2026-10-07T08:14:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S337",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "IB-pr-324's worker census reported irpt-ycharts-generate with 4 changed members and 0 riders; the issuer's re-census at f36a8cdefd reads 19 (15 fixtures/har and templates.json changes no order of the round produced), and the checker trusted the census file.",
    "evidence": [
      "investigation row IRPT_BCKEND-S337",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/r57_census/census-irpt-ycharts-generate.json (19 changed) vs deliverables/0.9.0_WK_IRPT_BCKEND~127/R56_REPIN_CENSUS.json (4 changed)",
      "irpt-ycharts-generate held out of r57 and r58; live CodeSha256 uFTONal/.. since 2026-10-04T01:57:24Z (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)"
    ],
    "remedy": "The next census criterion re-derives the census by its own build against live, never reading a worker-written file; the 15 unclaimed members of irpt-ycharts-generate get an owner before that function's next release.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S338",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Inflection's holdings_performance_daily gold holds no partition for 2026-05-11, 2026-06-30 and 2026-08-10, so leg A1 of ledger irpt-inf-performance-serving-20261002 cannot close.",
    "evidence": [
      "investigation row IRPT_BCKEND-S338",
      "IRPT_BCKEND_ROUNDS_52_60_P_DRAIN_END_20261007.md: OPEN; whether Inflection held positions on those days is UNMEASURED"
    ],
    "remedy": "Read Inflection's positions for the three days; a day with positions is a backfill under the producer's own rule, a day without is a declared absence on the ledger.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": true
  },
  {
    "id": "IRPT_BCKEND-S339",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "build_resident_package.py packages the whole tree at its --pin, so a resident build ships every merged-but-unreleased change under the package directories.",
    "evidence": [
      "investigation row IRPT_BCKEND-S339",
      "commits c1dd9ada9c (IRPT_YCDGEN TO-YCD-n-6, 'resident package builder --member PACKAGED=REPO; gate reads members_added') and 2b5f4f00e1 (TO-YCD-m-6, 'a named file list') on build_resident_package.py, 2026-10-05 (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)",
      "no disarm row filed by 2.0.0_SA_COO~Y"
    ],
    "remedy": "A resident build carries a named member list. The two IRPT_YCDGEN commits may be that remedy; the disarm owner reads one build against its list and files the disarm.",
    "owner": "2.0.0_SA_COO~Y2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y2",
      "round": "v61"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y2",
      "at": "2026-10-07T08:39:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-S340",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Ledger irpt-export-async-submit-20260927 closed SUPERSEDED on a content read of the running bytes; its A1 behaviour (async submit) was never exercised (CTO batch 270 item 2).",
    "evidence": [
      "investigation row IRPT_BCKEND-S340",
      "ledger close 4d5bb92d30; row 5f9926e04d"
    ],
    "remedy": "One export-render of a selection whose sections exercise the behaviour, read to READY with a %PDF body; starting an export is a write that may reach a vendor render path, so it waits on Andrew's per-use word. One export can carry S340, S341, S342, S345 and S346 together.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S341",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Ledger irpt-export-receipt-running-20260928 closed SUPERSEDED on a content read of the running bytes; its A1 behaviour (a pending receipt answers RUNNING) was never exercised (CTO batch 270 item 2).",
    "evidence": [
      "investigation row IRPT_BCKEND-S341",
      "ledger close 4d5bb92d30; row 5f9926e04d"
    ],
    "remedy": "One export-render of a selection whose sections exercise the behaviour, read to READY with a %PDF body; starting an export is a write that may reach a vendor render path, so it waits on Andrew's per-use word. One export can carry S340, S341, S342, S345 and S346 together.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S342",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Ledger irpt-export-reopen-rule-20260927 closed SUPERSEDED on a content read of the running bytes; its A1 behaviour (the reopen rule) was never exercised (CTO batch 270 item 2).",
    "evidence": [
      "investigation row IRPT_BCKEND-S342",
      "ledger close 4d5bb92d30; row 5f9926e04d"
    ],
    "remedy": "One export-render of a selection whose sections exercise the behaviour, read to READY with a %PDF body; starting an export is a write that may reach a vendor render path, so it waits on Andrew's per-use word. One export can carry S340, S341, S342, S345 and S346 together.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S343",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "build-and-upload.sh:354 sets S3_KEY=\"$PIPELINE/$FN_NAME.zip\", so irpt-49f-reporting-read-lambda uploads under its function name while the source map and reporting-read/main.tf read investor-reporting/irpt-reporting-read-lambda.zip; r57 and r58 each needed a server-side copy before apply.",
    "evidence": [
      "investigation row IRPT_BCKEND-S343",
      "lambda-source-map.json at c2bc15f427: the three irpt-49f-reporting rows carry artifact_s3_key investor-reporting/irpt-reporting-{gold,publish,read}-lambda.zip (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)"
    ],
    "remedy": "One key per function: the builder writes the key the map and Terraform read (or the map and main.tf move to the builder's key) in one change, so no release needs a hand copy.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S344",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "HELD, not re-measured: record-terraform-deploy.sh sweeps an already-dirty audit file into its commit, the lane gate refuses it, and each retry appends another CHANGELOG.json entry; irpt-holdings artifact_sha256 was left stale.",
    "evidence": [
      "investigation row IRPT_BCKEND-S344",
      "the row's grounding is INFERRED (from the predecessor's session log, gap (b)); a later fix 8be38c9dec by 0.7.0_AE_CloudOps~RV is not read for this"
    ],
    "remedy": "The owner measures the recorder at HEAD: it stages only its own paths, and a retry does not duplicate a CHANGELOG entry.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S345",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Ledger irpt-adapter-render-grant-kms-20260927 closes SUPERSEDED (CTO batch 270): DecryptRenderGrantsViaS3Only is live on irpt-performance-adapter-role, but its A1 proof (a RENDER_DELEGATE render reads Performance) was never exercised.",
    "evidence": [
      "investigation row IRPT_BCKEND-S345",
      "row commit 4584021a00 (2.0.0_SA_COO~P2)"
    ],
    "remedy": "One export-render of a selection whose sections exercise the behaviour, read to READY with a %PDF body; starting an export is a write that may reach a vendor render path, so it waits on Andrew's per-use word. One export can carry S340, S341, S342, S345 and S346 together.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S346",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Ledger irpt-adapter-render-selection-20260927 closes SUPERSEDED (CTO batch 270): the grant-pinned selection change is in the running irpt-performance-adapter build, but its A1 proof was never exercised.",
    "evidence": [
      "investigation row IRPT_BCKEND-S346",
      "row commit 4584021a00 (2.0.0_SA_COO~P2); live irpt-performance-adapter CodeSha256 NU6YVERLJ0.. = source map (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)"
    ],
    "remedy": "One export-render of a selection whose sections exercise the behaviour, read to READY with a %PDF body; starting an export is a write that may reach a vendor render path, so it waits on Andrew's per-use word. One export can carry S340, S341, S342, S345 and S346 together.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S347",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "An explicit deny in opal-data-inflection's bucket policy refuses s3:ListBucket to cloudops-dell2-agent-user, so the dell2 successor of workstream P cannot measure S338 or close leg A1 of ledger irpt-inf-performance-serving-20261002.",
    "evidence": [
      "investigation row IRPT_BCKEND-S347",
      "row commit ce0b9df49c (2.0.0_SA_COO~P2, surfaced 07:55Z)",
      "NFRA_CTLPLN PRD v0.12 C-ROLES (origin CLOUD 2f61412157): the laptop keeps roles, resource policies and any half that changes IAM; a Dell CTO lane does not"
    ],
    "remedy": "Either (a) a principal already permitted on opal-data-inflection reads the three gap days and their upstream positions, or (b) the dell2 identity is admitted read-only. Option (b) is an access change: under NFRA_CTLPLN v0.12 it goes to the laptop 1.0.0_SA_CTO as a role request, not to 1.0.0_SA_CTO~DELL2 as the row says, and it passes the cross-firm guard. This compile does not choose between them.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": "2026-10-07T08:14:00Z"
    }
  },
  {
    "id": "IRPT_BCKEND-W127-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "irpt-performance-adapter cannot be built: the ADHC_DRIFTD.002 parity gate refuses three source_dir files absent from files[] (build_candidate.py, build_dependencies.py, cot_probe.py).",
    "evidence": [
      "investigation row IRPT_BCKEND-W127-S1",
      "lambda-source-map.json at c2bc15f427: irpt-performance-adapter files[] (71 entries) still holds none of the three (this compile's read, dell2, 2026-10-07 ~07:5xZ-08:2xZ)",
      "CTO RULINGS batch 270 item 3: the adapter was held out of r57; nothing closes on r57's evidence for it"
    ],
    "remedy": "Register the three files in files[] or rule them out, before any deploy build of irpt-performance-adapter.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v61",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v61"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": "2026-10-07T09:46:49Z"
    }
  }
]
```
