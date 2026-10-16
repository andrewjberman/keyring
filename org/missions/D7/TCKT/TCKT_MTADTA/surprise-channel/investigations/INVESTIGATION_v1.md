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
  }
]
```
