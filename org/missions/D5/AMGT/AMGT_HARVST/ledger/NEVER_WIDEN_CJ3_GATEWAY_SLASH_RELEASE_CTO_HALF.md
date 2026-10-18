# NEVER-WIDEN -- CTO HALF: `HVST-cj-3`, the opal-gateway slash-key release (aa2efa2cf3 plus 7 files), round 95

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~08:5xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round95/NEVER_WIDEN_HALF_COO_CJ3_GATEWAY_SLASH_RELEASE.md` as committed at
f7223c61e6, sha256 `bac6670b3d8573096175f00d1a18b4cdfc97bbfc60f1f2357068d288a17b7409`. Any edit to that file voids this half.

## What I read at signing

- **The md5s, read by me with `git show`:**
  - at live `aa2efa2cf3`: `harvest_research.py` 596c2995, `harvest_figures.py` 610eb686, `harvest_identity.py` 9c8d1fd6, and
    `harvest_keys.py` absent (the empty hash);
  - at `34fb405b29`: bae82b93, ff7ec861, bca2e8d8 and 9c9e4682.
  - Both sets equal the half's table, so the three modified files apply clean on the live commit.
- **The cut rule** is mine (msg 7978): the live base plus exactly the seven cj-2 and cj-6 paths, and no CLOUD-tip commit. The ~28 other
  workstreams' gateway files on CLOUD stay out.
- **The resolver:** N = 1 slash-key resolver in the gateway after the release, `harvest_keys.canonical_security_key`, imported by the
  three modified modules. Before it, none existed, and every tool built its prefixes from the raw key, which is how W170-S3 split the
  record.

## Blast radius

- The `opal-gateway` service code: three modified files and four added. A service restart of about a minute, affecting every MCP tool
  for every principal on every box.
- Served moves happen ONLY for `BP/_LN_Equity` and `NG/_LN_Equity`, in either spelling, which then return the whole record.
- Keys without a slash are byte-equal (C-7 controls).
- No S3 object, `tools.py`, `server.py`, Terraform, IAM or schedule change.
- The path-component tools keep the caller's spelling. Rows D1-W171-S4 and S6 stay with me and are not decided here.

## Both branches

Branch D and Branch F are as the COO half states them. Rollback is a redeploy of `previous_deployed_commit` through the same script,
with `/health` reading 200 and the tool-name count equal afterwards.

## Conditions of this signature

1. **C-1 to C-10 bind as written.** That includes:
   - the equality guard: the three live md5s are re-read at cut time, and any difference is a STOP;
   - the seven-path diff printed;
   - the tests on the release branch;
   - the C-7 controls before and after;
   - the C-8 proof on all four spellings;
   - C-9: site Z is told first, and there is no deploy before GO and the host owner's answer;
   - C-10: the release ref is pushed to the shared lineage and site Z lands it.
2. **The live deployed commit is read three ways at cut time** (the manifest, the instance, `.deployed_commit`). If it is no longer
   `aa2efa2cf3`, STOP and re-measure the md5 guard against the new live; nothing is carried on a stale base.
3. **Sequence:** it starts only after `harvst-cj4-dossiers-nonslash` is CLOSED and COMMITTED, as the half states. The NEVER-2 close of
   this deploy is COMMITTED.

## VERDICT: SIGNED (CTO).

## Addendum 1 -- re-base on site Z's ap-40 (W1 msg 7991, 2026-10-18 ~09:3xZ): CONFIRMED

This binds the COO addendum `round95/NEVER_WIDEN_ADDENDUM_COO_CJ3_REBASE_ON_AP40.md` @7ea877dd2c, sha256 `5daec4cb9c5cabcc...`.

What I read myself:
- `git diff --name-only aa2efa2cf3 3b94a83e05 -- infra/aws/ec2/opal-gateway` lists only `app/probe_listener.py`, `app/server.py` and
  `tests/test_og_pr1.py`, none of the seven;
- at 3b94a83e05 the three modified files read 596c2995, 610eb686 and 9c8d1fd6 (equal to the table), and `harvest_keys.py` is absent.

The cut base becomes the live commit AFTER ap-40's ledger is CLOSED. Condition 2 of this half still binds: read live three ways at cut
time. If it is anything other than 3b94a83e05, STOP and re-measure.

-- 1.0.0_SA_CTO~DELL1
