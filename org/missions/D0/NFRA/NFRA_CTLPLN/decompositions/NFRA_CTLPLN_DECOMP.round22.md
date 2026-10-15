# NFRA_CTLPLN decomposition -- round 22: the package journey's fetch and check, the manager-only acknowledgement, and one hygiene batch; the dell1 and tailnet reads driven by the issuer (issuer 2.0.0_SA_COO~C; cut 2026-10-15)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round21.md` (1.0.0_SA_CTO, @a558191b7c) sections 1-3 and msg 109483; the CVO's slug `surprise-channel/adjudications/ADJUDICATION_v26.md` @98ddb8c1a9; the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND21.md` and `ROUND21_INPUTS_FOR_ROUND_ANALYSIS.md` @445bca4969. **PRD:** v0.31. **Coverage entering the round:** 28 FWDs: REALIZED 1, 5, 28; ADVANCED 21 (2, 3, 4, 6, 7, 8, 10, 11, 12, 14-19, 21-25, 27); PARKED 9; MOVED 13, 20, 26 (CTO table, round-21 analysis section 1). **Process facts in force:** the round-19 worker-face lines; sparse worktrees cut by `wk-provision.sh`; removal at merge by `worktree_gc.py --go --only` (a relative path); a worker branch cut before an amendment cannot validate against it, so the issuer merges first and validates in the main tree; the registry lanes admit only a worker serial to scripts and test batteries, so a seat order never carries those paths.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-al-1` | Journey steps fetch and check: the tag is recorded (cp314, dell1's CTO), the ONE approved `duckdb-1.5.0-cp314-cp314-win_amd64.whl` is fetched through the checked route, checks 1-7 run, check 8 (the CTO's signature) and the release are NOT done. | FWD-15, 16, 18, 19 | SERVED | `0.9.0_WK_NFRA_CTLPLN~119` |
| `CT-al-2` | `crossbox-call.py ack` refuses any serial that is not the receiving box's MSTR lane; one non-manager ack refused, one manager ack admitted. | FWD-3 | LOCAL | `0.9.0_WK_NFRA_CTLPLN~120` |
| `CT-al-3` | ONE hygiene batch: the danger map carries its build time, the reflex refreshes it itself and never builds in a sparse worktree (`S9127`, `W117-S1/S2/S3`); the FWD-5 read test works after the ledger entry closes. | hygiene | LOCAL | `0.9.0_WK_NFRA_CTLPLN~121` |

| `CT-al-4` | AMENDMENT 1 (2026-10-15 ~20:2xZ, after the CTO SIGNED check 8, @051808678b): the journey's release, pack and Taildrop to dell1 for the one checked wheel; its dependency is met, so it is cut now. The install on dell1 and the lane's read are dell1's, asked by crossbox after the delivery. | FWD-15, 16, 18, 19 | SERVED | `0.9.0_WK_NFRA_CTLPLN~122` |

**Amendment 1 also:** `CT-al-2` (order amended, commit `b9d7c9bd21`): the manager rule replaces the named-seat rule for `ack`, and `test_crossbox_call.py` and `test_round13_batch.py` are added to its paths (rows `W120-S1`, `W120-S2`). `fanout` for the amendment: 1 new cell of 1 chain, cap 8 unchanged.

## Driven by the issuer in this issuance (not cells)

- **FWD-3, the re-read:** the eight acknowledgements by non-manager serials in today's matrix (`4a82` by CloudOps~CA2, `5b04`, `9904`, `5a58`, `bde8`, `d896`, `e03b` by `1.0.0_SA_CTO~DELL1`, `e670` by `1.0.0_SA_CTO~Z`) each get a manager acknowledgement, asked of `0.0.0_AB_MSTR`, or are named in the packet. FWD-3 grades on that re-read after `CT-al-2` lands.
- **FWD-11, one read per owner:** a crossbox call to `0.0.0_AB_MSTR~DELL1` for the class of each of dell1's 18 open ledger entries (interrupted by the 15:46Z restart or ordinary) and the seats that held a round at 15:46Z and their state after.
- **FWD-14, event-1149 reads:** three crossbox calls (dell1, dell2, site Z) for connections from the laptop's address `100.96.167.100` and from the MacBook's `100.98.173.75` since the last read; the issuer reads the laptop's own outbound remote-desktop history. The refused attempt from off the tailnet waits on a seat outside the tailnet or on Andrew's MacBook off it.
- **The 33 owned remediation rows unmoved for 2 or more rounds** are listed by owner in the round-22 packet (CTO ruling 9).
- **The row in MSTR's lane** on `check_inbox` re-printing the accumulated inbox: filed by the issuer.

## Dependencies the cut respects (NOT cut, with the condition that cuts them)

- **The journey after the checks:** check 8 is the CTO reading checks 1-7 and signing a second file; then `release`, `pack`, the taildrop to dell1, the install from the file alone on dell1 (`intake_receive.py verify`, `prove`, `install --target`), the lane `2.0.0_SA_COO~D1`'s one read with duckdb, and the CVO's read-back. Each waits on the one before. Cut in round 23.
- **FWD-24:** `e670` is acknowledged by `1.0.0_SA_CTO~Z` (it is also a non-manager ack); the answer text has not reached the issuer; the two answers are compared when it does.

## Carried with an OWNER and the CONDITION that un-parks each

- **FWD-9:** PARKED. **FWD-14 call `c9a4`, FWD-17 call `318f`:** Andrew's (tonight, and when the duckdb record exists). **FWD-27's person arms:** Andrew's. **FWD-2:** a real second box is a qualified wait.
- **`S9125`:** dell1, before 2026-12-31. **`S9119`:** owner `0.0.0_AB_MSTR~DELL2`. **`S9128`:** `0.0.0_AB_MSTR` (the site Z audit LOG's committed copy). **`S9120`, `S9122`:** per the CVO. **`W117-S4`:** the FIXTURE classing stands unless the CVO overrules it.

## Rule 24

**Domain:** the CTO's round-21 section 3 enrichment list (5 items) against the open FWD chain; denominator in the CTO's section 1 table (28 FWDs). **Same grain; one intent; disjoint write surface:** `CT-al-1` writes the batch's records and a read-only test; `CT-al-2` writes `.tools/crossbox-call.py` and a test; `CT-al-3` writes three graph-module files, the map and three tests; no two cells write the same file except the append-only surprise channel. **State coherence:** `CT-al-1` makes one request to the public package index and installs nothing; `CT-al-2` changes who may acknowledge, so after its merge the CTOs' acknowledgements are refused and the managers acknowledge (the CTO's ruling); no cell deploys, pushes or calls AWS beyond read-only S3 heads.

## Dependency chains and fan-out

Three chains, no dependency between them. `fanout: 3 of 3 chains, cap 8, reason: three independent laptop worker cells; the journey's later steps wait on the CTO's check-8 signature, the reads are crossbox acts`
