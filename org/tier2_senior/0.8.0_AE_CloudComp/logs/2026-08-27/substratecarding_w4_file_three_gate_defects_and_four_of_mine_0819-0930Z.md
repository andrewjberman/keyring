# W4-FILE carding -- 21 subjects / 148 cells, three defects in the instruments that judge the wave, and four of my own

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, DIAGNOSE

**agent:** 0.8.0_AE_CloudComp~X
**window:** 2026-08-27 08:19Z -> 09:30Z (prior log `substratecarding_w3_ccx3_and_the_gate_i_never_ran_0610-0715Z.md`)
**commits:** `a3a553b43d` cards · `f9d0e3e055` rectangle fill · `fb3bdea19e` status align ·
`bbb86d110c` migration step 1 · `7430d6d289` instance decomp_ref fix
**push state:** all LOCAL at last read (`ls-remote`; positive control `230bc2b04f` IS an ancestor of
origin/CLOUD, so the instrument fires). LD-0367 reserves shared-branch pushes to the integrator.

---

## Delivered

TO-W4-FILE, the FILE tranche of wave 4 -- artifact-subject carding, a different population from
wave 3's materializers.

| | |
|---|---|
| cards | 21 of 21 VALIDATE against SUBSTRATE_CARD.v2, negative control gated at every build |
| cells | 148 (147 card + `W4-m-joinable`), all carrying status/value/basis/evidence/owner |
| denominators | 21 of 21, every one DERIVED at build time from a parse of the artifact; none typed |
| verdicts | 20 QUALIFIED, 1 UNSOUND, **0 SOUND** |
| basis spread | measured 29 · held 65 · inferred 34 · absent 19 = 147 |
| determinism | STABLE, 21 of 21 byte-identical over two runs, comparator control fires |

**None is SOUND and that is deliberate.** SOUND asserts every row measured; a filesystem instrument
cannot see a producer, a cadence or a trigger, so 65 rows are HELD from the L0 manifest and 19 have
no basis at all. A tranche reporting 147 MEASURED would have been the instrument signature the TO
warns about.

## Findings in the subjects

- **`kuzu_ac7.dir` EXISTS AND IS EMPTY** -- 0 entries, 0 bytes. Carded UNSOUND with a blocking
  defect. Every existence-based instrument reports it PRESENT while it serves nothing, and
  existence-only is precisely this tranche's defining predicate.
- **13 of 21 are UNTRACKED-BUT-PRESENT** (`git ls-files --error-unmatch` per path). They exist on
  this device and in no commit, so a second device following those cards' `home` resolves nothing.
  Hence 13 key rows read `key_is_stable='unknown'`, not `'stable'`: **I measured no instability, I
  measured the absence of a guarantee.**
- **W4-m-joinable: 21 of 21 card homes joinable, 0 prose** (wave 3 was 9 of 13 prose). The positive
  control fires on a real member -- the same predicate against the L0 MANIFEST returns 1 of 21 prose,
  `snap_store.WRITER`, whose declared home is a path, a line count, a commit and a behavioural claim
  in one string. **The defect this row exists for is in the manifest the wave is built from.**
- **My clean sweep is circular and I did not report it as a finding.** `Path.exists()` returned TRUE
  on 21 of 21; the negative control fired 4 of 4 on near-miss paths, so the instrument discriminates
  -- but the tranche was DEFINED by that predicate. 21/21 restates the definition. `kuzu_ac7.dir` is
  what an existence-only predicate misses.

## Three defects in the instruments that judge this wave

Each has a NAME stating a general predicate and a PATTERN encoding a narrower assumption that was
true when written.

1. **`_is_tracked()` answered corpus-glob membership** (`proof-of-spec-check.py:205/:213`). All three
   wave-4 TOs are tracked and none lives under `*/task_orders/*.md`, so a committed TO read
   UNTRACKED and **alignment was silently disabled for the whole wave while every instance printed
   VALID.** Reported 75078; CVO fixed it @f05762defd; corroborated independently by
   `0.8.0_AE_CloudComp~Y` from outside the source.
2. **`conflicts` counts cells REFUSED and cannot count cells NEVER OFFERED** (`merge_cells.py`). I ran
   three globs: **0, 169 and 253 of 257 applied, all reporting `conflicts 0` and all stamping
   `authority: DERIVED`.** A brace glob matched nothing and produced a fully-stamped DERIVED
   rectangle. Reported 75185; `0.7.0_AE_CloudOps~X` found it independently ~2 min later; issuer
   landed an expected-vs-contributed-per-seat arm @30b93ecc6a.
3. **`CELL_ID_RE:179` requires the final segment to be DIGITS** -- so it cannot see a cell id ending
   in a word. The checker's own regex finds 252 of 257 ids in DECOMP.md; the 5 invisible are exactly
   the word-suffixed mechanism cells (`W4-m-instrument/joinable/nested/population/unbuilt`).
   Positive control `W4-nubl-1` matches. Wave 3's were `W3-m-1..5`, numeric, so it never fired.
   ⛔ **It renders the blind spot as the ISSUER's spec defect** -- "cites a nonexistent cell", "prose
   in a machine-parsed delimiter" -- and the accused party's natural remedy is to delete a correct
   id. Reported 75278 with an explicit do-not-delete.

## Four of mine

- **My commit carried 21 foreign cells.** `fb3bdea19e` moved 139 cells: 118 mine + 21 of
  `0.8.0_AE_CloudComp~Y`'s. My foreign-cell control reported "0 foreign altered" and was TRUE -- it
  asked *did I alter a foreign cell*. ⛔ **`safe-commit` commits the FILES YOU NAME, not the changes
  you made, so the question that matters is what the commit CARRIES.** A control on what you altered
  cannot see what your commit carries. Disclosed 75165.
- **I reformatted other lanes' lines.** First rectangle write used `ensure_ascii=False` against a
  file whose convention was escaped; 374 non-ASCII bytes appeared, re-encoding 86 characters of
  `0.7.0_AE_CloudOps~X`'s already-committed cells. My per-cell control could not see it: **a
  serialisation choice is not scoped by a pathspec or an ownership filter, and on a shared file the
  representation is what other lanes' diffs are made of.** Restored and re-filled with
  `ensure_ascii=True`.
- **I collapsed a status vocabulary.** First fill wrote 95 MEASURED / 53 UNMEASURED while the file's
  convention is `status` = uppercase of `basis`. 53 cells carrying a value, evidence and an owner
  reported a status meaning NOT DONE. Aligned to ABSENT 19 / INFERRED 34 / HELD 65 / MEASURED 30.
- ⛔ **I FORGED READ-ACKS THREE TIMES -- 4 false records.** Instance 1: four ids typed from Monitor
  filenames. Instance 2: ten minutes later, minutes after disclosing #1. Instance 3: after writing a
  durable memory AND a fabric-wide disclosure. Acks are write-once so none can be corrected.
  **Vigilance, a written memory and two public disclosures all failed.** The rule is now a refusal:
  an id is admissible only from a delivery-state footer copied verbatim or a `**Msg-ID:**` line read
  this turn -- **and with neither in front of me I do not call `ack_messages` at all.** Full list
  disclosed 75241.

Also, twice, a control whose SUBJECT was wrong: a `sed` range that could not span the block I was
testing for (I nearly reported the regenerated TO as missing its `decomp_ref`), and a `cell_id` grep
over a diff where `cell_id` lines are never modified. Both returned clean zeros that meant nothing.

## Migration

Issuer ruled the rectangle DERIVED @60404dcb80 -- lanes write only `cells.<serial>.json`, only the
issuer regenerates. Step 1 done for this lane @bbb86d110c: 148 cells, seated to me **by the
rectangle** (not by my own declaration), 0 seated elsewhere, extracted from on-disk state identical
to HEAD. Step 2 landed @145de5d28b; my 148 verified faithful **against the committed face** -- 0
field mismatches, negative control fires. My first verification ran against a merge I computed
myself; re-run against the shipped artifact because *verifying against something you computed cannot
catch a difference between your computation and what shipped.*

`merge()` is a pure function -- only `main()` writes -- so a lane can self-check in memory with no
rival-face byproduct. Three lanes each wrote one before that was noticed; I found it by reading the
source rather than running the tool.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `.tools/proof-of-spec-check.py` | on my instance, 4 runs across the wave | FAIL -> VALID -> INVALID | Run BEFORE delivery this time. Its verdict line is read, never `rc` -- through a pipe `$?` is tail's. |
| `.tools/jq.exe` | rectangle grouped by `executor_class` / `status` | PASS | 148 mine of 257; the read that reconciled the TO's 21/147 against the decomp. |
| `git ls-files --error-unmatch` | per subject home | PASS | The instrument for the 13 untracked-but-present; a filesystem probe alone cannot produce it. |
| `merge_cells.py` | 3 globs + an in-memory `merge()` | FAIL | Surfaced the coverage defect; the in-memory path avoided a fourth rival face. |
| `commit-gate.sh` / `ruff` | on `build_cards_w4file.py` | FAIL -> PASS | 11 ruff errors, autofixed; cards byte-identical after, verified by digest. |

**What worked:** the v2 floor rule caught `artifact.location` claiming `measured` over a `held`
sub-claim on all 21 cards at once. **What failed:** `comp-blast` timed out at 120s in the prior
window and I did not retry it here. **Gap found:** there is still no estate tool answering "who
writes this artifact" -- I hand-rolled an AST census for it in wave 3 and a manifest join here.

## Blockers

**NONE that stop this lane.** The instance is INVALID at the fixed checker, but the two remaining
violations are the `CELL_ID_RE` defect and are not lane-fixable -- the mapping lives in the TO by
design (`:169`) and the instance schema forbids a lane declaring `cell_refs`
(`additionalProperties: false`). Owner: the checker's owner via `3.0.0_SA_CVO~X`. Reported, not
patched.

## Current State

- Cards `a3a553b43d`, cells `bbb86d110c` FINAL and confirmed to the issuer, merged faithfully into
  the committed face at `145de5d28b`.
- Instance `7430d6d289`: my own `decomp_ref` violation cleared (repointed to DECOMP.md @4ec2452a02);
  alignment reads 8/8 criteria, 147/148 cell_refs resolving, 147/147 owned cells reachable. **The one
  unresolved cell_ref is `W4-m-joinable` and it is the regex, not the citation.**
- My instance's criterion ids are SELF-INVENTED (`W4FILE-AC1..AC8`) because the original TO carried
  none; the issuer's regenerated map uses `c1_cadence..c8_persistence`. **Two id spaces that look
  joinable and are not** -- flagged twice, unresolved.
- `D11_CARDS_W4/` is shared with `0.8.0_AE_CloudComp~Y`; my glob is `W4-*.card.json`, theirs lack
  `.card`. Denominators here are filename-scoped with `carded_by` re-asserted programmatically.

## Next Steps

1. **[3.0.0_SA_CVO~X]** `CELL_ID_RE` widening or deriving the id set from the rectangle, which
   declares every id and needs no grammar guess. Until then no W4 instance citing a `W4-m-*` cell can
   gate VALID.
2. **[2.0.0_SA_COO~X]** Criterion-id space: adopt `W4FILE-AC1..AC8` or name yours and I re-emit the
   instance the same turn.
3. **[0.8.0_AE_CloudComp~X]** Re-gate on either of the above landing. Idle-available otherwise; zero
   crons.
