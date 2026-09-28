# AMGT_HARVST -- ROUND 7 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-28 ~00:1xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~O` (file 20260927T235328Z), compiled on this seat's routing because
`3.0.0_SA_CVO~Z` is wound down on Andrew's word: `surprise-channel/remediations/REMEDIATION_v1.md` and
`adjudications/ADJUDICATION_v15.md`, both @`aaf9822304`.

**Round 7 is CLOSED. The project is NOT closed: no FWD grades REALIZED.** Recut owner: `2.0.0_SA_COO~Y`.

---

## 1. THE HEADLINE -- ROUND 6's TWO BLOCKING ITEMS ARE DONE, AND L9 FINALLY HAD SOMETHING TO GRADE

| round-6 enrichment item | round-7 outcome | evidence |
|---|---|---|
| 1. Z-S28: sa listing pages reach silver | **REMEDIATED + DISARMED** (`HVST-v-1`, publisher-neutral empty-mapping fix) | REMEDIATION_v1 row Z-S28 |
| 2. the bounded vendor act | **RAN**: 4 requests, all HTTP 200, `auth_refreshes 0`, from `--runtime-root` = main tree (Z-W20-S1 disarmed) | `deliverables/0.9.0_WK_AMGT_HARVST~22/ac2_run_output.txt` |
| 3. the ungraded judgment criteria | **L9 graded one: HVSTv2-AC4 PASS with 3 limits** | ADJUDICATION_v15 row Z-C-S22 |
| 4. the COO drain-end packet | **EXISTS** | `4a1eb28e45` |
| 5. the 3 carried rows | folded into the remediation file | REMEDIATION_v1 |

**Item 3 is the one that matters most.** Round 6 had no plausibility oracle (0 of 8 judgment criteria graded).
Round 7's AC4 asked the question no mechanical column can: are the rows that reached silver ABOUT the security
they are filed under? **0 of 40 are filed under a wrong name.** The decomposition's choice to put the judgment
criterion on `v-2` -- where a green delta over the wrong rows reads identical to one over the right rows -- is
what produced it.

## 2. WHAT THE SLUG SAYS IT DID NOT MEASURE -- ADOPTED AS A LIMIT ON THIS ANALYSIS

1. **16 of the 28 backlog rows are carried OPEN and were NOT re-measured** (10 ARMED, 6 INERT). Their clocks
   come only from the disarm owner's own records. **This analysis does not grade them either**; it names who
   re-measures them (section 5, item 6).
2. **AC4's grade judges the FIXED join rule against PRE-FIX evidence** (limit 2): the LNVGY file-under column
   was presented before `4cc54df506`. The PASS is a PASS of the rule, not of a post-fix rerun.
3. **The `opal_data_harvest` suite is still 3 failed / 161 passed at HEAD** (Z-W21-S2). Any round-8 criterion
   that grades against this suite grades against a red baseline until the repair cell lands.

## 3. FWD GRADES -- all nine NOT REALIZED, and why, per outcome

No round-7 cell was cut to exercise a full DONE WHEN population; both cells were repair-and-drain on the sa
path. **So no FWD moves to REALIZED, and none is graded on inference.** What round 7 moved:

| FWD | status | what moved / what still stops it |
|---|---|---|
| FWD-1 byte-for-byte, five publishers | NOT REALIZED | sa listing bytes now reach the store; **bbg is in hard refusal since 2026-09-15 (Z-S32)**, so the five-publisher population is unreachable until that is explained |
| FWD-2 every field, queryable | NOT REALIZED | sa rows reach silver; an empty mapping no longer drops a row. Not exercised field-by-field for all five |
| FWD-3 how found; second run fetches nothing | NOT REALIZED | **layer 1 dedupe (`--new-only`) was never passed** -- every run read `previously_stored: 0` against 121 held rows (decomp section 19). The "second run fetches nothing" clause is unexercised |
| FWD-4 strength grade | NOT REALIZED | AC4 limit 1 (relevance is not subject: about half the LNVGY rows are sector pieces) is **exactly the FWD-4 distinction** and is input to it, not evidence of it |
| FWD-5 / FWD-6 timeline, events | NOT REALIZED | build cell `v-3` deferred to round 8 (decomp 18e) |
| FWD-7 chatter by strength | NOT REALIZED | depends on FWD-4 |
| FWD-8 stranded articles reach the store | NOT REALIZED | the 20 held sa listing rows were drained; the full desktop population (field map A: 83 bodies, 84 links) was **not measured here** |
| FWD-9 backfill from 2026-01-01 | NOT REALIZED | no backfill cell yet |

## 4. ANDREW'S TWO WORDS THAT BIND THE RECUT

1. **Article-id dedupe (2026-09-27, decomp section 19):** *"we need a mechanism for article ID so we dont
   constantly pull same articles into database."* The mechanism exists; it needs passing.
2. **serp and social feeds (2026-09-27 ~17:2xZ, this seat's terminal,
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260927_1723Z_OPEN_CALLS_RECS_APPROVED_PYTHON_PATH_AND_SERP_AFTER_IDENTITY.md`
   @`a89b7619ca`):** *"yes, i do want to do social feeds and serp feed sooner than later but need identify
   resolved through existing channels first."* **So no serp or social cell is cut in round 8.** The identity
   backlog comes first and goes through channels that already exist; the serp spend still needs his word when
   it comes up.

**And the vendor rule is unchanged:** round 6's egress word was scoped to "this session" and has lapsed; the
2026-09-26 22:15Z word ("vendor call is fine you have egress") was given to `0.7.0_AE_CloudOps~I` for the
Black Diamond producer and does not travel. **Every WORLD cell in round 8 needs a live per-use word from
Andrew before it fires; a cell without one is a card, not a queued order.**

## 5. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~Y` recuts, in order

| # | cell | why it is where it is |
|---|---|---|
| 1 | **REPAIR cell (LOCAL, `lib/opal_data_harvest/`)**: the listings half of **Z-W9-S1** (silver_append keyed by second-precision `run_stamp` with `IfNoneMatch="*"`: two writes in one second collide); the **3 red tests** (Z-W21-S2, one is WinError 183, filesystem-state); the `--harvest-grammar` help text (Z-S27) | Z-W9-S1's live half is ARMED on exactly the path the capture cell writes, so it lands BEFORE any capture. The red suite is the regression baseline every later criterion grades against |
| 2 | **CAPTURE cell (WORLD, needs Andrew's per-use word)**: `--new-only` AND `--harvest-grammar` on every `run`; the criterion prints `mode` and `previously_stored` from the run artifact; a batch that tolerates one timeout (Z-W22-S2: one slow body cost 7 of 8 jobs) | Depends on 1. Andrew's article-id word lands here. A dedupe nobody can see in the evidence is a dedupe nobody can grade |
| 3 | **`v-3`, timeline BUILD (LOCAL)**, cut only AFTER the issuer reads `SPEC_SECTION_timeline.md` at HEAD | FWD-5/6. Off the critical path. The issuer's own reason 2 (decomp 18e) stands: a criterion written against an unread surface is the defect this project paid for twice |
| 4 | **`v-4`, ft/barrons DIAGNOSTIC (WORLD)**, carrying **Z-S31** (ft: 15 rows under 14 article_ids, every other publisher 1:1; does any gold count double-count it?) | Same publisher, same live surface. Diagnostic only, no producer change |
| 5 | **bbg DIAGNOSTIC (Z-S32)**: why `search/query` refuses (9 consecutive 403s) while `/user-info` reads 200 | FWD-1's five-publisher population is unreachable until this is explained. **No bbg capture is plannable before it** |
| 6 | **The 16 carried backlog rows, re-measured by their disarm owner** -- an ISSUER act, not a worker cell | The slug carried them without re-measuring. **Z-W11-S1 is not this lane's to fix** (`.tools/missions-tree-index.py`, a shared mechanism): route it to the tool's owner and record the route |

**Cut rules carried (not cells):** a criterion asking for a passing test by name uses `-rA` or `-v`, never `-q`
(Z-W21-S1); a placeholder whose value contains whitespace is expanded to a literal and declared `NONE`
(Z-W22-S6, this seat's ruling 20260927T220426Z); `ls task-orders/ | cut -d. -f1 | sort -u` before naming a cell
(decomp 18f).

**Judgment:** round 8 carries at least one judgment criterion again, on the cell where a green mechanical
column can hide a wrong result. **Candidate: the capture cell** -- are the rows `--new-only` skipped truly
already held (same article), or did a url/id mismatch skip a new one?

**Fan-out:** derived, not chosen. `1 -> 2` is serial. `3` is independent and LOCAL. **The WORLD cells (2, 4, 5)
share the vendor ledger and the device-local session vault**; the issuer's own reason 3 (decomp 18e) says two
live vendor cells in one round contend on the one surface whose failure is a silent credentialed login. **The
issuer serialises them or states why not.** Each build order carries at most three mechanical criteria.

## 6. WHAT THIS ANALYSIS DOES NOT DO

It does not re-measure the 16 carried rows (section 2). It does not grant a vendor word. It does not cut serp
or social work. It adds no outcome and changes no ENDPOINT or CONTRACT text, so it re-opens no L4-R half: it is
a recut input, not a PRD addendum.

## Compiler Tools

The slug's own not-re-measured count (16 of 28) adopted as a stated limit, not absorbed -- `REMEDIATION_v1.md`
parsed as JSON for its state distribution (40 rows: REMEDIATED 18, OPEN 22) rather than read from its summary
line -- the PRD's nine DONE WHEN clauses read at HEAD and graded one by one against what round 7's two cells
actually exercised -- decomposition sections 18-19 read so the recut inherits the issuer's own deferrals and
Andrew's dedupe word instead of re-deriving them.
