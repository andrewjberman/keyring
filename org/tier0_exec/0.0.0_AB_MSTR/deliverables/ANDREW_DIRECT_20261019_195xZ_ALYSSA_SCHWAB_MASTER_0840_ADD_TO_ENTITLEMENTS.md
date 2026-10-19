# ANDREW-DIRECT 2026-10-19 ~19:55Z -- add master 0840 to Alyssa's Schwab entitlements

Given at the laptop `0.0.0_AB_MSTR` terminal (Claude Code session), 2026-10-19T19:55Z (3:55 PM ET). VERBATIM:

> "we need to add 0840 to her search ability for schwab. she has the 0824 and 0833 accounts at schwab, the smartx and black diamond masters. she needs the 0840 master too added to her entitlements."

## What it names (his words only)

- Who: "her" = Alyssa (the 3:00 PM ET gateway session; her Schwab grant is the `alyssa` role in the gateway entitlement store).
- What: add the "0840" Schwab master to her entitlements ("search ability for schwab"). She already has "0824" and "0833".

## Carried facts (measured, labelled; not his words)

- MEASURED 2026-10-19T19:5xZ, `.tools/aws s3 ls s3://opal-data-assets/schwab/`: three master prefixes: `08242234/`, `08335338/`, `08403355/`. The only prefix beginning 0840 is `08403355`, so "0840" most probably means master `08403355`. INFERRED mapping; the applier confirms it against the store.
- Existing process for a Schwab grant change: `ops/schwab_entitlement_admin.py` (`prepare`, `activate`, `revoke`) under `opal-gateway-access-admin`, with a never-widen ask signed by the CTO, COO and CVO halves (precedent: NFRA_OPLGTW `OG-mg-2`, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/NEVER_WIDEN_ASK_OG-mg-2.md`). This is a WIDENING (a new master for a principal), so it is that process's to run.

## What this record does NOT rule (relayed verbatim scope, never wider)

- It does not name Andrew's own grant, any other principal, any operation (including downloads), dataset, column or date window. Only "add the 0840 master to her entitlements".
- It does not ask `0.0.0_AB_MSTR` to write the grant. MSTR carries the word; the owner of the gateway entitlements (NFRA_OPLGTW, site Z) applies it.

-- 0.0.0_AB_MSTR (laptop), carrying Andrew's word
