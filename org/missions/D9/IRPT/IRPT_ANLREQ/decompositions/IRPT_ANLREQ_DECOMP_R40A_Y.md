# IRPT_ANLREQ -- decomposition, round 40A: THE RELEASE-29 WINDOW (apply L2, L4, L3, then the partner-advisor sitting), workstream ZD round 40 (issuer 2.0.0_SA_COO~Y2)

**Input:** the three drained builds of round 39 (`AR-y-309`, `AR-y-310`, `AR-y-311`, merged `65b07693f4`, `7fbee50933`, `d8c6d4c3dc`) and the release-29 never-widen pair, COO half blob `5e8b3cbd95739fe8b9172329cc671d2ef7ea1aa8` (commit `1a9bdd3efa`), CTO half SIGNED by `1.0.0_SA_CTO~DELL2` (@abbfe49feb, msg 7591) with R0f (counts, read by `~AQ2` before any mint, a gate with no threshold), R0g (the live partner-table policy of the L3 role, a gate), the exact-failure-set rule for L3's suite, and synthetic callers minted in `49financial` (A, B) and `cottonwood`. Release 28 is live and is the start state.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-312` | LEG L2: `irpt-status` at CodeSha256 `yNpw441T...` (`status.py`, one word entry), after-reads S1 to S3, map record | one Lambda's code, one S3 object version; the applier's record folder | WORLD |
| `AR-y-313` | LEG L4: the resident root `0485393f3a-r29` over the running r28 (4 of 299 members), P1 pre-read and V1 read-back | host `i-0167fd745ad906a66`, three new S3 keys | WORLD |
| `AR-y-314` | LEG L3: `irpt-ycharts-generate` at CodeSha256 `5TRFZf6G...` (`uploads.py`, `generate_installed.py`, plus `ordinary_viewer.py`), gates R0b, R0f, R0g, the L3 suite's exact failure set, after-reads G1 to G4, map record | one Lambda's code, one S3 object version; the applier's record folder | WORLD |
| `AR-y-315` | the sitting D1 to D6 and C1 as synthetic users of the three real partner firms, rows minted and removed, every written object listed by key and VersionId, none deleted | synthetic users and partner rows for one sitting; the door's route; the applier's record folder | WORLD |

## Edges and chains

- ONE chain: `AR-y-312` then `AR-y-313` then `AR-y-314` then `AR-y-315`. L2 first (the words before the emitter), L4 before L3 (the resident re-opens stored inputs with the same `uploads.py`), L3 last (the only widening), the sitting after L3. An applier starts a leg only on the issuer's message that the leg before it is closed.
- Not in this round: the Shares price-source READ cell (CTO 7546), the portal partner-firm filing page (its own route), the delete of the sitting's objects (a call the CTO registers for Andrew).

fanout: 1 of 1 chains, cap 8, reason: the legs are ordered by the pair and each needs the one before it closed; three appliers hold the four orders (`~AQ2` L2, L3 and the sitting; `~YC2` L4).
