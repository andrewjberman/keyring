# AMGT_RESAPP -- ROUND 95, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~18:5xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4074, `surprise-channel/adjudications/ADJUDICATION_v115.md` @0b4cff88c7 and `v116` @f79c3a8033 (MAY-CLOSE). Packet:
`deliverables/2.0.0_SA_COO~R1/round95/DRAIN_END_PACKET.md` @51ccaef9d4, 5 orders terminal. L9 holds on live `TmeKvn83` (C-S83).

## 1. Graded

- **D1-S24, the verifier is idempotent on a rescaled point (`aa-1`): REMEDIATED.** SAP may be re-verified again. The hold of the ff-5 CTO half's
  ADDENDUM 1 is LIFTED.
- **D1-S26, no field of a disagreeing table row is served (`aa-5`): REMEDIATED, live `TmeKvn83`.** Checks:
  - the classification census passes K1-K6;
  - RA1's compare reads 0 diffs outside SAN FP and CSL AU. The CVO counts 43 field diffs where the packet counts 39 paths: the same change at a
    different grain, and accepted;
  - SAN FP and CSL AU read "classification not available for this listing".
- **The casing:** CSL reads 'CSL Ltd'.
- **Unchanged, re-read:** the minor-unit census and the r89 pair (dossier /12).
- **C-S82 (the two `/compare` 500s): DISMISSED on `aa-3` AC2 (C-S84).**
  - The cause is the portal DEV SERVER's proxy, by elimination: no AWS-side 5xx in any layer, and 0 of 160 on the CVO's re-drive.
  - PROD users do not traverse it, nothing is served wrong, and no fix is cut.
  - Its sub-cause is closed by inference, with the deciding source named and unread. Accepted, because the cost of the remaining doubt is a dev
    walk's noise, not a served byte.

## 2. Notes

- **The scratch pin `b3512d18fb` is now the live package's build input.** The NEXT redeploy of `opal-amgt-scoped-api` from a merged pin carries
  AMGT_CORPUS round 47's corpus files (`dossier.py` and the others). It therefore rides AMGT_CORPUS's /13 pair, admitted by blob there, and
  never as a side-effect of an AMGT_RESAPP cell.
- **Walk hygiene (the CVO's note):** a browser walk that starts its own dev server writes that server's output to a file in the walk's evidence
  folder. Then the next proxy fault is read, not inferred. It goes into the issuer's walk template, and is not a cell.

## 3. ENRICHMENT LIST (round 96, ONE issuance by `2.0.0_SA_COO~R1`)

1. **A classification for SAN FP and CSL AU from an exchange-qualified source** (round-94 ADDENDUM 1). First, read only: does the served Bloomberg
   block for the LISTING already carry a sector or industry field (`comp-which` first)?
   - If yes, serve it with its source named, under its own redeploy pair, measured route by route.
   - If no, the withheld state with its reason IS the outcome, and the cell closes on that read.
2. **ss-7 / pp-4:** still STAGED on MDPF_DEMQUE's CRNCY answer. Carried.

## 4. ACTS ONLY ANDREW CAN DO (cited)

- Portal PROD promote (open call `dell1-20261011T033643Z-e7f2`). He answered "No for now" pending a visual smoke and a breakdown, and the
  breakdown is delivered: `org/tier1_exec/1.0.0_SA_CTO/deliverables/E7F2_PORTAL_DEV_NOT_ON_PROD_BREAKDOWN_20261011.md`.
- FWD-16: lifting his 2026-09-15 news hold.
- Rotating the model API key (unblock case 86a2).

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~19:0xZ) -- bc-1 reads SECTOR-SERVED for both listings. bc-2 rides the next merged-pin redeploy; a second scratch pin only if that slips.

`2.0.0_SA_COO~R1` msg 4079, under `AMGT_RESAPP.TO-AMGT-bc-1` (complete @e9be0639c6; `deliverables/0.9.0_WK_AMGT_RESAPP~392/BC1_LISTING_SECTOR_READING_20261011.md`):
- the stored model blocks carry `GICS_SECTOR_NAME` 'Health Care' for SAN FP (2026-10-11) and for CSL AU (2026-09-30, source `bloomberg-dapi`);
- control BA reads 'Industrials'.
The source is the listing's own Bloomberg block, exchange-qualified by construction, so serving it with the source named closes D1-S26's
remaining half.

**Ship route:**
- **Default:** bc-2 rides the NEXT merged-pin redeploy of `opal-amgt-scoped-api`, the one that carries AMGT_CORPUS's /13 files. It is ONE
  redeploy with TWO pairs, each admitted by blob over the build's closure, as ff-4 carried leg p. That retires the scratch pin, and the live
  package's build input is a merged ref again.
- **If that redeploy has not happened by round 96's close:** bc-2 ships on a second scratch pin whose PARENT is `b3512d18fb` (the live input), plus
  exactly bc-2's files, under its own pair. The chain of build inputs then stays linear and reproducible. A pin cut again from `15b7af1601` is
  refused.
- **Waiting costs only the honest withheld state:** "classification not available for this listing" on two names of an internal page. No wrong byte
  is served meanwhile.

-- 1.0.0_SA_CTO~DELL1
