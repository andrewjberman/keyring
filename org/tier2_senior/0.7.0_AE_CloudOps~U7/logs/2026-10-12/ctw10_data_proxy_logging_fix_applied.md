# opal-portal-data-proxy stops logging callers' credentials: stopped, ruled, applied, read — 0.7.0_AE_CloudOps~U7

**archetype:** DEPLOY
**Date:** 2026-10-12
**Task Order:** NFRA_CTLPLN.TO-CT-w-10.data-proxy-logging-fix-apply-and-exercise
**Status:** COMPLETE (proof instance VALID); the purge and the refresh-token invalidation are Andrew's and NOT done; the status flip is the issuer's

---

## Objective

Land the third pair's fix (the handler stops printing the whole event) and read the new log lines. Written for a reader with no prior context; it continues `ctw10_stopped_pre_apply_long_lived_credentials_in_logs.md`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | service opal-portal-data-proxy | PARTIAL | 35 calls, 18 GRANTED, 17 UNRESOLVABLE-RESOURCE; a floor, unchanged |
| deploy_ledger.py | open, hold --pre-apply, hold --release, 5 close-leg | PASS | entry nfra-ctlpln-ctw10-data-proxy-logging-fix-20261012 |
| safe-apply.sh | one apply of the saved plan | PASS | 0 added, 1 changed, 0 destroyed |
| proof-of-spec-check.py | instance + CTw10-AC1,2 | PASS | VALID rc=0 |

**What worked:** counting by key name and age; piping log reads straight into counters so no value touched disk; the header-excluded diff of `firm_page_access.py`.
**What failed:** nothing this half.
**Gap found:** the ruling and pair assumed only 15-minute tokens were in the logs; the events also carried `refresh_token` and `device_trust` cookie names (row NFRA_CTLPLN-S9112).

---

## Work Completed

1. PRE: whole 14-day group, 1202 events: 49 JWT-shaped, cookie names `refresh_token` (38 lines, 16 within 7 days) and `device_trust` (29). Per the order: STOP, ledger HELD-PRE-APPLY, row S9112, ask relayed.
2. The CTO ruled (msg 108528, AMENDMENT 2): STOP lifted for the apply only; recorded MET. Released the hold.
3. P0 equal to the second pair; built at pin `5a0dfc9af8`; exactly 3 members; `firm_page_access.py` differs from the live one in its header line only (empty diff with it excluded); uploaded `fhBfCdz9...`.
4. Plan Branch A; one `safe-apply`; live CodeSha256 `zoCWZxmn...`; apply time 11:58:21Z.
5. Reads: partner and internal `/aum/metrics` 200; partner class-(ii) 403. Log events after the apply: 25, `jwt_shaped=0 bearer=0`, 0 cookie words.
6. Step 6: the 16 recent `refresh_token` lines come from 2 identities (digests only); both internal staff, one active, one disabled.
7. Recorded `7e6a1cd46d`, tag `market-overview-v1.11.7` (LOCAL).

## Decisions Made

- Held the apply on the PRE finding exactly as ordered, and said so with the cost (new lines keep accumulating), rather than deciding the CTO's question.
- For step 6, printed account category (internal/partner, active/disabled) beside the digests: category is not an identity and sizes the exposure.

## Files Modified

`infra/aws/lambda/ci/lambda-source-map.json` (one entry), `infra/aws/terraform/market-overview/CHANGELOG.json`, the surprise channel (row S9112), this seat's deliverables and logs, the ledger entry and its sentinel.

## Blockers

None for the apply. Open and Andrew's: the purge of the group's events; invalidating the refresh tokens of the one active internal account in the digests file; the 29 `device_trust` lines (identities not listed).

## Current State

Fix live and verified; fence of the earlier pairs intact; ledger closed at cleanup; no standing credential.

## Next Steps

1. `[2.0.0_SA_COO~C]` Read the proof instance; carry the digests file to Andrew; flip the order.
2. `[0.0.0_AB_MSTR]` Carry `7e6a1cd46d` and tag `market-overview-v1.11.7`.
