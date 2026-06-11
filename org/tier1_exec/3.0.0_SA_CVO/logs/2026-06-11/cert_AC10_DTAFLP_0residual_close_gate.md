# CVO Certification — NFRA_DTAFLP AC10 (0-residual firm-separation close-gate)

**Certifier:** 3.0.0_SA_CVO · **Date:** 2026-06-11 · **Verdict: PASS — AC10 CLOSES.**
**Method:** independent structural re-derivation (not RAVC2-trail trust), verify-before-flag.

## What AC10 actually binds (scope precision)
AC10 §9 literal scope = **bd/cot firm-separation**: "no cot runtime path resolves to bd code or bd data — no shared script body, no shared lib/, no mirror sync, no `opal-data-bd` access from any cot role." This is distinct from **AC2** (the `data/orion`→`data/inf` rename 0-residual). The COO close-board bundled them; this cert separates them cleanly. The `data/black_diamond`→`data/bd` rename was **descoped** (LD-0179, "black_diamond stays") — so its tree legitimately remains at `data/black_diamond/` (931 files) and compiler refs to it are CORRECT, not residuals.

## AC7 — gold tree forked + FIRM_ID dropped — **PASS**
- `data/cot/scripts/gold/lib/` = 13 independent lib files (own `floored_percentiles`, `nna_flows`, `gold_utils`, `s3_layout`, `config.py`, …).
- `git grep "FIRM_ID','49financial'"` under `data/cot/scripts/gold/` = **0** (no shared-default env-switch).
- FIRM_ID is firm-native: `FIRM_ID = 'cottonwood'` (C_06:96, D_00:77). TO-4 satisfied.

## AC8 — mirror severed — **PASS**
- Live `ssm.tf:278-279` syncs cot FROM `s3://opal-data-cot/code/gold/` (cot's own git-versioned tree), **never** `opal-data-bd`.
- The `aws s3 sync opal-data-bd/code/gold → opal-data-cot/code/gold` at line 213 is inside a commented-out DO-NOT-mirror warning block — not live.

## AC9 — cot deploy gated — **PASS (structural confirm + TO-3 RAVC2-trail)**
- `safe_deploy_core.py` PIPELINE_MAP: `"cot": ("opal-data-cot", "cot")` — confirmed.
- TO-3 (gate wiring) RAVC2-accepted by COO. Note: an explicit `cot` literal in `comp-pipescript` was not found by grep; routing is covered by PIPELINE_MAP. Accepted on the RAVC2 trail + structural map confirm (the one leg not 100% independently re-derived — flagged honestly).

## AC10 §9 — no cot→bd code/data — **PASS**
- Real (non-docstring) `opal-data-bd`/`opal-data-inf` refs under `data/cot/` .py/.sh = **0**. The single scan hit (`cot_silver_merge.py:25` "Default BD_S3_BUCKET = opal-data-cot (not opal-data-bd)") is a guard-recognized reassurance docstring (ds-precommit explicitly whitelists this phrasing).
- Cross-firm AST guard LIVE (`ds-precommit-check.py:61` `_CROSS_FIRM_FOREIGN_BUCKETS['data/cot/'] = ('opal-data-bd','opal-data-inf')` + `check_cross_firm_bucket_refs`).
- IAM cross-bucket hard-Deny LIVE (`20617a347`, per PRD §1a backstops).

## Falsified-on-verify (verify-before-flag)
- **Hypothesis:** cot's `floored_percentiles.py` byte-identical to bd's ⇒ shared lib body ⇒ AC10 violation.
- **Falsified:** the ds-precommit byte-identical sync group is `bd + inf + smartx` ONLY (`ds-precommit-check.py:38-40`); the **cot copy is NOT a member** → it is an independent fork free to diverge, which *satisfies* AC10's "two trees diverge freely." Not a violation.

## Rulings on the two COO-raised questions
1. **floored_percentiles provenance comment (`data/orion/...` at line 5 + bd-centric docstring) — DOCUMENTED-EXEMPT; AC10 closes with it.** It is a docstring, not a runtime bucket reference; AC10 binds runtime path resolution, and the cross-firm AST guard skips docstrings by design (zero-false-positive real-bucket-ref matching). Scrubbing the bd/inf/smartx copies needs a 2-3-lane atomic commit against the sync group for zero contamination benefit — disproportionate. **Opportunistic recommendation (non-blocking):** the *cot* copy is NOT in the sync group, so its stale "bd / 49 Financial" docstring can be made firm-native independently during TO-4 follow-through.
2. **post-P1-mv vs independent — AC10 certifies INDEPENDENT of P1-mv.** P1-mv (`data/orion`→`data/inf`) is AC2-scope (inf rename), orthogonal to cot/bd firm-separation. Moot anyway: P1-mv already landed (`data/orion` = 0 tracked, `data/inf` = 190).

## AC2 (data/orion→data/inf 0-residual) — separable, effectively PASS w/ 2 cosmetic residuals
Not part of the AC10 binding gate, recorded for the DTAFLP macro-close:
- floored line-5 provenance docstring (above) — documented-exempt.
- 5 `manual_api` files (`probe_tax_txn`, `pull_inflection_{assets,representatives,transactions}`, `pull_tax_realize_full`) carry hardcoded **absolute Windows DEV paths** (`C:/.../data/orion/manual_api/...`) — non-runtime, dev-author-only ad-hoc utilities, blocked from sweep by pre-existing AE-inf Rule-14 debt. Documented-residual; AE sweeps opportunistically when clearing the Rule-14 debt. Their other `orion` tokens (`api.cloud.orionadvisor.com`, S3 key `orion/jwt/`) are vendor/bucket-key forms that correctly STAY (§2/§3 — buckets not renamed).
- Compiler `data/black_diamond/...` refs = correct (bd descoped). `orion-gold-dispatch.sh` / `_parse_orion_dispatch` = Orion vendor-name forms, stay (§2). Path-regex already `(black_diamond|inf|schwab)` — correctly updated.

## Disposition
**AC10 (firm-separation binding close-gate): CERTIFIED PASS — DTAFLP closes on AC10.** AC2 cosmetic residuals documented-accepted, non-blocking, opportunistic sweep. No contamination vector remains: code-plane (fork + AST guard), data-plane (IAM Deny), deploy-plane (own-bucket sync) all verified.
