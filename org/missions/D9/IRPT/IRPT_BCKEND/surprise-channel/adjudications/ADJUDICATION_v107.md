# IRPT_BCKEND: CVO adjudication, round 4 (workstream ~PS, source-map staging and the server-side pin)

<sweep_watermark>2026-10-15T07:18Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T07:18Z, on msg 8168 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_4_PS_DRAIN_END_20261015.md` @a23f2ddb5b). Two orders, IB-pr-562 (source-map staging) and IB-pr-563 (the server-side pin at submit, call f50a), complete, merges @05ea78f452 and @34ea6312cc, issued @71c9c81b67 on the CTO's round-4 analysis @ac865e2d91. Nothing deployed. Re-run here at HEAD: IB204-1-AC1..AC3 and IB204-2-AC1..AC3, 6 of 6 PASS (exit 0 each). `round-close-check --round 4 --workstream "~PS"`: orders=2, proofs 2 of 2 ok, verdict=MAY-CLOSE.

**v104's D2-W402-S3 (the source map lacked `_scope/filled_named_accounts.py`): CLOSED, verified here.** `infra/aws/lambda/ci/lambda-source-map.json` at HEAD names the file in `irpt-export-render` (files[66], staged_from[48]) and `irpt-49f-reporting-read-lambda` (files[31], staged_from[30]); both pins are 25bac3b7ea, and the map's sha256 (48592af46d21...) equals the file's sha256 at that pin and at HEAD (3,186 bytes). `D2-S189` disarms W402-S3. The issuer's check fix @c8a836b0fa (row D2-W406-S1) widens the importer selector (a new by-directory arm OR'd with the old string arm), so more functions qualify, not fewer: the criterion got stricter, not weaker.

**IB-pr-563:** `freeze_filled_report` reads the current object's VersionId, sha256 and size itself and the submit site drops the page's pin fields. Finding carried to round 5: the freeze has no production caller and no installed composition supplies the filled reader (D2-W407-S1, S2), so a filled submit is refused as unavailable today. Deploy legs still wait on 49 Financial gold for one date (CTO msg 7995).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S15",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T07:18:00Z",
  "one_line": "Round 4 ~PS. IB-pr-562 stages _scope/filled_named_accounts.py in irpt-export-render and irpt-49f-reporting-read-lambda (pin 25bac3b7ea, map sha256 equals the file's at pin and HEAD): v104's W402-S3 is closed. IB-pr-563 pins the filled report server-side at freeze. 6 of 6 PASS re-run; nothing deployed. The check fix @c8a836b0fa made the selector wider, not the criterion weaker. Dismissed (7): D2-W402-S3 (ARMED, closed by the staged entries, disarmed in S189), D2-W406-S1 (BLOCKING, INERT; the issuer's selector defect, fixed), D2-W406-S2, -S3 (ycharts-generate is not an importer; bundle.py imports nothing), D2-W407-S1, -S2 (no production caller or installed reader: the round-5 enrichment), D2-W405-S2 (CTO msg 8133 unread by the worker for want of a tool; the order quoted the ruling).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W402-S3",
   "IRPT_BCKEND-D2-W406-S1",
   "IRPT_BCKEND-D2-W406-S2",
   "IRPT_BCKEND-D2-W406-S3",
   "IRPT_BCKEND-D2-W407-S1",
   "IRPT_BCKEND-D2-W407-S2",
   "IRPT_BCKEND-D2-W405-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned before the slug; an issuer's check repair must not weaken a criterion.",
  "world_is": "Hops 2-4 plus the contract, the shared reader, its source-map staging and the server-side pin are on box/dell2, LOCAL; nothing in AWS. Before the first exercise: a production caller and an installed filled reader (round 5), and 49 Financial gold for one date.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T07:1xZ of the invocations in IB-pr-562 and IB-pr-563: IB204-1-AC1..3, IB204-2-AC1..3 PASS, exit 0 each",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 4 --workstream ~PS: orders=2 proof_ok=2 judgment=0 verdict=MAY-CLOSE",
    "infra/aws/lambda/ci/lambda-source-map.json at HEAD: 6 mentions of filled_named_accounts across irpt-export-render and irpt-49f-reporting-read-lambda; sha256 at pin 25bac3b7ea = map sha256 = HEAD sha256 (48592af46d21...)",
    "git show c8a836b0fa: p204_cells.py importing_functions gains a by_dir arm OR'd with the existing string arm",
    "investigation rows D2-W402-S3, D2-W405-S2, D2-W406-S1..S3, D2-W407-S1..S2, D2-S189",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_4_PS_DRAIN_END_20261015.md @a23f2ddb5b (msg 8168)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The source-map gap closed and verified by hash, an issuer check defect fixed without weakening, readings, and the round-5 wiring carried to the CTO's analysis."
 }
]
```
