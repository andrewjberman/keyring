# MDPF_CANON PRD v2.11 -- ratified-text half (ENDPOINT + CONTRACTS) re-sign review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on 1.0.0_SA_CTO msgs 108374, 108380 and 108382. 2026-10-11 ~18:4xZ.
**Verdict:** SIGNED. This is a wording re-sign under an unchanged ENDPOINT (proportionate sign-off, CLAUDE.md rule 27 L4-R).

## What was read

- Prior signature: `prd/signoff/3.0.0_SA_CVO.json`, v2.9 @12adb87963, half_hash `544bf90841d6...`, endpoint_hash `1a31840f1783...`.
- PRD at HEAD: `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` v2.11 @1e5dcef9cb.
- Hashes from `.tools/prd_signoff_lib.py` `half_hashes()` and `endpoint_hash()`:

| pin | ratified-text half_hash | endpoint_hash |
|---|---|---|
| 12adb87963 (v2.9, signed) | `544bf90841d6...` | `1a31840f1783...` |
| fa51c1f544 (v2.10) | `9535c5fe77ef960fefff6f6a0c93206bd819a92cf7c078133099b415c89bb076` | `1a31840f1783...` |
| 1e5dcef9cb (v2.11, HEAD) | `9535c5fe77ef960fefff6f6a0c93206bd819a92cf7c078133099b415c89bb076` | `1a31840f1783...` |

v2.11's L10 addendum changes no byte of the ratified half. Every change since the signature is v2.10's.

## The diff (unified diff of the two ratified sections, v2.9 to HEAD)

- **ENDPOINT:** no change. FWD-1 to FWD-8 are byte-identical.
- **CONTRACTS, row "the combined slice's written basis":** the path changes from `deliverables/X2_GLOBAL_BASIS.md` to
  `deliverables/<author serial>/X2_GLOBAL_BASIS.md`.
- **CONTRACTS, new note:** the v2.10 paragraph (msg 3244, row D1-W5-S1). The owned-paths lane admits no root file, so the
  M1, M7 and M11 documents live under their author's folder.

No contract changes its direction, shape, consumer or producer. FWD-3's ACCEPT ("points at a written explanation") still
has a target.

## Note for the issuer (does not block the signature)

The placeholder `<author serial>` matches three files at HEAD: `0.9.0_WK_MDPF_CANON~5/` (CN-b-2, b920b8f34c),
`~8/` (CN-c-1, 945e1add0c) and `~11/` (CN-d-2, c1965b5895). The three are byte-different. The ledger X2 row
(`infra/logic/06_CONFORMANCE_LEDGER.md:136`) names `~11`, the newest, so one live pointer resolves the placeholder. FWD-3's
exercise must point at the ledger's copy; the two older copies are superseded drafts.
