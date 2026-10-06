# ETFS_RIVALS -- ROUND 11 ANALYSIS (L10), with round 12 RIV-au-1's J1, `1.0.0_SA_CTO~Z`, 2026-10-06 ~19:2xZ

**Input:** CVO slug msg 30224. Review `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R11_R12_REVIEW_20261006.md` @69de0f08e0
(compile ADJUDICATION_v11.Z, REMEDIATION_v11.Z). Round 12's BBGLEG workstream (eb-1, pk-1) is NOT in this slug. It compiles at its
own drain-end, and ADDENDUM 5 of the round-10 analysis already rules its deploy order.

## 1. WHAT THE ROUNDS DELIVERED

- **Round 11:** gt-1 (G5 stamps `producer_version`, the `-v02` replay served) and dr-1 (C-S38 REMEDIATED). Both PASS. All 5
  Lambdas hold 39 of 39 package files at 50a2248fe9, against a negative control of 7 differing files at the prior pin.
- **Round 12 au-1** (ADDENDUM 4 steps 1 and 2): the audit trail is off the page, and every ticker mention is a button.
  - The served 10-06 page is 1,294,421 B, and the 2,073 buttons all resolve.
  - 234 of 234 real clicks open the right modal.
  - **J1 is PASS-in-part:** 15 mentions open a modal with no section for the linking fund (C-S47).

**Round 11 is CLOSED.** ADDENDUM 4 step 2 is GRADED. C-S47 is a defect inside a working link and does not hold step 3.

## 2. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **C-S47:** 15 mentions (3 securities, 2 funds) open a modal without the linking fund | **The CVO's one rule:** a mention in fund F's panel links to the key F holds or traded, and F's engagement gets a modal section even when F has no contribution row (a fresh entry such as SpaceX in GQGU). It is the same rule as Z-S50 (`NEVER_WIDEN_ROUND12_DEPLOY_CTO_HALF.md` @4a7b1cf411): a name with two listings resolves by F's own holdings. Nebius rides pk-1 after the ADDENDUM 5 alignment. **One round-13 cell** carries C-S47 and Z-S50. | Andrew's words are "the modal popup for **that fund's** engagement with that security". A modal without that fund answers a different question. |
| 2 | **The check the CVO says nobody had** | **A round-13 mechanical criterion, over EVERY button:** the target modal carries `section[data-fund=F]` for the fund F whose panel holds the button. Print the count of buttons, the count with the section, and the count missing (0). | It turns a judgment the CVO found by clicking into a gate that runs every day. The class may have been served since the 10-05 pages with no check seeing it. |
| 3 | **Machine keys in the AI modals' citation lines** (148 keys in 89 lines: CUSIPs and `<ticker>_XX_Equity`) | **They move to the audit page with ADDENDUM 4 step 3.** They are grounding records, not prose mentions, so Andrew's "any mention" does not make them links. They are also system keys on the presentation page, which is FWD-18's "not an audit log" (RFW-U08). Until step 3 they stay as they are. | They are audit material, and it belongs one step away. |
| 4 | **The slug gate refused round 11** (it reads the first `<status>` tag; the cell_ref check reads the decomposition at HEAD) | **The gate reads the LAST `<status>` tag**, since orders append their flips. **The cell_ref check reads the decomposition at the order's issuance commit**, since a later DECOMP version that replaces cells in place cannot void an issued order. COO~RV files it as a surprise row against the gate. The audited override on round 11 stands. | Both orders are complete, and both checks re-ran PASS. A gate that refuses a true terminal state invites routine overrides. |
| 5 | **nm-3 widened:** ticker-form names grew from 2 holdings to 4 securities (8053 JP, 9433 JP, RBLX US, 000270 KS) | They join C-S36's control set in the same round-13 cell as rulings 1-2. | The dialogs coming back exposed them. It is the same display-name class. |

## 3. ENRICHMENT LIST (round 13, ONE issuance by `2.0.0_SA_COO~RV`)

1. **ADDENDUM 4 step 3:** the `GET /rivalfunds/YYYY-MM-DD/audit` gateway route under a never-widen pair, then the page's one link.
   The audit page carries its own dialogs, plus the citation lines (ruling 3).
2. **The fund-engagement cell:** rulings 1, 2 and 5. Its mechanical criterion is ruling 2, plus the C-S36 control set.
3. **pk-1:** the alignment cell and one deploy pair (round-10 ADDENDUM 5), if not already landed in round 12's BBGLEG.
4. **The slug-gate row** (ruling 4), owned by the gate's lane, not by this project's cells.

Still OPEN and carried: S24 (the backfill-night proof) and W6-S2 (the planted proof not yet built).

## 4. ACTS FOR ANDREW (cited)

None. The audit route is a gateway deploy under its pair, which is in this fabric's normal path.
