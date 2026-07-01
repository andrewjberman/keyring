# 0.7.0_AE_CloudOps -- SCTY owner-ack + safe-deploy gate-hole (3 bugs) + MCP Integration Framework + YCharts live reverse-engineer + /ycharts-report skill

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT (framework + skill + fixes), DIAGNOSE (safe-deploy 3 bugs, SCTY grounding), EXPLORE (YCharts internal-API reverse-engineer), COORDINATE (SCTY deploy hand-off to ~A), DEPLOY (Secrets Manager swaps)
**Serial:** 0.7.0_AE_CloudOps (base lane) | **Date:** 2026-07-01 | **Window:** session start -> ~2225Z (first log of session)

## Summary
Four work streams, all Andrew-direct or Andrew-adjacent:
1. **SCTY_MCPGUARD gateway owner-of-record** -- answered 0.5.0's integration-point sync (grounded live), owner-ack'd the landing diff, then STOOD DOWN from the deploy-lane per Andrew's reinforced reassignment to 0.7.0~A; deconflicted + corrected an R8-PRIV mis-flag. (~A landed + CVO-certified the deploy: ledger 51090a2fa PASS 4/4.)
2. **safe-deploy pipescript-verify gate-hole** -- CTO-reported WinError-193; grounding revealed THREE stacked latent bugs; all fixed + a regression test institutionalizing the ADHC_PREFLT principle.
3. **MCP Integration Framework** -- generalized the gateway from M365-only to a registrable multi-source model (ships dormant); promoted to canonical STANDARD by the NFRA_INTEGRATIONS lane (P1/P2, ~A).
4. **YCharts** -- extracted + refreshed the session credential; live-reverse-engineered the client comparison/stress-test PDF flow via Playwright (the `custom_pdf_reports` engine); built the parameterized `/ycharts-report` skill that drops the finished PDF to the user's Downloads.

## Work detail

### 1. SCTY owner-of-record (base commits: none -- coordination + the framework in stream 3; deploy commits are ~A's lane)
- Grounded the m365-gateway source + LIVE box (SSM 6765cc58, box i-07dccb1615503ac99): **IDENTITY_PROVIDER=alb_oidc** (signature-verified; config.validate boot-guard fail-closes prod on spoofable providers), `_run()` (tools.py:47) = 100pct of the MCP-tool chokepoint + 3 NON-mutating REST bypass paths (/teams/poll [G6-audit gap], /ms/*, /otp/*), full delegated-write envelope (broader than Files.ReadWrite.All).
- Owner-ack'd 0.5.0's landing diff 8de441c6b (all 4 DIFFs grounded-correct); flagged the andrew@-only-writes behavior-change + the /teams/poll G6 fold.
- Andrew reassigned the DEPLOY to 0.7.0~A ("base is on the integration"); I stood down (no second ledger/deploy), deconflicted 3 collision surfaces with ~A (CLOUD strip = worktree-isolate so my YCharts stays intact; 0.5.0 source routes to ~A; DC1/DC2 -> I own on de-gate).
- **R8-PRIV correction (owned my error):** I'd flagged R8-PRIV (838d8790b) as "never deployed"; ~A ground-truthed it IS live (on-box md5 440b6f08 == git show 838d8790b:audit.py; ancestor of deployed 28ecbd838). Verified independently, corrected COO + ~A -- excluding it would have regressed a live privacy control.

### 2. safe-deploy gate-hole -- 3 bugs (base commits e33016197, cce08495c, 364ba9413)
CTO-reported WinError-193 was the surface of a gate that had NEVER functioned on Windows:
- **Bug 1 (fail-OPEN crash):** run_pipescript_verify subprocess-exec'd the extensionless comp-pipescript bash wrapper -> Windows WinError-193 after the S3 cp landed -> deploy GREEN + UNVERIFIED. FIX (e33016197): invoke the Python engine (pipeline_cli.py) directly via sys.executable -- the ratified 572a5d9b8 cross-platform pattern (NOT the bash-hop CTO floated, which re-hits the broken WSL relay).
- **Bug 2 (timeout soft-no-op):** big layers (inf-gold) exceed the 120s timeout -> fail-open WARN. CTO ruled (b); FIX (cce08495c): scope the verify to the CHANGED script(s) (iterate the deployed set, `deployed <repo-rel-path>` auto-detect) -> seconds, fails loud.
- **Bug 3 (fail-CLOSED-wrong, invisible until Bugs 1/2 fixed):** `"STALE" in output` matched the summary's literal "0 STALE" -> false-FAILED every completed run. FIX (cce08495c): parse the Summary COUNTS, not substrings.
- **Regression lock (364ba9413):** test_safe_deploy.py Case 7 asserts the verdict-parser on a known-good + known-bad fixture -- CTO cited it as the ADHC_PREFLT CANONICAL REFERENCE-IMPL. CTO endorsed all; COO closed the AE-infra item.

### 3. MCP Integration Framework (base commit 1bc81dd26)
- `app/integrations/`: base.py (IntegrationSpec schema + Integration ABC + AuthKind DELEGATED_USER/SHARED_SECRET/NONE + audited `run_integration_tool` separating caller-identity=audit+tier from credential=integration-shared + SecretsCredential), registry.py (fail-closed: registers ONLY config.ENABLED_INTEGRATIONS, default EMPTY), ycharts/ (first integration, SHARED_SECRET, read-only, 6 v1 tools). config.py + server.py wired; ships DORMANT (0 live tools until enabled).
- Promoted to canonical `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` + P2 min_tier wiring by the NFRA_INTEGRATIONS lane (5b540fda4/0d075b50b, ~A/CTO). YCharts-enable fired by ~A on my confirmed build-state (min_tier=standard, compartmentalized andrew@+alyssa@).

### 4. YCharts (base commits a24316e56, d65d339aa; SM secret swaps)
- Extracted the auth bundle from the colleague HAR -> `ycharts/credentials` (VersionId e26c06d1), then REFRESHED it from a live browser session I drove (VersionId 3ef8f649, 16 cookies/3 essentials, values never echoed -- captured via Playwright storageState -> gitignored temp -> file:// put -> temp deleted).
- **Live reverse-engineer (Playwright, as alyssa@):** drove the exact analyst flow (client portfolio vs Opal Long-Term Conservative, Comprehensive Comparison template) and captured the `custom_pdf_reports` engine: GET generate/collection (templates) -> GET generate/{session} -> POST validate_report_securities/{session} -> **POST /custom_pdf_reports/{session} -> 201** -> presigned-S3 PDF. Server-side generate -> retrievable PDF = fully automatable. Confirmed the read-only data endpoints too (/search/suggest/report_securities, custom_pdf_reports templates, job pollers).
- **`/ycharts-report` skill (a24316e56):** parameterized client-vs-model report generator; auths by injecting the shared cookie (no fresh login -> no single-seat eviction); documents exact selectors + the endpoint chain. **(d65d339aa):** step-7 transfers the finished PDF off the Playwright dir to the user's Downloads + wipes the working copy (client PII out of repo). Proven: David_Vickers_vs_Opal_LTC_Comparison_2026-07-01.pdf (709K) landed in Downloads.

## Files Modified / Commits
See commit messages: `e33016197`, `cce08495c`, `364ba9413` (.tools/safe_deploy_core.py + test_safe_deploy.py); `1bc81dd26` (infra/aws/ec2/m365-mcp-gateway/app/integrations/* + config.py + server.py + INTEGRATION_FRAMEWORK.md); `a24316e56`, `d65d339aa` (.claude/skills/ycharts-report/SKILL.md). All pushed to CLOUD. (SCTY deploy/enable + NFRA_INTEGRATIONS commits under the shared author name are 0.7.0~A / CTO lane, not this base session.)

## Deployment Sequence + Verification (AE)
- **Secrets Manager `ycharts/credentials`:** two put-secret-value ops -- e26c06d1 (from HAR) then **3ef8f649 (AWSCURRENT, from live session)**. Reread masked confirm: `cookies` key present, header 1208 chars, 16 cookies, ycsessionid/csrftoken/aws-waf-token(314) all PRESENT. No values in git/logs/messages (Third-Party Data Standard §3).
- **CLOUD pushes:** all 6 base commits pushed (`.tools/safe-commit.sh` per Rule 14a; safe-deploy pre-push = "no deploy-scope script files"; surface-check clean each).
- **safe-deploy fix verification (live):** run_pipescript_verify per-script -> cot-silver "1 MATCH" 2s / bd-silver / inf-silver MATCH; test_safe_deploy.py 7/7 (pytest + direct runner); ds-commit-gate clean each file.
- No EC2/Lambda deploy by base this session (the gateway SCTY deploy + YCharts-enable are 0.7.0~A's deploy-lane; deploy-completion ledger CLOSED by ~A, CVO PASS 4/4 per 51090a2fa).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `pipeline_cli.py deployed` (comp-pipescript ENGINE) | subject-of-fix + live verification of the safe-deploy repair (cot/bd/inf-silver) | PASS -- returns real MATCH verdicts (2-36s); was WinError-193/false-fail |
| `.tools/ds-commit-gate.sh` | every .py edit (Rule 14) | PASS (py_compile + AST + ruff) all files |
| native Read/Grep/Glob | gateway source grounding + collision/blast-radius (own just-made changes) | free per NFRA_COMPRAIL (native Read; Grep/Glob nudge-and-proceed) |

**What worked:** invoking the comp-pipescript engine directly (pipeline_cli.py) both proved the fix and IS the fix (the cross-platform pattern). **What failed:** n/a. **Gap:** none new. **Off-rail-appropriate (no comp-tool applies):** operational `aws`/`ssm` for LIVE-state grounding (IDENTITY_PROVIDER, box md5, IAM), Playwright for external-SaaS (YCharts) recon, Secrets Manager ops. comp-which/graph tools do not cover external-SaaS or a live-box env read.

## Blockers
None. (No assumption-blocks. The one hard external gate encountered -- SCTY code was staged-not-wired -- was resolved by the 0.5.0->~A source handoff, not a blocker on me.)

## Current State (handoff)
- **ycharts/credentials = AWSCURRENT 3ef8f649**, a LIVE working session (2 reports generated on it ~2223Z). Single-seat: valid until the ~96h aws-waf-token TTL (~2026-07-05) OR anyone logs into YCharts as alyssa@ (evict). **alyssa@ must stay out of the YCharts web UI until 0.7.0~A's enable-cert logs a live ycharts_freshness 200** (server-side cookie reuse by the skill/integration does NOT evict; a web login does).
- **/ycharts-report skill** live in `.claude/skills/ycharts-report/SKILL.md` (registered). Parameterized (client/comparison/template/report-fields/output_dir); drops PDF to `C:\Users\AndrewBerman\Downloads`. To be refined later for Alyssa (Andrew-direct: "document this, refine later for alyssa").
- **MCP Integration Framework** in `app/integrations/` (base+registry+ycharts, dormant); canonical contract = `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md`. Read-only `ycharts_*` MCP tools being enabled on the gateway by ~A (compartmentalized andrew@+alyssa@).
- **safe-deploy gate** now actually functions on Windows (3 bugs fixed + Case-7 regression lock).
- Example client PDF in Andrew's Downloads: `David_Vickers_vs_Opal_LTC_Comparison_2026-07-01.pdf`.

## Next Steps
- **[0.7.0_AE_CloudOps~A]** fire/complete the YCharts-enable + self-cert (roster->200, non-roster->min_tier_denied); ping base at deployed + freshness-200. If 403 -> base re-refreshes ycharts/credentials.
- **[0.7.0_AE_CloudOps base / Andrew]** keep alyssa@ out of YCharts web UI until the enable-cert 200 lands; refine /ycharts-report for Alyssa's real workflows next.
- **[1.0.0_SA_CTO]** (from safe-deploy) ADHC_PREFLT canonical case-study fold (Case-7) -- CTO confirmed, nothing owed.
- **[0.7.0_AE_CloudOps base]** on request: run /ycharts-report on a real client (confirm inputs first) + draft the Teams step-by-step back to Alyssa; declare ycharts_ audit-args metadata-safe fast-follow if not already shipped by ~A (it was: R8 allowlist CVO-co-verified).
