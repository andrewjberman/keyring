# Andrew-direct, 2026-10-13 ~14:1xZ (10:1x am ET), at the `1.0.0_SA_CTO~DELL1` terminal

**Verbatim:**

> We don't need anything prior to the earliest record of a client in the system, which generally would be 2020, in the case of Cottonwood Backfill could be as early as 2012. I think it is important to note that any backfill is thereby cut at 2012.

**Context:** MDPF_SECHIST CARD-A Bloomberg client history (1,319 names, about 2.4M cells as filed; `2.0.0_SA_COO~Q1` msg 4873). This seat ruled per-security windows, with P1 living-client
names first.

**Recorded as law for EVERY backfill (any vendor, any project, any box):**
1. **The start of a security's backfill window is the EARLIEST CLIENT RECORD in the system** that holds it: the client's (or the firm's) first date on our plane, generally
   2020.
2. **A HARD FLOOR of 2012-01-01:** no backfill request reaches before 2012-01-01, whatever a record says. Cottonwood's backfill may reach as early as 2012, and never earlier.
3. **The window a request may ask for** is therefore `[max(earliest client record for that security, 2012-01-01), today]`, intersected with the dates the security was actually
   held (this seat's per-security ruling). A request that asks for earlier dates is refused at the queue, not trimmed silently.

**Who it reaches:** the dell1 backfill and history owners (MDPF_DEMQUE `~Q1`, MDPF_SECHIST `~H1`), and, by relay, every box's backfill work, ADVI_COTBKF above all (dell2).

-- recorded by 1.0.0_SA_CTO~DELL1
