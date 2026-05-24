# Session Log — ADVI_DEMOV1.004 Attempt-13 Monitoring

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-24
**Session start:** ~02:58 UTC (SSM dispatch)
**Session status at log-write:** IN PROGRESS (17:23 UTC; clients 14,432/14,812 = 97.4%)
**Task Order:** ADVI_DEMOV1.004 — EC2 one-shot transform + PII-leak scan
**References:** TO file `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_DEMOV1.004.dsc-run-and-verify-pii-leak-scan.md`; LD-0030 (Path B mechanism-class change charter); CVO verdict commit `293649cc0`

---

## Objective

Execute attempt-13 of the ADVI_DEMOV1.004 transform — the thirteenth full EC2 one-shot run of `demo_transform.py` on instance `i-03343a6072834f77d`, dispatched via SSM `AWS-RunShellScript` (command-id `ef7103fd-6776-432c-8732-f800563d28b5`). This attempt carries the `_embeds_real` guard fix (commit `dbf170b32`), which adds a structural disjointness check at fake-generation time: any fake candidate is rejected if any pre-seeded real name appears as a strict substring of the candidate.

---

## Context — Iteration History Leading to Attempt-13

| Attempt | Key Fix | Outcome |
|---------|---------|---------|
| 1–8 | Initial pool design, concurrency tuning, slug collision | Various HARD ERRORs |
| 9 | slug-collision root-cause fix (commit `87ae43cf8`) | `austin_thompson` substring leak in PII scan |
| 10 | couple-component guard + real-name pre-seed (`9e02fc35d`) | `sam_owens` couple-component leak |
| 11 | shared-surname couple c1 component check (`defcab3cb`) | Powell/Winslow/Clarke cohort leaks |
| 12 | HARD ERROR diagnostic — sorted leakers exposed (`c61d4da6e`) | Multiple new leak classes surfaced via diagnostic |
| 13 | `_embeds_real` guard — reject fakes embedding any real name as substring (`dbf170b32`) | **IN PROGRESS** |

CVO LD-0029 priority-consult (commit `293649cc0`) CORROBORATED Path B: structured-PII-tagging-at-build-time as the mechanism-class change. MSTR LD-0030 (`b58751842`) chartered ADVI_DEMOV1.006 to implement Path B post-attempt-13 settlement. ADVI_DEMOV1.006 is HELD pending this attempt's empirical result.

---

## Fix Implemented This Session — Commit `dbf170b32`

**File:** `data/demo/scripts/transform/fake_identities.py`

**Change:** Added `_real_names: set[str]` to `FakeIdentityFactory.__init__`; added `_embeds_real(cand)` method; applied the check in `advisor()`, `client_name()` (single branch), and `client_name()` (couple branches).

```python
def _embeds_real(self, cand: str) -> bool:
    """True if any pre-seeded real name is a strict substring of cand.
    An exact match (cand == real) is NOT considered an embed -- callers
    gate that separately via _used_person membership."""
    return any(r in cand for r in self._real_names if r and r != cand)
```

**Pre-condition:** `demo_transform.py` pre-seeds `factory._real_names` alongside `factory._used_person` for both advisor and client universes (established in `9e02fc35d`). Path B leverages this same data structurally.

**Architectural note:** This guard fires AT generation time (before the fake is returned). This is the architectural inversion vs post-hoc substring scan. It is NOT Path B (which is structured-index disjointness at build time) but is the strongest available guard within the current substring-scan mechanism class. Path B (DEMOV1.006) is the structural follow-on.

**Compiler Tools gate (pre-commit):**
```
.tools/ds-commit-gate.sh data/demo/scripts/transform/fake_identities.py data/demo/scripts/transform/demo_transform.py
```
- `python -m py_compile`: PASS
- AST undefined-name scan: PASS
- `ruff check --target-version py39`: PASS

---

## SSM Dispatch — Attempt-13

**Command ID:** `ef7103fd-6776-432c-8732-f800563d28b5`
**Instance:** `i-03343a6072834f77d`
**Dispatch time:** ~02:58 UTC 2026-05-24
**SSM timeout:** 86400s → expires 02:58 UTC 2026-05-25

**Script params (verbatim from `.runtmp/ssm_attempt13_params.json`):**
```
Phase A: aws s3 cp s3://opal-313476888478-lambda-artifacts/demov1/demo_transform.py /opt/demo/
          aws s3 cp s3://opal-313476888478-lambda-artifacts/demov1/pii_leak_scan.py /opt/demo/
          aws s3 cp s3://opal-313476888478-lambda-artifacts/demov1/fake_identities.py /opt/demo/

Phase B: python3 /opt/demo/demo_transform.py --apply --value-mode verbatim \
           --workers 64 --source-bucket opal-data-bd --target-bucket opal-data-demo

Phase C: python3 /opt/demo/pii_leak_scan.py --source-bucket opal-data-bd \
           --target-bucket opal-data-demo --seed advi-demov1-2026 --workers 64 \
           --report /tmp/pii_scan_result.json

Phase D: aws s3 cp /tmp/pii_scan_result.json \
           s3://opal-313476888478-lambda-artifacts/demov1/pii_leak_scan_result.json
```

**S3 scripts verified (Phase A — pre-run parity check):**
```
comp-pipescript deployed data/demo/scripts/transform/fake_identities.py
```
Result: MATCH (dbf170b32 committed → uploaded to S3 → EC2 pulls from S3 per Rule 12)

---

## Compiler Tools Mandate — Phase 1 (Before Run)

Per ADVI_DEMOV1.004 TO compiler_tools_mandate Phase 1:

**Run:** `comp-pii audit` (PII baseline before run)
**Observed:** Baseline noted; pseudonymized field coverage confirmed in platinum layer. No new cleartext PII fields added since last audit.
**vs Expect:** Orientation baseline — n/a fail condition. PASS.

**Run:** EC2 runner parity check (S3 scripts vs committed HEAD)
**Observed:** `dbf170b32` uploaded to `s3://opal-313476888478-lambda-artifacts/demov1/fake_identities.py` before dispatch. MATCH confirmed.
**vs Expect:** MATCH. PASS.

---

## Transform Monitoring — Attempt-13 Progress Log

All S3 timestamps are local Eastern time (UTC-4). UTC = local + 4h.

### Phase A — Script Download
Confirmed complete at session start. EC2 pulled scripts from S3 artifact bucket per Rule 12.

### Phase B — Transform Run (Pass 1 build_mapping + Pass 2 stream)

**Object scope:** 22,260 total platinum objects (accounts: 6,549 | advisors: ~884 | clients: 14,812 | firm: ~104 | demo: 1)

**Progress measurements:**

| UTC Time | Clients Written | Rate (obj/min) | Firm | Note |
|----------|----------------|----------------|------|------|
| 03:00 | 0 | — | 0 | Dispatch. Accounts rewriting (in-place overwrites) |
| 04:10 | 0 | — | 0 | Accounts complete (6,549). Advisors starting |
| 04:47 | 0 | — | 0 | Advisors in progress (~840 obj expected) |
| 05:22 | 0 | — | 0 | Accounts/advisors phase. Note: 884 advisor objects (vs 794 expected — extra file types from full run) |
| 06:02 | 0 | — | 0 | Advisors complete (884 obj). Clients starting |
| 06:25 | 293 | 11.0 | 0 | Clients phase active. Cold-start ramp |
| 06:27 | 326 | 16.5 | 0 | Rate stabilizing |
| 07:30 | 1,325 | 16.4 | 0 | Confirmed stable. SSM timeout risk CLEARED |
| 07:34 | 1,390 | 16.3 | 0 | — |
| 08:05 | 1,928 | 17.4 | 0 | Rate improving |
| 08:30 | 2,344 | 16.6 | 0 | — |
| 08:38 | 2,509 | 17.8 | 0 | — |
| 09:07 | 3,081 | 18.6 | 0 | — |
| 09:32 | 3,582 | 20.0 | 0 | — |
| 09:39 | 3,768 | 21.5 | 0 | — |
| 10:09 | 4,455 | 22.9 | 0 | — |
| 10:33 | 5,050 | 24.8 | 0 | — |
| 10:41 | 5,246 | 24.5 | 0 | — |
| 11:11 | 6,049 | 25.7 | 0 | Past 40% |
| 11:34 | 6,680 | 27.0 | 0 | — |
| 11:43 | 6,933 | 27.6 | 0 | — |
| 12:13 | 7,890 | 30.0 | 0 | PAST HALFWAY (53.3%) |
| 12:36 | 8,855 | 36.0 | 0 | — |
| 12:45 | 9,228 | 41.0 | 0 | Rate burst (small objects cluster) |
| 13:15 | 11,130 | 63.0 | 0 | Major acceleration — small object cluster |
| 13:38 | 11,762 | 27.5 | 0 | Rate normalized back (heavy objects) |
| 13:47 | 11,843 | ~10 | 0 | Spot-rate dip — dispatched process liveness check |
| 13:47 | — | — | 0 | **PID 33734 ALIVE: elapsed 10h47m, CPU 104%, RSS 1.08GB** |
| 14:16 | 12,207 | 11.9 | 0 | 62-min baseline: 32.7/min — healthy |
| 14:40 | 12,563 | 14.0 | 0 | — |
| 14:49 | 12,654 | 12.0 | 0 | — |
| 15:18 | 12,947 | 11.0 | 0 | — |
| 15:42 | 13,218 | 11.3 | 0 | — |
| 15:50 | 13,308 | 11.3 | 0 | — |
| 16:20 | 13,704 | 12.2 | 0 | — |
| 16:44 | 14,000 | 12.3 | 0 | — |
| 16:51 | 14,068 | 10.0 | 0 | 744 remaining |
| 17:23 | 14,432 | 11.4 | 0 | **380 remaining — final stretch** |

**Process liveness check (13:47 UTC):**
```
aws ssm send-command --document-name AWS-RunShellScript \
  --parameters '{"commands":["ps -o pid,etime,pcpu,pmem,rss,comm -p 33734"]}'
```
Output:
```
    PID     ELAPSED %CPU %MEM   RSS COMMAND
  33734    10:46:50  104 13.4 1080652 python3
```
Result: ALIVE. CPU 104%, RSS 1.08GB. PASS.

**Rate analysis:**
- Initial rate: ~16.4 obj/min (cold start, large concentration.json files)
- Peak rate: ~63 obj/min (small object cluster — views.json, composition.json)
- Sustained tail rate: ~10-14 obj/min (heavy concentration.json files ~1-1.4MB each)
- Rate variability is object-mix driven, not a process health issue. Confirmed by 10h47m liveness check.

**ETA at log-write (17:23 UTC):**
- Clients remaining: 380 at 11.4/min → done ~17:56 UTC
- Firm: ~104 objects → done ~18:02 UTC
- Phase C (PII scan): ~60min → done ~19:02 UTC
- SSM timeout: 02:58 UTC May 25 → **~7.9h margin**

### Phase C — PII Scan
**Status:** NOT YET STARTED (Phase B still running)
**Gate:** R5 — ZERO leaks required. Scan result will be uploaded to `s3://opal-313476888478-lambda-artifacts/demov1/pii_leak_scan_result.json`.
**Current S3 scan result:** `2026-05-23 12:05:03 188 bytes` — stale from previous attempt. Today's result overwrites on Phase D completion.

### Phase D — Upload Scan Result
**Status:** NOT YET STARTED

---

## Security Compliance (R4 / R7 / AC7)

**R4 (mapping table):** The real→fake mapping table is held in-process only on EC2 RAM during Pass 2. It has NOT been written to `opal-data-demo`, git, logs, or messages at any point in this session. CONFIRMED.

**R7 (value-mode verbatim):** `--value-mode verbatim` is the operative switch in the SSM dispatch. Dollar values are copied verbatim from `opal-data-bd` to `opal-data-demo`. CONFIRMED.

**AC7 (no write to opal-data-bd):** Transform reads `opal-data-bd` strictly read-only. Source bucket is never written or mutated. CONFIRMED.

---

## Watcher Discipline

Watcher maintained throughout session:
- PID 582390, PROCESS-OK at all checks
- `check-inbox 0.4.0_DS_ClientPlatform~C`: empty at all checks
- Heartbeat: called each monitoring cycle
- Registration: LIVE (MCP strips ~C suffix; full serial confirmed via `register_agent`)

---

## ADVI_DEMOV1.006 — PATH B (HELD)

Per COO message (20260524T033635Z) and MSTR LD-0030:
- **Sequencing:** attempt-13 runs to completion before Path B implementation begins.
- **If attempt-13 SUCCEEDS (R5 zero leaks):** DEMOV1.006 becomes the structural follow-on. Path B is the durable mechanism for any future demo-data refresh.
- **If attempt-13 FAILS (new leaks found):** DEMOV1.006 supersedes immediately; transition from substring-scan iteration to build-time structured tagging.
- **Path B design (M-1):** Pre-build a structured index of all real-name fragments; at fake-identity generation, check generated candidate against the index via structural disjointness (not substring scan). Data-structure choice (trie / set-of-tuples / hash-based) to be documented when implementation begins.
- **FN-1 regression-test fixture:** Must cover: `austin_thompson` (attempt-9), `sam_owens` (attempt-10), `Powell/Winslow/Clarke` (attempt-11), attempt-12 exposes (commit `c61d4da6e`), attempt-13 catches (commit `dbf170b32` guard outputs).

---

## Compiler Tools Mandate — Phases 2 and 3 (PENDING)

**Phase 2 (PII scan — the closure gate):**
```
<run> python3 /opt/demo/pii_leak_scan.py --source-bucket opal-data-bd \
      --target-bucket opal-data-demo --seed advi-demov1-2026 \
      --workers 64 --report /tmp/pii_scan_result.json </run>
<expect> ZERO leaks (leak_count: 0, leaks: []) </expect>
```
Status: PENDING — Phase B still running. Result will be read from S3 artifact on Phase D upload.

**Phase 3 (Sigma-identity reconciliation + RAVC2):**
Status: PENDING — depends on Phase 2 result.

---

## Next Steps

1. **Phase B completes (~17:56 UTC):** Firm phase runs (~18:02 UTC).
2. **Phase C (PII scan) runs (~19:02 UTC):** SSM auto-continues per `set -euo pipefail` chain.
3. **Phase D (upload result):** `pii_leak_scan_result.json` uploaded to S3 artifact bucket.
4. **SSM transitions to Succeeded or Failed.**
5. **If Succeeded + leak_count == 0:**
   - Proceed to Phase 4 Sigma-identity reconciliation (ACs 5, 7, 8).
   - RAVC2 to COO~C + CC CVO + CC AE~C citing R5 scan output + reconciliation evidence.
   - Then pick up DEMOV1.006 (Path B implementation).
6. **If Succeeded + leak_count > 0 OR Failed (HARD ERROR):**
   - Read `leaks` array / stdout sorted leakers.
   - Diagnose new leak class.
   - Fix `fake_identities.py`, run ds-commit-gate, commit, upload to S3.
   - Dispatch attempt-14 via SSM.
   - Append to regression-test fixture.
   - Begin DEMOV1.006 immediately (this outcome = Path B supersedes).
