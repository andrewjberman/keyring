# TO ADVI_COTBKF.TO-CB-cn-1.sechist-reader-maps-vendor-source -- round 92 CB-cn-1: read_sechist maps each point's vendor `source` to the label the use_class guard reads, and fails closed to yahoo_finance on a missing or unknown value

<to_id>ADVI_COTBKF.TO-CB-cn-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~182</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>92</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cn-1` (`decompositions/ADVI_COTBKF_DECOMP.round92.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew, 2026-10-15: "Active accounts should get BBG pricing exclusively" and (call 3adb (a)) any served Yahoo day for a V2-held security stays, LABELLED. The label is read by the served-returns builder from each priced row's `source`: a row priced on `yahoo_finance` or `linear_interpolation` (`YAHOO_SOURCES`, `commonwealth_daily_valuation.py` L67) reads its security's `use_class`; any other source reads `NOT_YAHOO`. The reader `read_sechist` (`commonwealth_daily_valuation.py`, about L164 to L195) reads an operator-named price series (MDPF_SECHIST's `security_series`) and today labels EVERY row it reads with the constant `SECHIST_STORE = "sechist"`, whatever the series' origin, so a Yahoo-origin point would read `NOT_YAHOO` and escape the guard (armed row `ADVI_COTBKF-D1-W181-S1`). The series store holds 0 objects today, so nothing escapes yet. The writer's owner (`2.0.0_SA_COO~H1`, msg 6266) will carry a `source` column on every priced point with exactly two values, `bloomberg` and `yahoo_finance`, and refuse any other at the writer (staged, not landed). **You build the READER half now, against that contract, so the hazard cannot open the day the first object lands.**

**Read first (under the repository root):** `data/assets/scripts/silver/commonwealth_daily_valuation.py` (`SECHIST_STORE`, `_SECHIST_DATE`, `_SECHIST_PRICE`, `_SECHIST_KEYS`, `SechistError`, `read_sechist`, `_clean_priced`, `YAHOO_SOURCES`, `is_yahoo_source`, `_source_labels`, and how the price-resolution function carries `source` to the served frame); `data/assets/scripts/silver/commonwealth_fwd3_serve.py` (`yahoo_priced`, `use_labels`); `data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py` (the existing `read_sechist` tests, e.g. `test_sechist_raises_when_the_prefix_holds_nothing_readable`, and their stub S3 style; you add, you edit none); the writer staged by H1: `org/tier1_exec/2.0.0_SA_COO~H1/r7_staged/SH_VENDOR_COLUMN_REQUIRED_CELL_STAGED.md` is on another seat's tree and may not be present in your worktree: the contract you build against is exactly the three sentences above; and the writer module `data/mdpf/scripts/silver/security_series_writer.py` (read only: the shape of the parquet it will land); the armed row's text in `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md` (`ADVI_COTBKF-D1-W181-S1`, `D1-S7`).

**Your items.**

1. **The mapping.** In `read_sechist`, when an object's schema has a column named `source`, read it with the date, price and key columns and give each point the label `yahoo_finance` when its `source` is exactly `yahoo_finance`; `sechist` (the existing `SECHIST_STORE`) when it is exactly `bloomberg`; and `yahoo_finance` (FAIL CLOSED) when it is missing/null/NaN, an empty string, or ANY other string (a case variant, `yahoo`, `sechist`, `linear_interpolation`, a joined `a|b`). Match exactly; do not strip or lower-case. Count the points that failed closed and expose the count (a module-level `LAST_SECHIST_READ` dict with `points`, `bloomberg`, `yahoo_finance`, `failed_closed`, written the way `LAST_SPLIT_PIN` is, cleared at the start of each call).
2. **No `source` column at all.** An object whose schema has NO `source` column keeps today's behaviour for its rows (label `SECHIST_STORE`) ONLY IF an existing test pins that; check `test_commonwealth_daily_valuation.py`. If an existing test pins it, keep that behaviour, count those points under `no_source_column` in `LAST_SECHIST_READ`, and say so in the record as a named gap; if NO existing test pins it, FAIL CLOSED here too (label `yahoo_finance`). State which case held and why.
3. **No price moves.** Only the `source` label of a point changes. The price, the day, the key columns and the point count are identical to the pre-change read on every input, including a source-less object (control test).
4. **Tests**, a NEW file `data/assets/scripts/silver/tests/test_commonwealth_sechist_source.py` (stub S3 listing and stub parquet bytes built with pyarrow in memory, the way the existing sechist tests do; made-up CUSIPs; no network), eight tests, all names starting `test_sechist_source_`: `..._yahoo_finance_point_keeps_the_yahoo_label`; `..._bloomberg_point_reads_sechist`; `..._null_source_fails_closed_to_yahoo_finance`; `..._unknown_string_and_case_variant_fail_closed_to_yahoo_finance`; `..._mixed_series_carries_both_labels_per_point`; `..._no_price_moves_against_the_pre_change_read` (a control that compares the price/day/key columns to a pre-change stand-in computed in the test); `..._failed_closed_count_is_exposed`; `..._a_yahoo_point_reads_not_for_active_in_the_served_label_for_a_v2_held_security` (runs the REAL price-resolution function and the REAL `use_labels` with an injected class function, as round 91's `test_commonwealth_as_traded_use_class.py` does: read it for the pattern).
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~182/SECHIST_READER_RECORD.json` with exactly these top-level keys: `module_path`, `module_blob` (`git rev-parse HEAD:<module_path>` after your last commit), `contract` (`{"column": "source", "values": ["bloomberg", "yahoo_finance"], "fail_closed_to": "yahoo_finance"}`), `no_source_column_case` (`"kept_sechist_pinned_by_existing_test"` or `"failed_closed"`, with the test name or the reason), `new_tests` (the eight names), `existing_tests_unchanged` (true only if `git diff` of every existing test file shows added lines only; the new test file is new), `price_moves` (0), `writer_half_landed` (false, read from the repository: whether `data/mdpf/scripts/silver/security_series_writer.py` at HEAD refuses a source outside the two values), `not_established`; and a short `.md`. No account number, name or value in either.

### ACCEPTANCE

<criterion id="CB92cn1-AC1" cell_refs="CB-cn-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_commonwealth_sechist_source.py -q -k sechist_source</invocation><expect>8 passed</expect></criterion>
`CB92cn1-AC1` -- the eight source-mapping tests pass.

<criterion id="CB92cn1-AC2" cell_refs="CB-cn-1"><invocation>python -c "import subprocess,sys,glob;fs=sorted(glob.glob('data/assets/scripts/silver/tests/test_commonwealth*valuation*.py'))+sorted(glob.glob('data/assets/scripts/silver/tests/test_commonwealth*fwd3*.py'));r=subprocess.run([sys.executable,'-m','pytest']+fs+['-q'],capture_output=True,text=True);print('SECHIST-CONTROL files=%d rc=%d last=%s'%(len(fs),r.returncode,r.stdout.strip().splitlines()[-1]))"</invocation><expect>rc=0</expect></criterion>
`CB92cn1-AC2` -- every existing valuation and fwd3 test file still passes unchanged (the control that no price and no other label moved).

<criterion id="CB92cn1-AC3" cell_refs="CB-cn-1"><invocation>python -c "import json,subprocess;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~182/SECHIST_READER_RECORD.json',encoding='utf-8'));b=subprocess.check_output(['git','rev-parse','HEAD:'+d['module_path']]).decode().strip();print('SECHIST-READER blob_equal=%s tests_unchanged=%s price_moves=%s fail_closed_to=%s no_source_column=%s'%(b==d['module_blob'],d['existing_tests_unchanged'],d['price_moves'],d['contract']['fail_closed_to'],d['no_source_column_case']))"</invocation><expect>blob_equal=True tests_unchanged=True price_moves=0 fail_closed_to=yahoo_finance</expect></criterion>
`CB92cn1-AC3` -- the record names the module at HEAD and its blob equals what is committed; no existing test was edited; no price moved; the fail-closed label is `yahoo_finance`.

<expected_criteria>CB92cn1-AC1,CB92cn1-AC2,CB92cn1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. You edit `commonwealth_daily_valuation.py` (the sechist reader and its constants only) and add one new test file; you edit no existing test, no other module, and NOT `data/mdpf/scripts/silver/security_series_writer.py` (it is `2.0.0_SA_COO~H1`'s write surface: read it, never edit it).
- **NO S3, no AWS, no network.** Stubs and in-memory parquet only. Do not read the real `security_series` prefix.
- **No account number, name or dollar value** in any file, fixture, log or report.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; if it fails closed because the pinned set is absent on this box, report the exact error and do NOT look for the set.
- **NEVER** serve, `--apply`, push, override a gate or `--force`; do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed. If a gate refuses a function name or a dtype call, rename or adapt without behaviour change; never override.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W182-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only.

<paths>
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_sechist_source.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round92.md</decomp_doc> (round 92), cell `CB-cn-1`.
<owned_cells>CB-cn-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB92cn1-AC1, CB92cn1-AC2, CB92cn1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~182/ADVI_COTBKF.TO-CB-cn-1.sechist-reader-maps-vendor-source.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB92cn1-AC1,CB92cn1-AC2,CB92cn1-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the three criterion lines. Then: which no-source-column case held and why; whether the writer half had landed at HEAD; the diff size of the module and of each test file touched (removed lines must be 0 in every existing test file); the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a reader change proven on stubs; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call at all.
comp-adversary: RUN -- the label is built from a column the writer does not yet emit, so a mismatch of contract would show as every point failing closed (a visible count, never a silent pass); a case-variant or `yahoo` value is refused by exact match; BLIND: the real writer may emit `source` as a dictionary-encoded or large-string column (the stubs use plain strings), and the `source` column of an object read by the existing reader without it keeps today's label under the named-gap rule (the store is empty, so no point reads that way yet).
lane: the <paths> block IS the grant (worker RULING 1). The writer module is another seat's surface and is read only.
</preflight>

**ISSUER NOTES:** Source: CTO msgs 6255 and 6256; `2.0.0_SA_COO~H1` msg 6266. Row `D1-W181-S1` stays ARMED until BOTH halves have landed (this reader half and H1's writer half) and the first object is read through them; the disarm is this seat's with H1's concurrence.
