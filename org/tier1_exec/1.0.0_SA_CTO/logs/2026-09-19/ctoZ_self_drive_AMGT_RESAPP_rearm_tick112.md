# /self-drive AMGT_RESAPP -- ticks 102-112 (1.0.0_SA_CTO~Z), 2026-09-19 ~13:1xZ - ~15:5xZ

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_13xxZ_SELF_DRIVE_AMGT_RESAPP_REARMED.md`
**state: ARMED.** Cursor from the last log's COMMIT author time: `7d4e261a11` @ 2026-09-19T13:15:10Z.

⚠ **AND THE LOG CADENCE ITSELF WAS MIS-READ FOR THREE TICKS.** The rule is *delta OR the 6-tick floor, whichever
comes FIRST*. This seat took three substantive acts after 13:15Z and each tick said "goes in the next log at the
floor" -- treating the floor as the trigger when DELTA is the primary one and the floor is only the backstop for a
quiet loop. The acts were never at risk (all committed), but a log deferred on a misread rule is the same class as
a cursor re-typed from prose: **the rule was read once correctly and then paraphrased downstream into something
weaker.**

## Acts, in order

| what | commit / receipt |
|---|---|
| REFUSED the chain E `rk-49` COO half as first cut | msg 23886/23887 |
| SIGNED the re-cut half after being corrected on vintage | `9d84ea19f1` |
| RAISED a live credential staged for shared history | msgs 23894/23895/23896 |
| RULED the `comp-secrets --reveal` contract (row `W50-S4`) | this commit |
| corrected my own broker summary, twice | set_summary |

## 1. THE `rk-49` PAIR -- a refusal, a vintage error that was MINE, and a flag finding

`2.0.0_SA_COO~Z` asked for the CTO half before the cell's live write. This seat **refused** on five findings. **THREE
WERE WRONG, AND WRONG BECAUSE I READ THE WRONG PLANE**: I measured `enrich.py` at SITEZ HEAD, while the act runs on
`wk-amgt-14-50` -- **where `rk-49` IS the cell that retires the `domains.json` gate.** I cited the very defect the
cell exists to fix as though it were the cell's behaviour.

⛔ **THIS FILE'S OWN HEADER ALREADY CARRIED THE RULE I BROKE** -- *"where a claim depends on code the cell has yet to
write, mark it UNVERIFIED (diff not yet authored)"* -- written by this seat, for this chain, one cell earlier.
Rule 22 GRAIN at the vintage claimed. **A refusal is where a wrong vintage does the most damage, because it arrives
dressed as rigour.** Owned in the half at `9d84ea19f1`, not in a message that scrolls.

⭐ **AND `3.0.0_SA_CVO~Z` MADE THE SAME ERROR INDEPENDENTLY, WITHIN THE HOUR** (its section 4q): it verified the same
refusal at HEAD, and recorded that this is *"the same HEAD-vs-branch class as its own Z-S178, committed 12h later"* --
its own row, naming the class, did not stop it. **4p is marked wrong in place, not amended away.** Two seats, one
order, one hour. This belongs in the round-14 analysis: the HEAD-vs-branch error is not carelessness, it is which
plane a seat habitually reads, and writing the lesson down did not prevent the repeat.

**TWO findings survived and the re-cut took them:** there is no `FAILED` branch (an exception propagates and that key
is NOT rewritten), and a SKIPPED name's officers ARE stamped `NOT-ATTEMPTED`.

⭐ **AND ONE NEITHER HALF HAD NAMED, which decides whether the act writes at all.** The order names the act as
`enrich.main --enrich-only --skip-pool`. **Run exactly that and NOTHING is written.** On that path
(`enrich.py:1000-1017`): dry-run returns; `validate()` failing returns BLOCKED; then
`if not args.write_pool: "DRY: nothing uploaded"; return 0` -- and only past that does `write_document` land the
dated key. `--skip-pool` acts afterwards and governs only `_pool`. **So `--write-pool` gates the DATED KEY and
`--skip-pool` protects the pool -- the flag's name says the opposite, and the run exits 0 with a `DRY:` line, so a
worker following the literal command reports a completed act with zero writes.** `3.0.0_SA_CVO~Z` re-derived this on
the branch at section 4r, which makes it two independent reads rather than one repeated.

## 2. THE ACT WROTE NOTHING, AND THE PAIR IS WHY

`rk-49`'s live arm ran under the completed pair and **wrote nothing**: `validate()` refused CAT and CSL on
`'ceo_profile' is a required property`, Keyence was withheld after an independent pre-check proved the identical
block. **3 of 3 keys byte-identical pre=post, `_pool` ETag equal, 0 credits, ledger CLOSED with four legs proven.**
The block is `rk-48`'s schema requirement whose only writer is `rk-48`'s live arm -- refused on the Bright Data word.
So `rk-49` is SEQUENCED BEHIND `rk-48` and both wait on the same word (`Z-S180`).

⭐ **The pair constrained the REMEDY, not just the act:** `2.0.0_SA_COO~Z` declined both workarounds -- no schema
relaxation, no placeholder `ceo_profile` -- because either is a served-content change outside the signed chain E
pair. That is what a never-widen half is for, and it held without anyone invoking it.

**RECLASSIFICATION OF THIS SEAT'S OWN CARD:** the Bright Data word now gates **five criteria across two cells**, not
three across one. The CVO's quality-vs-count partition still holds -- both cells close by construction -- but the
magnitude inside "quality" doubled.

## 3. ⛔ A LIVE CREDENTIAL STAGED FOR SHARED HISTORY -- raised, contained, carded

Row `AMGT_RESAPP-Z-W50-S4` (this seat's to disarm) makes a correct finding about `comp-secrets`' output shape and
demonstrates it by **pasting the revealed `value:` line verbatim**. Measured before raising: present on
`wk-amgt-14-50` only; ABSENT from the shared tree (SITEZ carries only a mention inside `Z-S180`'s notes); ABSENT from
origin (`ls-remote` reads `047aee5478`). One local branch, undrained, unpushed.

Raised at msg 23894 with three asks: do not drain, hold pushes, and -- the part that matters --
**redaction is necessary and NOT sufficient**, because the blob is already in that branch's commit history and an
ordinary merge carries every commit. Rotation named as the sound remedy, **named and not performed**: it is an AE act
and Andrew's word.

`2.0.0_SA_COO~Z` executed all three within twelve minutes, measured the blast radius independently (one committed
file, three commits' trees, one worktree copy, 0 on SITEZ, nothing pushed), halted the re-grade worker, and carded
rotation to Andrew with REC yes plus a history rewrite regardless of the answer.

⭐ **THE IRONY IS THE LESSON.** `comp-secrets:248-251` guarantees its logger records the command NAME and never
stdout. **That guarantee held perfectly and was defeated one layer up, by a document ABOUT the tool quoting the
stdout the logger was careful never to touch.** No comp-tool change would have prevented it. **No blame on the
worker:** it found a real defect, refused rather than routing around it, charged nothing, and filed the row it was
told to file -- and nothing in a row's schema says *redact a quoted credential to its shape first.* That gap is
carded to `3.0.0_SA_CVO~Z`, which owns remediation rows.

Ruled separately at `deliverables/CTO_RULING_COMP_SECRETS_REVEAL_CONTRACT_20260919T155xZ.md`: the contract is the
four-line block; the extraction idiom is `grep '^value:'` + `sed` + `tr -d '\r'`; and **`--json --reveal` silently
returns TEXT** (`:236`), a defect proposed for a quiet window and deliberately NOT implemented mid-round on a shared
secrets CLI while a dozen workers run against it.

## The round, measured from the ORDER FILES

Line-anchored over `31 <= n <= 61`, denominator printed every read: **23 -> 25 of 31**, 6 pending
(`32, 37, 49, 50, 51, 52`). Drains this window: `rk-40` (three issuer amendments, four worker rows) and `rk-36`.

⚠ **8 pending against 1 unmerged worker branch is NOT seven stalled cells** -- the COO hands a worker its next order
rather than spawning a branch per cell, so the branch list LAGS wave state and the issuer's own log leads it. Two
commit gaps (21 and 46 minutes) were read as MOVING and both reads were right: the broker showed three workers
writing within two minutes, and later a worker mid-live-act with its ledger open.

## Scope and completion

AMGT_RESAPP: active, EXECUTING, PRD v0.13 ADMITTED. COMPLETION TEST: **NOT DONE -- 0 of 1 projects complete.**
**Open at Andrew: TWO** -- the bucket/tenancy shape (blocks TERMINALITY; `rk-32` + chain P held, builder refuses
under Rule 30) and the Bright Data per-use word (now five criteria, two cells). **A THIRD is at Andrew via the COO:
rotate the Lusha key.** Nothing stalled in any tick of this window; nothing routed to `0.0.0_AB_MSTR~Z`.

## Compiler Tools

`git worktree list --porcelain` + per-tree `ls-tree` union (NEVER-2), line-anchored status reads,
`git merge-base --is-ancestor` per branch, `git show <branch>:<path>` for branch-vintage source reads,
`rev-parse --show-toplevel` beside every per-worktree read, `sha256sum` on a counterpart half, `comp-find`,
broker `get_agent_status` / `get_live_agents` / `send_message` / `set_summary`, inbox Monitor.

-- `1.0.0_SA_CTO~Z`
