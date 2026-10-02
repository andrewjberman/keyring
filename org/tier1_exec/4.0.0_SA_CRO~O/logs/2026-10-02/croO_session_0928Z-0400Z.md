# 4.0.0_SA_CRO~O session log -- 2026-09-30 ~23:2x ET (03:2xZ 10-01) to 2026-10-02 ~04:0xZ

**archetype:** MIXED (TRACE, EXPLORE, SCRIBE)
**Seat:** 4.0.0_SA_CRO~O, site Z. Watcher armed at load and re-armed on each expiry. Zero crons.
**Close reason:** a wind-down ordered by Andrew, relayed by 0.0.0_AB_MSTR~Z (msg 28185): disk at 100%. Nothing in flight;
no worktree, deploy or merge was open by this seat.

## Work delivered (all read-only research; no code, deploy, apply or host change)

1. **/closer trace of the opal-gateway release train** for 1.0.0_SA_CTO~O (msg 27488): @b1b62bae9f,
   `deliverables/OPAL_GATEWAY_RELEASE_TRAIN_END_TO_END_GAP_BRIEF_20261001.md`.
   - Measured the served commit d61fde4693 on three planes.
   - Found 12 collisions.
   - Recommended the order MX-r-7 -> MS-d-2 -> OG-rl-1 -> G-RDR -> MS-dn-1.
   - Adopted as CTO ruling R1-R7 (@cf5989190d), and the train then landed in that order.
2. **DAPI 8194 wall research** (msg 27791): @5d804ea419. Recommended a per-user Firewall deny.
   **Falsified on the box** (F10: 5 of 5 OPEN), as the brief's own falsifier allowed.
3. **Fabric status brief + /draw** (Andrew-direct): @e039d63459,
   `deliverables/OPALAI_NFRA_FABRIC_STATUS_BRIEF_20261001.md`.
4. **Andrew-direct records**, each routed to 1.0.0_SA_CTO~O with one line:
   - @53ad7cb452: G-PUSH approved; Alyssa is the G-CLOSE colleague; D9 -> D6.
   - @ecc8f0e180: the 8194 wall YES; G-MSPID deferred; the partner rollout is downstream; MCPINDEX and employee MCP
     use come first.
5. **Finding to the CTO:** G-TEAMS-TX appears already met. The 9/29 pull got 200 text/vtt with attribution, and 90
   bronze objects sit in opal-data-transcripts.
6. **WFP loopback wall research** (msg 28056): @63a9b6da27,
   `deliverables/WFP_LOOPBACK_8194_WALL_RESEARCH_20261001.md`.
   - A block filter in our own sublayer, placed above the loopback permit, wins under Microsoft's arbitration rules.
   - Codex #48856 shows the max-weight boot-time permit on build 26200.
   - Installer: Add-Type P/Invoke.
   - The residual is one elevated `netsh wfp show filters`.

Push state: all six session commits were read ON ORIGIN at 00:43Z (ls-remote 0257976705). This log's commit state is
reported in its own commit.

## Open, at Andrew

- **Transcripts reader scope.** On 9/29 Andrew limited transcripts to andrew@ and opalbloomberg@. Do other Opal
  employees get per-principal grants through a bucket-backed MCPINDEX tool? The brief is written on his answer.
- **The WFP filter install.** It replaces the inert Firewall rules. The "sure" of 17:4xZ was read as covering it; he
  may confirm separately.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-find | the transcripts bucket refs (82 hits / 98,833 files); the GetSecretValue grants (19); WFP precedent | worked. `-o` was taken as the pattern (my error; switched to python) |
| comp-read | `transcripts/main.tf` reader principals | worked; `--for` surfaced the variable |
| aws (read-only) | S3 head-object git-ref; SSM md5 census (49cf7307); simulate-principal-policy plus a positive control | worked. The first simulation lacked a valid control; corrected with the real ARN |
| git | content diffs d61 -> CLOUD; per-file author attribution; ls-remote push reads | worked. A `--author` + `--name-only` log over the repo timed out; used subject grep instead |
| WebFetch / WebSearch | Microsoft Learn WFP docs; openai/codex #48856, #49840; WireGuard rules.go | on Andrew's in-session word, docs only |

**Gaps:**
- A raw `grep` of `.tf` is rail-blocked even for a single file. `# rail-checked` was used where no comp-tool fits.
- `get_agent_status` lane liveness lagged registration.
