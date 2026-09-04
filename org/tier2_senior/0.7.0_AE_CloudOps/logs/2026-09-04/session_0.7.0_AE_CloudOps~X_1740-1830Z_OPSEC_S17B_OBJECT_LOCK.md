# Session log -- 0.7.0_AE_CloudOps~X -- 2026-09-04 17:40-18:30Z -- NFRA_OPSEC202609 TO-OP-S-17B

**archetype:** DEPLOY

**Seat:** `0.7.0_AE_CloudOps~X` (site-z)
**Task order:** `NFRA_OPSEC202609.TO-OP-S-17B` -- Object Lock (GOVERNANCE) on `cases/`, executing
`OP-x-4`, CLOSED on Andrew's word 2026-09-04 ~13:00Z (*"Approved for all of these"*)
**Commits:** `cb67888289` (+ this log and the proof)
**Continues:** the same session as the `OP-s-9` faces; ~10h gap, state re-grounded at load rather than assumed.

---

## Current state

**DONE. Proof-of-spec VALID rc=0, all five criteria PASS, ledger CLOSED on 4 of 4 legs.**

**Object Lock is ON**: `ObjectLockEnabled`, `GOVERNANCE`, **365 days**, enabled **in place** on the
existing versioned bucket at **2026-09-04T18:09:25Z**. No new bucket, no migration, no replacement.

**The forward-only boundary is DEMONSTRATED**, not asserted, on two real sentinel-written case files
either side of the enable — and **839 pre-existing objects were not touched**.

## What was done

**Phase-1 re-grounding changed a number the face told me to re-read.** The issuer measured **438**
objects at 13:1xZ. I measured **839** at 17:4xZ — the prefix nearly **doubled in ~4.5 hours**, and the
newest object landed *during* my census. Versioning `Enabled`; no pre-existing lock config.

**The choice that mattered was which resource to use.** `object_lock_enabled` on `aws_s3_bucket` is
**create-time-only** — setting it would have planned a **REPLACEMENT of a live evidence store**. The
separate `aws_s3_bucket_object_lock_configuration` enables it in place. The plan proves it: **1 to add,
0 to change, 0 to destroy**, and zero `forces replacement` / `must be replaced` / `will be destroyed`.

**365 days is anchored, not chosen.** No evidence-retention period is stated anywhere in the project.
The WAF log group these case files are *built from* is `retention_in_days = 90`, so a case file
retained ≤90 days would expire no later than its own source. **90 is a measured floor; 365 clears it 4x**
without importing an unstated multi-year records posture.

## Blockers

**None.** The face is complete.

## Next steps

- **[a future reader]** The coverage boundary is written into `s3_evidence.tf`'s own header with the
  enable timestamp and both demonstration keys, so it is met where the store is defined.
- **[nobody, stated so it is not assumed]** The 839 pre-lock objects will never gain retention. For them
  **versioning remains the control** — tamper-EVIDENT, not tamper-RESISTANT.

## Errors and corrections at this seat

- **My commit was REFUSED and I nearly recorded it as landed.** safe-commit's stdout was replaced by a
  reminder not to grep tool output; I asked the repository instead (`git log -1`, with a bogus-hash
  negative control) and **HEAD was still the issuer's commit**. The refusal: **non-ASCII in the commit
  message** — the same `⛔` glyphs I had already stripped from the `.tf`. **I applied the rule to one
  artifact and not the other**, which is this session's recurring shape. The gate was right.
- **My edit guard fired on its own target.** The script refused on *"an object_lock argument already
  exists"* — the only occurrence was the **comment** saying there was none. `comp-read --enumerate`
  settled it in one call (1 hit, SUB, with its own WARN that every hit was a fragment). Narrowed the
  guard to non-comment lines rather than deleting it.
- **My first positive control for the bypass sweep was wrong.** `infrastructure-snapshot-role` returned
  `implicitDeny` for `s3:GetObject` on this bucket — its breadth is in Lambda, not S3. A fallback
  control on the same ARN fired, and **without it a universal deny would have been indistinguishable
  from a broken sweep.**

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `'opal-security-evidence' infra/aws/terraform` ; `'retention period\|days *= *[0-9]+'` over the project | The first found the owning root in 6 hits / 561 files. **The second is what made 365 defensible rather than invented**: no evidence-retention period exists anywhere in the project, and it surfaced the WAF log group's `retention_in_days = 90` — the measured floor the choice is anchored to. |
| `comp-read` | `--for` on `s3_evidence.tf`; `--enumerate 'object_lock'` | The `--for` gave the file's shape and its 17 qualifiers before any edit. The `--enumerate` **resolved a guard failure correctly instead of by override**: one hit, the comment I was replacing, with the tool's own WARN that every hit was a fragment. |
| `comp-schedule` | issuer preflight, not re-run | This face builds no monitor and discharges no gate; the preflight declares its own C1 correction as ORIENTATION rather than a criterion. Stated rather than left blank. |
| `comp-iam` | DECLARED-NOT-APPLICABLE for the verdict | The preflight rules it a DESIRED-plane lens whose silence is never an ALLOW, and sends `S17B-AC4` to `simulate-principal-policy` on the applied plane. That is what ran: 231 principals, one `--resource-arns` per call. |

## Evidence discipline worth carrying

**The undiscriminating instrument showed up again and the control caught it again.** *Before* the enable,
`get-object-retention` returned the **identical error for a real key and a deliberately nonexistent one** —
the call could not have supported a pre-enable "no retention" claim at all. It only becomes discriminating
*after* the lock exists, when the error moves from bucket-level to object-level. **Both AC2 reads were
therefore taken after the act**, which is not what a literal reading of the criterion suggests.

**A probe would have been permanent litter.** Any object written after the enable acquires 365-day
retention and becomes undeletable without a bypass. On a prefix gaining ~90 objects an hour, **a real
production write was available 15 seconds later** — cleaner *and* stronger evidence than a synthetic one.

**And the census had to compare keys, not counts.** On a continuously-written prefix the count moves on
its own; only a key-by-key `LastModified` comparison answers "was anything re-written".
