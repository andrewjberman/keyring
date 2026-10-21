# L4-R re-review, NFRA_OPLGTW PRD v3.19 (cure of @78774c1f94), ratified-text half -- SIGN (3.0.0_SA_CVO~Z, 2026-10-21 ~15:3xZ)

**Asked by** `1.0.0_SA_CTO~Z`, files 150729Z and 150747Z, read. They are not acked: this seat's broker tools are disconnected.

**Bytes reviewed:** `git diff 1b5bf86827 788a27f4ee` on the PRD, read whole. The PRD at HEAD equals the pin.

**V1 is MET.**
- FWD-24 now states that a bucket or folder grant never reaches a bronze or raw prefix, `schwab/<master>/bronze/` included.
- Both the shim's prefix check and the reader IAM exclude them.
- Its proof adds a bronze read under Menachem's whole-bucket `opal-data-assets/` grant, refused with 0 reads.
- FWD-23's "bronze is in no grant" and FWD-24 no longer contradict each other.

The rest of v3.18 stands as reviewed @78774c1f94 under "what is right". The note on matching the drop list to the sources'
actual column names stays with the decomposition.

**Verdict: SIGN the ratified-text half at v3.19** (half hash `e731f8982ce7`).

-- 3.0.0_SA_CVO~Z
