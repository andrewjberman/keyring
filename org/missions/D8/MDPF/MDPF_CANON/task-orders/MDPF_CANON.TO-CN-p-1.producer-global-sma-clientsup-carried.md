# MDPF_CANON task order -- `CN-p-1` -- THE GLOBAL AUA SERIES SERVES THE TREND GROUPS (CLIENT SUPERVISED, ETF STRATEGIES, ALT STRATEGIES, CARRIED DATES) FROM SMARTX AND GLOBAL'S OWN FIELDS; MUNI LEAVES THE SMA TREE (VARIANT 1; FWD-9)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-p-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~26</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell adds fields to an object the existing scheduled run already writes.
comp-iam: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1: `comp-iam simulate mdpf-gold-lambda-role s3:GetObject <arn>` on the aum-daily key and on the allocation-roster key (date=2026-10-14) -- decision=allowed on both, APPLIED plane (simulated, not EXERCISED; a real read is the first scheduled fire). No IAM change is made.
comp-adversary: RUN by the issuer on DELL1 at box/dell1 -- r9_cn_p_1.py pure 2 of 7 (M0, P0 controls), seams 2 of 7 (S0, T2 controls), oracle 2 of 7 (O0, Om controls) at base; a scratch reference tree reads 7 of 7, 7 of 7, 7 of 7 (the arms can pass); eight planted defects (a typed s3 literal, a missing Global All Equity TR subtraction, an unedited existing test, Muni kept, keys on Global only, a mutated input, a loader raise swallowed into empty legs, a loader raise that empties every scope) each turn at least one arm red; `r9_cn_p_1.py selftest` prints `CN-P-1 SELFTEST: OK`. AMENDMENT 1 re-ran all of it; the built branch @7d171b2281 reads seams 6 of 7 (S7 red).
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 0. AMENDMENT 1 -- READ THIS FIRST (you inherit built work)

Your branch `wk-MDPF_CANON-26` @`7d171b2281` already holds items 1, 2, 4, 5 and 6 below: keep them as they are. **Only item 3 (the `build_all` wiring) and one added test, (f), change.** Your own row `MDPF_CANON-D1-W26-S2` is right: the wiring `_smx = _isolated(...) or ({}, None)` turns the loader's `C2-SIBLING FAIL-LOUD` raise (a denied or failed SMArtX read) into empty legs, so Global would be built and published with null pre-2026-05-18 groups. That is a fail-open. A raise must leave Global refused ALONE (`arts["global"] = None`, `apply_global_trend_groups` not called); only `({}, None)` (no partition in the lookback: the honest absent, already WARNed) applies with empty legs.

What to do, in this order:
1. Bring trunk into your branch with a merge (`git merge box/dell1`, never a rebase) to receive the amended `round9/checks/r9_cn_p_1.py` (new arm S7, new `selftest` mode) and this amended order.
2. Replace the two wiring lines at about `mdpf_gold_consolidator.py:3060-3061` with the item 3 block below (CRLF file: Edit tool, keep its line endings). Nothing else in that file changes.
3. Add test (f) to `data/mdpf/tests/canon/test_global_trend_groups.py` (item 6) and keep (a)-(e).
4. Re-run all three criteria (AC2 now reads 7 of 7). Update your proof instance, then commit with a message file written by the Write tool.

## 1. THE CELL -- `CN-p-1` (round 9)

**The rule (PRD v2.19-v2.21, which you do not need to read).** The portal's Global AUA Trend will draw three groups it must READ from the served Global series, never recompose: Client Supervised, ETF Strategies, ALT Strategies. This cell makes the gold consolidator serve them, plus the dates on which a value was rolled forward. Nothing else about any served figure moves: every existing key of every scope stays byte-equal (check O5 reads it).

- `client_supervised_aua[i]` = `non_model_aua[i]` - Dividend - Growth - Opal Global All Equity Total Return.
- `etf_strategies_aua[i]` = Dividend + Growth + `sma_additive_aua[i]` (PFDE).
- `alt_strategies_aua[i]` = `tax_additive_aua[i]` (Tax-Managed ONLY). Muni is not an SMA.
- Dividend and Growth come from the SMArtX table (`closing_equity` per model per day) on dates BEFORE 2026-05-18, and from Global's own `by_model.opal_div_sma.model_value` / `opal_growth_sma.model_value` from 2026-05-18 (SMArtX equals them to $0.00 there). The Global All Equity Total Return model exists only in SMArtX (2024-08-30 to 2025-03-26) and is subtracted only before 2026-05-18.
- A row with no total (or no `non_model_aua`) has no value of its own; before 2026-05-18 a row with no SMArtX leg has none either (absent is NOT zero). Each group then takes its LAST KNOWN value (roll FORWARD only; never fill a row before the group's first value), and every date on which any group was filled that way goes in `carried_dates` (ISO strings, sorted). The 9 dates with no total today are 2026-05-30, 05-31, 06-06, 06-07, 06-13, 06-14, 06-19, 06-20, 06-21.
- Every other scope gains the same four keys all-None / `[]` (the key-set identity check has no ruled extra, so a key on Global alone would refuse the run). Global's `meta` gains `trend_groups`.
- The category tree drops the "Muni SMA" member of `SMA > ALT Strategies`.

**SMArtX read.** Two registry rows exist (landed in `infra/logic/registry/legacy_addresses.json`; read-only for you): call `legacy_address("smartx-platform-silver-fact-model-aum-daily", date=<d>)` and `legacy_address("smartx-platform-silver-fact-model-allocation-roster", date=<d>)`. Each returns `s3://opal-data-assets/smartx/platform/silver/<name>/date=<d>/data.parquet`; `.split("/", 3)[3]` leaves the key for `get_object(Bucket=ASSETS_BUCKET, ...)`. A call without `date` raises. Each partition carries the FULL history: read ONE partition (the newest that exists among the run date and the 9 days before it), not one per day. The code types NO `smartx/...` or `fact_model...` string. Columns: aum-daily `rmid`, `day` (a date), `closing_equity`; roster `rmid`, `model_name`. Model names: `Opal Dividend Income`, `Pathfinder Focused Opportunities`, `Opal Global All Equity Total Return`.

**The code (statement-level edits, in this order; the file is CRLF: keep its line endings; use the Edit tool).** File: `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`. The checks grade BEHAVIOUR by calling these three functions, by AST (no typed address; call order in `build_all`) and by EXECUTING the `build_all` statements from the load call to the apply call with stubs (arm S7), so a different but equivalent body is acceptable; the names, signatures and return shapes are the contract.

1. Import, directly ABOVE the line `from lib.opal_naming import address as taxsma_address  # noqa: E402 -- TX-a-2's own two` (leave that line and its comment continuation as they are):

```
from lib.opal_naming import legacy_address as smartx_legacy_address  # noqa: E402 -- MDPF_CANON CN-p-1: the two SMArtX read keys come from registry rows, never typed
```

2. Add this block at module level directly ABOVE `def write_taxsma_category_gold(`:

```
TREND_GROUP_KEYS = ("client_supervised_aua", "etf_strategies_aua", "alt_strategies_aua")
TREND_CARRIED_KEY = "carried_dates"
TREND_SMARTX_UNTIL = "2026-05-18"
SMARTX_AUM_ROW = "smartx-platform-silver-fact-model-aum-daily"
SMARTX_ROSTER_ROW = "smartx-platform-silver-fact-model-allocation-roster"
SMARTX_ROLE_OF_MODEL = {"Opal Dividend Income": "div", "Pathfinder Focused Opportunities": "growth",
                        "Opal Global All Equity Total Return": "gaetr"}
SMARTX_LOOKBACK_DAYS = 10


def compute_trend_groups(g: dict, smartx: dict) -> dict:
    """Pure. `g` is one Global timeseries dict; `smartx` is {iso date: {"div": $, "growth": $, "gaetr": $}}.
    Returns {"client_supervised_aua": [...], "etf_strategies_aua": [...], "alt_strategies_aua": [...],
    "carried_dates": [...]}, every list aligned to g["dates"]. Never mutates `g`."""
    dates = list(g.get("dates") or [])
    n = len(dates)

    def _col(v):
        v = list(v or [])
        return v + [None] * (n - len(v))

    total, nm = _col(g.get("opal_aggregate_aua")), _col(g.get("non_model_aua"))
    tax, sma = _col(g.get("tax_additive_aua")), _col(g.get(SMA_ADDITIVE_KEY))
    bm = g.get("by_model") or {}
    div_g = _col((bm.get("opal_div_sma") or {}).get("model_value"))
    growth_g = _col((bm.get("opal_growth_sma") or {}).get("model_value"))
    raw = {k: [None] * n for k in TREND_GROUP_KEYS}
    for i, d in enumerate(dates):
        if total[i] is None or nm[i] is None:
            continue
        if d < TREND_SMARTX_UNTIL:
            leg = smartx.get(d)
            if leg is None:
                continue
            div, growth, gaetr = (leg.get(r) or 0.0 for r in ("div", "growth", "gaetr"))
        else:
            div, growth, gaetr = div_g[i] or 0.0, growth_g[i] or 0.0, 0.0
        raw["client_supervised_aua"][i] = round(nm[i] - div - growth - gaetr, 2)
        raw["etf_strategies_aua"][i] = round(div + growth + (sma[i] or 0.0), 2)
        raw["alt_strategies_aua"][i] = None if tax[i] is None else round(tax[i], 2)
    out: dict = {}
    carried: set = set()
    for k in TREND_GROUP_KEYS:
        last, col = None, []
        for i, d in enumerate(dates):
            v = raw[k][i]
            if v is not None:
                last = v
            elif last is not None:
                v = last
                carried.add(d)
            col.append(v)
        out[k] = col
    out[TREND_CARRIED_KEY] = sorted(carried)
    return out


def load_smartx_sma_legs(s3, today: str, lookback: int = SMARTX_LOOKBACK_DAYS) -> tuple:
    """Reads ONE SMArtX partition: the newest of `today` and the days before it that exists. Returns
    ({iso date: {"div"|"growth"|"gaetr": closing_equity}}, partition date). None exists -> ({}, None) and a WARN.
    A denied or failed read is never an absence: RuntimeError whose message STARTS `C2-SIBLING FAIL-LOUD:`."""
    import io
    import pyarrow.parquet as pq   # noqa: PLC0415
    day0 = dt.date.fromisoformat(today)
    denied: list = []
    for k in range(lookback):
        d = (day0 - dt.timedelta(days=k)).isoformat()
        keys = [smartx_legacy_address(row, date=d).split("/", 3)[3] for row in (SMARTX_AUM_ROW, SMARTX_ROSTER_ROW)]
        try:
            bodies = [s3.get_object(Bucket=ASSETS_BUCKET, Key=key)["Body"].read() for key in keys]
        except s3.exceptions.NoSuchKey:
            continue
        except Exception as e:  # noqa: BLE001 -- deliberate breadth BECAUSE it re-raises
            code = ((getattr(e, "response", None) or {}).get("Error") or {}).get("Code")
            if code in ("AccessDenied", "403"):
                denied.append(d)
                continue
            raise RuntimeError(f"C2-SIBLING FAIL-LOUD: SMArtX partition read FAILED (NOT absent) for {keys[0]} "
                               f"({type(e).__name__}: {e})") from e
        names = {r["rmid"]: r["model_name"] for r in
                 pq.read_table(io.BytesIO(bodies[1]), columns=["rmid", "model_name"]).to_pylist()}
        legs: dict = {}
        for r in pq.read_table(io.BytesIO(bodies[0]), columns=["rmid", "day", "closing_equity"]).to_pylist():
            role, v = SMARTX_ROLE_OF_MODEL.get(names.get(r["rmid"])), r["closing_equity"]
            if role is None or v is None or v != v:
                continue
            legs.setdefault(str(r["day"])[:10], {})[role] = round(float(v), 2)
        return legs, d
    if denied:
        raise RuntimeError(f"C2-SIBLING FAIL-LOUD: SMArtX partition read DENIED on {denied} (NOT absent)")
    log(f"  WARN trend-groups: no SMArtX partition in the {lookback} days to {today} -> the Trend groups before "
        f"{TREND_SMARTX_UNTIL} stay honest-None")
    return {}, None


def apply_global_trend_groups(arts: dict, smartx: dict, smartx_partition: "str | None" = None) -> dict:
    """Every built scope gains the three group keys and carried_dates (Global computed, the rest all-None / []).
    Returns NEW dicts: the input `arts` is never mutated. Global's meta gains trend_groups."""
    out = {k: (dict(v) if v is not None else None) for k, v in arts.items()}
    for scope, doc in out.items():
        if doc is None:
            continue
        for k in TREND_GROUP_KEYS:
            doc[k] = [None] * len(doc.get("dates") or [])
        doc[TREND_CARRIED_KEY] = []
    g = out.get("global")
    if g is not None:
        g.update(compute_trend_groups(g, smartx))
        meta = dict(g.get("meta") or {})
        meta["trend_groups"] = {"smartx_partition": smartx_partition, "smartx_legs_until": TREND_SMARTX_UNTIL,
                                "smartx_dates": len(smartx)}
        g["meta"] = meta
    return out
```

3. In `build_all`, directly BELOW the line that reads `arts, fold_report = guard_global_min_firms_fold(arts, _isolated)   # CN-f-1: ...`, add (a raise from the loader is a denied or failed SMArtX read: Global is refused ALONE, as the fold's refusal leaves it, and `apply_global_trend_groups` is NOT called; `({}, None)` is the honest absent and still applies):

```
    _smx = _isolated("global", lambda: load_smartx_sma_legs(s3, process_start.date().isoformat()))
    if _smx is None:
        arts = dict(arts)
        arts["global"] = None
    else:
        arts = apply_global_trend_groups(arts, _smx[0], _smx[1])
```

No `or ({}, None)` on the first statement: it turns a raise into empty legs and publishes Global with null groups before 2026-05-18. Do not empty any scope other than Global (S7 grades both). `_isolated` already records the error in the manifest, so the run reads non-green.

4. Muni leaves the tree. File `data/mdpf/scripts/gold/mdpf_category_registry.py` (CRLF): in `SMA_MEMBERS`, delete the `("muni", "muni", "Muni SMA", True, "ALT Strategies", SMA_BASIS_CARVE_OUT),` tuple and its seven-line comment above it; put ONE comment line in their place: `# muni: removed (Andrew-direct 2026-10-14: "no muni in SMAs, Muni is no longer SMA" / "muni is just a custom model").` Do not touch `SMA_BASIS_VERIFIED`, the crosswalk or any other line. Existing non-ASCII elsewhere in these files stays as it is.

5. The one existing test that names Muni: `data/mdpf/tests/stratid/test_stratid_round2_inside_model.py` (CRLF), the line `assert set(rows) >= {"divz", "pfoe", "muni", "tax", "idvz", "pfde"}` becomes `assert set(rows) >= {"divz", "pfoe", "tax", "idvz", "pfde"} and "muni" not in rows`. Nothing else in that file changes.

6. New test file `data/mdpf/tests/canon/test_global_trend_groups.py`, synthetic data only, no network, at least SIX tests: (a) the difference, ETF sum and roll-forward on a small dict that straddles 2026-05-18; (b) a pre-cut-off row with no SMArtX leg is None, not zero; (c) ALT is never filled before its first value and the first dated row is never in `carried_dates`; (d) `apply_global_trend_groups` gives every non-None scope the four keys, leaves a None scope None and does not mutate its input; (e) `load_smartx_sma_legs` on a fake S3 reads exactly two objects when today's partition exists and raises `C2-SIBLING FAIL-LOUD` on AccessDenied; (f) the `build_all` wiring: parse the module with `ast`, take `build_all`'s top-level statements from the first one that calls `load_smartx_sma_legs` to the last one that calls `apply_global_trend_groups`, `exec` them with stubs for `arts`, `_isolated` (returns None when the callable raises), `s3`, `process_start`, the loader and apply -- a loader that raises `RuntimeError("C2-SIBLING FAIL-LOUD: x")` leaves `arts["global"]` None, the other scopes unchanged and apply uncalled; a loader returning `({}, None)` calls apply exactly once with `({}, None)`. Idiom of `data/mdpf/tests/stratid/test_stratid_round2_inside_model.py` (module import via `sys.path`). The issuer's check `round9/checks/r9_cn_p_1.py` (`FakeS3`, `_smx_fixture` for the fake client and parquet fixtures; `_grade_wiring` for how test (f) can slice and exec the wiring; read it, never edit it).

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`/`rm`, no `safe-deploy`. Read-only `get`/`list`/`describe` is allowed (criterion AC3 reads served objects and one SMArtX partition). No install, no push. REFUSE, do not rescue. The deploy of this code is CloudOps's, in its own window, after a never-widen pair; none of it is yours.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). Everything else is read-only; in particular `infra/logic/registry/legacy_addresses.json`, `lib/opal_naming.py`, `build_package.py` (it already ships both), `apply_sma_sleeve_overlay`, `apply_global_min_firms_fold` and the A4 shaping.
3. **Never** type an s3 address, a bucket-relative SMArtX key or a `smartx/` string in code; **never** add a registry row, a `lib/` file or a `PYTHONPATH` of your own; if the builder refuses, file a row and stop.
4. **No existing key moves.** Do not change `point_class`, `opal_aggregate_aua`, any `by_model` entry, or any existing `meta` key. `R2_RULED_EXTRAS` stays as it is (the new keys go on EVERY scope).
5. **CLIENT DATA:** never print an account id or a firm level (print dates, counts and differences). No non-ASCII in any text you add. Keep each file's line endings as you find them (read them first). Use the Edit tool.
6. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/mdpf_gold_consolidator.py
data/mdpf/scripts/gold/mdpf_category_registry.py
data/mdpf/tests/stratid/test_stratid_round2_inside_model.py
data/mdpf/tests/canon/test_global_trend_groups.py
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-p-1.producer-global-sma-clientsup-carried.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~26/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `infra/logic/registry/legacy_addresses.json` (the two SMArtX rows, reader `MDPF_CANON`), `lib/opal_naming.py` (`legacy_address`), `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` (`apply_sma_sleeve_overlay`, `apply_global_min_firms_fold`, `assert_keyset_identity`) and the issuer's checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/` (`r9_cn_p_1.py`; never edit it, read what each arm asserts).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-p-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_p_1.py" pure; echo "exit=$?"</invocation><expect>CN-P-1 PURE: 7 of 7 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-p-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_p_1.py" seams; echo "exit=$?"</invocation><expect>CN-P-1 SEAMS: 7 of 7 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-p-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_p_1.py" oracle; echo "exit=$?"</invocation><expect>CN-P-1 ORACLE: 7 of 7 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="CN-p-1" judgment="true"/>
</proof_of_spec>

AC4 is JUDGMENT, graded at the round close (never self-graded): `/seams` on the producer-to-served seam, grounded on the objects after the first scheduled run that carries the code -- MECHANICAL (the served Global object carries `client_supervised_aua`, `etf_strategies_aua`, `alt_strategies_aua` and `carried_dates` aligned to `dates[]`; every other scope carries them all-None / `[]`; every pre-existing key of every scope is equal to the prior day's rule), DECLARATIVE (`meta.trend_groups.smartx_partition` names the partition read; `category-views` for every scope that carried "Muni SMA" no longer lists it), SEMANTIC (the only client-visible deltas are the ones the never-widen pair names: the new keys and the Muni member leaving `SMA > ALT Strategies`).

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~26/MDPF_CANON.TO-CN-p-1.producer-global-sma-clientsup-carried.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for), with AC4 UNVERIFIABLE-BY-INSTRUMENT and status_reason
"graded at the round close". **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your
paths), and only when every mechanical criterion passes. Commit through `.tools/safe-commit.sh` with a message file written by the Write tool; the commit gate (py_compile, ds-precommit, ruff py39) and the naming gate must pass -- if either refuses anything this order did not foresee, file a row and stop.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W26-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (issuer, 2.0.0_SA_COO~D1, after the worker's row MDPF_CANON-D1-W26-S2; the amendment commit states which gate limb graded the modification, or that none did): the item 3 wiring was fail-open (`or ({}, None)` turned the loader's FAIL-LOUD raise into empty legs); corrected to refuse Global alone; check arm S7 added (behavioural, seams 6 -> 7), test (f) added, AC2 expect 6 -> 7. The CTO reads it at the round-N analysis. Built state inherited: branch `wk-MDPF_CANON-26` @7d171b2281 holds items 1, 2, 4, 5, 6.**

**ISSUER NOTES:** round 9, issuer 2.0.0_SA_COO~D1, on the CTO's msgs 5868-5886 and PRD v2.19-v2.21 (Andrew: Variant 1, "we might as well put the SMA strategies in there, we do have them", "Muni is just a custom model"). Spec: `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_CANON_GLOBAL_AUA_TREND_FULL_HISTORY_SPEC_20261014.md` @686f769e63.
- **Measured by the drafter (read-only, 2026-10-14):** on the served 2026-10-13 Global object the rule above reproduces the CRO's amended period-end oracle at all 9 period ends (max diff 0.00M); `model_aua + groups + the pre-05-15 Global All Equity TR leg` equals the total on all 487 dated rows (max 0.00); the 9 no-total dates are the 9 named; SMArtX equals Global's carve-outs on 103 overlap dates (max diff 0.00); SMArtX covers all 384 pre-05-18 dated rows. Client Supervised from the rule is continuous across 05-18 (checked by the CRO; the oracle arms O2/O3 grade it).
- **Contract fixed for CN-p-2 (portal), served on Global:** top-level `client_supervised_aua[]`, `etf_strategies_aua[]`, `alt_strategies_aua[]` (number or null, aligned to `dates[]`; null before the group's first value, never back-filled) and `carried_dates[]` (ISO strings). `point_class[]` is NOT changed (the headline must stay byte-equal), so the portal marks a carried point from `carried_dates`. Custom Models is NOT served by this cell (the portal takes the difference `model_aua` - the five primary lines from 2026-05-15; before 05-15 the internal-session stitch supplies it).
- **Decisions the drafter took and the issuer may overrule:** (1) new keys are on EVERY scope (all-None / `[]` off Global), because `assert_keyset_identity` has no ruled extra and a Global-only key refuses the whole run -- the alternative is a `R2_RULED_EXTRAS` entry, which is a contract amendment (CTO). (2) The gold parquet writer carries every list whose length equals `len(dates)` as a column, so the four-scope `aggregate_aua_timeseries` parquet gains three series columns (new partitions only; the pair names it). (3) SMArtX absent for every candidate day -> pre-05-18 groups stay None (honest absent) and the run stays green; denied/failed -> fail loud, Global refused alone (the isolation wrapper). (4) `TREND_SMARTX_UNTIL` is a constant (2026-05-18, the CRO spec's boundary), not derived from the data.
- **Deploy and pair:** WORLD. A same-`as_of` re-run would record `conflict` (A8); the first fire after the deploy mints a new date, so it is not reached. The pair (COO half) must: count the writers of each moved leaf (N printed; Global/49F/Inflection/Cottonwood `aggregate-aua-timeseries` gain keys, `category-views` for every scope that listed "Muni SMA" loses a member, parquet gains columns), state both branches, record prior VersionIds, and name the headline sums byte-equal. CloudOps ADHOC order by the CN-h-1 shape (named file, build_package at the merge pin, targeted safe-apply on `mdpf-gold-lambda`, `MDPF_GOLD_COMMIT`); its first fire is 2026-10-15 13:30Z at the earliest only if CN-h-1/CN-l-1 do not already occupy it -- ONE change per fire, so this order's fire is the next free one.
- **Base and ordering:** the worker's base must contain `ff00e3e265` (the two registry rows). CN-p-2 reads the contract above and does not wait on this cell's deploy to be BUILT; its real run does.
- **Risk and class:** WORLD, on the CN-d-1/CN-f-1/CN-h-1 precedents. `worker`: three functions and two small edits (about 130 product lines, two behaviours) plus a new test file.
- **Fanout:** one cell, one chain, slot ~26. Base box/dell1.
- **Not in this cell:** the portal (CN-p-2); Custom Models; any pre-2026-05-15 per-model value in any Global leaf (PRD v2.20: the portal stitches it read-side); `point_class`; a `R2_RULED_EXTRAS` entry; the deploy; the pair.

<status>pending</status>
<round>9</round>
<to_id>MDPF_CANON.TO-CN-p-1</to_id>
<slot>~26</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
