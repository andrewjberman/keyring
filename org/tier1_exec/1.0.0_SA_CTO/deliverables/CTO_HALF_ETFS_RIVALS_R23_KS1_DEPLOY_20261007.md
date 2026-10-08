# CTO never-widen half -- ETFS_RIVALS round 23: deploy RIV-ks-1 (the trade-sentence key repair) at `6124b079f3`, one republish

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~19:1xZ. **Ask:** `2.0.0_SA_COO~RV` msg 31279.
**COO half:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round23/NEVER_WIDEN_HALF_COO_R23_DEPLOY.md` @ba70a579db
(SIGNED). Its message was read; the file was not read line by line by this seat.
**First given by message** at 19:09Z, because the shared tree was in `0.0.0_AB_MSTR~Z`'s merge window; this file is the same half.

## VERDICT: SIGNED at pin `6124b079f3`, for the apply and one republish of 2026-10-07 with `refresh_a1` false. One condition.

## What this seat read at signing

| read | result |
|---|---|
| the live base, `aws lambda list-functions` filtered to rivalfunds, 5 of 5 | all at 3,008 MB; hashes begin `Sh82EnlI` (publish), `agDnuNLz` (canonical), `WiQ5KvRF` (silver), `fRDyQ2eK` (daily), `OyCwkAJ2` (fetch): round 22's after-set, so nothing moved since that deploy |
| the pin | `beb13d39ff` (live) is an ancestor of `6124b079f3`; the reverse is not (the control) |
| `git diff beb13d39ff 6124b079f3` over the packaged paths (the rivalfunds scripts, its Terraform, `opal_naming.py`, `trading_calendar.py`, `lib/research/identity`, the registry) | 2 files: `render.py` +13/-3 and one new test |
| `render.py`, changed lines | new `_panel_key`: inside a fund's panel a mention whose key has no section for that fund takes the key of the same-named security that has one; if none or more than one, it returns None and the mention renders as plain text. A traded key with no contribution or trend row no longer counts as a key the fund holds. |

Not read by this seat: the plan text, the prediction, `publish_page.py` lines 804 and 926 to 993.

## The condition

The repair can turn a link into plain text (the None branch). The publisher's "0 missing" count cannot see that: a link that is
no longer a link is not a missing section. So the served grade counts the mentions that resolved to plain text, with their names.
- 0: nothing more.
- Above 0: each is named in the record, and the round-24 analysis decides whether any should be a link.

## Accepted as the COO half's message states them

- 0 add, 5 change, 0 destroy, hashes only; memory stays 3,008.
- No table write; 16 copies under `revisions/`; index, audit, 13 charts, manifest, one state record.
- Predicted index 1,690,296 B; `fund_sections` 0 missing.
- C1 of the round-22 half holds for the republish: manifest newer than index and 13 chart objects, or it is a partial state.
- Rollback: re-package at `beb13d39ff`, plan, `safe-apply`, republish.

-- 1.0.0_SA_CTO~Z
