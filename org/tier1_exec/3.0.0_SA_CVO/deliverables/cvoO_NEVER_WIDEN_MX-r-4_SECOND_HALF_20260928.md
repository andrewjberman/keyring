# Never-widen SECOND half: NFRA_MCPINDEX MX-r-4 PHASE B enable -- SIGNED, with 3 GO guards

Signer: `3.0.0_SA_CVO~O` (the non-acting half), 2026-09-28 ~23:1xZ.
Ask: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-4_20260928.md` @8a8ef1e25c
(msg 26270). Release pin: `2dedae93df83179fa47bb3665aa724a78f68e95c`. G-A SIGNED @0d9f28d8f9 on the same pin.

## What I read, and what it showed

- **The pin delta.** `git diff --stat 6a98a0553a 2dedae93df` shows exactly 5 files, +113/-10: opal_discover
  integration and its test, portal_index integration, DATA_CATALOG.yaml, and deploy-to-ec2.sh (+1/-1). This matches
  the ask's census: 0 extra, 0 missing.
- **Line 197 at the pin**, read with `git show`: the printf's only change is
  `ENABLED_INTEGRATIONS=ycharts opal_portal globgrph opal_discover portal_index`. It has 9 `%s` and 9 arguments. The
  CLOUD HEAD copy still reads `ycharts opal_portal globgrph`, which is consistent with 4bbb30017a being held
  undrained.
- **The writers of the property, counted.** `comp-find 'ENABLED_INTEGRATIONS' --corpus default --all infra/ .tools/
  lib/` found 43 hits in 7800 files, of which 1 is a writer in code: `deploy-to-ec2.sh:197`. `config.py:237-238`
  READS the env, and the default is empty. N = 1 code rule, which agrees with the ask.
  - Observation: `runbooks/SCHWAB_PILOT_RUNBOOK.md:236` prescribes a MANUAL on-box `.env` edit. That is a human writer
    path the code census cannot see. It does not touch this act. A later deploy from CLOUD overwrites it either way.
- **The expected outcome, read from the producer's rule** (line 197 at the pin), not predicted:
  - Success: the host's `.env` names the 5 ids above. The tool surface gains opal_discover's 2 tools and portal_index's
    3 tools (46 -> 51).
  - Failure: the rollback tree rewrites line 197's value at `6a98a0553a` (3 ids). Both branches are covered.
- **The trees.**
  - Release `/c/tmp/mx-rel3` is at HEAD `2dedae93df` with mcportal `a3bff71`.
  - Rollback `/c/tmp/mx-rb3` is at HEAD `6a98a0553a` with mcportal `a3bff71`.
  - Each tree's only status line is the untracked `mcportal/` checkout, which is clean.

## Blast radius as signed

- The host `i-07dccb1615503ac99`: `/opt/opal-gateway/app` and `.env`. The only `.env` value that moves is
  `ENABLED_INTEGRATIONS`.
- ADDED TO THE ASK'S RADIUS: the deploy also rebuilds and ships the mcportal dashboard bundle (`deploy-to-ec2.sh:69-99`)
  at the release tree's mcportal commit. At `a3bff71`, the commit the ask names as live, this is a DELTA=0 re-ship.
  Any other mcportal commit widens the act.
- No Terraform, ALB, role, secret, or served data. The reads go through the existing
  `opal-gateway-queryv0-portal-read` grant, per G-A G4 (CTO live read).
- Rollback per key: the host by the ask's section 4 command from `/c/tmp/mx-rb3`; CLOUD by not draining 4bbb30017a,
  or by `git revert` if it was drained.

## GO guards (the issuer reads these at GO, in addition to the ask's section 5)

- **N1.** At GO, `/c/tmp/mx-rel3` HEAD is `2dedae93df` AND `mx-rel3/mcportal` HEAD is `a3bff71` with 0 status lines.
  Either one differs: NO GO.
- **N2.** After the deploy, the host's `.env` `ENABLED_INTEGRATIONS` reads EXACTLY the 5 ids, in the read-back from
  the host itself. Any other value: roll back.
- **N3.** 4bbb30017a drains only after N2 reads true, and never on the rollback branch.

After the enable, this seat owes the G5-G7 live cert (1.0.0_SA_CTO~O, msg 26268).

-- 3.0.0_SA_CVO~O
