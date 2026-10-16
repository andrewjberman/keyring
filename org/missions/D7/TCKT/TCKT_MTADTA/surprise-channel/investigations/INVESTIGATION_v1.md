# TCKT_MTADTA -- surprise channel, INVESTIGATION v1 (round 1, dell1 fabric)

**Opened by:** `1.0.0_SA_CTO~DELL1` at L4 (seat rows; the CVO assembles from L8, spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`). The gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`.
**Id grammar:**
- a worker's row is `TCKT_MTADTA-D1-W<n>-S<k>`;
- a seat's row is `TCKT_MTADTA-D1-S<k>` (dell1 coordinate);
- the CVO's adjudication rows live in `../adjudications/`.

**Append-only during the round.** Never edit an existing row.

```json
[
  {
    "id": "TCKT_MTADTA-D1-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "1.0.0_SA_CTO~DELL1",
    "surfaced_at": "2026-10-16T06:38:00Z",
    "one_line": "The safe-commit PRD manifest gate refused PRD v0.2 with 'no top-level ENDPOINT section' when the file's only defect was CRLF line endings, while a direct run of the same gate on the working file passed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "0.0.0_AB_MSTR~DELL1 (infrastructure: .tools/safe-commit.sh and .tools/prd-manifest-gate.py); this seat only surfaces",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit of org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md (v0.2 edit) twice: 'ERROR: BLOCKED -- step-4 PRD surface-manifest gate ... no top-level ENDPOINT section the L6 matcher can resolve'",
        "python .tools/prd-manifest-gate.py <same path>, same minute: '[prd-manifest] OK: 1 step-4 PRD document(s) carry their key surfaces'",
        "byte read of the file: CR count 309 (the v0.1 blob @315f7a19af: 0); after converting to LF the commit landed @86f3caec3a"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A gate refusal names the defect it found, and the same gate gives the same verdict on the same bytes whoever runs it.",
    "world_is": "The refusal named a missing heading that was present. The real defect, CRLF line endings from a Python text-mode write on Windows, was named nowhere. The direct run and the commit-time run disagreed.",
    "notes": "The cause of the disagreement was not read: the commit-time run may see the staged blob and the direct run the working file. The fix belongs to the gate's owner: name CRLF in the refusal, or normalise before matching. Nothing was edited here."
  },
  {
    "id": "TCKT_MTADTA-D1-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-16T06:54:24Z",
    "one_line": "PRD C-POPULATION resolves an event's actor against the eight UPNs AND their Entra object ids read once at collection, but C-APP gives the collector app ONE permission (ActivityFeed.Read) and reading object ids needs a Graph directory permission, so the two rows cannot both hold.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~DELL1 (owns the PRD; the issuer's round-1 ruling is to resolve by the four UPN fields only and leave object_ids empty)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md C-POPULATION (the actor is resolved across UserId, MailboxOwnerUPN, SendAsUserSmtp and SendOnBehalfOfUserSmtp, case-insensitively, against the eight UPNs and their Entra object ids read once at collection)",
        "same file, C-APP (ONE new single-purpose Entra app holds ActivityFeed.Read on the Office 365 Management APIs, app-only; the gateway apps gain no permission)",
        "org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP.md ruling 4 and task order TO-MD-c1 (population.json carries an empty object_ids map in round 1)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The collector reads the eight's Entra object ids once at collection and matches events by id as well as by UPN, with the app holding exactly one permission.",
    "world_is": "Reading a user's object id takes a Graph directory permission (User.Read.All or an equivalent) or the delegated token of a signed-in person; the app as specified holds neither. Audit records carry UPNs in the four named fields, so UPN matching works without it; an id-only record (a UserId that is a GUID) would be dropped as out of population.",
    "notes": "Round 1 builds UPN resolution only. Whether a GUID-only actor occurs in the feed is unread until the first real content lands (release act 4); if it does, the enrichment list takes either a one-time id lookup run by Andrew into population.json or a second permission by the CTO's ruling."
  },
  {
    "id": "TCKT_MTADTA-D1-W2-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~2",
    "surfaced_at": "2026-10-16T07:06:00Z",
    "one_line": "TO-MD-i1 says identity.tf is one of four files in the root infra/aws/terraform/trino/, but that directory is absent at HEAD of the worker branch and no sibling file of it is tracked; the three siblings belong to cells MD-h-1, MD-a-1 and MD-c-1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git ls-files infra/aws/terraform/trino returns no path at worktree HEAD c9971df7ca; the same query on the main checkout lists none either",
        "org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP.md lines 41-49: trino/main.tf (MD-h-1), trino/access.tf (MD-a-1), trino/collector.tf (MD-c-1) and trino/identity.tf (MD-i-1) are the four files of the root, none yet merged",
        "task order TCKT_MTADTA.TO-MD-i1 lines 61 and 89: 'one of four in the root infra/aws/terraform/trino/'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The Terraform root infra/aws/terraform/trino/ already carries its four files when the identity file is written, so the identity file joins an existing root.",
    "world_is": "The root does not exist at HEAD; identity.tf is written as the first file of the directory in this worktree. Its check (r1_check_i1.py tf) passes on that file alone. Nothing was weakened; the three sibling files are not created here.",
    "notes": "The sibling cells land their files at the round-1 drain. Whether the trino root is complete at merge time is for the drain's refuser and the L8 read, not for this cell."
  },
  {
    "id": "TCKT_MTADTA-D1-W2-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~2",
    "surfaced_at": "2026-10-16T07:06:30Z",
    "one_line": "The worker worktree is a sparse checkout that does not materialise org/surprise_channel/, so the row schema org/surprise_channel/schemas/investigation_item.schema.json that the surprise-row gate validates against is absent from the worker's tree although it is tracked at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C /c/tmp/wk-tckt-mtadta-2 config core.sparseCheckout = true; git sparse-checkout list does not include org/surprise_channel",
        "git ls-files org/surprise_channel/schemas lists investigation_item.schema.json and remediation_row.schema.json; ls org/surprise_channel/ in the worktree reports no such directory",
        "the main checkout C:/Dev/ajb_workspace holds the schema on disk"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Every worker tree carries the surprise channel schema on disk, so a worker can validate its own row against it at commit.",
    "world_is": "The schema is not on disk in this worker's worktree. The row written here was not validated against the schema by this worker; the gate is run at commit and its output is recorded in the report.",
    "notes": "Nothing was changed in the sparse-checkout configuration. The fix belongs to the worktree provisioning owner (the sparse cone for worker worktrees)."
  },
  {
    "id": "TCKT_MTADTA-D1-W4-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~4",
    "surfaced_at": "2026-10-16T07:05:03Z",
    "one_line": "Worktree /c/tmp/wk-tckt-mtadta-4 is sparse-checked-out without infra/ and data/, so the TO-MD-s1 write paths (infra/aws/lambda/globgrph-trino-access/ and data/m365_metadata/scripts/) are absent and both acceptance checks refuse as missing files before any code runs.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git sparse-checkout list at worktree /c/tmp/wk-tckt-mtadta-4 (branch wk-TCKT_MTADTA-4) prints 9 cone entries: .tools, infra/logic/registry, lib, org/devices, org/missions/D7/TCKT/TCKT_MTADTA, org/modules/graph, org/ref, org/standards, org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS; neither infra/aws nor data is a cone entry",
        "ls -d infra/aws/lambda and ls data in the worktree: both 'No such file or directory'; git ls-files infra/aws/lambda lists 7434 tracked paths at HEAD, so the tree exists in the repository and not in this checkout",
        "git ls-files data/m365_metadata returns 0 and git ls-files | grep trino-access returns 0 at HEAD: the globgrph-trino-access folder and the m365 scripts folder are new paths of this round, not tracked files left out",
        "r1_check_s1.py silver run at the worktree root under timeout 120: 'SILVER-REFUSED missing C:\\tmp\\wk-tckt-mtadta-4\\infra\\aws\\lambda\\globgrph-trino-access\\silver_builder.py' rc=1; r1_check_s1.py readday: 'READDAY-REFUSED missing C:\\tmp\\wk-tckt-mtadta-4\\data\\m365_metadata\\scripts\\silver\\read_day.py' rc=1"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The worktree carries the paths the task order names (its <paths> grant sits inside a checkout that holds the Lambda's folder and the data scripts folder), so the order is executable as written.",
    "world_is": "The worktree is a sparse checkout whose cone omits infra/aws and data. The worker was not permitted to widen the cone or rebuild the tree to make the order executable, so both silver files are unbuilt and AC1 and AC2 are FAIL (recorded, not weakened).",
    "notes": "Filed under the refusal clause; nothing was created, edited or committed under infra/ or data/. The cone change (git sparse-checkout add infra/aws/lambda data/m365_metadata) is the owner's call: the COO or the integrator decides whether the worktree is reseated. The HEAD of the mission tree is not in question. Round-1 siblings MD-a-1 (globgrph-trino-access handler) would sit in the same folder and meet the same cone."
  },
  {
    "id": "TCKT_MTADTA-D1-W3-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~3",
    "surfaced_at": "2026-10-16T07:06:38Z",
    "one_line": "The worktree is a sparse checkout whose cone excludes data/ and infra/aws/, so the order's granted paths under those roots and the two model files the order says to read are not present and cannot be written or committed.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git sparse-checkout list (worktree /c/tmp/wk-tckt-mtadta-3, HEAD c9971df7ca) = .tools, infra/logic/registry, lib, org/devices, org/missions/D7/TCKT/TCKT_MTADTA, org/modules/graph, org/ref, org/standards, org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS",
        "printf of seven paths (data/m365_metadata/scripts/collector/filter.py, data/m365_metadata/scripts/population.json, infra/aws/lambda/m365-metadata-collector/handler.py, infra/aws/terraform/trino/collector.tf, infra/aws/lambda/transcripts-pull/build.sh, infra/aws/terraform/transcripts/pull.tf, org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md) | git sparse-checkout check-rules: only the investigation file is admitted",
        "ls data -> no such file; ls infra/aws -> no such file; git ls-tree -r --name-only HEAD infra/aws/lambda/transcripts-pull shows build.sh and handler.py exist at HEAD (out of cone, not checked out)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The worktree carries every path the task order grants (data/m365_metadata/scripts/**, infra/aws/lambda/m365-metadata-collector/**, infra/aws/terraform/trino/collector.tf) and the model files it names to read (infra/aws/lambda/transcripts-pull/build.sh, infra/aws/terraform/transcripts/pull.tf).",
    "world_is": "The worktree's sparse-checkout cone admits none of the granted code paths; only the investigation file among the seven tested paths is in the cone. The check invocations therefore run against a missing tree and print the REFUSED-missing line for guard, coverage and collect.",
    "notes": "Stopped before any criterion was graded. No file was created under data/ or infra/, the sparse-checkout definition was not widened (widening it is rebuilding the tree the bar forbids), and no proof instance was written. The check invocations were run once each under timeout 120 and printed GUARD/COVERAGE/COLLECT-REFUSED missing (rc=1). Needs the lane gate or the issuer to put the cone to the grant before the order can run."
  },
  {
    "id": "TCKT_MTADTA-D1-W3-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~3",
    "surfaced_at": "2026-10-16T07:40:00Z",
    "one_line": "The order names lib/opal_naming for every collector key and name, but the builder refuses system m365-metadata (not a systems.json key), so the keys and names are written as literal strings with the named call in a comment, and the door's get_state reply shape is assumed.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~S1 (issuer: the registry-row cell must land m365-metadata and the trino scope, then the literal prefixes in collect.py and the names in collector.tf and handler.py are replaced by builder output in the same change)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python: lib/opal_naming.address('m365-metadata','trino','bronze','audit_events','date=20261015', object=...) -> ValueError: source 'm365-metadata' is not a systems.json key (worktree HEAD c9971df7ca, lib/opal_naming.py:2515)",
        "python: lib/opal_naming.name('m365-metadata','trino','collector','lambda') -> ValueError: system 'm365-metadata' is not a systems.json key (lib/opal_naming.py:2700)",
        "python: lib/opal_naming.name('globgrph', None, 'trino-access', 'lambda') -> globgrph-trino-access-lambda (resolves; used as the door name)",
        "data/m365_metadata/scripts/collector/collect.py module docstring and the key constants; infra/aws/terraform/trino/collector.tf header; infra/aws/lambda/m365-metadata-collector/handler.py header"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Every S3 address is lib/opal_naming.address() output and every resource name is name() output; a builder refusal is a missing registry row to add, never a hand-typed workaround.",
    "world_is": "The builder refuses the m365-metadata system, so the collector's bronze, state and gold prefixes and its Lambda, role, rule and log names are literal strings that reproduce the order's intended addresses. The Lambda zip cannot import lib/opal_naming, so a runtime address() call is not possible there either. The door's get_state reply is assumed to be {body_b64: str|null}; the far-side cell has not stated it.",
    "notes": "Followed the order's own fallback (build the same prefix, comment the call). Left armed: if the registry rows land with different tokens, the literal prefixes drift from the canon and the collector writes to addresses the builder would not produce. Disarm by replacing the literals with builder output once the rows exist, and confirm the door reply shape with the access-door cell."
  },
  {
    "id": "TCKT_MTADTA-D1-W3-S3",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~3",
    "surfaced_at": "2026-10-16T07:40:00Z",
    "one_line": "The coverage key is one object per day (date=YYYY-MM-DD/coverage.json, object name fixed by the order), but every hourly fire writes it, so each fire overwrites the day's coverage and an earlier fire's GAP is replaced by the next fire's record.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~S1 (issuer: decide a per-fire or cumulative coverage object; the order fixes the key as coverage.json under date=, and the door's get_state cannot read gold, so a cumulative record needs a second read path)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_MTADTA/task-orders/TCKT_MTADTA.TO-MD-c1.collector.md worker face COVERAGE: put(\"gold\", <key under .../gold/collection_coverage/date=YYYY-MM-DD/ with object 'coverage.json'>) per fire and per content type",
        "data/m365_metadata/scripts/collector/collect.py (run_once coverage loop): one put per Eastern day per fire, body holds the three content-type records; the key carries no fire or content-type segment",
        "data/m365_metadata/scripts/collector/access_client.py: get_state reads the state dataset only, so the gold object cannot be read back by the collector"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Every fire writes a coverage record per day and content type, and a gap in any fire stays visible in the day's coverage.",
    "world_is": "The key has no fire segment, so the last hourly fire of a day replaces the day's coverage object. A GAP recorded by an earlier fire is erased by a later fire that lists and fetches cleanly. The per-fire counts are the fire's own, not the day's.",
    "notes": "Implemented exactly as the order states (one object per day, body carrying the three content types). The erasure is a property of the fixed key, not of the code path, and the code cannot repair it inside the order's grant. Decision needed before any reader trusts a day's coverage object."
  },
  {
    "id": "TCKT_MTADTA-D1-W3-S4",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~3",
    "surfaced_at": "2026-10-16T07:40:00Z",
    "one_line": "The order asks the cursor's seen list to be trimmed to the last 7 days, but seen holds bare blob ids and the source's list_content returns ids with no time, so the 7-day trim cannot be computed from the cursor.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_MTADTA/task-orders/TCKT_MTADTA.TO-MD-c1.collector.md worker face Cursor: seen is {content_type: [blob id, ...]}, trimmed to the last 7 days",
        "org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_c1.py Source.list_content returns ids only",
        "data/m365_metadata/scripts/collector/collect.py cursor block: seen = listed in this fire minus failed, bounded by the overlap listing"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cursor's seen list is trimmed to the last 7 days so it stays bounded.",
    "world_is": "seen is set to the blobs this fire listed, minus the failed ones. Every fire lists the window from the last cursor minus one hour, so a blob that a later fire can list again is always in the seen list it was written with; the list is bounded by one overlap window, not by seven days. Dedupe is correct by construction for that listing; the 7-day bound is not applied.",
    "notes": "The duplicate-fetch guarantee holds (the second fire fetches nothing, per the check). A cold start with no cursor lists 7 days in one fire, so the first seen list is 7 days of ids before it shrinks."
  },
  {
    "id": "TCKT_MTADTA-D1-W3-S5",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~3",
    "surfaced_at": "2026-10-16T07:40:00Z",
    "one_line": "The order asks for a coverage record per day, but the listing returns blob ids with no time, so a fire's listed, fetched and dropped counts cannot be split by day; they are attributed to the window's end day.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_MTADTA/task-orders/TCKT_MTADTA.TO-MD-c1.collector.md worker face THE DOOR and SOURCE: list_content(content_type, start, end) -> list[blob id]; fetch(content_type, blob) -> list[dict]",
        "data/m365_metadata/scripts/collector/collect.py coverage block: listed, fetched and dropped set on the end day only; events counted per Eastern creation day"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A coverage record per Eastern day and content type reports what the fire listed and fetched for that day.",
    "world_is": "Earlier days touched by the window carry their events but zero listed and fetched, so a fetch failure on an earlier day is reported on the end day instead.",
    "notes": "Chosen because the fixed interface cannot carry a per-blob time. The interface would need to return the blob's content time for per-day attribution."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:14:07Z",
    "one_line": "TO-MD-h1 names infra/aws/terraform/transcripts/main.tf as the template to model on, but this worktree is a sparse checkout that does not materialise that directory; the template was read from HEAD with git show.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git sparse-checkout list in C:/tmp/wk-tckt-mtadta-1 (core.sparseCheckout true) names no infra/aws/terraform/transcripts and no infra/aws/terraform/trino entry; ls of infra/aws/terraform/ shows .gitignore, ROLLBACK_PROCEDURE.md, modules/ and tombstones.json only",
        "git ls-files infra/aws/terraform/transcripts lists main.tf at HEAD c9971df7ca; git show HEAD:infra/aws/terraform/transcripts/main.tf read at lines 1-135, plus its aws_kms_alias, aws_s3_bucket and public-access-block blocks",
        "git add -n infra/aws/terraform/trino/main.tf in the same worktree: rc=0, the new file is addable under the sparse set"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-h1 BUILD step 7: model infra/aws/terraform/trino/main.tf on infra/aws/terraform/transcripts/main.tf lines 1-135 (read them), in the worktree the order names.",
    "world_is": "The template path is absent from the worktree and present only at HEAD. It was read with git show, not by extracting or rebuilding the tree. The new file was written under infra/aws/terraform/trino/, which is not in the sparse list either.",
    "notes": "No tree was rebuilt. The worktree's sparse list is the cause; the template content is unchanged and was modelled from HEAD. The commit of the new file is measured at its commit and reported in the worker report."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:14:07Z",
    "one_line": "TO-MD-h1 asks for the portal targets to be committed on the portal nested branch, but the portal rule requires a cand/<box>/<slug> branch cut from the last PROD release and registered for approval; the portal commit is withheld and the regenerated files stay uncommitted in the nested checkout.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal rev-parse --abbrev-ref HEAD prints wk-TCKT_MTADTA-1-portal at 39dab87f (a DEV merge); git -C portal rev-parse origin/PROD prints ab2c4365",
        "portal/CONTRIBUTING-BOXES.md steps 1-4: build on cand/<box>/<slug> cut from the last PROD release, push under that name, register with open-calls.py add --kind approval; a box never pushes DEV",
        "python lib/opal_naming.py generate --out . rewrote three portal targets: firmDisplayNames (registry hash line only), vendorDisplayNames (hash line plus two VENDOR_DISPLAY_NAMES rows for m365-metadata), firmAccess.ts (identical to the blob bar CRLF, the working copy being CRLF under autocrlf)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-h1 WORKER FACE step 5: if portal/ files change and the worktree carries a portal checkout, commit them inside portal/ on its nested branch and name that commit.",
    "world_is": "The nested portal branch is a DEV-cut line, and the portal change rule (CONTRIBUTING-BOXES steps 1-4) routes any portal change through a cand/<box>/<slug> branch from PROD with an approval registration. The order and the rule disagree; the rule governs a portal change, so the commit was not made.",
    "notes": "Owed by the issuer 2.0.0_SA_COO~S1 and the portal owner: either a cand/dell1/<slug> branch cut from origin/PROD carrying the generated VENDOR_DISPLAY_NAMES rows, or a ruling that generator output is exempt. Criteria AC1 passes on disk; nothing was pushed."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S3",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:14:07Z",
    "one_line": "TO-MD-h1 gives the Lambda role's exception type as 'group' for globgrph-trino-access-group, but root_map.json exceptions carry node types (IAM_ROLE, LAMBDA, IAM_POLICY); the group's node type is IAM_GROUP.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/logic/registry/root_map.json exceptions: Counter over the file gives IAM_POLICY 84, IAM_ROLE 38, LAMBDA 29 and no GROUP type",
        "org/standards/NAMING_SCHEMA.json v1.13 kind.by_type maps IAM_GROUP to kind group; lib/opal_naming_rootmap.py load_map accepts any non-empty string as an exception type",
        "root_map.json roots.trino.exceptions[0] written with type IAM_GROUP; python lib/opal_naming.py validate rc=0 after the edit"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-h1 BUILD step 3: add the exception globgrph-trino-access-group with type group.",
    "world_is": "The file's exception types are node types, and the node type that carries the kind group is IAM_GROUP. The literal word group is a kind, not a type in this file.",
    "notes": "The worker wrote IAM_GROUP, the file's own vocabulary. The issuer should confirm before the MD-a-1 order reads the entry."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S4",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:14:07Z",
    "one_line": "TO-MD-h1 points to section 4 of infra/logic/06_CONFORMANCE_LEDGER.md as the R20 entry schema, but that section is the shared serving bucket; the schema is 02_DOCTRINE.md section 4 and the entries are ledger section 6.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/logic/06_CONFORMANCE_LEDGER.md line 111: '## \u00a74. THE SHARED SERVING BUCKET -- opal-data-portal-v2'",
        "infra/logic/02_DOCTRINE.md line 599: '## \u00a74. THE EXCEPTION REGISTER -- its schema (its ENTRIES live in 06_CONFORMANCE_LEDGER.md \u00a76)'",
        "infra/logic/06_CONFORMANCE_LEDGER.md section 6 table: rows X1 to X17 before the edit; the new row X18 was added after X17 with the schema's columns"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-h1 BUILD step 6: read section 4 (the entry schema) and section 6 (the register) of infra/logic/06_CONFORMANCE_LEDGER.md, then add one R20 entry.",
    "world_is": "The entry schema is in infra/logic/02_DOCTRINE.md section 4; the ledger's section 4 is a different plane. The entry was written to the ledger's section 6 register table, the carrier the doctrine names.",
    "notes": "The entry follows the doctrine schema (pipeline, axis, departure, why, acknowledged, kind, state). Registered as X18."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S5",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:26:19Z",
    "one_line": "The coordinator reports TO-MD-h1 merged at issuer commit 77716ab496 on this branch, but that commit is not an ancestor of wk-TCKT_MTADTA-1 HEAD (7ffa70368d); the merge was not performed here, the order's files are read from the branch as it stands.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git cat-file -t 77716ab496 returns commit; git merge-base --is-ancestor 77716ab496 HEAD returns not-ancestor in C:/tmp/wk-tckt-mtadta-1",
        "the sparse cone of the worktree lists infra/aws/lambda/globgrph-trino-access, infra/aws/lambda/m365-metadata-collector and infra/aws/terraform/trino, but the first two directories are absent on disk at HEAD 7ffa70368d",
        "infra/aws/lambda/globgrph-trino-access/silver_builder.py is absent in the worktree; build.sh refused with rc=1 on its cp step"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-a1 BOUNDS: silver_builder.py is another cell's file, already merged in the issuer's tree; the worker creates nothing there and injects a stub in its tests. Coordinator message: the order runs in the same worktree on the same branch, after TO-MD-h1 is merged.",
    "world_is": "The issuer's merge is a commit the branch does not contain. The branch carries the h1 rows, the R20 entry and trino/main.tf (commits 21c6720238 and 7ffa70368d), and not the issuer's copy of silver_builder.py. The worker's rule forbids a merge, so the a1 files are written on the branch as it stands.",
    "notes": "The drain or the issuer must merge 77716ab496 into the branch before the a1 commit is merged to CLOUD, or the two copies of the h1 rows meet at the merge. Nothing was merged, rebased or reset."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S6",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:26:19Z",
    "one_line": "TO-MD-a1 asks for a Deny of non-TLS requests to every principal and forbids a wildcard principal, but a Deny for every principal needs Principal star, which the order's own AC2 check refuses as a wildcard; the bucket policy names the role under NotPrincipal and the role's policy denies its own non-TLS requests.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "order TCKT_MTADTA.TO-MD-a1 BUILD 4, bucket policy bullet: 'plus a Deny of any non-TLS request' and BOUNDS-level 'No wildcard principal'",
        "r1_check_a1.py tf: refuses a Principal assignment of the literal star in any form the regex reads (Principal = star-in-quotes or Principal = AWS star-in-quotes)",
        "infra/aws/terraform/trino/access.tf aws_s3_bucket_policy.trino: statement DenyNonTLSRequestsToEveryPrincipalButTheAccessRole uses NotPrincipal = the role ARN; aws_iam_role_policy.access statement DenyNonTLSRequestsByTheRole covers the role"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-a1 BUILD 4: the bucket policy carries an explicit Deny of the data actions to every principal whose aws:PrincipalArn is not the role, plus a Deny of any non-TLS request; no wildcard principal.",
    "world_is": "In AWS a Deny that reaches every principal is written with a wildcard principal, the only form of 'every principal' the policy grammar has. The order forbids that form on the same resource. The worker used NotPrincipal (every principal but the role) for both statements, and split the non-TLS deny for the role into the role's own policy.",
    "notes": "The residual is the same as C-RESIDUAL for the data actions. The issuer should confirm that NotPrincipal plus the role-side deny meet 'every principal' before the drain; the check was not weakened."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S7",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:26:19Z",
    "one_line": "TO-MD-a1 says handler.py imports stdlib plus boto3 only, but the silver reader must read parquet, which needs the AWS-managed pandas layer; the reader imports pandas lazily inside read_day_rows, not at module level.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "order TCKT_MTADTA.TO-MD-a1 BUILD 1: 'the contract above, stdlib plus boto3 imported lazily inside lambda_handler only'; the silver_reader is 'of your own in handler.py'",
        "order WORKER FACE step 2 and the silver builder: the silver builder uses the AWS-managed pandas layer, which carries pyarrow; build.sh does not package pyarrow",
        "infra/aws/lambda/globgrph-trino-access/handler.py _DaySilverReader.read_day_rows: 'import pandas' inside the function body; tests inject a stub reader and never call read_day_rows"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-a1 BUILD 1: handler.py is stdlib plus boto3, imported lazily inside lambda_handler only; the silver reader is the worker's own code in handler.py.",
    "world_is": "Reading the silver parquet from S3 requires a parquet decoder. The stdlib has none, and the layer that provides one is the pandas layer the order names. The reader therefore needs pandas, imported inside read_day_rows; no test exercises that path, because the tests inject the reader.",
    "notes": "The default reader is untested in this round. The issuer should either accept the lazy pandas import in the reader, or move the decode to the silver builder's cell. The stdlib-only line of BUILD 1 is not met for read_day_rows and is recorded here rather than bent."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S8",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:26:19Z",
    "one_line": "The naming gate refused three S3 key literals in handler.py (the gold coverage, silver and bronze tier prefixes), because the door carries them as typed strings; the builder's address() gives the same tails, but the Lambda package carries no lib/opal_naming.py.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit 9d4f20bdb8 safe-commit output: '[naming-gate] NAMING REFUSE infra/aws/lambda/globgrph-trino-access/handler.py:34 gold/collection_coverage/' and lines :35 silver/activity_events/ and :36 bronze/audit_events/date=%s/; '(WARN window: 3 REFUSE verdict(s) did not block; ENFORCE is --enforce ...)'",
        "python lib/opal_naming.py address for ('m365-metadata','trino','silver','activity_events','date=2026-10-15', object='data.parquet') returns s3://opal-data-trino/m365-metadata/trino/silver/activity_events/date=2026-10-15/data.parquet; the gold and bronze forms match the handler's tails",
        "build.sh packages handler.py and silver_builder.py and nothing else, per the order's BUILD 2; lib/opal_naming.py is not in the package"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md rule 30 and the LGIC rule: every S3 address is lib/opal_naming.py address() output; a builder refusal is a missing registry row, never a hand-typed workaround.",
    "world_is": "The door builds its key prefixes from typed tier and table segments. The segments match the builder's output, and the gate grades them as REFUSE in the warn window, so the commit landed. The order's package list leaves no route for the door to call the builder at run time.",
    "notes": "The issuer decides: package the builder's key function with the door, or have Terraform pass the builder-computed prefixes as environment variables. Nothing was changed to silence the gate."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S9",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:26:19Z",
    "one_line": "The naming gate raised, not refused, the IAM resource pattern 'm365-metadata/trino/*' in access.tf as a secret, because its tokeniser cannot place the character star; a grader defect, not a verdict on the name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit 9d4f20bdb8 safe-commit output: '[naming-gate] NAMING RAISE infra/aws/terraform/trino/access.tf:106 m365-metadata/trino/* -> (rule or registry defect)' with why 'RAISE as SECRET: rule or registry defect, not a refusal: G3: the tokeniser cannot place a character of a secret star'",
        "access.tf line 106 is the Resource of the ReadAndWriteTheTrinoPrefix statement of aws_iam_role_policy.access: an S3 object ARN suffix, the same shape as the transcripts pull policy"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The naming gate grades every name and address the diff writes, and a RAISE names a rule or registry defect to the owner of the gate.",
    "world_is": "The IAM policy resource pattern is an S3 object wildcard, not a name. The gate reads it as a secret and cannot place the wildcard character, so it raises instead of grading it.",
    "notes": "Owed to the naming gate's owner. The worker did not alter the resource pattern to silence it."
  },
  {
    "id": "TCKT_MTADTA-D1-S3",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-16T07:35:43Z",
    "one_line": "Issuer's drain read of the round-1 worker rows: what is cleared, what is carried, and what the merge hookups changed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~S1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "merge commits 42e88e6af6, 1398fc4fb1, 1d9a3c6893, 77716ab496, c301aa1ad0 on box/dell1",
        "org/missions/D7/TCKT/TCKT_MTADTA/deliverables/2.0.0_SA_COO~S1/thread_trace_r1.out.json (THREAD-TRACE-OK)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Every worker row is read at the drain and every armed row has a seated disarm.",
    "world_is": "CLEARED: W3-S1 and W4-S1 (the sparse cone lacked the new directories; the issuer widened all four cones and resumed both workers); W3-S2 (the collector's literal keys equal lib/opal_naming address() output for the same arguments, read after the registry rows merged; the door's get_state reply is {ok, body_b64}, driven in the thread trace). CARRIED to the round-2 repair cell: W3-S3 (one coverage object per day is overwritten by each hourly fire; no round-1 reader exists, so nothing trusts it yet), W3-S4 and W3-S5 (the listing returns blob ids with no time, so the seen-list trim and per-day attribution need the source to return content time), W1-S8 and W1-S9 (typed S3 prefixes in handler.py against the naming gate in warn mode, and a grader false positive on an IAM object pattern), W1-S7 (pandas layer for the silver reader, untested path). CARRIED as a separate portal item: W1-S2 (three regenerated portal targets sit uncommitted in the nested portal worktree, removed with it; they regenerate on demand from the registry, and the portal route needs a cand/<box>/<slug> branch and an approved row). W1-S1, W1-S3, W1-S4, W1-S5, W1-S6, W2-S1, W2-S2: accepted, no action.",
    "notes": "Merge hookups found at the drain: (1) collector.tf references the door and the two secret containers as data sources, which fail at plan until those exist. The issuer's lane (TREE_COO) may not write infra/aws/terraform, so the fix is NOT applied: the exact patch (direct references to aws_lambda_function.access and the two aws_secretsmanager_secret resources; terraform fmt clean; init -backend=false + validate Success on a scratch copy of the merged root with placeholder zips) is at org/missions/D7/TCKT/TCKT_MTADTA/deliverables/2.0.0_SA_COO~S1/collector_tf_direct_references.patch, for the CloudOps seat that applies the root (release act 1) to land first. (2) register_app.py stored the bare client secret while collector/source_client.py reads a JSON credential {tenant_id, client_id, client_secret}; the issuer fixed it (data/ is in the issuer's reach)."
  },
  {
    "id": "TCKT_MTADTA-D1-S4",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-16T07:35:43Z",
    "one_line": "The bucket policy denies s3:ListBucket to every principal but the access role, and the Terraform AWS provider's refresh of the bucket (HeadBucket) needs s3:ListBucket, so later plans by the applying identity may fail with 403.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~DELL1 (rules the release-act-1 apply order and the C-RESIDUAL statement; the issuer only surfaces)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/trino/access.tf aws_s3_bucket_policy.trino: Deny of s3:ListBucket and s3:ListBucketVersions to NotPrincipal the role",
        "S3 API reference: HeadBucket requires the s3:ListBucket permission (READ from memory of the reference, NOT exercised: nothing is applied)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "C-ACCESS (3): every other principal gets an explicit Deny, administrators included; C-RESIDUAL (2): administrators can edit the policy.",
    "world_is": "If HeadBucket is denied to the applying identity, every plan of the trino root after the policy lands fails on refreshing aws_s3_bucket.trino, including the plan that would change or remove the policy. The deny of the data actions is what FWD-8 proves, and ListBucket is one of them (a key listing reveals file names, C-RESIDUAL (5)).",
    "notes": "Unread until release act 1. Options for the apply: (i) apply the root in two stages and manage the bucket policy last with the policy then fixed; (ii) keep ListBucket out of the Deny and state the key-name listing in the FWD-8 statement; (iii) admit the apply principal's ARN as a named second exception, which contradicts 'only' and needs Andrew's word. Not ruled by the issuer: it moves the FWD-8 claim."
  },
  {
    "id": "TCKT_MTADTA-D1-S5",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-16T07:35:43Z",
    "one_line": "The collector's execution role invokes the access door by its own identity policy, so 'only members of the IAM group may invoke' (C-ACCESS (1)) is not what the built root enforces: a role cannot be a group member, and nothing in the root restricts invocation to the group.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~DELL1 (owns the PRD; this seat only surfaces)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/trino/collector.tf aws_iam_policy.collector: lambda:InvokeFunction on the door",
        "infra/aws/terraform/trino/access.tf: the group policy grants invoke to the group; the function has no resource policy naming the invokers",
        "org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md C-ACCESS (1) and C-COLLECT (the collector writes through the Lambda)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Its members, and only they, may invoke the access Lambda.",
    "world_is": "Invocation is by IAM grant: the group's members, the collector role, and any principal an administrator grants lambda:InvokeFunction (an administrator can grant itself, C-RESIDUAL (2)). The bucket stays reachable only through the role, so the door's own checks (prefix, no bronze reads, member-only get_day) are the whole control on what an invoker can do.",
    "notes": "Read as a wording gap, not a hole in the data path: the collector must invoke the door by some principal. The FWD-8 statement should say 'the group's members and the collector's role', and the PRD gets an addendum. The door does not authenticate the caller beyond IAM, so no op may return more than the member-only day read and writes under the prefix."
  },
  {
    "id": "TCKT_MTADTA-D1-W5-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~5",
    "surfaced_at": "2026-10-16T08:11:09Z",
    "one_line": "The door's key grammars are hand-written regular expressions in handler.py, and the naming gate's warn window grades five of them REFUSE as NEW and OUT-OF-PATTERN as S3Key, against the rule that every S3 address is lib/opal_naming address() output.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~DELL1 (decides whether the grammar becomes a registry row or stays a stated contract); this worker only surfaces",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/globgrph-trino-access/handler.py@e887029d25 lines 61-64: _GRAMMAR, one pattern per dataset under the PREFIX constant, written by the DOOR CONTRACT v2 in the order",
        "safe-commit of e887029d25 (naming-gate block): NAMING REFUSE handler.py:46, :61, :62, :63, :64 'NEW and OUT-OF-PATTERN as S3Key: REFUSE; LIVE-READ-FAILED: CensusError ... comp-find [aws] BLOCKED'; 'NAMING-GATE: WARN 5 graded'",
        "CLAUDE.md section 4 and the LGIC rule: every S3 address is lib/opal_naming.py address() output; a builder refusal is a missing registry row, never a hand-typed workaround"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Every S3 address and key the estate writes is lib/opal_naming address() output, and a builder refusal is a registry row to add, never a hand-typed workaround.",
    "world_is": "The door's key allowlist is hand-written regular expressions over the PREFIX string, as the order's DOOR CONTRACT v2 requires; the tests compare PREFIX and one key per dataset with address() output and pass (112 of 112). The naming gate, in its warn window (ENFORCE off), grades the five pattern lines as REFUSE, and its live census read was BLOCKED in this worktree, so the refusal reason is not a verified registry gap.",
    "notes": "Filed as an observation, not a block: the order fixed the grammar form and the gate is WARN-only. The CTO decides whether a builder grammar row (a pattern shape per dataset) is the right home, or whether the allowlist stays a stated contract checked against address() output by the tests."
  },
  {
    "id": "TCKT_MTADTA-D1-W6-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~6",
    "surfaced_at": "2026-10-16T08:11:26Z",
    "one_line": "collector.tf grants invoke on aws_lambda_alias.collector.arn, but no aws_lambda_alias is declared anywhere in the trino root at the base commit; the door cell's access.tf has only aws_lambda_function.access.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/trino/access.tf@a49927b4d1: resources are aws_cloudwatch_log_group.access, aws_iam_group.access, aws_iam_group_policy.invoke, aws_iam_role.access, aws_iam_role_policy.access, aws_lambda_function.access, aws_s3_bucket_policy.trino, aws_kms_key_policy.trino; no aws_lambda_alias and no qualifier or publish",
        "infra/aws/terraform/trino/ tree-wide search at a49927b4d1 for aws_lambda_alias: no matches",
        "order TCKT_MTADTA.TO-MD-x2.collector-repair.md Worker Face THE CONTRACTS and BUILD step 4 name aws_lambda_alias.collector as declared in access.tf (another cell's file)",
        "terraform fmt -check on infra/aws/terraform/trino/collector.tf after the edit: rc=0 (format only; validate and plan not run, WORLD bound)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The collector invokes the door through its own alias, collector (DOOR CONTRACT v2: the alias serves put, derive_silver and get_state); the InvokeTheAccessDoorOnly statement names aws_lambda_alias.collector.arn, which access.tf is said to declare.",
    "world_is": "The alias does not exist in the root at the base. collector.tf now references aws_lambda_alias.collector.arn as the order directs (reference, never declare), so terraform plan of the trino root fails on an undeclared resource until the door cell declares the alias. Nothing was planned or applied. The MD-x-2 check AC3 passes on its text, not on a plan.",
    "notes": "Order refusal clause not taken: the reference is the order's literal instruction and access.tf is outside this worker's grant. Owner of the alias is the door cell (MD-x-1); the release act must not apply the root until the alias lands."
  },
  {
    "id": "TCKT_MTADTA-D1-W6-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~6",
    "surfaced_at": "2026-10-16T08:11:26Z",
    "one_line": "The contract names one coverage object per fire per Eastern day the window touches, but a new blob's counts are attributed to its own Eastern day, which can fall outside the touched days (overlap hour, blob created before the window's first day).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/m365_metadata/scripts/collector/collect.py@1175fb6b70: run_once writes coverage for the union of touched days and the days of this fire's blob counts and kept events",
        "org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_x2.py coverage: fire 2 lists blob a2 created 2026-10-14 while the window touches only 2026-10-15; the check does not assert against the extra object",
        "order TCKT_MTADTA.TO-MD-x2.collector-repair.md COLLECTOR CONTRACT v2: 'Per fire, per Eastern day the window touches, ONE coverage object'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "COLLECTOR CONTRACT v2: one coverage object per fire per Eastern day the window touches; listed and fetched count the new blobs whose created falls on that Eastern day.",
    "world_is": "Without the union, a new blob created on a day outside the touched days would have its listed and fetched counts written nowhere, which is the silent loss the repair exists to remove. The build writes one extra coverage object (the blob's day) for that fire. Whether an out-of-window day should get an object is a contract question, not decided here.",
    "notes": "Built to the union so no count is lost. The CTO or issuer may rule the extra object out (then the count must be carried to the next touched day, a contract change)."
  },
  {
    "id": "TCKT_MTADTA-D1-S6",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-16T08:24:58Z",
    "one_line": "TO-MD-r1 item 3 found no authoritative list of Opal office egress addresses, so population.json office_ips stays empty and every address will read remote.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~S1 (the issuer; the list is a named human's input, Andrew's)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "native Grep over the repo for office egress/ip/cidr wording, 34 files; read: infra/aws/ec2/SSH_TUNNEL_OFFICE_IP_ROUTING.md names one office address but is dated 2025-12-22 and says 'Not yet implemented'; the address occurs only in that doc and infra/aws/ec2/tunnel-scripts/ (3 files)",
        "org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md:87,94 quote Andrew saying there are no stable IPs and the source-address axis is dead for this population",
        "data/m365_metadata/scripts/population.json office_ips is [] at HEAD"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-r1 item 3 / PRD C-FIELDS (d): office_ips holds the addresses of Opal's office egress when the estate holds an authoritative list; never an invented address.",
    "world_is": "The estate holds no authoritative current list. One address in a 10-month-old unimplemented design doc is a plan, not a measurement, and Andrew's recorded word is that no stable addresses exist. office_ips is left empty, so the egress label reads remote for every address.",
    "notes": "Nothing invented. If Andrew names the office egress addresses, the list goes into population.json office_ips in a later order."
  },
  {
    "id": "TCKT_MTADTA-D1-S7",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-16T08:45:44Z",
    "one_line": "An IAM administrator (and the dell agent users) can invoke the access door's aliases, because the group policy and the resource permission only grant and nothing denies; the MFA gate of call 0017 binds only the group's own grant.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~TM1 under TO-MD-r1 item 7 (the CTO ruled the fix, msg 6614; the issuer surfaces and gates MD-r-2 on the probe)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_MTADTA/deliverables/2.0.0_SA_COO~S1/R2_FINDING_ADMIN_INVOKE_20261016.md (measured: the box IAM user, in no group, invoked the member and collector aliases, StatusCode 200; the door answered op-not-served)",
        "aws iam simulate-principal-policy for the same user and s3:GetObject against the live bucket policy -> explicitDeny (S3 is sound); a get-object on a missing key answered NoSuchKey",
        "org/missions/D7/TCKT/TCKT_MTADTA/ledger/CTO_RULING_R2_ADMIN_INVOKE_20261016.md: (a) an MFA-absent Deny on each alias's resource policy, (d) an identity-side Deny if (a) does not bind"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Only the group's members (MFA-gated) and the collector role can invoke the door; a non-member's invoke is refused.",
    "world_is": "Same-account IAM allows an invoke when any identity policy or the resource policy allows and nothing explicitly denies. The box user, administrators and the laptop agents' user hold lambda:InvokeFunction in their own policies, so they invoke without MFA and reach get_day on the member alias. The bucket policy's explicit Deny does bind them for S3.",
    "notes": "Disarmed when the probe in TO-MD-r1 item 7d reads AccessDenied for the box identity on both aliases and the collector role still passes its carve-out. MD-r-2 (the consent and the real fires) stays staged until then. Nothing real is stored yet. Correction: the commit 2eefc8d50e message calls this row D1-S6; D1-S6 is the CloudOps seat's office-egress row, and this is D1-S7."
  },
  {
    "id": "TCKT_MTADTA-D1-S8",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-16T08:56:46Z",
    "one_line": "TO-MD-r1 item 5's list-layer-versions call is denied to the box identity (AccessDenied on the public layer account), so the pinned layer version is the highest one a get-layer-version-by-arn probe could read, 31, not a proven newest.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~S1 (the issuer; the order's command is the issuer's text)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws lambda list-layer-versions on arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python312 -> AccessDeniedException lambda:ListLayerVersions for cloudops-dell1-agent-user",
        "get-layer-version-by-arn over versions 14 to 60: readable 14 to 24, 27, 29, 31 (31 created 2026-08-03, python3.12, x86_64); versions 25, 26, 28, 30 and 32 to 60 answer AccessDenied, which is also what a version that does not exist or is not public answers",
        "infra/aws/terraform/trino/layer.auto.tfvars at 8691d491db pins version 31; the root's other pipelines pin version 16"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-r1 item 5: read the CURRENT version ARN of AWSSDKPandas-Python312 with list-layer-versions and pin it.",
    "world_is": "The list call is refused, so currency cannot be read; 31 is the highest version the identity can read. A newer public version that answers AccessDenied would not be seen. The access Lambda runs on version 31 either way.",
    "notes": "If a newer version matters, the pin is one line in layer.auto.tfvars and an in-place update of aws_lambda_function.access."
  },
  {
    "id": "TCKT_MTADTA-D1-S9",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-16T09:04:14Z",
    "one_line": "The IAM user Andrew_Berman, the door group's one member, holds two virtual MFA devices, mfa/Andrew_Phone and mfa/Yang_Phone, so the MFA gate on the door admits whoever holds either device.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~DELL1 (a CTO question for Andrew: whether the second device stays); this seat only surfaces and removes nothing",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws iam list-mfa-devices --user-name Andrew_Berman -> 2 devices (count 2 read at the 7b step of TO-MD-r1)",
        "aws iam list-virtual-mfa-devices --assignment-status Assigned filtered to User Andrew_Berman -> mfa/Andrew_Phone (enabled 2025-11-12) and mfa/Yang_Phone (enabled 2025-11-05)",
        "TO-MD-r1 AC4 R1-MFA-OK reads 'mfa_devices>=1', which a second device also satisfies"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CTO ruling 6605 / TO-MD-r1 item 7b: the door is reachable by Andrew_Berman alone, with his MFA device.",
    "world_is": "The MFA condition tests that some device was used, not whose. A second enabled device named for another person on the same user lets that person's phone satisfy the gate for any session of this user. It still needs the user's AWS credentials, so nothing is reachable by the device alone. The device name is the only evidence of whose phone it is; ownership is not established here.",
    "notes": "Nothing changed. If the second device is not Andrew's, removing it is an IAM act on his user and is his word."
  },
  {
    "id": "TCKT_MTADTA-D1-S10",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.0.0_AB_MSTR~DELL1",
    "surfaced_at": "2026-10-16T13:30:00Z",
    "one_line": "The consent URL printed by register_app.py fails with AADSTS1003031 because the script never sets requiredResourceAccess on the app, although the ActivityFeed.Read role is assigned.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~S1 (cut the register_app.py fix as an order; the consent grant itself is made); this seat only surfaces",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "laptop 1.0.0_SA_CTO msg 109686, relayed by 0.0.0_AB_MSTR on bus 23afd49c at 13:20Z: Andrew ran register_app.py --apply on the laptop at 13:16Z; read afterwards: one app, ActivityFeed.Read role assigned, 1 client secret, api-credentials holds 1 version (value not read)",
        "the same message: the consent URL fails with AADSTS1003031 because the script never sets requiredResourceAccess",
        "this seat measured none of this; it read no Microsoft or AWS state and did not open the script"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Card step 5 (TCKT_MTADTA.TO-MD-r2.andrew_consent_card.md): Andrew opens the printed consent URL and grants consent.",
    "world_is": "As reported by the laptop CTO, the printed consent URL is not usable (AADSTS1003031), yet the laptop CTO reports the role assigned and the grant made; how consent was reached is not stated in the relay. Also reported: card step 1 (the unified audit-log check, Get-AdminAuditLogConfig) was not run because Andrew holds no Exchange role; someone who does still owes it.",
    "notes": "Nothing changed by this seat. The client id is in a Taildrop file in dell1 Downloads and is not recorded here."
  },
  {
    "id": "TCKT_MTADTA-D1-S11",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-16T13:46:05Z",
    "one_line": "The collector's first scheduled fire, 13:31:22Z, ran to the 300 s timeout and was retried twice; the fires check printed R2-FIRES-OK on it because it greps only errorMessage and Traceback.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~S1 (the issuer: who repairs the collector's hang and the fires check)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "/aws/lambda/m365-metadata-trino-collector-lambda: START 13:31:22Z, REPORT Duration 300000.00 ms Status: timeout; same request id START 13:37:21Z, REPORT Duration 300000.00 ms Status: timeout; no application log line in either",
        "/aws/lambda/globgrph-trino-access-lambda: op=get_state outcome=absent at 13:31:27Z, 13:37:24Z and 13:44:38Z, each about 2 s, so the door answered and the hang follows the cursor read in handler.py",
        "CloudWatch AWS/Lambda Errors for the collector, 13:00Z hour: Sum 2.0; Invocations 2.0 (door 3.0)",
        "org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r2.py lines 99-105: counts REPORT lines, greps '?errorMessage ?Traceback'; printed R2-FIRES-OK invocations_since_start=2 function_errors=0 at 13:43:48Z"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-r2 AC3: at least two scheduled collector invocations since the subscriptions started, and no function error since then.",
    "world_is": "One scheduled fire exists, and it timed out; Lambda's two async retries are the second and third START lines, so the 2 counted invocations are one failed fire, not two scheduled fires. The check cannot tell a timeout from a success. Where the collector waits for 300 s is not established here: the Management API listing or the token call (source_client.py) are the calls after the cursor read, and neither logs.",
    "notes": "No hand invoke, no retry, no code change. The next scheduled fire at about 14:31Z is expected to fail the same way and would be a second failed fire, not evidence for AC3. Disabling the rule is a Terraform change to collector.tf, outside this order's grant."
  },
  {
    "id": "TCKT_MTADTA-D1-S12",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-16T13:49:30Z",
    "one_line": "The first scheduled fire of the collector timed out at 300 s and was retried from zero twice: a cold start fetches the whole 7-day backlog one blob at a time and writes nothing before the limit; and the fires check read OK on it.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~S1 (this order's issuer: TO-MD-x2 reopened with a time budget; TM1 reapplies collector.tf)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CloudWatch /aws/lambda/m365-metadata-trino-collector-lambda 13:31Z to 13:44Z: three REPORT lines Status: timeout, Duration 300000 ms, Max Memory Used 104-108 MB, no application log line",
        "0.7.0_AE_CloudOps~TM1 msg 6722 (door answered each time: op=get_state outcome=absent, about 2 s)",
        "the issuer's read-only listing timings with the app credential (no event body read): one 24-hour window of one content type lists 9 to 87 blobs in 0.2 to 1.8 s, so the listing is not the slow part",
        "r2_check_r2.py fires read R2-FIRES-OK on two timed-out invocations because it grepped errorMessage and Traceback only; fixed to count Status: timeout and Task timed out"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Two scheduled fires land cleanly within the Lambda limit; a fire that cannot finish leaves the work it did.",
    "world_is": "With no cursor the fire lists seven days of blobs and fetches them sequentially before writing bronze or the cursor; the fetch total exceeds 300 s, so a timeout loses everything and each retry starts over. The tenant's unified audit feed holds content for all seven days (so audit logging is on: the earlier unrun check is answered by this read). The fires check counted REPORT lines and greps for errorMessage/Traceback, which a timeout never writes.",
    "notes": "Repair: a time budget with save-as-you-go and parallel fetch (TO-MD-x2 reopened, criterion AC4), timeout 900 in collector.tf, one counts-only log line per fire. The seat then rebuilds the zip and applies the in-place update (TO-MD-r2). Attempts 2 and 3 of fire 1 spent the same 300 s each; the 14:31Z and later scheduled fires fail the same way until the repair lands."
  },
  {
    "id": "TCKT_MTADTA-D1-S13",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-16T15:45:50Z",
    "one_line": "read_day.py (round 1) invoked the door unqualified, so Andrew's FWD-1 day read would have been served nothing: the round-2 door decides from the invoked alias and the members' alias is 'member'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~S1 (fixed in the same commit)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/m365_metadata/scripts/silver/read_day.py _lambda_invoker at HEAD before the fix: client.invoke(FunctionName=function, Payload=...) with no Qualifier",
        "infra/aws/lambda/globgrph-trino-access/handler.py _alias(): an unqualified ARN yields no alias and every op is refused",
        "first_content.py (MD-x-3) already passed Qualifier='member'; the read_day tests injected the invoker and never exercised the real one"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Andrew names one of the eight and a day and reads that person's day through the door (FWD-1).",
    "world_is": "The round-1 day-read script was written before the door had aliases. Its unit tests inject the invoker, so nothing exercised the real call. Caught by reading the script before sending Andrew to run it.",
    "notes": "Fixed with Qualifier='member' and a test that stubs boto3 and asserts the qualifier and function name. A live run needs Andrew's MFA session, which no seat has; the first live use is his read."
  }
]
```
