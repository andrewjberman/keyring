# Four IRPT_BCKEND releases landed, and the graders that would have passed on a false value — 0.7.0_AE_CloudOps~IB2

**Date:** 2026-10-09
**Task Order:** IRPT_BCKEND.TO-IB-pr-395, -397, -398, -401 (COMPLETE); -404 (L6 open, held); -413 (HELD)
**Status:** COMPLETE for four orders; one gated

**archetype:** DEPLOY

---

## Objective

Seated at launch for IRPT_BCKEND only, work the task orders `2.0.0_SA_COO~P2` delivers. Six arrived across the
session, each a WORLD-risk release under a never-widen pair. Four landed and closed; one is held on a signed
ruling; one waits behind it.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open \| close-leg \| close \| hold \| check` x4 slugs | PASS | `hold` correctly REFUSED a half-landed deploy, which is the behaviour that kept IB-pr-397's entry RED instead of quietly parked |
| safe-apply.sh | `-chdir=<root> apply <saved planfile>` x9 applies | PASS | every apply from a saved, pre-graded plan; no bare `terraform apply`, no console edit, no `update-function-code` |
| build-and-upload.sh | `BUILD_ONLY=1` then plain, 11 builds | PASS | every artifact built twice byte-identical before any upload |
| safe-commit.sh | `--author ... -F <msgfile>` x20 | PASS | message files written by the Write tool, never a shell heredoc |
| safe-merge.sh | 7 drains | PASS | refused twice while another seat held the shared worktree lock, and once on a real source-map conflict; both refusals were correct |
| proof-of-spec-check.py | 4 instances | PARTIAL | caught a dangling decomp cell (true), then crashed rc=2 fabric-wide on a schema defect (see Decisions) |
| symbol_closure.py | on the IB-pr-409 built zip | PARTIAL | `missing=0 PASS`, but its first control did NOT discriminate: deleting a whole module still PASSES with the pair count falling 28 -> 19 |
| reread_27.py | TCKT_VNEXT 27-route census | PASS | `READ27 27/27` rc 0, run here rather than copied from the issuer's read |
| comp rail | denied 4 raw searches | PASS | each answered with the named-file read or native Grep; no `# rail-checked` override and no `/freeform` |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | IB-pr-395: build 6 hosts at census pin `71e9aacf27` | all six sha256 == packet table |
| 2 | replay re-run before the ledger | BYTE-IDENTICAL to the packet's record (`PupboWdR...`) |
| 3 | upload 6, targeted applies | 6x `0 added, 1 changed, 0 destroyed`; all read back == built |
| 4 | IB-pr-398: `irpt-holdings` at pin `c18b5fec74` | `CKpZUMD5...`; parity gate PASSED with no skip |
| 5 | IB-pr-404: 3 narrow bundles, digest gate | 3 of 3 exact on sha256, md5, bytes and metadata |
| 6 | upload 3 one at a time, read back by new version id | all three content-sha256 == built |
| 7 | L5 replay on the UPLOADED bytes | 18 of 18 arms match the packet |
| 8 | IB-pr-397: reader first mint `WJUEl6Gl...` | targeted apply `5 added, 0 changed, 0 destroyed` |
| 9 | IB-pr-401: `irpt-narrative` at pin `b8a49eee0e` | `iEwSFL34...`; enforcer-scope arm IDENTICAL |
| 10 | 4 ledgers CLOSED, 4 proofs VALID, 4 statuses flipped | drained `770f25558f`, `236d19e1ae`, `4f15fc23f7`, `65d555c165` |

## Verification

```
reread_27.py (run by this seat, 15:1xZ):
  irpt-directory-search      4 2026-10-09T07:38:06 87d9ecc4 CLAMPED
  irpt-export-render         5 2026-10-09T07:47:08 87d9ecc4 CLAMPED
  irpt-holdings              1 2026-10-09T09:11:24 87d9ecc4 CLAMPED
  irpt-narrative             1 2026-10-09T14:48:05 87d9ecc4 CLAMPED
  irpt-performance-adapter   1 2026-10-09T07:41:59 87d9ecc4 CLAMPED
  irpt-status                6 2026-10-09T12:45:28 87d9ecc4 CLAMPED
  irpt-ycharts-generate      3 2026-10-09T09:32:22 87d9ecc4 CLAMPED
  READ27 27/27                                              rc 0

irpt-commentary-composition-read-lambda  ZZmWOFSA/GjO0d/cKHSm9G5+xDc5sNfEHOpbmfIabQ0=  (first mint)
49financial  irUPjpfrDLoM2zhnhunbBtIG9fP275kI  inflection qR5sZza4EjUT_cbGA5hLo0ar6zu2NfpI
cottonwood   oyIYMVdh_l2zCg5ZWvn3ISPPS6_9Q82_
```

---

## Decisions Made

1. **Four graders would have passed on a value I could have typed.** A relabelled WIDENS arm, a fabricated
   `narrative_census_row`, the void `QiNRKpaC` sha, and an unearned `"ONE"` — in each case the check reads a JSON
   field or a resource count and cannot see a wrong value. Each was reported as FAIL or held instead, and in three
   of the four the issuer re-cut the criterion. **The lesson for a successor: when a check is cheap to satisfy, that
   is the moment to measure, not the moment to write.**
2. **A resource-count guard cannot see a same-resource attribute.** IB-pr-395's ycharts plan carried release 6's
   `~ layers` AWSSDKPandas line inside its own `1 change`; my guard graded `0/1/0` plus two grepped keys and missed
   it. The CTO ruled KEEP and made line-by-line printing a standing rule. Every later apply in this session printed
   every changed attribute.
3. **Five of eleven rows were defects in other seats' carriers,** found by reading the artifact rather than the
   paperwork: a decomposition truncated 142 cells -> 3 (300 of 301 orders left citing an absent cell), a schema that
   pasted prose into its own `"type"` keyword and crashed its validator, a duplicated log group in two sibling
   Terraform files, and stale constants in a round check. All fixed by their owners the same day.
4. **Stopped three times rather than proceed on a plausible reading:** IB-pr-397 at a plan that could not succeed;
   IB-pr-401 at a non-identical enforcer-scope arm, before any upload; IB-pr-401 again at a CTO condition a sequence
   amendment did not relax. Each stop produced a ruling and then a clean landing.

---

## Files Modified

Four after-reads files and four proof-of-spec instances under
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/`; four ledger entries under
`org/critical_paths/change_management/`; `infra/aws/lambda/ci/lambda-source-map.json` (eight artifact rows plus the
reader's registration); `infra/aws/terraform/investor-reporting/export/commentary_composition.tf` (the CTO-ruled
log-group fix, pin `d5a48694a3`); eleven rows appended to the project's surprise channel.

---

## Blockers

**IB-pr-404 L6 — the only open leg.** The 14:15Z fire published cottonwood and inflection but SIGKILLed
49financial (`rc=137`) after 5m09s, before it printed either verdict line; its manifest is unmoved and no refusal
record exists, so it serves a publication one business day behind the other two. Its three previous fires all
succeeded, and today was the first on this bundle — association, not proof: the other two firms had finished two
minutes before the kill, so it was largely alone on a 4 GiB `t3.medium`, and it is much the largest firm. CTO
ADDENDUM 19.1: no rollback, keys stay as landed, L6 stays OPEN while `2.0.0_SA_COO~P2` cuts a memory cell; if no
fix is signed by **Monday 13:00Z**, 404's signed Branch B runs on the 49F key ONLY, by an amendment from that seat.
Row `IRPT_BCKEND-D2-S56`.

Also open and NOT this seat's: row `IRPT_BCKEND-D2-W272-S1` (a caller WITH a profile row classes OPAL_GLOBAL where
live classed UNKNOWN — stated by the packet, unwidened by IB-pr-401, the signer's call); and the
`commentary_draft_store.tf` duplicate log group (row S50), which will half-land that order unless its owner applies
the same one-line fix.

---

## Current State

Four orders COMPLETE with proofs VALID and ledgers CLOSED. Nothing half-landed: every artifact read back equal to
its built value, every re-plan clean, every rollback source retained and measured. One ledger open by design.
IB-pr-413 HELD behind 404's close. Push state LOCAL throughout — the integrator moves origin.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~IB2]` Event-driven hold: act on the next `[INBOX]` event the same turn; re-arm the Monitor
   on its `[WATCHER-EXPIRED]` line, same turn, one call, no skill load.
2. `[2.0.0_SA_COO~P2]` Cuts the 49F memory cell (peak RSS vs 4 GiB, an 85% line, and a fix). This seat does not
   chase it and does not re-run the producer ad hoc — a re-run would be a production publish off its own clock.
3. `[0.7.0_AE_CloudOps~IB2]` On a signed fix: close 404's L6 against the next scheduled fire's output line and
   refusal record, never the SSM status, then close the ledger — which is IB-pr-413's start gate 2.
4. `[0.7.0_AE_CloudOps~IB2]` If Monday 13:00Z passes with no fix: expect the issuer's amendment and run Branch B on
   the 49F key only, by `copy-object` from `3Q_W49U7kMa_xO30Q6LQE7QLsFu7ARur`, never through a WORSE window.
5. `[0.7.0_AE_CloudOps~IB2]` A durable output sink for the holdings commands is worth asking for: no S3, CloudWatch
   off, so a successful run's verdict line is permanently lost to the 24,000-char cap. Today the only line that
   survived did so because its run died early enough to fit.
