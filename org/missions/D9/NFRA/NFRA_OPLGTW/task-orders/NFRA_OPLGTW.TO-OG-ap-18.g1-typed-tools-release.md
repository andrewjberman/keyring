# NFRA_OPLGTW task order -- `OG-ap-18` -- APPLY: the ten G1 typed harvest tools' gateway release on the live ref after OG-hv-2 (FWD-22)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-18</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-18</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-18` (decomposition addendum R3-T.50, workstream G1-TYPED, FWD-22)

APPLY: the G1 typed tools' release (builds OG-gt-0 to OG-gt-4, hookups by the issuer) on the live ref `OG-hv-2` leaves, then the served read of all ten.

APPLY: release the ten G1 typed harvest tools (builds `OG-gt-0` to `OG-gt-4`, merged by the issuer with the one hookup commit) on the
live ref that `OG-hv-2`'s release leaves. These tools add NO reach: they read `s3://opal-data-harvest` through the grant and
the Opal-only admission that `OG-hv-2` already put live; each is a READ tool, SAFE, `legacy` class. `harvest_get_published_analysis`
(`OG-gt-5`) is NOT in this release: it rides its own ask.

The ten: `harvest_resolve_security`, `harvest_security_coverage`, `harvest_get_chatter`, `harvest_search_articles`, `harvest_get_article`, `harvest_get_fundamentals`, `harvest_query_columns`, `harvest_get_research`, `harvest_get_filing_analysis`, `harvest_get_peers_and_scores`.

### PHASE A (when `OG-hv-2`'s ledger `nfra-oplgtw-gateway-release-hv` is CLOSED AND the issuer's amendment A1 to this order names the merge and hookup commits): re-cut, ask. NO deploy

1. **Live ref.** Read `services.opal-gateway.deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` at HEAD, then one SSM md5 read of
   the host against it, walking `app/`, `deploy/` and `dashboard/`. A mismatch is a STOP and a BLOCKING row.
2. **Re-cut** in a worktree `C:/tmp/og-rel-gt`, new branch `rel-nfra-oplgtw-gt`, at that live ref. Take ONLY the files A1 names, from
   the commits A1 names: new `app/harvest_typed.py`, `app/harvest_identity.py`, `app/harvest_press.py`, `app/harvest_figures.py`,
   `app/harvest_research.py` and their five tests whole; `app/tools.py`, `app/destructive_ops.py`, `app/data_entitlement.py`,
   `tests/test_entitlement_admin.py` and `tests/test_data_entitlement_family.py` BY HUNK (the ten registrations, the ten names in
   `SAFE_TOOLS` and in `NATIVE_TOOLS`, the two re-pinned counts), 3-way where the base differs. Never a whole file from trunk for
   those five. Commit with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only. Write
   `W/gt_release.json` = `{"base_sha", "release_sha"}` (FULL 40-character shas). Run in the release tree: `tests/test_og_gt0.py`
   to `test_og_gt4.py`, `tests/test_og_hv1.py`, `tests/test_entitlement_admin.py` and `tests/test_data_entitlement_family.py`.
3. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-18.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`). It carries,
   each under a heading containing its word: (1) the `diff` by file; (2) the ten `tools`, their class and their `refused` arms;
   (3) the `widening`, stated plainly: no new bucket reach and no IAM change; ten more read tools over what `harvest_read` already
   reaches, for Opal principals only, with the data they now make easy to read named (research, filings, chatter, Bloomberg
   bronze tables read from the bucket, no vendor call); (4) the `order` of acts and that no grant is part of it; (5) `both branches`
   of a call (refused: zero S3 calls; admitted: reads capped and projected to 50 KB); (6) the `rollback` (redeploy the base);
   (7) the `triggers` (`/health`, the registry count +10, `.env` names unchanged, md5 = release). Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

4. Ledger `nfra-oplgtw-gateway-release-gt`, entry AND sentinel first. Deploy from `C:/tmp/og-rel-gt` through
   `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<base_sha>`; the deploy tree's `git rev-parse HEAD` must equal the
   signed `release_sha` in full and its parent must equal live `deployed_commit` at the act (a mismatch is a STOP; print both).
   The release cone carries `lib/`, `.tools/`, `org/modules/graph/`, `data/transcripts/scripts/teams/` AND your agent home. No
   `HALT_OVERRIDE`. Read back immediately against the triggers; on any trigger redeploy the base and file an ARMED row naming
   `2.0.0_SA_COO~O`.
5. **The served read**, through the INSTALLED code on the host, one SSM call writing `W/GT_SERVED.json` = `{"body": {"tools_listed":
   [...], "registry_before": N, "registry_count": N+10, "per_tool": {"<tool>": {"opal_served": true, "non_opal_refused": true,
   "s3_calls_on_refusal": 0}, ...}}}` for all ten tools: an Opal stand-in principal's real call returns an enveloped answer
   (`as_of`, `source_keys`, `denominator`, `absent_reason`), a non-Opal principal is refused `harvest_opal_only` with zero S3
   calls. `registry_before` is the registry count read BEFORE the deploy. No object content is printed.
6. **Standing release clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and `file_checksums` come
   from the release blobs. Close the ledger, commit, run AC2, and report once to `2.0.0_SA_COO~O`.

## 2. BOUNDS

- The release's files only. No IAM or Terraform change, no catalog edit, no `.env` change, no object written to any bucket.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform`; print an
  `.env` value, a person's name or email, or harvest object content; override a gate other than the one audited lane escape in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-gt.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-18"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap18.AC1.sh; echo "exit=$?"</invocation><expect>(?s)base [0-9a-f]+ is the live ref before this release: yes.*outside the G1 set 0 \(want 0\); tools registered 10 of 10; SAFE 10 of 10; NATIVE 10 of 10; OG-gt-5 module in release: no.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-18"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap18.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*landed=(?:current; rb\.AC2 PASS|superseded; rb\.AC2 skipped \(superseded\)).*registry [0-9]+ -> [0-9]+ \(\+10\); per-tool 10 of 10; tools listed yes; trading-day lag numeric yes; host calendar md5 equal yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-18" judgment="true"/>
</proof_of_spec>

- `AC1`: the re-cut carries exactly the G1 build and its hookups on the live ref, with ten registrations.
- `AC2`: the deploy landed and closed, and the installed code serves all ten tools to an Opal principal and refuses a non-Opal one.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`): the first typed answers read as a research user would want them (the newest-part counts, `data_status` on a quiet name, `not_held` for a CUSIP). Graded on a real call; never simulated here.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-18.g1-typed-tools-release.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.50 @d9371ffe81; PRD v3.0 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- The release this cell rides: `NFRA_OPLGTW.TO-OG-ap-18`; its grant is `NFRA_OPLGTW.TO-OG-hv-2` (A5).
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Pre-cut: ap18.AC1 and ap18.AC2 base FAIL as expected (gt_release.json and GT_SERVED.json absent).
- Cut staged: amendment A1 (the merge and hookup commits) and the spawn of this order wait on OG-hv-2's close and on gt-0..gt-4's drain.

- A1 (issuer, 2026-10-14 ~17:1xZ, row Z-S119): the release AC2 now grades the LANDING with a time anchor (`r37/checks/_landed.sh`): the manifest's deployed_commit is the release, or recorded it
  before a later release displaced it; runbook 7.2 (rb.AC2) is graded only while this release is the live one. "deployed_commit equals release_sha" flips to FAIL on work graded PASS the
  moment the next release lands, so it is no longer a criterion. Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A2 (issuer, 2026-10-14 ~18:3xZ): **PHASE A MAY START.** Preconditions met: OG-hv-2 CLOSED (live was 7c558b4e21, now bacec95ccd after MP-pc-5); the five G1 build cells and the hookup cell are merged on box/sitez: OG-gt-0 `077a46f5e1`
  (worker commit `4a707ab5f9`), OG-gt-1 `c053092447` (`ca2db2d5c9`), OG-gt-2 `7c0197d9c2` (`b47578c367`), OG-gt-3 `f4a65ac665` (`d79e6dda9a` + `a08c86df77`), OG-gt-4 `ca23de384a` (`dc1139265a`), the hookup OG-gt-7 `705e6f7406`
  (`0cda8e2505`). Take the five module files and the five test files WHOLE from `box/sitez` HEAD (`app/harvest_typed.py`, `harvest_identity.py`, `harvest_press.py`, `harvest_figures.py`, `harvest_research.py`; `tests/test_og_gt0.py` to
  `test_og_gt4.py`); take the five hookup files BY HUNK from `0cda8e2505` (only the hunks that name the ten G1 tools and the two pins 65 -> 75 and 56 -> 66) on the live base `bacec95ccd`. `app/typed_scope.py`, `app/harvest_published.py` and
  `tests/test_og_gt5.py`/`gt6.py` are NOT in this release (ap18.AC1 refuses them). Known reads before you ask: the commit-time naming gate passed every module; `lib/trading_calendar.py` is imported by the tools: confirm in the served
  read that it reaches the installed code (rows Z-W72-S2, Z-W79-S3 say the deploy ships app code and the calendar may fall back); `harvest_search_articles` reads one silver partition of about 110 MB for its sentiment join and took 65-97 s
  in its live probe: record the served latency in the ask. The order may be cut beside OG-ap-17's Phase A; the first fully signed one deploys and the other re-cuts on the new live ref. Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A3 (issuer, 2026-10-14 ~19:5xZ): ALL THREE HALVES SIGNED at `4275edccad` (CTO `7a485c883a`, COO `9a6a7eed58`, CVO `85ddb61584`). **PHASE B GO.** The CVO's condition replaces my 120 s STOP for `harvest_search_articles`: the live ALB `opal-gateway` has an
  idle timeout of 60 s, so Phase B reads that tool THROUGH THE PUBLIC ENDPOINT (`mcp.opalinvest.dev`) as well as on the host; a 502 or 504, or a call over 60 s, pulls ONLY that tool, with an ARMED row naming this seat (the release stays). Owed after this
  release, both Friday work: `OG-gt-8` (the trading calendar staged into the artifact) and `OG-gt-9` (the sentiment join reads only silver partitions inside the asked date window). Because ap-18 deploys first, `OG-ap-17` re-cuts on the new live ref.
  Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A4 (issuer, 2026-10-14 ~21:5xZ): **THE A3 GO IS WITHDRAWN; the release is RE-CUT.** The release `4275edccad` cannot start on the host: `app/harvest_identity.py:86` indexes `Path(__file__).parents[5]`,
  and `/opt/opal-gateway/app/<m>.py` has 4 parents, so the import raises IndexError (measured; confirmed by `~Z`, row Z-S126, msg 34210; nothing was deployed, the ledger was never opened). The signed halves do NOT carry
  to the new `release_sha` (C3 of both): all three re-sign. PHASE A re-opens at the live ref `bacec95ccd` (read it again; it moves if `OG-ap-17`, MX-r-13 or a `~MP` release lands first). Take, besides the A1/A2 set:
  - `OG-gt-8` (merged `43e5e0383e`, worker commit `d21927a248`): `app/harvest_identity.py` whole at that merge (the safe calendar root) and `deploy-to-ec2.sh` BY HUNK (the `lib/trading_calendar.py` staging and `lib` in the tar), and `tests/test_og_gt8.py`.
    `app/news_typed.py` is NOT in this release (it rides `OG-ap-19`); take the `harvest_identity.py` hunk only. The ask names `lib/` as a NEW artifact member and says so under `diff`.
  - `OG-gt-9` (merge commit named in A5 once it lands): `app/harvest_press.py` and `tests/test_og_gt9.py` whole at that merge.
  - The host-shaped import check is a Phase A trigger: copy the release tree's `app/` to a 4-parent path with `lib/trading_calendar.py` beside it, import all five G1 modules and `app.tools` in a fresh interpreter, and record the result in the ask (the A2 evidence was "imports cleanly in the release tree", which is a property of a module AT A DEPTH).
  - Phase B adds, after deploy: the md5 read-back of `lib/trading_calendar.py` on the host, and the served `harvest_resolve_security`/`harvest_security_coverage` answers carry `trading_days_behind_t1` (a number, not the absent reason): this CLOSES row Z-S125.
  The CVO's condition from A3 stands: `harvest_search_articles` is read through `mcp.opalinvest.dev` (ALB idle timeout 60 s); a 502/504 or a call over 60 s pulls only that tool. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>G1-TYPED</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
