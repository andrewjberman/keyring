# AMGT_RESAPP.TO-AMGT-r-4 -- THE SA COVERAGE RE-EXERCISE: the coverage reader run over the SA raw that has now landed -- a RIDE of the sound reader, not a re-write

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-r-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~2</issued_to>

## THE CELL, INLINED IN FULL (round 2, FWD-4; fixes AMGT-s-4's AC7 NOT_EVALUATED)

```
AMGT-r-4. THE SA COVERAGE RE-EXERCISE. AMGT-s-4's reader is sound and complete; its AC7 was
NOT_EVALUATED only because SA raw had 0 keys at grade time. AMGT-s-b4 has since landed 18 raw objects
across 3 tickers (BABA/RTX/+1) under raw/seekingalpha/. This cell RE-EXERCISES the landed reader over
that real SA content -- it does NOT re-write the reader.

WHAT TO PRODUCE, under lib/research/coverage/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~2/:

  (a) THE RE-RUN  run the landed reader (lib/research/coverage/reader.py, from AMGT-s-4) over the SA raw
      AMGT-s-b4 landed, for the tickers that have raw: coverage_items_<key>.json now carry SA-class items
      keyed by the identity layer, ranked by recency then frequency, each admitted PASS|REFUSE|PROVISIONAL
      by AMGT-s-11's held-back item rule (PROVISIONAL is honest at this cut). run_summary.json records
      sa_raw_keys_found as the real count (>= 3), not 0.

  (b) THE INVARIANTS STILL HOLD ON REAL SA CONTENT: the F11 redirect trap never stores a redirect as a
      domain; an item from a source whose identity is UNRESOLVED for that security is NOT attached
      (render_together's rule); the unscoped shared-defect pass still refuses two securities with an
      identical item set. If the reader needs a small adaptation to INGEST the SA JSON shape (the
      virtual_analysts/articles bodies), that adaptation is inside lib/research/coverage/ and is the
      minimum to read the landed artifact -- never an HTML parse (C-SA-NAMED-SOURCE: the API JSON is the
      source), never a new fetch.
```

## DEPENDENCIES

**NONE among the round-2 cells.** Reads AMGT-s-b4's landed raw (raw/seekingalpha/, 3 tickers already
resolved in the identity layer), AMGT-s-12's identity layer, and AMGT-s-11's item rule -- all landed.
Independent of AMGT-r-12 (the 3 SA tickers are already MEASURED; it does not wait on the coverage pass).

## BOUNDS

```
⛔ G-24 / C-VENDOR-EGRESS: NO NEW VENDOR CALL. Read ONLY the SA raw AMGT-s-b4 already LANDED. No SERP, no
Bright Data, no SA fetch. AC4.
⛔ NO HTML PARSING (C-SA-NAMED-SOURCE as amended): the raw JSON bodies are the source. AC4 refuses a
parser.
⛔ C-IDENTITY-RESOLVED: an item whose source identity is UNRESOLVED for the security is not attached.
⛔ C-RULE-MUST-EXIST: the item rule is applied as AMGT-s-11 shipped it (held_back, PROVISIONAL); no
threshold invented.
⛔ THIS IS A RE-EXERCISE, NOT A RE-WRITE: change the reader only as far as ingesting the landed SA JSON
requires; do not re-architect AMGT-s-4's engine.
⚠ Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
AMGT-s-b4 (landed @3be9d03962): 18 raw objects / 3 tickers under raw/seekingalpha/<key>/<stamp>/; sa_ids
    MEASURED for BABA (137271), RTX, +1; the report bodies carry createdAt/previousReportDate.
L10 analysis @4d31cf4caa s.2 (FWD-4): "s-4 AC7 NOT_EVALUATED -- its bar needs SA raw landed, which had 0
    at grade time and 18 objects/3 tickers since: a round-2 RE-RUN of an exercisable criterion, not a defect".
AMGT-s-4 (landed): reader.py, the F11 trap in extract_display_domain(), the unscoped pass, the item rule
    applied held-back. Its AC5/AC6 negatives (no vendor host, no HTML parse) still bind here.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/coverage/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-r-4.sa-coverage-re-exercise.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~2/`. AMGT-s-b4's landed raw, AMGT-s-12's identity
layer, AMGT-s-11's item rule and AMGT-s-4's reader are READ.
A path missing from that block is a path you are REFUSED on. Refuse a criterion you cannot satisfy as
written and report the refusal with its measurement; file a surprise ROW (`AMGT_RESAPP-Z-W2-S<k>`
continuing your sequence, project AMGT_RESAPP, fabric site-z) and STOP on that criterion if you need a
surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-r-4"><invocation>python -c "import json,glob; fs=glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/coverage_items_*.json'); sa=sum(1 for f in fs for i in json.load(open(f))['items'] if i.get('source_class')=='sa'); k=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/run_summary.json'))['sa_raw_keys_found']; print('sa keys found at run', k, '| sa-class items', sa)"</invocation><expect>"sa keys found at run" of 3 or more (NOT 0 -- the landed raw was read) AND "sa-class items" of 1 or more -- the reader ingested the real SA content AMGT-s-b4 landed; 0 keys or 0 sa items means the raw was not read and is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-r-4"><invocation>python -m pytest lib/research/coverage/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "5 passed" with no "failed" -- the reader's invariants still hold WITH real SA items in play: ranking, the F11 trap (difference arm), the unscoped pass refuse+admit, and the identity gate refusing an UNRESOLVED-source attachment; a regression here is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-r-4"><invocation>python -c "import json,glob; bad=0; n=0; [ (n:=n+1, bad:=bad+(1 if ('google.com/url' in (i.get('display_domain') or '') or (i.get('display_domain') or '').startswith('http')) else 0)) for f in glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/coverage_items_*.json') for i in json.load(open(f))['items']]; print('items', n, 'with a redirect or URL stored as the domain', bad)"</invocation><expect>"with a redirect or URL stored as the domain 0" -- NEGATIVE: F11's trap did not reach the output even with SA items ingested</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-r-4"><invocation>grep -r -c -i -E 'brightdata|serp_opal|seekingalpha\.com|requests\.get|urllib\.request|httpx|BeautifulSoup|lxml|html\.parser' lib/research/coverage/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no vendor host, no HTTP client, no HTML parser under the module; the re-exercise reads LANDED raw JSON only (G-24, C-SA-NAMED-SOURCE)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-r-4" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical): the reader ran on real SA content -- the count that was 0 at round-1 grade time is now real. FWD-4's SA half, exercised.
- **AC2** (mechanical, difference arms): the invariants survive real SA items.
- **AC3** (mechanical, NEGATIVE): F11's trap stayed caught.
- **AC4** (mechanical, NEGATIVE): no fetch, no HTML parse -- the re-exercise added no vendor egress.
- **AC5** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): read one SA-class item in the ranked list -- is its PROVISIONAL verdict carrying a reason a reader could act on, and does the ranking read as "most recent, most discussed" now that real SA items are in it?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>2</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.3 + L6 round 2) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L10 round-1 analysis @4d31cf4caa -> L5 recut decomposition v0.3 @3d2d7af6e0 (section 10, AMGT-r-4) -> this round-2 issuance.
**Chain:** round 2, an independent chain of one.
**Provenance:** the cell text is decomposition v0.3 section 10a's AMGT-r-4 row; the defect is s-4 AC7 NOT_EVALUATED and the L10 analysis s.2/s.4.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-24 binds this cell (no new vendor call).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 analysis @4d31cf4caa is the recut's authority; round-1's 10/10 stands at its vintage.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act.
</preflight>
**Preflight disposition:** a re-exercise of a landed reader over landed raw; the battery is not re-run because no new gate/IAM/vendor plane is touched (the SA raw was already landed and authorized under s-b4's word).
