# Deploy Completion Record
**Date opened:** 2026-07-23T11:02Z
**Status:** CLOSED -- nothing stranded -- closed 20260723T1112Z
**Deploy:** cot-pipeline WS-1 Lever-A AGE BOUND + visibility rider on `cot-bd-session-trigger` (Lambda source-only) -- CTO gate 104223Z amending his 2026-07-06 ruling
**Authored by:** 0.6.2_AE_PartnerETL~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

> **PROVENANCE OF THIS FILE (read before trusting its shape).** This record was **converted on 2026-07-23T21:2xZ**
> from `org/critical_paths/.open_deploys/ws1-lever-a-age-bound-20260723.json` (@31bc04cab), which I **hand-authored
> off the writer's schema** (`deploy_id`/`mechanism`/`result`/`rollback` instead of `slug`/`opened_at`/`legs`/
> `entry_path`) and left in the **open-sentinel dir despite the deploy being CLOSED**. Consequences, both real:
> `deploy_ledger.py close` unlinks the sentinel, so a closed record living in `.open_deploys/` reads to the gate as
> an **open-but-unreadable** sentinel; and `check --red` dereferenced `state["legs"]` unguarded and **CRASHED on my
> file, aborting the whole sweep** -- masking 7 unindexed ledgers until `0.8.0_AE_CloudComp` landed the reader fix
> (@839ee85cc, malformed entries now render a LOUD verdict and the scan completes). Found + routed by 0.8.0
> (211338Z); conversion **ruled mine** by CTO (211341Z) -- my record, my lane, nobody else authors or deletes it.
> **The evidence below is carried verbatim from that contemporaneous JSON; the leg decomposition is the conversion.**
> **GOING FORWARD: ledger entries via the writer (`deploy_ledger.py open`/`close`), never hand-authored JSON --
> the writer's schema is what the NEVER#6 instrument reads.**

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | commit the Lever-A age bound + visibility rider (cot-bd-session-trigger source) | hash pushed | `49601d885` -- Lever-A AGE BOUND per CTO amendment 2026-07-23T104223Z to his 2026-07-06 ruling: skip the OIDC mint only while the capture is younger than `MAX_SESSION_AGE_DAYS=7` (env-overridable); older-but-live -> scheduled re-mint via the unchanged fail-safe leg. Closes the fires-without-writing refresh-only-at-death defect (17-day aging caught 07-23). `expires_at` grounded ABSENT, so a FIXED bound was used rather than an expiry-margin. Visibility rider: capture age in the mode marker + a loud over-threshold log line (**no alarm**, per standing word). | CLOSED |
| L2 | s3-prefix | build + upload the Lambda artifact via the sanctioned `build-and-upload.sh` | uploaded zip sha recorded for the apply to tie against | Artifact built + uploaded through the sanctioned `build-and-upload.sh` (never `aws lambda update-function-code`); upload sha `9aroLn4r...` carried into L3's tie-out. | CLOSED |
| L3 | tf-lambda | `safe-apply` targeted at `module.cot_bd_session_trigger` (Lambda source-only; no other resource in scope) | apply complete + 0-diff replan + APPLIED (live) CodeSha256 == uploaded zip sha | `Apply complete 0/1/0` (**targeted**, `module.cot_bd_session_trigger` only). 0-diff on my module on replan. **APPLIED truth, not the TF DESIRED view:** live `CodeSha256` == uploaded zip sha `9aroLn4r...`, and `MAX_SESSION_AGE_DAYS` + the amendment citation are **present in the live zip**. Residual plan line = **pre-existing `cot_exporter_policy` drift, deliberately NOT swept** -- routed to CTO rather than folded into an unrelated apply (scope discipline: a targeted apply does not quietly repair someone else's drift). | CLOSED |
| L4 | git | tag + push the release | tag name pushed | `cot-pipeline-v0.7.2` tagged and pushed `--follow-tags`. | CLOSED |

## Rollback

Revert the commit + rebuild + re-apply (**the prior artifact is the rollback body**). At close, the live cookie was
**FRESH** (minted 2026-07-23T10:50:20Z), so **either lever version operates safely** across that night's window --
the deploy carried no forced-cutover risk.

## Log

- 20260723T1102Z OPENED by 0.6.2_AE_PartnerETL~A (hand-authored JSON sentinel -- off-schema; see PROVENANCE)
- 20260723T1112Z CLOSED -- targeted apply 0/1/0, bytes-verified, `cot-pipeline-v0.7.2` tagged+pushed; `cot_exporter_policy` drift NOT swept (routed to CTO)
- 20260723T2036Z record commit `31bc04cab` identified by 0.8.0_AE_CloudComp as an off-schema sentinel crashing `check --red`; reader hardened @839ee85cc
- 20260723T212xZ CONVERTED to this canonical change_management record by 0.6.2_AE_PartnerETL~A per CTO ruling 211341Z; stray `.open_deploys/*.json` removed in the same commit (record MOVES, never duplicates)
