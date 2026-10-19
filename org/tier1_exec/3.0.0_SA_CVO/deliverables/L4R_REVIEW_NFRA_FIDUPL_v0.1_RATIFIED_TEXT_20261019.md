# L4-R review -- NFRA_FIDUPL PRD v0.1 @3324161d52, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-19 ~18:2xZ. Delivered by 1.0.0_SA_CTO~DELL1 msg 8429 (acked). Half hash
`2f70753360a5`. Brief half: SIGNED (auto, CRO-written brief).

**Read:** `org/missions/D8/NFRA/NFRA_FIDUPL/prd/NFRA_FIDUPL_PRD.md` @3324161d52, whole (180 lines); the L2 record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_FIDUPL_20261019.md` @24f0400d63; `python .tools/open-calls.py list` on dell1.

## Verdict: REFUSE (two grounds)

- **Ground 1 -- the ENDPOINT has no ratified pin.** Open call `dell1-20261019T180825Z-e141` ("confirm NFRA_FIDUPL's 8 DONE WHEN lines") reads
  `[OPEN]` at this read. The L2 record says "L2 is not complete until Andrew confirms the DONE WHEN lines", and the PRD says "This PRD goes
  to L4-R after he confirms". This is the same ground on which ADVI_COTBOOKS v0.1 and v0.2 were refused (@8cc7a87a60, @8f584cb1a3).
- **Ground 2 -- two DONE WHEN lines are waits (CLAUDE.md rule 27 L2: NO FWD IS A WAIT).**
  - **FWD-2** is proven only by "the scheduled run is read on an ordinary business-day morning beside the Schwab run". That is the organic
    case alone, with no act a seat can drive on demand. The window may make this wait genuinely essential. If so, the line must say so
    expressly, with its reason and Andrew's word. Otherwise, name a driven arm (for example, the schedule's own target invoked inside the
    window) and keep the organic morning as the negative arm.
  - **FWD-4** is proven only by "a Monday morning's files ... are read". The next Monday is 2026-10-26. A driven arm is already within reach:
    an on-demand export of a past Monday, the mechanism C-BACKFILL plans. Either name it, or qualify the wait as above.
  - Andrew has not yet confirmed the lines, so a fix now does not cost him a second confirmation.

## Checks that pass

- **Verbatim:** the PRD's ENDPOINT block is byte-identical to the L2 record's (a script compared the two fenced blocks: IDENTICAL; 0
  non-ASCII characters).
- **Clean section:** the ENDPOINT section holds only the block, with no annotation, history or seat name.
- **Operative constraints present:** Andrew's 17:55Z order holds three operative constraints. The Terraform is FWD-7 (with C-TF). "Every
  morning at the same time that schwab does" is FWD-2 (with C-WINDOW). "The relevant tables" is FWD-1 and FWD-5 (with C-PULL, six files).
- **CONTRACTS:** no counterpart PRD exists, so there is nothing to disagree with. C-TOU, C-NAMES (rule 30) and C-RECORD (the moratorium,
  read-only) are consistent with CLAUDE.md.

## Nit, not a ground

- FWD-8's "both run on the same morning" can be driven on demand by running both on one morning. Wording it as "both run back to back on
  demand, and on one scheduled morning" would remove the calendar reading.

## Re-delivery

Re-deliver after Andrew confirms the lines. If the confirmed lines close ground 2 (a driven arm, or an expressly qualified wait, for FWD-2
and FWD-4), this half is signed on that delivery with no further reading.

-- 3.0.0_SA_CVO~DELL1
