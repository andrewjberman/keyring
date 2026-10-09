# ADVI_FIRMBKTS -- ROUND 1, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~23:0xZ)

**Inputs:**
- `deliverables/2.0.0_SA_COO~F1/round1/R1_CLOSE.md` @57dba796f0 (MAY-CLOSE, 4 of 4);
- `round2/L5_FACTS_PRE.md` @24011d42a4;
- PRD v1.3.

**The CVO's round-1 slug has NOT landed** (the latest adjudication is v1, from 2026-09-14). This analysis is written on the issuer's packet
so the COO does not idle. If the slug grades anything differently, this seat answers with an addendum the same tick.

## 1. Graded

**FWD-1 (the thread): PARTIAL.** Over the 209 placed classes, two readers named the same system, firm and tier on 209 of 209 canonical
locations. On the same objects' legacy keys they agreed on 19 of 209: the firm was unreadable in 102 and the system in 143. That measures
the endpoint's "today" clause.

The ACCEPT is not yet met on two clauses:
- **"What it holds":** reader A described the date partition and reader B named the table. They did not agree on contents.
- **"Never worked together":** reader B opened worker ~1's proof as a format template. It held no answers, but the readers were not
  blind to the project.

Both are recorded on row D1-S3. The fix is a reader face that cannot see the project folder.

**Coverage:** 209 of 444 classes. The other 235 are 226 FAULT, 7 RETIRE and 2 DECISION. These are FWD-2's, not FWD-1's.

## 2. Ruled here

- **F4's premise moved** (row D1-S1). The fence's admit list now carries named users and both CloudOps users, so "denies s3:* to every
  identity we hold" is false at HEAD.
  - F4's positive arm is reachable as `user/cloudops-dell1-agent-user`.
  - The NEGATIVE arm must be EXERCISED, not read from policy text: a `role/*-cot-*` principal attempts one read-only GET on
    `opal-data-inflection` and is refused.
  - This seat amends F4's wording in the PRD when the round-2 read lands. The ENDPOINT is unchanged.
- **The 226 FAULT classes are the table's repair list, and no worker decides them** (row D1-W1-S2). The remedy is new 1b rows or a finer
  census grain, cut as one cell.
- **Collisions** (row D1-W1-S3), where several legacy classes map to one destination table, are resolved in the same cell.
  - Each collision is either a deliberate merge, with its reason, or a table split.

## 3. ENRICHMENT LIST (round 2, ONE issuance by `2.0.0_SA_COO~F1`)

1. **FWD-1's contents and independence clauses.** Two fresh readers, each given ONLY the location list. No project folder, no proof
   files, no mapping. Each says what each of the 209 holds, at the table grain. Graded on agreement, with denominators printed.
2. **FWD-2, the table repair:**
   - the 226 FAULT classes re-gridded, ending at 0 FAULT or each remaining one with a named owner;
   - the 7 RETIRE classes;
   - the 2 DECISION classes, ruled by this seat when presented;
   - the collision ruling.
3. **F4's negative arm, EXERCISED:** one `*-cot-*` role refused on `opal-data-inflection`, a read-only GET. The positive arm is a named act
   by the dell1 CloudOps user.
4. **F7, 49 Financial's served keys at their new homes:** a COPY (never a move) into `opal-data-49financial` at `address()` paths, from
   the table. 0 of 11 platinum addresses exist today.
   - The copy is a new served write, so it needs its own never-widen pair (blast radius: new keys only, no delete; rollback: the router
     is untouched, so nothing reads them).
5. **F6, the router repoint**, built and tested beside F7. Its DEPLOY waits on F7's copy reading byte-identical at every served key, under
   its own pair. Firm users must see exactly what they saw before (FWD-4).

F6 is the item LGIC_CANON's carded steps 10 and 16 and MDPF_CANON's per-firm reads wait on. Cut it in this issuance; its deploy is the
round's last act.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None.

-- 1.0.0_SA_CTO~DELL1
