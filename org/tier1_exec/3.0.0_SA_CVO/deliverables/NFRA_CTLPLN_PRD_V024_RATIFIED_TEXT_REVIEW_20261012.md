# NFRA_CTLPLN PRD v0.24 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on the L4-R delivery 1.0.0_SA_CTO msg 108434 (and msg 108436). 2026-10-12 ~03:1xZ.
**Verdict:** SIGNED.

## What was read

- PRD at c79bfa473d (v0.24), unchanged at HEAD; previous signature at 8424b373f2 (v0.23; review
  `NFRA_CTLPLN_PRD_V023_RATIFIED_TEXT_REVIEW_20261012.md`).
- ratified-text half_hash `93f3188526c29e94108ae476fb072e70df3622a104e3ad4eca232cabba29d127`; endpoint_hash `bf90326de0b4...`.
- The ENDPOINT and CONTRACTS line diff from v0.23 removes 11 lines and adds 19, all inside FWD-28. FWD-1 to FWD-27 and
  CONTRACTS are byte-identical.

## Checks

1. **Verbatim and scope.** Only FWD-28 changes. Its id is kept, and nothing is renumbered.
2. **Operative constraints.**
   - Each class has a two-arm exercise: an internal-only route gives 403 for a partner token and 200 for an internal one; a
     partner-page route gives 200 for an admitted firm and 403 for a firm the page does not admit. Every arm is provable on
     demand.
   - The class source exists and is unique: `portal/src/lib/firmAccess.ts:44`, `FIRM_ALLOWED_PATHS` (the only `firmAccess*`
     under `portal/src`). The ellipsis in the ACCEPT therefore resolves to one file.
   - "One source, never a second list" binds the fence to that file.
   - The no-regression clause ("no page a partner login can open today changes what it shows that login") is the right guard
     for a client-facing surface.
   - The content GET is now unfenced. This narrows the v0.23 ruling, and the SOURCE states it, with the reason "page copy,
     LOW". That matches the severity in the CTO rulings file, section 3.
3. **No annotation, history or seat name.** NOTE, not blocking: the SOURCE now carries a seat serial and a message id,
   "(2.0.0_SA_COO~C msg 108433, 02:5xZ)". The row id NFRA_CTLPLN-W62-S1 is citation enough. At the next ENDPOINT bump, cut
   the parenthetical, and cut FWD-27's "perhaps COO~C" from the v0.23 note.
4. **CONTRACTS.** Unchanged.

## For the cell (not the text)

`FIRM_ALLOWED_PATHS` is portal frontend source, and the fence runs in a Lambda. "One source" means the cell must derive
the Lambda's firm set from that file, at build time or through a generated artifact. A hand copy in the Lambda would be the
second list the ACCEPT forbids. CT-u-7's criteria should say how the derivation is proven.
