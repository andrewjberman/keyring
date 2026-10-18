# AMGT_HARVST round 92 -- design note for HVST-cf-3 / HVST-cf-5 (issuer, 2026-10-18 ~00:4xZ)

**Status: NOT an order.** `HVST-cf-3` is cut when `HVST-cg-2` (the silver rewrite) closes, because its census needs real silver rows that carry `fund_relation`; the CTO's order is the same (round-91 analysis item 2: "cf-3 then cf-5, after item 1 lands"). This note holds what I read in `lib/research/corpus/fund_form.py` (working tree, `a9aecdd593`) so the cut is one step.

## What the code does today

- `gather_items(client)` (line 241) reads EVERY typed silver row (`store.silver_latest`, all 353 reports plus the 2 misfiled KMB reports, which `typed.MISFILED_REPORTS` drops only in `reports_for`, not here), fetches each row's extraction, and returns items `(report_id, row.get("fund"), report_class, headings, extract_key)` (line 262).
- `distinct_funds` / `build` / `_inputs_for_fund` / `absent_fund_reports` group by that `fund`, so a report that only NAMES a fund (a candidate, an initiation, a template) is counted in that fund's form. `write()` (line 289) writes one `research-fund-form` object per distinct fund, named by `sha256(method_version + sorted inputs)`.
- `read_latest` / `current_inputs` pick the stored object whose `inputs` equal the inputs recomputed NOW; `substrate._fund_form_member` (line 270 of `substrate.py`) picks by `inputs` AND `METHOD_VERSION`. **So the moment `gather_items` changes, every dossier build finds no stored fund form until `write()` has run** (the sequencing hazard of decomposition 121).

## The change `cf-3` makes (CTO round-91 item 2: holding reports only, no Mexico reports)

1. In `gather_items`: skip a row listed in `typed.MISFILED_REPORTS` (by `security_key` and `report_id`); the item's fund is `row["fund"]` only when `row["fund_relation"] == "holding"`, else `None`.
2. **Fail loud, not silent:** a kept row with no `fund_relation` key raises (a value must carry its claim; a silent count of zero would write empty forms). After `HVST-cg-2` every kept row has the key.
3. `METHOD_VERSION` `"1"` to `"2"` (the rule changed; the object name hashes the version, so no `v1` object is mistaken for a `v2` one by `substrate`).
4. `absent_fund_reports` keeps its meaning ("belongs to no form"); its printed count rises by the non-holding reports; its docstring says so.
5. Tests: offline arms for a candidate report excluded, a holding report counted, a misfiled report excluded, a row without the key raising, the version, and a mutant; the existing `tests/test_fund_form.py` fixtures gain `fund_relation: "holding"` and nothing else.
6. A read-only census after `HVST-cg-2`: per fund, reports before and after, the dropped non-holding reports, the 2 dropped misfiled; expected: the 14 `candidate`, 2 `initiate`, 2 `interest`, 1 `template` reports are dropped where their class is A/B/C/D, and the 2 Mexico class B reports.

## `cf-5` (the rebuild, SC1)

Under its own never-widen pair: `fund_form.write()` once, three funds (IDVZ, PFOE, DIVZ), three NEW objects (`method_version 2`), then ONE dossier-build probe on a holding name (UNH) and the control (CPA), served reads equal to before. The pair must say that between the code merge and this write no dossier build is run by anyone (no schedule runs it: `HVST-ce-1` section (g)), and that the code merges but is not deployed anywhere (lib code is run from a worktree by an ordered seat).

## Not decided here

Whether `substrate` should fall back to a `v1` form when no `v2` exists (no: the CTO wants builds to find nothing rather than a wrong form); the shared classifier of gold and silver (row `D1-S49`, round 93).

-- 2.0.0_SA_COO~W1
