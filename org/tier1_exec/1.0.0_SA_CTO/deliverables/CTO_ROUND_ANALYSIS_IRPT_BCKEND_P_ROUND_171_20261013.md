# CTO ROUND-171 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering the round-170 L10 slug (2026-10-13 ~03:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `surprise-channel/remediations/REMEDIATION_v47.md` @df840ac108 and the CVO's v0.52 review
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_PRD_v0.52_RATIFIED_TEXT_REVIEW_20261013.md` @cab1de19b0 (msg 6763): v0.52's half
SIGNED with an order condition; 6 rows OPEN, 4 ARMED. **No PRD addendum.**

## 1. Rulings

| row | ruling |
|---|---|
| **D2-W345-S3** (ARMED: every live 49 Financial build copies the Tax membership snapshot, which carries client account numbers, to a system temp file and never removes it) | **FIRST in round 171.** The builder reads it in memory, or writes it under a `finally` that removes it; a test proves no file remains after a build that raises. One read of the host's temp space for files left by past builds, counts only, no contents; any found are listed for a human delete (a delete of client-bearing files is a person's act). Row D2-S122's rule holds until the cell is live: no seat calls `retained_capture` or `build_49f_meshed` outside the schedule. This is client data at rest on a host, not git (Andrew's 2026-10-09 word covers git only). |
| **D2-W344-S1** (the producer pair's ORDER, the CVO's v0.52 condition) | Accepted as written: the old node schema has `additionalProperties: false` and `holdings/snapshot.py` validates at serve, so BOTH packaged copies (`irpt-holdings`, `irpt-ycharts-generate`) re-pin and deploy BEFORE the builder first writes `account_id`. **`irpt-ycharts-generate` is also IRPT_ANLREQ's reader release:** the two pairs never run on that function at once; IRPT_ANLREQ's release (a live defect) goes first, and this re-pin follows it, or rides it if the bytes are ready and that pair names it. |
| **D2-W344-S2** (`raw_keys.json` declares the smartx key; the live builder mints from Schwab `dim_balance.account_id`) | The builder cell corrects the declared key with a citation to the live mint (`holdings_49f.py:339`), before anything mints or audits 49F account ids from that file. |
| **D2-W346-S2, -S3** (two fixture generators cannot reproduce their committed bytes) | One portal cell repairs both generators so they reproduce the committed bytes, before anyone regenerates. |
| **D2-W346-S4** | Accepted: the portal fixture follow-up aligns `selected_sections`. |
| **D2-S121** (still listed OPEN, owner this seat) | Ruled at round 170 (@537391d103): the inferred branch is recorded offline-proven only, with its reason. Close at the CVO's next compile. |

## 2. ENRICHMENT LIST for round 171 (~P, ONE issuance; each build order at most three mechanical criteria)

1. The 49F temp-file cell (W345-S3), with the host read. FIRST.
2. The producer pair in the CVO's order: both packaged `HoldingsSnapshot` copies re-pinned and deployed, then the builder's
   `account_id` (with W344-S2's key correction), the last-four ACCOUNT entry, and the 49F node/account mismatch count.
3. The portal generator repair (W346-S2, S3) and the fixture alignment (W346-S4).

## 3. Acts only Andrew can do

None new; a delete of client-bearing temp files found by item 1's read would be one, raised then.

-- 1.0.0_SA_CTO~DELL2

## 4. After the drain (2026-10-13 ~04:1xZ; `2.0.0_SA_COO~P2` msg 6779, packet `IRPT_BCKEND_ROUND_171_P_DRAIN_END_20261013.md`)

- **W348-S2 (the `irpt-holdings` re-pin at HEAD also enables `include=target` and drops `multi_asset`): a MINIMAL pin.** The release
  moves only what the `account_id` order needs: the live members plus the two packaged `HoldingsSnapshot` copies (and the builder
  member, when its step comes). Enabling `include=target` and dropping `multi_asset` change what a client's answer carries; each is
  its own never-widen pair later, with its consumers read. Same rule as IRPT_ANLREQ's resident (only the members a release needs move).
- **IB-pr-497 parked** (the host is not Online; no start/stop is granted): accepted. A stopped host runs no build, so it writes no new
  temp file; the read runs when the host is next Online, and a start for a read alone is not cut. The temp-file cell's code ships
  regardless.
- The CVO's compile of round 171 is the L10 input; this file answers it when it lands.
