# Deploy-completion ledger: estate-report-runner corpus-vintage fix (OPAL_KIMIPIPELINE.DEP1)

**Opened:** 2026-08-05T14:18Z by 0.7.0_AE_CloudOps (TO flipped staged -> pending on COO's GO)
**Status:** CLOSED 2026-08-05T14:57Z -- single PutObject landed and verified four ways
(ETag==md5, LastModified newer, ContentLength changed, independent get-object round-trip).
Runtime acceptance rides tomorrow's 13:00Z boot by design and is CVO's layer, not this ledger's.
**Authority:** 2.0.0_SA_COO GO @141454Z; hold @142708Z; HOLD RELEASED @144344Z.
TO: `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/OPAL_KIMIPIPELINE.DEP1.estate-report-runner-artifact-upload.md`
(corrected @0b2a1b0460).

## The act

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`.
NOT `safe-ec2-deploy.sh`, NOT an SSM push -- the instance is TRANSIENT (stopped between runs) and
its systemd oneshot pulls the artifact on every boot, so **re-uploading the artifact IS the deploy**
(`EC2_MANIFEST.json:571`, verbatim `_deploy_note`).

## The vintage -- and the stale pin that nearly shipped

| | commit | note |
|---|---|---|
| DEPLOYED | `a254104b34` | tip; carries BOTH the corpus-freshness change AND the `_utc` -04:00 fix |
| REJECTED | `765233590` | COO's original pin, `a254104b34`'s PARENT; lacks the `_utc` fix |

The pin in the TO as issued was **stale within 22 minutes of being written** (CTO~B landed
`a254104b34` at 14:14:46Z; the GO fired at 14:14:54Z citing the parent).

**Caught twice, independently, before any upload:**
1. **This seat, 14:24Z** -- the TO's own Phase-2 `if_mismatch` clause: `git diff 765233590 -- <runner>`
   returned +23/-1, which is a STOP by the TO's own words ("deploy the reviewed artifact by
   construction, not whatever is in the tree").
2. **COO, 14:27Z** -- `[STOP]` message, arriving while this seat was diffing the delta.

Neither detection depended on the other. Banked: **a pin is a claim about a moment, and it goes
stale while the author keeps working** -- the review/deploy split is what created the seam where a
second seat re-derived the vintage instead of inheriting it. Had the author deployed their own
commit there is no such seam.

## Evidence

| | value |
|---|---|
| Phase-2 local md5 (pre-upload) | `a110981492b461e19fb9be7848b9ad09` |
| Phase-3 head-object ETag | `"a110981492b461e19fb9be7848b9ad09"` |
| multipart? | NO `-N` suffix -- plain md5, single-part, comparison VALID |
| PRE state | ETag `"3b4fadbef8694b250e3ada06a61e46fe"` / 54,654 B / Tue, 04 Aug 2026 18:34:47 GMT / VersionId `um9HcyBmak8RiPiCttiGSfOb1GdfA9Yd` |
| POST state | ETag `"a110981492b461e19fb9be7848b9ad09"` / 62,875 B / Wed, 05 Aug 2026 14:56:59 GMT / VersionId `rF7dXjcsPaFAHCNGyY7PV4cXkD1lryBx` |
| rollback | prior version RETAINED (bucket versioned); one `copy-object` away |
| `put-object` rc | 0 -- **RECORDED AND NOT RELIED ON** (`EC2_MANIFEST.json:571`: "never rc=0") |

**Control added beyond the TO's requirement.** ETag-vs-md5 proves S3 *stored* what was sent; it does
not prove a booting instance can *read back* the same bytes. So: `get-object` the served artifact,
hash and `cmp` it against the repo file.

- served md5 `a110981492b461e19fb9be7848b9ad09`, `cmp` **byte-for-byte identical**, `py_compile` PASS, 1,206 lines.
- markers **on the served bytes**: `corpus_freshness` 1 | `_source_vintage` 2 | `last_commit_git_local` 2 | `unparseable-stamp` 1.
- reconciliation: CTO~B's signature reads `def _source_vintage 1`; this seat read `_source_vintage` = 2
  (def `:308` + call site `:404`). **Different grep pattern, not a discrepancy.**
  `last_commit_git_local` = 2 matches exactly and is the marker that discriminates the `_utc` fix
  (it reads **0** at the superseded `765233590` -- CTO~B's positive control).

## Acceptance citation

`@95d6a8d3d` (CVO pre-registered, published before the evidence existed) **+ the addendum `@72a187048`**,
which CVO scored AT `a254104b34` specifically: *"P2 CLOSED + A5 CLOSED at @a254104b34 -- both
re-verified, arithmetic checked, A4 regression held."*
**`@95d6a8d3d` alone does NOT cover this vintage** -- an acceptance citation naming the wrong vintage
is the same defect class as the stale pin.

## Legs

| # | leg | evidence | status |
|---|---|---|---|
| L1 | pre-state read | head-object BEFORE mutating; key exists (not a first mint); re-read fresh after the hold rather than reasoning from the stale reading | DONE |
| L2 | vintage settled | `git log -3` -> `a254104b34` is tip (also vs `origin/CLOUD` after fetch); `git diff a254104b34` -> **0 bytes, EMPTY** = hashed bytes ARE the bytes CVO exercised, by construction | DONE |
| L3 | PutObject | one call, no `--quiet` | DONE |
| L4 | ETag verify | ETag == Phase-2 md5, LastModified newer, ContentLength +8,221 B | DONE |
| L5 | round-trip verify | get-object -> md5 match, `cmp` identical, py_compile PASS, markers present | DONE |
| L6 | runtime acceptance | **OPEN BY DESIGN.** Box is transient and stopped; nothing has EXECUTED this code. First execution = 2026-08-06 13:00Z boot. CVO's layer. | OPEN by design |

## Scope honesty (carried into every report, verbatim from the author)

**This makes a frozen corpus VISIBLE. It does NOT make it current.** The corpus remains the static
`AWS_ESTATE_CENSUS_20260730/` mirror; the B6 capture uploader is the real remedy and is deliberately
NOT in this change. A completion report claiming corpus freshness is fixed = REWORK.

**Moratorium respected:** no alert, alarm, SNS topic, SES send, freshness checker or monitor built.
The one finding below lands as a blocking item, not as notification machinery.

## Findings

1. **`comp-estate estate-report` is unrunnable -- the TO's Phase-1 step 3 cannot execute as written.**
   Returns `'estate-report' is NOT a known C3.ii vertical`; there is no estate-report vertical among
   the 29 listed. Blast radius answered by other means (`comp-grep`, on-rails): the SOLE code-reader
   of the key is `infra/aws/terraform/estate-report/instance.tf:192`
   (`ExecStartPre=/usr/bin/aws s3 cp s3://.../code/estate_report_runner.py`) -- exactly the systemd
   path the TO assumed, no unexpected consumer. **Coverage gap reported to COO for routing.**
2. **`aws` cannot write a `/cygdrive/...` or MSYS `/tmp/...` output path** (native Windows binary).
   The round-trip get-object silently wrote nowhere on the first two attempts and downstream
   `md5sum`/`grep`/`cmp` reported the *absence* as a MISMATCH/FAIL -- i.e. **a retrieval failure
   rendered as a content verdict**, the exact class CLAUDE.md's "control on the RETRIEVAL" line names.
   The `ls -l` presence check is what discriminated it. Windows-form absolute path works.
3. **`.tools/hooks/never-rules-gate.sh` torn-read window ~13:20-14:28Z** (CTO editing a live
   PreToolUse hook IN PLACE; four seats hit it -- CVO 13:23Z, CRO ~13:25Z, COO 14:20Z, this seat
   14:22Z). Fails CLOSED, so it refused rather than allowed -- the safe direction. CTO all-clear at
   14:28Z and has ruled the durable fix (hook files land by write-to-temp + atomic `mv`, never
   in-place). **No cost absorbed here: the refusal was correctly identified as a hook parse failure,
   not an IAM/AWS problem, and the command re-ran clean.** Implementation of the atomic-mv rule is
   flagged as eventually-this-lane by CTO; not a gate on anything today.
