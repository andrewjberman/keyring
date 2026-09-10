# AMGT_RESAPP.TO-AMGT-s-15 -- THE LIST REGISTER: the publisher allowlist and the social-account map, each with an OWNER field and a rot signal a person reads -- the owner surfaced as UNASSIGNED rather than invented

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-15</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~5</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-14; manifest row S15)

```
AMGT-s-15. THE LIST REGISTER -- the publisher allowlist and the company-to-social-account map, each
with a NAMED OWNER and a rot signal a person reads. Not an alarm.

FWD-14's bar, verbatim: "The lists the page depends on do not rot in silence. DONE WHEN EXERCISED -- a
list has actually gone out of date and somebody was told by the system rather than by a wrong page.
ACCEPT: The list of publishers the page will quote, and the map of companies to their official social
accounts, each have a named person responsible; and when one goes out of date somebody is told."

C-LIST-OWNER (PRD s.3): living lists rot; an enumerated list with no owner lapses silently -- the same
failure that left two vendor keys dead. G-20 (the alerting moratorium) binds: "somebody is told" is a
SIGNAL a person reads in the coverage-freshness view (AMGT-s-7), never an alarm, an SNS topic or a
scheduled checker.

WHAT TO PRODUCE, under lib/research/lists/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/:

  (a) publishers.json -- {owner, owner_status: NAMED|UNASSIGNED, reviewed_at, review_interval_days,
      entries: [{domain, name, status: PROPOSED|ADMITTED|RETIRED, added_at, added_by, reason}]}
      ⛔ THE OWNER IS A PERSON AND THIS WORKER CANNOT NAME ONE. Set owner_status UNASSIGNED and owner
      "UNASSIGNED -- Andrew names the owner (C-NO-CONTACT: not Adam's team directly)". Seed the entries
      as PROPOSED, never ADMITTED: a starter set of financial publishers you state a rule for (e.g. the
      publishers the brief's IR-scan sample and the SA route already touch), each with its reason. The
      source rule (AMGT-s-11) holds the class back until an owner ADMITS entries; nothing here admits.

  (b) social_accounts.json -- {owner, owner_status, reviewed_at, entries: [{security_key, platform:
      x|linkedin|youtube, handle, status: MEASURED|INFERRED|UNRESOLVED, evidence}]} -- one entry per
      platform per name in AMGT-s-12's universe.json, every handle UNRESOLVED at this cut with evidence
      "no vendor word for social lookup (G-24)" -- the map's SHAPE, its owner field and its rot signal
      exist; its content awaits a word. An official-vs-impostor test is stated in the schema (PART V:
      "an impostor or fan account must be distinguishable from the official one") as the rule a later
      resolution must satisfy.

  (c) THE ROT SIGNAL  lib/research/lists/rot.py -- a script a person runs: for each list, entries
      older than review_interval_days since reviewed_at are STALE; for publishers, a domain that no
      longer resolves in DNS (socket.getaddrinfo -- a name lookup, not an HTTP fetch) is UNRESOLVABLE.
      Prints ONE line per list: "ROT publishers: N of M entries stale (>D days); K unresolvable; owner
      UNASSIGNED" and the same for social_accounts. Writes rot_signal.json beside the lists, which
      AMGT-s-7's freshness view RENDERS -- that rendering is how "somebody is told", under G-20.

  (d) SPEC_SECTION_lists.md for AMGT-s-5: where the rot signal appears on the page.
```

## DEPENDENCIES

`AMGT-s-12` (the universe the social map is keyed by). Slot ~5 spawns after AMGT-s-12 lands -- and this
is the DEFERRED chain under the fan-out cap: it takes the first freed slot, because nothing depends on it.

## BOUNDS -- what this cell may not cross

```
⛔ G-20: NO alarm, NO SNS, NO SES, NO EventBridge rule, NO scheduled run. rot.py is invoked by a person or
by the freshness view's generator. AC5.
⛔ G-24 / C-VENDOR-EGRESS: NO HTTP fetch, NO social lookup, NO vendor API. DNS name resolution of a
publisher domain is the one network act allowed and it is a lookup, not a fetch; AC4 refuses an HTTP
client in the module.
⛔ C-NO-CONTACT: the owner is not asked for; it is surfaced as UNASSIGNED for Andrew.
⛔ C-LIST-OWNER: no list without an owner FIELD; no entry without a status and a reason.
⛔ NOTHING IS ADMITTED BY THIS ORDER. PROPOSED is the ceiling for a publisher entry; UNRESOLVED for a
social handle.
⛔ C-DESIGN-SPEC-FIRST: no .tsx.
⚠ Bound every invocation under `timeout 120`; DNS lookups over a short list fit; cap the list.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
PART V (CITED, the brief): "Someone owns the source allowlist and the social account map as living
    lists. Both rot -- IR domains move, handles are renamed -- and an enumerated list with no owner
    lapses silently. This is the same failure that left two Bright Data keys dead."
F12/F13 (CITED): the social substrate is a Bright Data datasets surface -- LISTED, never exercised; the
    cashtag-native venue is absent. The social map's content waits on AMGT-s-13's measurement and a word.
AMGT-s-12's universe.json (landed): the keys the social map is built over, with the denominator printed.
comp-schedule (RUN): 25 gates armed, none this project's; G-20 and G-24 bind this cell.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/lists/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-15.list-register-owned-lists-with-a-rot-signal.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~5/`. AMGT-s-12's universe.json is READ.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W5-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-15"><invocation>python -c "import json; d='org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/'; p=json.load(open(d+'publishers.json')); s=json.load(open(d+'social_accounts.json')); print('publishers: owner_status', p['owner_status'], 'entries', len(p['entries']), 'admitted', sum(1 for e in p['entries'] if e['status']=='ADMITTED'), 'with reason', sum(1 for e in p['entries'] if e.get('reason'))); print('social: owner_status', s['owner_status'], 'entries', len(s['entries']), 'measured', sum(1 for e in s['entries'] if e['status']=='MEASURED'))"</invocation><expect>both lines with owner_status "UNASSIGNED", publishers "admitted 0" with "with reason" EQUAL to "entries", and social "measured 0" with entries greater than 0 -- the lists exist with their owner field surfaced as unassigned, nothing admitted or measured by this order, every proposed entry carrying its reason</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-15"><invocation>python -m lib.research.lists.rot org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/</invocation><expect>two lines of the exact shape "ROT publishers: N of M entries stale (>D days); K unresolvable; owner UNASSIGNED" and "ROT social_accounts: N of M entries stale (>D days); owner UNASSIGNED", with M equal to each list's entry count -- the rot signal runs on demand and prints its denominator; and rot_signal.json is written beside the lists</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-15"><invocation>python -m pytest lib/research/lists/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "2 passed" with no "failed" -- (1) an entry whose reviewed_at is older than the interval is reported STALE; (2) the same entry with a fresh reviewed_at is NOT (the difference arm)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-15"><invocation>grep -r -c -i -E 'requests\.|urllib\.request|httpx|brightdata|api\.|twitter\.com|x\.com|linkedin\.com|youtube\.com/@' lib/research/lists/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no HTTP client and no platform URL under the module; DNS resolution is the only network act and it is a lookup</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-15"><invocation>grep -r -c -i -E 'aws_cloudwatch|aws_scheduler|schedule_expression|cron\(|rate\(|sns|ses\b|EventBridge|smtplib' lib/research/lists/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: nothing under the module schedules, alarms or sends; "somebody is told" is the freshness view rendering rot_signal.json (G-20)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-15" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): both lists exist, owner surfaced as unassigned, nothing admitted or measured, every entry with its reason.
- **AC2** (mechanical, a census): the rot signal runs and prints its denominators.
- **AC3** (mechanical): stale is detected and not-stale is admitted -- the difference arm.
- **AC4**, **AC5** (mechanical, NEGATIVE): no fetch; no alarm.
- **AC6** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): is the official-vs-impostor test stated in social_accounts.json's schema one that would actually separate a fan account from the company's own, and is the publisher seed's stated rule one an owner could apply without re-deriving it?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-2 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q5, `AMGT-s-15` alone; the DEFERRED chain under the cap of eight -- slot ~5 takes the first freed slot after `AMGT-s-12` lands (decomposition s.5: a build with no dependants).
**Provenance:** the cell text is the decomposition's row verbatim. The UNASSIGNED owner is this issuer's application of C-NO-CONTACT and of the plain fact that a worker cannot name a person: the field exists, the signal exists, and the name is Andrew's -- SURFACED in the drain-end read.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's; G-20 and G-24 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; this cell touches no AWS resource
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; nothing this cell writes is in AWS
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: two JSON lists, a script and tests; no deployed resource changes.
