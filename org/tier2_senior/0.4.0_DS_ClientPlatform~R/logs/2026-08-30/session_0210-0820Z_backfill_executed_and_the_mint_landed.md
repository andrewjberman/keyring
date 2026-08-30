# ADVI_INSURE TO-R1-DS — the backfill EXECUTED, the mint APPLIED, and the face now waits on a fire ~20 h out

**archetype:** BUILD + MEASUREMENT
**Seat:** `0.4.0_DS_ClientPlatform~R` · **Window:** 2026-08-30 02:10–08:20Z · **Predecessor log:**
`2026-08-30/session_0056-0210Z_step0_measured_and_the_stage_entry_built.md`
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`** (PRD s.3, Andrew ~16:1xZ).

---

## Current State — read this first if you are the successor

⭐ **THE CONVERTER IS LIVE.** `TO-S1-AE` applied 9/1/0 at 08:1xZ: the 49F insurance bronze that had
landed daily at 04:35Z into a prefix **nothing consumed** now reaches a converter
(`opal-assets-silver-bd49finsurance`).

| criterion | state |
|---|---|
| **AC1 · AC5 · AC6** | **PASS** — do NOT re-execute |
| **AC2 · AC3 · AC4** | **GATED ON THE NEXT 04:35Z SCHEDULED FIRE** (~20.5 h from this log) |
| the mint | **APPLIED**; apply leg CLOSED at the gate, ledger `7b4ebfc470` **stays OPEN** through S1-4 |

⛔ **THE FIRE IS THE ACCEPTANCE AND A MANUAL INVOKE IS NOT.** `1.0.0_SA_CTO` 86506 + `0.7.0_AE_CloudOps`
86497: the new family's OWN log carrying that day's `insurance_*` keys through the stage entry to
silver parquet at the grammar, rows == the bronze attested totals, **with the cottonwood family's log
showing NO invocation on those keys as the negative control.** A manual invoke is QA evidence only and
closes nothing. ⛔ **Do not spend the discriminator** — this is the same reason my predecessor declined
to convert 08-29 ad hoc.

⚠ **AND READ `MaxMemoryUsed` ON THAT FIRE BEFORE TRUSTING 1024 MB.** I sized it on a **tracemalloc
FLOOR** (23.5 MB python-object allocation; excludes interpreter, native buffers, layer). The gate
carried that limit into S1-4 rather than rounding it off. The first fire's own number is the real
measurement.

## What Happened

1. **The RULED backfill (78473, word given 84333) — EXECUTED, 3 of 3** `@77f4dbaca2`.
   All three pre-digest partitions reproduce **byte-for-byte**; manifests written and read back FROM
   S3. **0 of 3 served parquets moved** (ETag + LastModified + VersionId captured before, re-read
   after — on a versioned bucket a VersionId change alone would prove a write at identical bytes).
   The "silver present, manifest absent" class went **3 → 0 by measurement**. RAVC-closed 84609,
   graded ACCEPTED by `3.0.0_SA_CVO` 84666 on an independent re-derivation (set test + LastModified
   as a second instrument).
   ⛔ **A CODE CHANGE WAS REQUIRED FIRST:** the shipped `--backfill-manifest` returned `SUPERSEDE` and
   fell into the normal write path, which put_objects the PARQUET — the exact act the ruling forbids.
   New outcome `BACKFILL-VERIFY-THEN-MANIFEST-ONLY` (Rule 24 iv: one enum value cannot carry two write
   behaviours), plus a DATA-vs-SERIALISATION-ONLY discriminator for a mismatch, without weakening the
   byte gate.
2. **S1-1 handoff** (runtime profile, per-feed prefixes, family string) — ACCEPTED 84607.
3. **A BLOCKING finding on the scope pin** — see below. Remediated in plan, then on the applied plane.
4. **A CRLF finding — mine, and it nearly shipped.** See below.
5. **A platform-side session pause 06:07–07:51Z** (`0.0.0_AB_MSTR` 86322, grounded on the Windows
   System log + network profile + `git log`). No work lost; movement windows reset.

## ⛔ The two things I got WRONG, so the successor does not inherit them as true

1. **My prescribed remedy would have destroyed eight live IAM policies.** I wrote "repoint BOTH
   consumers". Taken literally on the write side that re-keys `aws_iam_policy.silver_write_per_source`,
   whose NAME embeds the key → **REPLACEMENT of 8 live policies** + attachment churn. `0.7.0_AE_CloudOps`
   found the non-destructive shape (sparse override + one resolver for both planes + sparse companion
   with fallback). **The proof is on the applied plane:** `iam list-policies` returns the eight
   per-source policies still under their ORIGINAL names.
2. **I counted RESOURCES and stated it as the FIX SCOPE.** Two consumer resources, but **FOUR
   expressions** (Resource list AND the `ListBucket s3:prefix` Condition, in each). A two-of-four
   repoint fails ASYMMETRICALLY. **My own census printed the extra line numbers and I did not let them
   reach the conclusion.** The TO-S1-AE acceptance wording carried my error until `2.0.0_SA_COO`
   corrected it `@d1ea47add2` — a wrong count with a live carrier is worse than a wrong count alone.

## ⛔ The CRLF near-miss — the highest-value thing in this window

`Path.write_text()` on Windows turns `\n` → `\r\n`. My splice scripts left
`bd49f_insurance_conversion.py` at **`i/lf w/crlf`** on a file that DECLARES `eol=lf`. Git normalises
on commit, so **the repo record was never wrong** — `git show`, `git diff` and review all read clean.

**It nearly shipped, and the parity gate would have certified it:**
```
commit 7d0ab9cdac   59,324 B   0 CRs      <- correct, and what any reviewer sees
worktree at build   60,525 B   1,201 CRs
uploaded zip        built from the WORKTREE -> the CRLF copy
vendor --check      cmp(worktree, vendored) -> rc=0 "3 of 3 parity"   <- CERTIFIED THE WRONG PACKAGE
```
A copy compared to its own source cannot see that the source is wrong. It would not have failed at
runtime either (Python reads CRLF fine) — **only the identity claim was false.**

✅ **What caught it: the LF sha per member taken from the INDEX BLOB by a seat that is not the
packager** — `1.0.0_SA_CTO` 86164's gate condition, which I supplied at 86198 before the build. That
was the only comparison in the chain with discriminating power. Fixed at source (`tr -d '\r'`; sha ==
the committed blob; `git diff` 0 lines; the ` M` a stale stat cache cleared by `update-index --refresh`).
**CTO amended BOTH plan shapes** (S1-2 and inf-silver-chain at `~V`) so every parity reference comes
from `git show <pin>:<path>`, never a worktree `cmp`, and added a falsifier arm: a CRLF-altered member
must REFUSE against the index reference. `~V` hit the same class independently on `build_billing_dim.py`.

## Decisions Made

- **Did not convert the 08-30 bronze ad hoc.** It would spend the discriminator S1-4 exists to produce.
- **Did not re-derive AE's 04:35Z fire read** — accepted at COO; a second pass with the same instruments
  is repetition, not corroboration.
- **Did not touch `vendor-manifest.sh` or `build-and-upload.sh`.** Real defects, but the CI tools'
  owner's call; the plans route around them and the gate carries the item.
- **Did not edit `org/XXX.md`** when I found two blocks labelled `B.0` with contradicting predicates —
  protocol owner's file; a third seat editing is how a law file gets a third copy. Struck by
  `1.0.0_SA_CTO` `@f5e9f6923d`; the investigation revealed that commit had ALSO swallowed MSTR's
  uncommitted worktree edit (the foreign-dirty-file class, swallowed rather than lost).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-keys` | 5 prefixes, `--all` | the before/after silver census (3 keys → 6), the bronze 14 |
| `comp-find` | `--name`, `--corpus all/aws` | located `vendor-manifest.sh`; the T4A artifact census (1 of 4 families over 136,670 files) |
| `git ls-files --eol` | the 3 package members | **found the CRLF** — the sound instrument; `grep -c $'\r$'` false-reads here |
| `git show <pin>:<path> \| sha256sum` | 3 members + 1 negative control | the index-blob LF shas; **the rung that caught the bad zip** |
| `python … --self-test` | baseline + 4 mutants on a scratch copy | 34 arms; 3 of 4 mutants fired on the predicted arm, **the 4th exposed an unarmed seam** |
| `comp-pipescript` / `comp-validate` | io ×5 trees, postdeps, validate | rc=1/1/2 — all REFUSE; positive control `a00_runner` → 0 |

## Push State

`77f4dbaca2` **ON ORIGIN**. This log commits after the 08:18Z CLOSE. AE's `7d0ab9cdac` /
`e6a508ac96` / `7b4ebfc470` were LOCAL at 08:14:15Z and ride the same window.

## ⛔ First act for the successor

1. **Read the next 04:35Z fire** — the new family's own CloudWatch log, `rows == attested_total` per
   feed, silver parquet at the grammar, **and the cottonwood family's log showing NO invocation** on
   those keys. That closes AC2/AC3/AC4 and the S1-4 face.
2. **Read that fire's `MaxMemoryUsed`** against the 1024 MB profile before treating the number as sound.
3. Expect **2 of 3 feeds**: `insurance_relationshipdetail` is INERT by ruling 84177 (the scheduled
   producer never invokes it; extending it is a widened BD egress needing Andrew's per-use word).
   **That is designed behaviour, not a gap in the stage.**
