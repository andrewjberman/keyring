# NFRA_OPALAI -- ROUND 1 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-09-28 ~20:xxZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (msg 20260928T152841Z; `ADJUDICATION_v2.Z.md` and `REMEDIATION_v1.Z.md`
@cf78e10896). Round 1 was issued and closed by `2.0.0_SA_COO~O` (close @4ce47993e4, on Andrew's word to close every
round so the CVO can slug). **The recut belongs to the project's new issuer, `2.0.0_SA_COO~AI`** (placement
@094c84f299), in ONE issuance. Grade tokens: `REALIZED | NOT_REALIZED | HELD` (HELD names its gate).

---

## 1. L7, L8 and L9 accepted

- **L7:** 15 of 15 orders are terminal. 13 are complete. OA-t-1 (hop 1, product files move) and OA-t-3 (hop 3,
  runtime setup and launch gate) are superseded at the close, HELD and never graded; each re-cuts unchanged once
  Andrew's gates land (section 3, R-3).
- **L8:** 30 of 30 undispositioned rows are dispositioned; the fold reads 0 of 54 open (5 files). 23 dismissed (C-S5),
  7 graduated (C-S6): 3 remediated on re-read (Z-W2-S2, Z-S11, Z-S14), 4 open (Z-S4, Z-S17 this seat's; Z-S20,
  Z-W8-S1 the issuer's).
- **L9: VACUOUS, cause named (C-S7).** 0 of 15 orders carried a judgment criterion, and 8 of them are WORLD risk
  (OA-f-1, f-2, g-1, g-2, g-3, t-1, t-5, t-6). Every grade in this round is mechanical. No criterion asked whether a
  served answer was the right answer. ADOPTED as the round-2 cut rule (section 4, rule J).

**What round 1 built** (read from the orders and their commits, not from status prose):
- the `opal_ai` submodule root, nested-repo gates, its CI workflow, and census tools that count submodule work
  (OA-w-1..w-4);
- the Opal_Agent provisioning script and boundary verifier (OA-t-2), and a Teams watch on its own token (OA-t-4);
- `opal_asker_query`, the asker-scoped query tool, live on the served gateway (OA-t-5, OA-t-6);
- the upload fence keyed on (identity, OAuth client_id), released narrow (OA-f-1, OA-f-2);
- portal-only asker grants, released narrow, and Alyssa Keith's portal-only grant ACTIVE (OA-g-1..g-3).

## 2. Outcome grades

| FWD | grade | why |
|---|---|---|
| FWD-1 (a colleague's Teams question answered from the Analyst's own account) | HELD, G-ACCT / G-AUTH / G-PUSH | Hops 2, 4 and 5 are built and hop 5 is served. Hops 1 and 3 (OA-t-1, OA-t-3) wait on Andrew's switchover sitting, Parts A-B. No live exchange exists. |
| FWD-2 (every message noticed, including pasted content) | NOT_REALIZED | The watch sees on its own token (OA-t-4), but no working day of messages was exercised. The hostedContents reader is served by the laptop's gateway release (I-5); it is not yet consumed. |
| FWD-3 (a routine answer inside the conversation) | NOT_REALIZED | Speed (S9) is enrichment; no exchange exists to time. |
| FWD-4 (routed right first time) | HELD, NFRA_MCPINDEX delivery | Graded here only once that project delivers into `opal_ai` (PRD). |
| FWD-5 (same answer in Teams and in one's own Claude) | NOT_REALIZED | It needs FWD-1's live path; not exercised. |
| FWD-6 (cannot be talked out of its limits) | NOT_REALIZED | Not exercised. The fence ships with OA-t-3, which is HELD. |
| FWD-7 (cannot reach the workspace; will not start if it could) | HELD, G-ACCT / G-AUTH | The launch gate and its negative arm are OA-t-3's close run. |
| FWD-8 (admit, narrow, remove; explain a past answer) | NOT_REALIZED | Graded against NFRA_MCPORTAL's Entitlements tab, which this project does not build (section 5). |
| FWD-9 (a change reaches colleagues only through Andrew's release) | NOT_REALIZED | The release flow (S13) is first exercised by E3's release. |
| FWD-10 (fresh setup gets the product code) | NOT_REALIZED | Submodule root and census built (OA-w-1, w-4). The fresh setup on EACH device is not exercised. |
| FWD-11 (gateway released from the product's history) | NOT_REALIZED | G-MOVE is now open (Andrew lifted the NFRA_OPLGTW stop). The move is not cut yet (E9). |
| FWD-12 (one entry plus one tool; unclassified tool refused) | HELD, NFRA_MCPINDEX delivery | As FWD-4. |
| FWD-13 (checks pass standalone and on every push) | NOT_REALIZED | The only CI run on record, 36203070607, is a failure (Z-S20). |

**Tally: 0 REALIZED, 4 HELD, 9 NOT_REALIZED.** Round 1 built every hop that did not need Andrew at the terminal. The
thread's missing hops are one sitting away, and that sitting is his call 2 = (a), first after the reboot.

## 3. Rulings on the open rows

**R-1, Z-S4 (this seat's): REMEDIATED @6bc980ad5d, not open.** The CVO carried it OPEN "not re-measured by this seat".
This seat re-read it: `.tools/owned-paths-validate.py:416-419` consults the worker's task-order grant
(`_owns_task_order_paths`) BEFORE emitting `UNDEFINED` for a path with no lane row. That is exactly the ordering the
row names. The fix (2026-09-25 ~05:0xZ) postdates the row (2026-09-24T23:12Z), is on CLOUD, and disarmed the sibling
NFRA_MCPORTAL-Z-W1-S1 in the same commit. The CVO closes the remediation row at the next L8; no cell is cut.

**R-2, Z-S17 (this seat's): CUT into round 2 as cell E11.** Re-read at HEAD: `.tools/git-hooks/owned-paths-check.sh:59`
still takes the FIRST `git worktree list --porcelain` entry, which for a submodule is its gitdir
(`.git/modules/opal_ai`) with no superproject; the fallback then skips the lane check. The remedy: resolve the
superproject from the committing worktree's own path, and FAIL CLOSED (refuse, loud) when none resolves. Criteria:
(1) a planted out-of-lane commit in an `opal_ai` linked worktree outside every parent worktree is REFUSED;
(2) the same commit in the main nested checkout is still refused, and an in-lane one still lands (positive control).
The hook is fabric gate code whose owner is this seat; the cell is a worker cell under the order's `<paths>`.

**R-3, OA-t-1 / OA-t-3: carried, unchanged, behind G-ACCT / G-AUTH / G-PUSH.** They re-cut as round 2's cutover
cells the moment the sitting's Parts A-B land. Their nested `opal_ai` work is published (0.0.0_AB_MSTR~Z correction
@74bce7565e), so the re-cut starts from origin, not from `C:/tmp/oa-1` or `oa-3`. OA-t-1 keeps AC2 at 1 re-point (I-4)
and carries Z-S13's six `census_ref` lines unlowered. **The precondition re-confirm the runbook assigns to
`2.0.0_SA_COO~O` passes to `2.0.0_SA_COO~AI`** for Parts A-C (Part D is NFRA_MCPORTAL's, `2.0.0_SA_COO~MP`), because
site Z's state moved with the S19 rewrite.

**R-4, Z-S20 (the issuer's): into E7.** CI installs pytest and ruff; `portal_lookup.py`'s 15 ruff findings are FIXED,
never waived; `run_checks.sh` reports ruff's real count; one green run on a real push is FWD-13's proof.

**R-5, Z-W8-S1 (the issuer's): into E1.** E1 changes the gateway, so E1's cell runs `tests/test_data_entitlement_guard.py`
with moto available and records the pass count. "Keeps passing" is never graded UNREAD again.

## 4. THE ENRICHMENT LIST ROUND 2 CUTS

The draft's E1-E10 (`deliverables/1.0.0_SA_CTO~O/ROUND2_ENRICHMENT_DRAFT.md`) is ADOPTED with three amendments: E1
gains R-5, E7 gains R-4, and E11 is added (R-2). Cut order:

0. **Cutover cells (gated):** OA-t-1 and OA-t-3 re-cut unchanged, issued when Andrew's sitting lands Parts A-B (R-3).
   Close run: one live exchange graded against A1 (FWD-1), plus one un-admitted asker refused, plus A7's launch-gate
   arms (FWD-7).
1. **E1, the asker-scoping repair** (I-1 + Z-S5, one cell: asker AND caller gate, recency plus same-chat binding,
   group-chat intersection; three negative arms) **+ R-5's moto run.**
2. **E2, the upload fence completed:** drop `opal_data_refresh_upload` from the Analyst's tool list (Z-S18/Z-S19,
   Andrew's option 2 and call 6).
3. **E3, the Analyst switched on for `opal_asker_query`**, only after E1 and E2 land. Its release is FWD-9's first
   exercise (S13).
4. **E4, consume the served hostedContents reader** (I-5) in the serve skill; a message it cannot read gets a plain
   "could not read it" (FWD-2).
5. **E5, re-measure the Teams watch** after the laptop's gap-B fix, before anything more is ruled on blocker (2).
6. **E6, the Bloomberg view server** (S15, design @b99ab96fdf); first cell measures whether Opal_Agent reaches
   `127.0.0.1:8194` and `:8790`.
7. **E7, the batch cell:** the teams-watch header naming its real consumers (I-3) **+ R-4's CI green.** (The
   `_ARGS_ALLOWLIST` row is REMEDIATED, Z-W2-S2, and drops out.)
8. **E8, speed** (FWD-3): measure only, stage by stage, against the 2026-08-20 baseline. Cut only after item 0 lands.
9. **E9, the gateway move into `opal_ai`** (FWD-5, FWD-11). G-MOVE is open. Cut after E1-E3 land, from the ONE release
   base (@75117e60d6); its first cell is the census of what CLOUD holds unreleased on the gateway paths.
10. **E10, retire the legacy `/login` GUI consent:** census first; remove only on zero dependents; never-widen halves.
11. **E11, the nested-worktree fail-open (R-2).**

**Rule J (the CVO's cut rule, adopted): at least one JUDGMENT criterion on a WORLD cell, graded at L9, never
self-graded.** It is placed on E1's release: the CVO reads the three negative-arm transcripts and the group-chat case
and judges whether each answer's scope is the asker's own, not merely whether the tool returned without error. The
item-0 close run carries a second one when it is cut: the CVO judges that the reply's figure, date, source and coverage
match the portal for that date. COST one criterion per cell; NON-APPLICATION a round touching no served answer.

**Standing on every round-2 face:** a device-neutral interpreter; every gateway release NARROW from the current
deployed commit (re-read the manifest at the cut); a criterion that exercises a served file names it in `<paths>`.

## 5. What this analysis does not do

- It does not build operator controls (FWD-8). Those are NFRA_MCPORTAL's Entitlements tab; FWD-8 is graded against it.
- It does not grade FWD-4 or FWD-12; NFRA_MCPINDEX delivers them.
- It does not schedule Andrew's sitting. `1.0.0_SA_CTO~O` schedules it after `2.0.0_SA_COO~AI` re-confirms the
  preconditions.
- It writes no remediation row. The CVO closes Z-S4 and dispositions R-2..R-5 at the round-2 L8.
