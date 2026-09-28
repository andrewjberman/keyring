# AMGT_RESAPP task order -- `AMGT-tt-3` -- THE AC4 SAMPLE, CHOSEN AGAINST ITS CLAUSES AND CAPTURED FRESH

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-tt-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~164</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reads of Opal's own deployed function (GET routes and its configuration); nothing is granted.
comp-adversary: RUN by the issuer at the cut -- the adversarial arm is a sample optimised for one clause that leaves the others unreachable (round 44's own finding): AC1 requires the members' stated clauses to cover a, b and c, and every member exercising b or c to carry px_last and a post-deploy fixture. Blind spot, stated: the render itself is the issuer's close run on 5174, graded at L9.
EGRESS CLASS, declared: ONE AWS READ SURFACE -- lambda invoke of Opal's own opal-amgt-scoped-api (GET routes) and get_function_configuration; no write, no vendor.
</preflight>

## 1. THE CELL -- `AMGT-tt-3` (round 45, decomposition s.53)

Round 44's judgment criterion asked whether each SERVED case value "reads as a price in a named currency, the same on both
surfaces". It has three clauses: **(a)** the value names a currency; **(b)** the same value on the page and in the export; **(c)** it
reads as a price (the value against the name's own `px_last`). Round 44's three names (RKT, AMD, GOOGL) were chosen for currency
variety: they reached (a), reached (b) only on a fixture captured BEFORE the change, and reached (c) on 1 of 3. **Choose the sample
against the whole clause set, and capture it fresh.**

Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~164/AC4_SAMPLE.json`, shaped `{"members": [...]}`, at least
three members, each carrying: `security_key`; `clauses` (which of "a", "b", "c" this member exists to exercise); `why` (one sentence);
`crncy`; `base_line` (the served export's "Base case: SERVED -- ..." line, verbatim); `px_last` and `ratio` (= value / px_last) for
every member exercising b or c; `fixture` (a repo path under your deliverables folder). Across the members: all three clauses, at least
two currencies, and at least one of round 43's first-mint names (AMD, GOOGL, LLY, PWR, UNH).

Each `fixture` is a served capture of that name from the DEPLOYED function, keyed the way `portal/scripts/ui-contract-check.mjs` reads
it: the six route keys `/api/scoped/amgt/security/BA_US_Equity/thesis`, `/api/scoped/amgt/watchlist`,
`/api/scoped/amgt/lead-panel/rankings/trending/chatter`, `/api/scoped/amgt/lead-panel/timeseries/trending/chatter`,
`/api/scoped/amgt/security/BA_US_Equity/overlay`, `/api/scoped/amgt/security/BA_US_Equity/peers` (the instrument navigates to BA
only, so the member's own payloads sit under BA's keys), plus `_provenance` {`served_from`, `captured_at` (UTC ISO, now),
`code_sha256` (the deployed function's CodeSha256 read at capture)}. The served capture library the sweep uses
(`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py`, `load_capture_lib`) reads those routes.
Round 43's `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/real-run-rkt.fixtures.json` is the shape to follow.

## 2. BOUNDS

1. **Reads only.** No write to AWS, no deploy, no server (the issuer renders on 5174), no vendor call, no S3 delete.
2. You change nothing but your deliverables folder.
3. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~164/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-tt-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/tt-3.AC1.py; echo "exit=$?"</invocation><expect>members >= 3; clauses covered ['a', 'b', 'c']; currencies >= 2; first-mint members >= 1; defects 0 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-tt-3" judgment="true"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/tt-3.AC2.sh; echo "exit=$?"</invocation><expect>each member's clause, served Base case line, px_last and ratio, for a person to judge beside the issuer's renders of the same fixtures on 5174 (round45/real-run-<key>/model.png) whether each value reads as a price in a named currency, the same on both surfaces; RECORDED, no verdict</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~164/AMGT_RESAPP.TO-AMGT-tt-3.the-ac4-sample-chosen-against-its-clauses.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.6 items 1 and 2. Base: AC1 FAILS (no sample). The render on 5174 is the issuer's close run (no worker runs vite); AC2 is graded at L9 against those renders.

<status>pending</status>

<status>complete</status>

**WORKER CLOSE (`0.9.0_WK_AMGT_RESAPP~164`):** AC4_SAMPLE.json written with 3 members (RKT_LN_Equity clauses a,b; AMD_US_Equity
clauses b,c; GOOGL_US_Equity clauses a,c) covering all three clauses, 2 currencies (GBp, USD), 2 round-43 first-mint names
(AMD, GOOGL). Each fixture freshly captured from the deployed opal-amgt-scoped-api (lambda:Invoke, read-only) into the six
route keys ui-contract-check.mjs reads, keyed under BA_US_Equity per the note in round43's shape, with `_provenance.captured_at`
2026-09-26T18:5x:xxZ (after the rs-2 deploy) and `code_sha256` LK9h47juBfZPaAyfztAxDe9z65W2ZtEw6H2IJ/DcO4s=. base_line strings
produced by calling `lib.research.print.render_pack._model_case_line` directly (byte-identical to the page/export renderer) on
each fixture's own thesis `model_cases.base` and header CRNCY figure. AC1: members 3; clauses covered ['a', 'b', 'c'];
currencies 2; first-mint members 2; defects 0; exit=0. AC2: recorded, no verdict (judgment). No surprise row filed (no premise
failure, no missing writer, no capability gap encountered).
<round>45</round>
<slot>~164</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
