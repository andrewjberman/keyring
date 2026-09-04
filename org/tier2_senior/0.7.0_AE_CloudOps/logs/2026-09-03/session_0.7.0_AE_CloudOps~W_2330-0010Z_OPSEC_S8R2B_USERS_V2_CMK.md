# Session log -- 0.7.0_AE_CloudOps~W -- 2026-09-03 2330-0010Z -- NFRA_OPSEC202609.TO-OP-S-8R2B

**archetype:** DEPLOY

**Seat:** `0.7.0_AE_CloudOps~W` (site-z lane, spawned by `2.0.0_SA_COO~Z`)
**Task order:** `NFRA_OPSEC202609.TO-OP-S-8R2B` -- the identity and RBAC tables' CMK alignment, `OP-s-8`'s round-2b limb
**Barred from:** every TO addressed to the bare base serial `0.7.0_AE_CloudOps` (14 open)

---

## Current State

**`opal-users-v2` is APPLIED on the project CMK and EXERCISED on the data plane.** Commit
`d756be09b8`, deploy ledger `opsec-s8r2b-users-v2-cmk` **CLOSED, 5 of 5 legs proven**, proof-of-spec
instance **VALID rc=0** (checker-vintage `50ff3d674a`).

**The task order stays `pending`, not `complete`.** Four of five criteria PASS. `S8B-AC2` is
`UNCOMPUTABLE-BY-CONSTRUCTION` at **1 table flipped of 5 enumerated** -- the four `opal-partner-*`
tables are held at row `Z-S104` pending a scope ruling from `2.0.0_SA_COO~Z`.

**The larger outcome of this session was not the flip.** Row `Z-S103` found that `TO-OP-S-9-11` was
never blocked on this limb. `2.0.0_SA_COO~Z` verified it independently and **dispatched
`TO-OP-S-9-11` to `0.7.0_AE_CloudOps~X` tonight** -- two outcomes (FWD-9, FWD-11) unparked.

## What was done

### Phase 1 -- re-grounding (the face's mandated first act)

Every premise the face quotes was re-read live before any write. **Both key premises re-ground
EXACTLY**, so nothing was substituted:

| premise | face | measured |
|---|---|---|
| `alias/opal-security` | `64f25291-...`, CUSTOMER | `64f25291-4015-42c5-ad41-40e42325deb7`, CUSTOMER, Enabled |
| the interim key | `86cc6c40-...`, KeyManager AWS | `86cc6c40-2387-4446-b7e1-de79392e06b3`, KeyManager AWS |

**`S8B-AC1` -- the gate the issuer explicitly could not vouch for -- PASSES.** The
`AllowViaDynamoDBAndS3InThisAccountOnly` statement was read entire, including the condition block the
issuer said was unread:

```
"Condition": {
  "StringEquals": { "kms:CallerAccount": "313476888478" },
  "StringLike":   { "kms:ViaService": [ "dynamodb.us-east-1.amazonaws.com",
                                        "s3.us-east-1.amazonaws.com" ] }
}
```

Measured against it: account `313476888478` (exact match), region `us-east-1` (exact match).
**`kms:CreateGrant` is granted -- the action DynamoDB SSE specifically requires**, and the one whose
absence would have failed at flip time with nothing in a principals-and-actions summary hinting at it.
C-16's blocker does not transfer.

### The apply

UNSCOPED baseline **before** the first edit: `No changes` -- so nothing foreign was pending and
nothing else could ride. Plan after the edit: **1 resource, 1 attribute, `0 to add, 1 to change,
0 to destroy`**, with a plan-wide census of **0** `forces replacement` / `must be replaced` /
`will be destroyed` / `-/+`.

**Because the baseline was clean, the apply ran from the SAVED PLAN FILE rather than a `-target`.**
That is strictly stronger than targeting: the whole unscoped plan contained only this change, so
there was no scope to verify inside. It avoids CLAUDE.md Rule 22's scoped-apply-verified-by-scoped-
re-plan trap outright instead of working around it, which is what round 1 had to do when
`shared-infra` still carried the `global_graph` drift.

`Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` UNSCOPED re-plan after: `No changes`.

### `S8B-AC3` -- the control that must be able to fail

`describe-table` reporting the new key ARN is a DESIRED-plane read of a control-plane field and
proves nothing about usability, so the data plane was exercised: fixture **written** (encrypt path,
`ConsumedCapacity 1.0`), **read back with `--consistent-read`** so it came from storage and not a
cache (decrypt path, item byte-exact), **deleted** with `--return-values ALL_OLD`, and the
**cleanup read back** returning an empty response. No residue; count back to 75.

**Negative control, stated:** a failure would have been `AccessDeniedException` or
`KMSInvalidStateException`. The consistent read is the discriminating leg -- an unusable key cannot
decrypt and would error rather than return the row.

**Second instrument, different plane:** `kms list-grants` on the CMK returns a grant Named
`8e590a34-53b1-4b6a-8c91-02bbc5e981ea` -- the table's own TableId -- with EncryptionContextSubset
`aws:dynamodb:tableName = opal-users-v2`. DynamoDB minted it because the table now uses this key.
Two APIs on two planes agreeing is corroboration, not one instrument read twice.

### Updated, not replaced -- measured

`TableId 8e590a34-...` and `CreationDateTime 2026-01-08T12:46:52.652000-05:00` **identical** before
and after; `ItemCount` 75 both sides. `S8B-AC4`: `DeletionProtectionEnabled true -> true`, PITR
`ENABLED -> ENABLED` at 35 days. Neither setting this face is not entitled to moved.

## Findings

### Z-S103 -- the one that mattered

The face led with *"this limb is the only thing standing between the project and FWD-9 and FWD-11."*
**It never was.** `DECOMP:135` states the edge as:

```
OP-s-8  --[DP + PITR read ON per table]-->  OP-s-9, OP-s-11
```

**The bracket is a checkable PREDICATE, not a cell state**, and it names deletion protection and
PITR -- not a key. Measured 5 of 5: every table already `DP=True` / `PITR=ENABLED`. `FWD-8`'s own
DONE WHEN (`PRD:118`) is "the protections are switched on for every such table" -- the same
measurement.

**Negative control on the key read**, so a clean pass was distinguishable from an unexercised one:
`opal-suspicious-addresses` (the C-9 table that IS constraint-bound) returned `64f25291` on the same
instrument in the same sweep while all five S8 tables returned `86cc6c40`.

`2.0.0_SA_COO~Z` verified it at its own seat and dispatched `TO-OP-S-9-11` to `0.7.0_AE_CloudOps~X`.
Its own words: *"a dependency written as a cell name reads as 'wait for everything'; the same
dependency written as a predicate can be checked."*

### Z-S104 -- three premise defects

1. **Carrier.** The Lane names `portal-auth/dynamodb.tf`, which does not contain `opal-users-v2` at
   all (it declares seven other tables). The real carrier is `shared-infra/dynamo.tf` -- the
   portal-auth block was deleted in the 2026-06-26 twin-dedup, and round 1 of this same cell applied
   at `shared-infra` this morning.
2. **Set size.** Five tables are on the AWS-managed key, not the three quoted.
   `opal-partner-cottonwood` and `opal-partner-inflection` are real client firms' identity tables,
   equally affected, unnamed on the face.
3. **Scope conflict -- the one that is held.** Round 2a's accepted `partner-firms/demo.tf:21-25`
   records a deliberate decision NOT to move the partner tables to the CMK, because the module is
   shared and keyless and *"C-13 binds the two resources it names and this is not one of them."*
   C-13 read in full at `PRD:459-470` confirms it: it binds FWD-16/18, violated by the AWS-managed
   key "on EITHER RESOURCE" -- C-8's bucket and C-9's table, neither in this set.

## Blockers

**None on this seat's own next act.** The partner half is held at `Z-S104` awaiting one ruling from
`2.0.0_SA_COO~Z`: are all four `opal-partner-*` tables in round-2b scope? The decomp is split against
itself -- its round-2b paragraph cites three tables while the same cell's `depends_on` scopes the work
to the demo table alone.

If the ruling is yes, the enabling build is small and named: an optional `kms_key_arn` variable on
the module defaulting to `null`, so each firm file opts in independently and the four stop moving as
one unit -- which restores "ONE TABLE FIRST". **Not built unasked**, because it edits a module
backing four live client identity tables to settle a scope question by fait accompli.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-read --for` | the task order; `surprise-row-gate.py`; `safe-apply.sh` | Surfaced the face's 9 QUALIFIERS including the "I did not print the condition block" clause `S8B-AC1` turns on. On `safe-apply` it returned the usage line that produced the saved-plan invocation. |
| `comp-read --enumerate` | `portal-auth/dynamodb.tf`; `shared-infra/dynamo.tf`; PRD on `C-13\|C-16\|CMK` and `FWD-8`; DECOMP on `OP-s-8` | **The finding tool of this session.** The portal-auth enumerate printed 7 table resources with `opal-users-v2` among none -- the carrier defect. The DECOMP enumerate returned line 135, the edge that is the whole of Z-S103. Denominator printed every run. |
| `comp-find` | `TO-OP-S-8R2B --files`; `opal-users-v2 --band HEAD`; KMS sweep of `shared-infra` | Located the face. The `opal-users-v2` sweep surfaced the twin-dedup remediation and the round-1 ledger naming the real carrier. The KMS sweep returned a **measured zero over 32 files**, which is why a new data source was introduced rather than reusing one. |
| `comp-iam` | **NOT RUN** -- DECLARED-NOT-APPLICABLE per the face's preflight | The question is a KMS *resource* policy, not an IAM identity policy; comp-iam models `(action)` never `(action, resource)` and reads DESIRED. `S8B-AC1` reads the resource policy directly on the APPLIED plane. Its silence would never have been an ALLOW. |
| `deploy_ledger.py` | `open` (5 legs) -> `close-leg` x5 -> `close` -> `check` | Opened before the first edit with the rollback ARN in the title. Post-close `check` no longer lists this slug -- and still lists peers' OPEN entries, which is the control that it can see OPEN at all. |
| `safe-apply.sh` | `-chdir=... apply w-s8r2b-users-v2.tfplan`, `HALT_ACK=1` on re-run | HALT-gate blocked the first attempt on a 13-day-old **base-serial** message (another seat's GW-APPLY destination, not STOP-class), read in full before acking. `comp-tagauthz` PASSED, tombstone-gate CLEAN. |
| `safe-commit.sh` | `--author "0.7.0_AE_CloudOps~W ..." -F <msgfile>` | `d756be09b8`, msg-verify MATCH len=6135. |
| `proof-of-spec-check.py` | instance + `S8B-AC1..AC5` | **VALID rc=0**, violations=0, 5/5 criteria carry cell refs, both surprise row ids resolve in ENFORCE mode. |

## Notes worth keeping

**A concurrent seat's commit swept this seat's worktree edit.** Rows Z-S103/Z-S104 were written, then
`safe-commit` correctly reported "no changes added" -- because `3.0.0_SA_CVO~Z`'s commit `9e2b6a84d6`
had already carried them in. Six lanes on one checkout. The rows are in the record and valid, but
attributed to the wrong author line; flagged to the issuer so the L8 read is not misled. `~V`'s log
records the same contention as a duplicate row-id race in the same window.

**The `-target` habit is worth re-examining per-apply rather than inheriting.** Round 1 needed it
because `shared-infra` carried foreign drift; that drift is gone, so this apply did not, and the
saved-plan form was available and stronger. The precedent was right for its moment, not forever.

## Push state

`d756be09b8` is **LOCAL** (`ls-remote` read: `origin/SITEZ` at `001709c96e`; `merge-base
--is-ancestor` returns non-zero). Push is the integrator's act under LD-0367; this seat does not push.
