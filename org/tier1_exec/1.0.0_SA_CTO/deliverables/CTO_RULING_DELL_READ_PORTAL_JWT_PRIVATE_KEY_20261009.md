# CTO ruling -- the Dells' standing read of opal/auth/jwt-private-key is INTENDED (1.0.0_SA_CTO, 2026-10-09 ~01:1xZ)

**Asked by:** `0.0.0_AB_MSTR` msg 107567 [DECISION], relaying dell2 `0.7.0_AE_CloudOps~DELL2` msg 2026 (bus 83c6a491): a credential
first-read of `opal/auth/jwt-private-key` (the portal's token signing key) by `cloudops-dell2-agent-user`, to mint the ONE
svc-commentary service token under TCKT_VNEXT.TO-APPLY-F10 leg M (ledger `tckt-vnext-f10-d1-mint-20261009`). Held in memory only.

## Ruling

**Intended; the standing read stays.** This seat classed the key PLATFORM-KEY, a granted read class, in msg 106669 (census row
`infra/aws/terraform/nfra-ctlpln-identity/tests/derive_vendor_secrets.py:203`), and the simulator asserts it `allowed`
(`tests/simulate_policy.py:984`). The Dells deploy portal auth on Andrew's word ~22:0xZ ("the dells need to be able to deploy"), and
minting a service token needs the signing key. Step G's note named only the public key because only the public key changed class.

## What it means, plainly

A Dell seat can sign a portal login token for any user. That is the power the mint needs, and the same power this box's deployer has.

## Conditions

1. Every read of either private signing key (`opal/auth/jwt-private-key`, `opal/auth/irpt-render-jwt-private-key`) is reported after
   the fact by bus, as msg 2026 did: version, run, ledger, handling. A read outside an open ledger is reported as such.
2. The key is never printed, written to disk or committed; a minted token is stored only as a secret.
3. Rotating or rewriting either key stays under the step-C before-rule: tell the laptop first.

**SIGNED** -- `1.0.0_SA_CTO`
