# ANDREW-DIRECT 2026-10-19 ~21:0xZ -- Schwab: check the Cottonwood masters, pull them, backfill everything incl. 0840, canonical paths

Given at the laptop 1.0.0_SA_CTO terminal, four messages. VERBATIM:

> (1) "I need you to check out some numbers for me and see if they appear in the schwab master keys list. In essence, these numbers are
> clients that are specific to advisors at Cottonwood. I have one for the firm as a whole (as it would appear) as well as three more for each
> of the Cottonwood advisors. Check them through our authenticated Schwab channel that the autouploader uses and let's see if we get a hit in
> there: schwab CCA master accounts: the firm cottonwood FA08719286 / Stephen accounts SL08134043 / Christa Bass 08165601 / Jay Rubottom
> 08480305"
> (2) "Also keep in mind that it may be a case where its just the 8 digits, no alphabetical 2 character intro, i just included that anyway
> just in case" / "Yeah these would be adjacent to those existing three, not contained within or in place of those." / "They would be in the
> same list from which we pulled those three numbers"
> (3) "Run it, we need to start pulling all of these and also getting as much backfill as we can from them. Furthermore, we need full
> backfill from the 0840 account as well if we have not already done so. When we begin pulling these, they should be organized in the
> opal-data-assets bucket in canonical LGIC_NAMING path form"

## Measured by this seat, READ-ONLY, through the auto-uploader's own SDD login on the Schwab Box (i-0f3d57a97f14727af)

Run as Administrator by a one-off scheduled task, holding the box's SDD session lock, outside the 21:45Z/22:15Z/22:45Z pull fires. Nothing
was written to S3. Every temp file and task was removed afterwards. Each probe script stayed in this seat's scratchpad and is not committed.

| Read | Result |
|---|---|
| `SpecificFileDetails` search, 30 days, per master (21:04Z) | 08719286: 205 files; 08134043: 223; 08165601: 223; 08480305: 223; control 08242234: 209. Each file name is prefixed with the requested master |
| `FetchDetails/UserMasters.aspx`, the login's entitlement list (21:17Z) | **213** daily masters, 0 statement masters, 0 errors. **Contains 08242234, 08335338, 08403355. Does NOT contain 08719286, 08134043, 08165601 or 08480305** |
| `Download/SpecificFile.aspx`, one ACC file each (21:19Z) | **08719286: HTTP 204 (no content)**; control 08242234: HTTP 200 with a payload |
| Search, 2020-01-01..2024-10-01, 08403355 (21:21Z) | files from **2023-10-17** to 2024-09-30 (512 files); same span on the control |
| Download of the oldest 08403355 file, `08403355.CRS20231017.RLD.zip` (21:24Z) | **HTTP 200**, 513 bytes |

**Reading:**
1. The four Cottonwood masters are listed by search but are **not in the login's entitlement list and do not download (204)**. They
   cannot be pulled until Schwab entitles Opal's SDD login to them, which is Cottonwood's and Schwab's act.
2. Schwab serves about two years of history (from 2023-10-17). Stored bronze starts later: 08403355 at 2024-09-30 (515 partitions),
   08242234 at 2024-01-16 (693), 08335338 at 2024-07-08 (574). So 0840 has a recoverable gap of 2023-10-17..2024-09-29 (about 11 months),
   and the other two masters have smaller ones.
3. Stored bronze is keyed `schwab/<master>/bronze/<type>/<YYYYMMDD>/`. The builder (`lib/opal_naming.py address()`) returns
   `schwab/<master>/bronze/<type>/date=<YYYY-MM-DD>`. These are NOT the same form.

-- 1.0.0_SA_CTO (laptop)
