# NFRA_OPLGTW task order -- `OG-bi-1` -- the gateway deploy's dashboard install fails on a cache miss and never fetches (row Z-W28-S24)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-bi-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~33</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a build-script change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's ruling (1.0.0_SA_CTO~Z msg 31231) on row NFRA_OPLGTW-Z-W28-S24.
EGRESS CLASS, declared: NONE. This cell exists to remove an egress; it makes no network request of any kind.
</preflight>

## 1. THE CELL -- `OG-bi-1` (decomposition addendum R3-T.23)

`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` line 206 builds Andrew's dashboard bundle on every gateway deploy:
`( cd "$MCPORTAL_DIR" && bun install --frozen-lockfile && bun run build )`. When the lockfile names a package version
that bun's install cache does not hold, that line fetches it from the public registry. Andrew's word of 2026-10-07 is
that no package, script or program is fetched from the internet on any box. On 2026-10-07 both deploys were served
from the cache (0 of 6,441 cache entries touched;
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/S24_BUN_INSTALL_SOURCE_READ_20261007.md`), so nothing
was fetched, but nothing stops the next one.

Make the install step FAIL on a cache miss and never fetch.

Do:
1. **Choose the mechanism and name it in `W/BI1_MECHANISM.md`.** Read `bun install --help` and `bun --version` (both
   local; neither opens a socket). Either:
   - (a) an installer mode of THIS bun version that refuses the network outright; or
   - (b) a pre-check, run before the install, that every package entry of the lockfile is present in bun's install
     cache, exiting non-zero with the list of what is missing.
   If (a) exists you still write (b): the pre-check is what produces the missing list, and the tests run it.
   State in the file, for the mode the script ends up using, **whether it can send a metadata request** to the
   registry even when every package is cached, and what you read to know that. If you cannot determine it without a
   network observation, say UNDETERMINED and why. Do not test it by watching the network.
2. **The pre-check** is one small program inside `infra/aws/ec2/opal-gateway/` (name its path in your report). It takes
   the lockfile path and the cache directory, defaults the cache to bun's own default location derived from the
   environment (never a typed user path), prints `<present> of <total>` and the missing `name@version` lines, and exits
   0 only when nothing is missing. It never runs bun and never opens a socket.
3. **In `deploy-to-ec2.sh`**, run the pre-check before the install as ONE guarded sequence: a failed pre-check stops
   the script before `bun install`, prints the missing list under a line starting `ERROR: bun cache miss`, and says the
   list goes to the laptop's package intake. Add the no-network mode of 1 (a) to the install line if it exists. Change
   nothing else in the script.
4. **Tests:** `infra/aws/ec2/opal-gateway/tests/test_deploy_install_no_fetch.py`, the four named tests the header of
   `bi1.AC1.sh` lists. Use a COPY of cache entries in a temp directory for the negative control; never delete or edit
   an entry of the real cache. No test runs `bun install`, `bun run` or any command that can reach the network.
   - The real lockfile: read it from the dashboard repository without checking anything out,
     `git -C "<main repo>/mcportal" show <commit>:<lockfile name>`, where `<commit>` is
     `services.opal-gateway.mcportal_commit` in `infra/aws/ec2/EC2_MANIFEST.json`. If that repository or lockfile is
     not readable from your session, build the tests on a small fixture lockfile you write, and SAY SO.
5. **One real read, recorded in `W/BI1_REAL_READ.md`:** the pre-check against the real lockfile and the real cache,
   read-only. State `<present> of <total>`. If anything is missing today, list it: that is a finding, not a failure of
   this cell.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~33/`.

## 2. BOUNDS

- **Fetch nothing.** No `bun install`, `bun add`, `bun x`, `npm`, `pip`, `curl`, `wget` or any command that can reach
  the internet. `bun --version` and `bun install --help` are allowed. If a step seems to need a package you do not
  have, STOP that step and report it.
- No deploy, no host act, no AWS call. The script is not run end to end.
- Never delete, move or edit anything in bun's real cache.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/ops/
infra/aws/ec2/opal-gateway/tests/test_deploy_install_no_fetch.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~33/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W33-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-bi-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r28/checks/bi1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a full cache passes; one missing entry stops the script before any install; the script cannot install past a
  failed pre-check.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-bi-1.deploy-install-no-fetch.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If the criterion PASSES, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC output; the mechanism and the metadata-request statement; the diff of `deploy-to-ec2.sh`;
   the pre-check's path; the real read's `<present> of <total>`; whether the tests used the real lockfile or a
   fixture; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 28 (R3-T.23), cut on `1.0.0_SA_CTO~Z` msg 31231: the hold on gateway deploys from site Z lifts on this cell.
- The change is to the deploy script, which is not installed on the host; it takes effect at the next deploy cut from
  a tree that carries it. It is a gateway-tree difference, so the next release's set names it as "the deploy tool, not
  shipped".
- If the pre-check lands outside `ops/`, the worker reports it and the issuer amends `<paths>`.
- Pre-cut 17:5xZ: `bi1.AC1` FAIL (the test file is absent).

<status>pending</status>
<round>28</round>
<slot>~33</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
