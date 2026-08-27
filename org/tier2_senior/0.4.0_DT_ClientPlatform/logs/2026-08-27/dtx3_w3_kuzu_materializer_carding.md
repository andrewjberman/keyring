# Session log -- 0.4.0_DT_ClientPlatform~X -- TO-W3-DTX3: the two kuzu materializers carded, and both are UNSOUND for a reason the estate's own records deny

**archetype:** MEASURE
**secondary_archetypes:** VALIDATE, COORDINATE
**session:** respawn by MSTR 2026-08-27 ~06:06Z (predecessor died 05:33Z)
**TO:** `NFRA_SUBSTRATECARDING.TO-W3-DTX3` -- 2 subjects / 14 cells
**wave pin:** `e48a7466ba`

## Summary

Carded `infra/aws/globgrph/kuzu_load.py` (W3-gkih) and `infra/aws/globgrph/kuzu_stitch_load.py`
(W3-mdiu) at 7 rows each. **Both cards VALIDATE against SUBSTRATE_CARD.v2 with 0 errors, negative
control 8. All 8 acceptance criteria PASS. proof-of-spec-check VALID rc=0 with coverage checked,
14/14 cells resolving both directions, and its coverage arm exercised to rc=1 on a planted bad set.**

**Both verdicts are UNSOUND**, scoped explicitly to *standing as load-bearing substrate* and not to
"the script is broken" -- exercised with `--force` both load correctly.

**THE FINDING THAT MATTERS:** the decomp cell text for both subjects asserts
*"standing=SUPERSEDED and REACHABLE FROM THE LIVE NIGHTLY."* SUPERSEDED is corroborated.
**REACHABLE FROM THE LIVE NIGHTLY is not supported by anything I could measure** -- and for
`kuzu_stitch_load` a nightly is *declared in a live config file* while the artifact sits 50.60 days
old with its own input 18 days newer than it.

**NO MODULE WAS TOUCHED.** Every exercise wrote into the session scratchpad via `--db-path`/`--db`.
Commits by this lane touching either carded module: **0**, positive control 5.

## Work done

### 1. Startup (org/XXX.md Step 1b) + /watcher

Registered `0.4.0_DT_ClientPlatform~X` (PID 18344). **No watcher existed for this serial** -- the
predecessor's had already gone, so the orphan-vs-live discriminator never had to be applied. Armed
the persistent Monitor (task `bjwobra1n`) and **read its arm banner: `parent-tied: pid 584242`**, i.e.
ARMED not OFF -- the check MSTR's 74791 doc-fix says seats skip. A.3 PATH read **105 of 105** comp-tools
resolving bare AND the mandatory exercise limb passed (a forwarder produced its own banner, so
resolution was not mistaken for execution).

### 2. The measurement

Read both subjects fully at source, then measured what the source cannot tell you:

| axis | kuzu_load.py | kuzu_stitch_load.py |
|---|---|---|
| writer class | CLASS 1 `:142` `:147` | CLASS 1 `:70` `:74` |
| bound set | ENUMERABLE `{CloudNode, CloudEdge}` | ENUMERABLE `{CloudNode, CloudEdge}` |
| write paths | **1** | **1** |
| mutation | `replaceable` (rebuild-or-nothing) | `editable` (MERGE upsert) |
| artifact age | 75.68 d | 50.60 d |
| trigger | none-found | none-found, **and a nightly is DECLARED** |

**WRITE-PATH MULTIPLICITY -- the TO's blocking question -- resolved as ONE for both, and I state the
test rather than the verdict.** Each file has a conditional `--force` delete prefix
(`shutil.rmtree`/`os.remove`) inside its single write path. That is *not* a second path under the
TO's own conjunctive test (mechanism AND bound AND authority, the test that split `derive_runner`):
same bound, same authority, and it never occurs without the create that follows. **Not filed as a
BLOCKING surprise.** Recorded so the certifier can disagree with the reasoning rather than guess it.

### 3. Trigger: three instruments, and the one that discriminates

1. **Repo-invocation plane** -- `comp-find --all`, denominator PRINTED: 27,093 files scanned / 13
   unreadable / 1,948 binary. 187 hits for `kuzu_load`, 70 for `kuzu_stitch_load`, **zero of them an
   invocation** -- docstrings, `NOT kuzu_load.py` disambiguations in sibling tools, audit-log echoes,
   config declarations, archive-prediction rows.
2. **Container plane, read from the image definition as AC5 demands** --
   `infra/aws/globgrph/Dockerfile:186` is `CMD ["python", "/app/derive_runner.py"]`. Neither loader.
   `Dockerfile:156` states a local Kuzu DB is ABSENT in-container.
3. **⛔ THE DISCRIMINATING ORACLE -- the artifact's own stamp.** `_provenance.write_manifest` is
   called *unconditionally* on every successful build, so a successful run cannot happen without
   moving `built_at`. `kuzu_db` still reads 2026-06-12, `kuzu_stitch_db` 2026-07-07. **Evidence that
   would differ if the claim were false**, which the first two instruments alone do not give you.

**RESIDUALS NAMED, NOT COVERED:** a trigger that fires and FAILS leaves no stamp; a trigger writing to
a non-default `--db-path` stamps elsewhere; I did not sweep `aws events list-rules` /
`aws scheduler list-schedules`. The claim is scoped to the default artifact and says so on both cards.

### 4. Failure modes, EXERCISED -- the schema says do not read them off a docstring

**kuzu_load.py, the silent degrade:** built a scratch DB from a 3-node snapshot, re-ran the same
command against a **9-node** snapshot with no `--force`. The run READ the newer snapshot, printed
`INFO: DB already exists ... Use --force`, **wrote nothing**, printed `OK: Kuzu DB at <path>` and
**exited rc=0**. Oracle: DB still held 4 nodes, manifest still carried the first run's stamp.
*A caller scoring this on rc or on the trailing `OK:` reads a refresh that did not happen as success.*

**kuzu_stitch_load.py -- sharper, and I did not expect it.** Built from a 5-node input, re-ran against
a **shrunken 2-node** input, no `--force`. rc=0, `KUZU_STITCH_LOAD_COMPLETE`. Oracle: **the DB held 5
nodes and the manifest claimed 2.**

> ⛔ `kuzu_stitch_load.py:123` passes `len(best)` -- the deduped **INPUT** count -- into
> `write_manifest`. Under the file's own MERGE semantics that is not the store's count. **The
> provenance artifact, whose entire purpose is making the store's vintage and scale checkable, can be
> wrong about the store it describes** -- and `_provenance.py:6-8` says `comp-kuzu` prints it as a
> header on EVERY invocation. NOT true of the sibling: `kuzu_load` writes its manifest only inside the
> rebuild branch, where the DB was just repopulated from exactly those nodes. **The defect is created
> by MERGE, not by `_provenance`.**

### 5. Controls

- **Two planted mutants, both REJECTED** in the same runs the real cards passed: (A) `owner` deleted
  from a row; (B) `basis="measured"` over an `inferred` sub-claim -- chosen because the schema
  enforces the floor rule only partially, so it is the arm most worth exercising.
- **Determinism STABLE** -- re-ran the generator, sha256 identical. The cards are GENERATED, so a
  regeneration cannot silently disagree with the committed bytes.
- **⛔ I SHIPPED A DEAD POSITIVE CONTROL AND CAUGHT IT ON RE-READ.** AC8's control pointed at the
  brand-new, uncommitted `D11_CARDS_W3` and returned **0** -- *a positive control returning zero
  certifies nothing*, and it would have vouched for the AC8 zero with an arm that cannot fire.
  Retargeted at `D11_CARDS_W2` (same query shape, filtered to the same serial), now returns **5**, and
  the PASS gate itself now requires `ac8_control > 0` so the dead arm cannot recur silently.
  This is the "a positive control has its own SUBJECT" class, in my own memory, committed by me.

## Compiler Tools

`comp-find` (both subject tokens, `--all`, denominator printed -- established the none-found trigger
verdict and surfaced `critical-surfaces.yaml:163`'s declared nightly, which is what made
DESIRED-vs-APPLIED *measurable* rather than merely suspected) · `comp-which` (A.3 exercise limb) ·
`git show <pin>:<file> | git hash-object --stdin` vs `git hash-object <worktree>` for all 5 cited
files, **blob hashes on both sides so CRLF/LF normalisation is identical** · `jsonschema
Draft202012Validator` · `.tools/proof-of-spec-check.py` · `.tools/commit-gate.sh`.

**One rail denial, handled correctly:** a repo-wide `grep` over `infra/` was hard-denied per Rule 21.
The Dockerfile read was re-run with `# rail-checked:` naming why no comp-tool fits (comp-aws/comp-iam/
comp-routes read live AWS resource edges and IAM; none reads a Dockerfile `CMD`), plus a positive
control. An earlier unscoped repo-wide grep also timed out at 2m -- the rail was right twice.

## Blockers

**NONE. Both workstreams are delivered.** DTX3 VERIFIED PASS by `3.0.0_SA_CVO~X` (74878) and
ACCEPTED by `2.0.0_SA_COO~X` (74880). W3-m-6 delivered @df687a488d.

⛔ **THIS SECTION SAID "W3-m-6 IS HELD" WHEN I COMMITTED IT AT 07:0xZ, AND IT WAS ALREADY FALSE.**
COO amended the oracle @7d03d9e788 *before* I wrote the sentence; the amendment and my log crossed.
I caught it only because I re-read my own file on the trigger *a ruling landed* -- which is a
standing memory entry of mine about exactly this: **your own committed artifact goes stale against
the rulings that corrected it, and nobody audits it because it is the thing everyone trusted enough
to commit.** Fourth crossing-in-flight of the session and the first one where I was the stale party.

## W3-m-6 -- THE COMPILE STEP (delivered @df687a488d)

Seated on this lane by COO 74846 on a premise that was already withdrawn. I held the from-zero
reading per MSTR 74850 / CTO 74856, said so in my report, and executed the moment the amended
oracle landed. **The work was EXTEND, not build.**

**Oracle met, re-measured independently of the compiler's own stdout:** validates 0 errors
(negative control 5, fires) · parts 42 > 39 · denominator NAMES BOTH POPULATIONS · 13 = 9 enrich +
3 add + 1 unresolved, and the partition sums.

**The deliverable is the GENERATOR.** MSTR's corrected finding was not that the manifest was missing
-- it was that it is hand-compiled with no generator, so at wave-3 close it would read COMPLETE
while being STALE. The instance was the easy half.

**⛔ THE JOIN COULD NOT BE DERIVED.** 9 of 13 cards carry PROSE in `artifact.location.home`; an exact
join resolves 2 of 13. v2 REJECTS prose in `joinable_ref.id` but never constrained `home` -- the one
field the compile step must join on. **Not a lane defect**: no lane could have avoided it while
following the schema, and my own 2 cards join only because a filesystem path is naturally clean --
my subjects' shape, not my rigour. So the join is DECLARED in `w3_card_part_map.json`, one row per
card, each with its own basis and evidence.

**A substring join would have been worse than none:** part id `cse` substring-matches any prose
containing those letters, and a FILE-grain join maps derive_runner PATH A and PATH B onto the SAME
parts -- the exact blend the wave's (FILE, WRITE PATH) grain exists to prevent.

### Three defects I found in my own compiler, all by reading its OUTPUT rather than its exit code

1. **Not re-runnable.** It read and wrote the same file; a second run re-appended every opinion and
   tripped an assert. *"It runs when cards land" requires a second run.* Input/output now separate;
   two runs byte-identical by sha256.
2. **It destroyed a true claim.** I floored the PART's basis with contributing cards'
   GENERATION-row bases, driving `graph_nodes` from `measured` to `absent`. That publishes "no basis
   exists yet" for a part whose existence, home and vintage were all measured. Wrong grain.
3. **It silently dropped my own DTX3 finding.** A card's `actual_trigger: null` at basis=measured
   means MEASURED NONE-FOUND; L0's `trigger: null` means NOT KNOWN. The fold converted the most
   expensive measurement in the DTX3 delivery into an absence of information. Now `"NONE-FOUND
   (measured)"`.

**Five findings surfaced, none resolved**, owners named in the map file -- including a STALE
ATTRIBUTION in the existing 39 (`fedobs_coevolution_snap` names a materializer that wave 3 measured
does not write it; COO falsified the same claim independently in 74880), flagged ON THE PART so the
next reader inherits the doubt rather than the claim.

## Current State (zero-prior-context handoff)

Cards, generators, POS, the L0 compiler and this log committed. TO status `complete`; DTX3 VERIFIED PASS (74878) and ACCEPTED (74880). L0 manifest at 42 parts @df687a488d.
Verdicts: **2 UNSOUND / 0 QUALIFIED / 0 SOUND / 0 INCOMPLETE** -- every row measured, so INCOMPLETE
was never in play. `forward_disposition` on both cards is born `undecided` with `set_by: null`; this
lane must not adjudicate its own subjects' fate.

## Next steps

1. ~~Report DTX3~~ DONE (74875/74876); verified 74878, accepted 74880.
2. ~~W3-m-6~~ DONE @df687a488d, reported 74895/74896.
3. Nothing outstanding on this lane. The five W3-m-6 findings sit with their named owners.

## Surprises routed (OBSERVATION, no action taken)

1. "REACHABLE FROM THE LIVE NIGHTLY" unsupported for both subjects (§3).
2. `kuzu_stitch_load.py:123` manifest reports input count, not store count (§4).
3. `kuzu_load.py` default invocation: no write, `OK:`, rc=0 (§4).
4. Three Kuzu DBs share one directory declaring the same two table names with **three** different
   column sets, guarded only by `IF NOT EXISTS` and prose warnings in four sibling tools.
5. The wave-3 DECOMP.md face carries internally inconsistent totals -- §1 says 11 subjects, §2 says
   "9 of 9", §3's class table sums to 70 cells, §5's seating table sums to 77. **My 2 subjects / 14
   cells are consistent everywhere**, so nothing in DTX3 was blocked by it. Issuer's face to amend.
