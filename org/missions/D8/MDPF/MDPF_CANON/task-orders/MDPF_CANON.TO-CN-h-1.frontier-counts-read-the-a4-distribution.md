# MDPF_CANON task order -- `CN-h-1` -- THE FRONTIER ACCOUNT COUNTS READ THE NEWEST A4 ACCOUNT-DISTRIBUTION AT OR BEFORE THE AXIS DATE, NEVER THE STAGED RUNNER OBJECT (S5 disarm; FWD-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-h-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~17</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell changes which object a loader reads.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is added that the gold lambda does not already make (it lists and gets under portal/gold/mdpf/ today in load_served_account_count); the criteria read served objects with read-only get/list.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r6_cn_h_1.py reader 1 of 8 (arm H0 is a control), seams 1 of 4 (S4 a control), comparator 1 of 5 (K0 a control) at base; a scratch reference tree reads 8 of 8, 4 of 4 and 5 of 5 (the arms can pass).
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-h-1` (round 7, decomposition v7)

**The rule (the CTO's ADDENDUM 5, which you do not need to read).** The gold lambda sets the FRONTIER account count of every model line from an
account distribution. Today it reads the STAGED runner object `gold/mdpf_revamp/{scope}/account_distribution.json`, which the dispatch stopped
writing on 2026-08-18, so the served 2026-10-09 frontier counts are the 2026-08-17 roster wearing a 2026-10-09 date. From now on the lambda reads
the newest A4 distribution AT OR BEFORE the axis date: `portal/gold/mdpf/{scope}/account-distribution/<date>.json`, key date `<=` the axis date,
where the axis date is the last date of the series being built. If there is none, the counts are ABSENT (None), exactly the honest-None the loader
already returns for an absent staged object; it NEVER falls back to the staged object ("that fallback is how they froze").

**Where it runs.** `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`. Read these first, at HEAD: `load_account_dist_frontier_counts`
(about :769-812), its two call sites (`build_firm_timeseries` about :1203, which serves `49financial` and `inflection`; `build_global_artifact` about
:2520), the two override sites (`acct[-1] = ad_frontier[mkey]` about :1233 and :2623) and `frontier_stamp_staleness` (about :876-912).
Cottonwood never calls the loader: its series is the staged cottonwood slice (`load_cottonwood_slice`); leave it alone.

### Step 1 -- the loader

```
def load_account_dist_frontier_counts(firm_id: str, axis_date: "str | None" = None) -> dict
```

Behaviour, exactly:

1. `axis_date` None or empty: log one WARN naming the scope and return `{}` (honest absent). Do not read anything.
2. List `portal/gold/mdpf/{firm_id}/account-distribution/` in bucket `ASSETS_BUCKET` (`list_objects_v2` paginator). A key qualifies when its file
   name is `<YYYY-MM-DD>.json` (15 characters) and the date is `<= axis_date`. Select the greatest such date. A listing failure of ANY kind raises
   `RuntimeError` whose message STARTS `C2-SIBLING FAIL-LOUD:` (the idiom already in this function: an absence-by-honest-None claim is only for an
   absent object, never for a failed read).
3. No qualifying key: log one WARN naming the scope and the axis date and return `{}`. Never read the staged object, never read any other key.
4. Read the selected object with `get_object` and parse it; keep the existing two failure branches (NoSuchKey returns `{}` with the WARN; any other
   failure and an unparseable body raise the existing `C2-SIBLING FAIL-LOUD` `RuntimeError`).
5. The object's `period` must be present and `<= axis_date`; otherwise log a WARN and return `{}` (a roster from after the axis is never stamped).
6. Return `dict(meta.account_count_by_model_key)` plus, when that map is non-empty, `out["__as_of__"] = period` (the sentinel the callers already
   pop; the staleness verdict then compares the A4's own period with the axis date: FRESH when equal, STALE when older, never refused).
7. Update the docstring: the source is the A4 distribution, the selection rule, the fail-closed rule, and that the staged object is no longer read.
   Remove nothing else. Do not edit `frontier_stamp_staleness`, `carry_forward_with_basis` or the `meta.frontier_count` stamp (its keys stay
   `date`, `source`, `staleness`; no new key anywhere).

### Step 2 -- the two call sites

In `build_firm_timeseries`: `ad_frontier = load_account_dist_frontier_counts(firm_id, dates[-1] if dates else None)`.
In `build_global_artifact`: `ad_frontier = load_account_dist_frontier_counts("global", dates[-1] if dates else None)`.
Nothing else at the sites changes: the `__as_of__` pop, the staleness log line, the override `if acct and ad_frontier.get(mkey) is not None:
acct[-1] = ad_frontier[mkey]`. A series key that is in the series but NOT in the A4 map keeps its COMPOSED count (the merged Global fold, CN-f-1,
drops the folded model keys from the A4 map; the two inflection blends and the fold line are such keys): state that in the docstring.

### Step 3 -- two existing tests stub the loader with a one-argument lambda

`data/mdpf/scripts/gold/tests/test_canplat_p1_1.py` (about :88, `load_account_dist_frontier_counts=lambda firm: {}`) and
`data/mdpf/scripts/gold/tests/test_global_fold_flag2.py` (about :46, `spine.load_account_dist_frontier_counts = lambda firm: {}`). The new call
passes two arguments, so each lambda must accept the second one: change exactly that lambda to `lambda firm, axis_date=None: {}` and nothing else
in those files.

### Step 4 -- tests (new file, synthetic data, no network; a fake S3 client injected through the module's `_s3` factory)

`data/mdpf/tests/canon/test_frontier_counts_a4.py`, at least FIVE tests: (a) the newest key at or before the axis date is read (axis on a key,
between keys, after every key); (b) no key at or before the axis date returns `{}` and the staged key is never requested, even when a staged object
exists; (c) a listing failure raises with the `C2-SIBLING FAIL-LOUD` prefix; (d) an object whose `period` is after the axis date is refused;
(e) the `__as_of__` sentinel equals the object's `period` and `frontier_stamp_staleness` reads FRESH on equal dates and STALE on an older period.
Idiom of `data/mdpf/tests/canon/test_global_served_identity.py`. The issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r6_cn_h_1.py` (`FakeS3`, `reader`; read it, never edit it) shows the
fake client's shape.

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`/`rm`, no `safe-deploy`. Read-only `get`/`list`/`describe` is
   allowed (criterion AC3 reads served objects). No install, no push. REFUSE, do not rescue. The deploy of this code is CloudOps's, in its own
   window, after a never-widen pair; none of it is yours.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). Everything else in
   `dim_mdpf_aggregate_aua_timeseries.py` is read-only; so are the staged object, the dispatch script, `build_mdpf_spine.py`,
   `dim_mdpf_account_distribution.py`, `mdpf_gold_consolidator.py`, the stage-6 scripts and every existing test not named in Step 3.
3. **Never** write, repair or refresh the staged `gold/mdpf_revamp/*/account_distribution.json`; never add a fallback to it; never add a
   `PYTHONPATH`, a `lib/` file or a registry file (Stage 6 is a separate question, ruled out by the CTO).
4. **No new key** in any served object or in `meta.frontier_count`; no change to `count_coverage_end`, the carry rules or the SMA preserve keys.
5. **CLIENT DATA:** never print an account id. No non-ASCII. Keep each file's line endings as you find them (read them first). Use the Edit tool.
6. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
data/mdpf/scripts/gold/tests/test_canplat_p1_1.py
data/mdpf/scripts/gold/tests/test_global_fold_flag2.py
data/mdpf/tests/canon/test_frontier_counts_a4.py
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-h-1.frontier-counts-read-the-a4-distribution.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~17/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` (the fold and the build order),
`data/mdpf/tests/canon/test_global_served_identity.py` (the idiom) and the issuer's checks under
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/` (`r6_cn_h_1.py`; never edit it, read what each arm asserts).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r6_cn_h_1.py" reader; echo "exit=$?"</invocation><expect>CN-H-1 READER: 8 of 8 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r6_cn_h_1.py" seams; echo "exit=$?"</invocation><expect>CN-H-1 SEAMS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r6_cn_h_1.py" comparator; echo "exit=$?"</invocation><expect>CN-H-1 COMPARATOR: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="CN-h-1" judgment="true"/>
</proof_of_spec>

AC4 is JUDGMENT, graded at the round-7 close (never self-graded): `/seams` on the loader-to-served seam, grounded on the objects after the first
scheduled run that carries the code -- MECHANICAL (each scope's served `account_count[-1]` of every overridden key equals the selected A4 map's value),
DECLARATIVE (`meta.frontier_count.staleness` names the A4's own as-of and reads FRESH on equal dates), SEMANTIC (the only client-visible deltas
are the ones the never-widen pair names: the per-scope frontier count moves and the aum-metrics row counts that follow them).

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~17/MDPF_CANON.TO-CN-h-1.frontier-counts-read-the-a4-distribution.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for), with AC4 UNVERIFIABLE-BY-INSTRUMENT and status_reason
"graded at the round-7 close". **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your
paths), and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W17-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the delta table AC3 prints, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7 (or an addendum to round 6, the CTO's call), issuer 2.0.0_SA_COO~D1, on the CTO's round-5 ADDENDA 3-5
(`ledger/ROUND_ANALYSIS.round5.md`; msgs 4773, 4776, 4780, 4782): "S5 becomes: the Lambda's frontier counts read the frozen 08-18 distribution.
Disarm it by moving that input off the runner object, under a priced pair, ahead of M10 ... Use the newest A4 at or before the axis date. If none
exists, refuse the counts (honest absent) and never fall back to the staged runner object ... Name the per-scope moves in the pair (global +424),
state both branches, and record prior VersionIds. Cut it after the fold's first fire is read. S5 disarms on its read-back."
- **Measured (issuer's price, `round6/S5_FRONTIER_COUNTS_PRICE.md` @b246f4786f, and this draft's comparator on the 2026-10-09 objects):**
  the served 2026-10-09 frontier counts equal the staged 2026-08-17 roster on 19 of 19 mapped keys (global 7, 49financial 5, inflection 7).
  On the A4 keyed 2026-10-12 the global move is +424 (8264 -> 8688); on the A4 keyed 2026-10-09, the one the rule selects for the 2026-10-09
  axis, the comparator prints global +419 (8264 -> 8683), 49financial +330 (7144 -> 7474), inflection +12 (548 -> 560). The first fire's actual
  numbers are read from that fire, not from either table.
- **Two things the draft carries that the brief did not name:** (1) two existing tests stub the loader with a one-argument lambda
  (`test_canplat_p1_1.py:88`, `test_global_fold_flag2.py:46`); the new call passes two arguments, so they are in the grant, one lambda each;
  (2) the A4 object for date D is the roster as of D (its `period` equals its key on every key read), so "newest key <= axis date" is the in-run-safe
  rule: the in-run A4 is keyed by the run date, after the axis, and is never selected (no circularity).
- **Not in this cell:** Stage 6 (ruled out), the `lib` sync, the nine runner keys, the IAM change on the runner role, `dim_mdpf_account_distribution.py`,
  the staged object itself (it stays frozen and unread by the lambda; its retirement is M12).
- **Pair:** `round7/draft/NEVER_WIDEN_PAIR_R7_CN_H_1.md` (COO half drafted, unsigned). **Deploy order:** a CloudOps WORLD order cut after the drain,
  by the CN-d-1 order's shape (named file, build_package at the merge pin, targeted safe-apply on `mdpf-gold-lambda`, the commit stamp
  `MDPF_GOLD_COMMIT` set from the pin built); its first scheduled fire is 2026-10-15 13:30Z at the earliest, after the fold's first fire
  (2026-10-14) is read; one change per fire.
- **Risk and class:** WORLD, on the CN-d-1 and CN-f-1 precedents (the cell changes served bytes once deployed and carries a never-widen pair).
  `worker-light`: about 40 product lines and one behaviour (CN-d-1 and CN-d-2 were light at the same size).
- **Fanout:** one cell, one chain, slot ~17. Base box/dell1.

<status>pending</status>
<round>7</round>
<to_id>MDPF_CANON.TO-CN-h-1</to_id>
<slot>~17</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
