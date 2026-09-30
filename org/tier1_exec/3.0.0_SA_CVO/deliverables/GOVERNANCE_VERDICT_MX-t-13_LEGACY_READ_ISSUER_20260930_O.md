# Governance verdict -- who issues MX-t-13's LEGACY-READ (3.0.0_SA_CVO~O, 2026-09-30 ~11:1xZ)

**Call:** 1.0.0_SA_CTO~O msg 27111 (self-drive NFRA four, tick 32). May 1.0.0_SA_CTO~O issue the LEGACY-READ for
NFRA_MCPINDEX MX-t-13's read of `opal-data-bd` `silver/fees/` (one Python helper site, one `tf_local`; COO~MI msg
27110, row Z-W21-S9)? Or must laptop 1.0.0_SA_CTO issue it, as owner of ADVI_FIRMBKTS and LGIC_ENFORCE?

**VERDICT: 1.0.0_SA_CTO~O issues it.** The laptop CTO gets a copy as remediation owner, not a hold.
**MOOT for MX-t-13 (see CORRECTION below):** its literals are NEW, and the gate refuses a NEW literal before any
waiver is read. The clear is an R20 acknowledgment from Andrew.

## Basis (measured at HEAD, not taken from the pitch)

1. **The lane grants the ROLE.** `.owned-paths.yaml:60-63` lane `NAMING_LEGACY_READ_AUTHORITY` reads "only the CTO
   role may author the exact NAMING_LEGACY_READS.json carrier. Existing canonical CTO suffix inheritance remains".
   `.owned-paths.yaml:1114` binds `org/standards/NAMING_LEGACY_READS.json` to that lane. `~O` is a suffix of the CTO
   role.
2. **The gate grades the record, not the seat.** `.tools/naming-gate.py` `authority_ok()` (from `:1052`) requires a
   full 40-hex pin that resolves, the record present at that pin, and the ruling id as a whole token in it. It names
   no issuing serial.
3. **Same project, same issuer, already.** `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/LEGACY_READ_AUTHORITY_MX-t-8_20260925.md`
   is 1.0.0_SA_CTO~O's own authority for MX-t-8's reads. The carrier's history shows 1.0.0_SA_CTO~O authoring it
   (e4ec197609, OG-m-2b).
4. **The pitch's cited delegation is not the basis.** Delegation `ecf350639a`
   (`IRPT_MVP_COMPLETION_20260922/AUTHORITY.md`) is Andrew's grant to the laptop CTO to adjudicate IRPT P/M/Y session
   open calls. It is IRPT-scoped and passes nothing to other projects. The verdict does not rest on it; it rests on 1-3.
5. **Ownership of the key is a different question.** A LEGACY-READ neither advances nor closes the owning migration
   (the MX-t-8 record says so in its own words). The owner of the `opal-data-bd` remediation is named in the entry's
   `remediation` / `owner` fields and gets a copy. Andrew's reinstatement order
   (`ANDREW_DIRECT_20260930_072xZ_NFRA_MCPINDEX_REINSTATE_NO_TEST_USER_NO_AUTH.md`) weighs against inventing a hold the
   mechanism does not have.

## Conditions (the MX-t-8 form, unchanged)

- READS only, of `opal-data-bd` `silver/fees/` at exactly the two sites named: one Python helper site, one `tf_local`
  (the `TF_LOCAL_FIELDS` shape). No other prefix, no write.
- The entries are computed with the gate's own functions against the final bytes, and landed by 1.0.0_SA_CTO~O in
  its own commit BEFORE MX-t-13's commit. They carry an `as_of_cutoff` for the commit window and a named remediation
  owner.

## CORRECTION 2026-09-30 ~11:2xZ -- the mechanism does not reach these literals (supersedes this section's first cut)

The first cut said a LEGACY-READ could clear Z-W15-S5 (and, by implication, MX-t-13). **That is wrong.**
1.0.0_SA_CTO~O (msg 27115) is right, and I re-read it at HEAD. In `.tools/naming-gate.py` `judge()`, a literal is
NEW when it is absent from the file's pre-image (`:1413`). NEW plus OUT-OF-PATTERN or ALIAS returns REFUSE at
`:1444-1445`, before the only waiver lookup at `:1446`. The code comment there says a NEW literal "can never reach it".
Z-W21-S9 grades all 5 MX-t-13 literals NEW, and Z-W15-S5 graded the ETF literals NEW, so no
`NAMING_LEGACY_READS.json` entry can clear either.

**What stands:** the issuer verdict above -- 1.0.0_SA_CTO~O may author LEGACY-READ entries. It is moot for these two
cases. **What replaces the clear:** CTO~O's ruling that MX-t-13 joins B3, and both go to Andrew as one R20
acknowledgment (CLAUDE.md rule 30).

-- 3.0.0_SA_CVO~O
