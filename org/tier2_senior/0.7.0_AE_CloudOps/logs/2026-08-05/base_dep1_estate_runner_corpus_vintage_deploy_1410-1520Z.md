# DEP1: estate-report-runner corpus-vintage fix -- deployed + verified (1410-1520Z)

**archetype:** DEPLOY

**Serial:** 0.7.0_AE_CloudOps (base) · **TO:** OPAL_KIMIPIPELINE.DEP1 · **Status:** COMPLETE

Session start (register, watcher armed task `b8f9xo3su`, 6 inbox messages pulled) through a landed
and four-ways-verified P1 deploy, inside the hard pre-2026-08-06 13:00Z boot window with ~22h spare.

## What shipped

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`.
The instance is TRANSIENT -- stopped between runs, systemd oneshot pulls on every boot -- so
**re-uploading the artifact IS the deploy** (`EC2_MANIFEST.json:571`). Not `safe-ec2-deploy.sh`,
not SSM; there is no live host to push to.

| | value |
|---|---|
| deployed vintage | `a254104b34` |
| rejected vintage | `765233590` (the TO's original pin -- `a254104b34`'s PARENT, lacks the `_utc` fix) |
| Phase-2 local md5 | `a110981492b461e19fb9be7848b9ad09` |
| Phase-3 head-object ETag | `"a110981492b461e19fb9be7848b9ad09"` |
| multipart? | no `-N` suffix -> plain md5, comparison VALID |
| PRE | ETag `"3b4fadbef8694b250e3ada06a61e46fe"` / 54,654 B / Tue, 04 Aug 2026 18:34:47 GMT |
| POST | ETag `"a110981492b461e19fb9be7848b9ad09"` / 62,875 B / Wed, 05 Aug 2026 14:56:59 GMT |
| rollback | prior VersionId `um9HcyBmak8RiPiCttiGSfOb1GdfA9Yd` retained |

Acceptance cited: `@95d6a8d3d` **+ addendum `@72a187048`** (CVO scored the addendum AT `a254104b34`;
`@95d6a8d3d` alone does not cover this vintage).

## The stale pin -- caught twice, independently, before any upload

The GO fired at 14:14:54Z citing `765233590`. CTO~B had landed `a254104b34` on the same file at
14:14:46Z. **The pin was stale within 22 minutes of being written.**

1. **This seat, 14:24Z** -- the TO's own Phase-2 `if_mismatch` clause. `git diff 765233590 -- <runner>`
   returned +23/-1, which the TO defines as a STOP ("deploy the reviewed artifact by construction,
   not whatever is in the tree"). I halted there.
2. **COO, 14:27Z** -- `[STOP]`, arriving while I was reading the delta.

Neither depended on the other. **A pin is a claim about a moment, and it goes stale while the author
keeps working.** The review/deploy split is what created the seam where a second seat re-derived the
vintage instead of inheriting it -- had the author deployed their own commit, there is no such seam.
CTO~B endorsed this framing on close.

I did **not** substitute my own judgment for the owner's on which vintage to ship. I waited for COO's
release (14:43Z) after independently confirming both conditions they named were discharged in the
record: CTO~B authored `a254104b34` at 14:14:46Z (tip), and CVO's addendum at 14:20:34Z reads
*"P2 CLOSED + A5 CLOSED at @a254104b34 -- both re-verified, arithmetic checked, A4 regression held."*

## Independent closure by three seats

- **CTO~B @151407Z** -- RAVC-4 CLOSED on **independent re-derivation**, not on my report:
  their md5 of `a254104b34` == my head-object ETag. Also conceded their `def _source_vintage 1`
  marker was pattern-dependent and mine was the correct read.
- **CVO @151429Z** -- verified at the served layer, byte-identical to the certified vintage; moved
  their committed-not-deployed warning OPEN -> DISCHARGED.
- **COO** -- TO corrected `@0b2a1b0460`, hold released `@144344Z`.

## Compiler Tools

Every `run` in the TO's mandate, with observed output and explicit pass/fail vs `expect`.

| Phase | run | observed | vs expect |
|---|---|---|---|
| 1.1 | `aws s3api head-object --bucket opal-estate-report --key code/estate_report_runner.py` | ETag `"3b4fadbef8694b250e3ada06a61e46fe"`, 54,654 B, Tue 04 Aug 2026 18:34:47 GMT, VersionId `um9Hcy...` | **PASS** -- key exists, so an UPDATE not a first mint. Re-run fresh after the hold rather than reasoning from the stale reading. |
| 1.2 | `git show <vintage>:...estate_report_runner.py` | resolved; **positive control** `wc -l` = 1,184 at `765233590` (a mangled `git show` returns CLEAN EMPTY stdout, so a line count is the retrieval control, not `grep -c`) | **PASS** |
| 1.3 | `comp-estate estate-report` | `'estate-report' is NOT a known C3.ii vertical` -- no such vertical among the 29 listed | **FAIL -- UNRUNNABLE AS SPECIFIED.** See Findings. |
| 1.3-alt | `comp-grep "code/estate_report_runner.py"` | 11 matches / 6 files; scanned 22,294 of 24,226 files in scope. **Sole code-reader:** `infra/aws/terraform/estate-report/instance.tf:192` (`ExecStartPre=/usr/bin/aws s3 cp s3://.../code/estate_report_runner.py`) | **PASS** -- blast radius is exactly the systemd path the TO assumed; no unexpected consumer. Denominator printed. |
| 1.4 (new) | `git log -3 --oneline -- <runner>` | `a254104b34` is tip, nothing above it; re-checked against `origin/CLOUD` after `git fetch` | **PASS** |
| 1.5 (new) | `git diff a254104b34 -- <runner>` | **0 bytes, EMPTY** | **PASS** -- the hashed bytes ARE the bytes CVO exercised, by construction rather than assumption. |
| 2 | `md5sum <runner>` | `a110981492b461e19fb9be7848b9ad09`, 62,875 B; cross-checked against an independently extracted `git show a254104b34` blob -- identical | **PASS** |
| 3 | `aws s3api head-object` (post) | ETag `"a110981492b461e19fb9be7848b9ad09"`, 62,875 B, Wed 05 Aug 2026 14:56:59 GMT, VersionId `rF7dXj...` | **PASS** -- ETag == Phase-2 md5; LastModified newer; ContentLength +8,221 B. `put-object` rc=0 recorded and **not relied on**. |
| extra | `aws s3api get-object` round-trip -> `md5sum` + `cmp` + `py_compile` | served md5 `a110981492b461e19fb9be7848b9ad09`; **byte-for-byte identical**; py_compile PASS; 1,206 lines; markers `corpus_freshness` 1 / `_source_vintage` 2 / `last_commit_git_local` 2 / `unparseable-stamp` 1 | **PASS** -- control added beyond the TO. |

**Why the extra control.** ETag-vs-md5 proves S3 *stored* what I sent; it does not prove a booting
instance can *read back* the same bytes. The round-trip scores the SERVED bytes, which is the
difference between verifying a deploy and verifying my own intent.

**Marker reconciliation (not a discrepancy).** CTO~B's signature reads `def _source_vintage 1`;
I read `_source_vintage` = 2 -- def at `:308` plus the call site at `:404`. Different grep pattern,
same file. `last_commit_git_local` = 2 matches exactly, and that is the marker that discriminates the
`_utc` fix (it reads **0** at the superseded `765233590`). Reconciled rather than raised as a phantom gap.

## Findings

1. **`comp-estate` has no `estate-report` vertical -- an ontology gap, not a footnote.** The pipeline
   that produces the daily estate report is not a named vertical in the estate ontology, so the TO's
   Phase-1 step 3 cannot execute. CTO~B took it onto the **v3 critical path** (v3's design is a
   VERTICAL JOIN: every changed path -> its c3.ii vertical, so this bites directly).
2. **`aws` cannot write a `/cygdrive/...` or MSYS `/tmp/...` output path** (native Windows binary).
   The round-trip `get-object` silently wrote nowhere on two attempts, and downstream
   `md5sum`/`grep`/`cmp` then reported the *absence* as `BYTE MISMATCH: FAIL` -- **a retrieval failure
   rendered as a content verdict**, exactly the class CLAUDE.md's "put the control on the RETRIEVAL"
   line names. An `ls -l` presence check discriminated it; a Windows-form absolute path works.
   Sibling of the documented `.tools/aws` shim arg-layer class.
3. **`.tools/hooks/never-rules-gate.sh` torn-read window ~13:20-14:28Z.** CTO was editing a live
   PreToolUse hook IN PLACE; the harness re-reads it per tool call, so concurrent readers sampled a
   half-written file. Four seats hit it (CVO 13:23Z, CRO ~13:25Z, COO 14:20Z, me 14:22Z). It fails
   **CLOSED** -- refused rather than allowed, the safe direction. I identified it as a hook parse
   failure rather than an IAM/AWS problem and re-ran; **no diagnostic cost absorbed and no IAM
   re-plumbed**, which was the specific expensive misdiagnosis COO and CTO both wrote to warn against.
   CTO all-clear 14:28Z + ruled the durable fix: hook files land by write-to-temp + atomic `mv`,
   never in-place. Implementation flagged as eventually-this-lane; not a gate today.
4. **Audit-archive invoker (startup A.2) reported 2 findings**, unrelated to DEP1 and not actioned
   this pass: `org/pipescript-suite-gate-audit.log` is audit-log-shaped but absent from MANIFEST
   (review + add or exclude), and `org/rcg-sweep-audit.log` shows a **non-append edit** (first
   divergence line 1 col 118; baseline 2,376 B / live-head 2,400 B). The second is an
   append-only-integrity signal on CRO's sweep log and is worth someone's eyes.

## Scope honesty (carried verbatim into all four reports)

**This makes a frozen corpus VISIBLE. It does NOT make it current.** The corpus is still the static
`AWS_ESTATE_CENSUS_20260730/` mirror; the B6 capture uploader is the real remedy, is deliberately NOT
in this change, and sits on MSTR's board for Andrew. A report citing this as "corpus freshness fixed"
should be stopped by this line.

**Deployed != exercised.** The box is transient and stopped; **nothing has executed this code.** First
execution is the 2026-08-06 13:00Z boot, and whether the emitted report actually carries the vintage
fields is CVO's verdict, not mine. I verified the artifact **at rest** only.

**Moratorium respected:** no alert, alarm, SNS topic, SES send, freshness checker or monitor built.
Findings above land as blocking/routed items, not notification machinery.

## Queue (COO-sequenced, unchanged)

1. MSTR's **7** past-window deploy-ledger dispositions (223718Z + the 233807Z addendum widening 4 -> 7).
   Exclusion stands: leg-4 L4 is FAIL BY DESIGN -- do not re-run, do not close.
2. The 11 pending TOs.
3. CRO's two RCG handoffs (cohort-A layer-refactor; the +70-file AE bundle) and `~E`'s AAS-ERR handoff
   (access-anomaly-scanner alert dispatch failing 353/983 over 30d -- repair-of-existing, NOT an
   alarm-build, and the value question is live given 30 days of dropped alerts nobody missed).
