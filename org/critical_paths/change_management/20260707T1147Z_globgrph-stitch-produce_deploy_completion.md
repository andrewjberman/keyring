# Deploy Completion Record
**Date opened:** 2026-07-07T11:47:21.032748+00:00
**Status:** RESOLVED-PARKED (external gate: secrets.PORTAL_REPO_PAT, Andrew-only GitHub org-secret) -- infra L1-L3 landed+proven; L4 first-produce-verify deferred to a fresh attempt when the PAT clears. Escalated loud (Andrew via COO); NOT a silent strand, NOT a half-landed deploy (infra fully landed).
**Deploy:** NFRA_GLOBGRPH stitch-produce: nightly-fresh cross-layer stitch (durable kuzu_stitch_db scratch-stale fix; COO NEAR-TERM, CTO domain-flag). 2-leg hybrid: GHA source-push + EventBridge->CodeBuild produce -> stitch_graph.json+marker; 0.8.0 builds the comp-debt ensure_fresh consumer.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit stitch-produce.tf (684c38511) + stitch-source-push.yml | hashes pushed origin/CLOUD | stitch-produce.tf + stitch-source-push.yml pushed origin/CLOUD @ 684c38511 (git merge-base --is-ancestor confirmed) | CLOSED 20260707T132725Z |
| L2 | activation | safe-apply LEG-2 (9 resources: GHA+CodeBuild+events roles, CodeBuild project, EventBridge rule+target) | plan 9add/0chg/0destroy applied + 0-diff | safe-apply (HALTGT, targeted) Apply complete 9 added/0 changed/0 destroyed: stitch_source_gha+policy, stitch_produce_codebuild+policy, stitch_produce CodeBuild project, stitch_produce_events+policy, EventBridge rule+target. (Was correctly HALTGT-blocked mid-run by the FEDOBS coordination; resumed after.) | CLOSED 20260707T115731Z |
| L3 | activation | LEG-1 workflow lands + GH-Action publishes stitch-source/source.zip | source.zip present in S3 | s3://opal-313476888478-globgrph/stitch-source/source.zip present (156994678 bytes, 2026-07-07 09:08:30) -- GHA stitch-source-push.yml published | CLOSED 20260707T132726Z |
| L4 | verify | first CodeBuild run produces a VALID stitch (node-counts validated vs known-good) + marker #1 published | stitch_graph.json+marker in S3, sane node counts |  | PARKED (external gate: PORTAL_REPO_PAT) |

## Log

- 20260707T114721Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260707T115731Z LEG L2 closed: safe-apply (HALTGT, targeted) Apply complete 9 added/0 changed/0 destroyed: stitch_source_gha+policy, stitch_produce_cod
- 20260707T132725Z LEG L1 closed: stitch-produce.tf + stitch-source-push.yml pushed origin/CLOUD @ 684c38511 (git merge-base --is-ancestor confirmed)
- 20260707T132726Z LEG L3 closed: s3://opal-313476888478-globgrph/stitch-source/source.zip present (156994678 bytes, 2026-07-07 09:08:30) -- GHA stitch-so
- 20260707T133840Z **CORRECTION to L3 close (proof was presence-only, not content-valid):** manually
  triggered `opal-stitch-produce` CodeBuild (build #2, post-extractor-fix) to close L4 in-window.
  Extractor ENAMETOOLONG bug (75d93eaf7) confirmed fixed -- derive_stitch.py ran past that point cleanly.
  But GRAIN-SENTINEL FAILED: REACT_QUERY_KEY 0 vs baseline 32, PORTAL_COMPONENT 0 vs baseline 27,
  API_ROUTE 77 vs baseline 263 (0.29x). ROOT CAUSE (source-grounded): downloaded + inspected the live
  stitch-source/source.zip directly -- 0 entries under `portal/src` (org/modules=366, infra/aws=6791,
  .tools=160 all present). GHA run log (28868558323 line 46) confirms `submodules: false` on the
  actions/checkout@v4 step; `portal` is a bare gitlink (mode 160000, `git ls-files -s portal`) with NO
  `.gitmodules` entry (grep .gitmodules = no match) -- it isn't a real registered submodule at all, so
  `actions/checkout submodules:true` would not fix it either. `zip -r ... portal/src` silently zips
  nothing (other paths succeed so `set -e` never trips). Fix needs a second explicit checkout step
  pulling `Opal-Capital/portal` (separate repo) into `portal/` at the pinned gitlink SHA or DEV ref --
  routed to COO/BASE_EXEC (`.github/**` = BASE_EXEC lane per `.owned-paths.yaml:1415`, same pattern as
  the original workflow landing e32896edd). L3's "source.zip present" proof is TRUE but content-invalid
  -- L4 (the actual content-validity gate) correctly caught it and stays OPEN. Window still open
  (opened 11:47Z, red 15:47Z).
- 20260707T141500Z **L4 code fix LANDED (COO, 4074fdf5a) -- now blocked on a genuine external gate.**
  COO landed the portal cross-repo checkout fix directly (BASE_EXEC lane, MSTR-directed). Independently
  verified (not self-report): `git show 4074fdf5a` matches the described diff exactly; `gh secret list`
  confirms only `GHA_ROLE_ARN` exists, no `secrets.PORTAL_REPO_PAT` -- Opal-Capital/portal is a PRIVATE
  repo the default GITHUB_TOKEN cannot read, so the new checkout step will fail until that PAT is
  provisioned (GitHub org-secret admin action, Andrew-only). COO surfacing to Andrew directly. Per COO
  instruction, holding re-trigger until the secret lands (a retrigger now would just fail at the new
  step with no new information). This is a hard external gate (CLAUDE.md Agent Autonomy exception) --
  window may go RED at 15:47Z waiting on Andrew/org-admin action; not a stranded/silent block, already
  escalated loud.
- 20260707T160700Z **Window expired as anticipated (RED at 15:47Z, `deploy_ledger.py check --red` now
  reports PAST-WINDOW).** State unchanged since 14:15Z entry -- still blocked solely on `secrets.PORTAL_REPO_PAT`
  provisioning, no COO-resolvable lever remains (code fix landed + verified, re-trigger held correctly to
  avoid a no-information failed run). Re-escalating the ask to Andrew directly in-session rather than
  re-attesting the same unchanged gate. Non-catastrophic overrun: L1-L3 are genuinely closed+proven, only
  L4 (a nightly artifact refresh, not a served/client-facing surface) is pending -- no live risk from the
  overrun itself, this is a deploy-ledger SLA miss on a low-stakes artifact, not a half-landed production
  change.
- 20260708T1545Z **FORMALLY PARKED (COO-directed disposition, 154000Z).** Status -> RESOLVED-PARKED,
  external_gate=secrets.PORTAL_REPO_PAT (Andrew-only GitHub org-secret; still not provisioned). L1-L3
  infra genuinely landed+proven; L4 first-produce-verify cannot run until the PAT clears (a GHA checkout
  of the PRIVATE Opal-Capital/portal repo). No agent/CVO lever remains -- code fix 4074fdf5a landed+verified;
  a re-trigger now fails at the checkout with no new info. Sentinel removed so `check --red` stops the
  RED-strand alert (dispositioned + escalated, not silent). RESUMPTION: when Andrew provisions
  PORTAL_REPO_PAT, re-trigger opal-stitch-produce CodeBuild + open a FRESH ledger. COO + Andrew notified. -- 0.7.0_AE_CloudOps
