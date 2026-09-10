# AMGT_RESAPP.TO-AMGT-s-b4 -- THE SEEKING ALPHA BACKEND: the ETL on the MEASURED route -- the parked session ridden by REST through the residential proxy, raw JSON landed, tested ONCE, never scheduled

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-b4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~9</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-4; manifest row S4, the SA half)

```
AMGT-s-b4. THE SEEKING ALPHA BACKEND -- the ETL that procures SA content for a ticker by the MEASURED
route (C-SA-NAMED-SOURCE as amended at v0.3; the reference @b1656bbebc): GET /api/v3/symbols/{ticker}
-> sa_id; GET /api/v3/virtual_analysts/{sa_id} (the report as JSON, carrying createdAt and
previousReportDate); GET /api/v3/symbols/{t}/analysis|news -> GET /api/v3/articles/{id}. NO HTML
parsing on the path. Rides the parked session through the residential proxy with the full
browser-minted cookie jar AND a per-ticker Referer (C-SA-SESSION-SHAPE); a 200 with a 2-byte body is
a FAILURE, a small-challenge 403 is a RE-HARVEST signal and never an auth failure; no POST through
the proxy (C-SA-NO-POST-THROUGH-PROXY); the credential and the session are LOCATED in Secrets
Manager at run time and no name is hardcoded. Raw JSON lands in the version store before any
derivation. Tested ONCE on a stated small ticker set inside the exploration word; NOT scheduled and
NOT served in production (C-SA-VENDOR-WORD); the comparison is DISCHARGED and not re-run
(C-SA-ROUTE-COMPARISON); the five unmeasured limits are carried, not assumed (C-SA-UNMEASURED), and
the terms question is Andrew's. The seven-Lambda archive estate is not this fetch path.

THE REFERENCE, BY ANDREW'S WORD (@d09e26e1b1: "this is just what should be referenced for any TOs
associated with SA news procural for this project"):
    org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md  @b1656bbebc
READ IT IN FULL BEFORE WRITING A LINE. Its scripts are the starting point and you EXTEND them, never
rebuild (the build ladder: the estate already has it):
    org/tier1_exec/4.0.0_SA_CRO/scripts/sa_harvest_session.py   (the harvester -- NOT run by this order)
    org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py        (the rider -- the thing you turn into an ETL)

WHAT TO PRODUCE, under integrations/seekingalpha/ (a new integrations folder, the estate's home for a
vendor surface, mirroring integrations/bloomberg/) and .../deliverables/0.9.0_WK_AMGT_RESAPP~9/:

  (a) THE FETCHER  integrations/seekingalpha/rest_fetch.py -- from sa_rest_fetch.py: for a ticker,
      symbols/{ticker} -> sa_id; virtual_analysts/{sa_id}; symbols/{ticker}/analysis and /news ->
      articles/{id} for the first N articles (N stated, small). EVERY request: the full cookie jar
      from the parked session (the PX cookies included) AND a per-ticker Referer header, egress
      through the residential proxy, GET only. The session and the credential are read from Secrets
      Manager by NAMES SUPPLIED IN CONFIG (integrations/seekingalpha/config.json carries the secret
      names; the code reads config; AC5 refuses a literal in code).

  (b) THE TWO DETECTORS, each a function with a fixture test:
      - empty_body(response): a 200 whose body is under 8 bytes -> FAILURE (the 2-byte trap). Never
        a silent empty row.
      - reharvest_signal(response): a 403 whose body is small (a few hundred bytes) and carries the
        challenge marker -> RE-HARVEST, never AUTH-FAIL. On this signal the ETL STOPS the run, writes
        status REHARVEST_NEEDED, and does NOT call the harvester (C-SA-UNMEASURED: headless untested;
        MFA unadapted; the harvester is a headed-browser act on this box and is a later order).

  (c) THE LANDING (raw before derived): every response body lands untouched at
          s3://opal-data-research/raw/seekingalpha/<security_key>/<YYYYMMDDTHHMMSSZ>/<endpoint>.json
      and the sa_id map is written to .../deliverables/0.9.0_WK_AMGT_RESAPP~9/sa_ids.json as
      {ticker: {sa_id, slug, status: MEASURED, measured_at}} -- the persisted key AMGT-s-12's identity
      layer consumes.

  (d) THE ONE TEST RUN, inside the exploration word (@ee0eacab07 "testing SA etl"; C-SA-VENDOR-WORD:
      exploration AUTHORIZED, recurring or production NOT): at most THREE tickers from the coverage
      universe, chosen by a stated rule, ONE run, paced at 1 request per 2 s or slower (C-SA-UNMEASURED:
      rate limits unmeasured -- do not go faster than the investigation did). Record every request in
      request_log.json with status code and body length.

  (e) NOT SCHEDULED, NOT SERVED: no EventBridge rule, no cron, no Lambda, no trigger of any kind is
      created by this order (AC6). The ETL is a script a person runs. Production use awaits Andrew's
      word and the terms question, which is his and not yours.
```

## DEPENDENCIES

`AMGT-s-12` (the identity layer defines the record your sa_ids feed) and, in the world, `AMGT-s-6` (the
store). This slot (~9) spawns after AMGT-s-12 lands, as the ninth chain -- the list register (Q5) is the
deferred chain under the cap, not this one.

## BOUNDS -- what this cell may not cross

```
⛔ C-SA-VENDOR-WORD (PRD v0.3 s.3a, L4's ruling with its author): the EXPLORATION and the test are
authorised; recurring or production use is NOT. One run, at most three tickers, then stop. AC4 and AC6.

⛔ C-SA-ROUTE-COMPARISON is DISCHARGED: do NOT fetch the modal page, do NOT try the cookieless unlocker,
do NOT re-compare. Both are measured unworkable in the reference.

⛔ C-SA-SESSION-SHAPE: full jar + per-ticker Referer, through the residential proxy. Identity cookies
alone return 403; the full jar with no Referer returns 200 with a 2-byte body. Both traps are FIXTURES
in your tests (AC2), not lessons in a comment.

⛔ C-SA-NO-POST-THROUGH-PROXY: GET only. The residential zone refuses every POST (policy_20130); a
login can never complete through it. AC5's grep refuses a .post( anywhere in the module.

⛔ THE HARVESTER IS NOT RUN BY THIS ORDER. A dead session is a REHARVEST_NEEDED status and a row, never
a headed-browser run, never a sign-in, never a Kimi call. The parked session was minted at 19:29Z with
an unmeasured TTL; if it has expired when you run, that IS the measurement -- record it.

⛔ NO SECRET NAME IN CODE, NO SECRET VALUE ANYWHERE. The names come from config.json; the values are
read at run time and never logged, printed, or written to a deliverable. The reference lists which
secrets it touched and printed none; you print none.

⛔ THE TERMS QUESTION IS ANDREW'S (C-SA-UNMEASURED). Nothing in this order reads the vendor's terms or
rules on them; the ETL is a test, not a posture.

⛔ THE SEVEN-LAMBDA ARCHIVE ESTATE (seeking-alpha-*-scraper/coordinator/dedup, LIVE-no-DECLARED) is NOT
touched, NOT invoked, NOT extended. It is an archive producer for a parked estate (brief PART II).

⚠ BOUND EVERY CALL under `timeout 120`; three tickers x (1 symbol + 1 report + 1 listing + N articles)
at 2 s pacing fits in a few minutes across several invocations -- one ticker per invocation.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
THE REFERENCE @b1656bbebc (read in full; the numbers below are ITS, cited): the account endpoint
    returns authorizedUser with an active annual pro subscription; virtual_analysts/{sa_id} returned
    200 for six tickers at 7.8-8.8 KB each; the full 65-cookie jar through the residential proxy was
    never challenged; the native IP was blocked after ~10 calls; every POST through the proxy is refused
    (policy_20130); the jar with no Referer returned 200 with a 2-byte body; a 413-byte 403 with
    blockScript in the body is the re-harvest signal; Secrets Manager holds seeking-alpha/session
    (17,202 bytes, 65 cookies) and seeking-alpha/credentials.

comp-find 'seeking-alpha' --corpus aws (vintage 12:24:50Z): 34 nodes -- 7 Lambdas LIVE-no-DECLARED,
    2 daily rules, 1 role, 1 secret at that vintage (the session secret was created after it). None of
    those Lambdas is on your path.

comp-iam stats (RUN): six services already carry secretsmanager:GetSecretValue as a GAP -- the shape a
    scheduled consumer's grant would take. Not this order's: a script a person runs reads the secret as
    that person's principal. If a later order schedules it, that is the grant to cut then.

comp-schedule (RUN to completion): 25 gates armed, none this project's; G-20 (no scheduled anything)
    and G-24 (through C-SA-VENDOR-WORD) bind this cell.

Interpreter: `python` on PATH = Python311 with boto3 importable; the reference's scripts ran under it.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
integrations/seekingalpha/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-b4.seeking-alpha-backend-the-measured-route.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~9/`. The reference and its two scripts are READ
(copy sa_rest_fetch.py into your module as the starting point; the CRO's folder is not your write
surface). Secrets Manager reads, the proxy and S3 writes are operational and not path-gated.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W9-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-b4"><invocation>python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~9/check_landing.py</invocation><expect>one line of the exact shape "SA LANDING: tickers 3; raw objects &lt;n&gt; across 3 keys; symbol+report present for 3 of 3; sa_ids MEASURED 3" -- read back from S3 and sa_ids.json by this script, never from the fetcher's own log; a ticker with no report object, or an sa_id not MEASURED, is NOT met -- and a run that stopped on REHARVEST_NEEDED records that status as its finding and leaves this criterion NOT met, never rescued by a harvest</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-b4"><invocation>python -m pytest integrations/seekingalpha/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "4 passed" with no "failed" -- the four fixture tests: a 200 with a 2-byte body is classified FAILURE; a 200 with a real body is classified OK (the difference arm); a small-body 403 with the challenge marker is classified REHARVEST; a plain 401/403 without it is classified AUTH_FAIL -- the two traps the reference measured, each with its pass twin</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-b4"><invocation>python -c "import json; l=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~9/request_log.json')); r=l['requests']; print('requests', len(r), '| with Referer', sum(1 for x in r if x.get('referer')), '| via proxy', sum(1 for x in r if x.get('via_proxy')), '| non-GET', sum(1 for x in r if x.get('method')!='GET'), '| min gap s', round(min((r[i+1]['t']-r[i]['t']) for i in range(len(r)-1)),2) if len(r)>1 else 'n/a')"</invocation><expect>"with Referer" and "via proxy" both EQUAL to "requests", "non-GET 0", and a "min gap s" of 2.0 or more -- every request carried the per-ticker Referer, went through the residential proxy, was a GET, and the pacing never went faster than the investigation's (C-SA-SESSION-SHAPE, C-SA-NO-POST-THROUGH-PROXY, C-SA-UNMEASURED)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-b4"><invocation>python -c "import json; l=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~9/request_log.json')); print('unique tickers', len(set(x['ticker'] for x in l['requests'])), '| runs', l['runs'])"</invocation><expect>"unique tickers" of 3 or fewer and "runs 1" -- NEGATIVE: one test run on a stated small set, inside the exploration word and not beyond it (C-SA-VENDOR-WORD)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-b4"><invocation>grep -r -c -E 'seeking-alpha/session|seeking-alpha/credentials|\.post\(|virtual_analyst_report|scrape_as_markdown|one_shotter|password' integrations/seekingalpha/*.py | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE and structural: no secret name as a literal in code (config carries it), no POST, no modal-page fetch, no unlocker, no password handling anywhere in the module</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-b4"><invocation>grep -r -c -i -E 'aws_cloudwatch_event|aws_scheduler|schedule_expression|cron\(|rate\(|EventBridge|aws_lambda_function' integrations/seekingalpha/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: nothing under the module declares a schedule, a rule or a Lambda; the ETL is a script a person runs, and production use awaits Andrew's word (G-20; C-SA-VENDOR-WORD)</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-s-b4" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical, read from S3): three tickers landed on the measured route, sa_ids measured for the identity layer.
- **AC2** (mechanical): both traps are fixtures with pass twins -- the 2-byte body and the re-harvest signal cannot ship silently.
- **AC3** (mechanical, a census over the log): every request had the Referer, rode the proxy, was a GET, and was paced.
- **AC4** (mechanical, NEGATIVE): one run, three tickers. The word's edge.
- **AC5**, **AC6** (mechanical, NEGATIVE, structural): no secret literal, no POST, no modal, no unlocker, no schedule, no Lambda.
- **AC7** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): read the landed virtual_analysts JSON for one ticker beside the reference's description of it -- does the ETL preserve createdAt and previousReportDate untouched (FWD-6's what-changed axis, served by the source), and does the deliverable state plainly which of C-SA-UNMEASURED's five limits this run could and could not observe?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output -- one ticker per invocation, paced.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2</round>
<slot>~9</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-2 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance. Andrew's three words: @ee0eacab07 (the SA word), @8c609decf7 (the hold), @d09e26e1b1 (the release and the reference).
**Chain:** Q9, `AMGT-s-b4` alone; slot ~9 spawns after `AMGT-s-12` lands. The ninth chain against the cap of eight; the deferred chain is Q5 (the list register), not this one.
**Provenance:** the cell text is the decomposition v0.2's row verbatim. The "tested ONCE, three tickers, never scheduled" bound is this issuer's application of C-SA-VENDOR-WORD (L4's ruling) to Andrew's own "testing SA etl": a test is inside the exploration word; a schedule is not. The harvester exclusion is C-SA-UNMEASURED read literally -- headless and MFA are untested and a worker is not the seat to test a headed-browser vision loop.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's; G-20 and G-24 (via C-SA-VENDOR-WORD) bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; six services carry secretsmanager:GetSecretValue as a gap -- the shape a scheduled consumer would need and this order does not create
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; no route touched by this order
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this order
comp-find --corpus aws: RUN -- 'seeking-alpha' 34 of 2382 nodes at 12:24:50Z; the 7 archive Lambdas are not on this path
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a script under integrations/ and objects under a new bucket prefix; no deployed resource is created or changed (AC6 refuses one).
