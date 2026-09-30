# Apply reads -- ledger irpt-holdings-contract-category-20260929, leg D1

Operator `2.0.0_SA_COO~P`, 2026-09-29. Packet blob 9f638d70; CTO half 102755 (condition amended by 102761, then replaced by
102767); CRO half 102759 (+ addendum 1, 102770). Check:
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r21/holdings_contract_three_firm_validate.py`.
It assembles each firm's served snapshot with the served `publication.HoldingsPublication.capture` (all accounts,
read-only) and validates it with Draft 2020-12 under the packaged copy.

## 1. BEFORE (11:50Z) -- under the live copies and the two signed artifacts

```
49financial revision 9ab377cef9 date 2026-09-22 parts 184 nodes 151697 kinds {'ACCOUNT': 7522, 'CASH': 9081, 'MODEL_LEAF': 7475, 'SECURITY': 120097, 'SLEEVE': 7522}
  under irpt-holdings.live.zip (schema 6fea9322): INVALID, 127572 errors
  under irpt-ycharts-generate.live.zip (schema 9fc8e32d): VALID
  under irpt-holdings.new.zip (schema 3795c927): VALID
  under irpt-ycharts-generate.new.zip (schema 3795c927): VALID
cottonwood revision fc199c8ed6 date 2026-09-22 parts 26 nodes 16749 kinds {'ACCOUNT': 841, 'MODEL_LEAF': 521, 'MODEL_WRAPPER': 462, 'SECURITY': 14426, 'SLEEVE': 499}
  under irpt-holdings.live.zip (schema 6fea9322): INVALID, 14947 errors
  under irpt-ycharts-generate.live.zip (schema 9fc8e32d): VALID
  under irpt-holdings.new.zip (schema 3795c927): VALID
  under irpt-ycharts-generate.new.zip (schema 3795c927): VALID
inflection revision ba9001d5ba date 2026-09-22 parts 43 nodes 33328 kinds {'ACCOUNT': 876, 'MODEL_LEAF': 624, 'SECURITY': 30881, 'SLEEVE': 947}
  under irpt-holdings.live.zip (schema 6fea9322): INVALID, 31505 errors
  under irpt-ycharts-generate.live.zip (schema 9fc8e32d): VALID
  under irpt-holdings.new.zip (schema 3795c927): VALID
  under irpt-ycharts-generate.new.zip (schema 3795c927): VALID
ALL FIRMS VALID UNDER irpt-ycharts-generate.new.zip: True
```

## 2. Apply

| step | irpt-holdings | irpt-ycharts-generate |
|---|---|---|
| S3 latest at apply (CRO condition 2) | `vN9FiyknGePr9_jjYB3r0rr7cbG11awK` (12:01Z) | `GP__8T1nIcOMpzQVh1saTMdBiYJQ5ovR` (12:01Z, re-read 12:07Z) |
| fresh plan | 0/1/0: s3_object_version ZbLWvaO1 -> vN9Fiykn, source_code_hash kZygK57y -> U4/P5Bh3 | 0/1/0: BIEsyaNn -> GP__8T1n, AdE17rT6 -> wnt7hjAB |
| safe-apply (halt gate: 28 routine messages, 0 STOP; HALT_ACK=1) | 12:05:32Z, 1 changed | 12:07:40Z, 1 changed |
| CodeSha256 read back | `U4/P5Bh3...` Successful, 12:06:54Z | `wnt7hjAB...` Successful, 12:09:06Z |
| deployed zip (get-function) vs signed artifact | 33 members equal; vs previous live only `contracts/HoldingsSnapshot.schema.json` | 111 members equal; the same one member |
| re-plan | No changes | No changes |

Rollback keys: irpt-holdings -> S3 version `ZbLWvaO1rvO2E9Q8Xv_ieUkS1XsFwRLn` (`kZygK57y`); irpt-ycharts-generate ->
`BIEsyaNnhqvviJymsOOJfc73Oyh5xgp0` (`AdE17rT6`).

## 3. Deployed invokes (CTO 102767 (b)), 12:12Z

| invoke | answer | log tail |
|---|---|---|
| irpt-holdings, API-shaped GET holdings, no identity | 200, refusal envelope `CONTRACT_VERSION`, no FunctionError | Init Duration 159.61 ms (fresh container); 0 error lines |
| irpt-ycharts-generate, API-shaped POST analysis `{"input_id": ...}`, no identity | 200, refusal envelope `CONTRACT_VERSION`, no FunctionError | Init Duration 187.44 ms; 0 error lines |
| irpt-ycharts-generate, `{"irpt_import_census": true}` | 59 modules, 0 failed | 0 error lines |

- The generate POST is the container's FIRST served call. `served.installed_entry` builds the Entry there,
  `build_boundary(compose_ports())`, before any routing. That build computes `ingestion_revision_for` over the 22
  packaged schemas, the new copy included. A returned envelope, not an `EntryError`, means that loader ran on the
  deployed bytes.
- The admission Registry is built only at a prospect submit that passes the verified-edge identity and the input-owner
  guard. A direct invoke cannot carry that identity without forging the edge headers, which this seat does not do.
  Offline, on the DEPLOYED bytes: `CompositionAdmission(contracts)` builds over 22 schemas with revision
  `schemas-4780eaf85be2...`. On the previous live bytes it also builds, with revision `schemas-7ad1289e34dc...`.
  The first real signed-in Analysis submit reaches it served.
- The ingestion revision moves from `schemas-7ad1289e34dc...` to `schemas-4780eaf85be2...`. Requests accepted from 12:09Z
  record the new string. Retained requests are unaffected, because `owned_requests.py:92-93` checks only for a
  non-empty string. See `HOLDINGS_CONTRACT_GENERATE_READER_TRACE_20260929.md` @1c9519d4a6.

## 4. AFTER (12:13Z) -- under the deployed copies

```
49financial revision 9ab377cef9 date 2026-09-22 parts 184 nodes 151697 kinds {'ACCOUNT': 7522, 'CASH': 9081, 'MODEL_LEAF': 7475, 'SECURITY': 120097, 'SLEEVE': 7522}
  under irpt-holdings.deployed.zip (schema 3795c927): VALID
  under irpt-ycharts-generate.deployed.zip (schema 3795c927): VALID
cottonwood revision fc199c8ed6 date 2026-09-22 parts 26 nodes 16749 kinds {'ACCOUNT': 841, 'MODEL_LEAF': 521, 'MODEL_WRAPPER': 462, 'SECURITY': 14426, 'SLEEVE': 499}
  under irpt-holdings.deployed.zip (schema 3795c927): VALID
  under irpt-ycharts-generate.deployed.zip (schema 3795c927): VALID
inflection revision ba9001d5ba date 2026-09-22 parts 43 nodes 33328 kinds {'ACCOUNT': 876, 'MODEL_LEAF': 624, 'SECURITY': 30881, 'SLEEVE': 947}
  under irpt-holdings.deployed.zip (schema 3795c927): VALID
  under irpt-ycharts-generate.deployed.zip (schema 3795c927): VALID
ALL FIRMS VALID UNDER irpt-ycharts-generate.deployed.zip: True
```

## 5. Open

The Holdings card read through the page on one firm (CRO half condition 1) is asked of `4.0.0_SA_CRO`'s signed-in walk.
D1 closes on that read.
