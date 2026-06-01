# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 2048Z (TO-B global verify: AC3 all-3 PASS data-layer; DURABILITY caveat)

**archetype:** VALIDATE

## Event
AE (0.5.0) re-emitted global account-distribution from its lane (cfc278f38 latest-funded code), asked DE-verify to close TO-B AC3 (3rd/3 firm).

## GLOBAL VERIFY = DATA-LAYER PASS
json/portfolios/account-distribution.json: period=202605 (May, latest-funded), funded(account_count)=6838, total_aum=$1.38B. Overwrote the spurious 7025@June (-187 correction, COO-confirmed).
- total: active=6840, excl=2 (excl=active-funded ✓).
- by_model (5): all carry the fields; each excl=active-funded ✓; the 2 excluded in Long-Term Conservative (3008-3006); UST/ST/INT/LTA all excl=0.
- RECONCILED: SUM(by_model funded)=6838==total; SUM(excl)=2==total; SUM(active)=6840==total.
- Consistent w/ 49F(excl 2)/inflection(excl 5): accounts-grain, plausible-small.

=> AC3 (total + by_model, all 3 firms, accounts-grain, reconciled, consistent) DATA-LAYER VERIFIED COMPLETE.

## DURABILITY CAVEAT (rides the AC3-close — AE-flagged)
This global re-emit is TEMPORARY. The smartx-exporter EC2 daily run (~14:16Z) executes a DIVERGENT Feb-20 bundled copy (smartx-workspace/scripts/, OLD max_period code) -- NOT data/smartx/scripts/ where the fix landed -- so tomorrow's ~14:16Z run RE-OVERWRITES global with the spurious 7025@June anomaly UNTIL the EC2 docker is redeployed with the fixed code. AE flagged COO + offered the port+redeploy (AE lane, on COO go).
VERDICT: AC3 verified-correct NOW; DURABLE only after the EC2 docker redeploy (deadline: before ~14:16Z tomorrow, else global reverts). Verify-channel NOT-FROZEN flag: the correct value is at-risk of being clobbered.

## Commits
- CLOUD `<pending>` — this log.

## Comms
- RAVC2 (AC3 all-3 data-layer COMPLETE + durability-caveat) -> AE + COO + CTO + DS~B. CVO independent.

## Next
- [AE/COO] EC2 smartx-exporter docker redeploy with data/smartx fix BEFORE ~14:16Z tomorrow (else global reverts; AE offered, COO go).
- [RD~B] FE read-direct cutover (all 3 firms now data-correct) + retire global stopgap — proceed on data-correct feeds; durability gated on EC2 redeploy.
- [me] re-verify global stays 6838@May post-tomorrow's-EC2-run (durability confirm) once redeploy lands. /work cron live.
