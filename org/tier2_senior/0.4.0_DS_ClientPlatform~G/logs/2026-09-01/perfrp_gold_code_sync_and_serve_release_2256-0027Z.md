# ADVI_PERFRP -- advi:gold `_code/` sync driven to 71 MATCH / 0 STALE across a sovereign hold discharge, plus a fail-open found in the gate that enforces the hold

**archetype:** MIXED
**secondary_archetypes:** DEPLOY (primary), DIAGNOSE, VALIDATE

**Serial:** `0.4.0_DS_ClientPlatform~G` | **Window:** 2026-08-31T22:56Z -> 2026-09-01T00:27Z
**Seating:** `2.0.0_SA_COO` 90157 -- ADVI_PERFRP ONLY (Rule 27), DS lane under Rule 13, BUILD-ONLY cap.
**Commits (3):** `b0afc8fbf5`, `9c7011f93d`, `7164a891ae` -- all **LOCAL** (`ls-remote` read;
push is INTEGRATOR-ONLY on CLOUD per LD-0367, not overridden). They move at the integration window.

---

## Current State

**The seated task is COMPLETE.** `s3://opal-data-49financial/_code/` now serves origin's bytes for
every gold script:

```
comp-pipescript deployed --pipeline advi   (final)
  DENOMINATOR [gold]: 71 object(s), 71 checked this run, 0 unrendered
  71 MATCH, 0 STALE, 0 TIMEOUT, 0 AWS_UNREACHABLE, 0 ETAG_NOT_COMPARABLE
```

The stale-core finding that opened the thread is closed: all 11 registered PERFRP wrappers now load a
deployed `perfrp_emit_core.py` that matches origin, instead of an object written 2026-08-25 that
predated 13 commits touching that file.

**Six objects served, in two acts separated by a sovereign discharge.**

| file | ETag now | written (s3api, UTC) |
|---|---|---|
| `a01_runner.py` | `3e1cf87cdaa6c497fe2968651b0129aa` | 2026-08-31T23:16:12Z |
| `d06_firm_mix_summary.py` | `64c186144cca44d202bcbe5b81ed1fe0` | 2026-08-31T23:16:17Z |
| `d14_advisor_nna_canonical.py` | `d7283d0911cfcee676245f2dab33b145` | 2026-08-31T23:16:21Z |
| `perfrp_emit_core.py` | `6adffc4949ffbfffea2d9a3ff116ab1f` | 2026-09-01T00:10:20Z |
| `perfrp_rollup.py` | `f01dd090d503776a79b16b033e5a0b27` | 2026-09-01T00:10:24Z |
| `perfrp_transactions.py` | `1ebf3016a32f79311289dec08812e1e5` | 2026-09-01T00:10:28Z |

**Repo home** `data/assets/scripts/gold/runners_49f/` -> `_code/` (`safe_deploy_core.py` CODE_TREES
`advi`, `deploy_gated: True`). HEAD == `origin/CLOUD` @`5b10b4eda0` at act 1; worktree == `git show
HEAD:<path>` by md5 for all six, so the served bytes ARE origin's and the autocrlf class is excluded
by measurement (`safe-deploy` independently: `worktree CR count 0 / index CR count 0`).

**Ledger:** `org/critical_paths/change_management/20260831T2320Z_advi-gold-code-sync-perfrp-serve-held.md`
-- CLOSED-COMPLETE @`7164a891ae`, carrying pre/post ETags for all six objects (nothing else in the
fabric holds the pre-sync values).

---

## What happened, in order

**1. Act 1 -- the task as issued was self-cancelling for its own primary target.**
Seated to sync six STALE rows "inside the BUILD-ONLY cap", `perfrp_emit_core.py` first. Re-derived the
STALE set twice as bound (`0.7.0_AE_CloudOps~G` 90166 s.3: a TIMEOUT is not a MATCH) -- both runs
65 MATCH / 6 STALE, identical set, 0 non-verdict rows, denominator 71/71/0 printed. `safe-deploy.sh`
served three and REFUSED three: each PERFRP file carried at line 1
`# DEPLOY-SERVE-HELD: ADVI_PERFRP.TO-R2-DS is BUILD-ONLY (Andrew 2026-08-19 open-calls`,
enforced at `safe_deploy_core.py:290` (`SERVE_HELD_RE`), removal gated at `:281-282`.
**The cap named as the task's boundary was the mechanism refusing the task.** Negative control: the
three that deployed carry the sentinel zero times. Reported at 90231-90234; `2.0.0_SA_COO` (90236),
`1.0.0_SA_CTO` (90240) and `0.7.0_AE_CloudOps~G` (90262) each corrected their own records at source.

**2. Discharge.** Andrew discharged the 08-19 cap (relayed `1.0.0_SA_CTO` 90310 s.1, record
`ce77e285b1`); 90310 s.3 handed the sentinel removal to this lane BY NAME -- the explicit hand-over
this seat had said at 90264 it would not assume. `2.0.0_SA_COO` 90331 s.1 sequenced it GO NOW.

**3. Act 2 -- release and complete.** Removed the full sentinel comment BLOCK from all three
(8+5+5 = 18 deletions), not only the regex-matching line: leaving the continuation lines would leave
text still reading as a live hold while no longer matching `SERVE_HELD_RE`. Committed @`9c7011f93d`
with `SERVE-RELEASE-ACK:` non-empty on one line, pre-checked against `SERVE_RELEASE_ACK_RE` itself.
Re-derived twice again (68 MATCH / 3 STALE both runs, 0 non-verdict), then `safe-deploy.sh`.
**Never `aws s3 cp`.** `SERVE_HELD_RE` / `SERVE_RELEASE_ACK_RE` byte-untouched throughout.

**4. The finding, against my own act.** No `OK: SERVE-RELEASE authorized` line printed and no entry
appeared in `org/safe-deploy-bypass-audit.log` (newest SERVE-RELEASE row still 2026-07-13).
`_resolve_serve_refs` (`:964-980`) pins `old_ref="HEAD~1"` for an explicit-file invocation, **resolved
at DEPLOY time**. Two peer commits landed in the 12 minutes after `9c7011f93d`; `9f0d8a84dc` at
00:10:17Z, **3 seconds** before the first object write. So `HEAD~1` was `be22deaf9e`, already past the
removal: sentinel 0/0/0 there vs **1/1/1 at the release commit's true parent `a50dd6721a`** (positive
control). `_old_blob_has_serve_held` returned False, `removed` came back empty, and the ACK check AND
the audit write were skipped together. **A valid ACK was present and never read; with no ACK at all
the deploy would have run identically at rc=0.** Reported 90422-90426; `3.0.0_SA_CVO` 90431 CONFIRMED
by a different instrument (code read vs this seat's runtime + blob control) and named the root cause
as a wrong QUESTION, not a wrong ref -- `HEAD~1` answers "what changed most recently", an
authorization gate needs "what did the AUTHORIZING commit change."

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-pipescript deployed` | `--pipeline advi` x6 runs | PASS | 71/71/0 unrendered every run. Pre 65/6, post-act-1 68/3, final **71 MATCH / 0 STALE**. 0 TIMEOUT / AWS_UNREACHABLE / ETAG_NOT_COMPARABLE in all six. Run TWICE before each sync, as bound. |
| `comp-pipescript io` | `<script> --pipeline advi` x3 | PASS | rc=0 on all three released scripts. rollup/transactions report a MEASURED zero over the recognizer set (library modules), denominator printed. |
| `comp-which` | "how do I deploy gold scripts to the advi _code S3 directory" | PARTIAL | Returned a 3-way near-tie, none of which was `safe-deploy.sh`. Router did not surface the Rule-13 deploy path for a deploy question. |
| `comp-find` | `--name` x7 | PASS | Located the 6 scripts + `build-and-upload.sh` census (6 hits / 144,247 scanned, corpus=all, ephemeral floor printed). |
| `.tools/safe-deploy.sh` | 3 invocations | PASS/PARTIAL | Act 1 served 3 of 6 (3 SERVE-HELD refusals); act 2 served 3 of 3. Per-script `VERIFY OK` each. |
| `.tools/safe-commit.sh` | 3 commits | PASS | commit-gate clean 3 of 3 on the `.py` commit; msg-verify MATCH on all three. |

**What worked:** `comp-pipescript deployed --pipeline advi` is the whole reason the shared-core
staleness is visible at all -- and running it TWICE is what makes it trustworthy, exactly as
`0.7.0_AE_CloudOps~G` warned. The HALT gate in `safe-deploy` earned its keep twice: it surfaced the
19:37Z revert incident and `0.6.2_AE_PartnerETL` 90208 before I served files named in both.

**What failed:** `safe-deploy`'s SERVE-RELEASE audit did not fire on a real sentinel removal (s.4
above) -- a fail-OPEN in a block whose header at `:283` claims "All three checks FAIL CLOSED". True of
every ERROR path; nothing errored, the PREMISE lapsed.

**Gap found:** (a) the `HEAD~1` baseline race above -- owner `1.0.0_SA_CTO`, and a fix must not loosen
either regex since the defect is the chosen BASELINE. (b) `safe-deploy` handed SIX files, serving
three, printed `OK: safe-deploy gate PASS -- all 3 file(s) deployed and verified` at rc=0 -- the PASS
line re-denominates to what was ATTEMPTED, not what was ASKED FOR. Routed to `3.0.0_SA_CVO`.

---

## Briefs Written

None. This window produced a change-management ledger entry and MCP reports, not a brief; the
durable record is `20260831T2320Z_advi-gold-code-sync-perfrp-serve-held.md` @`7164a891ae`.

---

## Files Modified

See commit messages: `b0afc8fbf5`, `9c7011f93d`, `7164a891ae`. Summary:

| file | change |
|---|---|
| `data/assets/scripts/gold/runners_49f/perfrp_emit_core.py` | -8 lines: sentinel block only, no logic change |
| `data/assets/scripts/gold/runners_49f/perfrp_rollup.py` | -5 lines: sentinel block only |
| `data/assets/scripts/gold/runners_49f/perfrp_transactions.py` | -5 lines: sentinel block only |
| `org/critical_paths/change_management/20260831T2320Z_advi-gold-code-sync-perfrp-serve-held.md` | new, then CLOSED-COMPLETE update |

---

## MCP Traffic

**13 messages read and acked** (90157, 90166, 90172, 90236, 90240, 90262, 90310 acked by id; 90331,
90368, 90378, 90208, 90427, 90431 read). **4 dispatches sent, 16 per-recipient deliveries**
(90231-90234 the sentinel collision; 90264-90267 ACK + the credit correction; 90422-90426 completion +
the fail-open; 90434-90436 my own retraction). 15 DELIVERED / 1 QUEUED / 0 REFUSED.

Significant: **90310** (Andrew-direct discharge + explicit hand-over of the removal), **90331** (GO
NOW), **90378** `[STOP]` (CALL 2 serve halted; CALL 1 exempted by name), **90431** (CVO confirmation
of the fail-open by a second instrument).

---

## Corrections issued against my own record

1. **90264:** three messages credited this seat with FINDING the sentinel. **The gate found it.** I ran
   all six expecting a six-file sync and read an unexpected refusal. What this seat did was stop rather
   than reach past `safe-deploy.sh` to `aws s3 cp` -- which was in lane under Rule 13 and would have
   violated a sovereign hold at rc=0. The protection is that the canonical path carries the check.
2. **90434:** my 90422 s.2 stated CALL 2 resumption "needs a CTO ruling or an Andrew waiver". Both had
   arrived 13 minutes earlier in 90406 -- a message not addressed to this seat. **I asserted a
   fabric-wide condition from my own inbox, which is a per-recipient slice.** The operative conclusion
   ("this report is not your GO") held anyway because the activation signal was independently never
   re-named -- a right answer off a stale premise, which is luck, not method. Retraction scoped to the
   refuted clause only.

---

## Blockers

**None at this seat.** Two items are owned elsewhere and correctly gated, neither a stall:
- The `HEAD~1` fail-open -- owner `1.0.0_SA_CTO` (gate owner), CONFIRMED by `3.0.0_SA_CVO` 90431.
  Explicitly not fixed here; I may not touch either regex.
- CALL 2 activation -- `0.7.0_AE_CloudOps~G`, awaiting a re-named signal from `2.0.0_SA_COO`. That seat
  declined to fire even on its own independently-measured 71 MATCH / 0 STALE sweep, which is correct:
  a measured world-state is not a named signal.

---

## Next Steps

1. **[`1.0.0_SA_CTO`]** Rule the `_resolve_serve_refs` baseline. The defect is WHICH baseline, not the
   patterns -- pinning to a merge-base or widening the scanned range both change what authorizes a
   serve. Also open, and unanswerable from the log: **whether any past SERVE-RELEASE was silently
   waived.** A skipped check and a genuinely-absent removal write the same nothing.
2. **[`2.0.0_SA_COO`]** Re-name the CALL 2 activation signal, or state that none is coming. 90332 named
   this seat's report, 90365/90368 withdrew it, and 90406 resumed CALL 2 without re-naming one.
   `0.7.0_AE_CloudOps~G` 90420 is holding for exactly one line.
3. **[`0.4.0_DS_ClientPlatform` base, or whoever seats PERFRP next]** Per `0.6.2_AE_PartnerETL` 90208:
   four of the eight files destroyed in the 19:37:15Z revert are the PERFRP/TWR lane. **Whoever is
   seated inherits those files at their 2026-08-29 COMMITTED state; any 08-30/08-31 working-tree work
   in them is gone and unrecoverable.** This did NOT contaminate tonight's deploy -- the revert
   restored files to committed state, so the sync shipped exactly the 08-29 bytes it intended.
4. **[integrator `0.0.0_AB_MSTR`]** Three LOCAL commits await the integration window.
