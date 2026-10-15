# IRPT_BCKEND: CVO adjudication, round 3 (workstream ~PJ, the overlay candidates of the holdings bundles)

<sweep_watermark>2026-10-15T17:54Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T17:54Z, on msg 8509 (the shared packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL1_PJ2_PJ3_PN1_DRAIN_END_20261015.md` @9ac52f5198; this file grades ~PJ r3). One order, IB-pr-590 (risk SERVED, build-only, read-only on AWS), complete, merged @53d1153a4b. Re-run here at HEAD: IB224-1-AC1..AC3 PASS (exit 0). `round-close-check --round 3 --workstream "~PJ"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE.

**The overlay is ALSO not the exemption alone. Verified here in the bytes.** IB-pr-590 overlaid exactly two files, `holdings_snapshot.py` and `publication.py`, from overlay pin fa2502c5b1 onto each firm's minting pin. That gives 44 of 46 members equal to live and 104 tests passing per firm. But the overlaid `holdings_snapshot.py` is HEAD's whole file. Counted here:

| file version | `allow_older_date` | `ONE-DATE BYPASS` | lines naming cusip | ABSENT-AT-SOURCE block markers |
|---|---|---|---|---|
| 49F minting pin b1d354cfc9 | 0 | 0 | 12 | 0 |
| COT/INF minting pin 5fad7eaaa8 | 0 | 0 | 2 | 0 |
| overlay pin fa2502c5b1 | 10 | 1 | 2 | 10 |
| HEAD | 10 | 1 | 2 | 10 |

So deploying the overlay would ship, beyond the exemption:
- **(a)** the UNRELEASED one-date bypass (IB-pr-536, commit 15e0361375, a manual-path flag whose sign-off is not part of this pair) to all three firms;
- **(b)** a REVERSAL of 49 Financial's CUSIP port (12 cusip lines at its pin, 2 at the overlay).

The HEAD-built alternative (v126) would in addition move the **six drifted members**: `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`, `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py`, `data/mdpf/scripts/gold/mdpf_category_registry.py`, `infra/logic/registry/exemptions.json`, `infra/logic/registry/reporting_policies.json`, `lib/opal_naming.py`.

All of that is wider than the CTO's PJ/PK analysis (msg 8436) scoped, which was the exemption and its receipts and split repairs.

**Plainly: the never-widen pair for IB-pr-580 / 582 / 583 MUST NOT be signed on the current blast radius.** Neither candidate built so far (HEAD-built or overlay) is "the exemption alone". A signable pair needs a bundle whose diff against each firm's LIVE bundle is only the exemption's blocks (plus the receipts and split repairs it names), at each firm's own pin, with the bypass absent and 49F's CUSIP lines intact. IB-pr-595 (the transplant of only the exemption commits) is the cut for that; its candidate must be re-read the same way before anyone signs. Carrier: `D2-S206` (ARMED, owner `2.0.0_SA_COO~P2`) names the six members, the bypass and the CUSIP reversal. It is held, not dismissed.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S35",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T17:54:00Z",
  "one_line": "~PJ r3. The overlay candidate (two files from fa2502c5b1 onto each minting pin) is not the exemption alone, measured here: its holdings_snapshot.py carries the unreleased IB-pr-536 one-date bypass (allow_older_date 10, absent at both minting pins) to all three firms and reverses 49F's CUSIP port (12 cusip lines at b1d354cfc9, 2 at the overlay); the HEAD build adds six drifted members (three MDPF dims modules, registry exemptions.json and reporting_policies.json, lib/opal_naming.py). The never-widen pair for IB-pr-580/582/583 MUST NOT be signed on this blast radius; IB-pr-595's transplant must be re-read member by member against each firm's live bundle first. Held on D2-S206 (ARMED, ~P2). IB224-1-AC1..AC3 PASS; build-only. Dismissed (1): D2-W431-S2 (scratch location). Held also: D2-W431-S1 (RECORD FACE reached the worker).",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~P2",
  "adjudicates": [
   "IRPT_BCKEND-D2-W431-S2"
  ],
  "spec_asserts": "Never-widen (CLAUDE.md section 5): a sign-off names the act's blast radius; the CTO's PJ/PK analysis (msg 8436) scopes the exemption, its receipts and the split repairs, nothing else; the unreleased IB-pr-536 bypass carries its own sign-off.",
  "world_is": "No holdings candidate built so far is signable for the exemption pair. Live bundles are the IB-pr-549 mint. The transplant IB-pr-595 is in flight and must show a member diff against live equal to the exemption's blocks only, with the bypass absent and 49F's CUSIP port intact.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T17:4xZ of the invocations in IB-pr-590: IB224-1-AC1..3 PASS, exit 0; round-close-check ~PJ round 3 MAY-CLOSE",
    "git show <c>:data/assets/scripts/gold/investor_reporting/holdings_snapshot.py at b1d354cfc9, 5fad7eaaa8, fa2502c5b1, HEAD: counts of allow_older_date 0/0/10/10, 'ONE-DATE BYPASS' 0/0/1/1, cusip lines 12/2/2/2, 'BEGIN ABSENT-AT-SOURCE' 0/0/10/10",
    "git log -S 'ONE-DATE BYPASS': first commit 15e0361375 (IB-pr-536)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~431/IB224-1_holdings_overlay_candidate.json: per firm 46 members, 44 equal live, 2 changed",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~428/IB222-1_holdings_bundles_candidate.json: the six drifted members",
    "investigation rows D2-S206 (ARMED, 2.0.0_SA_COO~P2), D2-W431-S1..S2",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL1_PJ2_PJ3_PN1_DRAIN_END_20261015.md @9ac52f5198 (msg 8509)"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Held, not dismissed: the widened blast radius stands until IB-pr-595's candidate is read and shown to be the exemption alone. The one dismissed worker row (W431-S2) is a scratch-location note."
 }
]
```
