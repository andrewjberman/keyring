# AMGT_CORPUS task order -- `CRPS-y-1` -- ROUND 23: unit families for every unfamilied mnemonic (the census, not a list)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-y-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (the map commit and re-derive are the issuer's act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 raw reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 23. Serves **every served figure's unit** (42.5% of served figures carry
none today).

## 1. THE CELL -- `CRPS-y-1`

**Where this came from.** `integrations/bloomberg/research/build_unit_map.py` classifies each mnemonic's unit by FAMILY:
- `TEXT_FIELDS`, `PERCENT_FIELDS`, `ABSOLUTE_OR_MILLIONS_FIELDS`, `PER_SHARE_FIELDS`, `RATIO_FIELDS`,
  `SHARE_COUNT_ABSOLUTE_FIELDS` and `SHARE_COUNT_MILLIONS_FIELDS` (about lines 63-90);
- `classify_unit` (about line 146).

A mnemonic in no family is recorded `UNRESOLVED-ON-<sec>: mnemonic X is not in any known field family`. Over the newest served
model block of 100 keys, 16,052 of 37,746 figures carry no measured unit: 9,595 UNRESOLVED and 6,457 carrying the reader's
"SEE field_map.json ... not yet built" pointer. Rebuilding the map with today's builder leaves `no_family_after 14082`. The
mnemonics are the ones the producer (`model_block_pull.py`: `HEADER_FIELDS`, `HIST_FIELDS`, `FORECAST_FIELDS`) pulls but no
family names: BS_CASH_NEAR_CASH_ITEM, IS_ADJUSTED_OPERATING_INCOME, NET_INCOME, RETURN_ON_INV_CAPITAL,
RETURN_ON_TANGIBLE_ASSETS, BS_TOTAL_LIABILITIES, RETURN_ON_CAP, EQY_DPS, and more.

**RULED -- what you build:**
1. **Find the unfamilied set by CENSUS, never by a typed list.** Take `ALL_MNEMONICS` minus the union of the families. Put each
   one into the family whose definition fits it: money amounts, percents, ratios, per-share amounts, text. Use the field's basis
   text (`FIELD_BASIS` / the producer's basis) as the ground for each placement, and name that ground in a code comment. A
   mnemonic you cannot place stays out and stays UNRESOLVED; list it in your report.
2. **`EQY_FUND_CRNCY`** (a currency code, e.g. 'USD') is TEXT.
3. **Per-share at a large-number currency:** `IS_DIV_PER_SHR`, `REVENUE_PER_SH` and `BOOK_VAL_PER_SH` are per-share already, but
   fail the `0 < |v| < 2000` magnitude band at JPY scale. Decide them by a CROSS-FIELD read: the value against `PX_LAST` in the
   same currency (the header's `CRNCY` equal to `EQY_FUND_CRNCY`), with a stated plausible band. Never widen the magnitude band.
   A currency mismatch, or no `PX_LAST`, stays UNRESOLVED.
4. A figure the families cannot decide stays UNRESOLVED with its reason. Never guess.
5. `integrations/bloomberg/research/tests/test_build_unit_map_families.py` (new):
   - the census covers every mnemonic the producer pulls (the unfamilied set is empty, or each remainder is named as
     undecidable);
   - `EQY_FUND_CRNCY` classifies as TEXT;
   - a JPY-scale per-share value with a same-currency `PX_LAST` resolves;
   - a currency mismatch stays UNRESOLVED.
6. Do NOT write the committed `field_map.json` and do NOT touch `model_block_pull.py`, `unit_anchor.py`, or the discriminator's
   currency branch. The anchor hookup is the issuer's at the merge.

## 3. SURFACES

<paths>
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_build_unit_map_families.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-y-1.unit-families.md
</paths>

READ-ONLY: every other file (`field_map.json` NEVER written; `model_block_pull.py` read-only), every S3 object. Scratch `.scratch/y1/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`); `data/`, `portal/` and the rest of
`infra/` are absent by design. If you need a path outside the cone, file a row and stop that criterion; never disable the sparse
checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible (no `newline=` on a `Path` text call).
- NO vendor call, NO S3 write, NO write to the committed `field_map.json`.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-y-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round23/y1_AC1.sh</invocation><expect>(?m)^y1 blocks \d+ before unresolved \d+ pointer_before \d+ no_family_before \d+ after unresolved \d+ pointer_after \d+ no_family_after 0 crncy_after 0 per_share_after \d+$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-y-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round23/y1_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the census over the same 100 served blocks, before (as served) and after (your builder into a temp map over the crosswalk
  population, about 70 s). After: 0 no-family figures and 0 UNRESOLVED `EQY_FUND_CRNCY`. The total and the per-share remainder
  are printed and reported, not demanded: an undecidable figure stays UNRESOLVED.
- AC2: your tests with the builder's suites.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-y-1.unit-families.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE: each AC line, the families each newly placed mnemonic joined (with its ground), any mnemonic left out, and the
   per-share band you set.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-22 analysis ruling 2 @`a940eb6813`. Dry-run at base CLOUD `afad83a02f` (worktree `C:/tmp/coox-crps23-issue`):
- y1_AC1 FAIL as expected: `y1 blocks 100 before unresolved 9595 pointer_before 6457 no_family_before 9176 after unresolved 14553
  pointer_after 0 no_family_after 14082 crncy_after 96 per_share_after 276` (68 s).
- y1_AC2 FAIL as expected (no tests ran).
<risk>LOCAL</risk>
<status>pending</status>
<round>23</round>
<slot>~1</slot>
<fabric>site-z</fabric>
