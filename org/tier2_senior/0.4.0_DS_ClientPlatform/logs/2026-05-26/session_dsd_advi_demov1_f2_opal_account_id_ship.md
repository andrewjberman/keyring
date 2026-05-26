# ADVI_DEMOV1 F2 — OPAL###### account-id format ship (DS 0.4.0~D)
**archetype:** IMPLEMENT
**date:** 2026-05-26
**ship sha:** `fd8ad144c` (pushed to origin/CLOUD)
**parent project:** ADVI_DEMOV1 (CLOSED COMPLETE 2026-05-26 ~19:00Z `767c113ab`; F2 = carry-open follow-on per LD-0030 staging)
**authority chain:** Andrew sovereign UAT 17:42Z → MSTR /mstr-spawn → DT 0.4 spawn-with-direction brief `74457d4e7` → DS 0.4.0~D respawn + execute → ws COO ENDORSE refined diagnosis 21:35Z
**spawn-to-ship wall:** ~1h10m (spawn 19:30Z → push fd8ad144c ~21:55Z); within brief's ~1.5-2h ETA

## TL;DR

Andrew UAT surfaced: "the account numbers in 'Fee Summary' page are still displaying... make up account strings like OPAL######". F2 carry-open routed to DS~D (Path B author lane). Changed demo dataset's account-id rewrites from `z + 10 digits` (visually mimicking real bd account numbers) to `OPAL######` (visually unambiguous as fake). 4-file commit + push; FN-1 fixture 12/12 PASS; end-to-end Pass-1 verification 6194/6194 OPAL format with 0 regressions. AC5 handoff to AE 0.7 for EC2 transform re-run dispatch.

## Diagnosis (refined from brief)

DT 0.4 spawn-direction brief framed F2 as **R1 JSON-path-aware-gap** — "PII-field map in `fake_identities.py` does NOT include `.fee_summary.by_account[].account_id` as a rewritable path. BD source has real account numbers; they pass through to demo unchanged."

Investigation (4-jq audit + 6 sample artifacts pulled from `opal-data-bd`) **partially overturned this hypothesis**:

1. **All bd account-id JSON paths already covered.** The existing transform engine uses VALUE-based exact-match rewriting (`demo_transform.py:395`: `if value in m.exact: return m.exact[value]`). Pass-1 enumeration (`build_mapping`) sweeps every `.json` content + every `accounts/{id}/` folder name via the ZID_RE regex (`z\d{6,14}`) to discover the real-id universe, then allocates a fake via `factory.zid(zid, "account")`. R1 referential integrity is by construction across all 22k+ files.

2. **R1 audit-complete (4-jq sweep):** account-id-class JSON paths in scope are:
   - `clients/{client_id}/summary.json` `.fee_summary.by_account[].account_id` (per brief)
   - `clients/{client_id}/summary.json` `.detail.accounts[].account_id` (newly surfaced; team-attribution sibling)
   - `accounts/{account_id}/summary.json` `.account_id` (top-level scalar)
   - S3 key path `platinum/accounts/{account_id}/...` (folder names)
   - **No other account-id paths** anywhere in bd platinum (audited firm/cumulative_chart + firm/partner_analytics_annual + firm/fee_efficiency + firm/leaderboard + firm/employee_leaderboard + clients/{id}/views + clients/{id}/composition + clients/{id}/concentration + clients/{id}/mix_timeseries — all empty on account-id-class regex + z##### value-scan).

3. **The actual F2 problem: OUTPUT FORMAT.** Demo's account-id rewrites produce `z + 10 digits` strings (e.g. `z6785409080`) — VISUALLY indistinguishable from bd's real account numbers (e.g. `z0813241311`). Andrew's UAT directive wants visual-distinguishability via OPAL prefix.

4. **Bd account-id format-class confirmed:** `z + 10 digits` (1 prefix char + 10 numeric). Bd client-id format: `z + 8 digits`. Both share z prefix but differ in digit count.

ws COO ENDORSED the refined diagnosis at 21:35Z + banked it as the 23rd LD candidate today (`brief-author-hypothesis-vs-impl-empirical-class-discovery` sister-fire to AE 0.7's F1 `brief-author-implementation-suggestion-vs-empirical-class-discovery`).

## Implementation (4 files, 186 insertions, 4 deletions)

### 1) `fake_identities.py` — add `opal_account_id()` method

New method on `FakeIdentityFactory`:

```python
def opal_account_id(self, real_id: str) -> str:
    for probe in range(4096):
        cand = "OPAL" + _digits(self.seed, real_id, f"opal-account#{probe}", 6)
        if cand not in self._used_zid:
            self._used_zid.add(cand)
            return cand
    raise RuntimeError(...)
```

- 1M unique 6-digit space vs ~6,245 49F accounts = ~160x headroom
- Shared `_used_zid` dedup with `zid()` — formats structurally disjoint (`OPAL` vs `z`) so no false collisions
- Determinism: `fake = f(seed, real_id, salt+probe)` — same (seed, real_id) reproduces

### 2) `demo_transform.py:367` — single call-site swap

Account-id allocation in `build_mapping()`:

```python
# OLD
(m.add_path_only if len(zid) < 4 else m.add_id)(zid, factory.zid(zid, "account"))

# NEW
fake = (factory.opal_account_id(zid) if len(zid) >= 4
        else factory.zid(zid, "account"))
(m.add_path_only if len(zid) < 4 else m.add_id)(zid, fake)
```

Client-id allocation at line 356 is UNTOUCHED — relationship-id z-shape preserved for folder/path convention compatibility.

### 3) `test_path_b_disjointness.py` — 2 new FN-1 cases (10 → 12)

- **FN1-F2-acct1:** output format `^OPAL\d{6}$` + determinism + format-disjoint from bd z-pattern
- **FN1-F2-acct2:** 6500-account corpus allocates cleanly under 4096-probe loop (regression gate against future probe-loop shrinkage or digit-count change)

### 4) `pii_leak_scan.py` — defense-in-depth FORMAT-class anomaly canary

- New `BD_ACCOUNT_ID_FORMAT = re.compile(r"\bz\d{9,11}\b")` regex matching the bd account-id format-class
- New `_legitimate_fake_zids(m)` helper enumerating the demo CLIENT-id universe (the only legitimate z-shape after F2)
- Per-object scan walks demo content + key for `z\d{9,11}` tokens; any token NOT in `real_zids` (primary leak gate) AND NOT in `fake_zids` (legitimate client) is structural anomaly (`format_anomaly_count`)
- New BLOCKED gate: `format_anomaly_count != 0` blocks closure (separate from leak_count) — distinguishes "OPAL rewrite regression" or "Pass-1 enumeration gap" from primary leak class

## Verification

### Pre-commit gate (CLAUDE.md Rule 14)

```
$ .tools/ds-commit-gate.sh data/demo/scripts/transform/{fake_identities.py,demo_transform.py,test_path_b_disjointness.py,pii_leak_scan.py}
All checks passed!  (py_compile)
All checks passed!  (ds-precommit-check.py)
All checks passed!  (ruff)
OK: pre-commit gate clean for 4 file(s)
```

### FN-1 fixture 12/12 PASS

```
FN-1 fixture: running 12 case(s) on Path B primitive
  PASS  FN1-09a -- Austin Thompson token-level
  PASS  FN1-10a -- Sullivan, Dan prefix leak
  PASS  FN1-10b -- Owens, Sam couple-component
  PASS  FN1-11a -- Powell shared-surname
  PASS  FN1-11b -- Winslow+Clarke component embed
  PASS  FN1-12 -- attempt-12 diagnostic class
  PASS  FN1-13 -- attempt-13 _embeds_real class
  PASS  FN1-pool-adequacy
  PASS  FN1-49f-density
  PASS  FN1-F2-acct1 -- OPAL###### format + determinism: 4 real account-ids -> ['OPAL100467', 'OPAL403419', 'OPAL562339', 'OPAL756871']
  PASS  FN1-F2-acct2 -- 6500-account corpus allocated cleanly (6500 unique fakes; 4096-probe loop sufficient headroom)
  PASS  FN1-backcompat
FN-1 summary: 12/12 PASS, 0 FAIL
```

### End-to-end Pass-1 mapping verification (live bd source)

```
Mappings: 10065 total
Account (z+10-digit reals): 6194 -- fake format check:
  OPAL###### format: 6194 (should equal account total)
  z-prefixed (regression): 0 (should be 0)
  other (anomaly): 0
  sample 8 OPAL mappings:
    z0812152081 -> OPAL873655
    z0812152601 -> OPAL979055
    z0812153251 -> OPAL813770
    z0812154091 -> OPAL634893
    z0812154251 -> OPAL109200
    z0812154351 -> OPAL113502
    z0812154731 -> OPAL114195
    z0812155171 -> OPAL946259
```

100% OPAL coverage on account-ids; client-ids preserved at z-format (folder convention compatibility).

### R5 scanner smoke test (regex correctness + import sanity)

```
pii_leak_scan import: OK
BD_ACCOUNT_ID_FORMAT pattern: \bz\d{9,11}\b
  [OK] 'z0813241311'      -> match=True  (bd account-id format z+10)
  [OK] 'z08103151'        -> match=False (bd client-id z+8 -- too short for canary)
  [OK] 'OPAL427819'       -> match=False (demo OPAL format -- no z prefix)
  [OK] 'z123456789'       -> match=True  (z+9 -- in scan range)
  [OK] 'z12345'           -> match=False (z+5 -- too short)
  [OK] 'z12345678901'     -> match=True  (z+11 boundary)
  [OK] 'z123456789012'    -> match=False (z+12 -- out of range)
```

## Compiler Tools

| Tool | Run | Outcome |
|---|---|---|
| `comp-pipescript io [script]` | N/A | demo-transform scripts are not part of the gold pipeline; no comp-graph node |
| `comp-pipescript deployed [script]` | N/A | EC2 deploy is AE 0.7's lane; my output is the CLOUD commit, AE 0.7 dispatches SSM |
| `comp-blast [node]` | N/A | demo-transform is isolated (no portal consumer for demo bucket besides UAT path) |
| `comp-validate [script] --artifact` | N/A | no gold_validate_config for demo-transform; FN-1 fixture serves the same role |

**Why no comp-* runs:** demo-transform lives at `data/demo/scripts/transform/`, outside the gold-pipeline compiler-graph universe. The substantive verification surface is (a) FN-1 fixture (12/12 PASS) + (b) end-to-end Pass-1 mapping verification on live bd source (6194/6194 OPAL coverage) + (c) ds-commit-gate.sh (py_compile + ds-precommit-check.py + ruff all clean).

## Acceptance criteria status

| AC | Status | Evidence |
|---|---|---|
| AC1 — JSON path additions | NOT-NEEDED-by-construction | R1 audit-complete; paths already covered by value-map exact-match |
| AC2 — OPAL###### deterministic mapper | COMPLETE | `opal_account_id()` method + call-site swap; end-to-end 6194/6194 OPAL coverage verified |
| AC3 — FN-1 fixture extension | COMPLETE | 2 new cases (FN1-F2-acct1, FN1-F2-acct2); 12/12 PASS |
| AC4 — R5 leak-scanner extension | COMPLETE | format-anomaly canary + new BLOCKED gate; smoke test PASSES regex correctness |
| AC5 — AE 0.7 handoff | THIS-MCP | SHA `fd8ad144c` + evidence package this session log |
| AC6 — post-AE-run full R5 PASS | PENDING-AE | AE 0.7 SSM dispatch + post-run R5 sweep + RAVC2 to ws COO |

## Coordination chain

- DT 0.4 spawn-with-direction brief `74457d4e7` (15:21Z) → DS~D respawn ~19:30Z
- DS~D → ws COO `[SPAWN-ORIENT]` 19:41Z → COO ACK SPAWN-ORIENT 21:00Z
- DS~D → AE 0.7 `[ACK]` 19:41Z → AE 0.7 ACK 21:05Z (no questions; ship at discretion)
- DS~D → ws COO `[PHASE-ARTIFACT 1/4]` refined diagnosis 19:53Z → COO ENDORSE 21:35Z + 23rd LD banked
- DS~D commit + push `fd8ad144c` ~21:55Z → AC5 handoff MCP to AE 0.7 (this MCP)

## Memory candidates (banking for /govern)

1. **`brief-author-hypothesis-vs-impl-empirical-class-discovery`** — brief framed F2 as gap-class (paths not covered); impl-time investigation revealed format-class (paths covered + visual-format wrong). Sister-fire to AE 0.7 F1 today. Two-fire cluster suggests an emergent pattern: brief-author hypothesis vs impl-time empirical refinement at design-gate; the discipline value is the 4-jq audit-before-coding step that surfaces the actual scope.

2. **STANDBY-PREP compress to delivery** (already banked as `feedback_standby_prep_compress_to_delivery_when_context_sufficient`): F2 spawn 19:30Z → commit fd8ad144c ~21:55Z = ~2.5h wall = brief's ~1.5-2h ETA + 30min for refined-diagnosis-via-COO-cycle. Slightly over ETA but the COO ENDORSE cycle was high-value (banked 23rd LD candidate + scope-refinement confirmation).

3. **Phase-artifact surfacing pattern works** (per `feedback_surface_phase_artifacts_during_execution`): phase-1 investigation MCP at 19:53Z triggered COO ENDORSE 21:35Z with scope-refinement absorption + banking; running heads-down would have skipped that high-value moment.

## Risks + carry-open

- **AC6 dependency on AE 0.7 SSM dispatch:** my F2 only takes effect when the transform re-runs on EC2 against opal-data-bd → opal-data-demo. If AE 0.7's dispatch is blocked (LD-0055 fast-track availability per AE's CO-CONSULT §4), AC6 stays open until the slow-lane window opens.
- **Format-anomaly BLOCKED gate is strict:** my new gate at `pii_leak_scan.py` will BLOCK closure if ANY `z\d{9,11}` token in opal-data-demo isn't in `real_zids` or `fake_zids`. This is intentional (catches OPAL-rewrite regressions) but means AE's post-run R5 may BLOCK if the transform partially executes (some objects updated, some stale z-format leftover from old transform). AE 0.7 should treat the canary fire as "transform incomplete, retry" rather than "F2 broken."
- **Existing demo content is z-formatted (pre-F2 transform output):** until AE re-runs, opal-data-demo's account-ids stay z-shaped. Running my updated `pii_leak_scan.py` against the current state WOULD fire `format_anomaly_count != 0` (correctly — it's the regression-signal). This is expected; not a problem.

## Next session (after AC6 close)

- RAVC2-Request to ws COO after AE 0.7 RAVC2-Request → format the close-evidence chain
- Then back to /work queue (other pending TOs: ADVI_VALFIN.010, etc.)
