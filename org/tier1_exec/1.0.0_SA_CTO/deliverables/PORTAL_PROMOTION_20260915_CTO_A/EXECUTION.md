# Portal promotion execution — 2026-09-15

Executor: `1.0.0_SA_CTO~A`. Status: **PORTAL DEPLOYED AND EXERCISED; ONLY L5 WORKSPACE PUBLICATION OPEN**.

**Publication approval resolved (CTO97067, 12:37:44 UTC): MSTR is authorized to push CLOUD after the foreign merge clears.** This seat measured that merge absent and the staged index empty at12:38Z. L5 still requires the actual publication receipt; no new approval is being requested.

**Latest data receipt (12:34:37 UTC, MSTR97063): characteristics vintage qualifier CLEARED.** The scheduled 12:30:54 UTC refresh supplies September 14 data for all 24 sourced holdings; CASH remains intentionally unsourced. Exact object version and bounded coverage proof are recorded below. Only L5 workspace publication remains open.

## Authority and exact release

MSTR's explicit **GO 97048**, exact root-level inbox notice at 11:52:03 UTC, was read and ACKed at 11:53:01 UTC. The verbatim message is preserved in `GO_97048.md`. It designates this exact seat as the Andrew-directed non-DT executor and binds the audited portal-push override to Andrew's deadline ruling. Authority records: `4524cc2466` (~07:4xZ merge/promote) and `02e9cb858c` (`ANDREW_DIRECT_20260915_080xZ_PORTAL_PROMOTED_BY_9AM_EASTERN.md`). Deadline: **13:00 UTC / 09:00 Eastern**.

- Admitted DEV candidate: **`9adad7ce750742e9806c373a71f7ce900f3e22b2`**.
- Required candidate tree: **`d3db406c198b325fee48790a84205f0695c6d7c2`**.
- GO-time live PROD / proposed rollback base: **`b1389c85759511e65ec5d5b26ee96d63c91984c2`**, to re-read before the merge.
- Required merge: no-ff, **second parent = admitted DEV SHA AND tree = admitted tree**, plus empty candidate-to-merge diff. Literal merge-HEAD equality to DEV is not required.
- AMGT is excluded. No other DEV pushes or main-tree merges are permitted during the active MSTR freeze.
- Runtime procedure: `.claude/skills/prod-deploy/SKILL.md`, read end to end at execution start; Codex exact-seat inbox/runtime rules supersede its Claude inbox helper examples. MSTR retains workspace pointer/publication ownership.

## Accepted proof and limitations

The prior source, lockfile and CI checks are pinned in `PREPARATION.md@323e1fdd75`. GO binds the IR gate (2 routes, 1 nav item, 3 partner exclusions) to the candidate. The required `10c2f07d4da3795c0e404a92a8b9515259e42be7` ancestor and candidate source checks are re-read at execution.

MSTR accepts presentation proof with a **named vintage qualifier**: Site Z reports 544/544 cells equal served values, mutation discrimination and no unrounded values; Satellite 15 and 80 render checks were 272/272 each on Positioning source identical to the candidate. At 11:51 UTC, `characteristics.json` still has reported VersionId prefix `PXyBGaqn`, published 08:10:03 UTC, with 23 positioning-data-sourced holdings dated 2026-09-11, while `positioning_data.json` reports 2026-09-14 since 11:06:20 UTC. **This execution does not call those vintages aligned.** The page reads the data key live; MSTR explicitly owns post-promotion verification after the third driven re-serve or the 12:30 UTC organic run. GO permits promotion with this qualifier and replaces the earlier wait for an unqualified new-SHA data recheck.

Known exceptions remain named: F25-AC8 line-ending instrument issue; F49-AC8 pre-merge invariant; all five lint errors adjudicated by CTO 97040 (two unused SentimentGauge imports, unused pre-envelope PERFORMANCE_KEY, ExportButton DOM/hook immutability diagnostic, historical alias-probe constant expression). DEV CI **34957141198** passed Install, failed lint, and skipped later checks. It is not green. Separate clean Bun 1.3.9 install/typecheck/build and the manual provenance-guard proof are attributed as in preparation. Required PROD deployment workflow success is not waived.

## Complete deployment ledger

Opened before execution mutations at 11:55 UTC:

- Ledger: `org/critical_paths/change_management/20260915T1155Z_portal-prod-promote-20260915-0900et_deploy_completion.md`.
- Sentinel: `org/critical_paths/.open_deploys/portal-prod-promote-20260915-0900et.json`.
- Seven declared legs: L1 admission/preflight; L2 PROD merge/push; L3 deployment/tag; L4 served artifact/behavior; L5 MSTR-owned workspace pointer/publication; L6 cleanup/report/freeze release/session log; L7 MSTR-owned characteristics vintage follow-up.

Every leg closes only against its actual proof. A still-pending MSTR follow-up stays visible rather than being represented as complete. After a failed PROD push/deploy, surface the exact failure to MSTR/CTO immediately; no unilateral revert or repush is authorized by the prepared rollback SHA.

## Execution observations

At **11:53:52 UTC**, independent `ls-remote` showed DEV at the admitted candidate and PROD at the recorded base. Main portal was DEV at that candidate with zero tracked changes. Bun resolved through PATH and printed **1.3.9**. Existing peer integration worktree remained on `43f18c17`; it will not be altered. The executor uses its own fresh candidate checkout for all-files cleanliness and a separate ephemeral PROD worktree; main portal stays DEV. No PROD branch, merge, push or installation has occurred at this initial record.

Further evidence and exact results are appended as execution proceeds.

## PROD execution and live artifact proof

- PROD pushed at **12:10:07 UTC**: `edf85ce503aad961b84b5ea3b2074eb84d416a16`. First parent/rollback `b1389c85759511e65ec5d5b26ee96d63c91984c2`; second parent `9adad7ce750742e9806c373a71f7ce900f3e22b2`; tree `d3db406c198b325fee48790a84205f0695c6d7c2`. The candidate diff was empty and all-files status clean immediately before the authorized push.
- Fresh PROD worktree baseline installation, merged frozen installation, typecheck and build passed under Bun 1.3.9. Pre-push provenance guard, VALGATE D-1 (no-op: no static partner adapters changed) and typecheck passed. The push command carried the same-command Andrew-direct override citing `02e9cb858c` and GO 97048.
- CI exact-head enumeration: **one workflow**, [Deploy to Production 34967303352](https://github.com/Opal-Capital/portal/actions/runs/34967303352), terminal **SUCCESS** at **12:12:00 UTC**. Build/typecheck, artifact upload/download, S3 static/index/JSON deployment, CloudFront invalidation and tag creation all succeeded. See `CI_34967303352.json`.
- Remote annotated tag **`portal-v2.1.178`**: tag object `968e6ab7e058e974cdc92a279cdb7a5ef5d1d63e`, peeled commit **`edf85ce503aad961b84b5ea3b2074eb84d416a16`**.
- At **12:16:00 UTC**, HTTP GET against `https://opalinvest.dev` matched **54/54 files byte-for-byte** to this exact run's downloaded `production-build`: `index.html` and all 53 JavaScript/CSS files in its assets root. Index SHA256 `7b70633fdc00be72f33bf5b43db1fe013aae141665df80617c9c52d2c19477e6`. Full bounded hash manifest: `SERVED_ARTIFACT_PROOF.json`. This proves served bundle identity; it does not assert dynamically fetched data freshness.

## Post-deploy behavior checks and remaining proof

The checked-in `portal/scripts/ui-smoke.mjs` exercised actual production JavaScript in fresh headless Edge at 1440x900, with its documented synthetic session claims and **no data fixtures**. Internal Opal admin reached `/investor-reporting` with its nav item present. A 49financial partner with both role=admin and firmRole=admin was redirected from that route to `/market`, with Investor Reporting absent from navigation. Positioning loaded the new page shell. Screenshots and network logs are private scratch evidence.

**Limit:** the harness's synthetic token is not a real bearer; protected APIs returned 401 as expected. The internal IR scope-error state and Positioning empty holdings under that synthetic token are **not** evidence that authenticated data works or that it is broken. No authenticated full data walkthrough is claimed. MSTR was notified at 12:17:19 UTC to provide the existing validation lane's authenticated served Positioning evidence and the separately owned vintage follow-up, alongside workspace pointer/publication and freeze-release receipts. The GO's dated vintage qualifier remains explicit.

Ledger L1-L3 are closed. L4-L7 remain open pending their specified actual proof. Main portal remains DEV; cleanup and canonical log follow before completion.

## Cleanup and additional gate checks

The same partner-admin synthetic session was redirected from `/investor-reporting/print` to `/market`. An internal Opal non-admin was also redirected from `/investor-reporting` to `/market`, with IR navigation absent. These are frontend identity-gate observations only.

Both owned worktree paths were resolved and verified inside the workspace `.runtmp/` directory and all-files clean before removal. `portal-candidate-20260915T115803Z` removal exited 0. `portal-promote-20260915T115803Z` removal exited 255 with Windows `Filename too long`; canonical `git worktree prune` followed, and neither owned path remains registered. The production skill explicitly permits this ignored physical residue. Peer worktrees were untouched. Main portal is verified **DEV at 9adad7ce**, and execution CWD is the workspace root. No workspace push occurred.

## Owner receipts and post-promote repair

MSTR **97051 at 12:19:50 UTC** independently corroborates release parents/tree/CI, confirms the 09:00 Eastern deadline was met at **08:12 Eastern**, and **releases the portal freeze**. It explicitly retains the dated characteristics qualifier and owns the 12:30 UTC organic re-serve follow-up. Its prior same-code presentation evidence remains the accepted qualifier; its data-plane follow-up is not represented as a new authenticated browser run.

MSTR **97057 at 12:23:05 UTC** relays Andrew's own mobile check verbatim: **"Just Checked promote on my cell phone it all looks good with the data"**. This supplies the actual authenticated served-user receipt missing from the synthetic harness. `OWNER_RECEIPTS.md` preserves both exact messages. L4 is closed against artifact, gate, accepted presentation and actual-user proof. L7 is closed through its declared **explicitly retained dated vintage** option, with the future data freshness read still MSTR-owned.

The assigned post-promote repair is committed **LOCAL in portal `acdb02e917f510a834c00ef33f8d4343d351f8eb`**, branch `codex/cto-a-portal-typecheck-20260915`, parent `9adad7ce750742e9806c373a71f7ce900f3e22b2`. Only `.github/workflows/ci.yml` and `.github/workflows/promote-to-prod.yml` change: `bun run tsc --noEmit` becomes `bun run typecheck` (project-reference-aware `tsc -b --noEmit`). Exact diff and parsed YAML comparison confirm all other workflow semantics unchanged. The target command's deliberate failure and valid pass were already measured in this session. No redundant dependency installation or frontend rebuild was required for those two command replacements. Both author and committer are the exact CTO~A serial. The isolated repair worktree was clean and removed successfully, leaving its branch/commit available to MSTR's normal drain. MSTR was notified at12:23:59Z; this seat did not push DEV.

**Workspace publication remains separate:** MSTR97057 says its gitlink move is LOCAL, but CLOUD push is held because it would deploy eight pipeline files. That ask names base CTO for adjudication. The portal GO does not authorize this seat to approve that broader deployment. L5 awaits the exact pointer/integration commit receipt; L6 awaits the canonical session log. No portal failure or rollback is outstanding.

## Final executor handoff at 12:29 UTC

Portal release is **DEPLOYED AND EXERCISED** at **edf85ce5 / portal-v2.1.178**, CI success 12:12 UTC / 08:12 Eastern, 54/54 served artifact hashes matched, and Andrew's mobile-data confirmation recorded. The portal freeze is released. Canonical log **`112a616b5c`**: `org/tier1_exec/1.0.0_SA_CTO/logs/2026-09-15/taxsma_hotfix_portal_promote_0425-1225Z.md`. Ledger **L1, L2, L3, L4, L6 and L7 are closed** against their specified evidence.

**L5 remains OPEN for actual workspace publication.** MSTR97059 supplies the LOCAL integration receipt **`8e5780daf6`**, gitlink `e85f6eb84f -> 9adad7ce`, also carrying LD-0568's outcome and Andrew's live check. MSTR explicitly says the publication leg closes only when its CLOUD push lands. Its reported origin/CLOUD is `6a5b276f8b`, with 537+ commits pending; base CTO's ruling97056 addresses the eight pipeline files the push would deploy. This seat does not claim that LOCAL pointer is published or that a portal GO approves the broader code deployment. The ledger's canonical HELD operation admits only verify-only residuals, so it is **not** used to hide an unclosed git leg. The open publication obligation and its one-hour window are explicitly routed to MSTR/base CTO.

The two-line CI repair **acdb02e9** is committed LOCAL on its isolated branch and handed to MSTR; publication is through its normal DEV drain. No post-repair production redeploy is claimed. MSTR retains the separate 12:30 UTC characteristics freshness follow-up. The actual release did not require a rollback and has no remaining executor-side deployment action.

## CI repair publication and merge-window interruption

MSTR **97060 at12:29:01Z** confirms the exact reviewed two-line repair was fast-forwarded and pushed normally. Independent `ls-remote` now confirms **DEV `acdb02e917f510a834c00ef33f8d4343d351f8eb`** and unchanged **PROD `edf85ce503aad961b84b5ea3b2074eb84d416a16`**. The workspace pointer8e5780daf6 intentionally records promoted9ad; a later pointer bump can capture the CI-only change. Exact-head DEV CI **34969078747** is **failure**: Install succeeds, ESLint fails, provenance/typecheck/build are skipped. This is the already named lint debt; the repaired typecheck step is not falsely reported as exercised by this CI run. Positive and deliberate-negative command validation remains the earlier measured local evidence. The production workflow remains independently successful.

The final four-file evidence commit encountered an active shared workspace merge (`MERGE_HEAD 60b48c5196a5e9d46bc52858e8dd16ef4814ab30`). `safe-commit` refused a partial commit and unstaged only its own four paths. MSTR was notified at12:30:08Z, base CTO at12:30:09Z; no merge/index/lock modification or bypass occurred. The closeout additions are preserved locally pending the integrator's CLOSE frame. Canonical log112a616b5c and prior deployment evidence6bafe30998 are already committed.

## Characteristics freshness completed - MSTR97063

At **12:34:37 UTC**, MSTR supplied its measured `head-object` and fully parsed object read for **`s3://opal-data-cot/platinum/satellites/characteristics.json`**:

- **VersionId `02SGBCPDoeVPy7JBJcEHxUw4J0.nQneh`**, LastModified **2026-09-15T12:30:54Z**, `bbg_run_class=scheduled`. This is the scheduled B6 refresh; the third requested driven run did not occur.
- `as_of=2026-09-15`, `holdings_as_of=2026-09-15`, **`positioning_data_as_of=2026-09-14`**, **`bbg_as_of=2026-09-14`**, `bbg_universe_count=172`.
- **25 tickers:** 23 positioning_data-sourced holdings dated September 14; 1 BBG-sourced holding (GLD) dated September 14; 1 intentionally unsourced CASH. Thus **24/24 sourced holdings are at T-1**.
- Non-null counts out of 25, compared with the 08:10 baseline: fee 24->24, AUM 24->24, returns 24->24 with eight periods each, active 23->23, yield 22->22, beta 11->11, duration **9->10**, credit 7->7; name25 and management_style25. No non-null measure was lost.

This owner-measured data-plane receipt **clears the GO's characteristics vintage qualifier** and supersedes the earlier retained-dated-vintage L7 proof. Historical admission and execution observations above remain dated audit evidence. Presentation proof remains the accepted same-code Site Z checks and Andrew's relayed mobile check; this receipt does not independently report a new authenticated browser run or an unrounded-value census.

The canonical L7 proof now records the completed freshness read; **L5 CLOUD publication remains the only open leg**, pending MSTR's publication after base CTO's97056 ruling. MSTR confirms the shared `MERGE_HEAD60b48c51` belongs to another seat's drain and is also preventing its own record commit. At12:35:43Z this seat still measured that merge active. These four owned closeout files remain saved locally, without staging or altering the other seat's merge.

## CTO publication disposition and shared-merge clearance

Exact notice **CTO97067 at12:37:44Z**, preserved in `OWNER_RECEIPTS.md`, authorizes **MSTR** to push CLOUD once the foreign merge clears, without per-file owner reconfirmation. The CTO's bounded measured write set is three objects across eight changed script paths in the reported origin/CLOUD6a5b276f8b..CLOUD range (541 commits):

1. `s3://opal-data-mdpf/code/scripts/assets_gold/build_cottonwood_mdpf_pair.py`: existing object updated to the already deployed whole-cents Lambda behavior.
2. `s3://opal-data-49financial/_code/perfrp_firm_pin.py`: existing object gains only two generated-marker comment lines; no code change.
3. `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`: reminted bundle; the generated firm-bucket literal matches the prior five-entry runtime map, so the CTO finds no served-behavior change.

The CTO reports target404 loud skips for the two silver closure modules and two tests; those skips do not deploy the OG-c-1 code outside OG-c-2's signed deployment. This seat records the CTO's measurement and disposition rather than claiming to have independently repeated that whole AWS census. The pipeline push proceeds under Rule13 and MSTR ownership, not under this seat's portal push authority. SentimentGauge's two unused imports remain assigned by the ruling to the separate IRPT_FNTEND round9 cellC.

At **12:38:43Z**, this seat measured `MERGE_HEAD` absent. The next read confirmed the staged index empty and HEAD `3f94e0a024`, COO~O's completed OG-q-1 worker drain. Thus the earlier shared-merge obstacle to the four-path documentation commit has cleared. The records can be committed with the canonical wrapper and exact pathspecs; no other seat's index or merge was changed. **L5 stays OPEN until MSTR's real publication receipt arrives**, and the earlier approval hold is resolved. The data-vintage qualifier remains cleared by MSTR97063.
