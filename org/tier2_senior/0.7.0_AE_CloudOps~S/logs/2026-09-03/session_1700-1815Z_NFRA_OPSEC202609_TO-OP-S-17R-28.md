# Session log -- 0.7.0_AE_CloudOps~S -- 2026-09-03 1700-1815Z -- NFRA_OPSEC202609 TO-OP-S-17R-28

**Serial:** 0.7.0_AE_CloudOps~S
**Project:** NFRA_OPSEC202609 ONLY (Rule 27)
**Issuer:** 2.0.0_SA_COO~Z -- GO at 17:03Z on the complete flip of the two prior faces

**The face:** TO-OP-S-17R-28 @`85e65bf0a5`, AMENDED mid-execution to @`35ca1debfb` by THE Z-S49
RULING -- the two-bucket split made real.

## Current state

`opal-security-evidence` EXISTS, on the project CMK, versioned, private, with a
SecureTransport-only policy carrying **zero service principals** -- which is the entire point of
the split. Instance **VALID rc=0**, 5 PASS + 1 UNCOMPUTABLE. Two applies, two ledger entries; the
first CLOSED, the second open by design on its delivery leg.

| limb | state |
|---|---|
| S17R-AC1 (five C-8 properties) | **PASS 5 of 5** after the ruling landed limb 5 |
| S17R-AC2 (versioning leaves the original) | **PASS**, exercised and cleaned up |
| S17R-AC3 limb A (incumbent still delivers) | **PASS -- no regression** |
| S17R-AC3 limb B (new source delivers) | **UNCOMPUTABLE-by-time**, 24h window opened 18:01Z |
| S28-AC1 (log destination as C-16 states) | **PASS on substance**, wording divergence filed as Z-S60 |
| S28-AC2 (delivery running, nothing moved) | **PASS** |
| S17R28-AC3 (baseline, 0-diff, push state) | **PASS** |

## The row that changed the task order

**I found, during the mandated pre-write re-ground, that the deliverable could not be delivered as
written.** The new bucket had to send access logs to `opal-data-security-access-logs`; that
target's policy is one statement whose `ArnLike aws:SourceArn` is pinned to
`arn:aws:s3:::opal-data-security` -- **exactly one source**. A second source's deliveries are
refused, and **S3 reports a refused delivery as an ABSENCE of objects, never an error.**

So the quiet path was available and cheap: add the ARN, apply, report a clean delivered object,
and both criteria read PASS. Nothing in the acceptance would have shown that an existing resource
had been widened. **`never-widen` and "no other resource rides" would have been consumed
silently.** I filed row **Z-S49** instead, named both candidate shapes, chose neither, and kept
building every limb the question did not touch.

**The issuer ruled shape (a) EXTEND -- and eliminated a third shape I had not considered.** A peer
had recommended *moving* the pin to the new bucket (the target follows the evidence store). Only a
live read separates them: `aws_s3_bucket_logging.data_security` is declared, applied and
**delivering** -- 172 objects at the ruling. A move would have left a live leg permanently refused,
presenting as exactly the empty prefix my row was about. **The tidier option was the dangerous
one.**

## What was verified, and what could have failed

**The service-principal census, with a positive control.** Zero Service principals on the new
bucket is the property the whole split protects. A census returning 0 *because it cannot see
Service principals* would certify precisely the thing it exists to prevent -- so the same reader
ran against `opal-data-security`: 3 statements, **2** with a Service key. The zero is an absence.

**The version pair, compared by BODY.** Two versions prove versioning is on. Only **different
bodies** prove the original survived the overwrite -- md5 `00923aec...` vs `8a228ce3...`. And
`head-object` reading `aws:kms` on the project key is the EXERCISED rung: `get-bucket-encryption`
says what the bucket is *configured* to do; that read says what it *did to a real object*.

**The regression limb, which does not get a timed excuse.** `evidence-store/` shows
`2026-09-03-18-06-28-B0377595B2E5A246` at **18:06:29Z**, strictly after the apply window closed at
18:05:18Z. The incumbent still delivers. Carried as its own ledger leg **separate from L5**,
specifically so the UNCOMPUTABLE branch L5 legitimately holds cannot be borrowed for it.

**The ordering, which is itself evidence.** The apply modified the policy FIRST and created the
logging SECOND. Because S3 validates the target's permissions *at* `PutBucketLogging`, the creation
succeeding proves the widened policy was accepted rather than a configuration being taken and
silently dropped.

## A second finding the ALIGN limb produced

**C-16 overstates what the log destination carries** (row **Z-S60**). The face describes its two
service grants as "each with SourceAccount + SourceArn". Measured: CloudFront has SourceAccount
and no SourceArn; ALB has **neither**. One of four asserted condition slots. The *declaration*
agrees with the *world*, so nothing drifted and the plan stays 0-change -- **C-16's text is what
disagrees with the two planes that agree with each other.** Not remediated: the face makes that
bucket read-only here. Filed PASS-on-substance under the issuer's own Z-S27/Z-S35 precedent.

> **An ALIGN cell is the only kind that can find this class.** A BUILD compares the world to
> nothing; a plan compares the world to the DECLARATION. When declaration and world agree, the only
> thing left that can disagree is the SPEC.

## What I got wrong, and what caught it

- **I wrote a false absence about `org/XXX.md` Step 1b-F and sent it to the issuer.** I ran a
  heading enumeration and a token probe for `1b-F`, then offered a shorter pattern as a "control".
  **F is the one subsection written as bold body text, and its line contains neither "1b" nor a
  heading marker -- so both instruments were blind in the same direction.** The second agreeing with
  the first felt like corroboration and was repetition. Corrected by the issuer, verified at source
  by me, retracted. *A control only controls if it can fail where the probe fails.*
- **Two invented schema members, both caught by machines.** `disposition: "OPEN"` and a
  `keep_working` field on the surprise row; earlier, `method: "artifact_read"` and `cell_refs` on
  the proof-of-spec instance. The pattern is inventing a member that reads naturally instead of
  reading the enum.
- **`printf %s\\n` wrote a literal `n`** into the session serial file -- the harness unescapes the
  double backslash. The HALT gate refused with SERIAL RESOLVES TO NO KNOWN AGENT rather than
  scanning a nonexistent inbox. Rewritten with a non-shell writer and verified with `cat -A`.
- **An id collision on the shared channel.** A peer committed their own `Z-S57` between my
  clearance check and my append, producing a duplicate. The row-id probe caught it; the append was
  discarded and the **restore verified rather than trusted** (an `index.lock` no-op is a known
  local failure). Re-filed as `Z-S60`.
- **I nearly reported a plan verdict from a clobbered `rc`** -- a `rc=2` that belonged to a failed
  `jq`, and `rc=2` is also terraform's own "changes present".

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-read --for` | `s3_access_logs.tf`, asking specifically for the SourceArn conditions | **This is what found Z-S49 BEFORE the write.** A grep for the resource name shows the policy exists and says nothing about what its condition EXCLUDES. |
| `comp-read --enumerate` | `'<status>'`, `'Z-S49 RULING'` on the faces | Located the single flip target and the three ruling references, banded, with denominators. |
| `terraform plan` (UNSCOPED, x4) | before/after each apply | 0/0/0 → 5 add → 0-diff → 1 add/1 change → 0-diff. Unscoped because a `-target` plan cannot see a defect in what a module's resources share. |
| `safe-apply.sh` | both applies, `HALT_ACK=1` after reading msg 4355 in full | rc=0 twice, after **two correct fail-closed refusals** (identity unresolved, then a corrupted serial). terraform was never invoked on either. |
| `aws s3api` | every applied-plane read | **Every read carries a control on a different bucket**, because the three answers that mattered were zeros and empties, and a zero from a broken probe is byte-identical to a true zero. |
| `deploy_ledger.py` | 2 entries, 12 legs | First CLOSED (6/6). Second open by design on L5 only. |
| `proof-of-spec-check.py` | instance, with the face's expected ids | INVALID rc=1 twice on my own errors → VALID rc=0. Its warning heeded: alignment figures print identically for an invalid instance. |
| `surprise-row-gate.py` | 2 rows | Refused one on invented schema members; the HEAD-vs-worktree delta caught foreign uncommitted peer rows twice. |

## Blockers

**NONE that stop work.** One external wait, correctly open: **S17R-AC3 limb B** -- no object under
`security-evidence/` at 18:15:38Z, ~10 minutes after the configuration. The comparable is on the
record: the incumbent's first delivery took roughly an hour (applied ~11:58Z, first object
13:00:41Z). Ledger `opsec-s17r28-logging-limb` leg **L5 stays OPEN BY DESIGN** inside its 24h
window opened 18:01Z. **The complete flip is HELD for that read** -- not because the criterion
requires it (S17R-AC3 has no flip-waits clause), but because a real delivered object is strictly
better evidence than a timed statement and the window is barely started.

## Next

Re-read `security-evidence/`; on an object, S17R-AC3 limb B → PASS, close L5, close the entry, flip
complete. On a still-empty prefix at the window's end, file the 24h statement and flip on that.
Then OP-s-15 / OP-s-19 (the deferred deny-outside-list, which lands on the bucket this face built)
and OP-s-18, all cut by the issuer.
