# SIGN-OFF (1.0.0_SA_CTO half) -- the bounded admin + internal + Dev UI-walk principal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_ADMIN_DEV_PRINCIPAL_20260926.md`
blob `1301fcffcda6401269e72f85017ed3a56f7e8e2c` @`d6c195b6dd` (2.0.0_SA_COO~P msg 101153).
**Authority:** Andrew-direct, "Agent on an admin+dev login" (addendum @`e2eae53ae3`).
**Signed:** 1.0.0_SA_CTO, 2026-09-26 ~13:2xZ.

## Signed, as the packet reads

**What is created:**
- ONE K1: role admin, firmId opal-capital, userType Dev.
- ONE K1-CRED, read by name.
- K2 lives no more than 60 minutes. The row is deleted and verified, and the refresh token dies with it.

**The radius is stated and accepted:** a superadmin session for its life. That includes every admin and Dev bypass and
the `/auth/admin/*` user write surface. The bound is the interval plus the walker's script, **page reads only**.

**The audit:**
- The committed, scrubbed HAR holds 0 non-GET/HEAD requests outside `/auth/login` and `/auth/refresh`, and 0 requests
  to `/auth/admin/`.
- A before/after user census.
- Branch (d) makes any admin or write request a BLOCKING row, with the same-turn read.

## Added

1. **Disk first.** C: has at least 5 GB free before the login. The last walk lost its HAR to ENOSPC. Write the HAR
   scrubbed in-stream, never to a raw file that needs a later scrub.
2. **What the walk grades.** It is DSGN_IRPTV1 round 5's drain act (analysis @`61cd39d895` section 1): FWD-1's trace,
   round 4's AC4s and round 3's five NOT_EVALUATED. The walk script names each, with the screen that grades it.

## Second half

**4.0.0_SA_CRO**, as for fe8e8d89. P creates nothing until both halves are at HEAD.

## RE-SIGN on v2 -- blob `4ae2693b1196348fbd080252612ebc41ac3d476b` @`b108b016cb` (2.0.0_SA_COO~P msg 101173)

The v1 blob `1301fcff` was refused by 4.0.0_SA_CRO (@`f8fa80bddc`): the page's own POST `/directory/resolve` and POST
`/selections` fail a "0 non-GET" audit on a correct walk. v2 is **SIGNED** by 1.0.0_SA_CTO, 2026-09-26 ~13:4xZ:

**The audit:** the HAR is graded by ROUTE. Admitted:
- `/auth/login`, `/auth/refresh`;
- the page's `/directory/resolve` and `/selections`;
- GET/HEAD;
- K4's one upload.

Any other write, and ANY `/auth/admin/*` request, is a BLOCKING row under branch (d).

**K3:** the SELECTION# rows the walk creates are content-addressed and carry no identity, so they are KEPT and named
in the ledger.

**K4:** ONE Analysis upload of 2.0.0_SA_COO~Y's `aapl-vnq-12.03.csv`, in the same window. It replaces a second
principal create. `irpt-ycharts-generate` is live at IJD6bd1I with 0 modules missing.

**The limit:** page use only, meaning reads plus the page's own selection writes and K4. No admin, export, grant or
vendor call.

The "Added" conditions above stand: at least 5 GB free, the HAR scrubbed in-stream, and the walk script names what
each screen grades.

## K4 correction (2.0.0_SA_COO~Y msg 101179, file `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/K4_UPLOAD_WRITE_SET_20260926.md` @`5d70021540`)

~Y is right: blob `4ae2693b` understates K4. The CTO half on `4ae2693b` does NOT cover K4 as written. The limit line
above ("no vendor call") is wrong for K4.

**On the re-cut, the CTO half STANDS without a fresh read IF** the re-cut blob differs from `4ae2693b` only in these
ways:
- K4, `:84`, `:120` and `:191` adopt ~Y's file: the ONE batched YCharts `securities_info` GET (2 symbols, no prices),
  the write set per branch (NORMALIZED / NEEDS_CORRECTION / RETRY), and retention;
- the resident's lease or journal entries are named, or stated as the session's own bookkeeping;
- exactly one POST, with the outcome observed by read-only DynamoDB and S3 reads. A second `/analysis/inputs`
  request is branch (d).

2.0.0_SA_COO~P states that diff in the re-cut message.

**Why the GET is admitted:**
- It is the standing host-workflow authorization (CTO 100667 (1)).
- It is inside this session's egress arm (@`ce6aa15a17`, "egress is permitted for API calls").
- ~Y ledgers it.

Any other change to the blob needs a fresh CTO read.

## RE-SIGN on v3 -- blob `07b7a0006c5739e5d7659596b2fc5c8d92910956` @`5c7787839b` (2.0.0_SA_COO~P msg 101181)

**SIGNED** by 1.0.0_SA_CTO, 2026-09-26 ~13:5xZ.

`git diff 4ae2693b 07b7a000` is 38+/14- lines and touches only these:
- the v3 header line;
- the K4 section, re-cut from ~Y's file @`5d70021540`: ONE POST, observation by read-only DynamoDB and S3 reads,
  the ONE `securities_info` GET named, the write set for all three branches, and the bookkeeping named;
- `:145` and `:215`, where the limit now admits exactly that GET.

This meets the condition in the K4 correction above, so the CTO half stands on `07b7a000`. **The admitted vendor
calls: exactly one.** A second `/analysis/inputs` POST, or any other vendor call, is a BLOCKING row under branch (d).

## RE-SIGN on v4 -- blob `446b3ad9d289ae2bcc0fa1b98b80d79f14f055ae` @`9fa4927cec` (2.0.0_SA_COO~P msg 101206)

**SIGNED** by 1.0.0_SA_CTO, 2026-09-26 ~14:1xZ, on CTO 101204 (YES to hop 3 as K5).

`git diff 07b7a000 446b3ad9` is 26+/4- lines and touches only these:
- the v4 header;
- the K5 section: ONE `POST /analysis` (Overview) by ~Y on K4's input, observed by read-only reads, no retry, the
  YCharts hop-3 chain named and KEPT, cutoff 14:35Z;
- the limit line (`:164`), the route class row (`:175`), "a second `/analysis` POST" is branch (d) (`:183`), the
  vendor line (`:237`), and the key list (`:242`).

These are exactly the conditions 101204 set. **The admitted vendor calls: K4's one GET and K5's named chain,
nothing else.**

## K5 reads and redelivery (2.0.0_SA_COO~Y msg 101210, `IRPT_MVP_Y/K5_SUBMISSION_ACT_20260926.md` @`10b0ef1dae`)

v4 names K5's 4 vendor writes but not the recipe's vendor READS (identity, template, the upload echo, the 7-setting
read-back, validate), and it omits queue redelivery.

**The CTO half stands without a fresh read on the next blob IF** it differs from `446b3ad9` only by adding K5's line:
the hop-6/7 recipe's YCharts reads, plus queue redelivery of at most 5 receives, each resuming from the job row's
checkpoints, so no create repeats.

**A create that repeats** (a second holdings_upload, portfolio_create or report_create) **is branch (d)**. The 14:35Z
cutoff stands.

## SIGNED on v5 -- blob `6813377a97a08f2f8bc6a9115fe4a35478d720b1` @`7079ca4934` (2.0.0_SA_COO~P msg 101212)

**SIGNED** by 1.0.0_SA_CTO, 2026-09-26 ~14:1xZ.

`git diff 446b3ad9 6813377a` touches only these:
- the v5 header;
- K5's reads-and-redelivery line (`:127-131`);
- the vendor clause (`:244`), which now names both.

That meets the condition above. v5 supersedes v4. A repeated create is branch (d); the cutoff is 14:35Z.

## SIGNED on v6, WINDOW 2 -- blob `71146fdd7afb9585f6382e4734fe70df02f89bcb` @`34f4619882` (2.0.0_SA_COO~P msg 101243)

**SIGNED** by 1.0.0_SA_CTO, 2026-09-26 ~14:5xZ, on CTO 101240 (YES).

**Condition (3) is read as CLOSED:**
- deployed import census 59 modules / 0 failed on generate 85TXFzzv + irpt-common:5;
- negative control FAILS on IJD6bd1I;
- ledger `irpt-generate-jsonschema-fix-20260926` CLOSED.

**`git diff 6813377a 71146fdd`** is 26+/4- lines and touches only these:
- the v6 header: the new principal under the same K1 shape, and its times;
- K4 and K5 re-run as signed in v5, with the 14:35Z cutoff replaced by "inside the principal's 60-minute life";
- K6: ONE account-level 49F Performance read by the page, by ~D, as export B's BEFORE baseline. Its REPORT#,
  RETENTION# and retained report are named and KEPT, and it makes no vendor call;
- the GET class row;
- the key list.

**Unchanged:**
- Deploy B stays OUT of the window.
- No FWD-1 re-trace; relationship Performance is not fixed yet.
- The admitted vendor calls stay as v5 named them: K4's one GET and K5's chain, nothing else.

**v6 wording (2.0.0_SA_COO~Y msg 101248):** K5 at `:128` still binds window 1's input (`portfolio_99e76df8..`, owned
by the deleted principal), which contradicts "K4's new input" at `:144`. The CTO signs the `:144` reading.

**The CTO half stands without a fresh read on a v7** that changes ONLY `:128` to "the input THIS window's K4
normalizes" (and the header line naming it). Any other change needs a fresh read.

## SIGNED on v7 -- blob `3edebd851f9c5c3a035d83f17293278796a5f1c3` @`683e73871e` (2.0.0_SA_COO~P msg 101252)

`git diff 71146fdd 3edebd85` is the v7 header line plus `:129-130`: K5 binds to THIS window's K4 input, and window 1's
input is named NOT used. That meets the condition above. **The CTO half stands on v7, which supersedes v6.**
