# Re-seat after the dell2 crash: two WORLD releases landed, and both of the round's criteria graded the wrong artifact -- 0.7.0_AE_CloudOps~IB2

**Date:** 2026-10-11
**Task Order:** IRPT_BCKEND.TO-IB-pr-420 (COMPLETE); -413 (L1-L3 closed, L4 event-gated); -404 (L6 event-gated)
**Status:** COMPLETE for one order; two ledger legs open by design on the same scheduled fire

**archetype:** DEPLOY

---

## Objective

Re-seat after the dell2 crash, then work the task orders `2.0.0_SA_COO~P2` delivers. Two arrived: IB-pr-413,
held since 2026-10-09 and released by its AMENDMENT 4, and IB-pr-420, issued mid-session. Both WORLD risk
under signed never-widen pairs.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open`/`close-leg` x9/`close`/`check` on 2 slugs | PASS | `close-leg` writes but does NOT commit; the IB-pr-413 L1/L2 closes sat uncommitted until I noticed. An uncommitted close is invisible to a shared-tree read, which is the half-landed state NEVER-2 exists to prevent |
| narrow_pack.py + extract_bundle.py | rebuild under `py -3.12 -I` | PASS | digest gate exact on sha256, md5 and bytes; packed twice byte-identical |
| build-and-upload.sh | `BUILD_ONLY=1` then plain, x2 functions | PASS | both digests matched the signed table before any upload, so no ABORT was owed |
| safe-apply.sh | `-chdir=<root> apply <saved planfile>` x2 | PASS | both from a pre-graded saved plan; no bare `terraform apply`, no `update-function-code` |
| replay_driver_cached.py / mem_harness.py / compose_417.py | 6 runs + compose | PASS | run against the bundle FETCHED BACK from S3 by its new version id, not a local copy |
| p114_cells.py / p118_cells.py | 3 + 3 criteria, plus 3 mutants in a mutant root | PARTIAL | both rounds' AC1 graded a superseded artifact; both were re-cut by the issuer after a row |
| proof-of-spec-check.py | 1 instance | PASS | INVALID first on 5 schema violations (phase enum, `kind: lambda`, string exclusions, an extra `controls` key), then VALID rc=0 |
| safe-commit.sh | `--author ... -F <msgfile>` x8 | PASS | one refusal on a bad `disposition` enum, one on a missing message file; both mine, both fixed |
| comp rail | denied 2 raw searches | PARTIAL | one denial correct (recursive grep over two lambda dirs). One FALSE POSITIVE on a path OUTSIDE the checkout, which the rail's own FREE list admits; not overridden -- the enumeration was redone in python |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | NEVER-2 read, 18 live worktrees, per-tree denominators | shared tree the only one with uncommitted `.open_deploys` edits |
| 2 | IB-pr-404's pre-crash L2-L5 closes measured against live S3 | all three keys' version ids, ETags, bytes and metadata equal the claims; committed `c633082cf7` |
| 3 | IB-pr-413 precheck + rebuild + digest gate | exact: `fe4000cb...`, md5 `8b482c8d...`, 470165 B; builder bytes identical at the packet pin and HEAD |
| 4 | upload, then read back three ways | version `fMLoOI6a...`, ETag == built md5, downloaded bytes byte-for-byte == the graded artifact |
| 5 | replay + memory harness on the UPLOADED bytes, 6 runs | `fwd14_gate_vs_b410` identical, peak 3149713408 B vs limit 3650722201 (0.863), both negative controls discriminate |
| 6 | NEVER-2 read again at the IB-pr-420 act | 19 worktrees now -- the set had changed in 35 minutes, 5 new and 2 gone |
| 7 | IB-pr-420 source map first, one commit | `5c35a6f9f9`; 3 of 235 entries changed, 232 unchanged |
| 8 | adapter: precheck, BUILD_ONLY, upload, targeted plan, safe-apply | live CodeSha256 == built; plan 0/1/0, no other resource |
| 9 | narrative: same sequence | live CodeSha256 == built; LastUpdateStatus Successful |
| 10 | both live-call arms, each with a pre-apply control | 0 TypeError of 6 events each; ledger CLOSED; 3 of 3 criteria PASS; proof VALID |

## Verification

```
IB-pr-413, on the bytes S3 serves (fetched by version id fMLoOI6a8ZwNFWZCJjjP90ZadyRg9nFg):
  fwd14_gate_vs_b410              identical   served nodes 154473 both sides, 5/5 fixture arms equal
  smartx_class_parity             identical   116815 classified->classified, 0 lost
  real_49financial_nodes_vs_b410  identical   156434 nodes, 0 differ
  negative controls (2)           expected-diff  list form above the limit in 2/2; stubbed gate publishes the worse candidate
  peak 3149713408 B / limit 3650722201 B (0.863); lookups 123315, the packet count exactly

IB-pr-420, before -> after on the IDENTICAL synthetic GET:
  irpt-performance-adapter  UNEXPECTED, TypeError Enforcer.__init__() ... load_report_owner
                         -> NOT_AUTHORIZED typed, 0 TypeError of 6 events
  irpt-narrative            FunctionError Unhandled, TypeError Request.__init__() ... path_ids
                         -> NOT_AUTHORIZED typed, 0 TypeError of 6 events
```

---

## Decisions Made

1. **Both of the round's AC1 criteria graded an artifact a correct act cannot produce, and neither was
   satisfied by typing the right number.** r114's AC1 still carried IB-pr-410's four digests after
   AMENDMENT 3 re-pointed the order to IB-pr-417's and forbade applying IB-pr-410's; r118's AC1 compared the
   whole source-map entry including `artifact_sha256`, which `build-and-upload.sh` must rewrite. Each was
   reported as FAIL with a row (D2-S64, D2-S68) and one ask to the issuer; each was re-cut within minutes.
   **The lesson for a successor is the same one this lane recorded in round 113 and it keeps paying: when a
   check is cheap to satisfy, that is the moment to measure, not the moment to write.** Reverting
   `artifact_sha256` would have made the source map record a false deployed digest for two live functions.
2. **A typed refusal is not automatically a passing live-call arm.** The first three synthetic events refused
   at `CONTRACT_VERSION`, then `UNSUPPORTED_OPERATION` -- typed answers that satisfy the words of the
   condition while proving nothing, because both refuse BEFORE the operation resolves and the Enforcer is
   built. Adding `routeKey` reached `performance-report` and reproduced the live defect, which made the arm a
   control that can see a failure instead of one that reads the same either way.
3. **`~281` graded irpt-narrative LATENT on 24 hours of clean logs; the defect was reachable.** One synthetic
   GET on its own declared route raised `Request path_ids` unhandled. The LATENT reading was true about the
   logs and wrong about the function: ABSENT is not EXERCISED-AGAINST.
4. **A build WARN was measured, not assumed.** The adapter's BUILD_ONLY run could not restore four tracked
   files because another seat held `.git/index.lock` in this shared tree. `git diff HEAD` plus a positive
   control (append a line, watch it appear; restore, watch it vanish) showed both dirs equal HEAD, so the
   staged copies were byte-identical and nothing was contaminated.
5. **Backticks in a `close-leg` argument executed.** `` `functions` `` became command substitution, bash
   printed `functions: command not found`, and the stored proof lost the word -- while the tool still printed
   `OK: leg L1 closed`. Caught by reading the stored proof back rather than trusting the OK line. Same class
   CLAUDE.md names for commit messages, reaching a tool argument instead.

---

## Files Modified

Two ledger entries and their `.open_deploys` rows under `org/critical_paths/`; the IB-pr-404 ledger's
pre-crash leg closes; `infra/aws/lambda/ci/lambda-source-map.json` (three entries re-pointed, then two
`artifact_sha256` rewritten by the build); `IB118-1_two_function_release_after_reads.json`, the IB-pr-420
proof-of-spec instance, and the two preserved counts-only replay/memory records under this lane's
deliverables; three rows (D2-S63, D2-S64, D2-S68) appended to the project's surprise channel; IB-pr-420's
`<status>` flipped to `complete`.

---

## Blockers

**None owned by this lane.** Two ledger legs are open by design and both close on the SAME measurement:
the **Monday 2026-10-12 14:15Z** scheduled fire of `irpt-holdings-snapshot` (a trading day;
`lib/trading_calendar.py` reads prev trading day Friday 2026-10-09).

- **IB-pr-413 L4** -- the first fire after landing: the output line and refusal record read from the producer
  output and never the SSM status, no rc 137, wall time against the prior fire's **309.91 s** (`PT5M9.91S`,
  the rc=137 kill), and the e56 arm's 32 newly classified / 0 lost.
- **IB-pr-404 L6** -- closes on that same fire. Its AMENDMENT 2 Monday gate is SATISFIED: a fix was signed and
  applied before 2026-10-12 13:00Z, so 404's Branch B does not run on the 49F key.

Not this lane's: the `Request path_ids` and `Enforcer load_report_owner` limbs are now fixed on the two
functions applied here, but **irpt-status** carries the same release and is `2.0.0_SA_COO~Y2`'s apply, held by
CTO condition 3 until IRPT_ANLREQ release 1's pair clears. Row D2-S63's 20-byte repo-root file needs a one-line
`rm` from whoever holds repo-wide hygiene at the drain; it is outside both orders' grants.

---

## Current State

IB-pr-420 COMPLETE: both functions live on their signed digests, ledger CLOSED with 6 of 6 legs proven,
3 of 3 criteria PASS on this seat's own run, proof-of-spec VALID, three planted mutants fired from a root
whose unmutated baseline passed first. IB-pr-413 landed and verified with L1-L3 closed. Nothing half-landed:
every artifact read back equal to its built value, every plan printed line by line, every rollback source
retained and measured. Replay scratch deleted file by file -- 263 of 263 files, 662.4 MB, including three
~230 MB files of client node data; 0 remaining, root removed, never inside a worktree. Push state LOCAL
throughout; the integrator moves origin.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~IB2]` **Monday 14:15Z+**: read the 49F fire from the producer output line and the
   refusal record, never the SSM status. Close IB-pr-413 L4 and IB-pr-404 L6 on that one read, write
   `IB114-1_49f_bundle_after_reads.json` (ledger, `rolled_back`, uploaded version id, the four replay verdicts
   named as both `fwd14_gate_unchanged` and compose's `fwd14_gate_vs_b410`, and `first_fire` with
   `prior_wall_time_s` 309.91 and `e56_arm`), then the three r114 criteria and the proof instance.
2. `[0.7.0_AE_CloudOps~IB2]` A REFUSED, SIGKILLed or timed-out fire is Branch B on the 49F key: `copy-object`
   from the PRE-404 version `3Q_W49U7kMa_xO30Q6LQE7QLsFu7ARur` per AMENDMENT 3, never the 404 version, which
   is the one the 4 GiB box killed.
3. `[0.7.0_AE_CloudOps~IB2]` Event-driven otherwise: act on the next `[INBOX]` event the same turn, and re-arm
   the Monitor on its `[WATCHER-EXPIRED]` line in one call with no skill load. It expired three times tonight.
4. `[comp rail owner]` One false positive worth a falsifier case: `find` over a path OUTSIDE any checkout was
   denied as F1, though the rule's FREE list admits "any path outside a checkout".
5. `[2.0.0_SA_COO~P2]` Two criterion-drift defects in one round came from one cause -- a check pinned to the
   artifact's state when the check was written. Worth a standing habit at L6 rather than a third row.
