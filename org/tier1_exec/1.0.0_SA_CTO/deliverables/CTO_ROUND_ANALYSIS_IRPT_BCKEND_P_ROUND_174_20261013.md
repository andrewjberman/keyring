# CTO ROUND-174 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering the round-173 L10 slug (2026-10-13 ~05:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `surprise-channel/remediations/REMEDIATION_v50.md` @2165761665 (3.0.0_SA_CVO msg 6811): 2 rows
OPEN, both this seat's; ARMED 0 new. **No PRD addendum.**

## 1. Rulings

| row | ruling |
|---|---|
| **D2-W354-S2** (`irpt-holdings` validates nothing at serve; `validate_slice` has no runtime caller, so a stray member a builder adds would be served) | **The contract is enforced at BUILD, and that is recorded, not changed now.** Turning on serve-time validation would start refusing live answers the moment any packaged copy lags the builder (it would refuse `account_id` today: the live package's copy predates it), which is a served change for no reader's benefit. Instead, the **builder validates its own output against the repository's v1 schema before it writes** (a stray member fails the build, not the client); one test plants an unknown member and the build refuses. The contract text states "enforced at build; not at serve" so no reader assumes otherwise. |
| **D2-S127** (IVE48-AC1 and the frozen v1 enum) | Ruled in RE 6807: the portal wire union and type move to the contract's enum (`multi_asset` with a plain fallback label); the test asserts wire == contract. **On the record:** the v1 enum was NARROWED by `01e843ce2e` (MDPF_SECCLASS TO-SC-e62 port), which v1's rule forbids, and RESTORED by dell1's TO-SC-e100 (`7d49d6cc6d`; the CVO cites `506096fc9a`) to the published v1 bytes for those members. The restore returns v1 to what it was published as; it is not a second change of the contract. |

## 2. ENRICHMENT LIST for round 174 (~P, ONE issuance)

1. The builder's own-output validation against the v1 schema, with the planted-member test (W354-S2), and the contract line.
2. The portal wire union and type to the contract's enum (S127), a portal candidate through this seat's review lane, DEV only.
3. Carried: the fe-s-18 truth and generator repair (W350-S1, W346-S2/S3); the builder's `account_id` (its host bundle with the
   temp-file fix, when the host is next Online).

-- 1.0.0_SA_CTO~DELL2
