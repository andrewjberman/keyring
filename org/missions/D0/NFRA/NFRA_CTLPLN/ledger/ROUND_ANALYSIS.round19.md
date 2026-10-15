# NFRA_CTLPLN -- ROUND-19 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~13:5xZ)

**On:**
- the issuer's drain end `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND19.md` and `ROUND19_INPUTS_FOR_ROUND_ANALYSIS.md` @d359d2bd70;
- the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v24.md` @ebf6c3668f (MAY-CLOSE, 28 of 28 proofs, two rows
  graduate ARMED to REMEDIATION_v9);
- the CVO's full re-grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_FWD_REGRADE_20261015.md` @e3297f2394.

**PRD:** v0.31 (ADMITTED @2283f3a389).

## 1. FWD coverage (rule of round 18: every analysis opens here)

| grade | count | FWDs |
|---|---|---|
| REALIZED | 2 | 1, 28 |
| ADVANCED (built in part, not exercised end to end) | 21 | 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 27 |
| GATED on Andrew | 1 | 11 (`7841`, his restart hour) |
| PARKED | 1 | 9 |
| MOVED | 3 | 13, 20, 26 |

**Round 19 served outcomes, not hygiene.** Five of its six cells drove an arm:
- FWD-5: the negative arm, an unsigned push deploys nothing;
- FWD-27: the laptop side, key login accepted and password refused on three boxes;
- FWD-7: the placement read across the four boxes, 56 overlaps and one real split;
- FWD-2: a fixture box named by 6 of 8 tools;
- FWD-23: the seat list, 10 seats named.

No FWD changed tier, because each arm driven was one arm of several. The gap that remains is the same in every case: **the real
case, not the temporary folder.** No real package has been requested, no signed change has been pushed, and no real box has been
added.

## 2. Rulings

1. **W106-S5 is ruled:** `.tools/safe_deploy_core.py` has one writer, IRPT_BCKEND on dell2
   (`org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261015_134xZ_SAFE_DEPLOY_CORE_ONE_WRITER.md` @c2dfedeecf). Both box CTOs
   acknowledged it through `0.0.0_AB_MSTR` at 13:39-13:40Z. FWD-7's one split is closed. FWD-7 reaches REALIZED when the CVO
   re-reads the placement and finds no split.
2. **FWD-15, 16, 18 and 19 are one chain and are cut as one real journey.** One package a Dell lane actually needs follows this
   path:
   - `1.0.0_SA_CTO~DELL1` names the package (the request);
   - this seat decides it: approve the real package, and refuse a second request that is out of policy;
   - the fetch writes a device key (W111-S1, first);
   - the package is checked and delivered by taildrop and installed;
   - the lane's own run uses it;
   - the CVO, which took no part, reads it all back.

   FWD-18's site Z arm (`kit_pip_no_egress.py wrap -- download six`) goes through `0.0.0_AB_MSTR~Z`.
3. **FWD-5's positive arm:** one signed change that names a script deploys exactly that script, in a real push, through
   `0.7.0_AE_CloudOps~U7`. D1-S8 (the bound on the deploy set) lands first in the same cell. A deploy is the act being proved, so
   the cell opens and closes its own NEVER-2 ledger entry.
4. **FWD-3:** the issuer reads `crossbox-matrix.py` once the managers have acknowledged pair 12 (v0.31: managers acknowledge, not
   workers). If it reads 12 of 12 acknowledged, that read is the cell.
5. **FWD-21** (v0.31): read site Z's broker for any ask before the 23:32Z respawns. With no ask, those respawns are the exercise,
   read against site Z's spawn audit and one MSTR day record.
6. **FWD-24** waits on site Z's answer to `e670`, a qualified wait on another box's lead, not on Andrew. When it lands, the issuer
   compares the two answers on the record. No cell is cut.
7. **FWD-2:** a real second exercise needs a real new box, and none is in sight. That is a qualified wait. One build cell points
   the 2 unreached tools at a register copy, so that the fixture read becomes 8 of 8.
8. **The four old `r18_batch_*` folders under Temp** are a recursive delete, so they are Andrew's word. The issuer adds them to the
   existing laptop clean-up call `715c` and does not open a new call.
9. **The `known_hosts` entries** written by worker `~109`'s diagnostic `ssh` are accepted. They are the boxes' real host keys, and
   FWD-27 depends on them.

## 3. ENRICHMENT LIST for round 20 (one issuance; fan-out per the issuer's chains, cap 8)

1. The package journey (ruling 2): W111-S1, then the chain end to end.
2. FWD-5's positive arm with D1-S8 (ruling 3).
3. FWD-21's site Z read (ruling 5).
4. FWD-3's matrix read (ruling 4), if the acknowledgement is in by the cut.
5. FWD-2's register-copy pointer for the 2 unreached tools (ruling 7).
6. **One hygiene batch:** W108-S2 (`test_named_commit_deploy.py` dies at case 8 on `git_bash_resolver`; fix the import path) and
   W110-S1 (the risk reflex's map, outside CT-ai-5's grant).
