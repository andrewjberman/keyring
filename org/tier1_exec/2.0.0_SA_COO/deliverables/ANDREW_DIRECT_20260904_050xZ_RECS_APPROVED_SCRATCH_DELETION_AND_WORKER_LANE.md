# ANDREW-DIRECT 2026-09-04 ~05:0xZ at the `2.0.0_SA_COO` terminal — "recs approved" on /open-calls (2 cards)

**Verbatim, in full:** `/open-calls` (the skill, run at this seat) -> the two cards below -> **"recs approved"**.

Recorded by `2.0.0_SA_COO` the same turn; broadcast the same turn to `1.0.0_SA_CTO`, `3.0.0_SA_CVO`,
`0.0.0_AB_MSTR` and `4.0.0_SA_CRO`. Push state at record time: **LOCAL**; origin/CLOUD @`351f309e0a`
(ls-remote read this session; pushes on Andrew's word, LD-0522).

He ran `/open-calls` at several terminals in the same window. This record is **this seat's cards only**.
The CTO's cards and the CVO's cards are recorded at their own seats
(`ANDREW_DIRECT_20260904_0458Z_...` and `ANDREW_DIRECT_20260904_050xZ_A_FOR_BOTH_...`).

## The frame he approved, verbatim

```
OPEN CALLS AT ANDREW — 2.0.0_SA_COO (2 calls, 2026-09-04 05:05Z)

BLOCKING (something waits on the word)

+-- CALL 1 of 2 ------------------------------------------------------+
  **Does the worker lane grant proceed now — (a) yes, or (b) hold?**
  Item 3 of your eight is NOT PASSED on this alone: no lane admits a
  0.9.0_WK_* serial, so every worker commit on a real file is an override.
  ----------------------------------------------------------------------
  **REC — (a), proceed.** The toolkit works: a worker built and proved real
  code tonight; the only thing it cannot do is commit without an audited
  override, which is precisely the acceptance test that failed. The CRO
  carries the wider question of whether the five new gaps are inside "right
  now"; this card asks only about the one that blocks a mechanism you named.
+----------------------------------------------------------------------+

+-- CALL 2 of 2 ------------------------------------------------------+
  **Do the 27 root scratch files get deleted — (a) delete, or (b) keep?**
  Last unswept bucket of the LD-0532 cleaning run. 16 `.runtmp_*`, 6
  `scratch_*`, plus `hit_tmp.txt`, `nonpyc.txt`, `.rules.txt`, a file named
  `-`, and a directory whose name begins with a double quote.
  ----------------------------------------------------------------------
  **REC — (a), delete.** They are run temporaries from dead seats, none is
  referenced by anything tracked, and the CVO independently classified them
  as deletion candidates. Deletion is the one act I will not take on my own
  read. I will list every path before removing anything.
+----------------------------------------------------------------------+
```

## RULING 1 — the worker lane: HIS WORD HERE COMPOSES WITH, AND IS NARROWED BY, HIS WORD AT THE CTO

This seat's card asked a **timing** question — proceed now, or hold. The CTO's card, put to him at
~04:58Z (fourteen minutes earlier), asked the **shape** question and offered `(a)` admit workers to every
Tier-2 lane versus `(c)` the task order is the grant. He approved the CTO's REC of **(c)**.

**So the composed reading, which this seat applies and does NOT adjudicate wider:** proceed now (this
seat's card), in shape **(c)** (the CTO's card, which is the more specific ruling on the same gap from
the same word). **This seat is NOT treating its own `(a)` as authorising a lane enumeration** — the CTO's
record is explicit that no lane in `.owned-paths.yaml` enumerates a worker and none will.

> ⚠ **Surfaced, not adjudicated:** if anyone reads this seat's `(a)` as ordering a lane grant, that
> reading conflicts with RULING 1 at the CTO. This seat defers to (c) as the narrower and more specific
> and says so here rather than resolving it silently. One word corrects it either way.

**RULING 1 AS THIS SEAT WILL EXECUTE IT.** A worker serial `0.9.0_WK_<CODE>~<n>` is admitted to exactly
the paths that a task order under project `<CODE>`, issued to that serial and non-terminal at HEAD, names
in its `<paths>` block — and nothing else.

- `1.0.0_SA_CTO`: the resolver limb in `.tools/owned-paths-validate.py`. **Not this seat's.**
- `0.0.0_AB_MSTR`: the registry stanza declaring the policy (SoD — the grantee never writes its own grant).
  **Not this seat's.**
- **`2.0.0_SA_COO` (this seat, DONE this turn):** `/dispatch`'s pre-spawn census now reads the same rule.
  Step 4 is rewritten: the `<paths>` block is a **PERMISSION, not a hint**; a surface left out of the
  order is a surface the worker is REFUSED on, exactly like a lane refusal, and a worker cannot ask for
  one — it files a row and stops. The state is recorded honestly as DESIRED-not-APPLIED: until the CTO's
  resolver and MSTR's stanza land, a worker's commit on a real surface is still refused and still needs
  the audited, singular `GIT_COMMIT_AUTHOR_OVERRIDE`, which is how v3's first drain actually committed.

## RULING 2 — the 27 root scratch entries: EXECUTED, with ONE DEVIATION AND ITS REASON

Measured fresh at execution (05:04Z, HEAD `160b1fc512`): **27 root-level untracked entries, all FILES.**
⚠ **This seat's own card was wrong in one detail and the record says so:** the card described "a
directory whose name begins with a double quote". No such directory is in the root-level set; that entry
is a second-level path counted in an earlier sweep. Nothing was deleted on the strength of that phrase.

**26 DELETED. 1 PRESERVED, NOT DELETED.**

**The preserved one, and why the rec's premise did not hold for it.** The file literally named `-`
(11,691 bytes) is **not scratch**. It is a **49F gold-chain production run log for date 2026-09-02**,
carrying stage-by-stage results and the line *"READ-BACK OK: 8,653 rows, 38 cols == built frame. THE
FIRST GOLD-GRAMMAR WRITE IS LANDED AND VERIFIED."* — almost certainly an accidental `> -` redirect of a
real run. This seat's recommendation to him rested on *"run temporaries, none referenced by anything
tracked"*, and **that premise is false for this file**, so it was not deleted on the strength of it.
Moved intact to the session scratchpad as `PRESERVED_49f_chain_runlog_20260902.txt`. **Andrew's word
covers deleting scratch; it does not cover deleting a production run record this seat had mis-described
to him.** If he wants it gone, one word.

⭐ **A second measurement error, recorded because it nearly mattered:** this seat's listing reported `-`
as "0h old". It is ~13h old. A filename that is a bare dash breaks `stat`, which parses it as an option
— the same class as every other leading-dash hazard. **The file that was hardest to measure was the one
that should not have been deleted.**

**The two that were checked before removal rather than assumed:**
- `mdpf-gold-lambda.BUILD_MANIFEST.json` — 28 corpus hits, so the "referenced by nothing" premise looked
  false. Resolved: every reference points at the **canonical, TRACKED** copy at
  `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/mdpf-gold-lambda.BUILD_MANIFEST.json` (6,379 bytes,
  differs from the 5,645-byte root stray), and a 2026-08-14 rail log shows an interrupted `mv` of this
  exact name — the root copy is a superseded leftover. DELETED.
- `etf-positioning-producer.BUILD_MANIFEST.json` — 0 hits. DELETED.

**Manifest of all 27** (sha256, bytes, mtime, name) written to the session scratchpad as
`DELETED_ROOT_SCRATCH_20260904_manifest.txt` before any removal, so the removal is reconstructible-by-name
even though the bytes are gone.

**VERIFIED AFTER:** root-level untracked **0 of 27**; total untracked 241 -> 213; **no tracked file
touched** by the removal.

## Scope

His word answers **these two cards and nothing else** — not the push hold (LD-0522), not the CLDGRPH
L8–L10 restart ("call b we will wait on this"), not the override-audit carrier (gap 4), and not whether
the five new gaps are inside "the mechanisms right now", which `4.0.0_SA_CRO` carries.
