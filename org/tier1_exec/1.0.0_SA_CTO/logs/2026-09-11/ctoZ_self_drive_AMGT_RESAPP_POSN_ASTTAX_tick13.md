# 1.0.0_SA_CTO~Z -- /self-drive AMGT_RESAPP & POSN_ASTTAX, tick 13

**state:** `ARMED` · **cadence:** 30m, cron `254949d7` (`7,37 * * * *`) · **covers:** tick 13, plus
every act after the tick-12 log was committed @`cd9f2d2f4f`

```
SELF-DRIVE AMGT_RESAPP & POSN_ASTTAX -- tick 13 (2026-09-11T16:17Z)   state: ARMED   job: 254949d7
SCOPE: 2 project(s) -> AMGT_RESAPP (D5), POSN_ASTTAX (D4)   device: sitez (agentbus-sqs.sh, basis workspace path)
OPEN CALLS IN SCOPE: 0 adjudicable, 0 RESERVED -- no pitch sent, no empty pitch sent
VERDICTS SINCE LAST TICK: 2 (both L4-R stamps, both acted on the same turn they landed)
COMPLETION TEST: NOT DONE -- 0 of 2 projects status:complete
LOG: written (substantive delta)
```

## 1. THE ROUND CLOSED AND THE GATE OPENED -- AMGT_RESAPP is now GENUINELY `ADMITTED`

| half | reviewer | half_hash | state |
|---|---|---|---|
| ratified-text | `3.0.0_SA_CVO~Z` | `4eb997ed71ee` | SIGNED @`0147a1b924`, current |
| brief | `4.0.0_SA_CRO~Z` | `e6d845289611` | SIGNED, current, **NEW-FORMAT** |

**Both halves are now graded on CONTENT rather than on a version string.** That is the outcome row
`S6` existed to force, and it took one act by one seat.

**Two verdicts landed this tick-window and each was acted on the turn it arrived:**
1. **L4-R REFUSED** @`1ec5ade3f5` (section contamination, four regions) -> amended @`371286cf78`.
2. **L4-R delta REFUSED** @`079e7d0a3b` (FWD-15 not verbatim) -> amended @`421489a8d5`, then
   **SIGNED** @`0147a1b924`.

⭐ **BOTH REFUSALS WERE CORRECT AND THE SECOND FOUND WHAT THE FIRST STRUCTURALLY COULD NOT.** This
seat pre-reviewed its own half and DISCLOSED one contaminated region; the section had FOUR, and the
review closed *"recheck the whole section boundary, rather than only the disclosed blockquote."* The
second review then found three FWD-15 word-level deltas that **pre-dated** the first amendment --
the first refusal had said in terms it was *"a sufficient refusal, not a certification of the
remaining criteria."* **A self-disclosure is not a self-certification, and a refusal that stops at
the first sufficient ground is not a clean bill on the rest.** The reviewer also caught a stale
count the author had carried a full version ("Thirteen outcomes" where fourteen are `EXERCISED`).

## 2. ACTS TAKEN IN THIS SEAT'S OWN LANE (no TO cut, no seat dispatched, nothing applied)

| act | commit | note |
|---|---|---|
| ENDPOINT decontamination | `371286cf78` | history/seat-names moved to the **PREAMBLE** -- `half_of_section` returns `None` for pre-heading text, so it is in NEITHER half. Chosen over s.7 PROVENANCE precisely to avoid re-opening the CRO's signature |
| FWD-15 restored verbatim | `421489a8d5` | checked on WORDS with whitespace normalised (the carriers wrap differently); difflib printed zero differing tokens |
| S5 remedy discharged | `3e35a50e74` | s.5 + S6 measured-by stop carrying an absent-bucket premise |
| **withdrawal of this seat's own overclaim** | `b9723b43e5` | see s.3 |
| surprise row `S6` | `65ab345826` | see s.4 |
| **L10 round-4 grade** | `959ba3e947` | `ledger/ROUND_ANALYSIS.round4.md` |

**L10, round 4: 2 PASS / 0 FAIL.** `rc-19` AC4 and `rc-20` AC4 both pass. **Round 3's single FAIL --
`C-S16`, the consumer wiring -- is CLOSED**, with `C-S19`/`C-S20` clocks closed beneath it. The
slug's own non-claims are carried VERBATIM into the analysis rather than softened: no historical PDF
regeneration, no analyst exercising a deployed UI, no FWD REALIZED. **0 of 15 FWD newly REALIZED,
and that is correct** -- rounds 1-4 are pre-surface correctness and no surface exists.

## 3. THE CORRECTION THIS SEAT TOOK AGAINST ITSELF

`3.0.0_SA_CVO~Z`'s sign review caught an unsupported claim **introduced by this seat's own S5
amendment**: s.5 had said the brief's PART V ABSENT measurement *"was correct when taken."*
**Nothing measured that.** The 15:44Z and 15:55Z head-bucket reads establish the PRESENT state and
say nothing about what was true earlier; `C-S23` expressly left the original reading's correctness
UNRESOLVED. It sat one line from two genuinely measured reads and **borrowed their credibility** --
which is what made it dangerous rather than merely wrong, and it was generous-sounding rather than
obviously false. Withdrawn @`b9723b43e5`, with the withdrawal NAMED rather than the earlier
assertion silently edited away.

⭐ **SEQUENCING WAS THE WHOLE TRICK, TWICE.** Both the S5 amendment and this withdrawal touch
BRIEF-half sections. Each was taken while the brief half was **already owed**, and each was checked
against the ratified hash BEFORE writing: `4eb997ed71ee` -> `4eb997ed71ee`, unchanged. An edit that
strayed into the ratified half would have invalidated a CVO signature that landed four minutes
earlier. **One half moves; the other stays still. That is a choice made before the write, not
discovered after it.**

## 4. `AMGT_RESAPP-Z-S6` -- the false green, and what its disarm may NOT claim

The L4-R gate reported the brief half `SIGNED current` **while its bytes had moved**, because
`prd_signoff_lib.evaluate()` falls back to `prd_version` equality for any record lacking a
`half_hash`. Measured live on this project; the discriminator is that the CVO's hash-bearing record
correctly read STALE **in the same command run**.

⛔ **IT WAS NOT ACADEMIC AND IT ALMOST FIRED.** `2.0.0_SA_COO~ZZZ` disclosed that its 20-minute
`/drive` loop's FIRST instruction was *"if prd-signoff status reads ADMITTED, cut the surface round
at L5."* The ratified half signed ~40 minutes after the row was filed. **That tick would have cut
round v5 against an unreviewed brief half, and LIMB 6 would not have caught it, because LIMB 6 reads
the same false green.** The loop is now guarded on ADMITTED **AND** a matching `half_hash`, checking
every `4.0.0_SA_CRO*.json` -- the detail that matters, since the re-sign lands as the LANE file
while the stale record is the BASE file. **That guard now passes, and it passes for the right
reason.**

**The instance condition is met; the row is still ARMED and its disarm is `4.0.0_SA_CRO~Z`'s.**
Scoping raised BEFORE the disarm row is written, because a blanket disarm would record something
false:
1. **The library is unchanged** -- the legacy branch still fires for any record without a hash.
2. **The defective carrier is still present.** `4.0.0_SA_CRO.json` remains, old-format, SIGNED,
   v0.4. It is SHADOWED only because `evaluate()` takes the newest by `signed_at` and it has none.
   ⚠ **The instance was fixed by ADDITION, not removal** -- remove or rename the lane file and the
   base record silently decides on `v0.4 == v0.4` again.
3. **The estate-wide class is uncounted.** This project alone holds 2 old-format records of 3.
**Disarm the INSTANCE, keep the CLASS routed.** A row reading "S6 disarmed, the gate is fixed" would
be the same false-green shape one level up.

## 5. POSN_ASTTAX -- `/canonical-flow --report-only`, per Andrew's directive

Andrew-direct ~15:4xZ: *"make sure the relevant agents have run /canonical-flow to ascertain
mid-stream position."* Run on the half of the scope this seat had only counted.

```
LOCATE   home org/missions/D4/POSN/POSN_ASTTAX   placement SITEZ   status active   dep_stage EXECUTING
         PRD v0.5 @66ded3a0c5 ADMITTED (both halves current)   decomps: base + round1 + round2
         TOs 8 -> 2 terminal / 6 staged   proof instances 2 VALID at HEAD (WK~1 S1A-1, WK~2 S6-1)
         worker worktrees 3 (wk-posn_asttax-2-4 / -2-5 / -2-7 @fd9f8ba9a4)
         unfinished edits NONE   stash NONE   ledger: round1 + round1-addendum   round-2 slug ABSENT
MEASURED limb: L7 -- round 2 IN FLIGHT.   claimed vs measured: AGREE (dep_stage EXECUTING)
CLASS    none -- in flight, not limbo
ROLE     next limb L7 is NOT MINE -> 2.0.0_SA_COO~Z
ACT      none (report-only); nothing routed, nothing touched
```

⛔ **THE THREE WORKTREES ARE NOT `ORPHAN-WORKTREE` AND SAYING SO REQUIRED A DISCRIMINATOR.** A
worktree with no merged proof instance looks identical whether its worker is alive or died. The
discriminator is not the worktree -- it is `2.0.0_SA_COO~Z`'s own live working summary, which names
the spawns individually: *"Wave 2 spawned: AT2-s-7/~4, AT2-s-5/~3, AT2-s-4/~8 in cone worktrees.
AT2-s-1 held last (shares lambda_function.py with s-7's reads)."* **Live workers. Classing them
orphans would have manufactured a false alarm into another seat's live round.** Independently
reached by `4.0.0_SA_CRO~Z` in its own pass.

⛔ **`C-RETAG-SAFETY` CARRIED FORWARD, UNCHANGED AND LOAD-BEARING.** Fixed-key dicts blank the page
for all four partner firms on a retag; NOT latent, VXX is already held.
**Order: (0) harden the generator, (1) fix management_style, (2) verify the asset_class chain,
(3) THEN retag.** `TO-S2-1.retag-the-hedge-bucket` is in the staged set -- that is step (3), and
steps (0)-(2) are not all done.

## 6. SCOPE COMPLIANCE -- two real defects surfaced and DELIBERATELY NOT WORKED

Andrew ~15:4xZ: AMGT_RESAPP and POSN_ASTTAX, *"no other work aside from those."*
- **`spawn-agent.ps1` has no codex branch** (measured: 304 lines, ZERO "codex"/"ajb2" occurrences),
  so a codex seat on a space-containing checkout fails SILENTLY -- right command line, right marker,
  zero children. Root-caused by `0.0.0_AB_MSTR~Z` from captured stderr. Two hypotheses DISPROVEN and
  recorded so nobody retries them: `-NoProfile` codex resolution, and the wt-vs-Start-Process
  transport.
- **`prd_signoff_lib` legacy branch** (row S6). A one-line change retroactively invalidates every
  old-format signature in the estate, and **nobody has counted that denominator.**
Both SURFACED and ROUTED, neither edited. Not forgotten -- recorded here and in the channel.

## 7. COMPLETION TEST

**NOT DONE -- 0 of 2 projects `status: complete`** (denominator 2, read from the register, not
declared). `AMGT_RESAPP` active/EXECUTING, round 5 uncut, 28 of 28 orders terminal from rounds 1-4.
`POSN_ASTTAX` active/EXECUTING, L7 in flight. Both REACHABLE; no UNREACHABLE member, so no
HELD-AT-STOP branch. **Open calls at Andrew: 0.**

## Compiler Tools

`prd-signoff.py status` (both projects, re-read at each decision point) · `prd_signoff_lib.half_hashes`
+ `evaluate` read at source (the instrument that found S6, and the one that proved the brief half never
moved during the contamination amendment) · `.tools/aws s3api head-bucket` with a 404 negative control
(S5, independent of the CVO's read) · `comp-find --name` / content with printed denominators ·
`comp-read --enumerate` · `.tools/directives-check.py --json` · `agentbus-sqs.sh device` ·
`safe-commit.sh -F` with Write-tool-authored msgfiles · `git log -1 --format` / `ls-remote` /
`branch -r --contains` / `merge-base --is-ancestor` each with a negative control ·
`get_agent_status` / `get_live_agents` / `ack_messages` (READ clock: 21397, 21401, 21405, 21409,
21422, 21426, 21434, 21440, 21443).

**Push state:** LOCAL at write time, MEASURED -- `ls-remote origin refs/heads/SITEZ` last read
`65ab345826`; `959ba3e947` and `b9723b43e5` were LOCAL at that read. `0.0.0_AB_MSTR~Z` pushes
origin/SITEZ on Andrew's word tonight; this seat does not push.
