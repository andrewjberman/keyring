# RULING -- COMM_ASSIST call laptop-20261014T123848Z-608c: the assistant may keep two scrubbed metadata records for FWD-13

**Written** 2026-10-14 ~12:4xZ by `1.0.0_SA_CTO` (laptop), on the 10-minute open-calls scan. Scope: OWN-BOX (measured on the row).

**Call:** may the assistant keep two small scrubbed records in the dell2 folder (a channel @mention record and a recent
considered-mail list) so muse can alert Andrew on them (FWD-13, PRD v0.10)? Source:
`org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md` AMENDMENT 7.

## Ruling -- YES, the REC as written, with three bounds

1. **Metadata only.**
   - Mention record: message id, team and channel names, sender, created time, and a scrubbed snippet of at most 120
     characters.
   - Mail list: the last 10 considered mails, as id, sender, firm, scrubbed subject, received time and tag.
   - Never a mail body. Never a link or token a reader could act with.
2. **Written where the item is texted today**, with no new store and no new principal. Rows expire after 7 days. The
   expiry is enforced by the writer on each write, not by a later sweep.
3. **The negative arm is unchanged.** An item outside the FWD-3 watched set and C-MAIL scope gets no row. One row per
   item.

**Why:** FWD-13 names the dell2 folder as the alert source. Today a mention leaves no row, and the single pending
draft hides older mail, so the outcome cannot be served without these two records. Restricting them to metadata keeps
the widening to what the alert itself shows Andrew.

**Route:** `2.0.0_SA_COO~CA` cuts it as one LOCAL code cell (CA-j-12) after muse's shape answer.
