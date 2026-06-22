# COT launch -- smoke-cred provisioning + gate#1 RUNTIME isolation confirm (opalinvest.dev domain-catch) + D_01 publish/chain fast-follow

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

Window: ~18:49Z -> ~20:45Z. Serial: 0.7.0_AE_CloudOps. TOs: COT-LAUNCH (HIGHEST-PRIORITY) + ADVI_COTETL publish/chain fast-follow.

## Current State

**COT launch is technical+display-ready -- both security gates PASS; the partner_analytics publish/chain durable-wiring is DEPLOYED.** My contributions this window:

### 1. COT-launch gate#1 (cross-firm isolation) -- provisioned + RUNTIME-confirmed
- PROVISIONED a cottonwood SCOPED smoke cred: reused the dormant DT cred user@cottonwood.com (firmId=cottonwood SCOPED, role=user, NOT internal), reset passwordHash to a known value (reversible -- old hash captured). Verified data-layer (email-index GSI resolves + bcrypt MATCH).
- CAUGHT + flagged a COO premise error: the TO said "firmId=cottonwood = full+internal"; per firmAccess.ts:44 + the provisioning standard, cottonwood=SCOPED, opal-capital=full+internal. A full+internal user sees all firms -> would have caused a security FALSE-PASS. Provisioned scoped deliberately; COO corrected the TO + the banked memory.
- RUNTIME-confirmed gate#1 via authed-curl (my env reaches the live portal; CVO+DE could not). THREE results: (a) ROOT CAUSE of the "no-DNS": the live portal is opalinvest.dev/www.opalinvest.dev, NOT portal.opalinvest.com (the CF aliases; the wrong domain = everyone's no-DNS) -- unblocked CVO's own exercise; (b) ZERO cross-firm leak: a scoped cottonwood JWT requesting ?firmId=49financial/inflection got COTTONWOOD data every time (firm_id=cottonwood), disallowed-artifact->403, unauthed->401; (c) Rule-22 nuance flagged (not glossed): the mechanism is JWT-firm-PINNING (router ignores ?firmId, serves own-firm) + per-artifact-403, NOT the expected uniform cross-firm-403 -- handed CVO the precise observable + the cert-question instead of declaring PASS. CVO formally CERTED gate#1 PASS.
- gate#2 (partner_analytics live-200) CVO+DE-verified on the same cred. On COO's gate#2-close signal, REVERTED the cred: restored old hash; LIVE-PROVED dead (test-pw login -> 401). Memory banked (opalinvest.dev + authed-curl + pinning isolation).

### 2. ADVI_COTETL publish/chain fast-follow -- D_01 chained (DEPLOYED)
- Problem: partner_analytics was a one-off direct-write @06-18; D_01 NOT in opal-cot-gold-run -> tomorrow's nightly advances siblings to ~06-22 but partner_analytics stays 06-18 = vintage skew on the live Distribution tab.
- Ground-truthed the wiring (CHAIN-ONLY, per DS): D_04.build_partner_analytics IS the publisher (gold/artifacts->platinum, already chained); the only gap was D_01 unchained. CAUGHT + resolved a dead-dep concern: D_01's docstring named the just-deleted C_02 client_performance as primary AUA source, but the actual code (D_01:311-313, c5bc7ba49) reads account_performance/C_03 snapshot (DS confirmed zero frozen reads; secondary refs use the C_03-derived variable).
- DEPLOYED: added D_01 BEFORE D_04 in opal-cot-gold-run (live order D_00/D_00b/D_01/D_02/D_03/D_04; D_01 idx14<D_04 idx17 verified on the live doc). D_01=optional. Parity deployed==c5bc7ba49. safe-apply 0/1/0; 0-diff; deploy_ledger (cot-chain-d01-partner-analytics; ae-chain-add CLOSED, nightly-verify OPEN). commit 9f8d290a5. Landed ~5h before 02:00Z. Direct-write kept tonight (belt-and-suspenders; DS removes after-confirm).

### 3. DEBTSCAN-D3 (paced) -- foundational vocabulary census
- Freshness gate PASS (comp-kuzu HEAD current), canon-patterns + suppression_v1 re-confirmed, schema grounded (single CloudNode/CloudEdge, type-as-property), node_type census (31 types) + edge_type census (READS 673/WRITES 576/FLOWS_TO 961/TRIGGERS 97/INVOKES 40...). Scorer fully grounded; 4-class enumeration build paced to fresh attention.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-routes | behaviors | PASS | mapped /api/scoped/* auth-validator-edge routes for the gate#1 curl |
| comp-kuzu | node_type + edge_type census; freshness | PASS | DEBTSCAN scorer vocabulary; HEAD current |
| comp-grep | partner_analytics / D_01 reads / client_performance producer | PASS | grounded the fast-follow wiring + the dead-dep |
| deploy_ledger.py | open/close-leg | PASS | cot-chain-d01 registered |
| (parity/aws) | D_01 deployed==c5bc7ba49; authed-curl opalinvest.dev; DDB provisioning -- rail-checked/operational | PASS | runtime ground-truth, not self-report |

**What worked:** verify-on-LIVE (authed-curl) found the wrong-domain root cause + proved zero-leak; premise-catch (scoped vs internal) prevented a security false-PASS; dead-dep catch (D_01/client_performance) verified via source before chaining ("don't rush-to-broken"); Rule-22 mechanism-nuance (pinning vs 403) handed to the cert owner not glossed. **What failed:** nothing this window. **Gap:** comp-pipescript deployed cot-blind (rail-checked parity overrides).

## Blockers

None. COT launch ready (both gates CVO-cert). Fast-follow nightly-verify = DS (tomorrow-AM) -> I close the cot-chain-d01 ledger.

## Next Steps

- **[0.4.0_DS_ClientPlatform]** verify-on-served tonight's nightly: partner_analytics reconciles fresh-date/$395.30M/"Not state-attributed" slice -> ping me; + remove the direct-write after-confirm.
- **[0.7.0_AE_CloudOps] TOMORROW-AM:** close the cot-chain-d01 ledger on DS's served-confirm; the cot-cleanup nightly-verify (de-chain no regression) + DATEMODE stick-verify (served advances past 06-18) + A_00 tripwire (all ride tonight's 02:00Z nightly).
- **[0.7.0_AE_CloudOps] queue (paced):** DEBTSCAN-D3 scorer-build (4-class enumeration + gates + AC4) -> ETFS-W1 (DS-contract locked).
- **[Andrew]** real Cottonwood users (AC2) provision off Andrew's list (NOT the smoke cred) -> go-live; + F-1 email click + the S3-orphan clearance (COO-bundled).

## Ops note

cot-exporter EC2 i-0643a5bee8a8feabf RUNNING (tonight's nightly). The smoke cred is REVERTED (live-proved dead). All cot writes via deployed code / sanctioned provisioning (no ad-hoc).
