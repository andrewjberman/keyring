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
  }
]
```
