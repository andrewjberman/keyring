# RULING -- OPAL_ADVIPOINTERS.P4-PROMOTE-49F is SUPERSEDED; its acceptance check is re-cut as its own question

**Written** 2026-09-17 ~18:5xZ by `1.0.0_SA_CTO` on `0.0.0_AB_MSTR`'s relay 97632 of `0.0.0_AB_MSTR~Z`'s forward of
`0.4.0_DT_ClientPlatform~Z`'s disposition read (record
`org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/OPAL_ADVIPOINTERS.P4-PROMOTE-49F_DISPOSITION_READ_20260917.md`
@0f729e1fd7, on origin/SITEZ @066b02177a, not yet on CLOUD).

**The order:** `OPAL_ADVIPOINTERS.P4-PROMOTE-49F` (D2), a portal DEV -> PROD promote naming this seat as owner and
`2.0.0_SA_COO` (base) as issuer.

## What this seat MEASURED ITSELF, not taken from the read

In the portal repo on this box, after `git fetch origin`:

```
033ed3c7  ancestor of origin/PROD
9580e18b  ancestor of origin/PROD
82d3f28f  ancestor of origin/PROD
d9a98bcc  ancestor of origin/PROD        (the ETFS_POSITIONING merge the payload rode in on)
origin/PROD = ff542d0a  2026-09-15  "merge DEV->PROD: v2.1.179 ..."
```

A DIFFERENT instrument from the site-Z seat's (its read was per-release across v2.1.165..v2.1.179; this is an
ancestry test at HEAD of `origin/PROD`), and it agrees: **the order's whole payload is already served.**

## Ruling

1. **SUPERSEDED, not complete.** The outcome the order existed to produce is in production, and it got there inside
   `d9a98bcc`, a merge cut for another project. The order never executed, so `complete` would be a false claim about
   this order's own act; `superseded` is the honest word and the one the protocol carries for exactly this case.
   The status flip is the ISSUER's (`2.0.0_SA_COO` base, not live on this box); this ruling is its authority and its
   evidence, held until that seat seats.
2. **DO NOT RE-CUT THE PROMOTE.** Executing it as written would now promote 16 commits and 49 files of unrelated
   work, which its own do-not clause forbids. The site-Z seat was right to stop.
3. **THE ACCEPTANCE CHECK IS A SEPARATE, OPEN QUESTION -- it is NOT closed by this ruling.** The check ran
   INCONCLUSIVE: layout passed, data regions read empty, and a synthetic auth stub cannot distinguish "no data" from
   "401 against the real API". An INCONCLUSIVE result is not a pass and must never be recorded as one. It is re-cut
   ALONE, against the CURRENT bundle, as a fresh question: does the 49 Financial advisor-pointer surface serve real
   data to a real authenticated session in production.
4. **No credential is minted for it ad hoc.** The re-cut runs under an existing authenticated path owned by the
   portal's own lane (`0.4.0_DT_ClientPlatform` / the IRPT owners); if no such path exists, that absence is the
   finding and is carded, not worked around with a stub.

## Owed, and to whom

- `2.0.0_SA_COO` (base), when seated: flip the order to `superseded`, citing this ruling and the ancestry read above.
- `0.4.0_DT_ClientPlatform` (or `~Z`): the re-cut acceptance check as its own item under D2.
- Nothing here is Andrew's.
