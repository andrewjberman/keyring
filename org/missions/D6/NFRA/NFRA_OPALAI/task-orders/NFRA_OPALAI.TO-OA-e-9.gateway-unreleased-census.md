# NFRA_OPALAI task order -- `OA-e-9` -- ROUND 2, E9's first cell: the census of what CLOUD holds unreleased on the gateway

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~10</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot census; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- one SSM md5 read on the existing host; nothing is written to AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- a read-only census; AC2 is an independent recount of it.
EGRESS CLASS, declared: AWS READ on Opal's own plane (SSM md5 reads). No vendor call.
</preflight>

## 1. THE CELL -- `OA-e-9` (round 2, decomposition section R2.1)

E9 moves the gateway into `opal_ai` (FWD-5, FWD-11). The move ships from ONE release base (CTO ruling @75117e60d6):
the commit the host actually serves. Before anything moves, the project needs to know every commit CLOUD holds on the
gateway paths that the served commit does not. This cell MEASURES that and changes nothing. The move is cut from what it
finds.

In order:
1. **BASE, by content.** Over SSM, read the md5 of `/opt/opal-gateway/app/identity_scope.py`, `app/data_entitlement.py`,
   `app/asker_scope.py`, `app/tools.py`, `app/server.py` and `/opt/opal-gateway/identity_tool_allowlist.txt`.
   - Compare each with `git show <candidate>:infra/aws/ec2/opal-gateway/<file> | md5sum`, for the release commits on
     `rel-nfra-opalai-r2-asker-switch-on-gateway`, `rel-nfra-opalai-r2-asker-binding-gateway`, any other `rel-*`
     branch, and `6a98a0553a` (served at the round-2 cut; see the tie-break).
   - **TIE-BREAK (AMENDED, row NFRA_OPALAI-Z-S38):** app files cannot tell a release from its ancestor when only the
     deploy template differs. At the round-2 cut the host served `6a98a0553a` (OG-s-1), not its ancestor `fe94911257`,
     whose app files are byte-identical; only `deploy-to-ec2.sh` differs (measured by `2.0.0_SA_COO~O` @e992df46c4). So
     ALSO read the live `/opt/opal-gateway/.env` KEY NAMES (never values) over SSM, and keep only candidates whose
     `deploy-to-ec2.sh` `.env` template writes exactly that key set (e.g. `SPRINT_VIEW_ALLOWED_EMAILS`). If more than one
     candidate survives, the base is the one whose md5 MATCHES the live host on EVERY file where the survivors DIFFER
     (AMENDMENT 2: never the newest by default; rows Z-W10-S3, OA-e-3's resolution), cross-checked by the host's served
     gateway tree; name every survivor and the differing-file md5s in your report.
   - BASE is the commit whose six files ALL match. Record `LIVE-MATCH: yes`. If none matches, record `LIVE-MATCH: no`,
     file a BLOCKING row, and stop.
2. **HEAD** = the CLOUD commit your worktree sits on when you count.
3. **The population:** `git rev-list --no-merges <BASE>..<HEAD> -- infra/aws/ec2/opal-gateway`. Its count is the
   DENOMINATOR.
4. **One row per commit**, classed exactly one of three ways:
   - `released-elsewhere`: its gateway change is ALREADY on the host. BASE is on a release branch, so a commit
     cherry-picked into a release reads here. Show it by the content of the files it touches at BASE.
   - `unreleased`: its change is not on the host.
   - `superseded`: a later commit in the population replaces or reverts it. Name that commit.
   The owning project is read from the commit subject (for example `NFRA_OPALAI`, `NFRA_MCPINDEX`, `MDPF_TAXSMA`). A
   commit that names none is `UNATTRIBUTED_GW`.

Write `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/E9_GATEWAY_UNRELEASED_CENSUS.md` with
these lines, each at the start of its own line:
```
BASE: <full or 10+ hex sha>
HEAD: <full or 10+ hex sha>
LIVE-MATCH: yes
DENOMINATOR: <n>
```
Then a markdown table. Its data rows are EXACTLY `| <10-hex sha> | <PROJECT_CODE> <order id or -> | <class> | <files> |`,
one per commit. Under the table, give a short summary: counts per class and per project, and the unreleased commits a
move from BASE would carry. Commit the file.

## 2. BOUNDS

1. Read-only. No release, no deploy, no edit of any gateway file, no branch deletion.
2. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/ec2/opal-gateway/`, `infra/aws/ec2/EC2_MANIFEST.json`,
`org/critical_paths/change_management/`.
Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W10-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the census is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-9"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e9.AC1.sh; echo "exit=$?"</invocation><expect>base, head and denominator named; rows = classed = with-project = denominator -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-9"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e9.AC2.sh; echo "exit=$?"</invocation><expect>recount = denominator; live-match=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/NFRA_OPALAI.TO-OA-e-9.gateway-unreleased-census.proof_of_spec.json`.
Report once: BASE and how it was matched, the denominator, the per-class counts, the census path and commit, any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E9's FIRST cell only, as the analysis words it. The move is cut from this census.

SPAWN ONLY WHEN (continue slot `~10`): OA-e-3 has drained. The census then reads against the release that switched the
Analyst on.

Dry-run at base (CLOUD `c8df03c408`, ~20:5xZ):
- e9.AC1 base: FAIL as expected (census not committed).
- e9.AC2 base: FAIL as expected (census not committed).

**AMENDMENT (2.0.0_SA_COO~AI, issuer licence, ~22:1xZ):** The served base at the cut is `6a98a0553a`, not `fe94911257`, and the base resolution gains the .env key-set tie-break
(row Z-S38). No criterion's expectation moves. Gate limb: to-pipeline-gate grades a MODIFIED order only on GATE (viii)
placeholders (NONE), so no limb graded this amendment.

**AMENDMENT 2 (2.0.0_SA_COO~AI, ~03:1xZ):** the tie-break no longer takes the newest survivor, which twice named a commit
the host was not running (rows Z-W10-S3; OA-e-3's resolution). The base is the survivor that matches the live md5 on every
differing file. Gate limb: none (GATE (viii) placeholders NONE).

<status>complete</status>
<round>2</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
