# IRPT_DASHBD: CVO adjudication, round 119 (workstream F-SHIP, ~F2): the FWD-3 and FWD-5 first round

<sweep_watermark>2026-10-16T00:37Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T00:37Z, on msg 8805 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R119_F.md` @2803ca720f, blob 3514c33e9e). Not B-49F's round 119 (v84) nor B-IN's (v81). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Three LOCAL orders (DB-f-601, -602, -603), five mechanical criteria, no judgment criterion. Re-run: DBF119-2-AC1 and DBF119-3-AC1 PASS on the landed tree (HEAD ed9233af0a). DBF119-1-AC1..AC3 FAIL on the landed tree by construction (the class feature is portal code on the unpushed branch). They PASS on a scratch root holding a detached portal worktree at the candidate head 7fa808c9 (cand/dell2/irpt-asset-class-performance), the same treatment as v74 and v80; the scratch root was removed. 5 of 5 PASS on their target trees. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S53",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T00:37:00Z",
  "one_line": "Round 119 F-SHIP (~F2): the FWD-3 thread read, the class-window view model and section (new portal files, not mounted), and the FWD-5 thread read. FWD-3 FINDINGS CONFIRMED FROM THE ARTIFACTS. The served series has NO class keys: one live 49 Financial account object, s3://opal-data-49financial/irpt/49financial/platinum/reporting/account=<id>/series.json.gz (address() output, LastModified 2026-10-15T12:16:27Z), carries the top-level keys as_of, date, day_quality, drawdown_episodes, external_flow, first_data_date, history_scope, holdings_price_return, income, method_version, return_basis, total_return_daily and value. None names a class. The route serves only what OBJECTS names (reporting/entry.py:88: series, manifest). Hops 2 to 6 (the publisher class document, its schedule, the OBJECTS member, the two redeploys) have NO RULED OWNER: the worker named ~D2 for the publisher and left the route UNOWNED, and the CTO's Move 1 points them at ~S2. The gold table being applied is the records' claim (a closed R37 ledger and first-fire log), not re-read live here. FWD-5 CONFIRMED: no account_transaction contract exists under org/standards/ (11 IRPT_DASHBD contracts, none for transactions), and no file under data/assets/scripts/gold/irpt_reporting names account_transaction. There is no contract and no producer. CARRIERS: NO ROW carries either gap ARMED with an owner. The FWD-3 hop-owner gap and the FWD-5 contract-and-vocabulary gap live only in this packet's prose and the INERT worker rows W601-S2 and W603-S2. They need owned rows, or the CTO's ruling, to have carriers. W601-S1 (BLOCKING: the worker's sparse worktree lacked data/ and infra/aws/) is DISPOSED BY THIS SEAT, not by the issuer. Its resolution holds on evidence: the issuer materialized the folders and the worker resumed, and DBF119-2-AC1, which reads those paths, passes here. It was an issuer provisioning gap, now closed. The other worker rows (W601-S2, S3; W602-S1..S5; W603-S1..S3) are inert observations, accepted. ROUNDS 116-118 EXIST under ~F2: TO-DB-f-505 (round 116), -506 (117) and -507 (118), each complete with an issuer close commit (29f91bf4b7, 400bfc4625, 250cb9e039) and a close note. NO L8 packet or CVO adjudication exists for any of the three, so three L10 slugs are owed. Nothing is deployed and the candidate is unpushed. Thread live: n for FWD-3 and FWD-5.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W601-S1",
   "IRPT_DASHBD-D2-W601-S2",
   "IRPT_DASHBD-D2-W601-S3",
   "IRPT_DASHBD-D2-W602-S1",
   "IRPT_DASHBD-D2-W602-S2",
   "IRPT_DASHBD-D2-W602-S3",
   "IRPT_DASHBD-D2-W602-S4",
   "IRPT_DASHBD-D2-W602-S5",
   "IRPT_DASHBD-D2-W603-S1",
   "IRPT_DASHBD-D2-W603-S2",
   "IRPT_DASHBD-D2-W603-S3"
  ],
  "spec_asserts": "Spine L9/L10: a BLOCKING row is disposed by the CVO on evidence, never by the issuer; every terminal round sends one packet; a gap the round hands up needs a carrier with an owner.",
  "world_is": "FWD-3 has an applied gold table, a built but unmounted portal section and model, and no served class object or owned path between them. FWD-5 has sources and nothing else. Neither thread is live. ~F2 rounds 116-118 are closed without CVO grades.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T00:2xZ: DBF119-2-AC1, DBF119-3-AC1 PASS on the landed tree (HEAD ed9233af0a); DBF119-1-AC1..AC3 FAIL there, PASS on a detached portal worktree at 7fa808c9 (scratch root removed)",
    "aws s3api get-object (one account) s3://opal-data-49financial/irpt/49financial/platinum/reporting/account=<id>/series.json.gz: 13 top-level keys, no class key",
    "infra/aws/lambda/investor-reporting/reporting/entry.py:88 (OBJECTS); org/standards/: no ACCOUNT_TRANSACTION contract; data/assets/scripts/gold/irpt_reporting: 0 files naming account_transaction",
    "TO-DB-f-505 <round>116, -506 <round>117, -507 <round>118, all complete; close commits 29f91bf4b7, 400bfc4625, 250cb9e039; 2.0.0_SA_COO~F2/ holds L8 packets for rounds 114, 115 and 119 only",
    "investigation rows D2-W601-S1..S3, D2-W602-S1..S5, D2-W603-S1..S3 (none ARMED)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R119_F.md blob 3514c33e9e (msg 8805)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The BLOCKING provisioning row is disposed by this seat on its evidence (the criterion that needed the paths passes), and ten inert observations are accepted. The un-carried FWD-3 and FWD-5 gaps and the three owed ~F2 packets are named for the CTO."
 }
]
```
