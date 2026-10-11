# TO ADVI_COTBKF.TO-CB-ax-2.cot-gold-redeploy -- round 50 CB-ax-2: redeploy cot B_00, the writer and the files beside them under ONE pair

<to_id>ADVI_COTBKF.TO-CB-ax-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~CB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>50</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ax-2` (`decompositions/ADVI_COTBKF_DECOMP.round50.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-ax-1, both pair halves

---

## WORKER FACE

### THE CELL

Round 50's `CB-ax-1` makes the cot gold scripts `data/cot/scripts/gold/B_00.canonical_holdings.py` and
`data/cot/scripts/gold/build_canonical_prices_v2.py` run with no `opal_naming`. Both read their own firm from the `scopes.json` beside
them and fail closed. The writer's `ticker_overrides` also fails closed, and its S3 keys are plain legacy constants.

The cot gold run syncs only `s3://opal-data-cot/code/gold/`. The mirror today:

| key | state |
|---|---|
| `scopes.json` | present (round 42) |
| `lib/ticker_overrides.py` | present (old import path) |
| `ticker_overrides.py` | ABSENT |
| `build_canonical_prices_v2.py` | VersionId `GAOI7tOR...` |
| `B_00.canonical_holdings.py` | VersionId `hU7ZrZTD...` |

**Your item. Do not start until this order's AMENDMENT names both pair halves and CB-ax-1's drain.**

1. **Pair first.** The COO half by `2.0.0_SA_COO~C2` and the CTO half by `1.0.0_SA_CTO~DELL2`. The write set is the UNION of every
   tool's printed key list (ADDENDUM 18):
   - `code/gold/ticker_overrides.py` (MINTS, the repo blob);
   - `code/gold/scopes.json` (only if its blob changed since round 42);
   - `code/gold/build_canonical_prices_v2.py`;
   - `code/gold/B_00.canonical_holdings.py`.
   Each names its prior VersionId (or `none`), its new sha256, and its rollback. A deployed script rolls back by `copy-object` of its
   prior version. A minted file is never deleted by the seat: deletes are Andrew's act.
2. **Order:** the beside-module files FIRST (`ticker_overrides.py`, and `scopes.json` if needed), then the writer, then B_00. Re-read
   each key's version just before its write.
3. **A condition infeasible as worded means STOP and ask** (ADDENDUM 18). Do not proceed on your own reading.
4. **Proof on the SERVED files.** Fetch all written keys, confirm each sha256, and place them in a detached scratch worktree with NO
   `lib/` on the path. Run CB-ax-1's `data/cot/scripts/gold/tests/test_cot_gold_failclosed.py` there:
   - a synthetic rps day with no ImportError;
   - the scopes-absent STOP with 0 rows;
   - the overrides-absent STOP with 0 rows;
   - 757 overrides loaded.
5. **Close the ledger** with every key's prior and new VersionId and sha256.

**AMENDMENT 1 (issuer, 2026-10-09 ~16:2xZ; CTO ADDENDUM 23, msg 3667) -- the proof adds an IMPORT-CLOSURE read. Still held on CB-ax-1 and
both halves.**

After the write, read the full import closure of the SERVED `B_00.canonical_holdings.py` and `build_canonical_prices_v2.py`:
- every `import` / `from ... import` at module level AND inside functions (`ast`), plus the stdlib and installed-package split;
- check every non-stdlib, non-installed module against what `s3://opal-data-cot/code/gold/` actually carries (list it, paginated,
  denominator printed).
A module the mirror lacks means STOP (restore the scripts by `copy-object` of their prior versions) and file a row. Print
`IMPORT-CLOSURE b00_modules=<n> writer_modules=<m> missing=0`. The CVO corrected its round-41 grade, which checked bytes but not
imports. This read is the guard against that class.

**AMENDMENT 2 (issuer, 2026-10-09 ~16:4xZ; CTO ADDENDUM 22.1).** The union list gains `code/gold/legacy_addresses.json` (MINTS, the repo
blob of `infra/logic/registry/legacy_addresses.json`). It is uploaded with the other beside-module files, BEFORE the writer.
- **The pair** is ONE pair covering B_00 (@7b85e1a074), the writer, `ticker_overrides.py`, `legacy_addresses.json` and `scopes.json`
  if changed.
- **The import-closure read** (AMENDMENT 1) is included.
- **The served written-key census** is read against the pre-change writer. A new key class means STOP.

**AMENDMENT 3 (issuer, 2026-10-09 ~17:3xZ) -- RELEASED. Both halves are GIVEN.**

- **The pair:**
  - COO half `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R50_COT_GOLD_REDEPLOY_COO_HALF.md` @ea3b5ad9f8
    (blob 2186cd1adc);
  - CTO half `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R50_COT_GOLD_REDEPLOY_CTO_HALF.md` @fe56ae564e
    (conditions 1-4).
- **The act, in order. Open the ledger first** (`org/critical_paths/change_management/` + `.open_deploys/`), and commit it right after
  `open` and after each leg.
  1. Re-read: `code/gold/ticker_overrides.py` and `code/gold/legacy_addresses.json` are 404, and the writer's and B_00's VersionIds are
     `GAOI7tORcF7V7F0fW9NMH35bonjXEwzj` and `hU7ZrZTD5NDlVvuSo9aBMUd1hKUg_lAe`. A miss means STOP.
  2. `put-object` of the exact repo-blob bytes, `ticker_overrides.py` first, then `legacy_addresses.json`. Read back each sha256:
     `4d407c3a...` and `34dfcb37...` (full values in the COO half).
  3. `.tools/safe-deploy.sh` the writer, then B_00. Read back their sha256: `8b733bb1...` and `2b38b142...`.
  4. Proof on the FETCHED served files (CTO condition 2): the fail-closed test (`CB50ax2-AC1`), a synthetic rps day, the written-key census
     equal to the pre-change writer's, and the line `IMPORT-CLOSURE b00_modules=<n> writer_modules=<m> missing=0`.
- **Any infeasible condition as worded means STOP and ask the issuer** (ADDENDUM 18).
- **Rollback:** `copy-object` of the two prior VersionIds. The minted files stay; deleting them is Andrew's act.
- **No client account id in any ledger line or report** (containment ruling item 6).

### ACCEPTANCE

<criterion id="CB50ax2-AC1" cell_refs="CB-ax-2"><invocation>python -m pytest data/cot/scripts/gold/tests/test_cot_gold_failclosed.py -q</invocation><expect>passed</expect></criterion>
`CB50ax2-AC1` -- the fail-closed proof passes on the bytes whose sha256 the served keys were read back to equal. The ledger records
the read-backs beside this run.

<expected_criteria>CB50ax2-AC1</expected_criteria>

## BOUNDS

- **Grant.** Exactly the keys in the pair's union list, the ledger files, and this order's file. No delete of any key.
- **Pair first.** No write before both halves exist and this order's amendment cites them.
- **Refusal clause.** If a key's version moved, or a read-back differs, or a written key falls outside the list, stop. Restore any
  overwritten script by `copy-object`; leave minted files in place for Andrew. Write the reason in the ledger, and file a NEW surprise
  row (id `ADVI_COTBKF-D2-WCB2-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your repo WRITE grant. The S3 grant is the pair's union key list.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round50.md</decomp_doc> (round 50), cell `CB-ax-2`.
<owned_cells>CB-ax-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB50ax2-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-ax-2.cot-gold-redeploy.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB50ax2-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the pair files; the union key list; the prior and new VersionIds; the read-back sha256 values; the pytest line on the
served bytes; the ledger entry.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- 4 keys read by the cot gold run's code sync (gold_dispatch.sh:497-498); the writer runs only on a manual silver-prep and B_00's _ff_worker only when rps holds data (0 keys today), so no scheduled output changes from this deploy; BLIND: none beyond the union list.
comp-iam: RUN at apply time -- the dell2 identity's PutObject on the listed code/gold keys; BLIND: none beyond them.
comp-adversary: RUN -- pair before write; beside-module files first; version re-reads; sha256 read-backs; proof on the served bytes with no lib/; infeasible condition = STOP and ask; BLIND: a manual silver-prep mid-deploy (the ledger notes the window).
lane: SERVED write by the box applier via safe-deploy.sh plus put-object for the pinned files.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDA 18, 21 and 22 (msgs 3536, 3597, 3620); rows D2-S71, D2-S72.
