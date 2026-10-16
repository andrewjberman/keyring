# TO ADVI_COTBKF.TO-CB-cu-1.store-derived-yahoo-set-vs-served-labels -- round 99 CB-cu-1: re-derive the Yahoo-sourced point set from the price stores' own source field and compare it with the served use_class labels; read-only, counts only

<to_id>ADVI_COTBKF.TO-CB-cu-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~188</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>99</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cu-1` (`decompositions/ADVI_COTBKF_DECOMP.round99.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** The three served FWD-3 tables carry a `use_class` label that marks every priced row whose price came from Yahoo (`yahoo_finance` or `linear_interpolation`). Round 98's check proved the labels equal the Yahoo-sourced points of the regrade's own price file (`security_day_price.parquet`). The CVO's caveat: that joins against the build's own price file, so it does not show which points came from Yahoo in the price STORES themselves. You re-derive the Yahoo point set from the stores' own per-row `source` field, read fresh from S3, and compare it with the served labels. **This cell is read-only: it writes nothing to S3, serves nothing, changes no code and no committed file except your own record.**

**What to read (all READ-ONLY).**
1. `data/assets/scripts/silver/commonwealth_daily_valuation.py` in your worktree: `load_price_store(s3, spec, uhash, wanted, cache_dir, refresh)` (one store's priced rows from a cache or one S3 pass), `security_day_prices(universe, stores, claims)` (resolves each store's rows to (cusip, day) and carries the store's `source` label(s), '|'-joined), `universe_from_tx(tx)`, `YAHOO_SOURCES`, `is_yahoo_source`, `_s3_client()`; and its `main` (the loop that builds `stores` from `pc.STORES` and the transactions) for how the regrade assembled its inputs. `data/assets/scripts/analysis/commonwealth_price_census.py`: `STORES`, `read_store`, `symbol_claims`, `norm_key`.
2. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~187/SERVED_MOVE_RELABEL_RECORD.json` (the labels' counts at round 97) and `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cs1_ac2_label_check.py` (the round-98 join you are checking independently of).
3. The transactions the universe comes from: the received cache `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/cache` (the regrade's `--cache`; read with the same loader the regrade used, `dh.load_tx_pos(cache)` / `dr.load_tx(cache)`). Your worktree has no `.scratch`: pass every path explicitly. The private sweeps config is NOT needed for this cell; do not look for it.

**Your items.**

1. **Fresh store pass.** Build the universe from the transactions and read EVERY price store in `pc.STORES` from S3 (read-only) into a NEW cache directory `C:/Dev/ajb_workspace/.scratch/cotbkf_r99/store_cache` with `refresh=True` (never reuse `C:/Dev/ajb_workspace/.scratch/cotbkf_r97/price_cache` or any older cache: the point of the cell is a fresh read of the stores). Then `security_day_prices(universe, stores, claims)` gives, per (cusip, day), the store's own `source` label. Record each store's row count and whether it came from cache (expect `cache=False`). Do NOT apply the as-traded substitution: the labels the stores carry are the same before and after it.
2. **The store-derived Yahoo set.** From that frame take the (cusip, day) points whose `source` names `yahoo_finance` or `linear_interpolation` (a `|`-split part equal to one of them: `is_yahoo_source`). Call it S.
3. **The served set.** Read the SERVED `account_day_value` from `s3://opal-data-assets/commonwealth/cottonwood/silver/account_day_value/date=2026-06-23/part-00000.parquet` (one get; record its VersionId, which must equal `ObKZXku7Am.QGjO.oSAsIScy8IcJxN5a`; columns `cusip`, `date`, `close`, `price_source`, `use_class` only). X = the distinct (cusip, date) pairs of its priced, non-cash rows (`close` not null and `price_source` not `cash-at-par`). L = the distinct (cusip, date) pairs among X whose `use_class` is not `NOT_YAHOO`.
4. **The comparison.** A = X intersect S (served priced points that the stores say are Yahoo). B = L. Report `|X|`, `|S|`, `|A|`, `|B|`, `|A and B|`, `|A minus B|` and `|B minus A|`. Equal means `|A minus B| = 0` and `|B minus A| = 0`. If not equal, LIST the difference by category in counts only: for each category, how many (cusip, date) points and how many distinct securities (cusips) are in it, and the categories you find (for example: a store that changed since the served build; a point whose store label differs from the price file's; a '|'-joined label; a point labelled for a reason other than its store source). Never print a cusip, account or value; a count per category is the finding. Say whether the stores changed since the round-97 regrade read them (compare each store's row count with the round-97 `regrade.log` counts: silver canonical 2,138,920; gold holdings 594,318; etfs gold 209; bbg testpull 132,015). A difference graduates as a row (see the refusal clause); it is not repaired here.
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~188/STORE_DERIVED_YAHOO_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `stores` (`[{"id","rows","from_cache"}]`), `served` (`{"VersionId","rows_read"}`), `sets` (`{"X","S","A","B","A_and_B","A_minus_B","B_minus_A"}`), `equal`, `difference_categories` (`[{"category","points","securities","note"}]`, empty when equal), `stores_changed_since_r97`, `not_established`; and a short `.md` beside it. No account number, name, cusip or dollar value in either: counts only.

### ACCEPTANCE

<criterion id="CB99cu1-AC1" cell_refs="CB-cu-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~188/STORE_DERIVED_YAHOO_RECORD.json',encoding='utf-8'));m=d['measured'];s=d.get('sets') or {};print('STORE-DERIVED measured=%s' % m + ((' x=%d s=%d a=%d b=%d equal=%s' % (s['X'],s['S'],s['A'],s['B'],d['equal'])) if m else ' reason=%s' % d['reason']))"</invocation><expect>^STORE-DERIVED measured=(True x=\d+ s=\d+ a=\d+ b=\d+ equal=(True|False)|False reason=.+)$</expect></criterion>
`CB99cu1-AC1` -- the record states the store-derived and served set sizes and whether they are equal, or states plainly why nothing could be measured.

<criterion id="CB99cu1-AC2" cell_refs="CB-cu-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~188/STORE_DERIVED_YAHOO_RECORD.json',encoding='utf-8'));s=d.get('sets') or {};ok=(not d['measured']) or (s['A']==s['A_and_B']+s['A_minus_B'] and s['B']==s['A_and_B']+s['B_minus_A'] and d['equal']==(s['A_minus_B']==0 and s['B_minus_A']==0) and (d['equal'] or sum(c['points'] for c in d['difference_categories'])==s['A_minus_B']+s['B_minus_A']));print('STORE-DERIVED-SUMS consistent=%s' % ok)"</invocation><expect>^STORE-DERIVED-SUMS consistent=True$</expect></criterion>
`CB99cu1-AC2` -- the set arithmetic closes: A and B each split into the shared part and their own remainder, `equal` agrees with both remainders being zero, and when they differ the listed categories add up to the whole difference.

<criterion id="CB99cu1-AC3" cell_refs="CB-cu-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cu1_ac3_served_unchanged_check.py</invocation><expect>^SERVED-UNCHANGED versions_equal=3 of 3$</expect></criterion>
`CB99cu1-AC3` -- the cell wrote nothing: the three served keys still carry the VersionIds the round-98 apply left. The issuer's script reads object metadata only; read it, do not edit it.

<expected_criteria>CB99cu1-AC1,CB99cu1-AC2,CB99cu1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder and your own NEW channel row. You change no code, test or committed file. Scratch stays under `C:/Dev/ajb_workspace/.scratch/cotbkf_r99/` (gitignored, never committed); you may create that directory.
- **AWS: READ-ONLY** (`get` / `head` / `list` of the price stores the regrade already reads and of the served `account_day_value` key); no write, no `--apply`, no vendor call, no Bloomberg, no Yahoo call.
- **No account number, name, cusip or dollar value** in the record, the report or any message: counts only. The received run data is off git: do not list or describe it beyond counts.
- **NEVER** serve, apply, overwrite, push, override a gate or `--force`; never edit any module; never write into the received tree `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/` or into `cotbkf_r97/`.
- **Timing.** A fresh pass over the stores and a 21-million-row read outlast the worker bar's 120 s: run each in the background under `timeout 2400` and read its log when it ends (round 97's regrade took about 10 minutes).
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W188-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. A difference between the two sets is recorded as a row (`OBSERVATION`, `INERT`, one row per category, counts only) and reported, and still PASSES AC1 to AC3: the cell asks for the measurement.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round99.md</decomp_doc> (round 99), cell `CB-cu-1`.
<owned_cells>CB-cu-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB99cu1-AC1, CB99cu1-AC2, CB99cu1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~188/ADVI_COTBKF.TO-CB-cu-1.store-derived-yahoo-set-vs-served-labels.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB99cu1-AC1,CB99cu1-AC2,CB99cu1-AC3` BEFORE the flip. The `output_evidence` of each criterion must equal its `expect` pattern exactly (no suffix); put any note in `denominator`. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when all three PASS** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the `STORE-DERIVED` line. Then: each store's row count and cache state; the served VersionId; the set sizes and the comparison; every difference category in counts; whether the stores changed since round 97; any step you could not run and why; the three criterion lines; commits; every gate refusal and hook denial, verbatim. No account number, cusip or value in the report.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a fresh read of the price stores and a count; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE read-only gets and lists under the roles the regrade already uses on objects it already reads; no new permission.
comp-adversary: RUN -- the check is independent of the round-98 join (the stores' own source field, read fresh, against the served labels); BLIND: the as-traded substitution is not applied (the stores' labels equal the substituted points' labels by the rule in `as_traded_store`), a store changed since round 97 would show as a difference and is named as one, and the served rows are read at their current VersionId.
lane: the <paths> block IS the grant (worker RULING 1). A read and a count: nothing outside the deliverables folder and one channel row is written to the repo.
</preflight>

**ISSUER NOTES:** Source: `1.0.0_SA_CTO~DELL1` msg 6578 (ROUND_ANALYSIS.round96-98, item 2) on the CVO's caveat in `ADJUDICATION_v64`. Item 1 (W181-S1) is met at the trunk (round 92's `CB-cn-1`); see the decomposition. Mechanical checks dry-run at the base (the record file is absent): AC1 and AC2 FAIL there as expected; AC3 PASSES (served versions unchanged).
