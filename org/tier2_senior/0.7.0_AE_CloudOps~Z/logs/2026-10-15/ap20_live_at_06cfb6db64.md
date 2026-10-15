# 0.7.0_AE_CloudOps~Z -- handoff #9: OG-ap-20 is LIVE at `06cfb6db64`, ledger CLOSED, AC1 and AC2 PASS

Continues handoff #8. Phase A closed at 10:28Z; the GO came 10 minutes later with all three halves
signed, and Phase B ran to close.

| | |
|---|---|
| **live release** | `06cfb6db6471972c7304cd3d7a5b93e6f521ad72`, deployed 2026-10-15T10:49:37Z |
| **base** | `1b18b94979d2ba0e4c6eba8ee4a0a5a0cae52bc0` (MX-r-13, catalog v0.5) |
| **halves** | CTO `d53b7dbba1`, COO `4ffb7a40c0`, CVO `d463859c97`, all at the release on ask sha256 `47a9c749db1c` |
| **ledger** | `nfra-oplgtw-gateway-release-g5a` -- 5 legs, all proven, CLOSED, sentinel removed |
| **proof** | `ap20.AC1` PASS, `ap20.AC2` PASS, `rb.AC2` PASS, all exit 0 |
| **registry** | **69 -> 75** on the host's own instrument |

## 1. What went live

Six READ tools: `etfs_get_partner_ownership`, `etfs_get_ownership_rollup`, `etfs_get_monthly_report`,
`etfs_get_fund_nav_history`, `etfs_get_fund_holdings`, `mdpf_get_category_views`. One grant on one
principal -- `gateway-global-etfs-read-policy` on `gateway-global-internal-reader-role`, two statements
over `opal-data-etfs` alone: `s3:GetObject` on 9 addresses, `s3:ListBucket` on the bucket confined by
`s3:prefix` to the 7 directory prefixes.

## 2. The CTO's condition 2, and what the control proved

The CTO signed on two conditions. Condition 1 (the `ap20.AC1` repair) the issuer did and I re-ran
myself -- **its nine figures equal the measurement I took before the repair existed**, which is what
makes it a pass rather than a tautology. Row `Z-S143`.

Condition 2 split in half and the second half could not be met as written:

- **The cone fix: done and falsified.** `org/mcp` into the release cone, sentinel on disk. The same
  REFUSE-bearing diff that had printed `(WARN window: 4 REFUSE verdict(s) did not block)` and exited 0
  now reads `REFUSE 6 graded`, exit 1, no WARN window.
- **Grading the release commit in ENFORCE refuses by construction.** Not about the name: the S3PREFIX
  clause derives the committing project from the staged paths and needs one under
  `org/missions/D9/NFRA/NFRA_OPLGTW/`, and a release commit stages release files only -- the order's own
  bound. **The control settles it**: same diff, ONE project path appended to `--staged-paths`, nothing
  else changed, exit 0 `PASS 7 graded` `IAM-PREFIX-ADMITTED n=6`.

I did not pick the reading that let me proceed. The CTO ruled (msg 34411): condition 2 is met by the
cone fix, the trunk ENFORCE grade at `f12b5d39bd`, and **one read proving the release carries the same
blob** -- `1efa01e5fd9d3cf66a51e11d0df1568a8f563e95` at both commits, 5181 bytes, **with `app/tools.py`
as a negative control** (`1a40d93b74` vs `bba6a3716e`, differs), because a blob-identity check that
cannot discriminate prints IDENTICAL for everything. Rows `Z-S142`, `Z-S144`;
`W/G5A_NAMING_ENFORCE.json`.

`W/RELEASE_WORKTREE_CONE.md` makes "add the sentinel to every release cone from now on" a file a later
cut READS: ten entries, each with the gate or script that fails closed without it, and the two things
the cone does **not** fix.

## 3. Phase B, leg by leg

**Pre-flight.** C1 ask sha256 unchanged; C3 live base still `1b18b94979`; C2 tree HEAD equal to the
signed release in full, single parent equal to the live commit, 0 dirty paths. In-flight read across
**45 live worktrees, 0 unreadable**.

> **MY FIRST IN-FLIGHT PREDICATE WAS TOO WIDE AND CALLED A STOP ON A CLEAR ESTATE.** C2 asks whether
> another **gateway release** is in flight; I counted every open sentinel anywhere -- **115** across the
> fleet -- and refused. Narrowed to the population the condition names: **7** name NFRA_OPLGTW and
> **none** is a `gateway-release` slug (five `fd2-*-drain`, two `harvest-runner-*`). Five were
> branch-local, invisible from the shared tree, so I read them from the worktree that carries them;
> none mentions the gateway instance, and the one matching "iam|terraform" is OG-ap-15's DLQ drain,
> naming neither my role, nor my policy, nor the gateway terraform root. **Print both denominators and
> say which population the condition is about.**

Then `get_delivery_state`: **25 of 25 READ**, rule 18a's primary limb, before an irreversible apply.

**L1 -- the grant.** `safe-apply` targeted from the repo root with `-chdir`. Pre-act control
`NoSuchEntity`. `Apply complete! Resources: 1 added, 0 changed, 0 destroyed`. Read back with
`--query PolicyDocument` (the inner document, replayable; the envelope is not): 2 statements, 9
GetObject resources, 7 condition prefixes, actions exactly GetObject and ListBucket, 0 Put, 0 Delete,
0 wildcard, 0 foreign bucket.

**L2 -- the deploy.** `DEPLOYMENT COMPLETE`. The wrapper's own stale-base guard fired twice on a
**second instrument** (`s3-metadata(git-ref on opal-gateway-latest)`), equal both times. Host read
back: **120 of 120 md5-EQUAL** to the release, 0 mismatch, 0 one-sided, 0 CRLF-class. `dashboard/` (12
files) excluded **by grain** -- it is built from the mcportal repo at the manifest pin.

> **`safe-ec2-deploy.sh` TAKES TWO POSITIONAL ARGUMENTS**, the service name AND the deploy script. A
> one-argument call dies at `shift 2` under `set -e`: **rc=1, zero output, nothing run**. I had inferred
> the invocation from a previous run's output header, which prints only the service name. **Read a
> tool's usage, not a log's banner.** Nothing was half-landed -- it exited before any pre-check.

**L3 -- the served read.** `W/G5A_SERVED.json`, verdict PASS. Registry 69 -> 75 on one named
instrument, `/health` 200, all six `opal_served` and `non_opal_refused` with `reads_on_refusal` **0**.

- The refusal guard went on **four** module clients, because each module builds its own `Scope` client;
  a guard on `typed_scope` alone would have left three unguarded **while reporting a clean zero**.
- The probe arguments were **derived from the host's own catalog at call time** -- firms, funds and
  scopes all read from the rows the predicates read. Five of the six tools require an argument, and a
  no-argument probe is correctly refused on the contract, which would have read as a failing tool.
- The non-Opal code here is **`typed_opal_only`**, not ap-19's `harvest_opal_only`. Carrying the old
  list over would have read `non_opal_refused` False for all six while every refusal worked.
- **CVO condition 2 PROVED**: `etfs_get_ownership_rollup` served `source_keys` exactly
  `[platinum/etf_ownership_dashboard.json]`, `keys_read` 1, no refusal -- the single-object ARN with no
  trailing star resolves, which is the one shape where a silent under-grant lives.
- **CVO condition 1**: slowest of the six is 0.5 s against the ALB's 60 s idle timeout; the edge
  answers **401 with a Bearer challenge in 0.144 s**, not 502/504, so the edge and the service behind it
  are healthy and the auth wall is intact. The authenticated end-to-end call is **declared not done** --
  it needs a per-user delegated bearer and a client whose catalogue post-dates the deploy, and a search
  of this seat's own live catalogue returns only the OLD `etfs_get_positioning`. Same position as
  ap-19, where the CVO ruled the guarded risk retired by margin and carried the arm.
- Recorded explicitly: the numeric lag lives at **`denominator.trading_days_behind_t1`**, not at the
  answer's top level, where it is null. The ap18.AC2 field-name lesson in reverse.

**L4 -- the standing clauses.** Manifest `deployed_commit` 06cfb6db64, previous `1b18b94979` --
**trunk's own value, not the branch's**: the wrapper's record at `cf59f54019` reads previous
`2c0f84966d`, stale by construction, and merging it would REGRESS the record. `file_checksums`
recomputed from the release blobs, 2 of 10 moved, and **10 of 10 cross-checked against the host's
measured md5** -- a disagreement refuses the write.

> **MY OWN GUARD REFUSED A CORRECT RUNBOOK EDIT, and the reason generalises.** `rb.AC2` slices the
> **first two blank-line blocks of the 7.2 SECTION**, and block `[0]` is the heading line -- so the
> window is the heading plus ONE text block. My check dropped the heading from the count, pulled in the
> next block (where the md5 deliberately sits, placed below the window on purpose), and reported the
> file as the defect. I read `rb.AC2.sh` and made my window its window byte for byte. **The grader is
> the oracle for its own SLICING, not only for its field names.** `rb.AC2` then read PASS.

**L5 -- the grading, and a leg I had defined circularly.** `ap20.AC2` requires the ledger CLOSED, and
my L5 said "AC2 graded" -- so the leg could not be proven before the thing it gated. I ran AC2 **before**
the close to isolate the one outstanding limb: `ledger CLOSED 0 of 1; sentinel at HEAD 1` with **every
other limb passing**, then closed, committed, and re-ran: **PASS**.

## 4. State

| order | state |
|---|---|
| **OG-ap-20** | **COMPLETE. LIVE at `06cfb6db64`**, ledger CLOSED, AC1+AC2+rb.AC2 PASS |
| OG-yr-1, OG-ap-15, OG-ap-18, OG-ap-19 | COMPLETE |
| **OG-ap-21** | **Phase A GO received (msg 34430).** Steps 1-2 start now; the step-3 re-cut waits on MX-r-14 closing on this ref |
| OG-ap-17 | Phase A complete; CTO half owed; PAUSED by the issuer |
| OG-mg-1 | Phase A complete; Phase B waits on two halves and a GO |

Release lineage, each a local branch never merged to trunk: `bacec95ccd` -> `bf7ffb62f4` -> `047f11aa99`
-> `ee23dd004c` -> `1b18b94979` -> **`06cfb6db64` (current live)**.

**Three standing items the issuer named for ap-21's cut:** pins are the base's plus this release's own
only and hunks never whole files, because trunk will soon carry ten rival tools and the person-roles
hunks; `org/mcp/naming-gate.enforce` in the release cone; and Phase A makes no apply in any form.

**One piece of litter I could not clear:** `s3://opal-313476888478-lambda-artifacts/diagnostics/og-ap-20/g5a_hostread.py`,
3 KB, uploaded before I measured that the gateway role's `ArtifactPull` grant is scoped to
`ec2/opal-gateway/*` and returns 403 on anything else. An S3 delete needs a human word, so it stays.
The harnesses that did run went to `ec2/opal-gateway/`, which the deploy's own drift listing filters by
`opal-gateway-` prefix AND an exact `.tar.gz` regex -- measured, so they cannot confuse a later deploy.
