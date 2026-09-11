# ANDREW-DIRECT 2026-09-11 ~18:5xZ -- both /open-calls cards RULED

**archetype:** SCRIBE (record) + VALIDATE · **recorded by** `1.0.0_SA_CTO~Z` · **channel:** Andrew-direct
at the `1.0.0_SA_CTO~Z` terminal, answering this seat's `/open-calls` (2 cards).

## 1. THE WORD, VERBATIM AND ENTIRE

> **"call 1 yes, call 2 no it should actuall be a rename there is no data in there anyway, better to
> have all of this stuff grouped by name right from the start."**

Nothing is paraphrased and nothing is omitted. No other words on this subject at this terminal.

## 2. CALL 1 -- RULED **YES**

**The call as put:** may POSN_ASTTAX round 2 route its slug with two cells DELIBERATELY un-run?
**His answer:** yes.

Round 2 may route with `TO-S2-1` and `TO-S3-1` carried forward EXPLICITLY as un-run, the measured
`TO-S7-1` NO-GO as their stated reason.

⛔ **SCOPE OF THE PERMISSION, read NARROW and stated so nobody widens it later.** He answered a card
about ONE round. **LD-0521 -- "We do not route until the job is over" -- is NOT amended and still binds
every other round on both fabrics.** This is an exception granted on a named case, not a new general
rule, and no seat should cite it as precedent without asking him again.

⛔ **WHAT IS STILL NOT AUTHORISED, because his word did not reach these:** flipping S2-1/S3-1 to a
terminal status, running the retag, or treating the NO-GO as lifted. The mechanical refuser in
`surprise-row-gate.py::_route_precondition_violations` will still fire on the remediation row.
⚠ **THAT IS NOW A MECHANICAL OBSTACLE STANDING AGAINST A SOVEREIGN PERMISSION** -- a genuinely new
state. Resolving it is `3.0.0_SA_CVO~Z`'s call on its own gate. If the clean path is the audited
`# surprise-row-override:`, it now has **Andrew's word behind it rather than agent judgment**, which is
precisely the distinction that made that escape unavailable an hour earlier.

The four proposed `DECOMP_INVALIDATING` dispositions (C-S13, C-S18, C-S19, C-S21) unblock on the same
word.

## 3. CALL 2 -- RULED **RENAME**, AGAINST THIS SEAT'S RECOMMENDATION

**The call as put:** does harvest naming reach `opal-data-research`, or only new resources?
**This seat's REC was (b) prospective-only. He ruled the opposite: RENAME.**

**The decision is ACCEPTED and is NOT re-litigated.** "Better to have all of this stuff grouped by name
right from the start" is a sound reason, it is his call, and the estate is cleaner for it.

### 3a. ⛔ HIS STATED PREMISE IS FACTUALLY WRONG, AND IT WAS MEASURED BEFORE ANYTHING MOVED

He wrote *"there is no data in there anyway."* Measured `2026-09-11T18:55:29Z`, before any act:

| instrument | result |
|---|---|
| `s3api list-objects-v2 --query 'length(Contents)'` | **53 objects** |
| `s3api list-object-versions --query 'length(Versions)'` | **60 versions** |

Contents: `derived/model_block/` for **BABA (4 snapshots), BA (4), NVDA (2), SAP_GY (4)**;
`derived/model_block_fye/` for BABA, BA, SAP_GY; `packs/<ticker>/input_ledger.json` for several
tickers.

**So the act he authorised is a DATA MIGRATION OF 53 OBJECTS, not the rename of an empty bucket.**
S3 has no rename primitive: it is create-copy-delete. That is a materially different act from the one
his sentence describes. **Surfaced to him, NOT used to hold his ruling hostage** -- he gets to re-rule
knowing it, and the default while he does is that nothing is deleted.

### 3b. ⛔ AND THIS SEAT'S OWN REC OVERSTATED THE HARM -- WITHDRAWN IN THE SAME BREATH

The `/open-calls` REC said a rename *"would destroy the evidence FWD-6's accumulate bar rests on."*
**That was TOO STRONG and is WITHDRAWN.**

Measured: the accumulate evidence lives in the **KEY GRAMMAR** -- distinct timestamped paths such as
`.../BABA_US_Equity/20260910T224432Z/` and `.../20260910T225428Z/` -- and **a copy preserves distinct
keys.** What a copy actually loses is the **S3 VERSION HISTORY**: 60 versions collapse to 53 objects,
so roughly **7 versions belonging to overwritten keys** are lost. Nothing in `FWD-6` depends on those,
because the accumulate bar reads the timestamped key grammar and not S3 versioning.

⭐ **So the honest position is weaker than this seat's own rec and is stated as such: the rename is MORE
expensive than he thinks and MUCH CHEAPER than this seat said.** Both corrections belong in the same
record, because reporting only his error while leaving mine standing would be a self-serving account of
the exchange.

### 3c. WHAT THIS SEAT RECOMMENDS NOW

Proceed with his rename **as a MEASURED MIGRATION, not a delete-and-recreate**: copy all 53 objects to
the harvest-named bucket preserving the full key grammar, VERIFY the destination count equals 53 and
the key paths match exactly, and only then delete the source. **Accept the ~7 lost overwrite-versions
EXPLICITLY rather than discovering the loss afterwards.**

⚠ The two DynamoDB tables are a DIFFERENT case and are unaffected: they are genuinely empty (0 items,
measured) and their rename was already approved in the ~18:3xZ draw.

## 4. CONSEQUENCES THIS SEAT OWNS

- **PRD v0.5 s.8c currently says NO retroactive rename of `opal-data-research` absent Andrew's word.
  HIS WORD HAS ARRIVED; that clause is SUPERSEDED** and is amended by this seat so the PRD does not
  sit contradicting a live ruling.
- The migration itself is `4.0.0_SA_CRO~Z`'s to sequence: it holds the harvest estate under his
  execute-and-oversee word. ⚠ **The approved execution order -- "consolidation + renames FIRST while
  both stores are empty" -- was written believing THIS bucket empty too, and needs re-reading against
  53 objects before it runs.**

**Push state:** LOCAL at write time. Broadcast to `4.0.0_SA_CRO~Z`, `2.0.0_SA_COO~ZZZ`,
`3.0.0_SA_CVO~Z`, `2.0.0_SA_COO~Z` and `0.0.0_AB_MSTR~Z` in the SAME TURN as this record (msgs
21531-21535), per `org/XXX.md`. `0.0.0_AB_MSTR~Z` pushes origin/SITEZ.
