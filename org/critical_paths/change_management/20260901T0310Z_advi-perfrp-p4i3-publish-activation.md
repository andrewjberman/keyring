# Deploy-completion ledger: ADVI_PERFRP -- P4I-3 PUBLISH ACTIVATION (CALL 2)

**Status:** ⭐ **CLOSED-COMPLETE.** 4 PUBLISHED / 7 emitter_refused BY DESIGN / **0 HARD_FAIL**.
Landing verified by LISTING; manifest byte sizes match the served objects exactly.
**Executor:** `0.7.0_AE_CloudOps~G` · **Issuer/sequencer:** `2.0.0_SA_COO` (GO @ 90617) ·
**Gate:** `1.0.0_SA_CTO` (no gate remains, 90498) · **Opened:** 2026-09-01 ~03:1xZ

## The act

First live emission of the 49F PERFRP served leaves under the ratified canonical serving tier.

```
  d_publisher_port.py --asof <lib.trading_calendar frontier, DERIVED>
                      --staging-root <staging>
                      --keys <perfrp_emitters.PERFRP_EMITTER_FAMILIES>   (NOT the publisher default)
                      --publish            with OPAL_ADVI_PUBLISH_GRANT=1
  target: s3://opal-data-portal-v2/platinum/advi/49financial/{leaf}
```

⛔ `--keys` is load-bearing: the publisher's default is EVERY EMIT key, which would drag the twelve
legacy ADVI families into an act that is not about them.

## The signal (`2.0.0_SA_COO` 90617) -- FRESH, not a substitution

> **RE-RUN YOUR OWN DEPLOYED SWEEP IMMEDIATELY BEFORE THE PUBLISH ACT. A `MATCH / 0 STALE` READ AT
> THAT MOMENT IS THE GO. It expires the moment anything else commits.**

Reason it is fresh rather than a substitution, and it is measured: `0.4.0_DS_ClientPlatform~G` found
(90423) that the SERVE-RELEASE audit did NOT fire on its own release because two peer commits landed
in the 12 minutes between its authorizing commit and its deploy; `3.0.0_SA_CVO` confirmed at source
(90432) that `safe_deploy_core.py:980` returns `HEAD~1`, answering *"what changed last"* where the gate
needs *"what did the AUTHORIZING commit change."* **The gate is documented fail-closed and is racy on a
shared branch**, so a sweep taken an hour ago is a perishable claim about a tree four seats have been
committing to all night. **The freshness IS the discriminator.**

## Gates, all discharged before firing

| gate | state |
|---|---|
| 08-19 BUILD-ONLY cap | DISCHARGED -- Andrew-direct 23:4xZ |
| 08-21 49F-flip publish hold | DISCHARGED for the serve act -- Andrew-direct 23:4xZ |
| CALL 1 `_code/` sync | COMPLETE -- 71 MATCH / 0 STALE, two seats |
| precondition, CLIENT-LABEL | SUPERSEDED -- premise measured false on the served plane |
| precondition, CUSTODIAN | ANSWERED -- Andrew-direct 01:2xZ; pseudonymisation RE-HOMED to a top-down all-keys project, **NOT cancelled** |
| BOOK-SCOPING | DISCHARGED as a per-leaf blocker @`5e11737907`, RE-HOMED, and explicitly **NOT RESOLVED** -- re-homing is not remediation |
| ACTIVATION SIGNAL | NAMED @ 90617 |

`DEPLOY-SERVE-HELD` sentinel on the shared core: GONE, lifted @`9c7011f93d`.

## How the result MUST be read -- pre-registered BEFORE the act

⛔ **PER-KEY MANIFEST STATUSES, NEVER rc.** `rc=1` IS THE EXPECTED CLEAN OUTCOME: the publisher folds
`emitter_refused` into the same `bad` bucket as `error` / `no_payload` / `twin_diverged` /
`verify_absent` and returns 1 for any of them, and families refuse BY DESIGN.
`HARD_FAIL = ("error", "no_payload", "twin_diverged", "verify_absent")` -- `emitter_refused` and
`deferred_by_ruling` are NOT hard failures.
⛔ **RE-READ THE ATTEMPTED SET AT FIRE TIME. Do NOT score against a remembered denominator** -- the
publishable set has MOVED TWICE against the chain docstring's 2026-08-25 census. Last measurement
(dry run, this session): **4 of 11 would write** -- `performance_account`, `gainloss_relationship`,
`gainloss_account`, `book_advisor`; 7 `emitter_refused`.
An ABSENT run manifest FAILS CLOSED: *"an absent manifest is not evidence of a clean run -- it is
evidence of no evidence."*

## Scope

COVERED: CALL 2 exactly as staged above. **NOT COVERED: anything else. This is not a standing publish
authorization.** No PROD portal promote (separate act, separate branch, not approved and not asked).

## Result -- CLOSED-COMPLETE 2026-09-01 ~03:2xZ

**THE GO, read at the instant of the act** (fresh sweep, per 90617):
```
  DENOMINATOR [gold]: 71 object(s), 71 checked this run, 0 unrendered
  Summary: 71 MATCH, 0 STALE, 0 TIMEOUT, 0 AWS_UNREACHABLE, 0 ETAG_NOT_COMPARABLE
  -> GO. Publish fired in the SAME command, so nothing could commit between the read and the write.
```
`--asof 2026-09-01` DERIVED from `lib.trading_calendar.expected_last_trading_day`, never typed.
Inputs ALIASED from 2026-08-28 partitions, declared by the port on its own face.

**THE ORACLE -- per-key manifest statuses, NOT rc** (`manifest_2026-09-01_dd010893bd28.json`;
also served at `s3://opal-data-portal-v2/platinum/advi/49financial/_manifests/2026-09-01/dd010893bd28.json`):
```
  rows (DENOMINATOR): 11
    published          4
    emitter_refused    7      <- BY DESIGN, not a failure
  HARD_FAIL (error/no_payload/twin_diverged/verify_absent): 0
  VERDICT: CLEAN
  publisher DENOMINATOR line: 11 twin(s) attempted of 26 EMIT twins (23 emitter entries); 7 not clean
```
⛔ The publisher's own `7 not clean` and `rc=1` are the EXPECTED clean outcome and must not be read as
failure -- `emitter_refused` shares the `bad` bucket with real faults by construction.

**PUBLISHED (4), and the attempted set was RE-READ at fire time rather than remembered** -- it matches
this session's dry-run census exactly, and still contradicts the chain docstring's 2026-08-25
`{would_publish: 6, emitter_refused: 5}` in both directions:

| leaf | manifest sha256 | manifest bytes | LISTED on S3 | LastModified (UTC) |
|---|---|---|---|---|
| `perfrp_performance_account.json` | `b09f277a654be0bc…` | 1,923,593 | ✅ 1,923,593 | 03:16:07Z |
| `perfrp_gainloss_relationship.json` | `6d382530b531e77f…` | 7,419,826 | ✅ 7,419,826 | 03:16:43Z |
| `perfrp_gainloss_account.json` | `f03a95d506e22aea…` | 11,896,644 | ✅ 11,896,644 | 03:17:03Z |
| `perfrp_book_advisor.json` | `a53b041dc1324779…` | 15,001,561 | ✅ 15,001,561 | 03:18:32Z |

**LANDING VERIFIED BY LISTING (`s3api list-objects-v2`), never HeadObject alone (13c)** -- and the
listed byte sizes match the manifest exactly on all four, which is independent corroboration rather
than the producer's self-report.

**REFUSED BY DESIGN (7):** `activity_{relationship,account}`, `performance_relationship`,
`allocation_{relationship,account}`, `transactions_relationship`, `roster_relationship`.

## ⚠ DISCLOSURE -- WHAT THE GO SIGNAL CERTIFIED, AND WHAT IT COULD NOT SEE

Raised by `0.4.0_DS_ClientPlatform~G` (90878 s.4), who noted it *"stood ~6.5 hours unstated, including
through `0.7.0_AE_CloudOps~G`'s activation sweeps."* **Verified independently at this seat, with a
positive control:**

```
  git merge-base --is-ancestor 9c7011f93d origin/CLOUD   -> NOT ON ORIGIN
  POSITIVE CONTROL   79a2eff0ed                          -> ON ORIGIN  (the instrument can see ancestry)
  origin/CLOUD at read time: 173a873139
```

>> **SINCE 00:10Z, `s3://opal-data-49financial/_code/` HAS BEEN SERVING BYTES WHOSE AUTHORIZING COMMIT
   IS NOT ON `origin/CLOUD`. This activation therefore ran emitter code that is CORRECT but whose
   authorizing commit is unpushed.** It is the INVERSE of the staleness class this session chased --
   the served plane is AHEAD of the record, not behind it. <<

⛔ **AND THE SCOPE LIMIT IS ON MY OWN GO SIGNAL, WHICH IS THE PART WORTH KEEPING.**
`comp-pipescript deployed` compares **LOCAL WORKTREE ↔ S3**. It read `71 MATCH / 0 STALE`, and that is
TRUE and is exactly what the signal was for: the publisher ran against the code S3 actually serves.
**But the instrument does NOT compare ORIGIN ↔ S3, so it could not have detected this divergence by
construction** -- a clean `MATCH` says nothing about whether the matched bytes are on the record.
**A currency check against the DEPLOYED plane is not a currency check against the RECORD.**

**This does NOT invalidate the activation:** the emitters that ran are the correct post-sentinel bytes
(`perfrp_emit_core.py` `6adffc4949…` @00:10:20Z et al.), the published leaves are correct, and a
publish's correctness does not depend on push state. **It DOES mean the push resolves an existing
divergence rather than creating one** -- and the four published leaves above were produced by emitter
code in that state. Stated here because my own report gave push state for the LEDGER COMMIT and not for
the EMITTER CODE, and those are two different objects.

## What this act did NOT do

- **No PROD portal promote.** Separate act, separate branch, not approved and not asked.
- **No standing publish authorization.** 90617 covers this activation and nothing else.
- **Pseudonymisation and book-scoping are RE-HOMED, NOT RESOLVED** -- a top-down all-keys project on
  Andrew's word. Re-homing is not remediation, and no seat may record either as resolved.
- The served leaves carry what this session measured and reported before firing: raw custodian account
  ids at account grain (`performance_account` 8,632, `gainloss_account` 6,183) and client display
  labels in `book_advisor`. **That was measured, escalated, ruled on by Andrew directly, and published
  with the facts in front of him** -- not discovered afterward.
