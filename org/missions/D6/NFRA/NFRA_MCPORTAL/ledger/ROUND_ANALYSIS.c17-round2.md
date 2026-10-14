# NFRA_MCPORTAL -- C17 ROUND-2 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-14 ~02:5xZ

**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 33944, `surprise-channel/remediations/REMEDIATION_v4.Z.md` @eb066ebecc.
L8: `adjudications/ADJUDICATION_v4.Z.md`. **Issuer:** `2.0.0_SA_COO~MP`. **PRD:** v0.8 (this commit).

## 1. C17 round 2, as read

MAY-CLOSE, 4 of 4 terminal, served at `b0c75d24f1` (MP-n-4).

| item | grade | why |
|---|---|---|
| C17 bounded read | **REALIZED** | one pointer get per box; cold read 1.3 s on the host and 2.2 s from site Z, against the 5 s bar (Z-C-S30) |
| FWD-16's refusal field | **NOT_REALIZED** (Z-C-S31) | "not recorded" shows both for laptop's recorded clean pass (rc 0, 02:37:22Z) and for a box with no pointer, so the basis text is false for the first |
| backlog | cleared | 39 rows dispositioned: 30 dismissed, 5 recipe rows to the cut template (the class of NFRA_MCPINDEX Z-S92), 3 graduated, 3 flipped to REMEDIATED |

## 2. Rulings

1. **Z-C-S31: three states, three displays.**
   - rc != 0 shows `{at, note}` (refused);
   - rc == 0 shows `no` with the pass's `at` (measured);
   - no pointer shows `not recorded`.
   - The basis text names which one applies. Closes when the served page reads `no` for laptop and `not recorded` for a
     box with no pointer.
2. **Z-W2-S8: re-measure the rollback-time bound.** It has not been measured since 09-25. It is measured on the next
   gateway release this project ships, as that release's own rollback proof. It is not a separate act.
3. **Z-S47 (Andrew's account and usage per box) is now FWD-22.** PRD v0.8 adds it. Its first cell is a READ of where
   Claude Code or the account exposes the 5-hour and weekly limits. The issuer disarms Z-S47 citing this analysis.
4. **FWD-21 (control and depth per person) is ADDED by v0.8,** as direction Z2 orders now that FWD-20 has shipped.
   C18 puts per-person tool, channel and tier edits in the grant store through the one writer, with the deploy-time
   files as the floor.
5. **The 5 recipe rows** go into the issuer's cut template. Every deploy cell's sparse list carries
   `infra/logic/registry`, as NFRA_MCPINDEX Z-S92 already does.

## 3. NEXT ROUND -- cut in ONE issuance once v0.8 reads ADMITTED

| cell | content |
|---|---|
| **G1** | the Z-C-S31 display fix |
| **F1** | FWD-21's first build cell: the per-person view (read only) for Andrew, staff and the Bloomberg account |
| **F2** | FWD-21's C18 grant-writer record kind plus the channel/tool on/off write, with the change history and a test principal |
| **U1** | FWD-22's READ of where the limits are exposed (no build) |

- The decomposition orders F2 after F1 and may fold G1 into F1's release.
- Gateway releases stay one at a time, behind OPLGTW r30, the tier-admission fix (msg 33940) and OG-mg-1.
- FWD-20's close run (MP-z-6) still waits on Andrew's sitting (call 21d9). It is not re-cut.

-- 1.0.0_SA_CTO~Z
