# TO ADVI_COTBKF.TO-CB-cm-1.as-traded-yahoo-reaches-the-label -- round 91 CB-cm-1: prove on the REAL code path that a holding priced on an as-traded Yahoo close reads its security's use class in the served label; fix the path only if the proof fails; list every line that reads a Yahoo price into an account value

<to_id>ADVI_COTBKF.TO-CB-cm-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~181</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>91</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cm-1` (`decompositions/ADVI_COTBKF_DECOMP.round91.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew, 2026-10-15, call `3adb` option (a): "yeah sure." Served Yahoo-priced days for securities held in the active Cottonwood set (V2) STAY, labelled; each security's points are replaced the day its Bloomberg series lands; nothing new is drawn from Yahoo for active names. The label is `use_class` (value `NOT_FOR_ACTIVE` for a V2-held security, `INACTIVE_USE` for any other, `NOT_YAHOO` for a row not priced on Yahoo), built in the served-returns builder `data/assets/scripts/silver/commonwealth_fwd3_serve.py` (functions `yahoo_priced`, `use_labels`, `nfa_yahoo_cusips`, round 89, merged @7608f2c550). One reader was never covered by a test: `data/assets/scripts/silver/commonwealth_daily_valuation.py` `apply_price_basis` (L303) replaces the store's `yahoo_finance` points with Yahoo Close points read from a cache keyed by TICKER (`read_yahoo_close` L241, `as_traded_store` L258). By reading, a replaced row keeps `source = "yahoo_finance"` and a re-derived row keeps `source = "linear_interpolation"` (both in `YAHOO_SOURCES`), and the resolved holding frame carries `source` (`_source_labels`, L400), so the served label should already cover them. **You do not assume that: you prove it by running the real functions on stub data, and you fix the path only if the proof fails.** The armed rows `ADVI_COTBKF-D1-W173-S3` and `D1-S2` are answered by your result.

**Read first (under the repository root):** `data/assets/scripts/silver/commonwealth_daily_valuation.py` (the header comment block on the as-traded basis, `YAHOO_SOURCES`, `is_yahoo_source`, `apply_price_basis`, `as_traded_store`, `read_yahoo_close`, the price-resolution function that takes `[(store_id, DataFrame)]` and returns `(cusip, day, price, store, source)` at about L409, `value_days` L448, and how `run` at about L1005 chains them); `data/assets/scripts/silver/commonwealth_fwd3_serve.py` (`yahoo_priced`, `use_labels`, `nfa_yahoo_cusips`, the class function that decides `NOT_FOR_ACTIVE` vs `INACTIVE_USE` and its fail-closed rule, `value_table`, `daily_table`, `build`); the round-89 tests `data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve_use_class.py` and `test_commonwealth_fwd3_serve.py` (their stub style; you add, you edit none); the round-87 trace `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~173/READERS_RECORD.json` (the four readers and row `D1-W173-S3`'s text); `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~178/USE_CLASS_SERVE_RECORD.json`.

**Your items.**

1. **Five tests**, added to a NEW file `data/assets/scripts/silver/tests/test_commonwealth_as_traded_use_class.py` (stub frames and a stub Yahoo cache directory under `tmp_path` holding small CSVs with `date,Close` columns; made-up CUSIPs `T00000001`... and made-up tickers; no real data, no network, no S3). Each test runs the REAL `apply_price_basis` and the REAL price-resolution and holding-frame functions the build uses, and the REAL served label functions; names, all starting `test_as_traded_`:
   - `test_as_traded_replaced_yahoo_point_reads_not_for_active_for_a_v2_held_security`;
   - `test_as_traded_rederived_linear_interpolation_point_reads_not_for_active_for_a_v2_held_security`;
   - `test_as_traded_replaced_yahoo_point_reads_inactive_use_for_a_security_outside_v2`;
   - `test_as_traded_store_point_that_is_not_yahoo_reads_not_yahoo_for_any_security` (a `transaction_observed` or other non-Yahoo source label on the same stub security);
   - `test_as_traded_unreadable_class_fails_closed_to_not_for_active` (the active set unreadable, or its hash wrong: every Yahoo-priced row reads `NOT_FOR_ACTIVE`).
   The V2 set for the stubs is injected the way the round-89 tests inject it; never read the real V2 file in a test that needs a made-up CUSIP.
2. **If all five pass at the base**, change NO production code: the served label already covers the as-traded reader, and the record says so. **If any fails**, fix the production path with the smallest change that makes it pass without moving a value in the other direction (the label is a column; no price may change), add the fix in `commonwealth_daily_valuation.py` or `commonwealth_fwd3_serve.py` only, and state in the record exactly what was missing. Either way the existing tests of both modules must pass unchanged.
3. **The reader list.** In the record, list EVERY line (file:line) in `commonwealth_daily_valuation.py`, `commonwealth_fwd3_serve.py` and `commonwealth_sweep_regrade.py` that reads a Yahoo-sourced price or the Yahoo Close cache into an account's holding value or return, and for each: `labelled_in_served_tables` true or false (true only when the row it produces carries a Yahoo source label that `yahoo_priced` recognises), the test that proves it (by name) or `UNTESTED`, and whether it is a PRICE or a corporate-action FACT (split ratios are facts and stay outside the guard by the CTO's ruling, msg 6175). Use `comp-find` or the native Grep tool for the search (a recursive shell grep is denied by a hook); state the denominator (files searched).
4. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~181/AS_TRADED_LABEL_RECORD.json` with exactly these top-level keys: `base_result` (`{"tests_passing_at_base", "tests_total"}`: how many of the five passed BEFORE any production change), `production_change` (`"none"` or a one-line description), `readers` (a list of `{"file", "line", "kind" (PRICE or FACT), "labelled_in_served_tables", "test"}`), `unlabelled_price_readers` (the count of `readers` with kind PRICE and `labelled_in_served_tables` false), `module_blobs` (`{"commonwealth_daily_valuation.py", "commonwealth_fwd3_serve.py"}` from `git rev-parse HEAD:<path>` after your last commit), `files_searched`, `not_established`; and a short `.md`. No account number, name or value in either.

### ACCEPTANCE

<criterion id="CB91cm1-AC1" cell_refs="CB-cm-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_commonwealth_as_traded_use_class.py -q -k as_traded</invocation><expect>5 passed</expect></criterion>
`CB91cm1-AC1` -- the five tests of the as-traded path pass.

<criterion id="CB91cm1-AC2" cell_refs="CB-cm-1"><invocation>python -c "import subprocess,sys,glob;fs=sorted(glob.glob('data/assets/scripts/silver/tests/test_commonwealth*fwd3*.py'))+sorted(glob.glob('data/assets/scripts/silver/tests/test_commonwealth*valuation*.py'));r=subprocess.run([sys.executable,'-m','pytest']+fs+['-q'],capture_output=True,text=True);print('VALUATION-AND-FWD3-TESTS files=%d rc=%d last=%s'%(len(fs),r.returncode,r.stdout.strip().splitlines()[-1]))"</invocation><expect>rc=0</expect></criterion>
`CB91cm1-AC2` -- every existing valuation and fwd3 test file still passes (the control that nothing moved).

<criterion id="CB91cm1-AC3" cell_refs="CB-cm-1"><invocation>python -c "import json,subprocess;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~181/AS_TRADED_LABEL_RECORD.json',encoding='utf-8'));ok=all(subprocess.check_output(['git','rev-parse','HEAD:data/assets/scripts/silver/'+k]).decode().strip()==v for k,v in d['module_blobs'].items());u=sum(1 for r in d['readers'] if r['kind']=='PRICE' and not r['labelled_in_served_tables']);print('AS-TRADED-LABEL blobs_equal=%s readers=%d unlabelled_price_readers=%d count_matches=%s base=%d/%d change=%s'%(ok,len(d['readers']),d['unlabelled_price_readers'],u==d['unlabelled_price_readers'],d['base_result']['tests_passing_at_base'],d['base_result']['tests_total'],d['production_change'][:40]))"</invocation><expect>blobs_equal=True</expect></criterion>
`CB91cm1-AC3` -- the record's module blobs equal what is committed, and its reader count is consistent with its own list.

<expected_criteria>CB91cm1-AC1,CB91cm1-AC2,CB91cm1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. You add one test file and the record; you edit `commonwealth_daily_valuation.py` or `commonwealth_fwd3_serve.py` ONLY if a test fails at the base (item 2), and then only to carry the label, never to change a price. You edit no existing test, no other module and no committed data.
- **NO S3, no AWS, no network, no Yahoo call, no real cache.** Stubs and `tmp_path` only. Do not run the build against any real data directory.
- **No account number, name or dollar value** in any file, fixture, log or report; counts, line numbers and test names only.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; if it fails closed because the pinned set is absent on this box, report the exact error and do NOT look for the set.
- **NEVER** serve, `--apply`, push, override a gate or `--force`; do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed. If a gate refuses a function name or a dtype call, rename or adapt without behaviour change; never override.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W181-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only.

<paths>
data/assets/scripts/silver/tests/test_commonwealth_as_traded_use_class.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_fwd3_serve.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round91.md</decomp_doc> (round 91), cell `CB-cm-1`.
<owned_cells>CB-cm-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB91cm1-AC1, CB91cm1-AC2, CB91cm1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~181/ADVI_COTBKF.TO-CB-cm-1.as-traded-yahoo-reaches-the-label.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB91cm1-AC1,CB91cm1-AC2,CB91cm1-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the three criterion lines and `base_result` (how many of the five tests passed before any production change; this is the answer to the armed row). Then: whether production code changed and why; the reader list's counts (PRICE and FACT readers, labelled and not); the denominator of the search; the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a test addition (and a conditional label fix) proven on stubs; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call at all.
comp-adversary: RUN -- the criterion is the real code path on stubs, not a mock of the label: a test that stubs `source` by hand would pass for the wrong reason, so each test must start from a store frame and a cache and run `apply_price_basis` to produce the source labels; BLIND: the real price store and cache may carry source labels the stubs do not (a joined `a|b` label is handled by `is_yahoo_source`; a label outside `YAHOO_SOURCES` that is nonetheless Yahoo-derived would read NOT_YAHOO), and a reader outside the three named modules (the round-87 trace found 49 readers by token; this cell lists those in the three files that value accounts) is not covered.
lane: the <paths> block IS the grant (worker RULING 1). Production edits are conditional on a failing base test; the label is a column, no price changes.
</preflight>

**ISSUER NOTES:** Source: CTO msgs 6237/6238 (the L329 guard in the next round, before the CRM window) and Andrew's call `3adb` (a). The armed rows `D1-W173-S3` and `D1-S2` are disarmed by this seat when this order's criteria PASS and the answer in the record reads that no PRICE reader of the three modules is unlabelled.
