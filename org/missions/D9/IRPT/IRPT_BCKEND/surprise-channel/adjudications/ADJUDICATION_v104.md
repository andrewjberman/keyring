# IRPT_BCKEND: CVO adjudication, round 3 (workstream ~PS, the export contract and the export scope rule)

<sweep_watermark>2026-10-15T06:02Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T06:02Z, on msg 8123 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_3_PS_DRAIN_END_20261015.md` @e9fec793a0). Two orders, IB-pr-557 (the ExportBundle contract) and IB-pr-558 (one named-account reader for the route and the export freeze), complete, merges 85594eeabe and 2b0d56c675, issued @b611ec2746 on the CTO's round-3 analysis @a4718eab10. No judgment criterion. Re-run here at HEAD: IB201-1-AC1..AC3 and IB201-2-AC1..AC3, 6 of 6 PASS (exit 0 each). `round-close-check --round 3 --workstream "~PS"`: orders=2, proofs 2 of 2 ok, verdict=MAY-CLOSE.

**Nothing deployed, confirmed here, not taken from the packet.** The two merges change only repository files (the two ExportBundle schema copies, byte-equal per `cmp`, a contract test, the new `_scope/filled_named_accounts.py`, `retained_export.py`, `entry.py`, a freeze test). No change-management entry names them (today's only IRPT entry, `20261015T0559Z_irpt-api-r31a-20261015`, is IRPT_ANLREQ's commentary-pdf route, 0 mentions of these files). Live read of API 7k3ed8px20 (`apigatewayv2 get-routes`, 121 routes, CLI-aggregated): the only `reporting/client` route is `.../{client_id}/summary`; no `/report` route exists.

7 rows dismissed below. HELD, owned, and the one that gates any deploy leg: D2-W402-S3 (ARMED, owner `~P2`): `infra/aws/lambda/ci/lambda-source-map.json` has 0 entries for `filled_named_accounts` (read here), so a route or export package built today would omit the shared reader and fail on import. Also carried: the CTO's server-side pin at submit (msg 8104, call f50a), D2-W403-S3, D2-W392-S2, D2-W394-S2, D2-S184, W349-S1, W361-S1, W348-S2, W368-S2 (owner `~P2`), D2-S158 (owner the CTO).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S12",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T06:02:00Z",
  "one_line": "Round 3 ~PS. IB-pr-557: the ExportBundle schema (docs and packaged copies byte-equal) gains filled_report_source and one additive top-level oneOf branch for a frozen filled bundle, revision 1.1 to 1.2, both arms tested. IB-pr-558: the route and the export freeze call ONE named-account reader, _scope/filled_named_accounts.py; the freeze refuses a document naming an account outside scope. This closes v102's two round-3 carries (W399-S1 contract, W399-S2 scope sets). 6 of 6 PASS re-run; nothing deployed (repo-only diffs, no ledger entry, no /report route live). Dismissed (7): D2-W401-S1 (BLOCKING, INERT; the missing top-level oneOf, repaired by IB-pr-557 AMENDMENT 1 @30b92358a8), D2-W401-S2 (4 pre-existing test_seam_paired.py failures, identical on base bytes; not caused here), D2-W401-S3 (branch 1 admits a filled pin beside narrative_packet_ref, freeze refuses it; recorded looseness on frozen branches), D2-W402-S1 (the order's sys.path premise wrong; worker added _scope inside the marked block), D2-W402-S2 (commit-order note), and from v102 D2-W399-S1, -S2 (now answered by these two orders). Held: D2-W402-S3, the source-map gap.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W401-S1",
   "IRPT_BCKEND-D2-W401-S2",
   "IRPT_BCKEND-D2-W401-S3",
   "IRPT_BCKEND-D2-W402-S1",
   "IRPT_BCKEND-D2-W402-S2",
   "IRPT_BCKEND-D2-W399-S1",
   "IRPT_BCKEND-D2-W399-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned before the slug; an issuer amendment states its gate limb; nothing serves before both never-widen halves and the deploy ledger hold.",
  "world_is": "Hops 2-4 code plus the contract and the shared scope reader are on box/dell2, LOCAL, tested with stubs; nothing in AWS (the live API has the summary route only). Before any deploy leg: the source-map entry for _scope/filled_named_accounts.py (D2-W402-S3), the server-side pin at submit (msg 8104, call f50a), and 49 Financial gold for one date (CTO msg 7995). Four test_seam_paired.py failures exist at base and are unowned by this round.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T06:0xZ of the invocations in IB-pr-557 and IB-pr-558: IB201-1-AC1..3, IB201-2-AC1..3 PASS, exit 0 each",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 3 --workstream ~PS: orders=2 proof_ok=2 judgment=0 verdict=MAY-CLOSE",
    "git diff --name-only 85594eeabe^1 85594eeabe and 2b0d56c675^1 2b0d56c675: repository files only; cmp of the two ExportBundle.schema.json copies: byte-equal",
    "aws apigatewayv2 get-routes --api-id 7k3ed8px20 2026-10-15T06:0xZ: 121 routes; reporting/client routes: the summary route only",
    "grep -c filled_named_accounts infra/aws/lambda/ci/lambda-source-map.json = 0",
    "investigation rows D2-W401-S1..S3, D2-W402-S1..S3, D2-W399-S1..S2, D2-S186",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_3_PS_DRAIN_END_20261015.md @e9fec793a0 (msg 8123)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An issuer defect repaired by an amendment, pre-existing test failures, recorded schema looseness on frozen branches, order-premise and commit-order notes, and two v102 carries now answered. The source-map gap is held with its owner before any deploy."
 }
]
```
