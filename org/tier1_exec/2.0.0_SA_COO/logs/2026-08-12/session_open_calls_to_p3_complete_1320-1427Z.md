# Session log — `2.0.0_SA_COO` — 2026-08-12 13:20Z–14:27Z

**archetype:** COORDINATE · **secondary_archetypes:** DIAGNOSE, VALIDATE
**Window:** Andrew's `/open-calls` rulings -> P3 cutover complete. `/drive` loop OFF by his word.

## WHAT ANDREW DECIDED (verbatim record @67b9fe8966)

> *"all recs approved, for securities im looking into it with CVO now, for edit rights yes i would
> like to make that text editable just want it to be extremely light and client-facing do not want
> overwrought process architecture around this should be extremely simple setup, for ETFS canonical
> location its opal-data-etfs"*

Six calls answered. **P3 AUTHORIZED · ETFS canon = `opal-data-etfs` · pillar text EDITABLE under a
hard ceiling · estate-pull backlog DROPPED · ETFS email = Andrew only · securities at Andrew+CVO.**

## SHIPPED

**P3 COMPLETE** — the write side of the Andrew-authorized 49F cutover. `@aa72ab5bc5`, ledger
`@e99231aeda`. 4,206/4,206 objects copied per-key (not `--recursive`, so every outcome OBSERVED not
inferred), two-sided counts per table on objects AND bytes, parquet parsed from each of four tables.
1+10 re-point as one act, `SCOPE` untouched with an inline DO-NOT-RE-POINT note.
**P4 exit condition live in the file: P4 MAY NOT CLOSE while `schwab/08335338/gold/` exists.**
**AE's IAM leg** `@b6e5cf9c2f` — three-layer verified, five isolated simulate calls, platinum fence
and pin both proven to hold.
**OPAL_INVPHL pillar-editability GO'd** on a scope with ZERO new artifacts — `GenerateCMA` was
already a step in the portal's Data Refresh pipeline.

## ⛔ FIVE DEFECTS IN MY OWN INSTRUCTIONS, ALL CAUGHT BEFORE EXECUTION

| # | my instruction | the defect | who caught it |
|---|---|---|---|
| 1 | "execute the 08-05 mirror backfill" | the mirror had nothing to mirror | AE |
| 2 | P3 IAM = `PutObject` | gold-reads-gold needs Get + conditioned List | DS |
| 3 | "three edits: K1 · K2 `SCOPE`'s gold derivation · K3" | named the variable you must NOT edit; real surface 1+10 | DS |
| 4 | ruling basis #1 (the `runner_common` docstring) | a sentence about HELPER duplication, silent on topology | DS |
| 5 | "rebuild + apply so deployed matches repo" | no drift existed; would have been a no-op that LOOKED like a fix | AE |

> ⚡ **DS's explanation is the one I am keeping: *"the reason these keep getting caught is that your
> dispatches carry the mechanism and not just the instruction — a vaguer order would have been easier
> to follow and harder to check."*** **A CHECKABLE order beats a correct one, because a correct order
> still fails when the world differs from the author's model and only a checkable one lets the
> executor find that out.**
> ⛔ **And defect 4 is the one that would have done lasting harm: my basis would have hardened a
> misread docstring into a COO ruling that blocked a legitimate P5 retirement. DS flagged it while
> AGREEING with my outcome.**

## ⛔ MY RELAY LATENCY EXCEEDED THE FABRIC'S SELF-CORRECTION CYCLE — TWICE

**I relayed two findings to Andrew that their own authors falsified 7 and 20 minutes later:**
- DS's "zero consumers read the gold root" -> retracted; consumers exist (variable-assembled paths)
- AE's "three lambdas running stale code" -> one confirmed, not three (two homes, not drift)

> **Both times the author caught it unprompted. Both times I had already spent Andrew's attention on
> the unsettled version.** ⚡ **The fix is not to hold findings — that reintroduces the invisible-hold
> problem — it is to RELAY THE SETTLEDNESS WITH THE FINDING.** *"This is 20 minutes old and the
> author is still auditing" is a different claim from "this is established," and I stated neither.*
> **Adopted going forward.**

## ⭐ THE VERIFICATION MOVES WORTH PRESERVING (none mine)

**CVO — the self-comparison refusal.** CTO asked for a full-history green on LEG-3's losslessness.
CVO refused it: *comparing a historical `.jsonl.gz` to its `.parquet` is SELF-COMPARISON — that
jsonl.gz IS the transform's output, so a match proves DETERMINISM not FAITHFULNESS.* **"The obvious
2,297-date exercise would have produced a perfect, meaningless PASS."** They produced a single-date
INDEPENDENT witness instead, ⭐ **where the proof of independence was the ROW-ORDER DIFFERENCE
ITSELF: *"the thing that made it fail byte-equality is what qualifies it as a witness."*** Verdict
FORMAT RESTORATION, to the BYTE per record (411,706/411,706 numeric comparisons). Routed to land in
`CONTROLS_OVER_CARE.md` as a fifth way, phrased as theirs.
**Also theirs: *"a sentence readable as either a PLAN or a RECEIPT will be read as a receipt by the
next agent"* — the docstring CTO cited was forward-looking. The citation was never a citation.**

**DS — the old-root discriminating control.** They verified the place the write should NOT have gone
did not move (old root untouched at 2026-08-11T18:43:30Z). ⚡ **Presence at the new root could never
have separated "re-point worked" from "re-point no-op'd."** Plus the ETag identity proving the
re-point changed WHERE and provably not WHAT, and **ruff flagging `SCOPE` as unused in `c01_runner`
— a style gate incidentally verifying a topology claim.**

**AE — the isolated negative control.** On the SEP-1 grant: the positive read was worthless without
proving the simulate DISCRIMINATES for that principal. Also caught `aws s3 ls` rendering
LastModified in LOCAL time and nearly reporting the wrong minute.

**DT — the mutation test.** Injected the naive `sheet_name='Philosophy'` read: `ValueError` —
**CMA generation going down on the NORMAL case, every workbook Yang has ever uploaded, from an
OPTIONAL feature.** It would have passed every test anyone would think to write.

## ⛔ WHAT I GOT WRONG ABOUT THE 17a REMEDY, AND CTO's CORRECTION

**I framed the daily bronze `.parquet` writes as bleeding-daily pressure and placed a port.**
**CTO withdrew it: *"the format divergence is the ONLY reason this collision was ever visible;
unifying the format without assigning ownership CONCEALS it. That is strictly worse than today."***
**The real defect is *a forked pipeline whose kill-half never happened* — two SCHEDULED producers two
minutes apart. The question is WHICH PATH SURVIVES, not which format wins.**
⚡ **I had the cost right and the remedy wrong.** *"A known, dated, tracked daily violation is cheaper
than a dark pipeline from a kill placed without a consumption map."*
**And CTO reframed what I had been calling a tax: *"the gate refusing daily is CORRECT behavior on a
real violation — what was wrong is that the violation had no adjudicated disposition, so a working
guard read as a daily tax."***

## THE BIGGEST FINDING IS NONE OF THE ABOVE
**`s3://opal-data-inf/code/bronze/pull_inflection_assets_v2.py` runs daily in production and has NO
REPO HOME anyone could locate** — unreviewable, ungateable, **impossible to drift-check because there
is nothing to compare it against.** A standing violation of the deploy law's own premise. CTO widened
the authorized census to cover EC2-staged code, and added `NO-MAPPABLE-BUILD-INPUT` as a fourth
classification value after I flagged the taxonomy was not MECE — **with the Rule-24(iv) note that it
is the one value that does not move with the others: the first three are remedied by a deploy or a
decision; this one needs a repo home ESTABLISHED FIRST.**
**And AE dated the EC2 copy from its own prose (`:19` records its docstrings were fixed 2026-07-22),
placing the deployed vintage ~3 weeks stale — the half-ported artifact carried the evidence of its
own staleness in a comment.**

## COMPILER TOOLS
`comp-find --name` (P3/P4 TO search, 523-TO denominator) · `deploy_ledger check --red` (the
false-RED cascade; CTO fixed the CLASS with a compound-field segmenter @a6b8b1dbda, 5 false REDs
cleared, ~15 true positives remain) · raw `aws s3 ls` **with two positive controls** on the P3
product-root absence · `sha256sum` + `git log` to verify AE's two-homes claim independently.
**Gap found:** no comp-tool answers "does this deployed artifact match its build input" — the class
CTO has now authorized a census for.

## OPEN AT SESSION END
- **CTO:** survivor + decommission ruling on the inf bronze fork (AE building the consumption map).
- **AE:** consumption map · SEP-1 carry #1 (roster-derived CSV count) · the two-source repoint
  differencing (the live candidate for the unattributed +$532,625) · CMA producer commit.
- **DT:** CMA producer edit is in-tree, owned-paths-refused to them, routed to AE (in-lane, no override).
- **DS:** queue EMPTY by design. 14:56Z step-4 tick.
- **P4** will bring the never-widen sign-off to me and CTO. **Not yet.**
- **Andrew:** nothing. Both items I escalated dissolved — the vendor egress word is not needed
  (CTO's third way) and the floor-race harm measured ZERO.
