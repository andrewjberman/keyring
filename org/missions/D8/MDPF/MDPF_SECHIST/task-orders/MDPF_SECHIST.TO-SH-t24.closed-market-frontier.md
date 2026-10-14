# TO MDPF_SECHIST.TO-SH-t24 -- round 6 SH-t-24: closed-market frontier (carry the last vendor day, with its date, under three guards)

<to_id>MDPF_SECHIST.TO-SH-t24</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~23</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>CLOSEDMKT</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-24` (`decompositions/MDPF_SECHIST_DECOMP_R6.md`) | **outcome_ref:** FWD-9 |
**depends_on:** none (the deploy that moves served returns is a separate act under its own never-widen pair, after this cell drains)

---

## WORKER FACE

### THE CELL

`SH-t-24` (FWD-9, CTO ruling ADDENDUM 2 of `org/missions/D8/MDPF/MDPF_SECHIST/ledger/ROUND_ANALYSIS.round5.md`). Today a security with NO vendor day on a book's as_of (SALXX on 2026-10-12,
Columbus Day, bond market closed) has every return window blanked, because `compute_returns` in `data/etfs/scripts/gold/etf_positioning_gold.py` (the `if as_of not in have: return out` FRONTIER test)
treats "no observation ON as_of" as stale. The ruling: the frontier is the security's last vendor day on or before as_of, the windows are anchored and LABELED on it, under three guards.

Build, in `data/etfs/scripts/gold/etf_positioning_gold.py`, `data/etfs/scripts/gold/etf_positioning_publisher.py` and ONE new test file. `compute_returns` itself stays byte-identical; do not edit it.

1. **New function in the gold script** (module level, after `compute_returns`), exactly this interface:

```
CARRY_MAX_CALENDAR_DAYS = 4

def frontier_returns(tkr, as_of, hist, gap_record=None) -> tuple[dict[str, float | None], dt.date | None]:
```
   - A reading ON as_of (a row for that tkr and date, a NULL return value counts as a reading): return `(compute_returns(tkr, as_of, hist, gap_record), as_of)`. A NULL reading therefore stays blank through compute_returns' own rule (C-MMF unchanged).
   - No row on as_of: let `f` be the greatest date of that tkr's rows that is before as_of. Carry ONLY when ALL hold: `f` exists; `(as_of - f).days <= CARRY_MAX_CALENDAR_DAYS`; `gap_record` is not None; the gap record's `securities` carries `tkr`; and that entry's `absent_count` is 0 (read through the existing `_gap_days`, whose second value is `absent_count`, or the `securities` entry directly). Then return `(compute_returns(tkr, f, hist, gap_record), f)`.
   - Otherwise return `({w: None for w in RETURN_WINDOWS}, None)`.
2. **`build_tables`** (same file, the call near `compute_returns(tkr, ret_as_of, hist, gap_record)` where `rec.update({"return_" + w: ...})` is built): call `frontier_returns` instead, keep the `ret_as_of is None` branch blank, and add ONE new key to the holding record `rec`: `"return_frontier": <the frontier date or None>`. The synthesized NAV-residual record (the `resid.update({"return_" + w: None ...})` line) gets `"return_frontier": None`. `holding_df` is built from the record dicts, so the column follows; do not hand-edit a column list unless one exists (check first).
3. **Publisher** (`data/etfs/scripts/gold/etf_positioning_publisher.py`, `build_document` near line 447): a holding gets an extra key `"returns_frontier": "<ISO date>"` ONLY when its `return_frontier` is not null AND differs from the book's `data_as_of`. A book gets an extra key `"returns_frontier_holdings": [{"ticker": "<t>", "frontier": "<ISO date>"}, ...]` (sorted by ticker) ONLY when at least one of its holdings carried. When nothing carried, NEITHER key is emitted: the served JSON of a session-day holding and book is byte-identical to today's. Do NOT add either key to `HOLDING_KEYS` or `BOOK_KEYS` (those are required-key lists; a required optional key would fail the shape check on every ordinary book). Dates go out through the module's existing `_date_out`.
4. **New test file** `data/etfs/scripts/gold/test_etf_positioning_closed_market_frontier.py`, offline (no S3), ASCII only, same style as `data/etfs/scripts/gold/test_etf_positioning_mmf_rule.py` (read it first for the `_hist` and gap-record fixtures). One test per arm: (a) a tkr with rows through Fri 2026-10-09 and none on Mon 2026-10-12, gap record carrying it with `absent_count` 0 -> windows equal `compute_returns` at 10-09 and frontier 10-09; (b) the last row 5 calendar days before as_of -> all windows None, frontier None; (c) `absent_count` 1 -> blank; (d) a NaN return ON as_of for a money-market ticker -> frontier == as_of, every window None; (e) a tkr with a reading on as_of -> `frontier_returns` windows equal `compute_returns` exactly and frontier == as_of; and a publisher test: `build_document` over a one-book fixture where one holding carried emits `returns_frontier` on that holding and `returns_frontier_holdings` on the book, and the same fixture with nothing carried emits neither key anywhere.

When AC1 and AC2 pass, the existing gold suites must still pass; run them once at the end and put the result in your report (not a criterion): `python -m pytest data/etfs/scripts/gold -q`.

### ACCEPTANCE

<criterion id="SH6-t24-AC1" cell_refs="SH-t-24"><invocation>python -m pytest data/etfs/scripts/gold/test_etf_positioning_closed_market_frontier.py -q</invocation><expect>passed</expect></criterion>

<criterion id="SH6-t24-AC2" cell_refs="SH-t-24"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R6_CHECKS/r6_closed_market_real.py</invocation><expect>CM-REAL-OK D=2026-10-13</expect></criterion>

<expected_criteria>SH6-t24-AC1,SH6-t24-AC2</expected_criteria>

Both FAIL at the base (2026-10-14 ~14:0xZ): AC1 because the test file does not exist (pytest rc 4, "file or directory not found"); AC2 prints `CM-REAL-BAD frontier_returns-missing-in-etf_positioning_gold`. AC2 reads the real S3 history (about 25 seconds, read-only) and prints the MOVED set: report that line in your final message. Run each invocation from the worktree root. Do not edit anything under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/`.

## BOUNDS

- Write only the files in `<paths>`. No S3, DynamoDB, Lambda or Terraform write; no gold, publisher or pull run against AWS; no Bloomberg call. Do not edit `compute_returns`, `etf_daily_pull.py`, `build_package.py`, or anything under `portal/`.
- The portal reads the served page through an allowlist adapter (`portal/src/pages/Positioning/shared/etfAdapter.ts`); that rung is another seat's. Your report names the two new served key names (`returns_frontier`, `returns_frontier_holdings`) and nothing more about the portal.
- ASCII only in code and tests (CLAUDE.md). Every `.py` edit must pass `.tools/commit-gate.sh` (the commit runs it).
- Anything odd outside this cell: append ONE surprise row (dell1 id form `MDPF_SECHIST-D1-W<n>-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) to `INVESTIGATION_v1.md` and keep working.
- Client-data bounds (0.0.0_AB_MSTR~DELL1, standing): never read, search, copy or `git show` any `org/**/W73_S*_EVIDENCE.json`, commits
  1ba8eafcda / f5645bb6e9, the ADVI_COTBKF ~74 / ~66 / ~70 cottonwood manifests, the IRPT_DASHBD tie-out files, or anything under
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/`. Search only inside the paths named here.

<paths>
data/etfs/scripts/gold/etf_positioning_gold.py
data/etfs/scripts/gold/etf_positioning_publisher.py
data/etfs/scripts/gold/test_etf_positioning_closed_market_frontier.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~23/MDPF_SECHIST.TO-SH-t24.closed-market-frontier.proof_of_spec.json
org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R6.md</decomp_doc> (round 6), cell `SH-t-24`.
<owned_cells>SH-t-24</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH6-t24-AC1, SH6-t24-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~23/MDPF_SECHIST.TO-SH-t24.closed-market-frontier.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH6-t24-AC1 SH6-t24-AC2`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is added or moved; the deploy is a separate act.
comp-iam: DECLARED-NOT-APPLICABLE the cell makes no new boto3 call (frontier_returns is pure over `hist` and `gap_record`).
comp-adversary: RUN -- AC2 dry-ran at the base 2026-10-14 ~14:0xZ: FAIL as expected (function missing); against a scratch reference of the interface it printed CM-REAL-OK, 339 session-day pairs equal, MOVED = KCDMY and UNVGY (2026-10-08) and SALXX (2026-10-09) at book as_of 2026-10-12; BLIND: whether the live Lambda package or the characteristics producer (which vendors an older gold script, row MDPF_SECHIST-D1-S6) computes the same windows, and the portal adapter's allowlist.
risk: SERVED (the code moves served returns once deployed; nothing is deployed by this cell).
</preflight>

Source: CTO round-5 analysis ADDENDUM 2 (@d3206f14a8, msg 5564) on CRO research 5563. The never-widen pair for the deploy names the served keys whose windows move: the books as_of a closed-market day for some holding; the AC2 MOVED line is the measured set.
