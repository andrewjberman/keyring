# Session log — 0.7.0_AE_CloudOps~Z — 2026-09-09 1810–1930Z — OPSEC TO-OP-S-12 restore + edge

**Seat:** `0.7.0_AE_CloudOps~Z` · **Face:** `NFRA_OPSEC202609.TO-OP-S-12` (cell OP-s-12, FWD-12)
**Issuer:** `2.0.0_SA_COO~Z` (GO msg 20547) · **Fabric:** site-Z · **Branch:** `ae-cloudops-z-s12-restore`

## What this session was for, and what it turned into

Seated to finish TO-OP-S-12 after the prior instance of this lane died with the face staged. The
face mandates a phase-1 re-grounding before any write and says **STOP on any difference** from its
cut. The re-grounding found one, and the difference was the session.

## The finding (row Z-S153 @`1a7963cc83`)

**The operative half deployed 2026-09-04 was GONE from the box**, and had been for five days.

- On-box, measured on the RUNNING process (one gateway dir; unit ExecStart runs `app.server` from
  it; live pid 552785 cwd=/opt/opal-gateway) — so the bytes measured are the bytes served.
- Resolved to a commit **by content, never by filename** (Rule 22a): `server.py` md5 `56cdab4f…` and
  `oauth_as.py` md5 `405b2d58…` double-match `4c3999de4a`. `405b2d58` is the **pre-S12** oauth byte
  for byte. `log_credential` 0/0/0, `otp/token` 0, `.env` had lost `OTP_BEARER_LABELS`.
- **The causal link is an exact timestamp identity**, which is what makes it a mechanism rather than
  a correlation: the last `gw_cred_observe` record in the lake is `2026-09-04T12:52:29.096470Z` and
  the running process's `ActiveEnterTimestamp` is `Fri 2026-09-04 12:52:29 UTC` — the same second.
  The instrument did not go quiet; it was removed by the restart that emitted that record's own
  successor process.
- Census behind it, full set not a sample: **11,893 objects** across six day-partitions of
  `s3://opal-mcp-audit/audit/`, all fetched, 0 errors, 1,395 `gw_cred_observe`, **none after
  12:52:29Z** — across five days in which the lake kept taking ~1,100 other records daily.

**A second, independent defect on the edge:** `/otp/token` and `/ms/token` appeared in **no ALB
listener rule**, so they fell to the default `forward+authenticate-oidc`. On the wire `POST
/otp/token` → 302 `Server: awselb/2.0` → login.microsoftonline.com, while `/otp/fetch` → 401
`server: uvicorn`. **The Server header is the discriminator**; a status-only read cannot separate
them, since both are "not 200".

**Why a correct proof and an unreachable endpoint coexisted:** the 09-04 proof exercised the
exchange **on-box, via localhost, where the ALB is not in the path.** That proof was true. It simply
could not observe the edge, and no criterion asked it to. A code deploy cannot add a listener rule.

## What was done

1. **Row Z-S153** filed and committed `1a7963cc83` — 28 insertions, **0 deletions**.
2. **Code half restored** — redeployed from HEAD. Verified on the running path: three md5s
   byte-identical to SITEZ `3054872f2b`, `log_credential` def=1 + 5 call sites, `OTP_BEARER_LABELS`
   back. **No lane rewound** — `graph_read.py` present, so NFRA_CLDGRPH shipped forward alongside.
3. **Edge half applied** `7bd89b5d71` — `/otp/token` in place on `otp_capability` (2→3 values);
   `/ms/token` as a **new** rule at priority 33, because `ms_ingest_capability` is at the ALB
   per-rule match-evaluation cap of 5 (verified on the live listener, not read from the comment).
   Apply: **1 added, 1 changed, 0 destroyed.**
4. **S12-AC3 re-exercised through the edge** — the same capability token: **200 at 19:14:26Z, 401 at
   19:19:51Z.** Strictly stronger than the on-box proof it replaces.
5. **Ledger** `opsec-s12-restore-and-edge` opened before the first act with rollback named, CLOSED
   5/5. **Proof-of-spec VALID (rc=0), 0 violations** @`e6ee3e79b8`.

## The number that changes the plan

The observation window's clock **had not started** and could not have. It starts 19:14Z tonight.
Its length is now measured rather than guessed:

| caller | cadence | n |
|---|---|---|
| liveness Lambdas (3, 5) | exact **6.0 h** (median gap 360.0 min) | 24, 25 |
| globgrph derive (4) | nightly, max gap 23.9 h | 9,524 |
| **BD auto-login boxes (1, 2)** | **3 requests in 6 days — ONE burst, 2026-09-08T11:31:34/45/55Z** | 3 of 8 |

One burst yields no inter-arrival estimate, so the honest floor is **longer than the six days
observed**, not the runbook's provisional 48h. And at the ALB layer the two boxes are
**indistinguishable** (one source IP) — which is exactly why the retirement gate reads the
`gw_cred_observe` caller label and not the access log.

## Errors I made and caught

- **A scoped read that would have shipped a false finding.** Checked `log_credential` in `otp.py`
  and `ms_ingest.py` at HEAD, got 0 and 0, and was one sentence from filing "the call sites were
  lost in a merge". An **unscoped** `comp-find` (6 hits / 76 files) put all five in `server.py`.
  The zeros were real; the conclusion would have been false.
- **An append that was a rewrite.** Parse-append-re-serialize reformatted all 152 predecessor rows
  into the diff (**798/771**) on a file whose contract is append-only. Replaced with a textual
  splice: 28/0, predecessors asserted byte-identical.
- **`aws s3 sync` exited 0 having written nothing** — every object failed `[Errno 22]` because the
  S3 keys contain colons, illegal in Windows filenames, and the loop's last command was an `echo`.
  Caught by a census that read 0 files. Replaced with boto3 straight into memory.
- **A clean zero from a matcher written against a format I had not read** — the ALB request field is
  a quoted triple, so `f[12]` is `"POST` and the URL is `f[13]`. First run: 23,092 lines, 0 matches.
  After the fix: 10,261.
- **`curl` status `000` is a connect sentinel, not an HTTP status.** The first static-bearer control
  returned it; re-run rather than interpreted (3× 200).
- **`git stash` was the obvious way to quote AC5's pre-edit baseline** and the shared-worktree gate
  correctly refused it — the stash stack is global even from a linked worktree. Replaced with a
  read-only derivation.

## Instrument gap worth knowing

`safe-ec2-deploy.sh` resolves the **main** tree via `git-common-dir` for the HALT gate;
`safe-apply.sh` does not, so from a linked worktree the gate looks for the session serial in the
worktree, does not find it, and **fails closed**. Since CLAUDE.md 14b and this face both mandate
worktree work, every terraform apply from a worktree hits this. Worked around correctly by pointing
`HALT_GATE_REPO_ROOT` at the main tree — which makes the gate read this seat's **real** inbox, i.e.
strictly more correct, not an override.

## Compiler Tools

| tool | invocation | what it decided |
|---|---|---|
| `comp-find` | `comp-find 'log_credential' infra/aws/ec2/opal-gateway --all --limit 40` | **Prevented a false finding.** Denominator 6 hits / 76 files put all five call sites in `server.py`, correcting a scoped read of the wrong two files. |
| `comp-find` | `comp-find 'TO-OP-S-12' --all --files --limit 60` | 77 hits / 52,650 files recovered the whole prior surface cold — runbook, closed ledger, the 5-caller enumeration. |
| `comp-find` | `comp-find 'aws_lb_listener_rule' infra/aws/terraform/opal-gateway --all --limit 20` | 5 rules across two files — placed the `/ms/token` gap in `ms-ingest.tf` rather than assuming it sat beside `/otp` in `alb.tf`. |
| `comp-read` | `comp-read app/audit.py --for '…gw_cred_observe…'` | 16 qualifiers surfaced the lake write as **best-effort and non-raising** — which is why the gate's presence condition needs its positive control rather than a bare count. |
| `comp-find` | `comp-find 'CAPABILITY_TOKEN_TTL' …` | TTL 300s + the `ttl` override at `oauth_as.py:244` — let AC3 run as a real elapsed-time expiry through the ALB. |

## State at close

- Proof-of-spec **VALID rc=0**, 5 rows: AC1/AC2/AC3/AC5 **PASS**, AC4 **UNCOMPUTABLE-BY-CONSTRUCTION**
  (0 of 5 callers observed; old credential stays; nothing retired).
- Commits `1a7963cc83` (SITEZ), `7bd89b5d71`, `9f76655b9f`, `e6ee3e79b8` (lane branch). **Push state
  LOCAL** — `git ls-remote` reads origin/SITEZ `3054872f2b294f5a0b4e101edd2fe86a18b00526`.
- **Open and named, not silent:** half 2 (two-slot bootstrap rotation) undone — though the accepted
  set is measured live at **2 slots** (`49f cot`) with constant-time no-early-exit matching, so the
  overlap mechanism is exercised in production and rotation is a capability short of demonstration;
  `MS_INGEST_BEARER` is single-slot. Caller migration is **cross-lane for 3 of 5** and remains the
  true critical path on FWD-12.
