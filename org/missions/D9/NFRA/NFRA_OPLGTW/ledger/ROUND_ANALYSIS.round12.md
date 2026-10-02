# NFRA_OPLGTW -- ROUNDS 3-12 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-02 ~01:4xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (msg 28125).
- The slug: `REMEDIATION_v2.md` @3776b394e3. Compiled by `ADJUDICATION_v3.Z.md` Z-C-S12/S13; graded by Z-C-S14.
- The channel holds 0 of 270 undispositioned rows.
- Every order is terminal except OG-g-1 (pending, held on G-C) and OG-v-7 / OG-v-8 (staged on G-C and G-D), carried by
  ruling 28091.
- Grade tokens: `REALIZED | NOT_REALIZED | DEFERRED | HELD`.

**Written under** `/self-drive OPALAI_MCP_SITEZ` (arming record @80102ed73d). **Issuer: `2.0.0_SA_COO~O`.** ONE
issuance (section 5), under the next free round label. **PRD amended to v1.5 in the same commit** (section 4).

**Priority this analysis applies** (Andrew-direct ~17:4xZ 2026-10-01, msg 28000): Opal-employee MCP use first.
FWD-1's user (Menachem, from his WORK Claude account) is exactly that. **MDPF_TAXSMA stays out of this seat's scope**
outside the one release Andrew lifted it for (section 3c).

---

## 1. What rounds 3-12 did

Most of rounds 3-12 served OTHER projects' outcomes through this host, which C7 says are graded there, not here:
- the NFRA_TRNSPT dependency workstream: transcript and mail tools, the `/hx` routes, bearers and secrets, the ALB
  rule, and the mail listing;
- the opal-gateway release train for MCPINDEX, MCPMSP and MCPORTAL (slots 1-5);
- the Tax SMA route (OG-tt-1, OG-tr-1).

Toward this project's OWN endpoint:
- **OG-t-2: tier auth released.** The principal tier is keyed on `tid`/`oid`, retiring the email-keyed top tier
  (W3-S9 / S61) that made FWD-3 NOT_REALIZED in round 1.
- **OG-x-3: streaming export released.** This answers the job-cap overrun (OGR2-AC4) behind FWD-4.
- **OG-n-1: Elastic IP** 3.214.118.242 (R-2).
- **OG-m-3: chain-log classifier.**

Live: `opal-gateway` `3a7d6a7dc8`.

**L8:** 26 rows dismissed (Z-C-S12) and 11 graduated (Z-C-S13). Adopted as stated.
**L9 (Z-C-S14):** **OGTX2-J1 PASS.** The four meetings are the spec's four, and REACH covers three meetings where
Andrew is an invitee and not the organizer. OG-tx-2's AC1 FAIL (3 of 4) is row Z-S43.

## 2. Outcome grades

The walkthroughs (OG-v-7 controlled, OG-v-8 pilot) are the instruments for FWD-1..8 and have not run. HELD means the
components are built and released and only the gated walkthrough is missing. NOT_REALIZED means a measured defect would
fail the walkthrough today. Grades marked *carried* were not re-measured this L10.

| FWD | grade | why |
|---|---|---|
| FWD-1 (Menachem uses Schwab from his work Claude account) | HELD | OAuth, principal cutover and browser OIDC are built and released (OG-a-1..a-3, OG-r-1, OG-t-2). The walkthrough waits on G-C (OG-g-1 evidence, whose seat is not registered, section 5 item 1), then G-D. |
| FWD-2 (accurate answers, masters separate) | NOT_REALIZED | Z-W10-S1: `dim_position` and `dim_asset` collide under the declared grain on all 8 snapshots. Ruled in 3a. |
| FWD-3 (each person sees only their grant) | HELD | The email-keyed top tier, round 1's defect, is retired by OG-t-2. The guard, admin, alias and denial envelope were built in round 1. Not re-measured here; the walkthrough grades it. |
| FWD-4 (download equals what he can query) | HELD | Round 1's cap overrun is answered by OG-x-3's streaming release. The contract-scale CSV is graded by the walkthrough (A7). |
| FWD-5 (answers state scope, date, limits) | HELD *carried* | Round 1's state. W5-S6 (an effective page of 250, not 500) is re-read in the item-6 batch. |
| FWD-6 (change or revoke without re-setup) | HELD *carried* | The admin command is built (OG-z-2); the revocation walkthrough is G-D. |
| FWD-7 (existing users keep working) | NOT_REALIZED *carried* | OG-r-2's capacity verdict was INSUFFICIENT at contract scale, before the streaming export. Re-measured in item 5. |
| FWD-8 (support and withdraw the pilot) | NOT_REALIZED *carried* | OGO2-J1 FAIL: the runbook misdirected the operator. It is re-graded at L9 against the current runbook (item 6). |

**Tally: 0 REALIZED, 3 NOT_REALIZED, 5 HELD, 0 DEFERRED** (round 1: 0 / 5 / 3 / 0). Two of round 1's defects are
retired by released code.

**The critical path to REALIZED** is one chain:
1. G-C evidence (OG-g-1);
2. this seat writes the G-C record;
3. G-D, Andrew's controlled walkthrough (OG-v-7, after S63's seal of record);
4. OG-v-8, the pilot with Menachem.

## 3. Rulings on the slug's rows

### 3a. Rows owned by `1.0.0_SA_CTO~O`

| row | ruling | reason |
|---|---|---|
| **Z-S43** (the Research Team Meeting refused 403/3003: Andrew is not an invitee) | **Reach is by INVITATION** (ruling 28043). Listed as Andrew's act, or the meeting organizer's. After it: re-run OG-tx-2's REACH arm on that one meeting. **No application route.** | The bound-identity design is confirmed on 3 of 3 meetings. An application route is a tenant-wide transcript read. |
| **Z-W10-S1** (Schwab position and asset grain collide; one more contract column makes each colliding snapshot unique, CANDIDATE only) | **MEASURE, then adopt or refuse.** A LOCAL cell runs the candidate grain (the declared columns plus the one candidate column named in `GRAIN_DECLARATION.json`) over EVERY available `dim_position` and `dim_asset` snapshot, not only the 8. It also reads why 5 of 10 colliding keys carry a blank component. **Adopt** into C3 by addendum only if the candidate is unique on every snapshot AND the added column is never blank. Otherwise the **C3 refusal stands**: the quantity-against-value question is answered as a refusal, and FWD-2 is graded with that refusal as correct behavior. | A grain inferred from 8 snapshots is a sample. C3 already makes "refuse on a non-unique grain" the safe default, so neither branch serves a wrong number. |
| **Z-W15-S23** (the gateway audit has no byte count for `read_meeting_transcript` and records email, not the principal key) | **Cut into the next gateway release** (item 2): `app/audit.py` adds returned-bytes and the principal key. Email stays as a display field. | The principal cutover (OG-t-2) is live, so an audit keyed on email no longer identifies the principal the tier decision used. |
| **Z-W13-S2** (a burst dispatch that aborts before writing a chain log reads UNKNOWN, not ABORT) | **Placed with the 49F ADVI chain's owner** through `0.0.0_AB_MSTR~Z`'s tool-owner routing register. Not cut here. | The chain is not this project's surface. OG-m-3 only reads its log. |
| **Z-S23** (`safe-merge.sh` carried a peer's uncommitted edit into a drain) | **Placed with `safe-merge.sh`'s owner** through the same register. Remedy: refuse a drain whose merge commit would carry a path outside the branch's diff. | Shared tooling, not this project's. |

### 3b. Rows owned by `2.0.0_SA_COO~O`

| row | ruling |
|---|---|
| **Z-S41** (ARMED: the Tax route's `_OTHER_ROUTE_BEARERS` omits the two `/hx` bearers) | See 3c: **the fix is MDPF_TAXSMA's module change**, shipped by this host's next release. Until then any bearer rotation compares DIFFER first (the standing check OG-tr-1 ran). |
| **Z-W13-S5** (ARMED: `DATA_CATALOG.yaml` stored CRLF on 1,614 of 1,614 lines; the naming limb refused the line-ending-only renormalization) | **Fix the gate, not the file's path.** The naming limb admits a diff that is empty under `--ignore-cr-at-eol`. Route the gate change to its owner (LGIC naming gate, laptop `2.0.0_SA_COO~G`) through `0.0.0_AB_MSTR~Z`. The renormalization lands after, then `ITEM_A_BLOCKED.md` applies. No override commit. |
| **Z-W12-S7** (the operator upload client expires ~2026-10-18) | **A dated act, listed for Andrew** (his interactive authorization-code exchange). The issuer names the session and records the new expiry. Due before 2026-10-15, leaving a 3-day margin. |
| **Z-W12-S8** (an ACTIVE `email_deny` POLICY record on write-capable person #1; 3 synthetic partitions) | Item 4: read the deny record's origin. Remove it under its own halves or record why it stays. Delete the 3 synthetic partitions or record them as fixtures. |
| **Z-S34** (the host roster log line reports 1 pair; 2 are held) | Item 2, with Z-S32. |
| **S63** (phase 1's seal of record lost its salt) | Item 4, before OG-v-7: record which seal is of record and mark AC8's probe MUTATING. |

### 3c. MDPF_TAXSMA boundary (correcting this seat's msg 28026)

`app/taxsma_workbook.py` is MDPF_TAXSMA's module: its bytes matched the laptop spec, sha256 `6acc3e8c...`, at OG-tr-1.
Andrew's TAXSMA exclusion was lifted for ONE release, now closed.
- **So this host does NOT edit that module.** The Z-S41 tuple fix goes to the MDPF_TAXSMA owner (laptop) as a spec
  change through `0.0.0_AB_MSTR~Z`. This project's next release ships the new module bytes verified by sha against
  their spec, as OG-tr-1 did.
- Moving `OG_TAXSMA_WORKBOOK_IDENTITY` from the deploy shell to the host (item 2) IS this project's: it is
  `deploy-to-ec2.sh` plumbing that touches no TAXSMA byte.

### 3d. Carried into this project by earlier rulings

| item | placement |
|---|---|
| Z-W21-S19 + ETFS_RIVALS-W5-S3 (the TF root does not plan, including from a FRESH worktree) | Item 3. |
| Z-W19-S13 (three copies of the contract) | Item 2: `org/standards/NFRA_OPLGTW_CONTRACT.json` is the single source. The release suite fails on a differing `deploy/` or grant-writer copy, and the release removes the stale host `deploy/` file. |
| Z-S32 (`.env` shape; never shell-source the host `.env`) | Item 2. |
| C7 text drift (`read_email` fields) and the `/ms` structure-only tension | **Amended in PRD v1.5, this commit** (section 4). |

## 4. PRD v1.5 (wording only; no ENDPOINT change)

- **C7 mail tools:** `read_email`'s `$select` is listed as the six fields shipped since OG-rl-1. The text named 4 and
  the build has 6, adding `bccRecipients` and `hasAttachments` (read at `3a7d6a7dc8` `app/tools.py`).
- **C7 headless routes:** the `/ms/*` structure-only rule holds for the generic routes. `GET /ms/taxsma-workbook` is
  named as a separately guarded route on Andrew's word, not a widening, and its spec is MDPF_TAXSMA's.

Under the proportionate sign-off clause (CLAUDE.md rule 27, L4-R), a wording change re-opens no half and withholds no
delivery. Only an ENDPOINT change re-signs, and there is none.

## 5. THE ENRICHMENT LIST THE NEXT ROUND CUTS (one issuance, `2.0.0_SA_COO~O`)

1. **G-C evidence (OG-g-1), the critical path.** OG-g-1 is issued to `0.7.0_AE_CloudOps~OG`, which is NOT REGISTERED.
   `0.0.0_AB_MSTR~Z` seats it, or the issuer re-issues it to a live CloudOps lane; Andrew named CloudOps the default
   test admin (record @768e6df290). On its evidence this seat writes and closes
   `deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md`. G-D (Andrew's walkthrough) then follows.
2. **The next gateway release (WORLD).**
   - Payload:
     - Z-W15-S23 (audit bytes and principal key);
     - Z-S32 (the `.env` shape) and Z-S34 (the roster log count);
     - `OG_TAXSMA_WORKBOOK_IDENTITY` moved host-side;
     - Z-W19-S13 (the single contract source, with stale host `deploy/` removal);
     - MDPF_TAXSMA's corrected module bytes for Z-S41, IF they have landed by the cut, verified by sha against the
       laptop's spec. If they have not, the release does not wait for them.
   - Cut on the live ref.
   - Never-widen halves: CTO + COO, and CVO for any capability change.
   - Read-back: `.env` keys before and after with nothing lost, host equals artifact, and every existing route's
     no-bearer probe unchanged.
3. **TF root hygiene** (Z-W21-S19 + W5-S3).
   - Re-measure first: OG-pr-1 created the `gateway/*` secrets.
   - Acceptance: `safe-apply` plan on the committed root, from a FRESH linked worktree, with 0 errors and no pruned
     copy. The closing commit hash goes to `0.0.0_AB_MSTR~Z` for the register.
4. **Walkthrough preparation:** S63 (the seal of record; AC8 probe MUTATING) and Z-W12-S8 (the deny record and the
   synthetic partitions). Both land before OG-v-7 runs.
5. **FWD-7 re-measure (SERVED, read-only on the live host):** OG-r-2's capacity read at contract scale through the
   streaming export on `3a7d6a7dc8`. It runs off-hours, inside the job caps, and moves nothing.
6. **Batch and judgment re-grades:**
   - W5-S6 (the effective page size) re-read;
   - OGO2-J1 re-graded at L9 by `3.0.0_SA_CVO~O` against the current runbook;
   - the 9 OPLGTW red tests named in NFRA_MCPINDEX's packet (section 4), repaired or each named with its reason.
7. **Z-W10-S1 grain measurement** per 3a (LOCAL).

**Stated dependencies, not cells:**
- G-D and OG-v-8 wait on G-C, then on Andrew and Menachem.
- Z-S43's re-run waits on the invitation.
- Z-W13-S5 waits on the gate owner.
- Z-S41 waits on MDPF_TAXSMA.
- The D9 -> D6 move lands before this issuance (section 6).

## 6. The D9 -> D6 move

Andrew agreed the move to D6 at round close (~15:51Z, record @53ad7cb452; CVO verdict 27494). This analysis is that
round close.
- This seat lands the move for BOTH NFRA_OPLGTW and NFRA_MCPINDEX in ONE commit before either next issuance: the
  members line, the tree paths, the unpinned live references, and redirect READMEs.
- The laptop row-owner removes the D9 rows.
- `2.0.0_SA_COO~O` waits for the move-commit message.

## 7. What this analysis does not do

It deploys, applies and flips nothing. It re-measured only:
- the order statuses of OG-t-2, OG-x-3 and OG-g-1;
- `0.7.0_AE_CloudOps~OG`'s registration;
- `read_email`'s `$select` at `3a7d6a7dc8`.

Every other figure is the slug's, the CVO's grade record, the investigation rows' or round 1's, as cited.
