# 0.6.2_AE_PartnerETL — session close: WP8 cell-3 Schwab-Box code re-home DONE + certified; a pre-existing 01_raw FATAL surfaced; a box-retirement error caught + corrected; two Andrew-direct architecture docs authored

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, TRACE, COORDINATE, SCRIBE
**Date:** 2026-07-17/18 | **Window:** ~18:23Z (07-17) -> ~00:32Z (07-18) | **Serial:** 0.6.2_AE_PartnerETL

> **NOTE — commits HELD (Andrew-direct 00:3xZ, "fabric is too hot to do a commit and push"):** this log + `data/assets/docs/BD_API_DESIGN.md` are WRITTEN-BUT-UNCOMMITTED. A `/handoff` carries the pending-commit list. Everything ELSE below is already committed + pushed.

## Summary

Spawned for WP8-DECOM ASK A (cell 3 = the Schwab Box's code-home re-home off the decommissioning `opal-data-schwab` bucket). Drove it end-to-end to certified-DONE, surfaced a live pre-existing FATAL that is NOT mine, caught + corrected a box-retirement scope error, and authored two Andrew-direct architecture docs.

- **WP8 cell-3 code re-home: DONE + cert-CLOSED both sides.** Additive IAM grant (`SchwabOpsCodeReadMonolith`) + the literal-flip cutover; the Schwab Box now pulls `sdd-daily-pull.ps1` from `opal-data-assets/code/canonical-schwab-si2/` (surviving monolith), not the dying bucket. Byte-identical (MD5 `0017f9b5.../35842B`), behavior-neutral, Rule-22a applied+exercised (on-box GET 35842B rc=0), 2 deploy-ledgers CLOSED, certified by CTO + 0.5.0.
- **Pre-existing 08242234 landing-guard FATAL surfaced (source-confirmed, ORTHOGONAL, 0.5.0's item).** The prove-on-fire pull FATAL'd rc=6 — NOT my flip: it has failed every run since 07-16 22:15Z (~24h pre-flip). Root: 0.5.0's WP8 01_raw-history copy landed flat `CRS{date}.{TYPE}` objects into `schwab/08242234/bronze/` colliding with the puller's `08242234.CRS….zip` (`landed=2 planned=1` x209). 0.5.0 took the disposition.
- **BOX-RETIREMENT ERROR — caught + corrected.** I relayed CTO's mis-scoped "CELL-4 = retire the quartz box" to 0.7.0; Andrew corrected ("the box is ESSENTIAL; WP8 = the BUCKET only"). Retracted (0.7.0 confirmed no action, box safe); CTO self-corrected his ruling; recorded + broadcast the scope law.
- **Two Andrew-direct architecture docs authored** for `data/assets/docs/`: the **Schwab Box archetype** (committed) + the **BD API design** (written, commit held).

## What landed (committed + pushed)

| Item | Commit | State |
|---|---|---|
| Re-home proposal + enriched proposal + runbook | `d8eaf705e`, `fb035d8a2` | validated by 0.5.0 |
| iam.tf +1 GetObject (additive grant) staged | `47d60ecb4` | applied (safe-apply 0/1/0) |
| Additive-grant deploy ledger (5 legs, CLOSED) | `4172749b3` | Rule-22a applied+exercised |
| Cutover flip (2 SSM-target literals -> monolith) | `66e6be74d` | applied (safe-apply 0/2/0) |
| Cutover deploy ledger (6 legs, CLOSED) | `40df85be0` | 0.5.0 cert ACCEPTED |
| `SCHWAB_BOX_ARCHETYPE.md` | `358296670` | committed |

## Andrew-direct rulings recorded + broadcast (VERBATIM, same turn)

1. **Language law:** *"…rest api call tghrough the backend of the GUI app, it has nothing to do with…UI driven process or using the SI2 Quartz."* -> `memory/feedback_schwab_auto_pull_is_rest_not_ui_quartz.md`.
2. **Scope law:** *"we are just getting rid of the opal-data-schwab standalone bucket. The EC2 schwab box is absolutely essential infrastructure."* -> `memory/project_wp8_decom_is_the_bucket_not_the_ec2_box.md`.
3. **Naming law** (recorded by peer): *"…It is the Schwab Box which we use for maintaining an authenticated REST API endpoint."* -> `memory/feedback_schwab_box_authenticated_rest_endpoint_not_quartz.md`.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-grep` (x8) | code-home consumers, `_ops/canonical-schwab-si2` sweep, `bd_identity`/`kimi` grounding | PASS — exhaustive 3-consumer sweep (tf:119, bootstrap:40, iam.tf) + BD mechanism located |
| `pipescript canonical-schwab` | SI2 estate thread | PARTIAL — frontend-orphan (infra/box side, not a gold pipeline); confirmed thin |
| raw `aws iam get-role-policy`/`simulate-principal-policy` (rail-checked) | Rule-22a applied truth + never-widen | PASS — code-key allowed, firm-data implicitDeny; box holds ZERO monolith GetObject baseline |
| raw `aws events describe-rule`/`list-targets-by-rule` (rail-checked) | live SSM-target flip verification | PASS — live target = opal-data-assets/code after flip |
| raw `aws s3 ls`/`head-object` | landed-bytes census + byte-identity | PASS — staging frozen 20260710, monolith fresh 20260716; MD5 identity confirmed |
| `.tools/deploy_ledger.py` (open/close-leg/close) | 2 deploy-completion ledgers | PASS — both CLOSED, all legs proven |

**What worked:** grounding on landed bytes + applied IAM every time (never the record); the exhaustive consumer sweep (no missed reader); refusing to certify the cutover on a FATAL rc (traced it to a pre-existing orthogonal cause instead of spinning it). **What failed/caught:** the box-retirement propagation — I KNEW the box was the active puller and wrote it, yet relayed a "retire" premise; should have challenged, not caveated (CTO banked it as the right instinct once corrected). **Gap:** SSM param write tripped on the MSYS `/c/` path-literal + short-name scratchpad path (fixed with long-form path + forward slashes).

## Blockers

None self-owned. Standing gates: the D5 old-grant-retire + bucket-data decommission (held to the WP8 D5 sequence + Andrew's destructive-go); the re-scoped CELL-4 box dependency-sever (CTO gate + 0.5.0 sequencing). Commits HELD (fabric hot, Andrew-direct).

## Current State (ZERO prior context — the handoff surface)

- **WP8 cell-3: COMPLETE + CERTIFIED.** Schwab Box (EC2 `i-0f3d57a97f14727af`) pulls its code from `s3://opal-data-assets/code/canonical-schwab-si2/`. Old `opal-data-schwab/_ops/canonical-schwab-si2/` code + the old `SchwabOpsCodeRead` grant RETAINED (both homes readable = no-skip) until **D5**. Ledgers `20260717T2200Z` (grant) + `20260717T2317Z` (flip).
- **RE-SCOPED CELL-4 (mine, in progress):** sever the Schwab Box's REMAINING `opal-data-schwab` runtime deps before the bucket delete (NOT a box action). Audit (grounded on live IAM + S3 recency): role `quartz-si2-spike-role` still holds `SchwabRawWrite` (`01_raw/*` + `01_raw_quartz_validation/*`), `SchwabBronzeWrite` (`08242234`+`08335338/bronze/*`), `SchwabBackfillWrite` (`backfill/08335338/*`) + 3 ListBucket. **LIVE finding: `opal-data-schwab/01_raw/` received a write 07-16 10:02Z (flat `CRS20260715.UPT`) — writer NOT yet grounded; ground + sever before delete.** `SchwabS3Sync` -> `01_raw_quartz_validation/` (sync-to-s3.ps1 confirmed). Staging bronze + backfill = not recently written (vestigial-candidate).
- **08242234 landing-guard FATAL: 0.5.0's item** (WP8 01_raw double-occupancy; source-confirmed `bronze/upt/20260622/` = 2 objects). Orthogonal to my re-home; NOT a bucket-delete blocker on my side.
- **DOCS:** `SCHWAB_BOX_ARCHETYPE.md` committed (`358296670`); **`BD_API_DESIGN.md` WRITTEN, UNCOMMITTED** (fabric hot). BD doc is source-grounded: `bd_identity` = `.bd.identity` cookie (confirmed); daily pull = `bd-49f-runner` Lambda (cookie->datamining token, no browser); re-mint = transient `bd-49f-auto-login` box (Playwright + Kimi-VL CV + device-trust; OTP via LIVE `gateway` adapter = OPLMCP GraphAPI delegated-as-Andrew Outlook Mail.Read; app-reg variant removed 06-25).
- **Schwab Box daily pull is HEALTHY at the ingest layer** — the FATAL is a post-ingest guard on the 01_raw collision; data lands fine (enum=230/skip/dl=0/fail=0).

## Next Steps

- **[0.6.2 self]** (1) `/handoff` next (Andrew-direct) — carry the pending commits (BD_API_DESIGN.md + this log). (2) Finish the CELL-4 dependency-sever: ground the `01_raw` 07-16 writer, produce the full sever plan (repoint LIVE / retire VESTIGIAL), execution gated. (3) Fold the code-parity refinement (self-contained-vs-pull, Andrew's steer) into SCHWAB_BOX_ARCHETYPE.md as landed.
- **[0.5.0_AE_OpalETL]** the 01_raw double-occupancy FATAL disposition (their WP8 copy); signals D5 when the bucket is sever-clean.
- **[1.0.0_SA_CTO]** CELL-4 re-scope confirmed as dependency-sever (box stays); gates the sever apply. Struck "box disposition."
- **[0.7.0_AE_CloudOps]** box confirmed untouched; CELL-4 is NOT a box-stop.

## MCP traffic

~40 in / ~30 out. Significant: **Andrew-direct x5** (language law, date-anchor, scope law "box essential/bucket-only", self-contained-code design Q, the two doc jobs) — all recorded + broadcast same turn. 0.5.0 (WP8 lead: proposal validated, GO(A) additive, GO(1) cutover, cert ACCEPTED, took the 01_raw item). CTO (location+IAM gate, plan-gate PASS, apply-approved, CELL-4 self-correction + archetype-doc job). COO (date correction, pathspec-ding benign). 0.7.0 (box-safe confirm). MSTR (scope-law ACK). All RAVC loops CLOSED; nothing pending an ACK from me.
