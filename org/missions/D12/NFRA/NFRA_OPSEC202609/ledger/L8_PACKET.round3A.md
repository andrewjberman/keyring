# NFRA_OPSEC202609 issuance 3A -- L8 PACKET (the COO's drain-end record for the one deferred order)

**From** `2.0.0_SA_COO~Z` (L5/L6 issuer) **for** `3.0.0_SA_CVO~Z` (L8/L9), read from files, not sent.
**Compiled** 2026-09-10 ~20:2xZ at HEAD `ea5d79c9c1`. Branch `SITEZ`. Push state LOCAL (origin/SITEZ `c0b5636ea9` by
ls-remote at session start; only `0.0.0_AB_MSTR~Z` pushes).
**Instruments:** `.tools/proof-of-spec-check.py` re-run at this seat from inside the worker's worktree (VALID rc=0) and
again from the main tree after the drain (VALID rc=0); `aws lambda get-function-configuration` read at this seat, not
relayed; `.tools/surprise-row-gate.py::_latest_dispositions(root, code)` for the channel census.

---

## 1. THE ORDER SET -- 1 OF 1 TERMINAL, AND 35 OF 35 ACROSS THE PROJECT (unscoped, every `<status>` read at HEAD)

| order | `<status>` | terminal? | how |
|---|---|---|---|
| `TO-OP3A-S-1` | `complete` | **yes** | worker `~6` @`1d103b4651`, drained @`ea5d79c9c1` |

**Three slots served this one cell, and the record says why:** `~4` found the `<paths>` grant could not reach the packaged
Python (row `Z-W4-S1`; amended @`775e6cf20a`); `~5` executed the migration in full and could neither commit nor deploy it
because that amendment left `<issued_to>` at `~4` (rows `Z-W5-S2`/`S3`, `Z-S178`, `C-S44`/`C-S45`); this session drained
`~5`'s record @`c3e6c8c6fe`, re-seated the WHOLE identity block `~4 -> ~6` @`1f87188985`, and `~6` performed the deploy.
Slots `~5` and `~6` are torn down; 0 worktrees and 0 branches remain for this project.

## 2. THE CRITERION LEDGER -- 9 of 9 carry a verdict

| verdict | n | which |
|---|---|---|
| PASS | **8** | `S3A-AC1` .. `S3A-AC8` |
| JUDGMENT, recorded, no verdict | **1** | `S3A-AC9` -- **yours at L9** |

**What the two probes did (S3A-AC6 / S3A-AC7), from the Lambda runtime, not a local run:**

| function | invoke result | own log line |
|---|---|---|
| `opal-otp-liveness` | `{"ok": true, "cred_path": "exchange", "detail": "status=200"}` | `cred_path=exchange url=https://mcp.opalinvest.dev/otp/token aud=gw:otp ttl=300s` |
| `opal-ms-ingest-liveness` | `{"ok": true, "cred_path": "exchange", "detail": "status=200"}` | `cred_path=exchange url=https://mcp.opalinvest.dev/ms/token aud=gw:ms ttl=300s` |

**Live state, read at this seat after the drain** (`get-function-configuration`):

| function | CodeSha256 | LastModified | exchange URL env |
|---|---|---|---|
| `opal-otp-liveness` | `3arS31NYi8MRfT2zpMny1r4xApcR7GffVRf1TWP9+xI=` | `2026-09-10T19:37:07Z` | `OTP_TOKEN_URL` present |
| `opal-ms-ingest-liveness` | `tsI6QgpY3ODD3CLYdrdZMv6vUleIUpWF7RgEXXVM7i4=` | `2026-09-10T19:37:02Z` | `MS_TOKEN_URL` present |

Both equal the targeted plan's predicted hashes (the worker's step 7). Pre-deploy values, for the rollback oracle, are in
the CLOSED ledger entry `org/critical_paths/change_management/20260910T1714Z_opsec-op3a-s1-liveness-exchange-migration_deploy_completion.md`.

**What the deploy deliberately did NOT do, so the grade is not read wider than the cell:** the static bearer is NOT
retired and neither secret is revoked (dual-accept measured intact before and after); the THREE CROSS-LANE callers are
untouched, by Andrew's ruling @`9382d107a3` s.1; no alarm, monitor or notification was added (2 `_alert()` sites per
file, unchanged); no gateway-side edit; the apply was `-target`ed to the two functions because the shared root carried
`0.7.0_AE_CloudOps`'s two `aws_wafv2_ip_set` changes (row `Z-W5-S1`, re-confirmed unchanged by `~6`'s baseline plan).

⚠ **BOUND, carried from both workers:** every live number was taken inside short windows on 2026-09-10 (16:13Z-16:31Z,
16:57Z-17:23Z, 19:26Z-19:4xZ). They support *"the exchange works and dual-accept is intact at those moments"* and support
no claim about stability across the 6-hour probe cadence. The next scheduled fires are the first organic evidence.

## 3. THE ROW CENSUS -- 4 UNDISPOSITIONED OF 190

`_latest_dispositions(root, "NFRA_OPSEC202609")`: **190 items, 122 GRADUATED, 64 DISMISSED_WITH_REASON, 4
UNDER_INVESTIGATION** -- exactly the four `~5` rows that landed with the drain @`c3e6c8c6fe`:

| row | class | hazard | disarm owner | state now |
|---|---|---|---|---|
| `Z-W5-S1` | OBSERVATION | ARMED | `0.7.0_AE_CloudOps` (**dark**) | the shared TF root still carries that lane's two ip-set description changes, unapplied; `~6` re-read it unchanged |
| `Z-W5-S2` | BLOCKING | ARMED | `2.0.0_SA_COO~Z` | **DISARMED BY EXERCISE** -- `~6` was ADMITTED by `safe-apply` (rc=0) after the re-seat @`1f87188985` |
| `Z-W5-S3` | BLOCKING | ARMED | `2.0.0_SA_COO~Z` | **DISARMED BY EXERCISE** -- `~6` was ADMITTED by `safe-commit` on all 9 paths incl. 6 under `infra/` |
| `Z-W5-S4` | OBSERVATION | ARMED | `1.0.0_SA_CTO~Z` | the proof-of-spec checker's PENDING-THIS-COMMIT handling of tracked-but-unstaged artifacts; `~6` hit the same and worked inside it |

Rows `Z-S178` / `C-S44` (ARMED, disarm owner *"a live COO lane"*) are discharged by the same exercise. **This seat owns
the DISARM, not the DISPOSITION** -- all four stay `UNDER_INVESTIGATION` until L9.

**ARMED at surfacing, whole project: 89 of 190.** Owner census: `2.0.0_SA_COO~Z` 65 · `1.0.0_SA_CTO~Z` 12 ·
`3.0.0_SA_CVO~Z` 3 · dark owners 9 (`0.7.0_AE_CloudOps` and lanes 8, `0.6.0_AE_PartnerETL~Z` 1 -- 8 of the 9 already
GRADUATED, `Z-W5-S1` the one open). The dark-owner list rides the drain-end read to the CTO, as the spine routes it.

## 4. WHAT THIS PACKET DOES NOT CLAIM

- **It does not grade `S3A-AC9`.** The two probes' outputs are above; the verdict is yours.
- **It does not assert FWD-12 is REALIZED.** It asserts the in-lane half is EXERCISED at the vintages named; the
  cross-lane half is another lane's by ruling and the PRD's own DONE WHEN for FWD-12 is the round-2 cell's.
- **It does not close the project.** `ledger/COMPLETION_REPORT.round3.json` (this seat, this commit, schema-valid) is the
  coverage read; `COMPLETION_GRADES` is `1.0.0_SA_CTO~Z`'s and follows the slug.
- **It does not claim stability.** See the bound in section 2.
