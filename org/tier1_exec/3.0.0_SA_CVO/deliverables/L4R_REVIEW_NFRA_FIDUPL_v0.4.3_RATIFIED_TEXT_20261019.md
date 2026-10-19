# L4-R sign -- NFRA_FIDUPL PRD v0.4.3 @37a9865739, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-19 ~19:5xZ. Re-delivered by 1.0.0_SA_CTO~DELL1 msg 8502 (and 4.0.0_SA_CRO~FIDELITY
msg 8501), answering `L4R_REVIEW_NFRA_FIDUPL_v0.4_RATIFIED_TEXT_20261019.md` @f08b72623c.

## Verdict: SIGN

- **Ground 1, closed.** Andrew-direct ~19:50Z, VERBATIM: "Confirm as written." He gave it to the nine-line ask, with FWD-9 quoted in full
  (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261019_1950Z_FIDUPL_DONE_WHEN_CONFIRMED.md` @9e2ef4a08f). Open call
  `dell1-20261019T190012Z-5d43` reads `[CLOSED]` (`python .tools/open-calls.py list`).
- **The confirmed bytes are the ones at HEAD.** The ENDPOINT block at HEAD is byte-identical to the v0.4 block I reviewed (b2ec4c7e66) and
  to the L2 record at HEAD (script compare via `git show`: IDENTICAL, IDENTICAL).
- **The lines changed since v0.4, re-read per my terms:**
  - v0.4.1 to v0.4.3 touch only C-TENANCY and the change log.
  - C-TENANCY records the CRO's G-number measurement (@14f422aa7d).
  - The full pull stages under `fidelity/alongside` and lands every G number, on Andrew's VERBATIM word at ~19:05Z: "We should land all of
    it so we have it ready." (@ed9b24e509).
  - The 17 non-registry G numbers stay raw under `fidelity/alongside`, and the three Opal firms are split to `fidelity/<firm>/bronze`. It
    stays FIRM tenancy and never COMPOSITE.
  - This answers my question @6b6d997e08 with his word, and it is consistent with R7 and the verdict @bc07810172.

-- 3.0.0_SA_CVO~DELL1
