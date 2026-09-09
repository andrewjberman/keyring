# NFRA_OUTSET round 2 -- L8 PACKET (PARTIAL, and the word is load-bearing)

**Compiled by** `2.0.0_SA_COO` 2026-09-09 ~14:1xZ, on the `/drive` obligation "terminal orders -> L8 compile NOW".
**Handed to** `3.0.0_SA_CVO` for L9. **This is NOT the L10 slug** -- the slug goes once, after EVERY order is terminal
and EVERY row is dispositioned, and one of the two round-2 orders is mid-act. This packet exists so the CVO's L9 work on
the terminal order can run while the deploy lands instead of queueing behind it. `COMPLETION_REPORT.round2.json` (the
full compile, schema 1.0) follows when `TO-OS-s-19` is terminal.

---

## 1. WHY PARTIAL, and the fact that decides it

Round 2 is two orders, both `0.7.0_AE_CloudOps~W`, sequenced (decomposition v0.3 s.9): `TO-OS-s-18` COMPLETE at HEAD
@`0c1c0110ae` (13:45Z); `TO-OS-s-19` PENDING with its NEVER-2 change-management entry OPENED and committed before the
upload @`6dbb1e6a3a` (13:52Z, `org/critical_paths/change_management/20260909T1352Z_estate-report-runner-outset-seam-consumer_deploy_completion.md`,
four legs unchecked). The upload lands outside the report host's run window (today's run 13:00:45Z -> 13:11:04Z; next
fire 2026-09-10 13:00Z), so the deploy is not late; it is in flight.

## 2. THE TERMINAL ORDER, with the instance the checker graded

| order | cell | outcome_ref | instance | checker (issuer's own run, 14:1xZ) | flipped at |
|---|---|---|---|---|---|
| `TO-OS-s-18` | `OS-s-18` | FWD-3 | `deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-18.the-publish-to-the-consumption-seam.proof_of_spec.json` @`0c1c0110ae` | `proof-of-spec-check.py <instance> O18-AC1,O18-AC2` -> **VALID rc=0**; alignment 2/2 criteria carry a cell_ref, 1/1 cell resolves, 1/1 owned cell reachable; 7 artifact rows (1 at pin, 3 co-committed, 3 s3_object); 4 of 4 surprises resolve to a channel row | `0c1c0110ae` by the assignee, against the face AMENDED @`cb43d05200` (read at HEAD by `git show`, lineage `merge-base --is-ancestor` YES) |

**The face was amended once, by the issuer, on row S18** (@`cb43d05200`): O18-AC1's `<invocation>` path moved from
`.tools/tests/` to the seat's own deliverables folder because a `<paths>` block is a grant for a `0.9.0_WK_*` serial and
for nobody else (`.tools/owned-paths-validate.py` `_WORKER_SERIAL_RE`; measured at the issuer with a negative and a
positive control). `<expect>` unchanged. **The battery was not byte-for-byte across the move and the assignee disclosed the
one changed line**: the workspace-root derivation (`Path(__file__).resolve().parents[2]`, true at the old depth, wrong at
the new) replaced by `git rev-parse --show-toplevel` with a marker-walk fallback -- CLAUDE.md's own rule for workspace
roots. Every arm and assertion unchanged.

## 3. THE MECHANICAL CRITERION -- read by the issuer, not re-run

- **O18-AC1** `timeout 300 python <amended path>` -> `OS18-SEAM-READABLE`, **rc=0 captured unpiped** (the assignee names the
  pipeline-rc trap explicitly); second grain `python -m pytest -q <same path>` -> 1 passed. **Determinism** as VERDICT SETS
  over two same-input runs (a stdout hash would have tested the clock: the battery stamps UTC and mkdtemp paths into its
  own output). Arms: 13 of 13 PASSED at 13:10:23Z with the host up; 12 of 12 PASSED + 1 NOT-EVALUATED (`A1`, the host
  self-stopped 13:11:04Z) at the graded 13:45Z run -- NOT-EVALUATED never counted as a pass, and the assignee declined to
  start the box to green it (starting it fires a full run under the served 2026-08-25 runner).
- **Nine RED arms, and the one W2-S21 named**: R1 a genuinely broken producer publishes `answer_state=FAILED` with
  `denominators.claim=absent` rather than nothing; R2 that FAILED artifact placed at a FIXED probe key on the live seam
  and read back through the real consumer -> `INSTRUMENT_FAILED`, `absent=False`, 0 rows; R3 the RENDERED report carries
  `STATUS: *** INSTRUMENT_FAILED` / `THIS STRATUM PRODUCED NO DATA`; R4 never-published reads FAILED with `absent=True`;
  R5 stale 999.0 h vs the 26 h ceiling; R6 future-dated refused; R7 an unmapped answer_state refused, never OK;
  **R8 the OK and FAILED renderings are NOT byte-identical (4151 vs 1436 B)** -- the arm 51 round-1 green arms assumed and
  none made; **M a planted mutant** (`"FAILED": "INSTRUMENT_FAILED" -> "OK"` in a COPY of the runner) is DETECTED, with
  anchor uniqueness asserted first so it refuses rather than silently mutating nothing.
- **Why the issuer did not re-run it**: arm R2 `put_object`s to the live bucket (one fixed probe key, overwritten never
  deleted, PRD R-5). The instance validates VALID here on the issuer's own instrument and the committed output carries
  the match; a third live-plane write buys no discrimination. Stated so the certification's basis is visible.

## 4. THE JUDGMENT CRITERION -- THIS IS THE L9 WORK

**O18-AC2** (`judgment="true"`) is RECORDED with vintage and NO verdict. A PASS/FAIL on it here would be INVALID.
Three planes, separately named by the assignee:

- **DESIRED**: `infra/aws/terraform/estate-report/iam.tf` @`54ccbdb47d` adds `${aws_s3_bucket.estate_report.arn}/outset/*`
  (GetObject ONLY; no ListBucket on the prefix, deliberately) to `ReadPredecessorAndOwnCode`; vendored
  `.tools/terraform.exe` v1.9.8; plan 0 add / 1 change / 0 destroy; `safe-apply` 0/1/0; UNSCOPED re-plan "No changes".
- **APPLIED**: `comp-iam refresh-census` FIRST (24 h TTL) -> `docs/briefs/cmpaws-iam-census-20260909.json` (13:00:19Z,
  224 roles; untracked, cited by path and vintage). The role's GetObject statement reads `daily/*`, `code/*`,
  `manifest/*`, `kuzu_nessie_db`, `outset/*` -- 6 resolved statements + **1 UNRESOLVED managed statement
  (`AmazonSSMManagedInstanceCore`) recorded as UNCOVERED, never absent**. `W1-S19` CORROBORATED, not corrected.
  The assignee also corrected its own draft: msg 94465's "11 resources" is right at the grain of the
  `estate-report-runner` inline policy BEFORE the change (12 after); two correct numbers at two grains.
- **EXERCISED**, the grain neither other plane gives: inside the 13:00 ET run window, principal read from
  `sts:GetCallerIdentity` in the same invocation = `assumed-role/estate-report-runner-role/i-0512bd3cbaf602b7f`;
  `GetObject outset/comp_heat_drift.json` rc 0, 27060 B, `answer_state=OK`; **negative control** `GetObject` on a REAL
  object under a Put-only prefix -> rc 254 AccessDenied (action-level, not 403-because-absent); **positive control**
  `head-object code/...` rc 0, separate call. `simulate-principal-policy` one ARN per call, three invocations; the
  target statement carries `condition:null`, so the conditioned-grant false-deny mode could not apply.
- **The publish**: 2 of 2 producers non-FAILED -- `outset/comp_heat_drift.json` 27060 B @13:03:50Z,
  `outset/comp_heat_freshness_tools.json` 63822 B @13:03:49Z (s3api, UTC); the prefix held ZERO objects before.

## 5. COVERAGE OF THE ROUND-2 CELLS, with the caveat the grader must not have to find

| outcome | cell | order | claim at this packet | what the claim does NOT say |
|---|---|---|---|---|
| FWD-3 | `OS-s-18` | `TO-OS-s-18` COMPLETE | **COVERED on the producer side**: an artifact reaches the seam and the runner's role reads it, exercised | **The consumer still does not look.** `ESTATE_OUTSET_SEAM_PREFIX` is unset in the host's `runtime.env` (`instance.tf:130-151`; 0 hits under terraform), so `_stratum_propagation` returns INSTRUMENT_UNAVAILABLE without composing a key (row S16). The CTO ADOPTED the placement @`e18317d0e0`: a manifest row `OS-s-20` for the L10 addendum v0.4 (set the prefix and replace the host, AFTER OS-s-19). **FWD-3's REALIZED reading is the CVO's at L10 and this seat expects it to wait on OS-s-20**, the third project in two days where cell PASS and outcome REALIZED part company on Rule 22's STATE axis. |
| FWD-2, FWD-4, FWD-7 | `OS-s-19` | `TO-OS-s-19` PENDING | not claimed | the deploy is in flight under its ledger entry; its accept is the served bytes matching HEAD, proven on the served object |

**Denominators**: FWD in the PRD header 8; cells in decomposition v0.3 19; round-2 orders 2; terminal with a valid
instance **1 of 2**; round-2 rows in the channel this packet names: S16, S17 (OBSERVATION/ARMED, placed by the CTO
@`e18317d0e0` as OS-s-20/OS-s-21 for the addendum), S18 (BLOCKING, the issuer's, RULED @`cb43d05200`), S19 (the S18
disarm ack measured at the assignee, grading nothing). Rows S16/S17/S18's dispositions are the CVO's at L9.

## 6. WHAT THIS PACKET DOES NOT DO

No verdict on O18-AC2. No claim on FWD-2/4/7. No row dispositioned. No cell cut: S16/S17 land as addendum rows at
L10 (the spec is frozen mid-round; Andrew's ~12:5xZ word lets OUTSET adjudications move and bars new work). The slug
is the CVO's, once, after `TO-OS-s-19` is terminal and every row is dispositioned.

Push state at compile: LOCAL; origin/CLOUD @`58adeff90c` (ls-remote 12:5xZ); every hash above is on this device only
under the LD-0522 hold.
