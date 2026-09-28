# NFRA_OPLGTW -- ROUND 1 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-09-28 ~20:xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (file 20260928T174852Z; `adjudications/ADJUDICATION_v2.Z.md` and
`remediations/REMEDIATION_v1.md` at faa6c87ab2, the post-rewrite id of the slug's @62779d812f). Round 1 was issued on
the laptop by `2.0.0_SA_COO~O` and closed on site Z on Andrew's word to close out the rounds (@4ce47993e4). Grade
tokens are `REALIZED | NOT_REALIZED | DEFERRED | HELD`. The recut belongs to `2.0.0_SA_COO~O`, now this project's
only COO (placement @094c84f299), in ONE issuance.

---

## 1. L7, L8 and L9 accepted

- **L7:** 36 of 36 orders are terminal: 33 complete, 3 superseded (OG-r-2 executed and drained with two FAILs;
  OG-v-4 and OG-v-5 held on gates and never graded). Tally read from the last `<status>` tag of every order file.
- **L8:** 154 of 154 rows dispositioned; the fold reads 0 of 167 undispositioned. 106 dismissed (Z-C-S6..S8), 16 INERT
  graduated OPEN (Z-C-S9), 32 ARMED graduated (Z-C-S10): 23 disarmed on evidence, S36 disarmed with its cleanup
  open under W2-S6, and 8 stay ARMED.
- **L9:** three judgment criteria graded (Z-C-S11). OGC1-J1 PASS. OGO2-J1 FAIL and OGV3-J1 FAIL; both become cells
  below.
- **Adopted as the round's most useful act:** S57. The CVO's L8 found that the export materialises the whole result set
  (up to three full-size copies) and refuses AFTER allocating. That settles R-OG-22 without moving either contract
  number (section 3, R-4).

## 2. Outcome grades

0 of 8 FWDs was exercised: the two walkthrough cells (OG-v-4, OG-v-5) were closed unrun. A grade of HELD means the
components are built and only the gated walkthrough is missing. NOT_REALIZED means a measured defect would fail the
walkthrough even if it ran today.

| FWD | grade | why |
|---|---|---|
| FWD-1 (Menachem connects from his work Claude account) | HELD | Durable OAuth, principal cutover and browser OIDC are built and released (OG-a-1..a-3, OG-r-1). The connect-and-reconnect walkthrough is G-D, then G-F. |
| FWD-2 (accurate answers, masters kept separate) | NOT_REALIZED | The sealed question set cannot prove it: OGV3-J1 FAIL (no units question; both between-date questions resolve to NONE_QUALIFIED on one date). The grain of dim_position is undeclared and collides on the real snapshot (W6-S2). |
| FWD-3 (each person sees only their grant) | NOT_REALIZED | The guard, admin, alias and denial envelope are built (OG-z-1..z-4). But the top tier keys on an exact email at four call sites plus the token broker (W3-S9, S61, ARMED), which breaks C1 ("email is display/audit metadata only"). |
| FWD-4 (download equals what he can query) | NOT_REALIZED | The CSV route and browser paths are built (OG-x-1, OG-i-3). An export at contract scale exceeded the job cap on the host (OGR2-AC4, LIMIT_EXCEEDED), and S57 shows why. |
| FWD-5 (answers state scope, date, limits) | HELD | The closure contract (OGC1-J1 PASS) and snapshot semantics are built. Not exercised. W5-S6 (an effective page of 250, not 500) must be fixed before the truncation statements are graded. |
| FWD-6 (change or revoke access without re-setup) | HELD | The operator admin command is built (OG-z-2). The revocation walkthrough is G-D. |
| FWD-7 (existing users keep working) | NOT_REALIZED | The release is live and p95 moved -0.33 percent (W2-S10). But OG-r-2's capacity verdict is INSUFFICIENT at contract scale, and its AC2 grader is vacuous (S48). |
| FWD-8 (support and withdraw the pilot) | NOT_REALIZED | The acknowledged audit is built (OG-o-1). The runbook misdirects the operator at named moments (OGO2-J1 FAIL). |

Tally: 0 REALIZED, 5 NOT_REALIZED, 3 HELD, 0 DEFERRED.

## 3. Rulings

**R-1, the switchover sitting goes FIRST** (Andrew's call 2 = (a), record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_180xZ_CTO_O_FOUR_CALLS_BD_ROTATION_LATER_SWITCHOVER_A_NO_SCRUB_COMMIT_GATE_YES.md`).
`2.0.0_SA_COO~O` is the seat named in call 2's routing. Before Andrew sits down, it re-confirms the runbook's four
preconditions (a)-(d) in ONE message, because the S19 rewrite moved site Z's state. Then Andrew runs Parts A-D of
`org/missions/D6/NFRA/NFRA_OPALAI/deliverables/1.0.0_SA_CTO~O/ANDREW_SWITCHOVER_RUNBOOK.md`. The sitting unblocks
NFRA_OPALAI and NFRA_MCPORTAL, not an OPLGTW FWD. One output is OPLGTW's: Part D records which identity claims the
owner's sign-in carries (`oid`, or `sub`), and R-3 needs that value.

**R-2, on S45 (ARMED, this seat's; the gateway has no Elastic IP).** RULED: take the EIP. The remedy offered two
paths: an EIP, or a statement that no allowlist depends on the address.
- The in-repo census reads 0 dependents. `54.197.78.28` appears in 6 files (comp-find, corpus=all, 77,801 files
  scanned): 2 CONFIG evidence files and 4 DOC records. None is a `.tf` file, a security group or an allowlist.
- That census cannot see out-of-repo planes, such as an Entra conditional-access named location or a vendor
  allowlist. So the statement cannot be made from evidence this seat holds.
- Cost is held, not measured: under AWS public-IPv4 pricing, an associated EIP bills at the same hourly rate as the
  auto-assigned address it replaces.
- The cell (E8) declares `aws_eip` plus its association in the gateway module. It applies with `safe-apply` and a
  ledger entry, and needs no stop/start. Association moves the egress address once, then never again.
- Proof: `describe-addresses` shows an AssociationId on the gateway instance, and the plan shows the declared
  resource.
- The row stays ARMED until that close; this seat files the disarm row citing it.

**R-3, on W3-S9 and S61 (ARMED; the email-keyed tier is the "L4 security design" the rows name).** RULED here as a
cell under the CURRENT C1. No addendum and no re-sign are needed: C1 already says "Carry validated `tid` and `oid` in
signed principal context; email is display/audit metadata only", so the code is out of conformance and the contract
is not. The design the cell (E7) builds:
- (a) `resolve_tier` takes the principal and keys on `principal_key()` (`<tid>/<oid>`) only. Config carries
  `MASTER_ADMIN_PRINCIPALS`, never emails, for every set `resolve_tier` reads. Five sites move: `app/tier.py:69` (the
  signature), `app/guard.py:75`, `app/integrations/base.py:143`, `app/token_broker.py:154` and `app/tools.py:124`.
  `config.py:233-235`'s SECURITY-CRITICAL comment is corrected to match `context.py:41-47`.
- (b) A principal with no `tid`/`oid` resolves to the lowest tier. There is no email fallback.
- (c) The admin principal's value comes from R-1's Part D record, so E7 is cut after the sitting.
- (d) Negative arms: a genuine token with the admin email but a different `oid` is NOT master admin, and the broker
  mints it no admin scope. The admin principal with a changed display email stays master admin.
- (e) Blast radius, pre-read at the cut: for every principal in the access-state table and the last 14 days of audit,
  the old tier equals the new tier. The only allowed delta is the fixture. It is a narrow release under never-widen
  halves (the CTO's half plus a second, non-acting half).
- (f) Out of scope and NAMED by the cell's first criterion, not moved: email sets that `resolve_tier` does not read,
  for example the `/sprint` roster (OG-s-1) and the `email_deny` record (C2 makes it denial-only by design).

**R-4, on R-OG-22 (the cap question this seat owed at L4) and S57.** RULED: the contract numbers stand (250,000 rows,
50 MiB, the 256 MiB job cap). S57 confirms R-OG-22's third branch at the source: peak RSS tracks the REQUESTED size
because the export materialises the result up to three times and refuses after allocating. The remedy is the export,
not the contract (E5). OG-r-2 then re-cuts against the unchanged contract with the R2-b grader repair (E6). If E6 still
measures INSUFFICIENT with a streaming export, that measurement is the input to a PRD revision. Nothing is revised
before then.

**R-5, on W3-S5 (INERT; a DCR registration never expires).** C1 names no lifetime, so this is the ONE L4 addendum this
seat owes for round 2. It adds a C1 clause: a registration with no live refresh family expires after a fixed idle
lifetime, via the table's TTL. It is a CONTRACTS change, so `3.0.0_SA_CVO~O` signs the ratified-text half at the new
bytes before E9 is cut (LIMB 6 refuses the newly-added order until then). E9's other two items do not wait on it.

**R-6, the issuer's ARMED rows**, all carried into the list below with owner `2.0.0_SA_COO~O`:
- W2-S8 (no eol rule for 7 deployed extensions) goes to E10;
- S43 (out-of-repo evidence: the `nfra-oplgtw-handoff` tree) goes to E10, which restores it to the repo or restates
  each citation as ABSENT;
- W2-S10 and S49 (regrade AC6 on the 09-11..09-17 window, per R-OG-23A) go to E6;
- S48 (the vacuous `_cap_respected`) goes to E6 via R2-b @94b0c19f27.

**R-7, the gates for the walkthroughs.** Per the order files' close text: Andrew approved G-C and G-E on 2026-09-28,
and G-D is his walkthrough after this device's reboot.
- G-C's closing owner is `1.0.0_SA_CTO` (decomp gate table). This seat writes the G-C record, with the identity
  evidence from `0.7.0_AE_CloudOps`, before E1 is spawned.
- G-E's activation runs through OG-z-2 by an authorized operator. G-F is the pilot walkthrough itself.

## 4. THE ENRICHMENT LIST ROUND 2 CUTS -- ONE issuance by `2.0.0_SA_COO~O`

The thread is FWD-1 end to end: a signed-in person asks and downloads through the live gateway. Round 2 exercises it.

0. **Before the issuance: R-1's precondition message and Andrew's sitting.** Neither is a cell.
1. **E1, OG-v-4 re-cut unchanged** (WORLD; FWD-1 and 3..8, controlled identity). Gated on G-C (this seat's record)
   and G-D. Cut after E3. It carries the round's **JUDGMENT criterion on a WORLD cell**: `3.0.0_SA_CVO~O` reads the
   walkthrough record and grades each FWD's ACCEPT sentence against what the person OBSERVED (screen, downloaded file,
   refusal text), never against server logs. PASS only when every ACCEPT clause has an observed line.
2. **E2, OG-v-5 re-cut** (WORLD; FWD-1 and 8, the pilot). Behind E1. G-E is approved; activate through OG-z-2. G-F is
   the owner-and-member walkthrough.
3. **E3, runbook text repair** (LOCAL; OGO2-J1). Correct the four cross-references (:47 to 6.1, :49 to section 8, :115
   to the right grant section, :11's section count) and rewrite 7.2 against the live release (6a98a0553a, with the
   valid rollbacks fe94911257 and 110d93fb73). OGO2-J1 is re-graded at L9 on the new bytes. It lands before E1,
   because the operator follows this text during the walkthroughs.
4. **E4, sealed question set v2** (SERVED reads; FWD-2; OGV3-J1).
   - At least one units question: quantity against value, sign, scale.
   - A real two-date alignment on the newer qualified date (W6-S5).
   - Declared grains for dim_position, dim_balance and dim_asset, with the colliding key handled per C3 (W6-S2).
   - A re-seal into SSM on the d5af54a90a pattern.
   - Its close run asks the sealed questions through the live gateway and compares the answers with the seal: that run
     is FWD-2's exercise. OGV3-J1 is re-graded at L9.
5. **E5, streaming export** (LOCAL build, SERVED narrow release; S57, R-4, W5-S6). Refuse BEFORE allocating, never
   hold more than one representation of the result, and count the 500-row cap once. Proof: peak RSS stays flat across
   two export sizes one order of magnitude apart.
6. **E6, OG-r-2 re-cut** (WORLD, on-host; behind E5). It carries R2-b (`_cap_respected` reads RSS on BOTH branches,
   S48) and regrades AC6 on the 09-11..09-17 window (W2-S10, S49). The contract is unchanged (R-4).
7. **E7, tier re-key on the principal** (LOCAL build, SERVED narrow release under never-widen halves; W3-S9, S61, R-3).
   Cut after the sitting's Part D record.
8. **E8, the gateway EIP** (WORLD; S45, R-2). `safe-apply`, ledger entry, no stop/start.
9. **E9, auth hardening** (LOCAL, rides E7's release).
   - The DCR idle lifetime (W3-S5), after R-5's addendum is signed.
   - W3-S11: `/ms/site_children` authenticates before it validates parameters.
   - W3-S18: the browser OIDC routes join `AUTH_PATHS` (`app/ratelimit.py:42`).
10. **E10, the batch cell** (LOCAL).
    - `.gitattributes` eol rules for the 7 extensions (W2-S8).
    - S43: restore or restate every out-of-repo citation.
    - The test hygiene rows: W3-S2 (the suite writes the tracked audit.jsonl), W3-S6 (the frozen monotonic clock), W6-S9
      (the non-deterministic sweep).
    - The W2-S6 probe cleanup: 8 fixture items in the production access-state table, a literal key list the probes
      wrote. It is CARDED to Andrew and not executed by the cell: Agent Autonomy puts deletes in a production store
      under human confirmation.
11. **E11, the Schwab marker storm** (SERVED; S4, S5, W4-S12). The first cell READS only: re-measure the PUT count
    per 08335338 marker date and the dispatch/refusal counts over a fresh 14-day window. The remedy cell is cut from
    that read. It moves when the 49F chain dispatches, so it needs the never-widen sign-off with the writer census of
    `meta/complete/`. Lane per CLAUDE.md rule 13.

**Close run:** E1 and E2 walkthrough records at HEAD, plus E4's live sealed run. Those three exercise all eight FWDs.

**Subtracted from round 2 and routed, not cut:**
- S19 (the halt gate scans a missing inbox in a linked worktree): fabric tooling, `0.0.0_AB_MSTR~Z`.
- W1-S9 (the naming limb REFUSEs PRD-fixed role names): LGIC_ENFORCE's owner.
- W4-S10 (`infra/aws/lambda/ci/build-and-upload.sh` aborts under `set -e`): the estate build script's CloudOps owner.

## 5. What this analysis does not do

- It does not write the G-C record or R-5's addendum. Both are owed by this seat, before E1 and E9 are cut.
- It does not measure the out-of-repo allowlist planes (R-2 takes the EIP instead).
- It does not delete the probe fixtures (E10, carded to Andrew).
- It does not touch NFRA_MCPINDEX's Schwab tools, which stay behind this project's thread.
