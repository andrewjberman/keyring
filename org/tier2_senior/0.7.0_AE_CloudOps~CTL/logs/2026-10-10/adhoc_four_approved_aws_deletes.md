# 0.7.0_AE_CloudOps~CTL -- ADHOC four approved AWS deletes

**Date:** 2026-10-10 | **Seat:** 0.7.0_AE_CloudOps~CTL | **Device:** laptop | **Branch:** box/laptop
**Order:** `ADHOC.delete-retired-tfstate-orphan-loggroup-stray-demand-state-20261010` (issuer `2.0.0_SA_COO~C`)

**archetype:** DEPLOY

Four unrecoverable-class AWS deletes on Andrew's verbatim per-item word. All four executed 13:56:18Z -
13:56:25Z, all four verified absent with a positive control on the same instrument, ledger CLOSED
13:58:50Z. Issuer closed the order `complete` with **AC1 graded MET** on its own independent live re-read.
Receipt and the four hashed copies: `deliverables/ADHOC_DELETES_20261010/`, commit `46cca3496a`, on origin.

## What this entry is for: three habits worth keeping on a delete order

**1. Verify the authority at the pin, not from the relay.** The order cited Andrew's record @`d02b5d81e1`
with a verbatim quote. I printed the record's bytes with `git show <pin>:<path>` rather than grepping for
the quote (CLAUDE.md: a citation ages separately from the text it quotes), and ran a bogus path at the same
pin as a control so the read could not be a mangle returning clean-empty. His words were as cited, and his
item map named exactly four targets -- item 12's "yes delete" is a dell2-local folder and stayed untouched.
For an irreversible act this is the gate, and it costs two calls.

**2. A measured zero still needs its reason.** `comp-find '<state key>' infra` read **0 hits over 12,923
files** for both T1 and T2, with a working control (289 `tfstate` hits in the same scope). I then read the
root directories and found the reason: both "retired roots" still exist as **directories holding no `.tf`
file at all** -- husks. A bare `test -d` printed "ROOT STILL PRESENT", which is literally true and would
have read as a STOP condition on its own. The zero and the husk together are the finding; either alone
misleads.

**3. The order's own control can be unrunnable -- say so and substitute deliberately.** Step 5 asked for
"a sibling object in the same prefix still reads 200" after each S3 delete. For T4 the deleted object was
the **lone object under the whole `demand_state/` prefix**, so the prefix is now empty and no same-prefix
sibling exists. I used the same-bucket canonical key instead, which is the stronger control anyway: it
proves the live request is unaffected.

## The T4 finding, because it is the one that mattered

The request's own definition (`org/missions/D8/MDPF/MDPF_DEMQUE/requests/ETFS_RIVALS-HISTORY-OWED-DAILY.json:28`)
declares `state_address` under **`request_state/`**, not `demand_state/`, citing MDPF_DEMQUE PRD ADDENDUM
v0.4. That canonical object is live -- 191 B, written 09:38:34Z, **four hours after** the 05:10:13Z stray
being deleted. So the live producer and any consumer read a different key, and the delete could not affect
them. Without that read, a 35-hit census on the request id looks like evidence of a reader.

## Recoverability, stated rather than assumed

Both buckets read `get-bucket-versioning` **Enabled** *before* the deletes, so T1, T2 and T4 left delete
markers and their object versions survive -- reversible by deleting the marker, with hashed local copies as
the second path. **T3 is different and was reported as such:** a CloudWatch log group carries no
versioning, so its 4,811 bytes of events are gone for good; only the saved metadata remains. Andrew's word
covered it explicitly. Checking versioning first is what turns "unrecoverable delete" into a statement with
a known answer per target instead of one blanket assumption.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `'canonical-schwab-si2-schedule/tfstate' infra`, `'opal-assets-absence/tfstate' infra`, `'tfstate' infra` (control), `-i 'ETFS_RIVALS-HISTORY-OWED-DAILY'` | 0 / 0 over 12,923 files with a 289-hit control; 35 hits over 245,998 files for the request id. The rail denied one directory-scoped `grep -rn` on the roots mid-task; `ls -1a` on the named directories answered it and produced the husk finding |
| `deploy_ledger.py` | `open` (4 legs) / `close-leg` x4 / `close` | opened before any act naming all four targets; each leg closed with its own before/save/delete/after proof; sentinel removed |

`comp-schedule` and `comp-iam` were DECLARED-NOT-APPLICABLE by the order (no schedule and no policy
change); step 2's reads covered the scheduled-reader question for T4 directly.

## Blockers

None. No target was STOPPED. AC1 was judgment and the issuer graded it MET.

## Session position

This lane now holds five terminal orders (NFRA_CTLPLN TO-APPLY-28, -29, -30, -31 and this ADHOC), eight
ledger entries opened and closed, zero sentinels. Across the session: zero `GetSecretValue` calls, zero
function invocations, zero test sends, zero untargeted applies, and no prefix, wildcard or recursive
delete. Event-driven hold; zero crons.
