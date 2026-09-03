# Session log -- 0.7.0_AE_CloudOps~S -- 2026-09-03 0740-0855Z

**Serial:** `0.7.0_AE_CloudOps~S` (PID 23844) - **Fabric:** site-z - **Branch:** SITEZ
**Project:** NFRA_OPSEC202609 ONLY (Rule 27, one project per instance)
**Task order:** `NFRA_OPSEC202609.TO-OP-S-17-16` (round 1, L7) - **Issuer:** `2.0.0_SA_COO~Z`
**Archetype:** BUILD (new Terraform module, two resources, applied and verified)

---

## Current state

`opal-suspicious-addresses` (DynamoDB) and `opal-data-security` (S3) are **LIVE and verified on
the applied plane**. New module `infra/aws/terraform/opsec/`, applied via `safe-apply`:
**7 added, 0 changed, 0 destroyed**; re-plan reads **"No changes"** (`-detailed-exitcode` rc=0,
run twice, identical). Deploy ledger `opsec-evidence-store-and-address-table` **CLOSED**, all
5 legs proven, sentinel removed.

**The complete flip IS made**, after the issuer corrected one character in the TO face
(`cell_refs` separator, @`beacddcf26`) that had been refusing an otherwise-VALID instance --
row Z-S11. `proof-of-spec-check` returns **VALID rc=0** (alignment-forward-2 2/2; surprises 4 of 4
resolving to channel rows in ENFORCE mode).

## What was done

1. `/watcher` armed (task `btl7n1hxl`, `parent-tied: pid 828625`, watching the canonical nested
   lane inbox `org/mcp/inbox/0.7.0_AE_CloudOps/~S`). `org/XXX.md` Step 1b A-F run in order.
   Step 1b-F confirms this seat's row: **`/watcher` once, ZERO crons, event-driven.** `CronList`
   empty; nothing to cancel.
2. GO 19489 received, opened and **ACKed** (READ on the delivery ledger -- the only clock an
   orphan cannot forge). Status flipped `staged -> pending` by this seat.
3. **The GO's named FIRST ACT -- re-ground every "today" claim at this seat's own vintage.**
   Four premises checked live; three held, three separate ones failed. That work produced four
   surprise rows and is the substance of this session.
4. Module authored, `fmt`/`init`/`validate` rc=0, plan reviewed as exactly 7 creates in no other
   module, ledger opened, `safe-apply`, nine applied-plane reads, fixture exercised and cleaned.

## The four findings (all rows, none a message-only surprise)

| row | class | finding |
|---|---|---|
| **Z-S3** | BLOCKING | The key the PRD/TO call "the estate CMK" (`86cc6c40-...`) is `KeyManager=AWS` -- the AWS-MANAGED `alias/aws/dynamodb` service key, not a CMK. An S3 bucket cannot encrypt with it; the account holds no general-purpose customer-managed key. C-8's SSE-KMS is unsatisfiable as written. |
| **Z-S4** | BLOCKING | Bound (b)'s two bucket-policy principals do not exist: **0 of 216** IAM roles match `admin|cto|terraform` (positive control: 55 match `lambda`); the applier is the IAM **user** `Andrew_Berman`. Writing the deny-outside-list would have denied the applier and **bricked the bucket at creation**. |
| **Z-S5** | BLOCKING | C-8's access-log target `opal-cloudtrail-logs-313476888478` grants only `cloudtrail.amazonaws.com` and has no LogDelivery ACL grant, so the limb needs a change to a bucket this TO does not own -- and its silent-failure mode is invisible to the specified `get-bucket-logging` read. |
| **Z-S11** | BLOCKING | `proof-of-spec-check.py:562` splits `cell_refs` on **comma**; the face declares `cell_refs="OP-s-17 OP-s-16"` **space**-separated, so it reads as one literal id and refuses the instance. |

Each was surfaced as a ROW and, being BLOCKING, also reached the issuer the same turn. **None was
self-resolved** -- every one names a spec decision an L7 worker may not make mid-round (Rule 27,
spec FROZEN). Issuer disarms: 19501 (Z-S3), 19517 (Z-S4), 19532 (Z-S5), plus DISARM RECORD rows
Z-S6..Z-S9. Z-S4 is the one where **building it exactly as written was the wrong act**.

## What went wrong at this seat, and what caught it

- **A false absence, caught by widening.** The compiler mandate's step-2 pattern
  (`opal-organization-trail|access-logs|server_access_logging`) returned no declaration and would
  have fired a spurious STOP and a wrong row. The bucket is named `cloudtrail-logs`, not
  `access-logs`. Widening found it Terraform-declared at `shared-infra/s3.tf:48`. **The corrected
  read, not the first, is what the criterion rests on.**
- **A case-sensitive census.** The first pass over `portal-auth/dynamodb.tf` was case-sensitive;
  the finding only became trustworthy on the `-i` re-run, because this estate capitalises its
  load-bearing words.
- **A directory pathspec staged a 685MB provider binary.** `commit-gate` refused it -- that commit
  could never have been pushed. Fixed by committing explicit file paths, not the module dir.
- **Two ARN rows in `artifacts_produced`** named live AWS resources against a git pin; the checker
  correctly refuted the `(commit, path)` pair. Removed; the live evidence lives on the `.tf` rows.
- **An id collision, twice.** The channel is lane-ANY and other seats appended between this seat's
  read and its write. The append script tests for a duplicate id and **refused rather than
  overwriting** both times; the row was re-filed (S2->S3, S6->S11) and an id correction was sent
  before the wrong id could be quoted.

## Controls actually run (not asserted)

- **Mutant, FIRED-AS-EXPECTED.** S16-AC3's census returns 0 across the module's 6 files. The same
  regex against `infra/aws/terraform` returns **69 hits across 530 files** -- so the zero is a real
  absence, not a dead matcher.
- **Absence-probe positive control.** A row `203.0.113.99/32` was planted, the same `get-item`
  probe rendered it present, then it was deleted -- so the three ABSENT verdicts are real.
- **Version-pair control (S17-AC2).** Both versions read back with **different bodies**; the 64-byte
  v1 surviving the overwrite IS the criterion.
- **Determinism, STABLE.** Two identical `plan -detailed-exitcode` runs, both rc=0.
- **Cross-instrument corroboration.** `comp-blast opal-users-v2` (kuzu estate graph) reports
  KMS_KEY `86cc6c40...`, agreeing with the live `describe-table` -- a **different instrument**, so
  the Z-S3 key identification is not one tool's artifact.
- **UNPROVEN, stated as such.** The sweep showing no estate bucket has access logging enabled has
  **no positive control** (0 of 31 configured), so an empty render and a broken probe are
  indistinguishable there. It is the absence of a counter-example, not evidence.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-read` | `portal-auth/dynamodb.tf --for` then `--enumerate '(?i)kms\|86cc6c40\|...'` | MISMATCH -> opened Z-S3. 1 hit in 238 lines, a COMMENT; zero CMK/SSE/DP declarations in the file the TO names as the source. |
| `comp-read` | `org/XXX.md --for` (Step 1b B-F) | SHAPE + the qualifier that inbox paths are NESTED while agent folders are FLAT. |
| `comp-find` | `'opal-organization-trail\|access-logs\|...' --files infra/aws/terraform` | Wrong pattern, near-miss false absence; corrected by `comp-find 'opal-cloudtrail-logs'` -> `shared-infra/s3.tf:48`. |
| `comp-find` | `'(?i)opal-data-security\|opal-suspicious-addresses' --files infra/aws/terraform` | 0 hits / 524 files -- neither resource previously declared, corroborating the live 404 / ResourceNotFound. |
| `comp-find` | `'(?i)dynamodb:(PutItem\|UpdateItem\|...)'` module vs parent tree | 0/6 files vs **69 hits/530 files** -- the S16-AC3 census and its positive control. |
| `comp-find` | `'cell_refs="[^"]*[ ,][^"]*"' --files org/missions` | 1 hit / 79 files, and it is this face -- why the comma convention was never exercised. |
| `comp-blast` | `comp-blast opal-users-v2` | KMS_KEY `86cc6c40...`, 238 callers; cross-instrument corroboration of Z-S3. |
| `comp-read` | `.tools/proof-of-spec-check.py --enumerate 'cell_refs'` | 7 hits/1127 lines; `:562` splits on comma -> Z-S11. |
| `deploy_ledger.py` | `open` (5 legs) -> `close-leg L1..L5` -> `close` | Opened at deploy-start per NEVER-2, closed only on proven legs. |
| `surprise-row-gate.py` | on every row commit | rc=0; corpus matches the exact legacy baseline (4 known, 0 new, 0 resolved). |
| `proof-of-spec-check.py` | on the instance | 3 violations -> 2 fixed at this seat, 1 (Z-S11) is the face's issuance half and is routed, not self-fixed. |

## Blockers

**NONE now. One existed and was cleared at source during the session.** `proof-of-spec-check.py:562` splits `cell_refs` on a comma;
S1716-AC4 declares `cell_refs="OP-s-17 OP-s-16"` with a space. The instance is otherwise clean
(artifact-resolution 5 resolved / 0 unresolved; surprises 3 of 3 rows resolve in ENFORCE mode).
Routed to `2.0.0_SA_COO~Z` (19538 + the id correction) because `cell_refs` is the TO's **issuance
half** and the assignee does not rewrite the mapping its own work is graded against. The issuer
typed the character at `beacddcf26` (1 insertion / 1 deletion, byte count unchanged, meaning of the
mapping unmoved); the checker then returned **VALID rc=0** and the complete flip followed.

## Push state

**MEASURED, not defaulted.** Commits `d59b3734c3` (rows + status flip) and `cdbdcb473c` (module +
ledger) are **LOCAL** -- `git ls-remote origin SITEZ` read a different head at report time. Push is
the integrator's (`0.0.0_AB_MSTR~Z`); this seat does not push.

## Next

1. DONE -- `cell_refs` corrected by the issuer, `proof-of-spec-check` VALID rc=0, instance committed
   with this seat's own `complete` flip.
2. Deliverable report to `2.0.0_SA_COO~Z` with the nine reads pasted, the module path and reason.
3. `TO-OP-S-8` then activates on the complete flip -- five identity/RBAC tables, five settings,
   **in place**; a plan that would REPLACE any table is a STOP and a row. Re-ground the five at
   their REAL declaration carrier, not the face's named one (the issuer flagged that the demo
   table's carrier claim is false the same way Z-S3's was).
