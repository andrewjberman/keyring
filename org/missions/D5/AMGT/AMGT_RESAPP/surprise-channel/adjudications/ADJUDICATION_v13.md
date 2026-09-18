# AMGT_RESAPP round 13: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-18T17:45Z. LOCAL on SITEZ.
**Inputs:** every round-13 proof instance at HEAD; the channel census by `.tools/surprise-row-gate.py`
`_latest_dispositions` and `_open_tos_census`; this seat's working record `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND13_L9_WORKING_RECORD_20260918_Z.md`.

## Round state and the L10 precondition

The resolver reads **0 of 97 orders open**. `AMGT-rk-26` was withdrawn by its issuer on Andrew's word at
`5dc9089ca7`, and "withdrawn" is one of the gate's terminal words.

Acceptance was read over **every one of round 13's 15 orders**, per criterion, in three classes: **26 PASS, 3 FAIL,
0 UNVERIFIABLE-BY-INSTRUMENT**. `rk-26` has no instance. All three FAILs are **criterion defects**, and none was
flipped (row C-S308):
- `rk-23` AC1 sends a raw slash where the page sends `%2F`.
- `rk-20` AC1 names a shape the world never had.
- `rk-30` adapter AC1 asks for measured values the round never committed to produce.

**Items.** 47 open at the census, plus **5** that non-CVO seats closed on their own rows. The resolver read those
as closed without an adjudication. **All 52 are adjudicated here**, in 30 rows (C-S292 to C-S321).

## Judgment grades

None can be recorded. `rk-26` carried round 13's only two judgment criteria, and it was withdrawn with no proof
instance; the grade carrier requires one. Round 12's `rk-2` AC6 and `rk-8` AC4 stay NOT_EVALUATED as graded in
ADJUDICATION_v12. The missing instrument is now named: an authenticated browser-network capture through the real
edge, which MFA blocks (row C-S316).

## Round-12 remediations advanced to REMEDIATED in REMEDIATION_v12

| row | evidence |
|---|---|
| `W23-S5` | R13-A landed (0f297b6ba6) and the chart serves three verified filing points for BA (C-S301, C-S302). |
| `S137` | rk-20 landed the generation contract; both axes serve 2026-09-15 on a COMPLETE pointer (Z-S161). |
| `S141` | rk-23 made artifact names path-safe; print serves both slash names on the page request shape (msg 23610); the routing question is W27-S10. |
| `S139` | rk-24 adapter serves the stored classed no-CIK reason for 21 of 21 names (Z-S165) and rk-24 producer wrote 178 of 178 UNRESOLVED-SOURCE objects. |

`S117`, `S119` and `S121` stay OPEN.

## Rows
```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S292",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED: round 13 was issued TWICE by two continuations of ONE seat identity -- f0cbb2d813 then the re-cut 7acf65b08b -- and each spawned its own workers, so four cells were written in two generations. ONE ISSUER PER ROUND held by no mechanism when both issuers carry the same serial.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S154 (2.0.0_SA_COO~Z, first-hand): the first continuation adopted an uncommitted, unattributed draft of the 15 orders, cut f0cbb2d813 and spawned five workers from da2c3c479a before learning a second continuation had re-cut the round (62e9cfbf60 / 7acf65b08b) and spawned seven more.",
        "Z-S152 @2f3840fc21 (this seat): at 14:45Z, 14:54Z and 15:08Z the live edits sat in worktrees based at da2c3c479a, which does not carry the re-cut; chain CK was written in both generations.",
        "Measured cost: rk-19 producer, rk-21 and rk-28 each drained ONE generation and left the other on an unmerged branch (0f297b6ba6 second parent 7aef98df54; 339473fab4; e56b59fa22 second parent c9816ba669). chain SP wrote two key shapes (Z-S155). BA_US_Equity analysis object written four times 14:57Z-16:02Z with thesis_driver points 3,1,1,3 (msg 23547)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "CLAUDE.md Rule 27: ONE ISSUER PER ROUND -- L6 ONE ISSUANCE is cut by ONE COO instance; two instances issuing into the same round is the collision (two cuts, two issuances, an ambiguous L8).",
    "world_is": "The rule names instances; the collision here was between two CONTINUATIONS of the same instance serial, which the rule text does not distinguish and no gate refuses. Both continuations acted correctly on what each could see.",
    "notes": "Remedy holder 1.0.0_SA_CTO~Z (law and gate): a round must not accept a second issuance commit once one exists. A mechanical refusal keyed to the round, not to the serial, is what distinguishes two continuations that share a serial.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S154"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S293",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED onto S154: four rows that record the same double issuance -- this seat observation (S152), the issuer consolidated account (S156), its correction (S157), and the worker row whose surprise it explains (W26-S5).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S156 (2.0.0_SA_COO~Z) carried disposition GRADUATED on its OWN row with no remediation row bearing its id; its cells are dispositioned one by one in this document, so the self-set disposition is superseded, not adopted.",
        "S157: rk-21 was NOT merged when S156 said so; verified here -- 339473fab4 and 0ebf8a54b8 are both ancestors of HEAD, with a positive control on the HEAD read.",
        "W26-S5: the object it found already corrected was written by the OTHER generation of the same cell. s3://opal-data-harvest/filings/v1/BA_US_Equity/000162828026004357.analysis.json has 7 versions and IsTruncated False; none between 05:18:47Z and 14:57:27Z. The row guessed the Z-S150/Z-S151 diagnostic pair had written a fix; both of those seats made GETs only (this seat msg 23547, 1.0.0_SA_CTO~Z msg 23548)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each of the four rows is filed as its own observation.",
    "world_is": "All four describe one event whose mechanism and remedy are carried by S154.",
    "notes": "W26-S5 is worth keeping in the record as a CORRECT worker observation with a wrong guess about the cause: it saw the twin writer and named the wrong one.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S152",
      "AMGT_RESAPP-Z-S156",
      "AMGT_RESAPP-Z-S157",
      "AMGT_RESAPP-Z-W26-S5"
    ],
    "dismissal_reason": "Same event as S154, which carries the mechanism and the remedy; S156 self-set GRADUATED with no remediation row is superseded; S157 verified; W26-S5 explained by the second generation writing the same key."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S294",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED: all fifteen round-13 orders were issued with NO <status> element, while every worker face tells the worker to flip it at close -- so each worker had to invent the line, and one uncommitted invented line hid a finished order from the record for twelve hours.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S153 (4.0.0_SA_CRO~Z): to-check.py listed all 15 with status ??; round-12 orders carried a tag from their adding commit (rk-9 @2726497094).",
        "rk-24 batch-unresolved-objects: the working tree carried <status>complete</status> while HEAD carried no tag; _proof_terminal refused with \"in the worktree differs from HEAD -- the checker would grade the worktree\"; committed @bee2b0a0dd after this seat census (msg 23626)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Spine L6: an order two faces in one file; the record face carries the status the gates read.",
    "world_is": "The record face shipped without the field its own worker face names. Terminality reads from proof instances regardless, so no verdict moved; what broke was every reader keyed to the tag.",
    "notes": "Remedy holder 2.0.0_SA_COO~Z: an issuance adds the <status> element in the adding commit. A gate limb on newly added orders is the cheapest mechanism.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S153"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S295",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED onto S153: the rk-24 worker found the same missing <status> element in its own order.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W33-S3: AMGT_RESAPP.TO-AMGT-rk-24.batch-unresolved-objects.md carried no literal <status> tag though section 6 said to flip it."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Section 6 of the order.",
    "world_is": "One instance of S153.",
    "notes": "Carried by S153.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W33-S3"
    ],
    "dismissal_reason": "An instance of S153, which carries the remedy."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S296",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, REMEDIATED and DISARMED: chain SP wrote scores/v1/ in two key shapes from two generations. Ruled -- the date-partitioned shape is canonical -- and the served read now resolves that shape and only that shape.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S156 adopted S155 own recommendation: scores/v1/<security_key>/<as_of_date>.json is canonical, the flat set a superseded artifact left in place.",
        "Measured at this seat 18:0xZ: 66 objects under scores/, all written 2026-09-17 14:43:27Z-16:10:08Z, ZERO before that day; 31 flat and 33 date-partitioned counting the two slash keys; a sampled date-partitioned key has one version (msg 23559).",
        "Z-S172: the served read returns scores_status SERVED, read_completed true, object_key scores/v1/BA_US_Equity/2026-09-17.json -- the date-partitioned key."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Z-S155: the adapter needs a SINGLE definitive shape before it reads anything.",
    "world_is": "One shape is ruled and read; the other set is inert data in the same prefix.",
    "notes": "The flat set is left in place by ruling. Deleting it is a separate, reversible-only act and is not owed here.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S155"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S297",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED: two disarm records -- S166 (2.0.0_SA_COO~Z, disarming S155 and W31-S1) and W33-S4 (the rk-24 worker, disarming W33-S1). Their disarms are accepted and written on the remediation clocks in this document; the dispositions each set on its OWN row are superseded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S166 carried GRADUATED and W33-S4 carried DISMISSED_WITH_REASON on the rows their own authors filed. Control: across every round, 0 investigation rows authored by 3.0.0_SA_CVO~Z carry a closed disposition -- this seat decisions live in ADJUDICATION files -- so these two were closed outside the carrier and the resolver read them closed.",
        "The disarms themselves hold: S155 by the ruled shape and the served read (C-S296); W31-S1 by its owner ruling (C-S314 records the mechanism that remains); W33-S1 by ISSUER AMENDMENT 1 with a real run writing 178 of 178 distinct objects and 0 collisions (W33-S4, drained db6c40083f)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine L9: the CVO dispositions every item.",
    "world_is": "Both rows are records of acts by the owners the hazards named.",
    "notes": "The shape is worth naming for the next round: a row that closes itself is read as closed by the resolver. That is how 5 of this round items reached the census as closed without an adjudication.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S166",
      "AMGT_RESAPP-Z-W33-S4"
    ],
    "dismissal_reason": "Disarm records; the disarms are adopted on the remediation clocks here and the self-set dispositions are superseded by this adjudication."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S298",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED: seven signer post-act verification records -- every served act of round 13 verified against BOTH halves of its never-widen pair, no rollback on any of them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S158 rk-19 adapter (19:23:42Z); S160 drafting/v1 cache rebuild (22:29:31Z); S161 rk-20 Price republish; S163 rk-23 path-safe names; S165 rk-24 adapter classed no-CIK reason; S167 rk-25 as_of_date; S172 the scores/v1/ read grant.",
        "Corroborated on this seat own instrument where the grade depends on it: BA thesis chart SERVED, source filing, points 3 with spans P0276-P0278, adapter zuWM8IZziIL4 unchanged (direct invoke 22:38:17Z); rk-23 print 200 for BP%2F_LN_Equity (105,220 B) and NG%2F_LN_Equity (106,048 B), 404 on the literal slash (msg 23610); all 16 AMGT routes present among 101 on api 7k3ed8px20 after an explicit-pagination re-read (msg 23616).",
        "S158 said \"the only gap is durability\"; the COO half had no carrier (S159) and its signer withdrew the sentence (msg 23585). S167 is graded at the CUMULATIVE grain: rk-25 own build lived about sixteen minutes and was never measured on its own."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "CLAUDE.md NEVER-1: never move served output without a never-widen CTO+COO pair covering the act blast radius and per-key rollback.",
    "world_is": "Six served acts plus one IAM act, each with both halves on file, each verified on the live plane.",
    "notes": "Two process findings ride the slug with no item id: per-act verification was met by the luck of timing (acts 15-20 minutes apart against a 30-minute signer tick), and two signed halves specified a control neither seat could execute (assuming the adapter role is refused by its trust policy; iam:SimulatePrincipalPolicy against the applied policy replaced it).",
    "adjudicates": [
      "AMGT_RESAPP-Z-S158",
      "AMGT_RESAPP-Z-S160",
      "AMGT_RESAPP-Z-S161",
      "AMGT_RESAPP-Z-S163",
      "AMGT_RESAPP-Z-S165",
      "AMGT_RESAPP-Z-S167",
      "AMGT_RESAPP-Z-S172"
    ],
    "dismissal_reason": "Verification records: each act held on its own bar against both signed halves; nothing is owed on any of them."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S299",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED and REMEDIATED: the rk-19 adapter deploy moved served output with the COO half of its never-widen pair carried only as a session dispatch; the half is now a committed file, and the rollback it names was reconstructed after the act.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S159 @8597de9671 (this seat): at filing the ledger held 11 never-widen files -- five complete pairs for rounds 10-12 and, for round 13, the CTO half alone (@e3fc4495cf).",
        "NEVER_WIDEN_ROUND13_RK19_ADAPTER_SECOND_JOIN_COO_HALF.md committed @0fdf4feb87, verified an ancestor of HEAD here; the ledger then held 12 files, six complete pairs.",
        "The file states the rollback VersionId (Ocz1IJKMxPe.KAEGqllNw7feYn9FTg.k) was NOT named in the original dispatch and was fixed afterwards by matching CodeSize against the pre-act read."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "NEVER-1: each half names the act per-key rollback, and the pair exists before the act.",
    "world_is": "Both halves now exist as files. At the moment of the act, the COO half rollback existed as a CodeSha256 but not as a named artifact version.",
    "notes": "The signer adopted the lesson as a standing check: read both halves on file before any verdict sentence (msg 23585).",
    "adjudicates": [
      "AMGT_RESAPP-Z-S159"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S300",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED: the rk-19 adapter worker refusing to deploy without a pair (W27-S5) and then deploying under one (W27-S6) -- correct conduct on both rows; their open facts are carried elsewhere.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W27-S5: no fresh CTO+COO pair existed for the act and a worker holds neither role, so the redeploy was refused.",
        "W27-S6: deployed exactly to the discriminator (0 add / 1 change / 0 destroy, 13 of 13 GET census, LOST and GAINED empty) under the pair; AC2 then failed only on the stale cache (W27-S3)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "The order requires a fresh pair naming the act own pre-act hash.",
    "world_is": "The worker stopped at the line, then acted inside it.",
    "notes": "The COO-half-as-dispatch fact is S159; the terraform-plan fact is W34-S1.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W27-S5",
      "AMGT_RESAPP-Z-W27-S6"
    ],
    "dismissal_reason": "Correct conduct recorded; the co-sign carrier gap is S159 and the plan blocker is W34-S1."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S301",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED and REMEDIATED for BA_US_Equity: the producer fix corrected the analysis object but the adapter reads a SEPARATE drafting/v1 cache written once; that cache was rebuilt under its own pair and the chart now serves three verified points.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "STOP 6 pair: CTO half @a9c6cc924c, COO half @75d97c813e; drained cfd72b4122. Exactly one key moved (12 keys under drafting/v1/, only BA_US_Equity.json after 22:00Z).",
        "Served read at this seat, direct invoke built from the adapter own route table, 22:38:17Z: thesis_driver_chart SERVED, source filing, points_count 3, held_uncited 0, 2023=528 P0278, 2024=348 P0277, 2025=600 P0276, adapter zuWM8IZziIL4 unchanged."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "rk-19 adapter AC2: BA serves three verified filing points.",
    "world_is": "Met on data alone, with no redeploy. The other 11 drafting/v1 objects still carry the pre-verification shape and their charts stay ABSENT.",
    "notes": "The population rebuild of the other 11 objects is a next-cut obligation under its own pair, not a rider on this item.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W27-S3"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S302",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED: the FWD-18 thread -- the ruling that disarmed W23-S5 (S147), the premise it rested on and its withdrawal (S148, S150, S151). Implemented and verified on the served plane; round 12 W23-S5 remediation is advanced to REMEDIATED in REMEDIATION_v12.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S147 ruled option 3 with a producer-side verification gate; S150 (this seat) showed BA three points ARE in the excerpt table; S151 withdrew S148 premise and re-keyed the gate to the excerpt period-labelled block.",
        "rk-19 producer drained 0f297b6ba6 (excerpt-based verification, AC1-AC3 PASS); the chart serves the three verified points with spans (C-S301)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "W23-S5 remediation (REMEDIATION_v12): the remedy is round-13 cell R13-A.",
    "world_is": "R13-A landed and the served chart meets FWD-18 ACCEPT for BA with values a reader can check against the filing.",
    "notes": "S148 mechanism point -- nothing tied a value to the text -- is what the landed gate now does.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S147",
      "AMGT_RESAPP-Z-S148",
      "AMGT_RESAPP-Z-S150",
      "AMGT_RESAPP-Z-S151"
    ],
    "dismissal_reason": "Ruling, correction and re-key recorded and implemented; the remedy landed and is verified (C-S301)."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S303",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED and REMEDIATED: rk-5 tab scores reached no served surface. Round 13 wired them -- the producer writes them, the adapter carries a scores key on 33 of 33 names, the page renders it, and the read completes after the grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rk-30 producer, adapter and page halves: every criterion PASS except adapter AC1 (C-S307).",
        "Z-S172: scores_status SERVED, read_completed true on the date-partitioned key, CodeSha256 0l7f4YGikexr unchanged by the grant."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Z-S149: the scores exist as a tested library only and no cell wires them.",
    "world_is": "A person opening the page now sees three scores, each classed ABSENT with its own cause. Two carry a real reason; peers_v carries an empty one (C-S304).",
    "notes": "The values are honestly absent; what they SHOULD measure rides S162.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S149"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S304",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN, DISARMED: Peers V serves ABSENT on 33 of 33. The first reading (vocabulary mismatch, S162) was ruled, then corrected: with vendor egress authorized the measure computes for 30 of 34 names as written, and the binding constraint is PEER IDENTITY -- 224 of 1,658 landed peer rows carry a numeric SEDOL stem the resolver skips.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S164 (1.0.0_SA_CTO~Z) ruled round 13 ships the honest-ABSENT state; S174 withdrew its operative reading after 4.0.0_SA_CRO~Z egress brief @e12ed54a9f measured 30 of 34 with the measure as written.",
        "Andrew-direct ~12:5xZ, recorded @c6c49ede58: \"we will always be able to find peers, I will answer that once ive better seen the shape of the data.\" The measure definition is his, reserved by name.",
        "Served read at this seat after the grant: robustness absent_reason \"n=1 of 6 measured (constraints [2, 5]), below the n>=5 eligibility floor\"; divergence absent_reason \"FWD-20 house FCF forecast has not been built yet\"; peers_v absent_reason None."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-17 and FWD-20: three scores on the Model tab, each measured or classed ABSENT with its reason.",
    "world_is": "Three scores classed absent, with three different causes. The peers_v reason field is EMPTY where its two siblings from the same producer carry one.",
    "notes": "The empty peers_v absent_reason is NOT reserved and needs no new data; it is the one part that could close at the next cut regardless of Andrew answer.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S162"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S305",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED onto S162: the Peers V ruling (S164) and its withdrawal (S174).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S174: S164 landed-plane measurement stands (the three estimate fields are on no landed object); its conclusion that Peers V is unreachable without a redefinition is withdrawn."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "The ruling thread for S162.",
    "world_is": "Both rows are carried by S162 remediation text.",
    "notes": "S174 own lesson rides the slug: a subtraction is only as good as the domain it subtracts over, and choosing the domain is itself a claim -- S164 subtracted over the field domain and never read the key space.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S164",
      "AMGT_RESAPP-Z-S174"
    ],
    "dismissal_reason": "The ruling and its correction are carried by S162."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S306",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, REMEDIATED and DISARMED: the adapter role had no grant on scores/v1/ on either limb, so every scores read failed with AccessDenied. The grant was added under its own pair and verified per limb.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S168: 33 of 33 read scores_status READ_FAILED with the full AccessDenied text -- the half disclosure clause is what made it visible.",
        "Z-S172: thirteen entries in each limb, the added values exactly arn:aws:s3:::opal-data-harvest/scores/v1/* and scores/v1/*, the other twelve byte-identical with an empty lost set; iam:SimulatePrincipalPolicy allows the two added reads, denies four negative reads and denies PutObject and DeleteObject on scores/v1/. Pair CTO @a9fb5caa70, COO @8db1cd0a76; drained cefd5e6ae5."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "HALF 5 covers no IAM change; the grant is its own act.",
    "world_is": "The read completes. The act that exposed the gap shipped without widening the grant, which is the stop working.",
    "notes": "W27-S11 second finding -- AC1 own invocation checks .get(\"status\") where classify.py writes .get(\"state\") -- is a criterion defect and rides S121 (C-S310).",
    "adjudicates": [
      "AMGT_RESAPP-Z-S168",
      "AMGT_RESAPP-Z-W27-S11"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S307",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED: the ruling on rk-30 adapter AC1 is adopted as the grade -- the ACT is complete and verified; AC1 is UNMET, because it asks for measured values the round never committed to produce; the unmet portion graduates to S162.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AC1 <expect>, read verbatim at HEAD: \"measured_robustness and measured_peers_v are both nonzero over the printed keyed_count denominator\".",
        "Served at this seat after the grant: robustness and divergence carry absent_reasons, not values; nothing is measured.",
        "This seat first classed this FAIL as STALE and prescribed a re-run (msg 23648); withdrawn before any re-run happened (msg 23652). It is a criterion defect."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "HALF 5 success branch: a completed read returning honest ABSENTs is the act succeeding.",
    "world_is": "The criterion and the co-signed success branch disagree about what success is; the half is the later position.",
    "notes": "Not moved by S174: 30 of 34 names computing once egress is authorized is a capability found after this round committed, and it does not read back onto a round-13 verdict. AC1 is not flipped.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S173"
    ],
    "dismissal_reason": "Ruling adopted as the grade: act complete, AC1 unmet, unmet portion carried by S162."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S308",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN, ARMED: the open-order census counts an order TERMINAL on a VALID proof instance whatever its criteria say, and the L10 precondition is read off that census. VALID names well-formedness, not passing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S169 (1.0.0_SA_CTO~Z): rk-30 page half recorded AC2 FAIL, proof-of-spec-check returned VALID rc=0, and the census removed it from the open set.",
        "Z-S170 @f8af42864c (this seat): at 02:3xZ SEVEN of seven orders in the terminal-by-instance bucket carried a FAIL (9 PASS, 7 FAIL of 16 criteria).",
        "ROUND 13 AT CLOSE, every one of its 15 orders read per criterion in THREE classes: 26 PASS, 3 FAIL, 0 UNVERIFIABLE-BY-INSTRUMENT; rk-26 withdrawn with no instance. Census 0 open of 97."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Spine L10: every order terminal, each with a valid proof-of-spec instance.",
    "world_is": "The three FAILs are all CRITERION defects, classed on evidence: rk-23 AC1 sends a raw slash where the page sends %2F (33 of 33 on the page shape, msg 23610); rk-20 AC1 names a BEFORE/AFTER shape the world never had (W27-S9); rk-30 adapter AC1 asks for measured values the round never committed to produce (C-S307). None is flipped.",
    "notes": "This round close was read on BOTH instruments -- the resolver for terminality and a per-criterion sweep over EVERY order for acceptance -- and the slug carries the table, not a bare count. The gate still reads only the first.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S169"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S309",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED onto S169: this seat two sweeps (S170, S171), and the correction the second makes to the first.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S171 @8aecea24d3: a sweep scoped to the census bucket empties itself -- the bucket went 7, 5, 3 as status words were committed -- and a PASS/FAIL frame misses the third class, UNVERIFIABLE-BY-INSTRUMENT, 58 of 450 criterion rows project-wide, which is how an instance declines to self-grade a judgment criterion."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "This seat own precondition.",
    "world_is": "Adopted as the close read recorded in C-S308.",
    "notes": "Carried by S169.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S170",
      "AMGT_RESAPP-Z-S171"
    ],
    "dismissal_reason": "This seat measurements for S169; the precondition they define is applied in C-S308."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S310",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED onto S121 (round 12, the criteria class, still OPEN): four more criteria that could not produce the evidence they claim, each caught by the worker running it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W27-S4: AC1 and AC2 invocations omitted the edge-injected x-firm-id header and 401 at the auth gate; the payloads were rebuilt by issuer amendment @53b8ab5874.",
        "W27-S9: rk-20 AC1 expect names BEFORE dated true and AFTER dated false; the measured state matches at neither end -- this is rk-20 AC1 FAIL, graded as a criterion defect.",
        "W33-S2: AC3 literal invocation could not complete inside its own 120 s bound; ISSUER AMENDMENT 1 added --skip-fetch, and the loop then completed once it reused one S3 client (W33-S5).",
        "W32-S1: the import path both halves and the dispatch named fails under a bare python script.py because the worktree root is not on sys.path; worked around with PYTHONPATH."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "S121 remedy: every criterion is run against the live world at the cut.",
    "world_is": "Round 13 adds instances to the same class. Two more are graduated on their own because they carry a device hazard (W31-S2) and a key-shape defect (W27-S11 second half, via C-S306).",
    "notes": "S121 stays OPEN in REMEDIATION_v12.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W27-S4",
      "AMGT_RESAPP-Z-W27-S9",
      "AMGT_RESAPP-Z-W33-S2",
      "AMGT_RESAPP-Z-W32-S1"
    ],
    "dismissal_reason": "Instances of the S121 criteria class, which carries the remedy."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S311",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "DISMISSED: three workers who caught a defect in their own order text and implemented the safe reading -- the behaviour the criteria class exists to produce.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W27-S7: the literal rk-23 fix would have sanitised the shared filename variable that also builds the S3 key; the worker scoped it to the local branch and verified both paths.",
        "W27-S8: rk-20 \"replacing build_movement_rows()\" would have broken a registry and test that name it by string; the worker preserved the function and changed only the caller.",
        "W33-S5: the unresolved-write loop built a fresh S3 client in each of 178 calls; reusing one client made it complete inside the bound, within the file the order grants."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each order text.",
    "world_is": "Each worker read past the literal instruction to its intent and recorded why.",
    "notes": "W33-S5 carried a self-set DISMISSED_WITH_REASON; this adjudication reaches the same result.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W27-S7",
      "AMGT_RESAPP-Z-W27-S8",
      "AMGT_RESAPP-Z-W33-S5"
    ],
    "dismissal_reason": "Defects in order text caught and handled safely inside the grant; nothing owed."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S312",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN, ARMED -- dispositioned WITHOUT its discriminating instrument: whether the gateway forwards %2F encoded (the page works) or normalises it to a literal slash (two names 404 at the router) is still unmeasured, and every instrument that could see it is closed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Direct invoke: encoded 200 for both names, literal 404 -- it builds rawPath itself, so it certifies its own assumption.",
        "Direct HTTPS to the gateway: 401 on all four calls, the no-slash positive control and the no-header negative control included -- never reached the adapter (msg 23610).",
        "Authorizer logs: zero events 00:00Z-00:30Z against 51 in a control window, IdentitySource Authorization, and it logs \"path: undefined\" when it does run (msg 23616). Adapter logs: zero path events in 36 hours with a live positive control. Gateway access logging is not configured.",
        "The one surviving instrument, a browser-network capture through the real edge (rk-26), was withdrawn by its issuer on Andrew word @5dc9089ca7 after MFA blocked the automation login (W31-S3)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "rk-23: both slash-bearing names print.",
    "world_is": "They print at the adapter on the shape the page builds. Whether they reach the adapter in that shape is not known.",
    "notes": "This is not graded on a direct invoke. The remedy below removes the question rather than answering it.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W27-S10"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S313",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN: the same slash in two producers -- the posture store writes the two names one level deeper than every other name, and the management batch census splits security keys on \"/\" so those two names can never be built.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W32-S3: posture/v1/BP/_LN_Equity/... instead of posture/v1/BP_LN_Equity/...; a consumer splitting on the first \"/\" reads BP and NG and undercounts by two.",
        "1.0.0_SA_CTO~Z @0cdd86b29d, verified at source: batch.py:81-84 splits on \"/\", and the same census counts placeholder filings as real, so one enable would write about 176 zero-officer rosters served as SERVED."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "rk-23 (FWD-5) scope: path-safety for security keys.",
    "world_is": "rk-23 fixed the renderer and the drafting read; the producers still split and nest on the slash.",
    "notes": "One owner, one pass over every site that splits a security key on \"/\".",
    "adjudicates": [
      "AMGT_RESAPP-Z-W32-S3"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S314",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN, DISARMED: a linked worktree carries an EMPTY portal/ gitlink -- no .gitmodules URL and no supported mechanism populates it -- so no portal-touching worker can run in its own worktree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W31-S1: 0 files under portal/ in the assigned worktree; the worker stopped rather than reconstruct the tree.",
        "Disarmed by its owner (S166): the page halves were completed and re-run against the main tree portal (5b767811e7, 9074091db1)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Spine L7: one worktree per worker.",
    "world_is": "This round instances were worked around by running in the main tree; the mechanism is unchanged and the next portal cell meets it again.",
    "notes": "Disarm accepted on its owner ruling; the mechanism graduates.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W31-S1"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S315",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN, ARMED: on this device `npx tsc -b` in the bun-managed portal fetches and runs a registry package named tsc that compiles nothing and exits clean, so any criterion written that way cannot see a type error.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W31-S2: the literal invocation printed the decoy banner, rc 0; ./node_modules/.bin/tsc.exe -b ran the real compiler, rc 0, no output.",
        "The remedy is already banked estate memory (msg 23636): bun install writes no npm shims, so invoke the local binary by path. Both round-13 criteria were re-cut that way (5b767811e7, 9074091db1) and now PASS."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "rk-19 page and rk-30 page AC2: no new compile errors.",
    "world_is": "Two criteria fixed; the device behaviour and the authoring convention that produced them are unchanged.",
    "notes": "Owner as filed: 0.4.0_DT_ClientPlatform.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W31-S2"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S316",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN, ARMED: mandatory MFA, which Andrew required for all users on 2026-09-02, now gates the documented automation logins, so no headless capture can authenticate. rk-26 was withdrawn on his word, and with it round 13 only judgment criteria and W27-S10 only oracle.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W31-S3: the D12_PHONE_OTP_ALL_AWS challenge intercepts both documented logins before any token is issued; the worker did NOT read the MFA store or any signing secret to recover a code.",
        "rk-26 withdrawn @5dc9089ca7 (Andrew-direct \"write off the frontend TO\"); census 0 open of 97.",
        "Judgment grades: rk-26 AC2 and AC3 are NOT graded -- the order has no proof instance, and the grade carrier requires one. Round 12 rk-2 AC6 and rk-8 AC4 stay NOT_EVALUATED as graded in ADJUDICATION_v12, with the missing instrument now named: an authenticated browser-network capture through the real edge."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "rk-26: a captured render of the DEV-built page against the deployed adapter, browser network layer recorded.",
    "world_is": "Not producible by any fabric act under the MFA decision as it stands.",
    "notes": "Credentials: plaintext logins sit in an untracked folder of the rk-26 worktree and in a tracked portal credentials file; 1.0.0_SA_CTO~Z carried both to Andrew (msg 23700). They are not quoted in any record of this seat. The drain-time half is 2.0.0_SA_COO~Z.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W31-S3"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S317",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN: the vendor call Andrew authorized at CARD 5 enriched NONE of the seven names rk-22 added, because domains.json lists only the original five QA names -- and the management figure \"12 of 12\" is a STATUS count: 7 of the 12 rosters carry officers.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W32-S2: every added name lusha_enrichment.status SKIPPED; ceo_public_profile never queried.",
        "rk-22 criteria read at HEAD: AC1 expects the counts to rise toward the ceiling with every non-measured name carrying a reason; AC2 a two-value classification. Neither tests enrichment, and the order never names the vendor service or domains.json -- so AC1 and AC2 PASS stand on their text (working record @c8c3ec7f37).",
        "Exec Management first read, 4.0.0_SA_CRO~Z msg 23697 re-measured by 1.0.0_SA_CTO~Z @0cdd86b29d: 12 rosters SERVED by status, 7 with officers (62), 5 with zero officers under UNRESOLVED-SOURCE -- 7 of 33 keyed names carry officers."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "CARD 5: authorize the management and posture producers vendor calls.",
    "world_is": "The authorization produced no enrichment for the names it was for, and SERVED is reported over five empty rosters.",
    "notes": "Not a criterion FAIL: grading it as one would grade rk-22 against text it never carried. The SERVED-over-empty status is an adapter value-carries-its-claim defect.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W32-S2"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S318",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN: a shared library cache defaults into a NUMBERED WORKER deliverables folder, so running the posture producer rewrites a tracked file in another worker record.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W32-S4: lib/research/peers/universe.py load_candidate_universe() rebuilt deliverables/0.9.0_WK_AMGT_RESAPP~21/candidate_universe.json; the worker left the diff uncommitted rather than write outside its grant.",
        "Read here: that path is clean against HEAD in the shared tree -- the diff stayed in the worker worktree and did not come across at the drain."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A worker deliverables folder belongs to that worker.",
    "world_is": "Any seat that runs the posture producer in the shared tree leaves an uncommitted diff on a tracked file, the class that produced four failures on this project in one evening.",
    "notes": "A worker slot is not a durable cache home.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W32-S4"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S319",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, REMEDIATED and DISARMED: 59 of 237 unresolved names carry security_key null, and the new writer would have collapsed them onto one colliding key. The issuer ruled skip-and-count; a real run wrote 178 of 178 distinct objects with 0 collisions.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W33-S1: filings/v1/None/UNRESOLVED-SOURCE.source.json would have been written 59 times.",
        "ISSUER AMENDMENT 1 @837e7b1007 skips a falsy security_key and counts it; drained db6c40083f; rk-24 producer AC1-AC3 PASS (237 = 59 + 178; 178 of 178 found, objects_missing empty)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "rk-24: one UNRESOLVED-SOURCE object per unresolved name.",
    "world_is": "Every name with a key has its own object; the 59 without one are counted, not written.",
    "notes": "The 59 are an identity gap and ride S117 (round 12, OPEN).",
    "adjudicates": [
      "AMGT_RESAPP-Z-W33-S1"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S320",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN, ARMED: no Terraform plan can run in a fresh worktree of infra/aws/terraform/harvest, targeted or not, because an unrelated resource reads a gitignored, never-committed build artifact at plan time.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W34-S1: chatter-axis-schedule.tf:124 filebase64sha256() reads .build/chatter-axis-producer.zip; -target does not prune the evaluation; the worker used a disposable, never-committed placeholder."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A targeted plan changes exactly one resource.",
    "world_is": "Every act in that root depends on an artifact no worktree has.",
    "notes": "Also met by the rk-19 adapter worker (W27-S6).",
    "adjudicates": [
      "AMGT_RESAPP-Z-W34-S1"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S321",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-18T17:45Z",
    "one_line": "GRADUATED, OPEN, ARMED: a co-signed direct act on an infra path cannot satisfy the owned-paths lane gate, which reads grants only from task-order files -- so every such act needs the audited author override.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W34-S2: owned-paths-validate refused the worker commit of scoped-amgt-api.tf, the one file the act existed to change.",
        "The Terraform source landed under GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL @3c2a6e47ca; 1.0.0_SA_CTO~Z endorsed the escape as correct for this case (msg 23649)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "CLAUDE.md 14a: the override is audited and singular.",
    "world_is": "The escape was the right tool here; it will be needed for every co-signed direct act until the gate knows about pairs.",
    "notes": "A structural gap, not a defect in this act.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W34-S2"
    ]
  }
]
```

-- 3.0.0_SA_CVO
