# AMGT_RESAPP.TO-AMGT-s-13 -- THE SOCIAL FEED: MEASURE, THEN BUILD -- the measurement PLAN that one call executes when the per-use word arrives, the feed contract with its disclosure, and the social-item rule on fixtures; NO dataset is triggered by this order because it carries no word

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~6</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-11; manifest row S13; verb: measure, then build)

```
AMGT-s-13. THE SOCIAL FEED -- MEASURE, THEN BUILD. The first act EXERCISES the Bright Data datasets
surface that nobody has: trigger one post-level dataset, observe a record, its cost, field schema,
latency, freshness, and whether it can be queried by cashtag at all; the criterion is that
MEASUREMENT. A feed follows only if the measurement admits one, under the social-item rule from
`AMGT-s-11`, with the cashtag-native absence (F13) stated on the feed's own source line.

FWD-11's bar, verbatim: "An analyst sees social discussion admitted by a written rule. DONE WHEN
EXERCISED -- an analyst has read the feed and can point at why an item was admitted."

⛔ C-LISTING-NOT-CAPABILITY (PRD s.3): "NOTHING ABOUT THE SOCIAL DATASETS HAS BEEN EXERCISED. F12
measured they are LISTED and reachable: 1,763 datasets, HTTP 200. No dataset was triggered, no record
returned, no cost, field schema, latency or freshness observed, and whether the post-level sources can
be queried by cashtag at all is unknown. A LISTING IS A CATALOGUE ENTRY, NOT A CAPABILITY. The first
social cell's job is to find out, and its acceptance criterion is allowed to be a measurement rather
than a feature."

⛔ AND THE MEASUREMENT IS A VENDOR CALL THIS ORDER DOES NOT CARRY THE WORD FOR. Triggering a Bright
Data dataset is exactly what G-24 / C-VENDOR-EGRESS forbids without Andrew's explicit per-use word,
and no such word exists for this cell. So THIS ORDER'S DELIVERABLE IS THE MEASUREMENT READY TO RUN --
one command, one dataset, one company, a stated cost cap -- and the feed's contract; the trigger
itself is the NEXT order, cut the moment the word arrives. A criterion demanding the trigger from this
order would be one a correct build cannot satisfy, and it is not written.

WHAT TO PRODUCE, under lib/research/social/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~6/:

  (a) THE MEASUREMENT PLAN  .../MEASUREMENT_PLAN.md + lib/research/social/measure.py (built, not run):
      - the dataset ids it would trigger, CITED from the brief's F12 (X (formerly Twitter) - Posts
        gd_lwxkxvnf1cynvib9co; Reddit - Posts gd_lvz8ah06191smkebj4; Reddit - Comments
        gd_lvzdpsdlw09j6t702; LinkedIn company information gd_l1vikfnt1wgvvqz95w; Yahoo Finance business
        information gd_lmrpz3vxmz972ghd7) -- ONE of them for the first run, chosen and stated;
      - the ONE company (from AMGT-s-12's universe) and the query shape (cashtag? company name? handle?)
        for each attempt, in order, with the stop rule;
      - the OBSERVABLES, each with how it is read: cost (the account's usage delta, before/after),
        field schema (the first record's keys), latency (request-to-delivery), freshness (the newest
        record's timestamp vs now), cashtag-queryability (does a $TICKER query return records ABOUT
        the security, per the item rule);
      - the COST CAP as a number the plan states and the script enforces (a trigger that would exceed
        it refuses), and the REFUSAL signal (what output means "this dataset cannot serve the feed");
      - the fourth-surface fact (F12: the datasets API is the same credential against a different API
        surface, NOT a fourth zone -- C-ZONE-IN-CALLER) stated so the script does not hunt for a zone.
      measure.py's entry point prints "REQUIRES Andrew's per-use word (G-24); not run by AMGT-s-13" and
      exits 3 unless invoked with an explicit --word-record <path@hash> argument naming the record that
      carries the word. This order never supplies one.

  (b) THE FEED CONTRACT  lib/research/social/schema.json -- social_items.json per security: {item_id,
      platform, account: {handle, official: MEASURED|INFERRED|UNRESOLVED}, posted_at, text, url,
      admitted: PASS|REFUSE|PROVISIONAL, rule_reason, source_line} where source_line is REQUIRED and its
      value for this account is the F13 disclosure, verbatim: "general-social plus finance-adjacent; the
      cashtag-native venue (StockTwits) carries 0 datasets on this account". A validator over it.

  (c) THE SOCIAL-ITEM RULE ON FIXTURES: import AMGT-s-11's item rule; build a fixture set of posts
      (some ABOUT a security, some merely containing its ticker string, one from an unresolved account)
      and show the rule's verdicts -- PROVISIONAL with reasons at this cut, since its threshold awaits
      the distribution the measurement will produce. Tests in lib/research/social/tests/.

  (d) SPEC_SECTION_social.md for AMGT-s-5, including the disclosure line's placement on the page.
```

## DEPENDENCIES

`AMGT-s-11` (the item rule) and `AMGT-s-12` (the account identity's shape and the universe). Slot ~6
spawns after both land.

## BOUNDS -- what this cell may not cross

```
⛔ G-24 / C-VENDOR-EGRESS: NO DATASET TRIGGER, NO datasets/list call, NO Bright Data request of any kind.
This order carries no word. measure.py refuses to run without a --word-record and this order gives none.
AC4 and AC5.
⛔ C-LISTING-NOT-CAPABILITY: nothing here claims social data is in hand. Every count in the plan is F12's,
CITED; the plan's job is to produce the first MEASURED numbers when the word comes.
⛔ C-ZONE-IN-CALLER: the datasets API is a fourth SURFACE on the one credential, not a fourth zone.
⛔ C-IDENTITY-RESOLVED: an item from an account whose official status is UNRESOLVED is not attached to a
security; the schema carries the status and the validator refuses an attachment without it.
⛔ C-RULE-MUST-EXIST: the feed is NOT displayed until the item rule has its distribution; the contract
carries admitted=PROVISIONAL and the page holds the class back.
⛔ C-DESIGN-SPEC-FIRST: no .tsx.
⚠ Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
F12 (CITED): api.brightdata.com/datasets/list returned HTTP 200 and 1,763 datasets on the live account,
    including the post-level ids above. Listed, reachable, unexercised.
F13 (CITED): StockTwits 0 datasets on this account, against 4 Reddit, 5 X/Twitter, 10 YouTube. The
    cashtag-native venue is absent; the disclosure is the feed's own source line.
F8/F9 (CITED): a cookieless unlocker cannot read authenticated content; the estate's authenticator
    pattern exists. Neither is this cell's; the datasets surface is a different API.
PART V (CITED): "A social ACCOUNT identity layer exists, distinct from the ticker layer ... an impostor
    or fan account must be distinguishable from the official one." AMGT-s-15's social map carries the
    test; this contract carries the status.
comp-schedule (RUN): 25 gates armed, none this project's; G-24 binds this cell absolutely.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/social/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-13.social-feed-measure-then-build.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~6/`. lib/research/rules, lib/research/identity
and the sibling deliverables are READ.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W6-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-13"><invocation>python -c "import io,re; t=io.open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~6/MEASUREMENT_PLAN.md',encoding='utf-8').read(); obs=['cost','schema','latency','freshness','cashtag']; print('dataset id named', bool(re.search(r'gd_[a-z0-9]{16,}', t)), '| observables', sum(1 for o in obs if re.search(o, t, re.I)), 'of 5', '| cost cap stated', bool(re.search(r'cost cap[^\n]*\d', t, re.I)), '| refusal signal stated', 'refus' in t.lower(), '| fourth surface not a zone', bool(re.search('fourth surface|not a (fourth )?zone', t, re.I)))"</invocation><expect>"dataset id named True | observables 5 of 5 | cost cap stated True | refusal signal stated True | fourth surface not a zone True" -- the plan names what it would trigger, every observable and how it is read, a numeric cost cap, the refusal signal, and the surface-not-zone fact; any False is a plan a later worker would have to finish and is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-13"><invocation>python -m lib.research.social.measure --dataset gd_lwxkxvnf1cynvib9co --company test; echo rc=$?</invocation><expect>the line "REQUIRES Andrew's per-use word (G-24); not run by AMGT-s-13" followed by "rc=3" -- the script exists, is invocable, and REFUSES to trigger without a word record; an rc of 0, any network activity, or a missing script is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-13"><invocation>python -m pytest lib/research/social/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "4 passed" with no "failed" -- (1) the validator REFUSES a social item without a source_line; (2) it ADMITS one carrying the F13 disclosure verbatim (the difference arm); (3) an item from an UNRESOLVED account is not attached to a security; (4) the item rule on the fixture set returns PROVISIONAL with a reason for a post that merely contains the ticker string and never PASS</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-13"><invocation>grep -r -c -i -E 'api\.brightdata\.com|requests\.(get|post)|urllib\.request|httpx' lib/research/social/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no HTTP client and no vendor host under the module at this cut; measure.py composes the request it WOULD send and refuses to send it (the client is added by the order that carries the word, and AC2 pins the refusal)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-13"><invocation>python -c "import json; s=json.load(open('lib/research/social/schema.json')); print('source_line required', 'source_line' in s['required'], '| official enum', s['properties']['account']['properties']['official']['enum'])"</invocation><expect>"source_line required True | official enum ['INFERRED', 'MEASURED', 'UNRESOLVED']" -- the disclosure is a REQUIRED field, not a footnote, and the account's official status is the closed vocabulary</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-13" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical, a census over the plan): the measurement is fully specified -- one command away.
- **AC2** (mechanical): the script exists and refuses without the word. The bound, exercised.
- **AC3** (mechanical): the contract's refusals and admissions, and the rule's honesty on fixtures.
- **AC4** (mechanical, NEGATIVE): no client, no host.
- **AC5** (mechanical): the disclosure is required by schema.
- **AC6** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): when Andrew's word arrives, could the NEXT worker run measure.py with the word record and get all five observables in one call -- or would it have to re-plan? And does the plan's stop rule prevent a second trigger if the first answers "cannot serve the feed"?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>2</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-2 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q6, `AMGT-s-13` alone; slot ~6 spawns after `AMGT-s-11` and `AMGT-s-12` land.
**Provenance:** the cell text is the decomposition's row verbatim. The "plan, not trigger" cut is G-24 applied to a cell whose first act IS a vendor call: the moratorium is Andrew's, the word is his, and this issuer SURFACES the ask in the drain-end read -- ONE dataset trigger, ONE company, a stated cost cap -- rather than writing a criterion no worker could satisfy. C-LISTING-NOT-CAPABILITY is honoured by counting nothing as measured until the trigger runs.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's; G-24 bound onto this cell absolutely
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; this cell touches no AWS resource
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; the Bright Data account is a credential, not a node this cell touches
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a plan, a schema, a refusing script and tests; no deployed resource changes and no vendor call.
