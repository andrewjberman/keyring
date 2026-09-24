# NEVER-WIDEN CO-SIGN -- CTO HALVES. Round 14, chain F. One section per co-signed cell.

**Signer:** `1.0.0_SA_CTO~Z`. **SIGNED as recorded in the CTO SIGNATURE block at the end of this file.**
**Counterpart:** `2.0.0_SA_COO~Z`'s COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_F_COO_HALVES.md`, read at
`9a6aa12da2` (branch `coo-amgt-r14-issue-20260918`, tip at read time).
**This plane:** **DESIRED -- the SOURCE DIFF and THE PRODUCER'S OWN RULE.** The COO half carries
APPLIED/EXERCISED (live keys, per-key rollback measured fresh). Neither half stands alone.
**Repo vintage for every unqualified `path:line` below:** HEAD = `c898937600` (branch `SITEZ`),
read 2026-09-18. **Ratified rule read against:** PRD `prd_version: v0.13`,
`org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` -- `C-VERBATIM-GATE` at `:907-921`,
`C-FILINGS-ANALYZER` at `:663-694`, `C-VALIDATION-NAMES` at `:1652-1659`.

⛔ **READ THIS BEFORE THE SECTION.** This half is NOT a clean concurrence. It carries **four
disagreements with the COO half measured at source**, one of which (D3) names a reachable branch
in which the act does not shrink the served set but **removes it entirely for every rebuilt key**.
Per CLAUDE.md s.5 NEVER-1 a half covers **both branches or it is not signed**, so D3 is a
sign-blocking item, not a note. A disagreement between halves is the finding, never something to
smooth over.

**Cells covered: 1** (`AMGT-rk-41`). `rk-38`, `rk-39`, `rk-40`, `rk-42` are not co-signed and are
not read here; that partition is the COO's and this half neither widens nor narrows it.

---

## `AMGT-rk-41` -- C-VERBATIM-GATE = HOLD applied by rebuilding the served drafting objects (R14-F4; FWD-9, FWD-18, V6/D18)

### 1. THE ACT, restated

ONE rebuild, through one composing function, of every `s3://opal-data-harvest/drafting/v1/<key>.json`
whose key is in the measured population AND carries an analysis object (12 at the COO's cut; the
denominator re-measured at spawn). The rebuild re-applies `C-VERBATIM-GATE` **as the cell changes
it** -- a drafted sentence with no verbatim span is HELD rather than served. No model call, no SEC
fetch, no Lambda redeploy.

⚠ **THIS RESTATEMENT DOES NOT AGREE WITH THE COO HALF'S, AND THE DISAGREEMENT IS IN THE COO HALF'S
FIRST LINE.** The COO half states the act as the literal invocation:

> `python -m lib.research.filings.drafting_build --rebuild-pool --population crosswalk/v1/2026-09-15.json --pre-act-dir .scratch/drafting_v1_preact`

**That command does not exist at HEAD and cannot exist without the cell first writing it** -- see
**D1** below. The act as stated is therefore a DESIRED command, not an existing one, and this half
covers what the cell must BUILD. The same shape was bound in chain I (`add_security.py` does not
exist at HEAD; msg 23819) and it is bound here for the same reason: the producer's rule cannot be
read from a producer that has not been written, so **every outcome below is read from the code the
rebuild will CALL** -- `build_drafting_document` and the gate beneath it -- which does exist, plus
the ratified rule the new CLI must implement.

### 2. THE SOURCE DIFF -- what the cell changes or calls

**Called, unchanged (exists at HEAD):**

| file:line | what it does |
|---|---|
| `lib/research/filings/drafting_build.py:212` | `def build_drafting_document(analysis, section_limit=SECTION_LIMIT)` -- the ONE composer. Pure transform: no `boto3`, no `put_object`, no `write_pool` anywhere in the file's 248 lines (read whole). Its own docstring `:9`: *"it makes NO model call of its own and adds no rule the gate does not enforce"*; `FilingsProducer` docstring `:177`: *"NOT A MODEL CALL."* **The COO half's "NO model call" is CONFIRMED at source.** |
| `lib/research/filings/drafting_build.py:220-221` | `run_pipeline(FilingsProducer(...), records, source=..., max_attempts=1)` |
| `lib/research/drafting/pipeline.py:122-144` | `_gate_sentences()` -- validation (`validate_evidence`, `:86-111`) then the gate (`:137`); a REFUSE is dropped and counted, never shipped (`:138-142`) |
| `lib/research/drafting/verbatim.py:65-79` | `check_against_sources()` -- THE GATE |
| `lib/research/identity/crosswalk.py:609-657` | `write_pool()` -- the only S3 put on this path |

**Changed by the cell (the source diff this half is signing the shape of, not the bytes -- the
bytes do not exist yet):**

1. **A CLI and a rebuild driver.** `drafting_build.py` at HEAD has **no `argparse`, no `main()`, no
   `if __name__ == "__main__"`, and no S3 read or write** (whole-file read, 248 lines). `comp-find
   'held_no_span|served_no_span|rebuild-pool|rebuild_pool' --all`: **1 hit across 66,307 files
   scanned, band DOC=1**, in an unrelated `0.8.0_AE_CloudComp` log -- **0 in CODE, DEF or HEAD
   anywhere in the corpus.** So the flags, the two split counters and the module entry point are
   all NEW.
2. **The gate's own rule.** `verbatim.py:60-61`: `if not span: return True` -- an empty span is
   *vacuously verbatim*. `check_against_sources` therefore returns `"PASS"` for a sentence with an
   empty `quoted_spans` list (`:75` `continue`, `:79` `return "PASS"`). `drafting_build.py:44`
   states the same in prose: *"A sentence with NO verbatim run carries an empty list and is
   vacuously PASS"*. **At HEAD a no-span sentence is SERVED.** The HOLD is the change.
3. **Where the no-span sentence goes.** This is the one design choice that decides the blast
   radius, and it is NOT stated in either half. See D3.

**What the change makes the code do:** it converts the no-span outcome from a served PASS into a
withheld one, and makes the pass count print its split (passed-on-span / passed-with-no-span /
held), which `C-VERBATIM-GATE` `:911-913` requires in terms: *"EVERY PASS COUNT PRINTS ITS SPLIT
... A count that omits the split is not evidence of verbatim coverage."*

**Read against the ratified rule.** `C-VERBATIM-GATE` `:914-915`, verbatim:

> "⛔ **A drafted sentence with no verbatim span is HELD: never served, and counted in the split**
> (v0.12, Andrew-direct ~19:4xZ, *"Agreed, yes."*)"

The act's DIRECTION is ratified and is Andrew's own word. `:916` measures the size: **179 of 389
sentences over 12 served documents (46%)**, CAT 17 of 39 and CSL 16 of 40. That figure is the PRD's
(`4.0.0_SA_CRO~Z`, msg 23744), carried here as a cited magnitude, **not re-measured by this seat**.

### 3. THE PRODUCER'S RULE, per branch

**3a. `write_pool()` (`crosswalk.py:609-657`) -- the only writer of bytes on this path. Every branch:**

| branch | condition | what it writes | what it does NOT write |
|---|---|---|---|
| ABSENT | `head_object` raises 404 / `NoSuchKey` / `NotFound` (`:624-626`) | `put_object` with `IfNoneMatch: "*"` (`:629`), Metadata `document-sha256` + `schema-version` | nothing else |
| UNCHANGED | key exists and its `document-sha256` **equals** the new digest (`:628`) | **NOTHING. `put_performed=False`.** A re-run of the identical rebuild mints nothing | no put at all |
| CHANGED | key exists, digest differs | `put_object` with `IfMatch: head["ETag"]` (`:629`) -- **overwrites in place** | no other key |
| RACE | `IfMatch`/`IfNoneMatch` fails (a concurrent writer moved the ETag) | nothing -- `ClientError` propagates | -- |
| READ-BACK FAIL | post-put `head_object` digest or `ContentLength` mismatch (`:639-650`) | raises `ValueError` **after the put has landed** | -- |
| OTHER `head` ERROR | any `ClientError` code outside the three (`:625-626`) | re-raises; **nothing is written** | -- |

⭐ Two consequences the COO half should carry: the **UNCHANGED** branch means a re-run is a
recorded no-op (the rollback's re-put is therefore also idempotent and safe to repeat); the
**READ-BACK FAIL** branch is the one where the exception arrives with the object already
overwritten, so the per-key rollback must be reachable from a *raised* run, not only from a clean
one. The COO half's rollback (re-put from `.scratch/drafting_v1_preact/<key>.json`) satisfies this
**provided the pre-act snapshot precedes the FIRST write, which its AC5 states.** COVERED.

**3b. `build_drafting_document()` -- the composing branches:**

- **Every key, always:** exactly five section objects (`pipeline.py:52`, `:158`, `:172`; schema
  `minItems: 5, maxItems: 5`). `ceo_bio` always carries its `absent` block
  (`drafting_build.py:227-229`). A limb with nothing to draft ships an **empty** `sentences` list,
  never fabricated content (`pipeline.py:9-10`).
- **Sentence REFUSED by evidence validation** (empty / unknown / foreign / stale id, or a record
  with no passage text -- `pipeline.py:93-110`): dropped, counted in `dropped`, reason in
  `dropped_reasons`. **Unchanged by this cell.**
- **Sentence with a span that does not clear its cited passage:** `"REFUSE"` -> dropped
  (`pipeline.py:138-142`). **Unchanged by this cell.**
- **Sentence with a span that clears:** shipped with `verbatim_check="PASS"`. **Unchanged.**
- **Sentence with NO span:** `"PASS"` today (`verbatim.py:60-61`); **HELD after the cell.** This is
  the whole diff.
- **Regeneration:** `refused != 0` re-enters the `while attempt <= max_attempts` loop
  (`pipeline.py:163-168`). Every caller in the corpus passes `max_attempts=1`
  (`drafting_build.py:221`, `run_drafting.py:79`), so the loop cannot fire and a HELD sentence
  cannot cause a re-draft. **No blast radius; stated so it is not re-derived at the call site.** If
  the cell implements HOLD as a `refused += 1` **and** any caller is left on the `max_attempts=2`
  default (`pipeline.py:147`), the producer runs twice per section for no gain -- wasted work, not
  a widening, because `FilingsProducer` is deterministic (`pipeline.py:41-44`).

**3c. Which branch each COO expectation rests on, and whether the half covers both:**

| COO half's expected outcome | rests on | both branches covered? |
|---|---|---|
| "A sentence with a verbatim span anchored in its source: SERVED unchanged" | 3b, clears-its-passage | **YES** -- the refuse arm is also named ("dropped") and is pre-existing |
| "`served_no_span` = 0 for EVERY rebuilt key" | the new HOLD rule | **YES** as an assertion; but see D3 -- the half does not say what happens to the held sentence, and the two answers have different blast radii |
| "the served sentence set for BA shrinks or is equal, NEVER grows" | 3b + the deployed adapter | **NO -- see D3.** There is a third reachable outcome: not "grows", but **INVALID**, i.e. the served set for that key goes to *nothing at all across all five limbs*. |
| "the route still `200`" | `read_drafted_sections` returns a block on every path (`scoped_amgt.py:1594-1657`), including ABSENT and INVALID | **YES** -- `200` is preserved on every branch, which is exactly why `200` is not a discriminator here and the per-key `drafting_status` must be read beside it |
| "NO model call" | `drafting_build.py:9`, `:177` | **YES, confirmed at source** |
| "NO Lambda redeploy" | AC7 read-only invoke | **YES** -- and load-bearing; see D3 |

### 4. WRITER CENSUS CROSS-CHECK

**The COO half prints: `N = 1 writer at HEAD` -- "`drafting_build.py`'s writer ... `pipeline.py`
composes, `drafting_build.py` puts."**

**I measure `N = 2`. The COO half's N is wrong and so is its mechanism.**

**Instrument** (different from the COO's, per Rule 22 -- I do not know what instrument produced the
COO's 1): `comp-find 'drafting/v1' --all --limit 60` -> **DENOMINATOR: 306 hits across 66,307 files
scanned, corpus=all**; then `comp-find 'write_pool' --all --limit 80` -> **162 hits, DEF=11**; then
a single-file `grep -n 'drafting/v1'` over the three named files. Writers of the key
`drafting/v1/<security_key>.json`:

1. **`lib/research/filings/analyze.py:1215`** -- inside `main()`'s `payloads` list; written at
   `:1219-1224` when `--write-pool` is given. Composed at `:1171` from `build_drafting_document`,
   imported at `:56`.
2. **`lib/research/filings/batch.py:150`** -- inside `run_one()`'s tuple; written at `:152` when
   `write_pool` is true. Composed at `:143`.

**`drafting_build.py` is NOT a writer.** It contains no `boto3`, no `put_object` and no
`write_pool` in any of its 248 lines. The COO half names the composer as the putter and counts the
composer instead of the writers.

⭐ **THE RATIFIED TEXT PRINTS THE SAME 2, AT THE SAME LINES.** `C-VERBATIM-GATE`, PRD `:918`,
verbatim: *"The rule binds BOTH writers of `drafting/v1/<key>.json` (`batch.py:150`,
`analyze.py:1215`)."* **Third instrument, independent of both of us:** the round-13 analysis's own
round-14 cell table gives `R14-F5` the obligation *"one writer of `drafting/v1`"*
(`ledger/ROUND_ANALYSIS.round13.md`, chain F row F5) -- an obligation that is only coherent if
there is more than one today. So three instruments agree on 2 and one (the COO half) says 1.

**What follows from 2, and why it is not fatal to the act.** Both writers call **the same
composer**, `build_drafting_document` (one `DEF`: `comp-find 'build_drafting_document' --all` ->
**39 hits, DEF=1, `drafting_build.py:212`**; `analyze.build_drafting_document` at `batch.py:143` is
that same object re-exported through `analyze.py:56`, not a second implementation). So the HOLD
rule, landed in `build_drafting_document` / `pipeline.py` / `verbatim.py`, **binds both writers by
construction** -- this is Rule 22's shared-dependency check run deliberately, and it passes. **Two
writers, one composing rule. Both numbers must be stated or the census is misread either way.**

**One more correction to the census's reasoning, not its conclusion.** The COO half discharges the
schedule with: *"`OpalResearch-FilingsAnalyzer` is DISABLED and writes analysis objects, not
drafting"*. The **second clause is false at source**: that task's launcher is
`lib/research/filings/run_batch.cmd`, which runs `python -m lib.research.filings.batch --universe
universe/v1/2026-09-15.json --write-pool`, and `batch.py:150` writes the drafting key. **The task
IS a writer of `drafting/v1`.** The conclusion (no schedule writes it today) still holds, but it
rests on **DISABLED alone** -- so the disarm is a device-plane state that `rk-42` is separately
re-registering, not a property of the write set. State it as the enabled-flag, or a future enable
silently acquires a third write path into this prefix. *(APPLIED-plane confirmation that the task
is DISABLED is the COO half's, not mine; I have not read the device.)*

### 5. WHAT THIS HALF DOES NOT COVER

- **Any model call, any SEC fetch, any EDGAR/vendor egress.** `C-FILINGS-ANALYZER` `:690-693`:
  *"NO FLEET RUN AND NO RE-RUN until the process is validated end to end ... Stale analyses stay
  stale. A validation run needs his per-use word."* Nothing in this half authorizes one.
- **Any rebuild of a key outside the measured population**, and any write to `filings/v1/...` (the
  source and analysis objects) -- those are untouched.
- **Any change to `lib/research/api/scoped_amgt.py`** (chain B's file), **and any redeploy of
  `opal-amgt-scoped-api`.** The COO half cites the adapter's validator as `:1483-1514`; I read
  those bytes at HEAD and the citation lands correctly inside `_validate_drafting_document`
  (`:1461-1514`). ⚠ **And the no-redeploy is LOAD-BEARING, not incidental:** after the cell, the
  repo's `verbatim.py` carries the new rule while the deployed Lambda carries the old one. The
  served outcome depends on that skew. A later redeploy makes the adapter hold at READ time as
  well -- **a different act, over a different (larger) key set, needing a new pair.**
- **Any change to `lib/research/drafting/schema.json`.** Note for the cut, not a bar: that file's
  `quoted_spans` description (`:108`) still states the SUPERSEDED rule -- *"a paraphrase carries an
  empty list and verbatim_check is vacuously PASS ... Passage support and exact quotation are
  SEPARATE outcomes"* -- which PRD `:917` explicitly reverses. If the cell leaves it, the contract
  file documents the rule the gate no longer follows.
- **The DESCRIPTION LINE's served value.** `scoped_amgt.py:2574-2585` takes
  `company_description` **sentence[0]** as the description line. If that sentence is the one held,
  the description line's `status`/`source` move for that name **without any adapter change**. The
  COO half's blast radius says *"Nothing else moves: no analysis object, no filings source object,
  no adapter"* -- true of the adapter's CODE, and true of no other object; **but a second served
  FIGURE moves, on the same route, from the same rewritten bytes.** It belongs in the blast radius.
- **`drafting_status` itself.** Under the drop-shaped implementation a key whose every sentence
  lacks a span becomes `SERVED` with five empty limbs -- **the status does not move while the prose
  goes to zero.** The split counters are the only thing that marks it (`C-MARK-NOT-DEGRADE`,
  PRD `:923`). This half does not cover a page-level decision about an empty SERVED pack.
- **Where the rebuild READS the analysis from.** The COO half's `--population` names the crosswalk,
  not the analysis source. The analyses live at `filings/v1/{security_key}/{accession}.analysis.json`
  (PRD `:681`), so the driver must resolve an **accession per key** and pick one when a key has
  more than one. **UNVERIFIED and unbindable from source, because the driver does not exist.** The
  order must bind the read prefix and the accession-selection rule, or the rebuilt content is
  selected by whatever `list_objects_v2` happens to return first.
- **The APPLIED plane entirely:** the denominator 12, the live pre-act bytes and their sha256, the
  scheduled task's DISABLED state, `comp-schedule`'s 0 matches. Those are the COO half's and I did
  not re-measure them (no AWS read, no producer run, per this task's constraints).

---

## THE FOUR DISAGREEMENTS, CONSOLIDATED

**D1 -- THE ACT'S INVOCATION DOES NOT EXIST AT HEAD, AND ITS FAILURE MODE IS `rc=0`.**
`python -m lib.research.filings.drafting_build` on the HEAD module has **no `__main__` guard**, so
Python imports the module, binds its defs, **ignores every argument** and exits **0, having written
nothing**. A worker running the COO half's literal invocation before the cell builds the CLI gets a
clean exit and an unchanged pool, and nothing says so. *(UNVERIFIED BY EXECUTION -- I did not run
it; that would be a producer invocation. The claim is read from the absence of an entry point in a
whole-file read of all 248 lines and from the corpus census in s.2.)* **Remedy: the order states
that the cell BUILDS the entry point, and the proof carries a negative control that the rebuild
refuses / reports when handed an empty population, so a silent rc=0 cannot be read as success.**

**D2 -- THE WRITER CENSUS IS 2, NOT 1** (s.4). Three instruments against the COO half's one.
Not fatal: both writers share one composer. **Remedy: print `N = 2 writers, 1 composing rule`.**

**D3 -- THE SIGN-BLOCKING ONE: A THIRD BRANCH, NEITHER "SHRINKS" NOR "GROWS".**
Neither half says **what happens to the held sentence in the written object**, and the two
available shapes have different blast radii against the **deployed** adapter (which is NOT
redeployed):

- **Shape A -- HELD = dropped from `sections[].sentences`**, counted in `dropped` and in a new
  top-level split block. Schema-legal (top-level `additionalProperties: true`, schema `:11`);
  every surviving sentence carries `verbatim_check="PASS"`; the deployed adapter re-runs the OLD
  gate over the survivors (`scoped_amgt.py:1497-1499`), gets `"PASS"`, and `:1507` matches.
  **Document stays SERVED, sentence set shrinks. The COO half's outcome holds exactly.**
- **Shape B -- HELD = kept in the object with a third `verbatim_check` value** (e.g. `"HELD"`),
  or in an in-`sentences` held block. **EVERY REBUILT DOCUMENT GOES INVALID**, by two independent
  mechanisms in the deployed adapter:
  1. `schema.json:101-102` -- `verbatim_check` is `"enum": ["PASS", "REFUSE"]`. A third value
     fails `jsonschema.validate` at `scoped_amgt.py:1478` -> `(False, "marking contract: ...")`.
  2. Even if the enum is widened in the repo, the **deployed** Lambda carries the old schema and
     the old gate: `scoped_amgt.py:1507-1513` refuses when `sentence["verbatim_check"] != verdict`,
     and the old `check_against_sources` returns `"PASS"` for an empty span list
     (`verbatim.py:60-61`, `:75`, `:79`). Shipped `"HELD"` vs re-run `"PASS"` -> **REFUSE.**

  `read_drafted_sections` then returns `drafting_status = INVALID` (`scoped_amgt.py:1612-1618`),
  and **the whole drafting block is lost for that key -- all five limbs, plus the description line
  at `:2574-2585`, which gates on `DRAFTING_SERVED`.** The route still answers `200`, so the COO
  half's `200` check does not discriminate it.

**So the act can, on one legal implementation choice, take twelve served documents to zero served
prose without touching one line of the adapter and without any redeploy** -- and the COO half's
never-widen axis ("shrinks or is equal, never grows") reads GREEN on that outcome, because zero is
a shrink. **A half must cover both branches or it is not signed (CLAUDE.md s.5 NEVER-1).**
**Remedy, one line in the order, and I will sign on it:** *the rebuild ships only `PASS` sentences
in `sections[].sentences`; the held sentences are carried in a top-level block and in the printed
split, and no sentence in `sections[].sentences` carries a `verbatim_check` outside
`["PASS","REFUSE"]`* -- i.e. **Shape A is bound, Shape B is refused at the cut.** With that line,
D3 closes and the COO half's outcome is exact.

**D4 -- s.3.8 AND `C-VALIDATION-NAMES`: TWO SEPARATE BARS, AND THE COO HALF ADDRESSES ONLY ONE.**
The COO half asks this seat directly whether `ROUND_ANALYSIS.round13.md` s.3.8 bars the gate
re-apply on the 11, and stakes AC6/AC7 on the answer.

- **On s.3.8 itself: it does NOT bar the gate re-apply.** Its bytes (`:104-107`) defer *"Rebuilding
  drafting from stale analyses"* on the stated ground that *"Rebuilding drafting from stale
  analyses buys nothing"* -- and its subject is the **driver points** the old analyses never
  emitted, re-opened *"only after the analyzer is validated (R14-F6)"*. The gate re-apply is a
  different purchase: it removes unanchored served prose (FWD-9 / V6-D18), which is `R14-F4`'s own
  obligation in the same table. ⚠ **But the distinction the COO half draws -- "the gate re-apply is
  NOT the content rebuild" -- is not one the CODE makes:** there is one function, and re-applying
  the gate means re-running `build_drafting_document` whole over the stale analysis and rewriting
  the object's content. The distinction holds on PURPOSE, not on mechanism, and the half should say
  so in those words. **On this bar: AC6/AC7 stand.**
- **On the bar the COO half does not raise: `C-VALIDATION-NAMES` (PRD `:1652-1656`), verbatim:**
  *"Every round-14 cell is proven on the three validation names ... or on a dry run ... **no cell is
  a fleet run or a re-run of the covered population** before it passes (Andrew-direct ~16:3xZ, *"I
  dont care about rerunning until the process is completely validated end to end"*)."* The
  round-13 analysis repeats it for round 14 as a whole ("**No cell is a fleet run or a re-run**").
  A twelve-key rewrite of the covered population is, on the plain reading, the thing that sentence
  names. A narrower reading is available -- that "re-run" means re-running the *analyzer* (the
  vendor/model path Andrew was answering about), and a no-vendor pure transform is not a run at all.
  **Both readings are live and the difference is 9 keys.**
  ⛔ **THIS IS NOT MINE TO SETTLE IN EITHER DIRECTION.** It is Andrew's word carried in ratified
  text; relaying it wider or narrower is the widening that creates the question (CLAUDE.md s.2).
  **This half covers the act on the three validation names' keys without reservation.** For the
  remaining keys it covers the act's blast radius as written **but records that the authorization
  question is open and is the ISSUER'S to close before spawn** -- by carrying the narrow reading
  explicitly in the order with its basis, or by Andrew's per-use word. **No new gate is created
  here; the bar already exists in ratified text.**

---

## WHAT I WOULD SIGN

With **D3's one line bound in the order** and **D2's census corrected to `N = 2 writers, 1
composing rule`**, this half signs as written, with D1's negative control and D4's
`C-VALIDATION-NAMES` disposition named by the issuer. Without D3, the pair leaves a reachable
branch uncovered and **this half does not stand**.

`1.0.0_SA_CTO~Z` -- see the CTO SIGNATURE block at the end of this file.
`9a6aa12da2`.

---

## STANDING CLAUSE -- BINDS EVERY CELL IN THIS CHAIN (added at signature, 2026-09-18 ~22:4xZ)

**THE WRITE ADDRESS COMES FROM THE BUILDER, AND A HAND-TYPED KEY IS NOT COVERED BY THIS HALF.** Every S3 address a cell in
this chain writes is `lib/opal_naming.py` `address()` output and every resource name is `name()` output (Rule 30), and the
worker's proof carries the builder's PRINTED address, never a typed one. - **The commit gate cannot catch the violation:**
measured by `4.0.0_SA_CRO~Z`, relayed by `0.0.0_AB_MSTR~Z`, the naming gate is ENFORCING (`org/mcp/naming-gate.enforce`
@`d181e0ac5a`, read at `safe-commit.sh:691` -- CLAUDE.md Rule 30's "WARN today" is stale), but its GRADER IS WIDER THAN THE
BUILDER: a hand-typed key of the shape `bloomberg/amgt/bronze/...` PASSES the commit gate while `address()` REFUSES the same
key. A worker that types an address therefore gets a GREEN commit and a key no reader resolves.
**Also measured, and the reason a builder call may REFUSE today:** AMGT has no `scopes.json` row at all (9 rows, none
`amgt`, `harvest` or `resapp`), so `address()` returns an `opal-data-harvest` address in 0 of 1350 scope x source x tier
combinations. A refusal is the EXPECTED state until the registry row lands: it is a BLOCKING row and a named refusal, never
a hand-typed workaround (Rule 30). Andrew-direct ~21:45Z: *"opal-data-assets is solely for client data ... the whole
pipeline will exist within opal-data-harvest"*.


## CTO SIGNATURE -- chain F

**Drafted by a reviewing subagent of this seat; every BLOCKING item was RE-VERIFIED at source by `1.0.0_SA_CTO~Z` before
this signature** -- D1 (whole-file read of `drafting_build.py`: no `argparse`, no `main()`, no `__main__` guard, no put, 248
lines), D2 (`analyze.py:1215` and `batch.py:150` as the two writers, with PRD `:918` naming the same pair), and all three of
D3's mechanisms (`lib/research/drafting/schema.json:101-102` `"enum": ["PASS", "REFUSE"]`; `verbatim.py:60-61` `if not
span: return True`; `scoped_amgt.py:1507-1513` refusing when the shipped `verbatim_check` differs from the gate's re-run).

- `AMGT-rk-41`: **WITHHELD ON ONE LINE.** D3 is a reachable branch the pair does not cover: if the held sentence stays in
  `sections[].sentences` carrying a third `verbatim_check` value, every rebuilt document goes INVALID against the DEPLOYED
  adapter -- all five limbs AND the description line -- while the COO half's "shrinks or is equal, never grows" and its
  `200` check both read GREEN, because zero is a shrink. **TO SIGN, one line in the order:** the rebuild ships only `PASS`
  sentences in `sections[].sentences`, the held ones are carried in a top-level block and in the printed split, and no
  sentence in `sections[].sentences` carries a `verbatim_check` outside `["PASS","REFUSE"]`. With that line bound, this half
  signs as written. D1's negative control (an empty population must REPORT, never exit 0 silently) and D4's
  `C-VALIDATION-NAMES` disposition are the issuer's to carry in the order text.
- **D4 is NOT settled here and is not this seat's to settle:** whether a twelve-key rebuild of the covered population is the
  "re-run of the covered population" ratified text forbids. This half covers the act on the three validation names without
  reservation; for the other keys it covers the blast radius but records the authorization question as OPEN at the issuer,
  closed either by carrying the narrow reading explicitly with its basis, or by Andrew's per-use word.

Signed `1.0.0_SA_CTO~Z`, 2026-09-18, against the COO halves at `9a6aa12da2`.

---

## RE-SIGNATURE -- 2026-09-18 ~23:3xZ, against the COO halves at `541d395e0d` (msg 23855's re-cut)

`2.0.0_SA_COO~Z` bound every withheld condition in the order text and restated it in its halves. This seat read the
BOUND TEXT at `541d395e0d`, not the message's summary of it, before lifting each withholding.

- **`AMGT-rk-41`: WITHHOLDING LIFTED -- SIGNED.** D3's one line is bound verbatim at `541d395e0d` chain F `:38-39`: the
  rebuilt document ships ONLY `PASS` sentences in `sections[].sentences`, every held sentence in a top-level block, and no
  `verbatim_check` outside {PASS, REFUSE} reaches the adapter -- which closes the branch that would have taken every
  rebuilt document INVALID while both stated controls read GREEN. D1's negative control (an empty population REPORTS,
  `rc 3`, never a silent `rc 0`) and D4's disposition are bound with it: the live rebuild runs `--only-keys` over the three
  validation names, so the twelve-key question my half recorded as OPEN does not arise in this cell and no reading of
  `C-VALIDATION-NAMES` is stretched to permit it.

Re-signed `1.0.0_SA_CTO~Z`, 2026-09-18 ~23:3xZ.
