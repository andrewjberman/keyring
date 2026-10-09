# 0.7.0_AE_CloudOps~TV2 -- session: lane bring-up and the SA-r-1 FWD-1 seat-arm run

**archetype:** MIXED

Lane `0.7.0_AE_CloudOps~TV2`, seated on dell2 for TCKT_VNEXT only (MSTR msg 3206), branch `box/dell2`,
workspace root `C:/dev/ajb_workspace`.

## Current State

Brought the lane up from nothing: registered LIVE (PID 22688), armed the inbox Monitor and re-armed it on
every `[WATCHER-EXPIRED]` line, wrote the session serial file, ran the audit-archive invoker (18 findings,
all owned by the exec startup path -- not re-filed), confirmed 101 of 102 comp-tools resolve bare with a
forwarder exercised live, wired the owned-paths hook and the comp context. Zero crons, per the launch table.

Held idle through five quiet windows, then measured that the quiet was real rather than deafness: the
watcher's own line names `org/mcp/inbox/0.7.0_AE_CloudOps/~TV2`, the canonical NESTED lane path, and the dead
flat form `inbox/0.7.0_AE_CloudOps~TV2` does not exist (LD-0202).

`TCKT_VNEXT.TO-RUN-SA-r-1` arrived as a FILE at 13:38Z with no broker message, which is the spine's
files-not-messages discipline; a re-measure found it (`to-check` 1 ACTIVE) where the 11:33Z census had
correctly read zero. GO at 15:03Z (msg 3535) cited the order at `@104bc493ed`, a NEWER commit than the staged
bytes with a GO block the staged version lacked, so the order was re-read at current bytes before acting.

**The run (WORLD risk, one pass, complete):**

- **AC1 PASSED.** `reread_27.py` printed `READ27 27/27` rc 0 at 15:08Z. `irpt-status` LastModified
  12:45:28Z -- unmoved since 14:5xZ, so the GO's condition-(1) re-run is satisfied by that invocation.
- **Deployed bytes resolved by CONTENT, never by filename.** `_authz/served.py` at pin `74a62fb46c` hashes to
  `87d9ecc4`, the deployed member on all 7 IRPT hosts, with `HEAD` = `ada9bf5b` as the negative control. The
  409-vs-390 delta is only the IB-pr-405 additive (`SVC_CUSTODY_STATEMENT_OPERATIONS` gains
  `analysis-request-read`), a different subject from this filer. `ticket_center/lambda_function.py` local
  bytes equal the deployed R13 `67068626`.
- **Step 4's one-firm proof ran BEFORE any hop**, the CTO half's condition. Over 27 clamped routes
  (21 IRPT + 6 ticket-api): **22 of 22 EXERCISED arms refused `cottonwood`, 0 admits.** All 21 IRPT routes
  returned `public_reason_code FIRM_BINDING`; `GET /api/scoped/tickets` returned 8 tickets whose distinct
  requester firms are `['49financial']` only.
- **5 ticket-api arms recorded NOT_EXERCISED, not as refusals.** Their gate is
  `_in_profile_scope(actor, ticket.requester.firm)`, keyed on a DynamoDB read, and takes no
  `selected_tenant`; a synthetic id refuses at `cur is None`, a NOT-FOUND byte-identical to a clamp refusal.
  Counting it would be ABSENT read as EXERCISED-AGAINST (rule 22a). Acquiring a cottonwood ticket id to
  exercise it properly is another firm's data and out of bounds.
- **Instrument control held.** The own-firm arms returned varied codes (`NOT_FOUND`, `INVALID_INPUT`,
  `OBJECT_NOT_COVERED`, `None`), not a uniform 401, so the clamp was genuinely reached. This control mattered
  because this principal is DENIED on `opal/auth/jwt-public-key`, so the private/public key pair could not be
  compared directly and the live calls were the only available control.
- **STOP met at step 4:** `GET /api/scoped/data-refresh/history` admitted the filer at **HTTP 200**. Per the
  order no hop ran, and the run went straight to cleanup.
- **Cleanup, same session:** filer row deleted, ConsistentRead read-back **ABSENT**. No ticket existed to
  complete, recorded as `NO_TICKET_CREATED` rather than as a pass. Token left to expire 17:40:57Z.
- No IAM change, no code change, no route change. Every call went over HTTPS through the real CloudFront host
  `d2n2nzpeqf34ge.cloudfront.net`; a direct `lambda invoke` was deliberately NOT used, because the CTO's
  IRPT_YCDGEN ruling `@d54e0b7515` condition 1 says a crafted-context invoke proves one hop and does not
  count. The predecessor lane's script used exactly that pattern and was not copied.

**Two findings, both surfaced before they cost a run:**

1. **Hop (b) was impossible under pair v2.1** -- found from deployed bytes BEFORE minting, reported as
   INFERRED rather than asserted (msg 3584), then confirmed by the issuer in code as row
   `TCKT_VNEXT-D2-S15`. `_create_firm_allowed` requires the firm in BOTH the token's authorizer-derived
   `allowedFirmIds` and the PROFILE row's scope, and v2.1 makes them disjoint (`{opal-capital}` vs
   `{49financial}`). Order amendment n=1 followed; the run's own STOP had already reached that outcome
   independently.
2. **Row `TCKT_VNEXT-D2-S16`, filed by this seat.** W6-S2's routed fix is LIVE and is *why* the pair's
   data-refresh arm cannot be met: `validate_user_type` admits `'Dev'` OR an Opal-internal principal, and
   `_is_opal_internal` is true on `tier == 'internal'` (`OPAL_INTERNAL_TIER`, :138/:161) OR
   `firmId == 'opal-capital'`. The filer must carry `firmId opal-capital` for the ticket service to class it
   INTERNAL, so it is admitted as Opal-internal and `userType` is never consulted. The admit also *proves*
   the fix is deployed: the pre-fix gate refused a non-empty non-Dev `userType`, and `'test-filer'` was
   admitted. Critically, pair **v2.2 does not close this** -- its internal-tier token satisfies the first limb
   directly -- so SA-r-1b would have stopped at step 4 exactly as SA-r-1 did. Raised before minting
   (msg 3607); the COO put the arm to the CTO and issued a HOLD (msg 3612).

## Blockers

**`TCKT_VNEXT.TO-RUN-SA-r-1b` is HELD before minting** on the CTO's ruling for the data-refresh arm
(COO msg 3612). Owner: `1.0.0_SA_CTO~DELL2` via `2.0.0_SA_COO~V2`. This seat does not chase it and builds
nothing on it. Not a blocked seat -- a held order is not a blocked one.

One structural note, not a blocker: the order names the trace path
`deliverables/2.0.0_SA_COO~V2/R1_RUN/sa_r1_trace.json`, which `owned-paths-validate.py` clause 4 refuses to
this lane. The file was written there as ordered and an identical copy (same sha256) was committed under this
seat's own deliverables; `2.0.0_SA_COO~V2` commits the ordered path itself (msg 3612). Authorship was NOT
overridden to get around the gate.

## Next Steps

1. `[1.0.0_SA_CTO~DELL2 via 2.0.0_SA_COO~V2]` Rule the data-refresh arm for pair v2.2. Until it lands,
   SA-r-1b does not mint.
2. `[0.7.0_AE_CloudOps~TV2]` On that ruling: re-read the order at current bytes, open a fresh NEVER-2 ledger,
   STOP 1, then step 4's **widened** census -- every `/api/scoped` route enumerated from the authorizer's
   route list and each host's route table, denominator PRINTED (117 at `@41b7e28bdf`; a different live count
   is itself a finding to print).
3. `[0.7.0_AE_CloudOps~TV2]` Event-driven otherwise: act on each `[INBOX]` event the same turn and re-arm the
   Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `comp-find 'TV2' --band HEAD --limit 40` | 226 hits / 76,942 files; found the seating message that identified TCKT_VNEXT as the scope |
| `comp-find` | `comp-find 'issued_to.*TV2' --band HEAD` | measured 0 across 76,941 files -- one of three agreeing reads that the lane held zero orders at 11:33Z |
| `comp-find` | `comp-find --name 'index.mjs' infra/aws` | 8 of 9,202; located `portal-authorizer/index.mjs` |
| `comp-find` | `comp-find 'Ticker,Dollars\|Ticker,Shares\|Symbol,Dollars'` | 100 hits; found the committed holdings fixture `aapl-vnq-12.03.csv` (35 B, sha256 `bb079cbf...`) |
| `to-check.py` | `--all --assignee 0.7.0_AE_CloudOps~TV2` | 0 active at 11:33Z, then 1 ACTIVE at 14:59Z -- the re-measure that caught the staged order |
| `sequence-check.py` | `--project TCKT_VNEXT` | UNPLACED: a register project the sequence does not list, so D7's own rules govern |
| `commit-gate.sh` | on `sa_r1_run.py` | All checks passed (py_compile + ds-precommit + ruff py39) |
| `deploy_ledger.py` | `open` / `close-leg` x4 / `close` | ledger `tckt-vnext-sa-r1-fwd1-seat-arm-20261009` CLOSED, 4 legs proven |
| `reread_27.py` | per AC1 | `READ27 27/27` rc 0 |
| `safe-commit.sh` | the run record | `e652ac4d3e`, 5 files |
| `aws` shim | `lambda get-function`, `dynamodb describe-table/put-item/get-item/delete-item`, `secretsmanager get-secret-value`, `lambda get-function-configuration` | all read/wrote as expected; `get-secret-value` on `opal/auth/jwt-public-key` AccessDenied |

**What failed, and what it taught.** `safe-commit` refused the trace at the ordered path on an owned-paths
lane violation -- the right refusal, and the fix was a copy under an owned path, never an authorship
override. The `to-pipeline-gate` then refused the `complete` flip with no proof-of-spec instance beside it;
I had judged the instance unnecessary because step 7 names the report as the deliverable, and the gate was
right where that judgment was wrong. The comp rail denied three piped census calls (F4) and each denial's
RUN NEXT line was the command that answered.

**Gap.** `comp-iam` was DECLARED-NOT-APPLICABLE by the order's preflight and was not run; no IAM changed.
