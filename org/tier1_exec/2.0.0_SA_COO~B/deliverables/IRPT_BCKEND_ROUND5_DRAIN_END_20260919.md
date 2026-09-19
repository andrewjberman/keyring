# IRPT_BCKEND -- ROUND 5 DRAIN-END READ AND L8 HAND-OFF (2.0.0_SA_COO~B, 2026-09-19 ~02:1xZ)

**Measured on the shared tree after the last drain (`9b07b7b7ea`, rte-6's instance pin repair) and the IB-rte-2 close.** Terminality
is read from proof instances at HEAD, never `<status>`: `surprise-row-gate._open_tos_for_project('.', 'IRPT_BCKEND')` -> **open = [],
total 61** once rte-2's `superseded` lands (before it: open = [rte-2 staged] -- the reader's own line names five orders terminal by a
VALID instance whose status word is not terminal: rt-6, rte-3, rte-4, rte-6, rte-7; four of those carry a FAIL and stay OPEN BY
THEIR FAIL for the CTO's analysis, which is the spine's shape, not a defect). No `wk-irpt*` worktree or branch remains (0). ONE IRPT
sentinel in `.open_deploys/` at HEAD: `irpt-bckend-ib-rte-3-lgic-firm-buckets.json`, OPEN and RED, correctly (NEVER-2; the half-landed
apply is escalated, not worked around). Push state: LOCAL; origin/CLOUD `74ced0a3c6` (ls-remote read 02:0xZ).

## 1. The round's orders -- 2 PASS, 4 truthful FAIL, 1 closed SUPERSEDED (issuer re-grade on the shared tree with `--governing-order`)

| order | owes | assignee | mechanical | drained @ / instance blob | what it proved |
|---|---|---|---|---|---|
| IB-rte-1 | Andrew call 2: the bounded test principal DECLARED + packet | WK~1 | PASS | 01ba67fe65 / `6460664555` | the identity plane is `opal-portal-authorizer`'s RS256 JWT over `opal-users-v2` (not Cognito); K1 = ONE row reusing `abby_horton`'s live 49financial entitlement, K2 an ephemeral token, K3/K4 NOT NEEDED; 6 of 263 identity-plane writers; packet blob `3d9f57335b`; both halves signed (COO @a0f05dda0c, CTO @482b2c627e). Rows W1-S21 (advisor ids are raw ownership-map keys), **W1-S22 (EVERY live FIRM_ADVISOR request refused `UNPROJECTED_GRANT` -- the finding that shaped the round)**, W1-S23, W1-S24 (cottonwood termination unpopulated 260 of 260) |
| IB-rte-2 | the principal CREATED, EXERCISED, DELETED | AE `~N` (never spawned) | -- | SUPERSEDED for round 5 (this seat, 02:1xZ) | never handed: gated on rte-6, whose arm (d) FAILED on a POLICY outside this round's write surface (W1-S27, at the CTO); handing it would spend the bounded identity measuring a refusal already measured. Both halves are hash-bound to the packet, not the round, and CARRY; re-cut in round 6 once the policy ruling lands (LD-0521: closed rather than deadlock this round's L10 on another seat's L4 question -- the IB-rtd-7 / OG-r-2 precedent) |
| IB-rte-3 | Andrew call 1: the two LGIC firm buckets CREATED EMPTY | WK~3 | **FAIL** (a PASS; b/c/d/e FAIL) | 8a1b923c1f / `0c1e7b5863` | names built by `name()` 2 of 2; declared registry-derived (`for_each` over `scopes.json`) after the naming gate REFUSED a literal copying 49financial's idiom (W3-S41); plan 10/0/0; **8 of 10 landed and the per-firm Deny fence, applied with an EMPTY exemption list, locked out the applying identity** (W3-S43, ARMED this seat); `bucket_provisioned` stayed false so the ds-precommit fence does not refuse the new names (W3-S42); host `i-02448edb624a7a7cf` STOPPED (W3-S44); ledger + sentinel OPEN RED |
| IB-rte-4 | W1-S20/W2-S59: served members declared from TRUE sources, no third copy | WK~4 | **FAIL** (7 of 9) | 162b657207 / `a37e4b6677` | `staged_from` pinned-blob mechanism in `build-and-upload.sh` + 48 declarations in `lambda-source-map.json`; served zips verified member-for-member; **2 of 9 functions carry members with NO source anywhere** (W4-S34/S35) -> the CTO's L4 ruling @457cf494c6: ROUND 6's FIRST cell, measure-then-branch, never labelled before the diff; 3 UNRESOLVED members get the same treatment; W4-S38 to the ci owner |
| IB-rte-5 | W2-S57 residual: manifest-history census, FWD-7's five arms on the controlled clock | WK~2 | PASS 16 of 16 | 589610f663 / `cb2a1367f5` | rtd-2's Q2 CLOSED at `k = 0 of 5` over 84 of 84 manifest-object versions with a planted-defect mutant; FWD-7's five arms driven 5 of 5 against the served `CodeSha256`; the fresh-dispatch case NAMED-BLOCKED (every firm `REFRESH_NOOP_SAME_FRONTIER`, `runner_script()` hard-codes `--upload`, no dry-run) -- a design finding for the CTO |
| IB-rte-6 | W1-S22: the served path admits a projected advisor grant (cut mid-round) | WK~1 | **FAIL** (a/b/c PASS, d FAIL) | be2fa1dd19 + pin repair 9b07b7b7ea / `7a8c58ec1b` | 13 of 13 entry points wired through `served.Entry.enforcer_for` with the VERIFIED tenant (AST census, mutant fires); **my REC (a) `dim_identity_crosswalk` resolves 0 of 22,646** (W1-S25, CTO); the face's own alternative `dim_account_xref` seam resolves 17,895 of 22,646, `abby_horton` 21 of 43; 7 of 7 functions deployed under ledger, `CodeSha256 == built`; **the same real request still reads `UNPROJECTED_GRANT` because `enforce.py`'s unedited all-or-nothing policy refuses the whole grant at 79 pct coverage** (W1-S27, BLOCKING, CTO); two more untracked-source packaging gaps (W1-S26, this seat); inflection + cottonwood ownership maps EMPTY at the cut (0 of 0, VACUOUS) |
| IB-rte-7 | the CTO's registry-deadlock step 1 (cut mid-round on 98087/98090) | WK~3 | **FAIL** (8 of 9 arms) | 0aad91ed59 / `060bf0df60` | the `lgic_firm` selector re-keyed on a drafted registry field `bucket_managed_by` OR the unflipped flag, addresses unchanged, no `moved` block; validate precondition rc=0 (scope rows have NO field-closure check -- a registry finding); PLAN-1 0 differences; PLAN-3 mutant `0/0/10 to destroy`; the delta drafted for the CTO (`registry_delta_ib_rte_7.md`); **a live plan cannot refresh under the W3-S43 lockout, and the only completed plan shows `versioning` + `bucket_policy` TAINTED for both firms -- residue of the half-landed apply** (W3-S45, ARMED this seat); the delta's isolated effect is exactly the three exemption ARNs per policy |

Judgment criteria RECORDED and never self-graded: the AC2 row of rte-1, rte-3, rte-4, rte-5, rte-6 and rte-7 (six) -- **the CVO's at L9.**
S56's bar held on every instance (the issuer's bare-citation grep at each drain).

## 2. The channel -- L8's input

`INVESTIGATION_v1.md` at HEAD: **269 rows across every json fence** (the first fence alone reads 245 -- a `[0]` parse under-reads).
**17 rows carry `surfaced_at >= 2026-09-18T19:02Z`** (the round-5 issuance @391e4ad948): W3-S41..S45, W1-S21..S27, W4-S34..S38. The
CVO's watermark decides which are new to it. By standing: **ARMED on this seat (10):** W3-S42, W3-S43, W3-S45 (the bucket incident --
disarm when steps 2-5 land, none of them this seat's act), W1-S21, W1-S22 (served by rte-6's wiring; the policy half is W1-S27), W1-S24,
W1-S26, W4-S34, W4-S35, W4-S38 ("to route" -- the ci owner). **ARMED at the CTO (2):** W1-S25, W1-S27. **INERT (5):** W3-S41, W3-S44,
W1-S23, W4-S36, W4-S37. Carried ARMED from earlier rounds unchanged: W4-S28, S56 (the CVO's), W1-S20 / W2-S59 (served by rte-4 for 7 of 9).

## 3. FWD state after round 5 (for the CTO's analysis; the grade is the CVO's)

- HAVE (new this round): the identity plane measured and the test principal DECLARED under both halves; the served path's refusal
  CAUSE measured to a single policy line with a 79 pct bridge deployed behind it; two firm buckets EXIST (locked, empty, tainted);
  48 served members declared from true sources; FWD-7's five arms driven; the manifest history certified clean; the registry deadlock
  measured on both surfaces and its Terraform half repaired at HEAD.
- LACK (each named with its owner): **(i)** the entitlement policy under a partial projection -- W1-S27, `1.0.0_SA_CTO` at L4, REC (a)
  admit-and-disclose; **(ii)** Andrew's `delete-bucket-policy` on both buckets (step 4, the gating human act); **(iii)** the CTO's registry
  commit (steps 2-3, delta drafted); **(iv)** the re-apply that clears the taint and lands the last 2 of 10 (rte-3's re-hand, step 5);
  **(v)** the test principal EXERCISED (rte-2's re-cut, after (i)); **(vi)** the no-source members (round 6's first cell, @457cf494c6,
  population now W4-S34/S35 + W1-S26's two functions + the 3 UNRESOLVED); **(vii)** IB-rtd-7's port (still SUPERSEDED: needs (ii)-(iv),
  both halves, the FNTEND reader cell); **(viii)** the FNTEND per-firm as-of carrier at L4; **(ix)** a fresh SSM dispatch driven from cold
  (rte-5's finding: a frontier advance or a dry-run flag); **(x)** inflection/cottonwood ownership maps are EMPTY, so every advisor-facing
  FWD is VACUOUS for two of three firms until their producers populate them -- named, not graded here.

## 4. Reserved and parked

- Nothing RESERVED surfaced this round. Andrew's two approvals (17:3xZ, @af794c77e3) are executed as far as the estate allowed: the
  buckets exist; the principal is declared and signed, not yet exercised.
- `0.4.0_DS_ClientPlatform~X` holds no round-5 order; `0.7.0_AE_CloudOps~N` was never spawned (rte-2 never left `staged`).
- The Rule 22 law relay (97970) still reaches the DS/AE lanes through this seat's next GO (LD-0529).

**L8:** this file, at `org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND5_DRAIN_END_20260919.md`, is the hand-off; the
channel compile and its watermark are `3.0.0_SA_CVO`'s; the ONE slug to `1.0.0_SA_CTO` follows L9; the CTO's round-5 analysis is what
this seat recuts from, in ONE issuance -- round 6 is not cut before that slug (LD-0521).
