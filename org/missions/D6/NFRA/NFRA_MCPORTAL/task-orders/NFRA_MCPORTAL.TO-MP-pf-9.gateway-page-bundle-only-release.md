# NFRA_MCPORTAL task order -- `MP-pf-9` -- WORKSTREAM PF ROUND 6: the bundle-only release -- the Gateway page that does not scroll sideways at 390 px goes live

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-9</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-9</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a release; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the release moves a static dashboard bundle only.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2's control is the old live bundle (index.html a0ee33db...), which the same read must NOT match.
EGRESS CLASS, declared: S3 artifact upload + SSM pull and restart of opal-gateway on i-07dccb1615503ac99, by safe-ec2-deploy.
</preflight>

## 1. THE CELL -- `MP-pf-9` (workstream PF round 6, decomposition section PF6.1)

**Two stages, two messages from the issuer.** STAGE 1 starts at the issuer's first message (the GO-PREP): steps 1, 2 and 3 are read-only or commit-only, so you do them then (the release tree, the census, the ASK, the rollback proof) and wait for the two halves. STAGE 2 is step 4, the act, and starts only at the issuer's second message (the GO), which names the mcportal commit and comes when G-REL9 holds:
- the never-widen pair is signed against YOUR release ASK (step 2);
- the gateway queue is free: no `opal-gateway` release is open in `deploy_ledger.py list` (one release in flight at a time; the MX-r-15 catalog applies are ahead of you when open).

**What this release is.** ONE swap of the dashboard bundle. The Gateway page at mcportal `c66ca82952` fixes the page scrolling sideways at 390 px on real data (row Z-S64): an index list that holds an unbroken ~65-character name now scrolls inside its own box. No gateway code moves: the census (step 1) must be EMPTY.

**Your worktree.** Cut it from `box/sitez` HEAD. If you go sparse, use a NO-CONE pattern list and pass it on STDIN (`git sparse-checkout set --no-cone --stdin`), never as argv, because Git Bash rewrites `/`-leading argv into `C:/Program Files/Git/...` and the cone silently comes up empty (row Z-S44). The list:
- `/.tools/ /org/ /lib/ /infra/logic/ /infra/aws/terraform/ /infra/aws/lambda/ci/ /infra/aws/lambda/mcportal/ /infra/aws/ec2/ /data/transcripts/scripts/teams/`;
- the 12 root-level tracked blobs: `.gitattributes .gitignore .gitmodules .mcp.json .owned-paths.yaml AGENTS.md CLAUDE.md README.md ajb.ps1 comp-constants.config.yaml pytest.ini requirements.txt`.
A full checkout also works. The gateway on `i-07dccb1615503ac99` runs the commit recorded as `services.opal-gateway.deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` (1bc2df0b13 when this order was cut): read it there at the act; never assume it.

In order:
1. **The release tree.** `git worktree add -b rel-nfra-mcportal-pf <path> <live deployed_commit>`. Change ONE thing: `EC2_MANIFEST.json` `services.opal-gateway.mcportal_commit` becomes `c66ca82952c01575968d16cc736cdabe36606572` (it reads `090b9cdc85...` today). Commit it.
   - **Census:** `git diff --stat <live> HEAD` names ONLY `infra/aws/ec2/EC2_MANIFEST.json`, and `git diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway` names NOTHING. Anything else STOPS with a BLOCKING row.
   - **Resolve, do not deploy:** `MCPORTAL_RESOLVE_ONLY=1 bash infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` from the release tree prints `MCPORTAL-RESOLVED: <dir> @c66ca82952...`. Any other commit, or an error, STOPS.
   - **Tests:** run `tests/test_admin*.py tests/test_owner_gate.py` on the release tree: 0 failed, except a test whose failure is `FileNotFoundError` on a repo path outside `infra/aws/ec2/opal-gateway/` whose `git ls-tree` reads 0 at the live base and 1 at HEAD, and which passes at HEAD (a release tree's `org/` is frozen at the chain's vintage, row Z-S45); list each in the ASK. Any other failure STOPS.
   - Run `ops/bun_cache_precheck.py bun.lock` against the c66ca82952 lockfile. A miss STOPS: no package is fetched.
2. **The ASK and the pair.** Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~Z/NEVER_WIDEN_ASK_MP-pf-9.md` with: the blast radius (the dashboard bundle's `index.html` and two assets swap; `routes.json` is unchanged; no gateway code, no tool added or removed); what it may never touch (the MCP tool surface, IAM, any store write); the census, the tests and the rollback (step 3); the read-backs AC1 and AC2.
   Commit it, then send ONE message to BOTH `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~MP` naming the ASK path and commit and asking each for its half. WAIT for both halves at HEAD of `box/sitez` (`deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MP-pf-9_<date>.md`, `deliverables/2.0.0_SA_COO~MP/NEVER_WIDEN_HALF_COO_MP-pf-9_<date>.md`), each citing your ASK by path. A refused half STOPS the act.
3. **Rollback, proven before the act.** The live bundle is the build of mcportal `090b9cdc85`: rebuild it from a clean detached worktree WITHOUT uploading and compare `index.html`, `routes.json`, `assets/index-pbBdUBWu.css` and `assets/index-DzjZpju-.js` by sha256 with the host's `dashboard/` (read-only over SSM); the issuer's own read at ~12:2xZ found all four equal (index.html a0ee33db..., routes e6d4a9ac..., css cd4abedd..., js 52466cff...). Negative control: the same members of the c66ca82952 build differ in `index.html` and the CSS. Name the command that re-deploys the previous pin (the manifest edit back to `090b9cdc85` and the same deploy). Record the seconds of the release's own pull-and-restart in step 4 as the rollback bound. If the rollback cannot be shown: STOP, no deploy, a BLOCKING row.
4. **NEVER-2 ledger, on your branch, in this order.**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-pf-bundle-release`. Legs: bundle build, release build and upload, SSM pull and restart, manifest record. Write the census, the test results and this order's path to `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~Z/MP-pf-9_PRE_ACT_RECORD.md` and put ONE pointer line to it in the entry.
   - Commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-pf-bundle-release.json`.
   - ACT from the release tree with ITS scripts: `bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`. Its stale-base guard must read the live ref unchanged at both reads. If another release has opened since the GO, STOP and say so.
   - Immediately after the restart, poll `/health`. If it is not 200 within 90 seconds, run the named rollback AT ONCE, close the entry as rolled back, and stop.
   - The MCP tool surface does not move. Before and after the act, list the registered tool names on the host and record the two counts and their difference, which must be empty.
   - **Record the release on your branch:** in `EC2_MANIFEST.json`, `services.opal-gateway` gets the release commit as `deployed_commit`, the previous one as `previous_deployed_commit`, `mcportal_commit` stays `c66ca82952...`, and a `release_note`. The wrapper writes a stale `previous_deployed_commit` from the tree's own vintage; correct it.
   - Close every leg with its proof, and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway code, no IAM, no Terraform, no store write. The release commit changes `EC2_MANIFEST.json` only.
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report.
3. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion; the check scripts and the proof lines are the issuer's.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/*nfra-mcportal-pf-bundle-release*
org/critical_paths/.open_deploys/nfra-mcportal-pf-bundle-release.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~Z/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, every gateway file, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the close commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pf-9"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf9.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD=[1-9].*sentinel=no; listed OPEN/HELD=0.*is c66ca82952: yes; descends from 090b9cdc85: yes.*gateway files changed between them=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pf-9"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf9.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; no-identity / =40[13] /gateway=40[13].*host bundle == build of c66ca82952: yes; index.html names exactly the two assets: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~Z/NFRA_MCPORTAL.TO-MP-pf-9.gateway-page-bundle-only-release.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with:
- the census;
- the before/after tool counts;
- the two check outputs;
- the rollback time, and how it was measured;
- the ledger entry path and its CLOSED state;
- the release commit and the mcportal commit;
- every commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the PF round-6 issuance (decomposition v16) on the CTO's ruling msg 34980 (b). The MP-pc-5 shape with every lesson baked in (the sparse list on stdin, the release-tree test rule, `infra/logic/registry`), minus the gateway cherry-picks and the route hookup: this release moves one manifest pin. The SSM read at ~12:2xZ (a local build of the deployed 090b9cdc85 equals the host's dashboard byte for byte on all four members) is what makes AC2 a comparison of deployed bytes with build input.
Checks dry-run at the base (run from /c/Users): pf9.AC1 FAIL as expected (no entry; mcportal_commit 090b9cdc85ce; descends yes); pf9.AC2 FAIL as expected (SSM 668450e9 Success: /health 200, no-identity / and /gateway 401, host index.html a0ee33db3f2e against the expected 5a6e2eeef8ec; the new assets absent).
The graded read at 390 and 1280 px is the issuer's real run after the release (the served body, rendered through the deployed CSS, measured), not a criterion here. ~O's round-38 release then carries the same pin with no delta (CTO). Gate G-REL9, holder the issuer.

<status>staged</status>
<round>6</round>
<workstream>PF</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
