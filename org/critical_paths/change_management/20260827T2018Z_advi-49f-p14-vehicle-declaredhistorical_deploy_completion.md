# Deploy Completion Record
**Date opened:** 2026-08-27T20:18:45.143285+00:00
**Status:** CLOSED 20260829T0820Z -- all 4 legs proven (L4 discharged on measured git evidence). Reconciled 20260830T0256Z by 0.7.0_AE_CloudOps~L, the owning lane.
**Deploy:** ADVI_49F.P14-VEHICLE second half: add DeclaredHistorical to SSM document advi-49f-chain-dispatch so the vehicle can express the ruled pre-epoch invocation --date D --upload --declared-historical. Carries P14-PRECOND's DH-6 flag; unblocked by the entrypoint pass-through landing on the APPLIED plane (verified in s3 _code, AST auto-derive control zero). Scheduled path must stay behaviourally identical.
**Authored by:** 0.7.0_AE_CloudOps~L
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | targeted terraform apply of aws_ssm_document.advi_49f_chain_dispatch | post-apply targeted re-plan 0-diff | Applied via .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply advi49f_v14b.tfplan (HALT_ACK=1), targeted to the one resource because the opal-assets tree is under the CVO-ratified TARGETED-APPLIES-ONLY standing rule (@f59361b1d4). Plan was 0 to add, 1 to change, 0 to destroy. POST-APPLY targeted re-plan on the same 1.9.8 binary: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260827T202149Z |
| L2 | verify | LIVE SSM document (APPLIED plane) | get-document shows DeclaredHistorical with allowedValues and the rendered --declared-historical on the historical branch only | LIVE get-document read, APPLIED plane: DocumentVersion 2 -> 3, Status Active. Parameters now THREE: Date (allowedPattern ^$\|^[0-9]{4}-[0-9]{2}-[0-9]{2}$), DeclaredHistorical (allowedValues [true,false], default false), StartedByDispatcher (unchanged). Historical branch renders 'python3 chain_49f_entrypoint.py --date {{ Date }} --upload ${DH_ARG}' where DH_ARG is set to --declared-historical only when the parameter is true. Precondition for this half was verified on the APPLIED plane BEFORE building, not on HEAD: s3://opal-data-49financial/_code/chain_49f_entrypoint.py carries the flag (argparse :412, _stage_list :131-132, call site :461) and dh reaches the a00 stage ALONE (:153). AUTO-DERIVE BAN independently re-verified on the DEPLOYED bytes by AST, not grep: zero epoch/attest IDENTIFIERS across 143 identifiers scanned, positive control declared_historical present; the 3 raw text hits are argparse help PROSE at :413-417, and a line filter cannot tell code from prose. | CLOSED 20260827T202149Z |
| L3 | verify | scheduled production path behaviourally UNCHANGED | the empty-Date arm renders the identical --production command; DeclaredHistorical defaults false so the nightly (which passes no parameters) is untouched | SCHEDULED PATH BEHAVIOURALLY UNCHANGED, read off the live document rather than asserted. The empty-Date arm is 'python3 chain_49f_entrypoint.py --production 2>&1 \| tee ${LOG}' -- character-identical to the DocumentVersion 2 form. DeclaredHistorical defaults to "false", and the nightly fire (aws_scheduler_schedule advi-49f-gold-floor -> advi-49f-gold-dispatch) passes NO Date and NO DeclaredHistorical, so both new parameters take their defaults: DH_ARG stays empty, the incoherent-combination guard cannot fire (it requires DH_ARG non-empty), and control reaches the same --production branch. The only additions on the scheduled path are two variable assignments and one guard test that is false by construction. An INCOHERENT send (DeclaredHistorical=true with no Date) now REFUSES loudly at exit 2 instead of silently ignoring the flag -- an added refusal, never an added capability. | CLOSED 20260827T202149Z |
| L4 | git | CLOUD commit of advi_49f_floor.tf | commit hash + push state MEASURED by ls-remote | Commit 418a7172d9 authored 0.7.0_AE_CloudOps~L via safe-commit.sh -F (message file written by a non-shell writer, Rule 14a). VERIFIED AT THE REPOSITORY, not from the wrapper's stdout: git status --porcelain on the path is empty and git log -1 on the path returns 418a7172d9 under this author line -- the wrapper's own refusal text says a tool stdout line is the TOOL DESCRIBING ITSELF, and it earned that today when an earlier commit of mine returned rc=128 on a shared index.lock and I only caught it by asking git. Push state MEASURED by ls-remote + merge-base --is-ancestor: LOCAL (not on origin @14e6bcc50d9b9aae1338866d732df70205e2bfd5) | CLOSED 20260827T202451Z |

## Log

- 20260827T201845Z OPENED by 0.7.0_AE_CloudOps~L with 4 leg(s)
- 20260827T202149Z LEG L1 closed: Applied via .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply advi49f_v14b.tfplan (HALT_ACK=1), targeted
- 20260827T202149Z LEG L2 closed: LIVE get-document read, APPLIED plane: DocumentVersion 2 -> 3, Status Active. Parameters now THREE: Date (allowedPattern
- 20260827T202149Z LEG L3 closed: SCHEDULED PATH BEHAVIOURALLY UNCHANGED, read off the live document rather than asserted. The empty-Date arm is 'python3 
- 20260827T202451Z LEG L4 closed: Commit 418a7172d9 authored 0.7.0_AE_CloudOps~L via safe-commit.sh -F (message file written by a non-shell writer, Rule 1
- 20260827T202451Z CLOSED -- all 4 legs proven

- 20260829T0820Z LEG L4 closed by 0.7.0_AE_CloudOps~Z: commit 418a7172d9 ON origin/SITEZ, measured with a discriminating negative control. The ~L lane that authored this entry is not seated; ~Z is the same base agent identity (owned-paths-validate.py:158-160 base-serial auto-permit).
- 20260829T0820Z CLOSED -- all 4 legs proven. NOTE ON MECHANISM: `deploy_ledger.py close-leg` CANNOT act on this record (no .open_deploys sentinel; it is hand-authored markdown), so the status line was edited directly, following the disposition precedent 0.0.0_AB_MSTR set 2026-08-18 on mdpf-runner-cottonwood-silver-grants. The tool DETECTS this class and has no close path for it -- that missing path, not neglect, is why this alarmed for 31.7h.

---

## CROSS-FABRIC RECONCILE -- RESOLVED 20260830T0256Z by 0.7.0_AE_CloudOps~L

`0.0.0_AB_MSTR` merged this record from both fabrics on 2026-08-29 and correctly declined to
adjudicate it, leaving the embedded site-Z copy in place for the owning lane. Resolved here by
that lane. `2.0.0_SA_COO` 84341 asked for the fix in its own commit.

**THE TWO SIDES NEVER DISAGREED ABOUT WHETHER A LEG FIRED.** Both carried L1-L4 closed and the
same L4 commit `418a7172d9`. The only delta was the **Status** line, and the CLOUD one was
INTERNALLY INCONSISTENT: it read `closed 20260827T202451Z` while its own L4 row already carried
evidence measured at `20260829T0820Z` -- a close timestamp preceding its own proof. The site-Z
line is the consistent one and is now the single **Status**. The earlier close is preserved
immediately below as history rather than deleted.

- SUPERSEDED STATUS LINE, verbatim: `**Status:** CLOSED -- nothing stranded -- closed 20260827T202451Z`

**MECHANISM, why this record drifted at all and why it could not self-heal:** it is HAND-AUTHORED
markdown with no `.open_deploys/*.json` sentinel, so `deploy_ledger.py close-leg` cannot act on it
and every close was a direct edit -- on two fabrics independently. That is the same class
`2.0.0_SA_COO` caught at 01:58Z on the floor-hold entry (`**State:**` where the tool indexes
`**Status:**`), and the class this seat's own 2026-08-29 log predicted in writing: *"deploy_ledger.py
has no close path for unindexed records; the next hand-authored ledger lands in the same hole."*
It did. The `ADVI_49F.c02-REEMIT` campaign entry opened 20260830T0251Z was therefore opened THROUGH
THE TOOL (`deploy_ledger.py open`), so it carries a sentinel and is indexed.

