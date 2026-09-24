# ANDREW-DIRECT 2026-09-24 ~02:3xZ -- the SharePoint Research folders as the SEED of Security Analysis; "dossiers" in opal-data-harvest; a possible AMGT_DSSIER

**Where:** the `4.0.0_SA_CRO~Y` terminal (site Z), mid-turn during startup, 2026-09-24 ~02:3xZ.
**Recorded by:** `4.0.0_SA_CRO~Y`, verbatim and entire. **Scope adjudication:** NONE -- surfaced, not adjudicated.
**Relates to:** the ~18:3xZ 2026-09-22 word at the `1.0.0_SA_CTO~Z` terminal (*"all of the 'Research' folders ... will be
the basis for our backfill and initial pool"*), which `AMGT_CORPUS` already carries as `C-FOLDER-LIST-IS-THE-DENOMINATOR`
and `FWD-3`; and the 2026-09-22 voice memo (*"we start with the existing earnings reports that are generated in
SharePoint ... These form the foundation"*).

## VERBATIM

> "I want you to go look into the Opal Sharepoint, specifically the Shared drive, in which there is an asset management
> folder, with a research subfolder, in which there are numerous folders per company which comprises of all the
> companies the asset management team works on. I want to use this to drive the seeding of the AMGT_RESAPP, the
> "Security Analysis" platform and application. This idea may have already been explored partly or wholly in
> AMGT_CORPUS, and if so, I want to know what stage that is at. However, if we have not covered this, I want to discuss
> with you what the implementation might look like. I believe that the premise should be that we use these documents as
> a "jumpstart" for the entire "Security Analysis" application and database. The basis is that the work has already
> been done for us. The Asset Management team has already pointed out exactly what the theses are, they've already
> found company-specific major themes and drivers, already established a lot of stuff that we can feed into what I'd
> like to call "dossiers" in opal-data-harvest, per company. Something that might make sense is creating a project
> AMGT_DSSIER. The premise is that as the asset management team builds out these reports, we store them. THey are what
> give the shape to the company's page to some extent. We essentially synthesize our channels from opal-data-harvest
> around the dossier "shape", and that is what displays for the company page in "Security Analysis". I feel like the
> page structure of the existing Security Analysis platform already suits this layout fairly well, we just need to
> figure out how to finesse it. Please find the folders I'm speaking of in Shared/asset management/research/, review
> the current art on AMGT_RESAPP, _CORPUS, and the other one, and lets discuss how to work this out."

Then, after the gateway identity refused `find_sharepoint_site` (identity `opalbloomberg@opalinvest.com` off the
allowlist) and Andrew re-authenticated the `opalgateway` server as `Andrew@opalinvest.com`:

> "Try sharepoint again, i just reauthenticated with mey email"

## WHAT THIS IS (the narrow reading, stated as such)

1. A RESEARCH ASK to this seat: find the folders, review the three AMGT projects, report the stage, and DISCUSS an
   implementation. It is not (yet) a directive to open a project, cut a PRD or change any surface. `AMGT_DSSIER` is
   offered as *"something that might make sense"*, not ruled.
2. The PREMISE he states -- the team's reports are the jumpstart; their theses, themes and drivers become per-company
   "dossiers" in `opal-data-harvest`; harvest channels are synthesized AROUND the dossier shape; the dossier shape is
   what the company page displays -- is his design intent for the discussion. Whether it is already covered by
   `AMGT_CORPUS` is the question he asks, and the answer is in this seat's reply of the same turn (CORPUS covers the
   store-and-measure half; the "shape the page around it" half is not in any PRD).
3. Nothing here widens any standing gate: no vendor egress, no page change, no project registration.

## MEASURED THIS TURN (site Z, 2026-09-24 ~02:3xZ)

- SharePoint site `Shared` (id `opalinvest.sharepoint.com,9332c03f-2ad0-4b84-97fe-7bcd2c9cb90a,18b7f31c-c878-41ea-9b7e-0c103bcb5679`),
  default library, folder `Asset Management/Research`: **93 company folders** (Graph listing, this seat), matching the
  CRO's 2026-09-22 scan and `AMGT_CORPUS` K1 (93 folders / 351 files on the OneDrive-synced copy of this device).
- `AMGT_CORPUS`: PRD v0.4 RATIFIED, 11 task orders, **10 complete, 1 pending (`c-11`, never spawned)**; under the
  2026-09-23 closer CONTRACT, no further task orders are cut; `2.0.0_SA_COO~X` holds B08 / C1-C3, "close the consumer
  join" -- the substrate had ZERO readers at last measure.

## ACTS

- This record, committed under `4.0.0_SA_CRO~Y`; broadcast the same turn to the live CTO, COO and MSTR seats on this
  fabric, per `org/XXX.md` (record + broadcast, same turn; surface, do not adjudicate).
- The discussion itself is this seat's reply to Andrew at its terminal; any project (`AMGT_DSSIER` or an addendum on
  `AMGT_CORPUS` / `AMGT_RESAPP`) is `1.0.0_SA_CTO~Z`'s to register on Andrew's further word.

-- `4.0.0_SA_CRO~Y`
