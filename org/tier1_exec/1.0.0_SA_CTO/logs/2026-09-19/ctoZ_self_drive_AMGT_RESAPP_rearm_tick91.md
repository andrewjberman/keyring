# /self-drive AMGT_RESAPP -- ticks 86-91 (1.0.0_SA_CTO~Z), 2026-09-19 ~03:1xZ - ~06:3xZ

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_13xxZ_SELF_DRIVE_AMGT_RESAPP_REARMED.md`
**state: ARMED.** Written at the 6-tick / ~3h FLOOR: the last log `23c5308b8f` has author time 2026-09-19T03:10:18Z, read
from the COMMIT and never from the filename.

## Acts

| what | commit |
|---|---|
| the CRO's read of `REF_A` / `REF_C` appended to the report-format intake, and THIS SEAT'S OWN CARD CORRECTED | `d50d2601a2` |

No other act by this seat in this window. Nothing was owed: all 13 co-signed round-14 cells carry both never-widen halves.

## The round, measured at each tick from the ORDER FILES

`complete` counts, line-anchored (`^[ \t]*<status>\s*([A-Za-z_-]+)\s*</status>[ \t]*$`): 9 -> 11 -> 13 -> 13 -> 13 -> **14
of 31**, 17 pending. Drains this window: slots 37, 41, 43, 45, 48, 58. `rk-41` landed after its AC7 was repaired to match
its bind and re-spawned for re-grade. Held cells remain on their real gates, two of them on the registry gate this seat's
own rows set.

⚠ **AN INSTRUMENT CORRECTION THIS SEAT MADE ON ITSELF, and it is the reason the counts above are trustworthy.** Three
readings were wrong before one was right: (1) `grep -c complete` over `*rk-*.md` mixes ROUNDS, because `rk-` numbering runs
back into round 13 -- 64 files, not 31; (2) a naive `<status>` match reported one order's status as `WORD`, because it was
matching PROSE inside `rk-56`, the cell whose whole subject is the status element and which quotes `<status>WORD</status>`
as a template; (3) the line-anchored form -- **specified by that same order** -- reads `rk-56` as `complete`, so the earlier
count of 9 was two short. ⭐ **The order that exists because status parsing is fragile is the one that broke the parse.**
Every count in this log uses the line-anchored form over the `31 <= n <= 61` range, with the 31-of-31 denominator printed.

## The report-format intake, and the correction of my own card

`4.0.0_SA_CRO~Z` read `REF_A` and `REF_C` (@`2d098d2ab7`) at this seat's ask, hashing them by a DIFFERENT path (`git show`
out of the object store) and matching all three prefixes -- two seats, two paths, same hashes. **Nothing contradicted the
nine-item delta** and quarterly grain was corroborated on both documents; eight items were added, including four forward
years rather than three, a balance-sheet block we do not pull at all, no product or segment time series anywhere, and an
earnings-call transcript as a cited source.

⚠ **AND IT CORRECTED THIS SEAT'S CARD TO ANDREW.** My card asked whether an Opal report issues *"a recommendation and a
PRICE TARGET"*. `REF_A`'s rating-actions section reports what OTHER analysts did; **neither document issues a house
target**, so the fork is the POSITION LINE alone. I put that correction to him rather than leaving the wider framing
standing. **This is the PRD's own citation rule broken one level up:** I characterised a document I had not read, from a
summary, and the characterisation was wider than the source. The delta items survived because each names a CLAUSE; the
card did not, because it named the DOCUMENT.

⭐ Also surfaced for his open card: `REF_C` s.8 already prints Bear / Base / Bull with assumptions, so the methodology
discussion he reserved at v0.12 is answered inside the document he sent.

## Scope and completion

AMGT_RESAPP: `status` active, `dep_stage` EXECUTING, PRD v0.13 ADMITTED, 14 of 31 round-14 orders complete. COMPLETION
TEST: **NOT DONE -- 0 of 1 projects complete.** Nothing stalled in any tick of this window; nothing routed to
`0.0.0_AB_MSTR~Z`. **Open at Andrew: TWO** -- the bucket shape (doctrine vs new tenancy), and the position line
(`REF_A` issues one, `REF_B` declines; REC is `REF_B`).

⚠ **One nudge NOT sent, recorded because the restraint was the right act:** at 01:09Z worker branches read 0 of 13 moved
and index mtimes read most trees quiet for ~58 minutes. Both instruments are blind to a worker that is reading or
building, and the COO -- which sees its own subagents -- measured all 13 active. The better instrument won.

## Compiler Tools

git log / safe-commit (verify by HEAD), line-anchored status reads over the order files with the denominator printed,
`pymupdf`, `sha256sum`, broker `get_live_agents` / `send_message` / `set_summary`, inbox Monitor.

-- `1.0.0_SA_CTO~Z`
