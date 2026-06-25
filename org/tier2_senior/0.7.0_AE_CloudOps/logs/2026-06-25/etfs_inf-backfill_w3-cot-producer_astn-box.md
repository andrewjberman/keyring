# Session 2026-06-25 ~1307-1403Z -- ETFS_SETUP: Inflection AC#2 backfill + W3 Cottonwood producer + ASTN-box residuals

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE

Morning bring-up (COO-requested, MSTR-authorized). Lane = ETFS only (NOT BD ingest-restore).

## Summary

Bring-up reconcile corrected a stale dispatch premise, then drove three GO'd legs to verified completion:

1. **Bring-up reconcile.** The COO bring-up said "resume W1 + W2." Ground truth: **W1 already LANDED+LIVE** (ledger d2dd0d5d6 closed, tagged, served slice comp-freshness PASS ~$82.2M/4-ETF) and **W2 reassigned to 0.5.0_AE_OpalETL** (commit a711bd379). RAVC2'd the reconciliation; COO flipped W1->complete, accepted the correction. My one FYI -- the Inflection producer was forward-only (no historical slices) -- turned out to be the real AVGCAP.AC#2 gate.

2. **Inflection historical backfill (unblocks ETFS_AVGCAP.AC#2).** Added an additive `event["date"]` target to inf-etf-ownership-daily (default latest-partition path unchanged), deployed (inf-pipeline-v1.7.75), and backfilled the DEPLOYED lambda per-date over 2026-05-15..06-23 = **40/40 days WRITTEN, 0 skip/0 error**, byte-identical methodology to the live slice. Verified-on-served, comp-freshness PASS.
   - **2 grounded observations surfaced (Rule 22, mechanism not asserted):** (a) regime step at 06-03 (~$23-26M -> ~$78M); (b) flat-line 06-17..06-22 (4-ETF total identical to the cent $82,143,198.74 while source ETags DIFFER). DS source-grounded (b) = **REAL inf-gold ETF-price staleness** (T3 linear_interpolation carrying a flat 06-17 price). Traced the producer = `data/inf/scripts/gold/INF_build_canonical_prices.py`, **owner = DS (Rule 13)**; reprice routed to DS as a separate non-urgent TO.

3. **ETFS_SETUP W3 -- Cottonwood producer (new, GO'd).** Built cot-etf-ownership-daily as an inf-clone write-out producer; deployed (cot-pipeline-v0.4.4, 9-add/0/0); backfilled. COO-ACCEPTED + **CVO VERIFIED/GO** (sharp test ties to the cent).

4. **ASTN-box residuals (CVO go-live enable-flip).** Disposed the uncommitted instance.tf "drift" + stopped the replaced EC2 (Andrew-confirmed).

## ASTN-box residuals (done first per COO queue)

- **(a) instance.tf disposition = reverted-to-pristine.** Premise correction: the dispatch said "uncommitted associate_public_ip_address false->true WIP = committed-vs-live drift." Ground truth: `associate_public_ip_address = true` is **already COMMITTED** (instance.tf:44) and **intended/CTO-arch-gated** since instance creation (commit e0f7c24fb -- "ephemeral public-IP (EC2-own-IP FT test)", documented at instance.tf:4 + subnet var:15). The ONLY uncommitted delta was a cosmetic comment-whitespace alignment on the IMDS hop-limit line (Terraform ignores comment formatting). Reverted -> tree pristine, no future re-flip.
- **(b) STOP i-059405dfefcb4b44a** (astn-wsjft-scraper, was running @35.174.172.183) -- Andrew-confirmed via COO. `aws ec2 stop-instances` -> running->stopping->**stopped** (verified). Returns to normal idle-stopped; tonight's 3am orchestrator starts it.

## Deployment Sequence + Verification

### Deploy 1 -- inf-etf-ownership-daily (backfill enablement), inf-pipeline-v1.7.75
- code cfb653561 (ds-commit-gate clean) -> build-and-upload (sha 5yDLvUDP) -> source-map 2ff1d4fa5 -> ledger opened -> `safe-apply` **0-add/1-change/0-destroy** -> `plan` = **No changes** (0-diff) -> record-deploy e5cfef946 -> tag inf-pipeline-v1.7.75 pushed --follow-tags -> ledger CLOSED (aace8f361).
- Backfill: per-date invoke 05-15..06-23 = 40/40 OK. Verified: `aws s3 ls daily/inflection/` = 40 slices; comp-freshness PASS; 06-22 sample sum ties DS's $82.14M/476.

### Deploy 2 -- cot-etf-ownership-daily (new producer), cot-pipeline-v0.4.4
- source 0dd808ef3 (ds-commit-gate clean: .py + .tf) -> source-map entry 450e87009 -> build-and-upload -> ledger opened (single explicit `--leg`, avoided the inf --pipeline phantom-leg expansion) -> `terraform init` -> `safe-apply` **9-add/0-change/0-destroy** -> `plan` = **No changes** -> record-deploy 8b910e0e6 -> tag cot-pipeline-v0.4.4 pushed -> ledger CLOSED (e9c2b665e).
- comp-iam CLEAN (own-firm cot read + Deny-free etfs write, NO bd, NEVER#1).
- Backfill: 35 partitions in window -> **10 valued WRITTEN (06-08..06-22), 25 SKIP (no-valued-source, nonzero_mv_frac=0.0), 0 error.** Verified-on-served: 10 slices at daily/cottonwood/, 06-22 schema-valid (DIVZ $638,656.56/IDVZ $173,763.07/PFDE $143,625.44/PFOE $84,970.97), comp-freshness PASS.
- CVO sharp test PASSED: 06-22 $1,041,016.04 EXACT, 06-15 EXACT, 06-08 1c-rounding; firm-sep NEVER#1 confirmed at data level (every source_artifact = opal-data-cot only).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-freshness artifact | daily/inflection/ (x2), daily/cottonwood/, opal-data-inf gold/holdings (attempted) | PASS | validate-on-served for both backfilled series |
| comp-iam service | cot-etf-ownership-daily (pre+post-apply) | CLEAN | own-firm read + Deny-free write, no bd, no cross-firm; boto3 calls all covered |
| comp-which | cot gold-source Q; inf-price-producer Q | manifest-backstop | routed to backstop (known limited routing); rail-checked the raw enumerations |
| comp-grep | linear_interpolation/transaction_observed in data/inf | 3 matches/2 files | traced obs#2 producer = INF_build_canonical_prices.py |
| ds-commit-gate | inf + cot lambda_function.py | PASS | py_compile/ruff/AST clean |
| safe-apply | inf-pipeline, cot-pipeline | applied, 0-diff after | HALTGT clean |

- **What worked:** comp-iam service gave a clean pre-deploy NEVER#1 verify on the new cot role; comp-grep cleanly traced the price-staleness producer + owner.
- **What failed:** comp-which routed both substantive questions to the manifest-backstop (no rich tool for parquet-schema/prefix-enumeration); used rail-checked raw `aws s3 ls` for source grounding. comp-freshness needs subcommand `artifact <prefix>` (not a bare path).
- **Gap found:** `deploy_ledger.py open --pipeline inf` auto-expands a single-lambda TF deploy into all 8 inf S3-code phantom legs (NEVER-law false-half-landed noise). Filed: docs/briefs/deploy-ledger-phantom-leg-gap-20260625.md (COO low-pri tooling TO). Workaround proven: open with explicit single `--leg`.

## Files Modified

See commit messages: cfb653561, 2ff1d4fa5, e5cfef946, aace8f361 (inf backfill); 0dd808ef3, 450e87009, 8b910e0e6, e9c2b665e (cot W3); 2a95cb25e (core-doc + gap brief). instance.tf reverted (no commit).

## MCP traffic

~18 messages. Significant: RAVC2 bring-up reconcile (W1-done/W2-reassigned) -> COO ACCEPTED; backfill feasibility ACK + ETA -> COO accepted; ASTN-box confirm (instance.tf + EC2 stop); backfill RAVC -> ACCEPTED; obs#2 trace (owner=DS) -> ACK, reprice routed to DS; W3 RAVC2 -> COO ACCEPTED + CVO VERIFIED/GO cert (RAVC closed); deploy_ledger gap filed.

## Blockers

None. ETFS lane CLEAR.

## Current State

- **ETFS_SETUP producers built:** W1 inf-etf-ownership-daily (inf-pipeline-v1.7.75; live forward via S-D4 sentinel + backfilled 40 days 05-15..06-23; ~$82M/4-ETF). W3 cot-etf-ownership-daily (cot-pipeline-v0.4.4; daily-schedule cron(30 10 * * ? *) since cot has no gold-complete sentinel + opal-data-cot EventBridge-off; 10 valued slices 06-08..06-22; cot valued series STARTS 06-08, May unpriced). W2 (49F) = 0.5.0_AE_OpalETL.
- Both producers: write-out model, read own-firm only, write opal-data-etfs/daily/{partner}/{date}.json (schema_version 1.0), NEVER#1 by construction. Both date-targetable via event["date"].
- ASTN scraper EC2 i-059405dfefcb4b44a STOPPED; astn-pipeline instance.tf pristine (public-IP=true is committed/intended).
- inf-gold ETF-price staleness (obs#2): producer INF_build_canonical_prices.py, owner DS, reprice = DS non-urgent TO (06-18..22 historical, AVGCAP-immaterial).

## Next Steps

- **[3.0.0_SA_CVO]** W3 verify-leg DONE (VERIFIED/GO cert received + RAVC-closed).
- **[0.4.0_DS_ClientPlatform]** run AVGCAP.AC#2 (inflection full May-partial + June-MTD over 40 written days) + AVGCAP-W3 (cottonwood June-MTD over 10 written days, May N/A per D3 partner-clocks); confirm reader codes against daily/cottonwood/. Reprice INF_build_canonical_prices.py T3-interpolation (separate non-urgent TO).
- **[2.0.0_SA_COO]** slot the deploy_ledger phantom-leg gap brief under an NFRA tooling project; re-aim me (staged TOs: COTETL AUAFIX-DATEMODE-B/C, DC1-orion, DC2-eclipse, NFRA_TSGRAPH P2-2 -- need GO; smartx 3-support-lambda reconcile still held).
- **[0.7.0_AE_CloudOps]** IDLE-available, event-driven; will act on next dispatch. Won't self-initiate non-GO'd TOs (scope-discipline).
