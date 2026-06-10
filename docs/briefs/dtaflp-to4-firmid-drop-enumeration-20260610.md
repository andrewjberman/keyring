# NFRA_DTAFLP TO-4 prep — FIRM_ID env-switch site enumeration (cot gold tree)

**archetype:** TRACE
**Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-06-10 · **TO:** NFRA_DTAFLP TO-4 prep (COO GO, LD-0177)
**Scope:** READ-ONLY enumeration. TO-4 execution (drop the FIRM_ID env-switch, hardcode firm-native, add cherry-pick README) is HELD pending Andrew DTAFLP go. No `.py` edited.

---

## Headline

- **8 FIRM_ID declaration sites** (the edit targets) across 8 production gold scripts.
  - 6 env-switched: default `'49financial'`.
  - **2 HARDCODED to `'49financial'` (D_03, D_04) — these do NOT honor the env** → latent label mismatch under cot (see Finding 1).
- **4 FIRM_NAME env-switch sites** (default `'49 Financial'`), paired with the FIRM_ID ones.
- **Drop-target values (confirmed empirically):** `FIRM_ID='cottonwood'`, `FIRM_NAME='Cottonwood Capital Advisors'`. cot's live platinum partition is `s3://opal-data-cot/platinum/cottonwood/`.
- **S3-path blast radius = exactly ONE firm_id-templated key:** `lib/s3_layout.py:186` `platinum/{firm_id}/ownership_map.json` (consumed only by D_00). Every other platinum key partitions by advisor_id / rel_id / account_id / date — firm_id is a **JSON field**, not a path component, everywhere else. So the drop is label/output-correctness + removing env ambiguity; **no S3 path migration** (cot already writes `cottonwood/`).

---

## The 8 FIRM_ID declaration sites (edit targets)

| # | File:line | Current | Type | TO-4 action |
|---|---|---|---|---|
| 1 | `C_06.client_mix_timeseries.py:98` | `FIRM_ID = os.environ.get('O6B_FIRM_ID', '49financial')` | env (**`O6B_FIRM_ID`** — distinct var name!) | `'cottonwood'` + see Finding 2 |
| 2 | `D_00.portal_aggregates.py:77` | `os.environ.get('FIRM_ID', '49financial')` | env | `'cottonwood'` |
| 3 | `D_00b.portal_timeseries.py:53` | `os.environ.get('FIRM_ID', '49financial')` | env | `'cottonwood'` |
| 4 | `D_00c.portal_leaderboard.py:53` | `os.environ.get('FIRM_ID', '49financial')` | env | `'cottonwood'` |
| 5 | `D_01.partner_analytics.py:88` | `os.environ.get('FIRM_ID', '49financial')` | env | `'cottonwood'` |
| 6 | `D_02.advisor_client_detail.py:82` | `os.environ.get('FIRM_ID', '49financial')` | env | `'cottonwood'` |
| 7 | `D_03.composition_artifacts.py:95` | `FIRM_ID = '49financial'` | **HARDCODED** | `'cottonwood'` (fixes Finding 1) |
| 8 | `D_04.client_portal_summary.py:132` | `FIRM_ID = '49financial'` | **HARDCODED** | `'cottonwood'` (fixes Finding 1) |

## The 4 FIRM_NAME declaration sites (paired)

| File:line | Current | TO-4 action |
|---|---|---|
| `D_00.portal_aggregates.py:78` | `os.environ.get('FIRM_NAME', '49 Financial')` | `'Cottonwood Capital Advisors'` |
| `D_00b.portal_timeseries.py:54` | `os.environ.get('FIRM_NAME', '49 Financial')` | `'Cottonwood Capital Advisors'` |
| `D_01.partner_analytics.py:89` | `os.environ.get('FIRM_NAME', '49 Financial')` | `'Cottonwood Capital Advisors'` |
| `D_02.advisor_client_detail.py:83` | `os.environ.get('FIRM_NAME', '49 Financial')` | `'Cottonwood Capital Advisors'` |

(D_00c, D_03, D_04, C_06 have no FIRM_NAME declaration.)

---

## Findings (decision-grade, for COO/CTO before TO-4 execution)

**Finding 1 — D_03 + D_04 hardcode `'49financial'` and IGNORE the FIRM_ID env.** The cot runner sets `FIRM_ID=cottonwood` in its environment, and the 6 env-switched sites honor it — but D_03:95 and D_04:132 are literal `'49financial'`. Consequence: cot's D_03 (composition `scope.firm_id`) and D_04 (client_portal_summary `firm_id` field) outputs currently carry **`firm_id='49financial'`** even though the data is Cottonwood's. This is a label-only mismatch (those firm_id values are JSON fields, not S3 paths — the artifacts still land in the correct advisor/rel-partitioned keys), but it is a real latent inconsistency. **TO-4's hardcode→`'cottonwood'` flip FIXES it.** Worth a quick portal-consumer check on whether the FE reads `firm_id` from D_03/D_04 payloads.

**Finding 2 — C_06 switches on `O6B_FIRM_ID`, not `FIRM_ID`.** `C_06.client_mix_timeseries.py:98` reads the env var **`O6B_FIRM_ID`** (legacy "O6B" naming), not `FIRM_ID`. If the cot runner sets only `FIRM_ID=cottonwood` and not `O6B_FIRM_ID`, then C_06 currently defaults to `'49financial'` for cot — same latent mismatch class as Finding 1. **Verify the cot runner's env** (AE domain) or simply hardcode `'cottonwood'` in TO-4 to make it env-independent (the firm-native intent).

**Finding 3 — single S3-path firm_id dependency.** Only `platinum_advisor_ownership_key()` (`lib/s3_layout.py:186`) puts firm_id in a path. D_00 calls it with the env-switched FIRM_ID (=`cottonwood`), so cot already writes `platinum/cottonwood/ownership_map.json` correctly. The FIRM_ID drop does **not** move any cot output; it removes the env-switch and aligns the label fields. Zero path-migration risk.

---

## TO-4 mechanical recipe (when Andrew DTAFLP go lands — HELD, no writes now)

1. Replace all 8 FIRM_ID declarations with firm-native `FIRM_ID = 'cottonwood'` (drop the env-switch entirely per PRD §1a.4).
2. Replace the 4 FIRM_NAME declarations with `FIRM_NAME = 'Cottonwood Capital Advisors'`.
3. The ~30 downstream **usage** sites (`'firm_id': FIRM_ID`, `scope={'firm_id': FIRM_ID}`, `firm_name`) need NO edit — they reference the variable; fixing the 8+4 declarations fixes them all.
4. Add the deliberate-cherry-pick divergence README to the forked cot gold tree (PRD §1a.4 / TO-4).
5. Rule 14 gate (`.tools/ds-commit-gate.sh`) on every edited `.py`; Rule 13 deploy cycle to `opal-data-cot/code/gold/`.
6. Sequencing: TO-4 follows the TO-1b retarget write; both gated post-GLDINC-night-4 and behind Andrew's DTAFLP go.

---

## Cross-reference
Pairs with the TO-1b classification (`docs/briefs/dtaflp-to1b-cot-gold-bd-ref-classification-20260610.md`, commit `0e5b6e5f3`). Together they give a complete firm-native fork edit map: 7 live bucket-retargets + Schwab default (CTO-APPROVED → `opal-data-cot`) + 8 FIRM_ID + 4 FIRM_NAME declaration flips.
