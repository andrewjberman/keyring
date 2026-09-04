# Session log -- 0.7.0_AE_CloudOps~S -- 2026-09-03 1140-1230Z (TO-OP-S-25-26-27, ROUND 2)

**Serial:** `0.7.0_AE_CloudOps~S` (PID 23844) - **Fabric:** site-z - **Branch:** SITEZ
**Project:** NFRA_OPSEC202609 ONLY (Rule 27) - **Task order:** `NFRA_OPSEC202609.TO-OP-S-25-26-27`
**Issuer:** `2.0.0_SA_COO~Z` (GO 19669) - **Archetype:** BUILD (three new resources + one uncomment)
**Round 1 on this seat:** TO-OP-S-17-16 @`f9b2a16c2c` and TO-OP-S-8 @`2da0c78f6a`, both ACCEPTED.

---

## Current state

**Built and verified.** This round builds the three referents round 1 could not name -- each one a
row this seat filed *before* a write, each ruled at L4:

| cell | resource | the round-1 row it answers |
|---|---|---|
| OP-s-25 | `alias/opal-security` -> key `64f25291-4015-42c5-ad41-40e42325deb7`, **KeyManager=CUSTOMER**, rotation true | **Z-S3** -- "the estate CMK" was the AWS-*managed* `aws/dynamodb` key |
| OP-s-26 | role `opal-security-admin`, trust = **one** principal, assume-role **exercised** | **Z-S4** -- neither named principal existed |
| OP-s-27 | bucket `opal-data-security-access-logs` + the logging uncomment | **Z-S5** -- the CloudTrail bucket cannot receive |

Instance **VALID rc=0** with the seven expected ids. Ledger `opsec-r2-key-role-logs-target`: L1 L2
L3 L4 L6 CLOSED, **L5 OPEN BY DESIGN** inside its 24h window.

**The complete flip is NOT made**, and that is the criterion's own instruction, not a stall --
S27-AC2 says the flip waits on a delivered log object or on the 24h statement, nothing else.

## What was verified, and what could have failed

- **The key.** `KeyManager=CUSTOMER` is the discriminating read: the thing round 1 was told to use
  reads `AWS`. Policy = exactly 3 statements; **2 of 2 explicitly-named principals exist**.
- **One key, not two**, agreed by three independent counts: alias count 1; account CUSTOMER census
  4 -> 5; source declaration census 1 of 9 files. Pagination checked -- `NextMarker` absent, so 20
  and 21 are totals, not page sizes.
- **The trust, exercised.** `sts assume-role` succeeded. The **negative control** -- a *different*
  existing role on `sts:AssumeRole` -- read `implicitDeny`, run as its own invocation because two
  `--resource-arns` in one call silently flip held results and would have manufactured the answer.
- **Never-widen, proven by re-reading.** `opal-cloudtrail-logs-313476888478` still reads exactly its
  two CloudTrail statements, no `logging.s3` principal. Satisfying C-15 by widening that bucket was
  the tempting wrong answer round 1 refused; this read proves it was still refused.
- **Ordering as a control.** The target and its policy applied FIRST, the source's logging block
  SECOND, with a `depends_on` so a future plan cannot reorder them. `PutBucketLogging` **succeeded**,
  which means S3 accepted the target's permissions rather than taking a dead configuration --
  suggestive, and deliberately *not* offered as the criterion.

## Three findings, all from running the gate rather than reading the face

- **Z-S27** -- S26-AC2's census ("the diff reads 0 occurrences of the user ARN") and the same face's
  DELIVERABLE 2 ("TRUST POLICY = ONE principal, `...:user/Andrew_Berman`") are mutually exclusive: a
  role cannot trust a principal it does not name. Measured and banded: **3 occurrences = 2 comments
  + 1 mandated trust line + ZERO in any grant.** The substance holds; the literal wording cannot.
- **Z-S29** -- S27-AC2 prescribes status `UNCOMPUTABLE-BY-TIME`, which is **not a schema enum member**;
  the checker refuses the instance on it. Exercised: INVALID rc=1, then VALID rc=0 after moving to
  `UNCOMPUTABLE` with the qualifier in `status_reason`. The schema was **not** edited -- widening a
  ratified estate contract is not an assignee's act.
- Both are OBSERVATION/ARMED and left to the issuer. Grading either against the reading I happen to
  prefer, silently, would be the assignee choosing its own acceptance test.

**The pattern worth naming:** this is the third face-vs-tooling mismatch on this project after
Z-S11's `cell_refs`, and all three share a shape -- *a face prescribing something the gate will not
accept, discoverable only by running the gate.* The round-2 cut rule (one live read per named
referent) closed the class where a face names a thing that does not exist; the sibling rule this
suggests is that a face prescribing a **value** should have that value checked against the schema
that will grade it.

## What I got wrong, and what caught it

- **A dropped character in a row id.** My substitution produced `NFRA_OPSEC202609-Z-27` (no `S`).
  Caught before the commit by re-validating every id in the channel against the required form, then
  repaired to `-Z-S27`. A malformed id would have broken the surprises-to-row resolution silently.
- **A citation to a row that did not exist.** The instance cited `Z-S28`; the next free id was
  actually **S29**. Corrected before commit -- a dangling citation is exactly what the surprises limb
  exists to catch.
- **`git checkout` failed and my echo said it succeeded.** An `index.lock` from a concurrent seat
  made the revert a no-op while the message printed anyway. Caught by re-reading the diff; redone
  with an index-free restore (`git show HEAD:path` written straight to the worktree), and the lock
  was **not** deleted -- it may belong to a live peer.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `terraform plan` (unscoped baseline) | before any edit, the named first act | "No changes" rc=0 -- 0/0/0. Not a foregone conclusion: a peer had edited this module's `s3.tf` for OP-s-5 since round 1. |
| `aws sts/kms/iam/s3api` | phase-1 referent re-reads, each with its control | **All five agree** with the face's 11:3xZ line at my 11:44:34Z vintage -> no row, proceed. |
| `comp-find` | `'aws_kms_key' --files infra/aws/terraform` | 46 hits/539 files; idiom read at `nfra-agentbus/kms.tf` and followed for statement (a). |
| `comp-read` | `--enumerate ':user/'` per module file | The banded census behind Z-S27. The banding *is* the finding -- an unbanded count settles nothing. |
| `simulate-principal-policy` | one `--resource-arns`, separate invocation | `implicitDeny` -- the negative control S26-AC1 requires. |
| `deploy_ledger.py` | open (6 legs, 24h) -> close L1 L2 L3 L4 L6 | L5 left OPEN BY DESIGN, which is what S27-AC2 prescribes rather than a stranded leg. |
| `proof-of-spec-check.py` | with the seven expected ids | INVALID rc=1 on the status enum -> VALID rc=0 after the Z-S29 fix. |
| `surprise-row-gate.py` | on each row, committed ALONE per the bound | rc=0 each time; corpus matches the exact legacy baseline. |

## Blockers

**NONE.** One item is outstanding and it is a designed wait, not a block: S27-AC2's delivered log
object. Read at 12:15:42Z, 17 minutes after the logging apply, the prefix is empty -- far inside S3's
best-effort delivery latency. Ledger leg L5 holds it inside a 24h window.

## Next

1. **Re-read `opal-data-security-access-logs/evidence-store/`** for a delivered object. On a real
   object: S27-AC2 -> PASS, close L5, flip complete, report. If still empty at 24h: file the timed
   statement, close L5 on it, and flip on that -- the criterion allows exactly those two exits.
2. Deliverable report to `2.0.0_SA_COO~Z` with every read pasted.
3. **NOT started, correctly:** the key flips (OP-s-16/OP-s-17) and the demo import are the NEXT task
   order, dispatched on this key's APPLIED read rather than on this face's complete flip.
