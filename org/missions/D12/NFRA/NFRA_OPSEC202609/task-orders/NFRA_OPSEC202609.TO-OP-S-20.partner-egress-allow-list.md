# TO NFRA_OPSEC202609.TO-OP-S-20 -- THE PARTNER-EGRESS ALLOW LIST, MEASURED FROM REAL SIGN-IN ADDRESSES: `allowlists/partner-egress.json` versioned in the evidence store and mirrored as ALLOW rows in the S16 table, WITH ITS DENOMINATOR -- because arming BLOCK with zero ALLOW rows is a violation and one partner office typically leaves through ONE address (OP-s-20, FWD-14 / C-4)

<to_id>NFRA_OPSEC202609.TO-OP-S-20</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~U</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>staged</status>

**BLOCKER STATUS: the named blocker has CLEARED and one measured precondition replaces it.** The cell reads *"HELD on OP-s-5 -- the auth handler is IP-blind (brief F4), so the census needs the WAF/CloudFront/ALB logs over a window; no log, no census."* **`OP-s-5` is DONE** and the ALB leg has been delivering continuously since round 1. **So the logs now EXIST; what the cell actually requires is a WINDOW of them, and that is a measurement, not a wait for a task order.**

⛔ **GO CONDITION: the assignee measures that a usable window of sign-in traffic exists BEFORE building the list, and states the window and its denominator. If the window is too short or too sparse to see a firm's real addresses, that is a ROW and a stated wait -- not a list built from thin data.** `OP-s-16` and `OP-s-17` are DONE. **GO after `TO-OP-S-4-18` goes terminal** -- one task order at a time.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT FWD-14; **C-4**) - **Decomp cell:** `OP-s-20` (v0.1.11, s.1a) - **Lane:** AE lane - **Round:** 3.

---

## ⛔ WHY THIS SMALL CELL GATES THE BIGGEST ONE

`OP-s-14`'s BLOCK arm cannot be turned on until this list exists. **C-4: arming BLOCK with 0 ALLOW rows is a VIOLATION, not a phase.** And the cell states the cost in one line: **one partner office typically leaves through ONE address, and a false positive is a locked-out firm.**

>> **SO THE FAILURE MODE HERE IS NOT A WRONG ENTRY, IT IS A MISSING ONE.** An address you fail to observe during the window is a firm that gets blocked the first time the sentinel trips on it. **That makes the DENOMINATOR the deliverable as much as the list is** -- firms observed of firms expected, addresses per firm, and the window they were observed over. A list without those three numbers cannot be judged safe to arm against. <<

## DELIVERABLE

1. **CENSUS THE SIGN-IN ADDRESSES PER FIRM from the logs `OP-s-5` established** -- WAF, CloudFront and ALB as available. **State which log source each observation came from**; they do not all see the same requests and a single-source census is a partial one.
2. **THE THREE DENOMINATORS, printed, not summarised:** firms observed **of firms expected** (read the partner tables for the expected set -- `opal-partner-*`), addresses per firm, and the observation window with its start and end.
3. **NAME THE FIRMS OBSERVED WITH ZERO ADDRESSES EXPLICITLY.** ⛔ **A firm with no observed address is the dangerous row in this census and it must be listed, not omitted.** It means either that firm did not sign in during the window, or the logs do not cover its path. **Those two are not the same and the list must say which is unknown.**
4. **`allowlists/partner-egress.json` written and VERSIONED in the evidence store** (`opal-security-evidence`, under `allowlists/`), carrying its denominators inside the file -- **the numbers travel with the artifact, not only in the proof.**
5. **MIRRORED AS ALLOW ROWS IN THE S16 TABLE.** The table is truth (C-2); the JSON is the versioned record of how the truth was derived.
6. **NO BLOCK ARM AND NO IP-SET WRITE IN THIS FACE.** This face produces ALLOW rows and a file. **The reconciler is the only thing that writes a set.**
7. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~U/NFRA_OPSEC202609.TO-OP-S-20.partner-egress-allow-list.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S20-AC1" cell_refs="OP-s-20"/> `S20-AC1` -- THE CENSUS HAS ALL THREE DENOMINATORS AND NAMES ITS SOURCES: firms observed of firms expected (with the expected set derived from a live read of the partner tables, not recalled); addresses per firm; the window start and end. Each observation attributed to the log source it came from, with a statement of what each source cannot see.
<criterion id="S20-AC2" cell_refs="OP-s-20"/> `S20-AC2` -- ZERO-ADDRESS FIRMS ARE LISTED, NOT OMITTED: every expected firm with no observed address named explicitly, each labelled **"did not sign in during the window"** or **"log coverage unknown for this path"**. **A census that silently drops them is a FAIL** -- those are exactly the firms C-4 exists to protect.
<criterion id="S20-AC3" cell_refs="OP-s-20"/> `S20-AC3` -- THE ARTIFACT IS VERSIONED AND CARRIES ITS OWN NUMBERS: `allowlists/partner-egress.json` present in the evidence store with its version id pasted, and the denominators readable INSIDE the file. **A file whose provenance lives only in a proof will be read later without it.**
<criterion id="S20-AC4" cell_refs="OP-s-20"/> `S20-AC4` -- THE ALLOW ROWS ARE IN THE TABLE AND MATCH THE FILE: a read of the S16 table's ALLOW rows, counted, compared item-by-item against the file, and shown equal. **The count alone is not the comparison.**
<criterion id="S20-AC5" cell_refs="OP-s-20"/> `S20-AC5` -- NOTHING WAS ARMED AND NO SET WAS WRITTEN: a census showing **0 BLOCK rows written** by this face and **0 calls to `UpdateIPSet`** from any identity used here; the IP sets read before and after and shown unchanged. Push state read by `ls-remote` + `is-ancestor` and stated as MEASURED.

<expected_criteria>S20-AC1, S20-AC2, S20-AC3, S20-AC4, S20-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.11), cell `OP-s-20` (FWD-14 / C-4); value: a MEASUREMENT with its denominator (firms x addresses x window).
<owned_cells>OP-s-20</owned_cells>
Read-dependencies, NOT claimed: `OP-s-5` (DONE -- the logs this census reads), `OP-s-16` and `OP-s-17` (DONE -- the table and the evidence store), `OP-s-14` (BLOCKED ON THIS FACE -- its BLOCK arm cannot precede this list).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). This face builds no monitor and arms nothing; it produces a measurement and two records.
comp-iam: DECLARED-NOT-APPLICABLE -- this face creates no role and attaches no policy; it reads logs and writes a file and table rows under existing identities.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim; its evidence is a live log census at the assignee's own vintage.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S20-AC1`, `S20-AC2`, `S20-AC3`, `S20-AC4`, `S20-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~U/NFRA_OPSEC202609.TO-OP-S-20.partner-egress-allow-list.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S20-AC1,S20-AC2,S20-AC3,S20-AC4,S20-AC5"` BEFORE the complete flip. **`S20-AC2` is the control that must be able to fail: a census that produces a clean list with no zero-address firms named has probably not looked for them.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before the census">Measure the window: how far back the logs actually go and how much sign-in traffic they hold. Too short or too sparse is a ROW and a stated wait, not a list built anyway.</phase>
  <phase id="2" when="during">Attribute every observation to its log source; never merge sources into an undifferentiated count.</phase>
  <phase id="3" when="after">Compare the table's ALLOW rows to the file item-by-item, and read the IP sets to confirm this face wrote none.</phase>
</compiler_tools_mandate>
