# NFRA_REPORT -- surprise channel, REMEDIATION v2 (site Z) -- THE ROUND-3 SLUG

**Home:** the project tree's channel (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5). **Lane:** the CVO only.
**Cut by:** `3.0.0_SA_CVO~Z`, round 3, 2026-09-10 ~11:0xZ. **Reader:** `1.0.0_SA_CTO~Z`, and no one else.

**L10 PRECONDITION, BOTH LIMBS, SOURCE = THE INDEX** (`_latest_dispositions` imported and called):

```
27 items | UNDISPOSITIONED 0 | GRADUATED 15 | DISMISSED_WITH_REASON 12
JUDGMENT criteria: ZERO, measured on BOTH keys -- the `judgment` field AND the `criterion_verbatim`
                   prefix -- across RP-s-20's single proof instance (6 criteria, all PASS).
                   Round 1's C-S4 ASSERTED an empty judgment set without measuring and C-S5 had to
                   correct it; this is measured.
task orders        20 files read UNSCOPED, 0 NON-TERMINAL
CONTROL            the same census on NFRA_OPSEC202609 returns 168 items -- it fires on a second project
```

**THIS SLUG CARRIES TWO ROWS**, the round's whole graduated set. Neither asks for a build.

- `Z-W1-S6` wants a **RULING, not a cell** -- whether FWD-4's bar requires every rendered axis value to be
  ratified, or only that unratified ones be legible as such. 2 of 26 are ratified BY NAME; 23 are the
  worker's own citation-disciplined judgment, and the worker surfaced that against its own deliverable.
- `Z-S14` is a **standing harness hazard with a demonstrated workaround**. Its law surfaces are corrected;
  the primitive is not, and the read-only-subagent extension is expressly NOT disarmed.

**`remedy` and `owner` are this seat's judgment, stated as such** -- both rows name no disarm owner of their
own, so `owner` is the lane that would rule or hold rather than one the rows nominated. Neither is an
assignment; `2.0.0_SA_COO~ZZ`'s recut is the only thing that turns any of it into work.

**AUDITED GATE OVERRIDE** as on both prior slugs: `_coordinate_violations` refuses a NEW row carrying `W<n>`
from a non-worker committer while protocol s.5 requires the remediation id to EQUAL the graduated id.
`Z-W1-S6` is worker-surfaced. The gate cannot tell MINTING an id from CARRYING one.

---

```json
[
  {
    "id": "NFRA_REPORT-Z-W1-S6",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RP-s-20's ACT and the v0.7 ruling ground the ATTRIBUTION value for only 2 of the composer's 26 rows by name (opal-gateway -> Gateway, opal-globgrph -> Graph); the other 24 rows' axis values are UNSPECIFIED by any spec document and this cell had to perform its own per-row grounding search across round-1 deliverables to fill them, defaulting to UNGROUPED wherever no citation tied a row to a named member.",
    "evidence": [
      "The task order's ACT (LIMB B) names exactly two rows by description -- 'opal-gateway is Gateway (the MCP server); opal-globgrph is Graph (the ECS Fargate cluster)' -- and BOUNDS forbids re-deriving the row set. Neither the PRD (v0.7 sec.6/sec.8) nor the decomposition states which of Dashboard/Website/Gateway/Graph/UNGROUPED the other 24 ROW_FACTS entries (e.g. the seven SNS alert topics, the three cost segments, the three undeclared API Gateways, the four deprecation-candidate scripts) take.",
      "This cell resolved the remaining 24 by reading each row's own round-1 citation (DEPRECATION.md, ANOMALY_BREAKDOWN.md, INVESTIGATION_v1.md row NFRA_REPORT-Z-S7, COMPUTE_MANIFEST_FINDINGS.md sec.5, MONITORED_VS_SERVED.md sec.3a/3b) and assigning Dashboard/Website only where that citation itself names the surface as feeding opalinvest.dev/opalinvest.com or the Platinum portal, else UNGROUPED per ATTRIBUTION.md sec.3's own 'never guessed' rule -- final distribution (26 of 26 rows): Website=1, Dashboard=6, Graph=1, Gateway=1, UNGROUPED=17 (git hash-object of compose_edition.py at this row's filing: 66a63940a2d64c1c4376b787370a2f7c3784f943).",
      "Each of the 24 rows' attribution grounding is folded into that row's own 'citation' field in compose_edition.py's ROW_FACTS as an 'ATTRIB ...' fragment, so the reasoning is auditable per-row rather than asserted in bulk -- but none of those 24 groundings is a citation Andrew or a prior round ratified FOR THAT SPECIFIC ROW the way the v0.7 ruling ratified opal-gateway and opal-globgrph by name."
    ],
    "remedy": "NO ACT IS OWED AND THE ROW IS EXPLICIT THAT NONE IS. The remedy, if any of the 23 inferred attributions is judged wrong, is a ONE-LINE ROW_FACTS EDIT in compose_edition.py for that row -- not a re-architecture -- and each of the 23 is auditable through its own `citation` field's ATTRIB fragment. WHAT THE NEXT ROUND ACTUALLY NEEDS is a RULING, not a build: whether FWD-4's bar requires every rendered axis value to be ratified, or only that unratified ones be legible as such. The deliverable already satisfies the second reading. That call is 1.0.0_SA_CTO~Z's at L4 or Andrew's, and this row exists so it is made deliberately rather than by a reader assuming 26 uniform values carry 26 uniform authorities.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_REPORT-Z-S14",
    "project": "NFRA_REPORT",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE AGENT TOOL'S `isolation: worktree` CUTS THE SUBAGENT'S TREE FROM THE REPOSITORY'S DEFAULT BRANCH, NOT FROM THE BRANCH THE ISSUER IS ON. On this device origin/main's tip is af88fcdd01 (2026-01-19), 34,117 commits behind origin/SITEZ, with NO org/ and NO .tools/ at all -- so a v3 worker spawned that way lands on a tree from BEFORE this estate's work existed and every path its order names resolves to nothing, including the order itself. Cost this lane one worker spawn on RP-s-20.",
    "evidence": [
      "INSTRUMENT 1, the worker's own filesystem (0.9.0_WK_NFRA_REPORT~1, first spawn of TO-RP-s-20): reported worktree HEAD af88fcdd01 committed 2026-01-19, `ls` at the worktree root showing lowercase `tools/` and NO `org/` and NO `.tools/`, and `git remote -v` resolving to the CORRECT repo (Opal-Capital/ajb_workspace.git) -- so it separated 'wrong repo' from 'right repo, wrong commit' before concluding. It refused to rebuild, extract or reconstruct the tree and returned BLOCKED without attempting a criterion.",
      "INSTRUMENT 2, this lane, reading the COMMIT rather than a filesystem: `git log -1 origin/main` -> af88fcdd01 2026-01-19T20:01:30Z, i.e. ORIGIN/MAIN'S TIP IS THAT COMMIT; `git ls-tree --name-only af88fcdd01` -> START_HERE.md, data/, tools/ and no org/, no .tools/; `git merge-base --is-ancestor af88fcdd01 SITEZ` -> YES, so it is genuinely this repo's history and not a foreign tree.",
      "INSTRUMENT 3, 0.0.0_AB_MSTR~Z (msg 20874), reading the TREE OBJECT path-scoped WITH A POSITIVE CONTROL -- a third reading, not a re-run of either above: `git ls-tree --name-only origin/main -- org` -> 0 ABSENT; `-- .tools` -> 0 ABSENT; `-- START_HERE.md` -> 1, THE PROBE FIRES; `git rev-list --count origin/main..origin/SITEZ` -> 34117. The control is what makes the two zeros evidence rather than a possibly-broken pathspec.",
      "THE REMEDY, EXERCISED AND ISSUER-VERIFIED BEFORE THE RE-SPAWN: `git worktree add \"C:/tmp/wk-NR3-1\" -b \"wk-NFRA_REPORT-3-1\" HEAD` from SITEZ HEAD a2a4a179ac, then the bar checked by the ISSUER rather than left to the worker -- org/ PRESENT, .tools/ PRESENT, TO-RP-s-20 PRESENT, compose_edition.py PRESENT. The stale worktree and its branch worktree-agent-* were removed.",
      "THE PATTERN WAS ALREADY IN USE BY TWO LANES AND THIS LANE SIMPLY DID NOT FOLLOW IT: 2.0.0_SA_COO~ZI's four live workers sit on C:/tmp/wk-iamroles-1 and -2 (branches wk-NFRA_IAMROLES202609-1/-2), and round 2 of this project used C:/Users/Opal Bloomberg/Desktop/wk-NR2-1 (cited inside row NFRA_REPORT-Z-W1-S5's own evidence). Both are manually created from SITEZ."
    ],
    "remedy": "REMEDY DEMONSTRATED AND THE LAW SURFACES ALREADY CORRECTED at @c1a0077dd7 -- the agent-definition listing and /dispatch's skill no longer contradict each other, and the working pattern is a manually-created worktree from SITEZ HEAD rather than the harness `isolation: worktree` flag. ⛔ THE HARNESS PRIMITIVE ITSELF IS UNCHANGED and this row does not claim otherwise: a seat passing `isolation: worktree` on this device still gets a January tree. What remains is not a build but a STANDING HAZARD with a documented workaround, plus the extension 0.0.0_AB_MSTR~Z added and which Z-S15 explicitly does NOT disarm -- a READ-ONLY subagent spawned the same way has no order to fail to find, so it does not return BLOCKED and its wrong-tree answers look normal.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v3"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZ",
      "at": "2026-09-10T10:45:00Z"
    }
  }
]
```
