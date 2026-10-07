# AMGT_RESAPP task order -- `AMGT-ba-1` -- FWD-7, THE STALE RULE: THE FLAG KEYS ONLY ON INPUTS COLLECTED FOR THE NAME, AND THE DATE IS THE OLDEST COLLECTED INPUT (CTO RULINGS 1-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~267</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a pure rule module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read path; the check reads the /freshness view the function already serves.
comp-adversary: RUN by the issuer at the cut -- on deployed OVpDhfwD, 95 of 95 covered names are flagged stale, because Seeking Alpha reads NEVER on 92 and Web search on 95. The page, not the function, computes the flag today (`portal/src/pages/Freshness/freshnessRows.ts`), and it counts a never-read input as stale.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r77-267` (branch `wk-AMGT_RESAPP-267`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-267`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-1` (round 77, decomposition s.85)

CTO round-76 analysis @c8bbeeac10, rulings 1 and 2. Today every covered name reads stale, so the page singles out nothing.
The rule is rewritten ONCE, on the server, as a new module `lib/research/freshness/stale_rule.py`. The page (cell ba-4) will
render what this module returns; the adapter cell (ba-11) wires it into the route. You do NOT edit `scoped_amgt.py`.

**The rule.**
1. An input is one of the four the view carries per name: `bloomberg`, `seekingalpha`, `serp` (under `per_input`) and `pack`.
   Its stamp is a compact UTC stamp (`20261006T132108Z`), an ISO day, the word `NEVER`, or null.
2. An input with no readable day was **never collected for that name**. Its state is `not_collected`. It is NEVER stale and
   never appears in `stale_inputs`.
3. A collected input is `stale` when its day is MORE than 7 trading days before today (`lib/trading_calendar.py`; 7 is current,
   8 is stale), else `fresh`.
4. A row is stale when at least one COLLECTED input is stale.
5. `keyed_date` is the day (YYYY-MM-DD) of the OLDEST collected input: the date the flag keys on. So the flag and the date
   cannot disagree on a row. It is null when nothing was collected.
6. A row with nothing collected is not stale and carries a plain `stale_reason` ("Nothing has been collected for this
   company yet." or similar). A stale row's `stale_reason` names each stale input and its day in plain words.

**Exports** (the names are the contract; ba-11 and ba-2 call them):
- `STALE_AFTER_TRADING_DAYS = 7`
- `annotate_row(row, today) -> dict`: returns a COPY of the row with `stale` (bool), `stale_inputs` (list of input names),
  `keyed_date`, `stale_reason`, and `inputs`: `{<input>: {"state": "fresh"|"stale"|"not_collected", "day": <YYYY-MM-DD or
  null>, "age_trading_days": <int or null>}}` for all four inputs. The source row is not changed in place. `today` is a
  `datetime.date`.
- `annotate_view(view, today=None) -> dict`: a copy of the view with every row annotated and a `stale_rule` entry:
  `{"stale_after_trading_days": 7, "covered": n, "covered_stale": n, "covered_not_stale": n, "words": "<the rule in one
  plain sentence>"}`. `today` defaults to the current UTC date.

**Plant tests** in `lib/research/freshness/tests/test_stale_rule.py`: the six plants the check's AC1 uses, plus the
view-level counts.

In your report, name the hookup ba-11 adds (one line: where `annotate_row` is applied to the page view). Do not add it.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W267-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. The default /freshness body does not change: no row gains or loses a key (AC3). The stored snapshot is not rewritten.
3. Any words you serve are plain. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/freshness/stale_rule.py
lib/research/freshness/tests/test_stale_rule.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~267/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba1.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>six plants: never-collected inputs read not_collected and flag nothing, the oldest collected input is the keyed date, 7 trading days is current and 8 is stale; C1-C6 PASS; R77 BA1 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba1.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>over the covered rows of the served view: 0 never-collected inputs flagged, 0 flag/date disagreements, the stale and not-stale counts printed; C1-C3 PASS; R77 BA1 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba1.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the default /freshness rows keep exactly their ten keys; C1 PASS; R77 BA1 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~267 <0.9.0_WK_AMGT_RESAPP~267@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~267/AMGT_RESAPP.TO-AMGT-ba-1.stale-flag-keys-on-collected-inputs.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the covered stale and not-stale counts on the served view, and which names read stale;
- the hookup line for ba-11;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-76 analysis @c8bbeeac10 rulings 1-2, enrichment item 1 (data half). Wave 0, chain A. Checks dry-run at the base: AC1 FAIL as expected, AC2 FAIL as expected, AC3 PASS as expected. Measured at the cut on OVpDhfwD: covered 95; bloomberg dated 95; seekingalpha dated 3 (2026-09-11), NEVER 92; serp NEVER 95; pack dated 95. Under the ruled rule the 3 Seeking Alpha names read stale and 92 read not stale. The rule is annotated at SERVE time (today's date), so the stored snapshot stays the unannotated view and r75 c59's row equality is untouched.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~267</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @4ff402dfc0; proof VALID (worktree checker); the stale rule as one server module; AC1 6 of 6 plants, AC2 95 covered rows 3 stale 92 not stale, AC3 default body 302 of 302</status>
