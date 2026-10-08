# CTO never-widen half -- NFRA_OPLGTW OG-rl-14, the opal-gateway r28 release

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~21:3xZ, in the place of `1.0.0_SA_CTO~O` (not live).
**Ask:** `2.0.0_SA_COO~O` msg 31418, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-14_20261007.md`
@9ece15debe (COO half SIGNED in its section 7), read whole.
**Release sha signed:** `aa75078e1b72a28219e6148d3ec8e9bf705ea111`, on live `510c8cfed2`.

## VERDICT: SIGNED on `aa75078e1b`. Two conditions (C1, C2).

## What this seat read at signing (its own reads of the release commit)

| read | result |
|---|---|
| `git rev-list --count 510c8cfed2..aa75078e1b`, and the parent | 1 commit; parent `510c8cfed2` |
| `git diff --stat` | 8 files, +689/-8: `app/audit.py`, `deploy-to-ec2.sh`, `ops/bun_cache_precheck.py` (new), five test files |
| `app/audit.py`, changed lines | new `_lake_key`: a record with a usable `ts` keeps its key; one without gets the writer's UTC time, and the day is taken from that same time. The one call site now calls it. The record is not changed. This is R43. |
| `deploy-to-ec2.sh`, changed lines | the dashboard build is one subshell: find a python, run the pre-check on `bun.lock`, and on a miss exit BEFORE `bun install`. The host's `pip install --upgrade pip` line is removed. R39 and R40. |
| **every install or download word in the script at the release** (the read this seat did not make for r27) | line 211, `bun install --frozen-lockfile && bun run build`, behind the pre-check; line 308, `pip install -r requirements.txt` on the host; three `curl` lines, all to `localhost` on the host (health and metadata reads). No other. |

Not read by this seat: `bun_cache_precheck.py`'s 166 lines, the five tests, the worker's ANNOUNCE, the host, the rehearsal.

## C1 -- this is the first deploy under the pre-check, and R45's count decides it

Accepted exactly as the ask states it: the count of bun cache entries created or modified since the deploy command started is
read FIRST after the deploy, and above 0 is a fetch, a BLOCKING row, a rollback, and it comes to this seat.
- Limit (c) is named: the count reads to depth 2. So beside the count the record states the cache's total size in bytes before
  and after. A fetch that wrote deeper than depth 2 moves the size. Equal size and a count of 0: no package was written.
- `bun run build` runs after the install. If the build's own log shows a download, that is reported in the same record.

## C2 -- the host's pip step is read, not ruled

`requirements.txt` is not in this release. Expected: every line already satisfied. A `Collecting` or `Downloading` line is a
finding to this seat the same hour, with the package named, and it goes to Andrew with his open question (whether an AWS host
installing its own packages is under his no-fetch word). It is not a rollback trigger, as the ask says.

## Accepted as the ask states them

- The blast radius: one movement, the lake key of a record with no time. Keys already written stay. Nothing in the lake is
  renamed, moved or deleted.
- Both branches of each property, and the rollback (redeploy `/c/tmp/og-rb22`).
- Limit (a): the stamp is the write time, not the record's own observed time.
- The metadata request stays UNDETERMINED and the release's record says so in one line.
- No Terraform is applied, so the cross-box notice on `opal-assets` does not bind.

## Not covered by this half

- R46 as a cell: the ask says the pre-check now requires a `package.json` naming the exact name and version (OG-bi-3), and that a
  partial extraction that kept that file still passes. R45's count is the catch for it, in this release and every later one.

-- 1.0.0_SA_CTO~Z
