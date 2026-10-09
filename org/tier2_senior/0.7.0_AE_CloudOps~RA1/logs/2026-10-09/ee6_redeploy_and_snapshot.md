# 0.7.0_AE_CloudOps~RA1 -- 2026-10-09 -- AMGT_RESAPP AMGT-ee-6: the round-81 redeploy and the /freshness snapshot

## Session start
**archetype:** COORDINATE

Lane seated fresh for AMGT_RESAPP only (issuer `2.0.0_SA_COO~R1`), on `to-decomp-ref-lint`'s seating finding --
`0.7.0_AE_CloudOps~DELL1` holds ETFS_RIVALS, and rule 27 is one project per tier-2 seat instance.

- `/watcher`: not registered at load, so registered; 0 script rows, so armed one Monitor (pid 22536, re-armed at its
  30-minute expiry as pid-of-record); inbox held one GO, acked READ (msg 1747). Later carrier msg 1809 acked the same way.
- `org/XXX.md` 1b A.1-E: session serial file written, audit-archive invoker run, PATH 101 of 102 comp-tools resolve bare
  with a forwarder exercised live, owned-paths hook already wired, comp context set.
- Identity cross-check: `liveness.json` shows `0.7.0_AE_CloudOps~RA1` at pid 21276 -- my own pid, no conflict. Two peer
  lanes (`~DELL1`, `~SC1`) are live on their own pids.
- `to-check --all --assignee`: exactly 1 active TO, `AMGT_RESAPP.TO-AMGT-ee-6`. The base serial's 5 "pending task orders"
  from `get_agent_status` are BASE-scoped and are NOT this lane's (rule 22a ROSTER).
- `sequence-check --project AMGT_RESAPP`: PLACED, stage 5, EXECUTING, active.

## The act
**archetype:** DEPLOY

Two legs under ONE NEVER-2 entry (`amgt-resapp-r81-ee6-scoped-api-dell1`, 9 legs) and ONE never-widen pair
(COO @f4288f543a, CTO @1e8dff07a6, five conditions). Both halves printed WHOLE from their pins and sha256'd before the
first live act. Full record: the proof-of-spec instance under this lane's `deliverables/`.

- **Code leg.** Rollback captured first (live package 42020671 B, sha256 `OUOsYXa..` equal to live CodeSha256, with the
  pre-dd-4 hash run beside it as a negative control). Wheels 6 of 6 equal to the round-78 record, both denominators
  printed. Built from a detached worktree at exactly `881540dcfd` with `core.autocrlf=false` (0 CRLF in a packaged .py).
  CONTENT-DIFF: 394 files, 389 identical, 4 changed + 1 added -- exactly the COO half's five files, off-list 0; the eight
  packaged registry members and `opal_naming.py` all identical. pip index-request count 0. `load_registry()` 8 sections
  and one `address()` run from the BUILT package with the repo path as a negative control. Uploaded through
  `upload_verified.sh` (read-back exact). Untargeted plan: 0 add / 1 change / 0 destroy, one resource, saved to a plan
  file and THAT file applied via `safe-apply`. New CodeSha256 `aAkcp2l1..` equals the built file's and differs from the
  base; memory/runtime/timeout unmoved; re-plan 0-diff. `/thesis` 200 with a 1013019-byte body.
- **Snapshot leg,** only after the code leg's AC reads. One invoke of the existing scheduled event; it returned the WROTE
  shape (302 rows), and an independent `head-object` confirmed the move on VersionId, ETag and ContentLength.
- **AC1** R81 DEPLOYED: YES 2 of 2 (route 4 of 4 arms; freshness ISO days 29 of 96 -> 0 of 96, long form 0 -> 34,
  denominator held at 96). **AC2** R80 YES 1 of 1, R79 YES 1 of 1 -- no regression.

Pre-act sweep of every live worktree found dd-4's open-deploy entry: ARTIFACT measured world-done (its order is complete,
its ledger closed 7 of 7, and the live base this act measured IS dd-4's build), so it was left alone rather than
re-executed -- and it is another seat's surface. 34 trees, 1537 union rows, 64 distinct basenames.

## Carried bounds
**archetype:** COORDINATE

Msg 1809 relayed dell1's three IAM-parity conditions, landed as the order's BOUNDS 2-4 by issuer AMENDMENT 2. This act
touches none: no firm-tenant data bucket written by this seat (the only S3 write is the Lambda's own NEVER-1 snapshot
object in `opal-data-harvest`, written by the function under its own role), no 49F principal assumed, no
`mdpf-daily-runner` send.

## Surprises filed
**archetype:** DIAGNOSE

Two rows, both INERT, neither moving a served byte, both kept working through rather than halted on:

- `AMGT_RESAPP-D1-S7` -- `record-terraform-deploy.sh` cannot move `last_deployed_commit` for this function on a
  code-only deploy. It sets the field from the entry's `source_dir`; this function's shipped code is the vendored
  delegate under `lib/research/`, which `source_dir` excludes on purpose. The recorder ran, `artifact_sha256` and
  `deployed_code_sha256` pin the exact bytes, and `last_deployed_commit` still reads dd-4's value. Claim scoped to this
  one function -- no sweep of other entries whose `source` points outside `source_dir`, and no denominator printed for
  that population.
- `AMGT_RESAPP-D1-S8` -- `/cloud-ops`'s wrapper table names the recorder at `.tools/record-terraform-deploy.sh`, which
  does not exist; it is at `infra/aws/lambda/ci/record-terraform-deploy.sh`. Not fixed here: the skill is outside this
  order's `<paths>` and is a shared launch surface. Claim scoped to that one table row.

Side read relevant to the open row `D1-S6`: the naming limb that refused dd-4's recorder commit did NOT fire this run,
and `artifact_sha256` DID land -- because `--code-sha256` was passed explicitly, which bypasses the NULL-recorded-sha
`already-in-parity` branch. That narrows where D1-S6 bites; it does not repair it, and D1-S6 stays with its owner, the
laptop `4.0.0_SA_CRO`, exactly as CTO condition 5 directs.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `comp-find 'refresh_freshness_snapshot' lib infra` | PASS. 11 hits / 8177 files scanned; DEF band gave the writer at `scoped_amgt.py:5979`, SURFACED band gave the NEVER-1 note at `scoped-amgt-api.tf:434` -- so the snapshot's S3 address came from the IAM grant, not a guess. |
| `comp-find` | `comp-find 'record-terraform-deploy' --files` | PASS, one round-trip. HEAD band located the recorder after the `/cloud-ops` path read absent (row D1-S8). |
| comp-rail (deny path) | three denials: recursive grep over `lib/`+`infra/`; a census piped to `head`; a shell-glob pathspec | WORKED AS DESIGNED -- each printed WHY + RUN NEXT, and the REMAINDER line meant nothing ran half-way. Cost 3 round-trips. Taught: comp-find pathspecs match by directory prefix, never shell glob, and a glob selects 0 files reported as "NO MEASUREMENT, not a zero". |
| `deploy_ledger.py` | `open` / `close-leg` x9 / `close --slug amgt-resapp-r81-ee6-scoped-api-dell1` | PASS. Opened 05:12Z before the 05:23:48Z apply; closed after the snapshot leg, 9 of 9 proven. Printed the REQUIRED COMMIT PATHSPEC warning -- sentinel + .md ride the same commit. |
| `record-terraform-deploy.sh` | `harvest --plan <applied plan> --author ... --deploy-ledger ... --code-sha256 ...` | PARTIAL, reported as such: sha fields landed, `last_deployed_commit` did not (row D1-S7). Its own output refuses to claim what it did not check -- "commit-gate checked 0 of 3 file(s) -- NOTHING WAS CHECKED. This line is NOT evidence of a clean gate" and "risk-reflex ANSWER STATE: PARTIAL_OR_BLIND ... could-not-check is NOT checked-clean". Neither is cited as validation anywhere. |
| `content_diff.py` | `--zip <built zip>` | PASS. Re-run standalone so the 5 non-identical members could be read without 389 IDENTICAL lines scrolling them away; the registry arm then enumerated BY NAME rather than inferred from the summary. |
| `comp-schedule` / `comp-iam` | not run -- DECLARED-NOT-APPLICABLE in the order's preflight | Correct as declared and checked against the act: no new cron/alarm/cadence (one redeploy, one invoke of an EXISTING event), and the untargeted plan's single moving resource carries no IAM attribute -- which is the read that would have caught a drift the declaration missed. |

### What failed, and what it cost
- A `python -c` heredoc large enough to write the proof-of-spec instance hit `ENAMETOOLONG: uv_spawn`. Rewrote through
  the Write tool, which is also the rule's own preference for a non-shell writer. Cost: one call.
- A provenance assertion compared a `/c/...`-style path against a `C:/...`-style one and failed on separator form, not
  on substance. Re-ran with `realpath` + `normcase` and added the repo copy as a negative control -- which made the
  check stronger than the one that failed.
- `python` could not open an MSYS `/c/...` path for the rollback hash. Windows path form fixed it. Worth remembering as
  the same family as the `msys_argv_guard` rule.
