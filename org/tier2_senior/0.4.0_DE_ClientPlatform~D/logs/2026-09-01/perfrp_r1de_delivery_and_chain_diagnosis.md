# ADVI_PERFRP.TO-R1-DE delivered on DEV; then eight hours as a measuring seat in someone else's diagnosis — 0.4.0_DE_ClientPlatform~D

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, COORDINATE

**Date:** 2026-09-01
**Task Order:** ADVI_PERFRP.TO-R1-DE (ACTIVE, issued 08-24)
**Status:** COMPLETE for the TO's DE-lane scope; two criteria remain gated by producer-side work
**Portal DEV commits:** `63db8242` -> `729b7617` -> `f4812aba`, merge `7d0ca60c` (origin/DEV tip, ls-remote MEASURED)
**Workspace CLOUD commit:** `293938c12d` .. `fd2dc003b8` (6 commits, all ancestors of origin/CLOUD `c92aece496`, ls-remote MEASURED)

---

## Objective

Reseated on TO-R1-DE with the START CONDITION explicitly UNVERIFIED. Bind the remaining
AdvisorIntelligence perfrp cards on portal DEV, move the fetchers onto the ratified key class,
and stay event-driven on fabric dispatches. The TO's own premise (that the pages were empty
because the wiring was missing) turned out to be half true: half the panels were already wired
and DEV emptiness was the designed pre-serve state.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | 11 invocations 08-31 | PARTIAL | located producers/leaves; one FALSE ZERO from `--name` matching BASENAME not path |
| comp-find | 2 invocations 09-01 | PASS | census work during the chain diagnosis |
| comp-read | 3 invocations 09-01 | PASS | file-shape reads under the 09-01 single-file rule |
| comp-cache collisions | NOT RUN | FAIL | DE minimum. See gap below. |
| comp-transform schema-check | NOT RUN | SKIPPED | no change to existing data props; new components author their own |
| comp-blast | NOT RUN | SKIPPED | no endpoint function deleted; fetchers were added and re-pointed |

Counts are MEASURED from `org/mcp/comp-which-rail.log` filtered on `serial=0.4.0_DE_ClientPlatform~D`
for 2026-08-31 and 2026-09-01 — 16 rail-logged invocations total, not recalled. The rail sees only
routed calls; native `Read`/`sed`/`git`/`aws` work is not represented and was the bulk of the session.

**What worked:** `comp-read` earned its 09-01 mandate on `perfrp_emit_core.py` — the qualifier and
contradiction index is what a grep of that file structurally cannot show.

**What failed:** `comp-find --name` with a path-glob returned `0 hit(s)` over a large denominator and
I converted it into an absence claim in a message to three seats. `--name` matches the BASENAME; the
glob could never match. The false zero survived review because it AGREED with a correct conclusion.
Retracted at full width and banked to memory.

**Gap found:** I added React Query keys in `AdvisorBookView.tsx` (threading `firmId` through seven
call sites INCLUDING the query keys) and never ran `comp-cache collisions`, which is a DE role
minimum for exactly that act. Zero invocations of any DE-minimum tool across the whole session,
measured. The keys are namespaced by leaf filename and I have no evidence of a collision — but I
have no evidence against one either, and that is the point of the minimum. Recording it as a FAIL
against myself rather than a SKIPPED with a reason, because there was no reason.

---

## Work Completed

### 1. Bound the two genuinely-unwired cards

`PerfrpAllocation.tsx` (NEW) renders allocation as a CLOSED DISTRIBUTION, not through
`PerfrpFigureCell` — routing it through the figure path would have fabricated a producer
disposition the leaf never emitted. Residue is classified from the leaf's own
`residue_states_declared`, never from a literal. Nothing is dropped. `CLOSURE_TOLERANCE = 0.0005`
and the closure control renders ONLY when it fails.

`PerfrpTransactions.tsx` (NEW) zips `prd_card_columns` against `served_columns` positionally and
REFUSES to render on a length mismatch — mislabelling Units/Price/Amount is worse than no table.

### 2. Precondition #2 — the fetcher key class

Moved the four perfrp fetchers onto `platinum/advi/{firm}/` via a new `perfrpLeafBase()` helper.
The firm segment is the portal-canonical LONG form and deliberately does NOT go through
`bucketSuffix()`, which maps `49financial` to `bd` on a different axis (S3 bucket suffix) and
would have built `advi/bd/{leaf}` — a 404 indistinguishable from an unpublished leaf.

### 3. A rendering defect in my own new code, caught on a read render

`formatShare` flattened real shares of a 1.79B book to a misleading `0.0%`. Fixed to use
`toPrecision(2)` below 0.05%, re-rendered, re-read. A nonzero share must never render as zero.

### 4. Pre-registered the post-push predictions BEFORE the push

`ADVI_PERFRP.TO-R1-DE_POST_PUSH_PREDICTIONS.md`. Headline, counterintuitive and still
UNFALSIFIED: the L3 Performance card will STILL render a shell after a fully successful push,
because `perfrp_performance_relationship.json` is not served. That is the card on Andrew's
original screenshot, at the grain he was looking at. Recorded so the outcome would be a confirmed
prediction rather than a fresh alarm — the fourth time on this surface a correct act would have
read as a defect. Amended twice at the file rather than in a message, because a stale prediction
file is the carrier a future reader hits first.

### 5. Measuring seat in the chain 6-to-0 / publish diagnosis (not my TO)

Contributions that survived: the CONSUMER denominator (7 required, 4 served, 3 missing) that
became `R2DS-AC3`; the list-then-read observation with ONE choke point and eleven call sites,
ratified as the primary hypothesis; all three S3 publish manifests measured, finding the
`inputs_missing` discriminator CONFOUNDED when `asof` is empty (the filter compares each date
against an empty string, so a fully successful list still populates it — the 11:06Z manifest is a
worked instance at 541 partitions found); and a read of
`chain_49f_entrypoint.py::_run_perfrp_projection`, which NO seat had opened all day — establishing
that the chain is structurally BUILD-ONLY and never wrote a served leaf, that the source NAMES the
by-design refusers, and that the stage classifier has NO FLOOR on `built`, so
`built=0 refused=11 hard_fail=0` prints `STAGE OK rc=0`.

---

## Postmortem — four corrections I issued against my own claims

| Claim | Why it was wrong | Scope of retraction |
|---|---|---|
| "the router source is NOT in this worktree" | `comp-find --name` matches BASENAME; my glob could never match | full width, 3 seats |
| "AC11 is an equality test" | reasoned from the TO's paraphrase, never opened `PRF-inv-3`, which says RECOMPUTE — on my own acceptance criterion | fixed the prediction file, the carrier |
| "the calendar explains it; refusals are correct" | post-fix code ALIASES a Monday to Friday and builds 9 — measured twice by the producer seat | to Andrew, same turn |
| "the anomaly is 7 of 11" | accepted an issuer's split without testing it; `held_by_determination` is reachable only from a built status, so the held pair are genuine failures. It is 9 | to 5 seats |

The pattern in all four is one thing: a sound measurement with an interpretation stapled to it
that I had not tested. Three of the four were caught by me within a turn or two; the fourth was
caught by a peer. I also raised a `[STOP]` on a ruled precondition without checking whether its
premise still described the world — it had been false for months.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Render allocation as a closed distribution, not figures | Its dispositions live in the class dimension; the figure path would invent a producer state |
| REFUSE to render transactions on a column-count mismatch | A mislabelled money column is worse than an absent table |
| Long-form firm segment, bypassing `bucketSuffix()` | That helper addresses the bucket axis; using it yields a 404 that reads as "not yet published" |
| Pre-register predictions before the push | This lane's own precedent; it converted an expected shell into a confirmed prediction |
| Do NOT re-measure the served plane to feed the producer seat's test | The owning seat had already run it; a second read of one artifact is repetition, not corroboration |
| Narrow my own confound warning rather than let it stand wide | Overstating a confound retires a working instrument; the arm is sound whenever `asof` is non-empty |

---

## Files Modified

See commit messages: `293938c12d`, `b84d267e3b`, `7cb8209166`, `2c4e7cf420`, `4f56e89c7c`,
`fd2dc003b8` (workspace) and `63db8242`, `729b7617`, `f4812aba` (portal). Rows needing context:

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/_shared/perfrp/PerfrpAllocation.tsx` | NEW — closed distribution, residue from declared states, closure guard | Yes — `63db8242` |
| `portal/src/pages/AdvisorIntelligence/_shared/perfrp/PerfrpTransactions.tsx` | NEW — positional column zip, refuses on mismatch | Yes — `f4812aba` |
| `portal/src/api/endpoints/advisor-intelligence.ts` | `perfrpLeafBase()`, two leaf fetchers, b-3/b-5 types | Yes — `729b7617` |
| `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx` | two queries, `detailSlots` passed for the first time, `firmId` threaded through 7 call sites incl. query keys | Yes — `729b7617` |
| `org/tier2_senior/0.4.0_DE_ClientPlatform~D/deliverables/perfrp_b2_fixture_build.py` | b-3/b-5 leaves, residue-spanning row pick, closure guard that ABORTS, second PII gate | Yes — `293938c12d`, `7cb8209166` |

---

## Blockers

None at this seat. Two TO criteria are gated, and both gates are producer-side and named:

- `PRFR1DE-AC11` — scoring BARRED by issuer ruling (COO 91090) until the weighting harness is
  LIVE AND DISCRIMINATING. The harness rides ADVI_PERFRP as a precondition, owned by
  `0.4.0_DS_ClientPlatform~G`. I did not ask for the bar to lift. Additionally the recompute
  cannot run until `performance_relationship` is SERVED, which it is not.
  Evidence: `ADVI_PERFRP.TO-R1-DE_POST_PUSH_PREDICTIONS.md`, ruling section.
- `PRFR1DE-AC8` — producer-owned unreachable enum. Not a DE act.

Activity Summary has no emitted leaf, so its shell is correct and not a blocker.

---

## Current State

All DE-lane deliverables for TO-R1-DE are on `origin/DEV` at `7d0ca60c1d` (portal submodule) and
on `origin/CLOUD` at `c92aece496` (workspace), both push states MEASURED by `git ls-remote` plus a
`--contains` check, not defaulted. Four perfrp leaves are served under
`s3://opal-data-portal-v2/platinum/advi/49financial/` — `book_advisor`, `performance_account`,
`gainloss_account`, `gainloss_relationship` — and three required leaves are NOT
(`performance_relationship`, `allocation_account`, `allocation_relationship`); `transactions` is
deferred by ruling. The cards for the unserved leaves render their shells, which is the designed
pre-serve state documented at `AdvisorBookView.tsx:428-431`, not an error. The publish path has a
measured empty-`asof` defect whose manifest sits at the double-slash key
`platinum/advi/49financial/_manifests//4b36d4f5743c.json` (11:06:00Z, 7 rows, 10 inputs missing,
0 vintages) and `latest.json` currently points at that run.

**AMENDED 16:2xZ — THE REGRESSION FRAME ITSELF WAS THE DEFECT.** ⛔ **RE-AMENDED 18:2xZ: my first
amendment over-read this, and the over-read is the dangerous direction.** The frame finding retires
the BEFORE; it does NOT retire the question. Today's zero is REAL, UNEXPLAINED and a LIVE PRODUCTION
REGRESSION — `0.7.0_AE_CloudOps~M` measured that today's `asof=2026-08-31` partition holds **6% MORE**
data than the last-good 08-28 (flow_ledger 4.2x, nna_canonical 2.9x, every table present) and that
FOURTEEN other chain stages consumed it and wrote **30 objects** from it, while only the eleven
emitters refused. A no-new-data story has to explain why fourteen stages populated. **"The frame
dissolved, the DISCONTINUITY did not"** (`1.0.0_SA_CTO` 92293 s.2) — and running those two together
in one word is exactly what I did. `0.7.0_AE_CloudOps~M` measured the
untruncated per-day chain logs in `gold/advi/_logs/` (control: zero truncation sentinel):
**08-29, 08-30 and 08-31 ALL re-processed `asof=2026-08-28`.** The three pre-fix `built=6`
observations are ONE RESULT REPEATED ON THE SAME DATA, not three independent days, and today is the
first new as-of in four days. **THE BEFORE/AFTER COMPARISON HAD NO VALID BEFORE.** That is
corroboration-by-inheritance operating on the FRAME rather than on any single claim, which is why
every measurement inside it was sound and the conclusion still went nowhere — and it explains the
one thing no mechanism could, namely families sharing no code path failing identically. They did
not start failing; the input changed for the first time in four days. Andrew supplied this
hypothesis from a single high-level summary roughly forty minutes before it was measured
(`2.0.0_SA_COO` 92288 records it verbatim).

Every mechanism candidate is now dead: IAM (false deny from a prefix-conditioned grant read with no
context), the trading calendar (post-fix code aliases a Monday to Friday and builds 9), stale bytes
(ETags identical), the wrapper-argv seam (green), and the absent-dependency story
(`0.7.0_AE_CloudOps~M` killed its own candidate — five modules import pandas and all ran STAGE OK in
the very run that refused 11 of 11, and emitters spawn under `sys.executable`, so there is no
interpreter gap either). What survives is the DISCONTINUITY, and it is unowned and live: seven
authorised families that were measured clean produced no payload from a partition richer than the day
they last built. `0.7.0_AE_CloudOps~M` narrows where to read — `perfrp_emit_core.py` went 19,742 ->
114,406 B at `2026-09-01T00:10:20Z`, the only change in the window to the file all eleven emitters
import, spanning the last-good/first-fail boundary exactly — so the cause sits inside ~94 KB of NEW
LOGIC rather than in what it imports, and that read is emitter-lane.

⚠ One caveat of mine is now DISCHARGED and I record it rather than leave it standing: I wrote at
92135 that the runner's interpreter was "inferred from chain-level pycache names". `0.7.0_AE_CloudOps~M`
corroborated it on an independent instrument — AMI `ami-0c7217cdde317cfec` is Ubuntu 22.04 LTS, whose
system `python3` IS 3.10. Different plane, same answer, so per Rule 22 that is corroboration and not
repetition. The runner is CPython 3.10.

---

## Next Steps

1. **When a publish lands, re-list the served plane BEFORE reading the render** — the input state
   in the prediction file is a measurement with a timestamp, not a constant. Then report AC11 and
   GATE A against the pre-registered predictions. Committed to doing this unprompted.
2. **Build AC11 as `PRF-inv-3`'s RECOMPUTE, not an equality check** — recompute each level from
   the level below on the served block, print all three. Scoring stays BARRED until the harness
   is live.
3. ~~Run `comp-cache collisions`~~ **CLOSED 16:2xZ, CLEAN.** `captured 118 of 118 useQuery
   call-site(s); 0 unparseable` / `17 shared key(s); 0 with a TYPE MISMATCH (the bug-class)`, and
   ZERO of the 17 are perfrp keys. The process gap was real; there was no defect behind it. Tool
   states its own bound: `useQueries`/`useInfiniteQuery`/`useAutoSaveQuery` are NOT audited — my
   additions are plain `useQuery`, so they are inside the covered set. Detail:
   `comp_cache_minimum_closed_1600-1620Z.md`.
4. ~~Compare runner-vs-laptop dependency versions~~ **SUPERSEDED 16:2xZ.** The dependency axis is
   DEAD: `0.7.0_AE_CloudOps~M` measured five modules importing pandas running STAGE OK in the same
   run that refused 11 of 11, and emitters spawn under `sys.executable`, so no interpreter gap
   exists. Recording the supersession rather than deleting the row — a next-step a reader acts on
   after it is moot is the same stale-carrier failure this log's own Postmortem is about.
5. ~~Read `run_emitter`'s exception handling~~ **ANSWERED 16:0xZ** by `0.7.0_AE_CloudOps~M` against
   bytes verified equal to the deployed ETag: `rc != 0` maps to `emitter_refused`, NOT to
   `error`/HARD_FAIL — which REFUTES the counter-indication I raised twice (92135 s.3, 92165 s.3).
   The same read explains the empty reason fields: `emitter_tail` captures STDOUT and a traceback
   goes to STDERR, so the reasons were never missing and the wrong FIELD was being read.
6. **The one finding of mine that survives the frame collapse** — the chain stage classifier has no
   floor on `built`, so `built=0 refused=11 hard_fail=0` prints `STAGE OK rc=0`. Whatever the
   cause, nothing failed on that number, which is how four days of a repeated as-of went unseen.
   Remedy shape is a producer-lane call, not mine.
