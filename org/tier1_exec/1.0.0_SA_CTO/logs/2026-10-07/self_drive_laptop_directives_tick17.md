# /self-drive laptop directives -- ticks 16 and 17 (2026-10-07 22:4xZ to 23:5xZ)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`.
**Cadence:** 60m, cron `77f028d5`. **paired_with:** solo. **state: ARMED**. Covers tick 16 (quiet at its fire; its line is in
`org/mcp/drive_ticks/1.0.0_SA_CTO.md`) and tick 17, since the tick 15 log (author time by `git log`: 2026-10-07T18:32:23 -04:00).

## Measurements (23:46Z unless stated)

- Trunk (fetch): origin CLOUD `58b23cc581`; the shared laptop tree 16 ahead, 719 behind.
- Sequence: no DRIFT, no UNREADABLE, no OUT-OF-SEQUENCE. Capacity 3 of 3 COO lanes: AT CAP.
- Inbox: every message of the hour read and acked (106616 to 106636).
- Laptop memory: 4.3 GB free of 31.7 GB by this seat at 23:46Z; 8.7 GB by `0.0.0_AB_MSTR` at 23:55Z after it closed two lanes
  and stopped a disk scan of its own that had run since 21:10Z.
- `cot-rebalancer-runner-daily` target input: `{"mode":"pull","induce":"auth-lapse"}`.
- At ~23:1xZ the harness killed dell1's vendor classification run on this laptop at 3.93 GB free, 187 of 2,291 keys landed
  (`0.7.0_AE_CloudOps~SC` msg 106632, record @559feeeb5b). Nothing rolled back; order pending; entry OPEN.

## Calls ruled (the driver's own REC, each)

| # | Call | Ruling | Carrier |
|---|---|---|---|
| 1 | The CTO half for the Dell vendor-secrets grant (106616) | signed for THREE, not four: the OpenAI key is out (the whitelist scopes it to one project; need not shown; a read is undone only by rotation) | @922ebc4b5d |
| 2 | Both Dell users may overwrite any secret (same half) | wider than Andrew's words; a cell input to narrow it, measured first | msg 22:59Z |
| 3 | The Python 3.12 kit (106617) | tarred, hashed, sent to both Dells by this seat; both verified 161 of 161 | Taildrop rc=0, sha256 3493f72a...1dd4 |
| 4 | python.org publishes only an MD5 for the installer (106622) | the valid publisher signature plus the MD5 match is enough; dell1's sha256 becomes the listed hash | msgs 23:08Z |
| 5 | The kit verifier reads ok=False on dell2 over the same bytes (106626) | kit accepted; the limb is the verifier's defect, a cell input | msgs 23:26Z |
| 6 | The voice file's home (CVO 106609) | client mail is not committed to the repository; citation corrected | PRD v0.19 clause 10 @b44686cebc |
| 7 | Who holds TO-HG-d3 after the restore (106612) | `0.7.0_AE_CloudOps~F`, respawned at 10:30Z; this seat's first word, "as soon as", was wrong on memory and was reversed | msgs 22:42Z, 23:40Z |
| 8 | dell2's Black Diamond pull, refused a secret on dell2 (106629) | a fresh `0.7.0_AE_CloudOps~I` runs it under dell2's own pair once the order is published; the refused secret enters the grant by name | msgs 23:34Z, 23:35Z |
| 9 | dell1's vendor run killed for memory (106632) | resume is its issuer's call, REC resume; the vendor-secrets grant goes ahead of the remaining SEATS cells | msgs 23:40Z |
| 10 | Site Z's six wheels (106635) | five pure wheels sent from the verified kit by this seat; the sixth is a registry fetch waiting on the batch file this seat signs | Taildrop rc=0; msg 23:58Z |

## Andrew, this hour

- Asked whether the CRO's brief on the overlap streaming system had arrived. Answered: it is a research file addressed to him
  (`org/tier1_exec/4.0.0_SA_CRO/deliverables/FABRIC_PROXIMITY_MAP_RESEARCH_20261007.md` @f0b12ccd02), not sent to this seat.
  This seat ruled its calls B, C and D (a board first; every commit names its box; no refusal at first). Call A is an act of
  his: the standing rule bars building a monitor without his explicit word.

## Open items this seat owns

- The 06:17Z restore check (tick 14 log). Owner (1) is closed until 10:30Z; owner (2) is dell1's 06:10Z task.
- My signature on the first fetch batch, when `2.0.0_SA_COO~C` sends its path.
- An amended half when the counterpart names the fourth secret.
- PARKED on the close record: two facts about 49 Financial's gold chain; un-parks when a laptop deploy lane is free of an order.

## Acts only Andrew can do

- Run `python-3.12.10-amd64.exe` elevated on each Dell (his word: "I can run admin on the Dell boxes").
- "Build it", in so many words, for the cross-box map (CLAUDE.md: never build a monitor unless Andrew explicitly asks).
- The walk-through of the two Dell reports; the naming exception for MDPF_HEALGAP HG-t-2; LGIC_BLANKFIX's DONE WHEN lines.

## Completion test

NOT DONE, read from the register: 9 laptop directives of 15 live; 56 member projects: 5 complete, 14 closed, 3 merged, 34 active.
D10 has no member projects: UNMEASURABLE.

## Compiler Tools

| Tool | Purpose | Result | Note |
|---|---|---|---|
| `sequence-check.py`, `directives-check.py --json` | capacity, completion | PASS | the combined read took over 120 s under memory pressure |
| `tailscale file cp` | two kits to three boxes | PASS | each hash checked against a manifest first |
| `safe-commit.sh` | the half, the clause, this log | PASS | one refusal on another seat's open merge, retried |

- **What worked:** a refused run naming the secret it needs, as the half's condition 5 was written to produce.
- **Gap found:** the laptop hosts the Dells' vendor runs and has the least memory of the four boxes.
