# AMGT_HARVST round 2 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~Y`. **For:** `3.0.0_SA_CVO~Z` at L9.
**Copied:** `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`, `0.0.0_AB_MSTR~Z`.
**Round issued** @`004f6621c7` from the L5 recut v1.1 @`04a235adb7`, itself cut from the CTO's round-1 L10 analysis @`f869aa705c`.

## THE ROUND IN ONE LINE

**5 of 5 task orders terminal, every one graded VALID, 22 of 22 mechanical criteria PASS, 1 judgment criterion left for the CVO, 0 worktrees open, 0 branches open, and NOT ONE VENDOR CALL in the whole round.**

## 1. THE FIVE CELLS

| Cell | Criteria | Outcome |
|---|---|---|
| `HVST-r-1` | 3 mechanical PASS + AC4 judgment | the timeline spec gains its failed-call state and error envelope |
| `HVST-r-2` | 3 PASS | as-received printed check, verdict PARTIAL, paths_proven 2 of 5 |
| `HVST-r-3` | 6 PASS | publisher column on gold mention, all three snapshots rebuilt |
| `HVST-r-4` | 5 PASS | package conftest poison, autouse, positive control, one opt-out |
| `HVST-r-5` | 4 PASS | listing capture WIRED 5 of 5, vendor_calls 0 from a counter |

### `HVST-r-1` -- the spec amendment, ranked first and delivered first
Section 6 gains one state, `The timeline request itself failed`, which draws a distinct page-level
error rather than a blank chart, an empty series or a zero-height line, states that it is visibly
apart from a quiet security and from PARTIAL or DENIED, offers a retry, and fails the dissection
panel independently of the line. Section 5 gains the envelope
`{"error": true, "error_code": <string>, "message": <string>}` with the rule that a failure is never
merged into `series`, `events` or `articles`. Section 7 carries the one-line pointer to the
`Z-S227` / `C-S400` precedent. Eight sections intact, pure ASCII, LF only, 30 insertions and 0
deletions, nothing under `portal/`, `infra/` or `lib/`.

**AC4 IS THE ROUND'S ONE JUDGMENT CRITERION AND IT IS YOURS.** Recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming you. Its question: does the amended spec
now draw every state, including the call's own failure, such that a build cannot reproduce that
defect on this new surface? AC2 is a keyword probe and the order says in its own text that the probe
is deliberately weak and cannot answer this.

### `HVST-r-2` -- PARTIAL is the honest verdict, and the flip was never conditioned on PROVEN
`as_received_proof PARTIAL paths_proven 2 of 5`: seeking-alpha 3 of 3 and wsj 11 of 11 with
`mismatch 0` on both, and bloomberg, barrons and ft carrying no objects from the live act at all.
16 test arms including the two load-bearing negative controls (the shape test rejects a deliberately
re-serialised body; the checker reports a mismatch when stored bytes are altered). The bound is
printed in the output and not only in the report: a session-layer hash proves what the TRANSPORT
received, not what the SERVER sent.

**ISSUER CORROBORATION ON A DIFFERENT INSTRUMENT.** The cell reaches its counts through the local
capture database and hash comparison. I never opened that database: I censused S3 object metadata
directly over every key under the bronze article prefix. Denominator 103 objects, distribution
`as_received 14`, `normalised_record 83`, `no received-form key 6`. The 14 agree exactly, which is
corroboration rather than repetition.

**AND MY OWN ROW `Z-S3` COMES OUT OF THAT CENSUS.** The verdict's grammar is wider than its
population: `paths_proven 2 of 5` names paths while the evidence covers 14 objects of 103, and all
6 unlabelled objects sit under the one path the cell grades PROVEN. Filed as an EXPOSURE, not an
incident, because whether any consumer reads bronze as as-received wholesale is UNMEASURED.

### `HVST-r-3` -- the only cell that wrote to the world, verified on the served artifact
I read the three rebuilt parquet snapshots straight out of S3 rather than trusting the cell's own
scratch scripts. Mention: 98 rows, 24 columns, `publisher` present as the second column, per-security
`BA 36 / COST 25 / HD 26 / 992_HK 11`, publisher values spread across all five publishers. Daily:
1596 rows, `data_status` `DENIED 1595` and `PARTIAL 1`, the single PARTIAL being the one WSJ listing
hit that now exists. Event: 5 rows. Determinism held, symmetric difference 0 on both recomputed
tables. Snapshots ACCUMULATE and nothing was deleted: the three prefixes hold 2, 3 and 2 objects.
**Lenovo is now in gold**, which the other coordination lane's trial report was told would ride this
recut.

### `HVST-r-4` -- the poison, and a stronger measurement than any worker could make
The conftest is autouse at the package pytest actually collects, proven by measurement rather than
assumed path, patching the module attributes rather than dotted strings, with three poison-control
arms that deliberately call each poisoned attribute and assert it raises, and one narrow opt-out
carrying its reason in its own docstring (a test that drives the CLI in a real subprocess with
networking refused).

**THE POPULATION THE WORKER COULD NOT REACH.** Its bar was that no existing test's outcome changes,
and it could only measure that inside its own sparse worktree. I re-measured every suite in the full
shared tree after the merge, with the poison active: retrieval_provenance 18, bronze_capture 12,
silver_from_bronze 16, legacy_upload 6, harvest_grammar 7, worker 2 failed and 18 passed, catalog 5,
verification 1 failed and 3 passed, plus the three new suites at 3, 16 and 18. Every pre-existing
count held and both pre-existing failures are unchanged.

**The order told the worker to say plainly that row `Z-W10-S3`'s mechanism stays unexplained, and it
did.** The poison CONTAINS that hazard; it does not root-cause it, and that row stays ARMED.

### `HVST-r-5` -- the code half of FWD-1 is settled, and the dichotomy was wrong
`wired 5 of 5`, `paths_examined 5 of 5`, `vendor_calls 0` read from a counter rather than typed, and
all three poison sites shown raising under a positive control. 18 arms including the negative control
where the capture is removed and the census correctly reports False. I verified on my own read that
the wired count is computed per result and never asserted, and that the capture check reads the real
`Publisher.listings` surface.

**SO THE LIVE ZEROS ARE NOT A CODE-WIRING CAUSE. BUT THE CELL FOUND A THIRD CAUSE MY OWN ORDER HAD NO
SLOT FOR, AND THIS IS THE ROUND'S MOST CONSEQUENTIAL FINDING.** Row `Z-W15-S1`: the harvest-mode
listing persist sits AFTER the whole per-article loop, so a job that raises mid-loop discards every
listing page already captured in memory. I re-read that placement at the source myself and it holds.
Seeking-alpha's live run fetched multiple listing pages and then took an HTTP 502 on a later article,
so its zero is closer to CODE than to SESSIONS.

**THE CONSEQUENCE FOR THE HOLD:** a fourth vendor act, if Andrew ever grants one, would NOT reliably
produce listing pages for any publisher whose job raises after page 1. The persist placement is a
round-3 candidate and it is cheap. **I am not asking for the vendor act and nothing in this round
did.**

## 2. THE CHANNEL

The channel now holds **26 rows**. Round 2 added **7**: five from workers (`Z-W11-S1`, `Z-W13-S1`,
`Z-W14-S1`, `Z-W14-S2`, `Z-W15-S1`) and two of mine (`Z-S3`, `Z-S4`).

Three drains conflicted on the channel, which is the normal path for an append-only file, and each
was resolved as a **UNION BY ROW ID** rebuilt from the two clean git stages rather than by editing
conflict markers. Row counts after each union: 21, 23, 25. No row was dropped and no two rows with
one id diverged.

## 3. MY OWN DEFECT, MEASURED AND OWNED -- ROW `Z-S4`

**Three of the five worker rows have ONE root cause and it is my dispatch, not the repository.** I
provisioned all five worktrees with a ten-path sparse cone because a full checkout risks an
out-of-memory failure on this device. Each row is a different surface failing on a path outside that
cone:

1. `Z-W11-S1`: the missions-tree hook walks the directory physically, so unmaterialized directive
   folders read as 24 false orphan violations and BLOCKED a correct commit.
2. `Z-W14-S1`: `test_harvest_grammar` read 1 failed and 6 passed in the worktree. **The
   discriminating measurement is mine and it inverts the row's own framing: the same suite reads 7
   passed in the full shared tree, and the worktree failure is `ModuleNotFoundError` on a module
   under `integrations/`, a directory the cone never materialized.** The row calls it a third
   pre-existing failure. It is not pre-existing and it is not the cell's.
3. `Z-W14-S2`: an absolute import resolving to a namespace-package duplicate, the same sparse-layout
   sensitivity one level down.

**Why this shape is dangerous rather than merely annoying:** each face looks like a finding about the
CODE to the worker that meets it, and that worker has no way to see the full tree, so it gets filed
as a repository fact. **No cell's grade changes** -- every criterion was met against the population
its own order named. The remedy is a dispatch-recipe change, and the standing lesson is that a
baseline measured in one checkout is not a baseline for another.

**I caught this because the dispatch note I sent the four still-running workers after the first row
landed saved three of them from rediscovering it**, and because I re-measured in the shared tree
instead of accepting a worker's environment as the repository.

## 4. WHAT MOVED ON THE OUTCOMES

- **FWD-1, article half:** the as-received remediation is now PROVEN on the two paths that have live
  objects and honestly UNPROVEN on three. **Listing half: NOT REALIZED**, and round 2 changed its
  OWNER rather than its status -- the code-wiring cause is eliminated, the sessions cause stands, and
  a third code-shaped cause is now named.
- **FWD-4 and FWD-7:** advanced. The publisher column exists and all three snapshots are current
  through Lenovo.
- **FWD-5 and FWD-6:** the spec is complete as a document. **The build cell against it is still
  held on Andrew approving the AMENDED spec**, per the round-1 analysis, and I have not cut one.

## 5. FOUR ASKS

1. **Grade `HVST-r-1` AC4.** It is the round's only judgment criterion.
2. **Read `Z-W15-S1` as the round's real finding**, and note its consequence for the vendor hold:
   the listing half of FWD-1 is not purely a sessions question any more.
3. **Note that `Z-W14-S1`'s own framing is measured wrong**, correction in `Z-S4`, and that the
   correction is mine about my own dispatch.
4. **`Z-S3` is a wording bound, not a defect in `HVST-r-2`.** The cheapest disarm is that no later
   artifact restates `paths_proven 2 of 5` as a claim about the paths' whole history.

## 6. STATE

`dep_stage` moves EXECUTING to ROUND_CLOSE with this commit. Five orders terminal, zero worktrees,
zero branches, zero open vendor asks. Everything is on origin as of the drain commits listed below;
push state is stated as measured in the covering message.

Drain commits, in order: `59d6347d37` (r-1), `8aefec368d` (r-2), `db04dbbc5d` (r-5),
`e7a664c5c0` (r-3), `e68dc69503` (r-4).
