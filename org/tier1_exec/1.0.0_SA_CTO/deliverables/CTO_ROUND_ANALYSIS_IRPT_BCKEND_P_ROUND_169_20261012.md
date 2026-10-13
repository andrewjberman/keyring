# CTO ROUND-169 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering the round-168 L10 slug (2026-10-12 ~23:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `surprise-channel/remediations/REMEDIATION_v45.md` @0827bac92d (3.0.0_SA_CVO msg 6659), on
the drain packet `deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_168_P_DRAIN_END_20261012.md`. **No PRD addendum.**

## 1. Where it stands

The claim-by-status reader is LIVE on `irpt-performance-adapter` (`abep4h7R...`, 22:35:06Z), released under the pair as amended
(CTO half Amendments 1 and 2): digest, plan and 0 TypeError measured; the nine kept refs refuse identically before and after (import
smoke). The served change is orion only (SI 750, YTD 76, QTD 7, 1Y 106); the 49F row was struck (this seat's error, Amendment 2).
**The changed path has not run on one live answer** (row D2-S114, owner this seat): the function computes only for Inflection, and
`2.0.0_SA_COO~D2`'s walker could not reach an Inflection client.

## 2. Ruling on D2-S114: an on-demand act, not a wait

Rule 27 L2: no FWD is a wait. The act exists and is small: **`/ui-walk` gains a `--firm "<option>"` flag that selects the header's
Firm option before the client search**, so a walk reaches an Inflection client's Performance tab. No identity is minted and no
selection is written by hand: the walk's own page creates the selection, as every 49F walk did. The organic wait is NOT qualified
with Andrew's word, because a seat can drive it.

## 3. ENRICHMENT LIST for round 169 (~P, ONE issuance; each build order at most three mechanical criteria)

1. **The walker's `--firm` flag** (the `/ui-walk` engine): selects the header Firm option by its visible label, fails loud if the
   option is absent, and is proven by one walk that lands on an Inflection client's Performance tab (screenshot read). Grant on the
   engine file only if `owned-paths-validate` finds no other live order naming it.
2. **The live read that closes D2-S114:** one walk with `--firm Inflection --performance-state` on one Inflection client; the
   answer's claim and its two counts compared with the reader's offline prediction for that account at the pin; the function's
   `irpt_retained_phases` line shows a computed path (not `refused:*`). No client name in any file or message; the ref id only.
3. **Carried, unchanged:** C-VALUEFACTS (`bd_adapter.py` rename built; its APPLY waits until the portal reader is on PROD, which
   rides Andrew's held promote `e7f2`); the DSGN_IRPTV1 fixture cell (row D2-W63-S1, routed @5f3be4e3da).

## 4. Acts only Andrew can do

None new for this project.

-- 1.0.0_SA_CTO~DELL2

## 5. Row D2-S116: Inflection Performance answers fail (client-facing), and NO rollback of IB-pr-487 (2026-10-13 ~00:4xZ)

- **Measured by this seat:** `irpt-performance-adapter` log since 2026-10-13T00:00Z: "not authorized to perform: s3:ListBucket on
  resource opal-data-inflection with an explicit deny in a resource-based policy". The bucket's `DenyForeignFirmPrincipals` admits
  `role/*-inf-*` and a named list; `irpt-performance-adapter-role` is in neither. The role's own policy, the table key's policy
  (root delegation only) and the role (no boundary) allow the DynamoDB/KMS reads; the issuer's first read (DynamoDB at
  pointer_get) was wrong.
- **Not caused by IB-pr-487:** `holdings_gold.py` 361c44fa9d..05219b8444 is 31+/7-, all claim logic, 0 lines naming S3, a bucket,
  a prefix or a list; the zips differ in that 1 of 71 members; the ListBucket is `partition_dates()` (`:154`) on a bucket the
  caller passes, and `opal_naming.address("irpt","inflection","gold",...)` resolves to `opal-data-inflection`. The issuer's
  CloudTrail read: 0 bucket-policy events on `opal-data-inflection` since 10-11. The live version before ours (`kMB8xCI9`,
  14:11Z) is ADVI_FIRMBKTS act 4's build (ledger `20261012T1340Z_advi-firmbkts-fb-f-11-act4-irpt-leg-20261012_deploy_completion.md`);
  no Inflection request ran 14:13Z-22:35Z, so timing cannot split the two. **Ruled: no rollback** (it restores act 4's build and
  the same deny; Branch B's triggers are not met). dell1's CTO (msg 4588) read the cause as ours; the evidence above is sent back,
  with the ask that dell1 act or the laptop cluster lead rule ownership.
- **The fix, whoever owns it:** the estate pattern (`holdings-performance/iam.tf:7-21`) -- a firm-scoped Inflection read principal --
  or act 4's ledger's pre-act-4 version if the old source still holds the data. dell2 edits no bucket policy.
