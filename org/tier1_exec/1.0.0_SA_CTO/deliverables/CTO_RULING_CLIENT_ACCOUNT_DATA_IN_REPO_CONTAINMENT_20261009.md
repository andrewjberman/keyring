# CTO RULING -- client account data in tracked files on dell2: containment scope

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~16:1xZ | **Sources:**
- CVO msg 3606 (URGENT);
- `~D2` msgs 3634 and 3639 (census);
- `~P2` msg 3636; `~G2` msg 3635.

## What is measured

**Removed so far** (bytes kept outside the repo; history still holds them):
- @20e0b6408b: W73_S1, W73_S2 (IRPT_DASHBD);
- @cb16f8b2f9: the ADVI_COTBKF ARD manifest (1,533 account ids);
- @d2eb7316f2: 15 IRPT_DASHBD tie-out files (up to 5,252 accounts each).

**Census of every file under `org/missions/D9/IRPT/` at HEAD:** 3,776 files, **130 hits**.
- IRPT_DASHBD: 59 evidence JSONs, 27 docs, 14 code files.
- IRPT_BCKEND: 10 evidence, 8 docs, 12 code.
- Some filenames are themselves account numbers.
- The path list is OUTSIDE the repo: `C:/dev/_irpt_private_evidence_20261009/IRPT_WIDE_CENSUS_20261009.json`, sha256 `168225f140882ea2...`.

**Today-only censuses:** `~G2` (YCDGEN/ANLREQ) 0 of 108; `~P2` (BCKEND) 0 of 414. That denominator was too narrow, since BCKEND has 30 hits at HEAD.

## Ruling

1. **Evidence files (DASHBD 59, BCKEND 10): MOVE NOW** under the audited `TREE_DELIVERABLES` override, byte-copied outside the repo first, by `~D2` and `~P2` this hour.
2. **Docs (DASHBD 27, BCKEND 8): REDACT in place.** Each account number becomes a stable token, `acct#<first 8 hex of sha256(firm:account)>`, so cross-references survive.
   - Task orders, PRD and decompositions are redacted by their lane owners.
   - Channel and adjudication rows are the CVO's (append-only), so the CVO redacts them, by relay.
   - The token key never enters the repo.
3. **Code (DASHBD 14, BCKEND 12):**
   - a real account number in a TEST becomes a synthetic fixture;
   - in a RUNTIME literal, it moves to a config read from outside the repo, or from the firm's served data.
   - ONE cell per project in the next issuance, under its own pair where the code is deployed.
4. **Filenames that are account numbers:** renamed to their token, in the same commits.
5. **A census over EVERY `org/missions/` tree at HEAD, not only IRPT:**
   - every dell2 COO, for its own projects, with the denominator printed, this tick;
   - a hit follows items 1 to 4.
6. **Rule from now on (msgs 3628-3632):** no account id, balance, fee or flow in any tracked file. The repo carries counts, sha256 and reason codes only. Every
   worker prompt states it.
7. **History:** every path above remains in git history on origin box/dell2 and CLOUD (GitHub Opal-Capital/ajb_workspace). **Purging it is destructive git and
   Andrew's act.** MSTR~DELL2 holds the full path list (outside the repo) for him.
8. **Proposal only, to the laptop commit-gate owner:** a `ds-precommit` limb that refuses tracked files carrying tokens equal to served account ids. It is a gate
   edit, not an approval gate, and it waits on its owner.

-- 1.0.0_SA_CTO~DELL2
