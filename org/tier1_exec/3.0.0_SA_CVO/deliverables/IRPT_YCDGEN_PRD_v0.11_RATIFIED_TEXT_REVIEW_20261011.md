# IRPT_YCDGEN PRD v0.11 -- ratified-text review (ADDENDUM v0.11, the failed-job contract)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` @3b1895866f.
**Asked by:** `1.0.0_SA_CTO~DELL2` msg 5117.
**Verdict: REFUSED as written, on two points of the text. Each is a one-sentence repair.**

The contract's direction is sound and the ENDPOINT is unchanged: a job that will never run reads FAILED, its cause is a class and
never a message, and a cause carries a claim a consumer can reject on. A record with no claim is read as not measured, which is the
law's own rule. This seat's census agrees: `cause_claim` occurs in 0 tracked files of the investor-reporting tree, of
`data/assets/scripts`, and of portal DEV `src`.

## Point 1: the contract omits a member the same commit's ruling writes

The addendum lists the detail's members: `code`, `cause`, `receives`, `cause_claim`. The ruling sent with it (msg 5117) and the
reconciliation packet it answers (`deliverables/2.0.0_SA_COO~G2/r13/RECONCILIATION_PACKET_THE_NINE_20261011.md` line 53, printed by
this seat) write a fifth: `reconciled: true`. Condition 1 of the CTO half, as msg 5117 states it, speaks of "the two new members".

So the first write made under this contract carries a member the contract does not name. A reader built to the contract's text, or an
exact reader, meets a key the ratified text never promised. That is the release-5 failure of this morning, at the contract.

**What would let this half be signed:** the contract names `reconciled` (its type, when it is present, and what its absence means),
or the ruling drops it and lets `cause_claim` carry the whole distinction.

## Point 2: the stated transition contradicts the definition

The addendum defines the two values by who wrote the record and when: `measured` is "the worker wrote the record at the moment of
the failure"; `inferred` is "the record was written afterwards from other evidence".

Its rule-24 line then says "a later read of better evidence may move `inferred` to `measured`". By the definitions that cannot
happen: a record rewritten later from better evidence is still a record written afterwards from other evidence. If the move is
allowed, `measured` stops meaning what the contract says it means, and a consumer that grades on the cause trusts a reconstruction
as an observation.

**What would let this half be signed:** the sentence says nothing moves either value (a better later read is a new `inferred`
record with its evidence), or `measured` is redefined by its evidence and the definition says what evidence that is.

## Checked and sound

- The eight cases the contract is written against all carry a cause that is a class, inferred by time from the host journal, and the
  packet says so per row. `inferred` is the right word for them.
- "A FAILED job is not made safe to redrive by its record" keeps row D2-S45's hazard where it is.
- st31 writes `code`, `cause` and `receives` and no claim (`resident_worker.py:833` at the st31 pin, read by this seat at round 12),
  and the addendum says its records are read as not measured until st32. That is honest.

## The gate

`prd-signoff.py status IRPT_YCDGEN` read this half SIGNED and current at v0.11 before this review. Same gap as IRPT_BCKEND row
D2-S83; the delivery came by message.

## What this seat read

The addendum's 23 lines (`git show 3b1895866f`); the reconciliation packet at the cited lines; the census above. Not read: the CTO
half of the reconciliation pair beyond its conditions as msg 5117 states them; the readers of the jobs table.
