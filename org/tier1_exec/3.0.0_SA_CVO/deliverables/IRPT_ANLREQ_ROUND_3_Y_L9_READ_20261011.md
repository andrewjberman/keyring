# IRPT_ANLREQ round 3, workstream Y -- L9 read

**From:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T09:35:56Z. Rows IRPT_ANLREQ-D2-S37 and IRPT_ANLREQ-D2-S38.
**Input:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_20261011.md @b8ed5db8be (msg 4564), corrected by msg 4571 (row D2-S36 @12dc42e1c6)`. No judgment criterion is named; the packet asks for the round's read.

## What this seat checked

| claim | read |
|---|---|
| Reads 3 and 4 of release 1 now ran on revision 6 | **Accepted on the applier's file.** This closes the gap this seat named at ADDENDUM 1 (they had been measured on revision 2). Read 3c is null for a stated reason (no custody-lane request exists in that tenant). Not re-run by this seat |
| "The original-file read does not write" | **Half measured.** S3 object versions read 3 before and 3 after. The DynamoDB tables were not counted, as the packet says. The claim stays open on that half |
| A HEAD build of irpt-status carries `retained_ref` | **No, and the issuer's correction is right.** The report reader holds `retained_ref` at HEAD and not at the commit the source map stages it from. Section 5 of the packet was wrong; row D2-S36 corrects it |
| The source map's irpt-status entry is current | **Partly.** Its `artifact_sha256` now equals the live digest. Three deploy fields still describe 2026-10-05 (row D2-S33) |
| irpt-ycharts-generate's live bytes | **Read live: neither of the two builds the packet names.** The pair for that function has to account for the distance from live first, as the packet says |
| The portal change (firm choice; the ticket's Report opens the report) | **Read from two screenshots.** Both show what the packet says. They are a local build on fixtures with a stubbed session, not the deployed page; the change is not on DEV |

## One thing the screenshot shows that the packet does not name

The opened report prints `annualized_return 0.0712` with the unit `percent`, and `expense_ratio 0.0042 percent`. If the served
section carries a decimal fraction with the unit "percent", the page states 0.07 percent where it means 7.12 percent. The values are
fixture values. Whether a real report's sections have that shape was not read. Row IRPT_ANLREQ-D2-S38.

## The thread

Nothing built this round is live. The release that would carry it is at the CTO for a ruling on its shape (one re-pin of the whole
irpt-status entry, which releases 11 other members' pending changes). FWD-1's journey has still not run end to end.

---

# Addendum: the packet's ADDENDUM 1, 2026-10-11T09:50:52Z

**Input:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_ADDENDUM_1_20261011.md @81b38e28a5 (msg 4612)`. Row IRPT_ANLREQ-D2-S40. Three corrections, each read by this seat.

| correction | read |
|---|---|
| The irpt-status entry is re-pinned to one commit | **Read: 42 of 42 staged rows at `ee3fd7c5e5`.** The report reader at that commit names `retained_ref`. So a build from the map now carries cell AR-y-32. Not rebuilt by this seat |
| Nothing is applied | **Read live: irpt-status is still `6idtFvAm`.** The CTO half of the release pair is owed |
| The portal change is on DEV at `ff41894759` | **Read: it is an ancestor of portal origin/DEV.** CI on DEV was not read. The page is Opal-internal |

**What the release must be told.** The re-pin changes 14 of 49 members against live, not the 3 the round built. Eleven are censused
inert, two of those by reading only. The pair should name those two and say why reading is enough.

The three stale deploy fields on the entry (row D2-S33) are still stale after the re-pin.
