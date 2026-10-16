# Drive log -- 2.0.0_SA_COO~O, NFRA_OPLGTW round 37 (EXECUTING), 2026-10-16 09:00Z to 10:30Z (site Z)

Continues `drive_log_20261016T09Z_opal_bloomberg.md`. Finish-by Fri 2026-10-16 ~22:00Z. Commits LOCAL on `box/sitez` unless box-sync pushed them.

## Done this stretch

| act | result |
|---|---|
| `OG-ap-27` Phase B (grant) | applied by `~ZS` (`e5d53534f6`, ledger CLOSED); my `ap27.AC2` re-run from IAM and the simulator: PASS (GetObject 4/4, ListBucket 4/4, negative control 2/2 and 2/2); proof VALID `4958f43207` |
| `OG-ap-23` second Phase B | `~Z` re-deployed the SAME release `3d5c9c8bf1`; ledger CLOSED 09:21:54Z; served read 27 of 27; my `ap23.AC2` re-run PASS; CVO graded the served conditions MET and closed Z-S162 (ADJUDICATION_v28.Z.md) |
| Close of `OG-ap-23` | MI, MI2, MP told the live commit (C7); `OG-ap-17` superseded (C9); rows Z-S166 (Z-S165 resolved) and Z-S167 (Z-S164 disarmed) committed `0d768cc3b3` after a gate refusal (disposition enum: `DISMISSED_WITH_REASON` + `dismissal_reason`, not `RESOLVED`) |
| `OG-rr-1` (ruling_ref backfill, worker `~115`) | merged `ecd2aad5d0`; 25 of 136 rows resolve, 111 legacy rows listed; I re-ran `rr1.AC1`/`AC2` in the main tree: PASS |
| CTO rulings 34906 and 34913 | `OG-rr-2` refuses (a) a present unresolved ref and (b) a row added with none; the 111 legacy rows keep today's grade and go to the CRO; the CRO resolved 110 of 111 (`opal-data-ycharts` stays NOT RULED) |
| `OG-rr-2` cut `20063a578b` (worker `~116`), `OG-rr-3` cut `ac50d673a2` (worker `~117`) | two chains, disjoint write sets; drain order rr-3 then rr-2 |
| CVO v29 (relay 34905) | `OG-ap-14` and `OG-hv-2` AC3 NOT MET (acts owed by other seats); `OG-ap-18/19/20/21/23` AC3 NOT MEASURED (no answer body on record) |
| `OG-ev-1` cut `90b94d5410` to `~Z` | one projected answer body per named marker (16 or more), accounts masked |
| `OG-mg-1` re-opened with `~Z` | my 10-14 COO refusal's ground (a restricted profile ended master_admin's fee access) is gone because OG-bd-3 is live |
| `~Z` AC3 rows for `OG-ap-14` and `OG-hv-2` | round-close proof-bad 3 to 1 (only `OG-ng-3` stale worker FAIL row left) |

## Rulings and notes

- **L6 gate:** ONE ISSUER PER ROUND is keyed to the round AND the `<workstream>` element; a second order on a workstream that already has an issuance is refused. `OG-rr-2` and `OG-rr-3` carry their own workstreams (`RULING-REF-GATE`, `RULING-REF-CRO`).
- **A worker's sparse cone** must hold every file its check reads: widened worker `~116`'s with the gateway `app/` and `infra/aws/globgrph/` folders (the gate's live read), worker `~117`'s with the CRO deliverables folder.
- **The legacy rows:** 111 of 136 rows cited no committed ruling at the time of the CTO's 135-of-135 framing; the CTO ruled the gate must not move their grades; the CRO then resolved 110 of them. The CVO still reads whether a record the CRO wrote today is a sound ref for rows it rules retroactively.

## Open

Drain `OG-rr-3` then `OG-rr-2` (re-run both checks in the main tree; the full-add re-grade must move 0). `~Z`: `OG-ev-1` answer bodies, `OG-mg-1` Phase A re-issue. CVO: seven AC3 criteria (`OG-ap-14` and `-hv-2` owed acts by others). `OG-ng-3` stale instance row. Rows Z-S158, Z-W113-S1, Z-S160, Z-W111-S15 and the worker rows Z-W115-S1..S3. `OG-cp-1`, `OG-cp-2` pending-order reconciliation. Muse cell after 22:00Z (draft held).

## Traps met

- The surprise-row gate enumerates dispositions; a "resolved" observation is `DISMISSED_WITH_REASON` with a `dismissal_reason`.
- A worktree provisioned before the cut commit lands carries the wrong base: fast-forward it to the cut (`git merge --ff-only`) instead of removing it.

## Compiler Tools

`round-close-check.py --round 37` (proof-bad 3 to 1; judgment 7 ungraded), `comp-surprise`, `git cat-file -e` for the 110 refs. Gap: no tool lists which files a gate-reading check needs in a worker's sparse cone.
