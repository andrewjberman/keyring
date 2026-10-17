# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 88 (covers ticks 87a and 87b, about 21:19Z to 21:48Z)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **RESAPP round-113 item 3, layout:clipped (R1 7740).** The clipped container is an overflow-x-auto scroller: 228 px of horizontal scroll,
  with a transparent scrollbar 9,291 px down the grid. The walker counts the scroller's hidden width as clipped.
  - RULED: by design, so no cell; the walker's probe is corrected by its owner.
  - Round-114 candidate: a scroll affordance the reader can see (a bounded-height scroller or a visible cue), graded on a built page.
  - Item 2 (the scroller clipping the last rows' tooltip) is being re-cut by R1.
- **HARVST cf-2 merged @80d0701876 (W1 7742).** 17 names change, with HOLDING_CHANGED = 0; the controls are unchanged. 13 lose a non-holding
  fund_of_record, and the 4 JP names lose a description-as-position.
  - cf-4 is the 17-name add-only rebuild. COO half 275d5739 @74ff9ed727.
  - CTO half SIGNED @8a5ea52464: C-1 to C-10, the S44 foreground rule with a manifest check after every write, and site Z told first.

## Completion test

NOT DONE. This is the standing box drive, which ends on Andrew's word.

## Acts only Andrew can do (each with its citation)

1. ADVI_COTBOOKS: confirm the 6 DONE WHEN lines (row 0cf5). Canonical loop L2.
2. SOC2_MSLOGS round 2: run the 8-day re-derive with his MFA session (row 89c9). The access group holds Andrew_Berman alone (TO-R2-r2 :29).
3. SOC2_MSLOGS FWD-1: his read of the enriched block, through the same MFA door.
4. EWS delivery channel. Nothing sends until he names one.
5. FWD-10's portal source line to PROD, a client-facing push (CLAUDE.md PUSHES).

## Compiler Tools

| tool | result | note |
|---|---|---|
| sha256sum on the cf-4 COO half | PASS | binding |
| git log on the COO half | PASS | committed at 74ff9ed727, clean |

What worked: a real-browser measurement settled a walker finding that no CSS tweak could. Gap: none new.

-- 1.0.0_SA_CTO~DELL1
