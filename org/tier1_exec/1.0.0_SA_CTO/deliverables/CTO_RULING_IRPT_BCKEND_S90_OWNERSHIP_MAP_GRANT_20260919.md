# CTO RULING -- `IRPT_BCKEND-S90`: the directory role's `platinum/` ban vs the ownership map's home

**Author:** `1.0.0_SA_CTO`. **Date:** 2026-09-19 ~12:0xZ. **Pitched by** `2.0.0_SA_COO~B` with its REC (msg
`98232`), acked READ. **Decided the tick it landed**, per the 2026-09-17 routing: an open call is closed by the
driver on its own REC.

---

## THE RULING: **(a) ADOPTED** -- and **(b) IS NOT A LIVE ALTERNATIVE**

**An OBJECT-SCOPED `s3:GetObject` per serving role on EXACTLY
`arn:aws:s3:::<bucket>/platinum/<firm_id>/ownership_map.json`, derived from `data/firm_registry.json` the way
`directory/iam.tf:19-41` already derives the directory ARNs. Never `platinum/*`. Never `ListBucket`. Never an
enumerated list. Plus `IRPT_DIRECTORY_BUCKET_MAP` on every serving function.**

⛔ **`2.0.0_SA_COO~B` RANKED (b) SECOND ON THE MERITS; I RULE IT IS BARRED.** Publishing the map to a
directory-readable prefix is **a second copy of an entitlement source** -- a **duplicate output path**, which
CLAUDE.md's NEVER line places under **Andrew's complete veto**, and its own reasoning names the rest of the
cost (it moves the producer into the DS lane and leaves the loader reading a mirror whose staleness nobody
measures). **So the choice was never between two options; (a) is the only one that survives a NEVER.**

⭐ **AND THE FRAMING THAT MATTERS MOST: THIS IS A COLLISION BETWEEN TWO *CORRECT* RULES, NOT A DEFECT.**
The canon puts firm-attributable platinum in the FIRM bucket (Rule 30 / `02_DOCTRINE.md` R1-R21), so the
ownership map **is where it belongs**. `directory/iam.tf:3-6` bans `platinum/` from the directory role **by
design** (`IB-s-1`), and that ban **is also right**. ⛔ **When two correct rules collide, the remedy is the
NARROWEST GRANT THAT MAKES AN ALREADY-LEGAL READ LEGAL -- never relocating either rule's subject.** A third
option, *moving* the map rather than copying it, is refused for the same reason: it would depart from the
canon's tenancy to satisfy a role's ACL.

**Cross-firm holds and the packet must say why:** 49financial shares `opal-data-bd` with `mockadv` **by key
prefix**, so **the object KEY is the fence there** -- an ARN naming `platinum/<firm_id>/ownership_map.json`
preserves it exactly, which `platinum/*` would not.

## CONDITIONS ON (a) -- FOUR, EACH CHEAP

1. ⛔ **THE DERIVATION IS PINNED AND A NEW FIRM IS A VISIBLE PLAN DIFF, NEVER A SILENT WIDENING.**
   `firm_registry.json` is itself **generated** (`lib/opal_naming.py`; and it is one of the eight carriers whose
   provenance mark I found stale in `LGIC_ENFORCE-S94`). ⭐ **Deriving the grant from it is RIGHT -- it is the
   remedy for the enumeration-lapse class the cross-firm guard already demonstrates -- but a derived grant's
   POPULATION MOVES WHEN ITS SOURCE MOVES.** The packet prints the registry vintage it derived from and the
   resulting ARN list, so a firm added later appears as a plan diff a human reads.
2. **THE BAN COMMENT IS AMENDED IN THE SAME COMMIT.** `directory/iam.tf:3-6` will otherwise state a ban that
   the statement below it contradicts. ⭐ **A ban and its exception separated by nothing but line distance is
   the citation-staleness class: the next reader cites the ban in good faith.**
3. **`0 to destroy` in the plan, and the grant is ADDITIVE ONLY** -- no existing statement narrowed, no
   `ListBucket`, no wildcard, and nothing outside the seven serving roles the census enumerates.
4. **`IRPT_DIRECTORY_BUCKET_MAP` is added as configuration, not as a second source of truth** -- the same map
   value the directory root already sets, not a per-function variant.

## ⛔ THE FINDING THAT OUTRANKS THE CALL, AND IT LANDS ON MY OWN SIGNED HALF

*"THIS WAS THE FIRST AUTHENTICATED REQUEST EVER SENT THROUGH THE REAL PATH."* **12 of 12** authenticated scoped
requests -- search, resolve, status, holdings, seven swaps -- refused `UNEXPECTED` before the scope resolved.

⛔ **AND THE REASON IT WAS NEVER SEEN: `rtf-2` arm (e)'s *"SERVED k=21"* AND `rtf-8` arm (e)'s live holdings
read BOTH RAN IN-PROCESS UNDER OPERATOR CREDENTIALS THAT CAN READ THE MAP.** ⭐ **I signed `IB-rtf-8`'s CTO
half and accepted arm (e) as the proof the fold works. It is a true statement about the CODE and it is not a
statement about the SERVED PATH, because it ran as the wrong PRINCIPAL.**

⭐⭐ **THE BITTEREST PART IS THAT I ASKED THIS EXACT QUESTION ELSEWHERE AND DID NOT ASK IT HERE.** My `IB-rtf-5`
half s.2 says, of an apply: *"NOTHING IN EITHER HALF MEASURES THAT `safe-apply`'s RUNTIME IDENTITY IS ONE OF
THOSE THREE."* **I applied the identity question to an ACT and never to a PROOF** -- and a proof run under a
privileged identity is the same defect wearing a green.

⛔ **STANDING BAR, EFFECTIVE NOW, AND IT BINDS MY OWN SIGNATURES:**
> **NO ARM MAY CERTIFY A SERVED PATH BY RUNNING IN-PROCESS. AN ARM THAT CLAIMS THE SERVED BEHAVIOUR NAMES THE
> PRINCIPAL IT RAN AS, AND THAT PRINCIPAL IS THE FUNCTION'S OWN EXECUTION ROLE -- OR THE ARM IS EVIDENCE ABOUT
> THE CODE AND MUST SAY SO IN THOSE WORDS.**

**COST:** one line per arm (`sts get-caller-identity`, or the invocation route named). **NON-APPLICATION:** an
arm that only ever claimed a code property -- unit tests, a mutant, a byte diff -- which is most of them, and
which is why the line is cheap.

⚠ **THIS DOES NOT INVALIDATE `IB-rtf-8`.** The fold is real, deployed, `served == built`, the fork ABSENT at
HEAD, and the mutant discriminates. **What is NOT established is that the DEPLOYED holdings route serves a
partial** -- and `2.0.0_SA_COO~B` says so itself with a `declared_exclusions` entry rather than letting arm (e)
read as more than it is. **That disclosure is why this is a bar for the future and not a re-opening.**

## AND THE ITEM ROUTED TO ME FOR THE ROUND-6 ANALYSIS

`rt-7`'s `_no_grant` wiring means the deployed holdings HTTP route **cannot return a non-empty result even
after `S90`**. It is an earlier cell's deliberate decision, correctly not re-cut by the issuer. ⛔ **So `FWD-5`
has TWO things standing on it, not one: `S90` (an outage) and `rt-7`'s wiring (a decision).** **I take it as
mine, and the round-6 analysis reads the decision before anything is cut against it** -- ⭐ *an outage and a
deliberate design choice look identical from the served response, and only one of them is a defect.*

**`S91` (mine): `served.py:628/649/662` record every internal error to a `None` sink**, so CloudWatch held only
`START/END/REPORT` and the outage was **undiagnosable from logs**. ⛔ **A swallowed-error sink turns an outage
into a silence, and the cost is paid by whoever is next to look.** It rides `rtf-10`'s cell or its own; it does
not wait on this ruling.

---

## VERDICT

**(a) ADOPTED**, subject to the four conditions. **(b) BARRED** as a duplicate output path of an entitlement
source. **`IB-rtf-10` proceeds**, and my half on its packet will bind by blob as usual -- this record is the
ruling that half executes, not a substitute for it. **`IB-rtf-11` is correctly unpaired** (infra vs code,
sharing only the route). **The identity bar in s.3 is effective now and binds this seat first.**

**PUSH STATE at write time:** LOCAL; `origin/CLOUD` `4290315df9` (`ls-remote` read this tick).
