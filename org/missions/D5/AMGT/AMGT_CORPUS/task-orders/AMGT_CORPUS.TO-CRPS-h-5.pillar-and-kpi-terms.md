# AMGT_CORPUS task order -- `CRPS-h-5` -- ROUND 6: each thesis pillar and each KPI row names its TERMS, drawn only from the pillar's own heading and the KPI vocabulary, never generated

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-h-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~5</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 1 drift candidate, on data/black_diamond; 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- the new mode reads S3 and writes nothing; the continuation rewrite is the issuer's drain act.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~5`**, slot `~5` of round 6. Serves **FWD-18**'s DATA half: "Each pillar and KPI row names its
terms". The header feed and Chatter filter that consume the terms are a page, not this project: out of scope.

## 1. THE CELL -- `CRPS-h-5`

**Where this came from.** `lib/research/corpus/continuation.py` produces the per-name continuation artifact. Its
`thesis_pillars` field is a list of `{"citation": {...}, "pillar": <the heading, e.g. "Strong pipeline">, "text": <the
passage>}` (built at `continuation.py:428` and `:586`); its `kpi_set` field is a dict of KPI names (e.g. `FCF`, `NIM`,
`ARR/RPO/backlog`, 25 of them), each `{"citations": [...], "count": n}`. `METHOD_VERSION = "amgt-corpus-continuation/1"`
(`:127`). The dossier copies these fields unchanged, so the dossier needs no edit. The word `terms` occurs 5 times in
`continuation.py` today, none of them a pillar field.

**RULED -- what you build:**
- Each pillar gains `terms`: a list whose FIRST member is the pillar's own heading (the `pillar` string, stripped), followed
  by every KPI-vocabulary term found in the pillar's `text` as a whole word, case-insensitively, in order of first appearance,
  each spelled as the vocabulary spells it, no duplicates. The KPI vocabulary is the lexicon the module already loads from
  `KPI_LEXICON_PATH` (`continuation.py:147`, the same names that key `kpi_set`), each name split on `/` into its parts (so
  `ARR/RPO/backlog` contributes `ARR`, `RPO`, `backlog`). Nothing else becomes a term.
- Each `kpi_set` row gains `terms`: its name split on `/`, stripped, in order.
- `METHOD_VERSION` becomes `"amgt-corpus-continuation/2"`.
- A read-only mode `python -m lib.research.corpus.continuation --show-terms --security-key <key>` builds that one name's
  continuation IN MEMORY with the same code path `--write` uses, writes NOTHING, and prints one line per pillar
  `pillar <heading> terms <t1>|<t2>|...`, then the one summary line
  `pillars <p> with_terms <p1> kpi_rows <k> with_terms <k1>`.
- `lib/research/corpus/tests/test_continuation_terms.py` (new): the heading comes first; a KPI term inside a longer word is NOT
  matched (`NIM` in `NIMBLE`); case-insensitive match with the vocabulary's spelling kept; the `/` split; no duplicates; the
  method version; `--show-terms` makes no put.

## 3. SURFACES

<paths>
lib/research/corpus/continuation.py
lib/research/corpus/tests/test_continuation_terms.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-h-5.pillar-and-kpi-terms.md
</paths>

READ-ONLY: every other `lib/research/corpus/` module, `dossier.py` included. Scratch `.scratch/h5/`.

## 4. BOUNDS
- Pure ASCII in code, LF, Python 3.9-compatible; pillar text may carry non-ASCII, so any read you add is explicit
  `encoding='utf-8'`. NO S3 write: never run `continuation --write` or `dossier --write` for real.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W5-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-h-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h5_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-h-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h5_AC2.sh</invocation><expect>(?m)^pillars ([1-9]\d*) with_terms \1 kpi_rows (\d+) with_terms \2$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-h-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h5_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-h-5" judgment="true"/>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: AstraZeneca's live continuation, built in memory, names terms on every pillar and
  every KPI row; AC3 the bound: the corpus suite still passes.
- **AC4 (JUDGMENT, the CVO's, at L9 on the issuer's served rewrite -- nothing for you to produce):** are a pillar's terms
  readable as that pillar's theme, and is every term traceable to the heading or the KPI vocabulary with none invented? The
  sample is a FLOOR and names every venue present (R-1): at least one London, one US, and one Asian listing.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/AMGT_CORPUS.TO-CRPS-h-5.pillar-and-kpi-terms.proof_of_spec.json`
   (AC4 as a declared exclusion; the checker admits no judgment row).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's pillar lines and summary line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-5 analysis s.5 item 6 @`37217d8053` and the CTO's re-measurement (msg 25973: `continuation.py` is the
producer). PRD FWD-18 is PROPOSAL/LATER; its feed-filter clause sits on the page, the seam `@64d0a493ac` measured for
FWD-10/11/15, so it is not cut. The served rewrite (95 continuations, then every dossier whose inputs move) is the issuer's
drain act under a never-widen pair, AFTER h-1 drains (Z-S42). Checks dry-run at the base: AC1 FAIL (no such file), AC2 FAIL
(no such flag), AC3 bound.

<risk>SERVED</risk>
<status>pending</status>
<round>6</round>
<slot>~5</slot>
<fabric>site-z</fabric>
