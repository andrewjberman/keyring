# IRPT_BCKEND: CVO adjudication, round 2 (workstream ~PO, the Orion Inflection raw feed)

<sweep_watermark>2026-10-15T04:59Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T04:59Z, on msg 8061 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_2_PO_DRAIN_END_20261015.md` @17172025c0). One order, IB-pr-556 (the Orion pairs packet), complete, merged @7dc4dbbc6e, issued @8cdd704be7 on the CTO's msg 8014; three amendments (8110ace2ee, 846731c0d9, e75ef171d7), each stating its gate limb (GATE (viii)). No judgment criterion; nothing built, pulled, deployed, written to AWS or invoked; no Orion request. Re-run here at HEAD: IB200-4-AC1..AC3 PASS (exit 0). `round-close-check --round 2 --workstream "~PO"`: verdict=MAY-CLOSE. Verified here: `deliverables/0.9.0_WK_IRPT_BCKEND~400/ORION_PAIRS_PACKET_V1.md` hashes to sha256 c3dcc22f...19bc56b62 at HEAD, and the COO half `NEVER_WIDEN_IB_pr_556_ORION_PAIRS_COO_HALF.md` names that same hash. The CTO half is unsigned and owed.

**v101's D2-W396-S4 (source-absent transactions and performance days): MOVED, not closed.** The design's pair (a) day lists (`IB200-4_orion_pairs_design.json` `.pair_a.feeds`) carry transactions 7 days (2026-07-01, 07-13, 07-14, 07-15, 08-06, 09-28, 09-29: exactly W396-S4's list) and performance 22, beside positions 7, 36 keys in all, each read ABSENT first and recorded ABSENT-AT-SOURCE where the vendor returns nothing, never an empty key. So the gap v101 named is now inside the re-pull's scope. It is designed, not done: pair (a) is cut only after pair (b) produces a clean scheduled day, and the CAUSE of the producers writing nothing on those days is still unread (the packet says so, line 75). Small note: the positions list holds 2026-07-03 (holiday), 07-04 and 07-05 (weekend), which `lib/trading_calendar.py is_trading_day` reads False, while the packet's line 7 says "every absent trading day"; the binding key list and section 8 (a non-trading fire pulls the calendar day it owes) cover them, so the wording is loose, not the scope.

**IRPT_DASHBD v79's missing-account finding (an Inflection account holding positions every Q3 day with no Scope group over Q3 or YTD).** This round HANDLES it and does not own it: the packet's Scope addendum records such an account as ABSENT with NO_GROUP (line 7), never a zero or a fill, and lifts the one-account limit at `orion_account_mapping.py:84`; it does not read why the account has no group. A row now carries it: `IRPT_DASHBD-D2-S60` (ARMED, disarm owner `2.0.0_SA_COO~I2`, surfaced by `1.0.0_SA_CTO~DELL2` 2026-10-15T04:45:18Z, landed @72a670b1c8, after v79), cause class NOT_DETERMINED, requiring the Scope feed to carry it as ABSENT NO_GROUP. This packet's rule meets that row's requirement; the cause stays with `~I2`. A parse of all 1388 IRPT_BCKEND rows found no row naming it, which is correct: it lives in IRPT_DASHBD.

3 rows dismissed below. HELD, owned: D2-S184 (ARMED, owner `~P2`: the writer of the daily flat keys is unlocated; COO half condition 1 makes finding it the release's first read-only step, with a STOP), plus the carried D2-W394-S2, D2-W392-S2, W349-S1, W361-S1, W348-S2, W368-S2 (owner `~P2`) and D2-S158 (owner the CTO).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S11",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T04:59:00Z",
  "one_line": "Round 2 ~PO. One never-widen packet for both Orion pairs: (b) the manual raw producer ported to one 06:00 New York scheduled handler for positions, transactions and performance (manual CLI writes and three 11:15-11:32Z rules retired in the same pair; Scope account feed by addendum, fee basis NET); (a) the re-pull of 36 absent keys (positions 7, transactions 7, performance 22, about 15,300 requests) through (b)'s path. IB200-4-AC1..AC3 PASS re-run; the packet sha256 at HEAD equals the COO half's signed hash; CTO half owed. v101's D2-W396-S4 is moved into pair (a)'s scope (the transactions list is exactly W396-S4's), not closed and its cause unread. IRPT_DASHBD v79's missing-account finding is handled here (ABSENT NO_GROUP) and owned by row IRPT_DASHBD-D2-S60 (ARMED, ~I2). Dismissed (3): D2-W400-S1 (BLOCKING, INERT; flat keys with no builder output: superseded by AMENDMENT 1, an existing pipeline's read contract, rule 30 non-application), D2-W400-S2 (the live rule name grades OUT-OF-PATTERN; a reading), D2-W396-S4 (re-dispositioned: now carried by pair (a)). Held: D2-S184 (the unlocated daily writer).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W400-S1",
   "IRPT_BCKEND-D2-W400-S2",
   "IRPT_BCKEND-D2-W396-S4"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned before the slug; never-widen (CLAUDE.md section 5) holds both halves at the same bytes; an issuer amendment states its gate limb.",
  "world_is": "A COO-signed packet, nothing built or pulled. Before anything moves: the CTO half at the packet's bytes, then condition 1, finding the unlocated writer of the daily flat keys (D2-S184), since retiring the CLIs could stop the feed and deploying beside it would double it. Pair (a) waits on a clean scheduled day from (b). Source-absent days are in scope but uncaused; the missing Scope-group account is handled by rule and its cause sits with ~I2 on IRPT_DASHBD-D2-S60.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T04:5xZ of org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py: IB200-4-AC1..3 PASS, exit 0",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 2 --workstream ~PO: orders=1 judgment=0 verdict=MAY-CLOSE",
    "sha256sum org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~400/ORION_PAIRS_PACKET_V1.md = c3dcc22f02e8624eca4f402f77fe95ba28c3df331a0896e22ef94dd19bc56b62; the COO half file carries that hash (1 hit)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~400/IB200-4_orion_pairs_design.json .pair_a.feeds: positions 7, transactions 7, performance 22 days; lib/trading_calendar.py is_trading_day False for 2026-07-03, 07-04, 07-05",
    "IRPT_DASHBD INVESTIGATION_v1.md row IRPT_DASHBD-D2-S60 (ARMED, disarm owner 2.0.0_SA_COO~I2, surfaced 2026-10-15T04:45:18Z, @72a670b1c8); parse of 1388 IRPT_BCKEND rows: 0 carry it",
    "amendment commits 8110ace2ee, 846731c0d9, e75ef171d7: each states 'Gate limb: GATE (viii) placeholders'",
    "investigation rows D2-W400-S1, D2-W400-S2, D2-S184, D2-W396-S4",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_2_PO_DRAIN_END_20261015.md @17172025c0 (msg 8061)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A superseded issuer defect, a naming reading, and v101's source-absent days now carried by a designed pair. The unlocated daily writer (D2-S184) is held with its owner; the missing Scope-group account has its own owned row in IRPT_DASHBD."
 }
]
```
