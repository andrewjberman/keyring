# AMGT_RESAPP task order -- `AMGT-rk-41` -- the verbatim gate closed: a drafted sentence with no verbatim span is HELD, never served; every pass count prints its split

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-41</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~43</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; no schedule is read
  or written; the scheduled batch task stays DISABLED and is not touched.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to the already-provisioned pool prefix `drafting/v1/` in
  `opal-data-harvest` through the existing `crosswalk.write_pool` path under the credentials this project already
  writes with; it grants no permission, provisions no resource and touches no Terraform. No Lambda is redeployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~43`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and every path in
section 3 exists; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~43;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-41` (R14-F4; FWD-9, FWD-18; validation V6 / D18)

**The analysis row, verbatim (ROUND_ANALYSIS.round13.md s.4 @9c8e04cd9a):** *"the verbatim gate closed: every drafted
sentence carries a verbatim span or is held; pass counts report vacuous vs on-span"* -- serves FWD-9, FWD-18, V6/D18;
co-sign: yes (served prose).

**THE CARD IS ANSWERED -- HOLD.** Analysis s.5 card 5 asked whether a sentence with no verbatim span is HELD or served
LABELLED. Andrew-direct ~19:4xZ, verbatim *"Agreed, yes."* to the REC HOLD (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md`, frame card 4:
*"HOLD. Such a sentence is held and never served; the label interim ends. Every pass count still prints its split"*).
PRD v0.13 @1699960261 `C-VERBATIM-GATE` `:907-920`, verbatim where it binds: *"EVERY PASS COUNT PRINTS ITS SPLIT: passed
on a span / passed with NO span / held"*; *"A drafted sentence with no verbatim span is HELD: never served, and counted in
the split (v0.12, Andrew-direct ~19:4xZ, "Agreed, yes."). Over today's 12 served documents this withholds 179 of 389
sentences (46%, measured 2026-09-18 by `4.0.0_SA_CRO~Z`, msg 23744); the validation names ran 17 of 39 (CAT) and 16 of
40 (CSL)"*; *"The rule binds BOTH writers of `drafting/v1/<key>.json` (`batch.py:150`, `analyze.py:1215`)"*; *"a span
pointed at the neighbouring passage, and a one-character mutation of a passing span, must both be REFUSED"*. **No
LABEL interim is built and no switch exists: the rule is HOLD.**

**1.1 The measured current state (read at HEAD; `lib/research/filings/` last moved @db6c40083f).**
- **D18, the hole:** `lib/research/drafting/verbatim.py:53-62` `is_verbatim()` returns True for an EMPTY span
  ("vacuously verbatim"); `check_against_sources()` `:65-79` therefore returns `"PASS"` for a sentence whose
  `quoted_spans` is `[]`; `pipeline.py:122-144` `_gate_sentences()` appends every such sentence to `passed` with
  `verbatim_check="PASS"` (`:143`). `drafting_build.py:212-248` `build_drafting_document()` counts `verbatim_pass`
  (`:243`) and `quoted` (`:244`) side by side but never SPLITS the pass count, and its own docstring `:44-46` says a
  sentence with no run "is vacuously PASS". `schema.json:105-109` documents the same. Measured: CAT 17 of 39 and CSL
  16 of 40 served sentences pass with no span; over the 12 served documents, 179 of 389 (46%).
- **The served plane reads the object as shipped:** `lib/research/api/scoped_amgt.py:1483-1514`
  `_validate_drafting_document()` re-runs `check_against_sources` per sentence and compares with the shipped
  `verbatim_check`; `:1594-1650` `read_drafted_sections()` serves every sentence of a valid document with its
  `quoted_spans`; `:2574-2592` builds the DESCRIPTION line from `company_description` sentence 1 (C-DESCRIPTION-LINE,
  v0.12: Bloomberg's field FIRST, a drafted sentence only past a describes-the-business test). `lib/research/posture/
  packs.py:107` reads `drafting/v1/<key>.json` as the Thesis D-1 input of a posture pack.
  WARNING: **OUT OF THIS CELL, named so nobody assumes it:** the adapter's validator would still ACCEPT a zero-span sentence
  (`check_against_sources([], ...)` is PASS at `:1496-1500`). After this order no writer emits one; making the adapter
  refuse one is a served-plane change in `scoped_amgt.py` (chain B's file, a Lambda redeploy) and is NOT in this
  order's paths -- the COO places it. AC4 below is a READ-SIDE assertion that discriminates, not an adapter change.
- **Two writers of `drafting/v1/<key>.json`, COUNTED:** `batch.py:150` and `analyze.py:1215` (N = 2, measured by a
  repo-wide census: no third `.py` writes the literal `drafting/v1/`; `posture/packs.py:107` and
  `scoped_amgt.py:1336` READ it). `AMGT-rk-42` collapses them into ONE writer, `analyze.write_outputs(...)`; this
  order's rebuild (1.3) writes THROUGH that writer, so this order depends on `AMGT-rk-42` having landed.
- **The population of record:** `crosswalk/v1/2026-09-15.json` MEASURED = 33; the served drafting set is the subset of
  those 33 whose `filings/v1/<key>/<accession>.analysis.json` exists (12 today) -- never a `drafting/v1/` listing
  (`C-PRODUCTION-HOME` `:1617-1618`).
- **s.3.8 of the analysis, placed:** the other 11 `drafting/v1` objects derive from analyses written before the driver
  points existed; rebuilding them to GAIN content is DEFERRED (R14-F6). This order rebuilds them only to APPLY THE GATE
  -- a deterministic pass over the stored analyses with NO model call (the `AMGT-rk-19` producer-half precedent: a
  re-apply over already-stored objects) -- and gains nothing else from them.

**1.2 What you build.**
1. `lib/research/drafting/pipeline.py`: `_gate_sentences()` classes every sentence into exactly one of REFUSED
   (validation or verbatim failure, as today), **HELD-NO-SPAN** (`quoted_spans` empty after validation -- NOT appended
   to `passed`, recorded under `held_no_span` with `section`, `text`, `evidence` and
   `reason: "no verbatim span: HELD (C-VERBATIM-GATE v0.12, Andrew-direct ~19:4xZ)"`), or SERVED-ON-SPAN (appended with
   `verbatim_check="PASS"` and `anchored: true`). `run_pipeline()` returns `held_no_span` (the list) and
   `held_no_span_count` beside `dropped`. `verbatim.py` is NOT edited: `is_verbatim("")` staying True is harmless once
   an empty list never reaches the gate as a served sentence, and `AMGT-rk-40` owns that file.
2. `lib/research/filings/drafting_build.py`: the document carries `held_no_span` and denominators
   `sentences_drafted`, `served`, `served_on_span`, `served_no_span` (MUST be 0), `held_no_span`, `refused`
   (`== dropped`), `verbatim_pass` (kept for readers; `== served`), and `split: "served_on_span/held_no_span/refused"`.
   Its docstring `:22-46` is rewritten to say HOLD. `schema.json` gains `held_no_span` (optional) and `anchored`; the
   `quoted_spans` description `:108` no longer says vacuous PASS.
3. A CLI on `drafting_build.py`: `--analysis PATH --report` prints the split for one analysis object;
   `--rebuild-pool --population crosswalk/v1/2026-09-15.json [--dry-run] [--pre-act-dir DIR]` walks the population's
   MEASURED keys, reads each key's newest `filings/v1/<key>/*.analysis.json` from the pool, rebuilds the drafting
   document under the new gate, and -- without `--dry-run` -- writes it through `analyze.write_outputs(...,
   drafting_only=True)` after saving the PRE-ACT bytes and their `document-sha256` (from `head_object`) of every key it
   will touch to `--pre-act-dir`. Prints per key: served_on_span / held_no_span / refused, pre-act sha256, post-act
   sha256, read-back; then `REBUILT k of 33 (N no analysis: ABSENT with reason)`. `--dry-run` writes nothing anywhere.
4. Tests in `lib/research/drafting/tests/test_drafting.py` and `lib/research/filings/tests/test_filings.py`: the
   planted arms in AC1. `test_filings.py:363`'s `assertEqual(sentence["verbatim_check"], "PASS")` now runs over SERVED
   sentences only, and a new assertion says served sentences all carry a non-empty `quoted_spans`.

**1.3 The deploy: served prose MOVES -- co-sign, change-management entry, rollback.** Rebuilding the 12 served
`drafting/v1` objects withholds about 179 of 389 sentences (re-measured at the act, AC5): the Thesis tab's drafted
prose, the description line's drafted route and any future posture pack change for those keys. **Before the first
live write (AC6):** (1) a FRESH never-widen pair on file -- the CTO half (`1.0.0_SA_CTO~Z`) and the COO half
(`2.0.0_SA_COO~Z`) -- each naming the blast radius as the 12 keys AC5 prints (and no other), the readers
(`scoped_amgt.py:1594` thesis bundle, `:2574-2592` description line, `posture/packs.py:107`), **the writers of the
property COUNTED (N = 1 after `AMGT-rk-42`; N = 2 before it -- print which)**, the expected outcome READ FROM THE
PRODUCER'S OWN RULE (every served sentence carries a span; a document whose every sentence is held still serves its
five sections with empty sentence lists and `held_no_span_count`, never INVALID -- both branches covered), and a
per-key rollback FROM THE LIVE PRE-ACT sha256 OF THIS ACT (never a prior act's); (2) the change-management entry under
`org/critical_paths/change_management/` opened and COMMITTED (not staged), naming the 12 keys, the pre-act sha256 per
key from `head_object`, and the rollback (`crosswalk.write_pool` of the saved pre-act bytes per key); closed on
completion with the post-act sha256 per key. Per NEVER-2 the entry is never left open. **If either half is not on file,
STOP before AC6 and file a row -- AC1-AC5 are complete without it.**

**1.4 The validation bar (`C-VALIDATION-NAMES`).** The COO's instruction for this cell: *on the validation names, 0
served sentences without a span; held count printed with denominator; planted negative: an unanchored sentence in the
served bundle is a FAIL.* CAT is the validation name proven live (one EDGAR fetch by CIK 18230 through the EXISTING
`fetch.py` path and one two-pass analysis, about USD 0.65 -- within the bar; cap USD 2.00 for this order); the planted
negative is AC4. NO fleet run, NO analyzer re-run on any of the 33: the rebuild in AC6 is a gate re-apply over STORED
analyses with no model call.

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.4 row R14-F4 @9c8e04cd9a, s.3.8 (placed), s.5 card 5
(ANSWERED HOLD); validation V6/D18 (@b527b93214). PRD v0.13 @1699960261: `C-VERBATIM-GATE` `:907-920`,
`C-FILINGS-ANALYZER` `:693-696` (the drafting reader validates, then runs the gate against the passage), FWD-9 (S9
`:1273`), `C-PRODUCTION-HOME` `:1617-1618` and `:1643-1650`, `C-VALIDATION-NAMES` `:1652-1658`. The COO's round-14
decomposition record for this cell in `AMGT_RESAPP_DECOMP.md` is the postulate paragraph landed beside this order.

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain F is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_F_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_F_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-41`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-41` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

**ISSUER BINDS on `1.0.0_SA_CTO~Z`'s withheld half (msg 23833, D1/D3/D4):** (D3) the rebuild ships ONLY `PASS`
sentences in `sections[].sentences`; every HELD sentence is carried in a TOP-LEVEL `held_no_span` block and in the printed
split, and NO sentence in `sections[].sentences` carries a `verbatim_check` outside `["PASS","REFUSE"]` -- a third value
there takes every rebuilt document INVALID against the DEPLOYED adapter while the shrink check reads GREEN; AC6's expect
carries this as a printed per-key line `sections_values <set>` that must read a subset of {PASS, REFUSE}. (D1) an EMPTY
population or an empty key set REPORTS (`REBUILT 0 of 0 -- nothing to do`, rc 3), never exits 0 silently. (D4, the issuer's
reading, carried with its basis) a rebuild of the twelve served `drafting/v1` objects of the COVERED population is a
producer re-run over covered names, which Andrew's standing word bars until the process is validated end to end (*"I dont
care about rerunning until the process is completely validated end to end"*): so the LIVE rebuild in AC6 runs with
`--only-keys CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity` (the validation names; a key with no analysis object yet -- `rk-38`
not drained -- is reported NOT ATTEMPTED with that reason, never a FAIL), and the twelve covered keys are DRY-RUN only (AC5
prints their split and pre-act shas; nothing is written). The covered rebuild is re-opened after end-to-end validation on
Andrew's word, under a fresh pair. The CLI gains `--only-keys K1,K2,...` (step 3).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/drafting/pipeline.py
lib/research/drafting/schema.json
lib/research/drafting/tests/test_drafting.py
lib/research/filings/drafting_build.py
lib/research/filings/tests/test_filings.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~43/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-41.verbatim-gate-hold.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_F_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant; this block governs WRITES. In
  `drafting_build.py` you own `draft()` `:188-209`, `build_drafting_document()` `:212-248`, the docstring `:22-46` and
  the new CLI; `:70-128` (the run finder and `quoted_spans`) are `AMGT-rk-40`'s. `verbatim.py` is `AMGT-rk-40`'s.
  `analyze.py` and `batch.py` are `AMGT-rk-42`'s (you CALL `analyze.write_outputs`; you do not edit it).
  `scoped_amgt.py` is chain B's. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~43 <0.9.0_WK_AMGT_RESAPP~43@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Never push, merge, rebase, `checkout --`, `stash` or `clean`.
- **THE POOL WRITE:** `drafting/v1/<key>.json` for the keys AC5 prints, through the ONE writer, after 1.3's gates.
  No Lambda redeploy: the adapter reads the object at request time.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** Secrets through `comp-secrets` only (the model key for AC2, per `analyze.py:226-231`). **EGRESS,
EXACTLY:** one EDGAR fetch (CAT, CIK 18230) and one two-pass Anthropic analysis of CAT under USD 2.00; nothing else.
**No non-ASCII in anything you write.** **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with
`0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- serving a labelled unanchored sentence is that
route.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- re-measure 389 / 179 / 12 fresh
(AC5); they may have moved.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W43-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it)
and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-41"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest discover -s lib/research/drafting/tests -p "test_*.py" -q 2>&1 | tail -3 && python -m unittest discover -s lib/research/filings/tests -p "test_*.py" -q 2>&1 | tail -3</invocation><expect>both runs end "Ran N tests" and "OK", including the planted arms: (1) a sentence with valid evidence and quoted_spans [] is HELD -- absent from the section's sentences, present in held_no_span with its reason -- and held_no_span_count is 1; (2) the same sentence with a span its passage carries is SERVED with verbatim_check PASS and anchored true; (3) a span pointed at the NEIGHBOUR passage is REFUSED and counted in dropped; (4) a one-character MUTATION of a passing span is REFUSED; (5) the split sums: sentences_drafted equals served plus held_no_span plus refused, and served_no_span is 0; (6) the fixture's drafted document is still schema-valid and every served sentence carries a non-empty quoted_spans</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-41"><invocation>cd "$(git rev-parse --show-toplevel)" && export ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal | grep '^value:' | sed 's/^value:[[:space:]]*//')" && python -m lib.research.filings.fetch --security-key CAT_US_Equity --cik 18230 --form 10-K --cache-dir .scratch/filings_cache 2>&1 | tail -2 && python -m lib.research.filings.analyze --security-key CAT_US_Equity --source-json .scratch/filings_cache/CAT_US_Equity.source.json --no-fetch --cache-dir .scratch/filings_cache --out-dir .scratch/cat --stage pass1 2>&1 | tail -3 && python -m lib.research.filings.analyze --security-key CAT_US_Equity --source-json .scratch/filings_cache/CAT_US_Equity.source.json --no-fetch --cache-dir .scratch/filings_cache --out-dir .scratch/cat 2>&1 | tail -6</invocation><expect>the validation name live under the new gate (the two analyze invocations are the pass-1 cache split, analyze.py:308-317): SOURCE prints CAT's 10-K accession and hashes; the DRAFTING line prints the SPLIT -- served_on_span S, held_no_span H, refused R over sentences_drafted D with D = S + H + R and served_no_span 0 (the validation measured 17 of 39 held before this gate existed; print the fresh figures); USD under 1.00; NOT-UPLOADED lines (no --write-pool)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-41"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import glob, json, os, shutil
os.makedirs('.scratch/cat_root', exist_ok=True)
src = glob.glob('.scratch/cat/drafting_v1_CAT_US_Equity.json')[0]
shutil.copy(src, '.scratch/cat_root/CAT_US_Equity.json')
os.environ['AMGT_DRAFTING_ROOT'] = os.path.abspath('.scratch/cat_root')
from lib.research.api import scoped_amgt
block = scoped_amgt.read_drafted_sections('CAT_US_Equity')
sents = [s for sec in block['drafted_sections'] for s in sec['sentences']]
no_span = [s for s in sents if not s.get('quoted_spans')]
doc = json.load(open('.scratch/cat_root/CAT_US_Equity.json', encoding='utf-8'))
print('drafting_status', block['drafting_status'], 'source', block['drafting_source'], 'served', len(sents), 'served_without_span', len(no_span), 'held_no_span_on_object', len(doc.get('held_no_span') or []), 'denominators', json.dumps(doc.get('denominators')))
raise SystemExit(1 if no_span else 0)
"</invocation><expect>the served bundle for the validation name, read through the adapter's OWN offline root (scoped_amgt.py ENV_DRAFTING_ROOT :1331, the same object the pool would serve): drafting_status SERVED, source local, served N, served_without_span 0, held_no_span_on_object H greater than 0 with the object's denominators printed, rc 0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-41"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, os
doc = json.load(open('.scratch/cat_root/CAT_US_Equity.json', encoding='utf-8'))
planted = dict(doc['sections'][1]['sentences'][0]); planted['quoted_spans'] = []; planted['text'] = 'PLANTED: an unanchored sentence that cites real evidence but quotes nothing.'
doc['sections'][1]['sentences'].append(planted)
os.makedirs('.scratch/cat_planted', exist_ok=True)
json.dump(doc, open('.scratch/cat_planted/CAT_US_Equity.json', 'w', encoding='utf-8'))
os.environ['AMGT_DRAFTING_ROOT'] = os.path.abspath('.scratch/cat_planted')
from lib.research.api import scoped_amgt
block = scoped_amgt.read_drafted_sections('CAT_US_Equity')
sents = [s for sec in block['drafted_sections'] for s in sec['sentences']]
no_span = [s for s in sents if not s.get('quoted_spans')]
print('drafting_status', block['drafting_status'], 'served', len(sents), 'served_without_span', len(no_span))
raise SystemExit(1 if no_span else 0)
"</invocation><expect>THE PLANTED NEGATIVE: one unanchored sentence injected into a copy of the served document; the adapter still serves it (drafting_status SERVED -- the adapter change is out of this cell, section 1.1) and the SAME assertion as AC3 reads served_without_span 1 and exits rc 1 -- the read-side check discriminates, so AC3's 0 is a measurement and not a vacuity</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-41"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.drafting_build --rebuild-pool --population crosswalk/v1/2026-09-15.json --dry-run 2>&1 | tail -16</invocation><expect>the PRE-ACT split over the population of record, read-only: one line per MEASURED key with an analysis in the pool -- served_on_span / held_no_span / refused and the LIVE pre-act sha256 of its drafting/v1 object -- then "REBUILT (dry-run) k of 33; N ABSENT (no analysis object)", with k re-measured (12 at the cut) and the totals printed against the served total (389 at the cut; the CRO measured 179 held). Nothing is written: the line "DRY-RUN: no pool write, no file write" is printed</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-41"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.drafting_build --rebuild-pool --population crosswalk/v1/2026-09-15.json --only-keys CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity --pre-act-dir .scratch/drafting_v1_preact 2>&1 | tail -16</invocation><expect>THE DEPLOY on the VALIDATION NAMES ONLY (issuer bind D4; the covered twelve stay DRY-RUN), run only after section 1.3's pair is on file and the change-management entry is committed: per key the pre-act sha256 (matching AC5's), the post-act sha256 and read-back VERIFIED through the one writer; "REBUILT k of 3" with k = validation names carrying an analysis object (0 reported NOT ATTEMPTED per name with the reason if rk-38 has not drained -- not a FAIL); every rebuilt object's served_no_span 0, held_no_span_count printed, and its per-key line sections_values reading a subset of {PASS, REFUSE} (bind D3); a covered-population key written by this run is NOT met; the pre-act bytes of every touched key saved under .scratch/drafting_v1_preact/ (the rollback input named in the entry). If the pair or the entry is absent, this criterion is REFUSED with that reason and nothing is written</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-41"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
lam = boto3.client('lambda')
payload = json.dumps({'rawPath': '/api/scoped/amgt/security/BA_US_Equity/thesis', 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
resp = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
body = json.loads(resp['Payload'].read())
inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
sents = [s for sec in inner.get('drafted_sections', []) for s in sec.get('sentences', [])]
print('statusCode', body.get('statusCode'), 'drafting_status', inner.get('drafting_status'), 'served', len(sents), 'served_without_span', sum(1 for s in sents if not s.get('quoted_spans')), 'held_uncited_count', inner.get('held_uncited_count'), 'provenance_dropped', (inner.get('drafting_provenance') or {}).get('dropped'))
"</invocation><expect>ISSUER REPAIR (2.0.0_SA_COO~Z, on row W43-S1; consistent with bind D4): BA_US_Equity is a COVERED key and D4 keeps the covered twelve DRY-RUN this round, so the served plane for BA must be UNCHANGED by AC6 -- the before and after reads are IDENTICAL: statusCode 200 both, drafting_status SERVED both, served and served_without_span EQUAL before and after (21 of 38 at the cut; re-measure), the counts printed side by side. That equality is this criterion's never-widen control: the validation-names rebuild touched nothing served. A BA count that MOVED is NOT met (something wrote a covered key). The zero-unanchored state for BA is re-opened with the covered rebuild after end-to-end validation, under a fresh pair, as D4 says</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-rk-41"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.drafting_build 2>&1 | tail -3; echo "rc=${PIPESTATUS[0]}"; python -m lib.research.filings.drafting_build --rebuild-pool --population crosswalk/v1/2026-09-15.json --no-such-flag 2>&1 | tail -2; echo "rc=${PIPESTATUS[0]}"</invocation><expect>THE ENTRY POINT EXISTS AND REFUSES A BAD CALL (CTO msg 23830: at HEAD the module has no main, no argparse and no __main__ guard, so python -m on it exits 0 having done nothing -- a GREEN that proves nothing): the first call prints argparse usage naming --analysis, --report, --rebuild-pool, --population, --dry-run, --pre-act-dir and exits rc=2; the second call prints "unrecognized arguments: --no-such-flag" and exits rc=2; neither call reads the pool or writes anything (this criterion runs BEFORE AC5). An exit of 0 on either call is NOT met</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
**AC6 and AC7 run AFTER the never-widen pair and the change-management entry exist, never before.**

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~43/AMGT_RESAPP.TO-AMGT-rk-41.verbatim-gate-hold.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7` (rc 0 is the verdict); close the
change-management entry with the post-act sha256 per key; flip `<status>` to `complete`; commit with `--only --
<paths>`. Report once, with the pre/post split totals.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>14</round>
<slot>~43</slot>
<fabric>site-z</fabric>
