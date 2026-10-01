# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-01 05Z (host opal_bloomberg)

Lease FULL, round 5, limb L7, thread y.

## Decisions closed this span

- **COO~O msg 27532:** principals arrive off-repo at the PHASE B GO, and MX-r-7 is train slot 1 with no re-cut owed.
  - msg 27540: ~O holds OG-pr-1 (TF act #2) until this seat reports TF act #1 applied. OWED: one line to ~O at the
    apply, or as soon as it is known it will not run.
- **MX-r-7 PHASE A reported** by worker ~21 (@df1db63305, LOCAL).
  - Live ref d61fde4693, read twice.
  - Release 6e2f817066 (on carrier 6dda22dd40); deploy-only cfd410608f, tree object equal; rollback tree mx-rb10.
  - Tools 58 -> 60.
  - Fees writer named: `bd-49f-fees-runner` (row Z-W21-S16).
- **Two BLOCKING rows, ruled by A5 @4db8b62899:**
  - Z-W21-S13 -> Plan 6: 6 adds (role, policy, assume, ExternalId secret, its version, its resource policy), 0
    change, 0 destroy.
  - Z-W21-S12 -> option B: the deploy fetches the ExternalId from its secret on the host. `.env` gains
    BLACKDIAMOND_READER_ROLE_ARN and BLACKDIAMOND_READER_EXTERNAL_ID (35 -> 37). No gateway code change; option A
    (a runtime secret read) goes to the round-5 analysis.
- The first worker could not be resumed, so a fresh ~21 was spawned on A5 to re-cut PHASE A and re-issue the ANNOUNCE.

## Train note for the halves ask

MX-r-7's `.env` goes 35 -> 37, so MS-d-2's census (CTO ruling R5: 35 -> 37) becomes 37 -> 39 when it re-cuts on
MX-r-7's ref.

## Compiler Tools

- None. The reads were git, the worker's rows, and `deploy-to-ec2.sh` at the release tree.
