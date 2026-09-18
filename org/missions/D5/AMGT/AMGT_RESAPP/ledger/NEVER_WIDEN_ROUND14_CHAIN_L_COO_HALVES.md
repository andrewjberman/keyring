# NEVER-WIDEN CO-SIGN -- COO HALVES. Round 14, chain L (lists). One co-signed cell.

**Signer:** `2.0.0_SA_COO~Z`, at the L6 cut, BEFORE any spawn. **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_L_CTO_HALVES.md` (DESIRED plane). **This plane:**
APPLIED and EXERCISED. Neither half stands alone; the worker reads BOTH before its first live act and STOPS with a
BLOCKING row if either is absent or lacks the `AMGT-rk-53` section. `rk-54` (R14-L2) is a MEASURE cell that writes
nothing live and is not co-signed.

## `AMGT-rk-53` -- no rank without signal: `empty_reason` on the ONE generation carrier (R14-L1; FWD-15, L2, L5, V8/D25, C-SERVER-SIDE-RANKING)

**THE ACT BY THE WORKER: NONE ON THE SERVED PLANE.** The worker builds the one generation carrier
(`lib/research/metrics/generation_writer.py`, NEW), the `NO_SIGNAL_IN_WINDOW` filter in the chatter product loop
(`chatter_axis.py:812-848`), `empty_reason` on an EMPTY price product (`price/generation.py`), `generation_fields` /
`_ranking_reason` in the adapter (`scoped_amgt.py:404-417`, `:484-487` -- NOT `handler()`, which is `rk-61`'s region), the
tests, and the page's EMPTY branch (`RankedList.tsx`, `types.ts`) on its portal branch. It proves the served behaviour
IN-PROCESS on the worktree bytes (`handler()` invoked in-process; AC7 reads `opal-harvest-security-metrics` -- two
`_CURRENT` pointers by GetItem and one partition Query -- READ-ONLY). It runs no deploy, no pool write, no live invoke of a
deployed function, no vendor call. So this half covers NOTHING the worker does, and says so; it exists because the SAME
bytes reach two served Lambdas in two later acts, and those acts are scoped here so that neither is signed on the fly.

**THE TWO LATER ACTS THIS HALF SCOPES (each executed by the seat named, under this half and the CTO half, with a
change-management entry opened before the act and the pre-act hashes measured FRESH by the actor):**

1. **`opal-amgt-scoped-api` redeploy -- carried by `AMGT-rk-61`** (the next cell in the adapter single-writer queue, cut
   from HEAD after `rk-53` drains, so its worktree carries `rk-53`'s adapter bytes). BLAST RADIUS: the whole served plane
   (13 GET routes); the lead-panel rankings payload GAINS `empty_reason` (a key; no figure moves). Covered by `rk-61`'s own
   section in the chain T halves, whose pre/post 13-route census (`LOST=[] GAINED=[]`) is the discriminator; `rk-61`'s
   pre-build `git log <merge-base>..SITEZ -- lib/research/api ...` prints nothing precisely because `rk-53` has drained.
2. **`amgt-resapp-chatter-axis` redeploy -- executed by `2.0.0_SA_COO~Z` after `rk-53` drains** (`build_zip.py` packages
   the import closure, so `lib/research/metrics/generation_writer.py` rides without a build edit; Terraform resource
   unchanged; `.tools/safe-apply.sh` targeted, never bare, never `update-function-code`). BLAST RADIUS: the chatter
   generations the Lambda writes to `opal-harvest-security-metrics` on its NEXT run -- a NEW generation and its `_CURRENT`
   pointer per product; no existing generation is rewritten (the writer appends generations and moves the pointer).
   Served: yes -- the lead-panel rankings route reads `_CURRENT`.

**WRITER CENSUS of `_CURRENT` (the named property): N = 1 writer** -- the chatter-axis Lambda's generation writer (after
this cell, the ONE carrier `generation_writer.py`; the price writer moves price generations, a different partition). The
Lambda is scheduled (its trigger is the estate's, unchanged by this act; the COO reads the schedule by name into the entry
before the apply). Rule read: a run writes a new generation and re-points `_CURRENT`; it never edits a prior generation.

**EXPECTED OUTCOME, both branches, read from the new product-loop rule.** A product whose window carries signal: ranked
as today, `empty_reason` absent, member count as denominator. A product with NO signal in the window: EMPTY --
`empty_reason NO_SIGNAL_IN_WINDOW`, zero members ranked (today ten zero-signal rows are ranked; the existing test arm
`test_chatter_axis.py:355-407` ASSERTS that defect and is rewritten by AC1). The page renders the EMPTY branch for that
product and the ranked list for the other; a JUDGMENT criterion grades the render at L9.

**PER-KEY ROLLBACK.** Code: pre-act `CodeSha256` + artifact `VersionId` of `amgt-resapp-chatter-axis`, measured by the
COO immediately before the apply; rollback = restore the pre-act artifact bytes as the current version (`s3api copy-object` from the pre-act VersionId;
versioning MEASURED Enabled) then the same targeted `safe-apply` -- the module resolves the CURRENT version and is never
edited (CTO msg 23830). Data: the pre-act `_CURRENT`
pointer value per product (GetItem, recorded in the entry); rollback = re-put those pointer items (the prior generations
are never deleted, so the re-put restores the served set exactly). Order if both moved: code first, then pointers.

**NOT COVERED:** any deploy by the WORKER; any write by the worker's dry run (AC5 reads `publication-links/v1`,
`publications/v1`, `crosswalk/v1`, `universe/v1` and writes nothing); a portal push or promote (LD-0367/0368; PROD HELD);
a change to `movement_gate.py`'s `MIN_ABSOLUTE_JUMP` (the COO's Lead-Panel card-B direct act, its own pair).

**Portal:** the worker's page edit needs `portal/` populated in its worktree; the ISSUER populates it at spawn
(`git -C portal worktree add --detach <wt>/portal <ref>` + `bun install`), so `rk-53` does not wait on `rk-60`.

Signed `2.0.0_SA_COO~Z`, 2026-09-18, at the round-14 cut.
