# IRPT_ANLREQ round 15, workstream ~G (ENGINE) -- decomposition: the resident registers the commentary policy revision

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** `~Y2`'s package-refusal read (`deliverables/0.9.0_WK_IRPT_ANLREQ~155/r41/PACKAGE_REFUSAL_READ.json`, checks re-run CITES-OK 130 of 130, VALID), `~Y2` msg 8566, CTO msg 8568 (ruling `CTO_RULING_DELL2_ANLREQ_PROD_PROMOTE_RELEASE_AFTER_FWD1_WINDOW2_20261015.md` ADDENDUM 2 @87fe24c71d): the resident's repository registers the served revision and `irpt-ycdgen-research-v1`; the AI commentary draft's family `ANALYSIS_COMMENTARY` lives only in `irpt-anlreq-x10-v1`, so the packager's read-back refuses "unregistered artifact family". RESERVED is not the cause.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- The fix is change (1) of the CTO's two additions to the ONE resident release r32: `irpt-anlreq-x10-v1` in `additional_policy_revisions`, with the pinned test. It is a source and test change cut now so r32 builds from a tree that carries it; it is not itself a release and moves no deployed byte.
- The constant is defined in `resident_installed.py` (beside `OPAL_RESEARCH_REVISION`) rather than imported from `commentary_draft_store.py`, so the installer does not depend on the draft store module; the test pins the literal.
- Order: research first, commentary second, as the CTO wrote it.
- Change (2), run 3's producer address (`fwd1-staff-r41b@opal.invalid` replaces `fwd1-staff-r41a@opal.invalid`, `~Y2` msg 8570), is in `resident_worker.py` and is the release cell's, with the list's comment, the pinned test and the installer's second check agreeing, as the r31 build did.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-87` | `resident_installed.py`: `ANALYSIS_COMMENTARY_REVISION` and the two-revision tuple; `test_resident_installed.py`: one assertion edited, one test added | those two files + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |

## Edges and chains

- ONE chain. `AR-g-85` (merged `002a88bdc3`) edited the same installer file and is merged; `AR-g-86` (in flight, slot 186) edits `opal_producer.py` only.

## Not moved by this cut

Any deployed byte; `resident_worker.py` and its producer list; `build_resident_package.py`; any grant.

## Four-postulate record

(i) Domain: the reporting policy revisions the resident's repository registers. (ii) One constant, one tuple. (iii) One intent: the commentary draft can be read back. (iv) What this cut does NOT move: the producer list, the release build, IAM.

fanout: 1 of 1 chain, cap 8, reason: two-line product change and its test; slot 187.
