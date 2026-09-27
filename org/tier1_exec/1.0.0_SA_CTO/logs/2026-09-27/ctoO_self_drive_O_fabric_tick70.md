# /self-drive ~O fabric -- ticks 69-70 (13:46Z-14:3xZ), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** CVO~O refused my contract text and re-signed after the fix, and a gate defect was filed as a row.

## OPLGTW v1.0 ratified text: REFUSED, fixed, SIGNED

- `3.0.0_SA_CVO~O` REFUSED the ratified-text half (@22e06eabdf, review @1d5ff9f415). My C2 clause said the email_deny key is
  "sha256 of the normalized email". A route built to that text would never match the operator's record, so the deny
  would fail open silently. **Its catch was right; the defect was mine.**
- Fixed @2d2fb1f905: C2 and the contract's POLICY text now name
  `POLICY#EMAILDENY#<sha256hex("og-email-deny/v1|" + email.strip().lower())>` (the design's key at `:15`), and state that
  routes and the operator writer compute the same function.
- CVO~O re-signed @2e371ea304 (re-review @cc775d6f86). `prd-signoff status`: NFRA_OPLGTW v1.0 @2d2fb1f905 ADMITTED.
- That is the THIRD catch CVO~O has made on this seat's texts tonight (MX-r-3's `.env` writer, MX-r-3's bundle pin, and now
  this key). All three are one class: a text that names an input without pinning the exact function or source.

## Row NFRA_OPLGTW-Z-S1 (@928ef53f1e) -- LIMB 6 let OG-e-1 through a REFUSED half

- COO~O issued OG-e-1 (the R2-k build) @11657b48df, 84 s after the REFUSED stamp. Its only parent IS the refusal commit
  22e06eabdf, so the stamp was in the committed tree.
- At that commit `prd/signoff/` held TWO ratified-text files: the base `3.0.0_SA_CVO.json` (old SIGNED) and
  `3.0.0_SA_CVO~O.json` (REFUSED). The gate and `prd-signoff status` share `prd_signoff_lib.evaluate()`, so their inputs
  differ, not the rule.
- ARMED, disarm owner this seat (the gate's owner); inert for OG-e-1 after the re-sign. Disarm = reproduce on a scratch
  estate, then fix or name it a non-defect.
- Commit note: the row gate refused the first id `NFRA_OPLGTW-S63`, because a site-z row needs the `Z-` infix; it was
  renamed `Z-S1`.

## Calls, completion

One card at Andrew: Alyssa's portal-only grant locks her out of her own tools (REC (a) keep). NOT DONE -- 0 of 4 projects
`complete`. All REACHABLE.

state: ARMED

## Compiler Tools

`prd-signoff.py status`; `git merge-base --is-ancestor` on the stamp and order commits; `surprise-row-gate.py` run on the
staged file to read its exact refusal.
