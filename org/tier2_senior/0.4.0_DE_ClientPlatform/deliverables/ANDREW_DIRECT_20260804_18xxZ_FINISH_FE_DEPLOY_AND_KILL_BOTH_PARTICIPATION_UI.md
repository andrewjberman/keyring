# ANDREW-DIRECT (2026-08-04 ~18:2x-18:4xZ, at the 0.4.0_DE session terminal): finish all FE work for the portal deploy; participation UI "Kill both"

**Recorded per XXX.md record-verbatim law; broadcast to COO + CTO + MSTR same turn.**
**Channel:** direct chat at the 0.4.0_DE_ClientPlatform session (post-crash resume).

## VERBATIM 1 — resume + deploy push (~18:2xZ)

> "Ok the fabric is cooling off, you should be able to safely identify where your work left
> off and pick up and continue. ALso, if you need a visual smoke, do not waste time trying
> to go do it, just ask me i will go look. I need you to finish all the frontend work we
> were doing both on MDPF pointing as well as the LTA->ULT and LTC->LT logic adjustments
> because we need to get the portal deploy out"

## VERBATIM 2 — the held footnote question resolved (~18:4xZ, structured answer)

Question put (the open item from
`ANDREW_DIRECT_T1_RULING_NO_CARRIED_UI_DEPLOY_WHEN_CLEAN_20260804.md` par.3): does the
always-on "Carry windows: ..." T3 footnote die too, with the rare-outage T2 dark marker
read as outside the strike? Answer selected from the offered options:

> **"Kill both"** — *"Remove the footnote AND the rare-outage dark-marker notes — no
> participation rendering at all."*

## Operative reading (executor's, scope surfaced not adjudicated)

1. **The ~05:4xZ no-carried-UI ruling widens to ALL participation rendering**: T3 window
   footnote + dark notes AND the rare-outage T2 treatments (window-end ReferenceLines,
   absent tooltip rows). Nothing of `meta.channel_participation` renders on the page.
2. **Data layer untouched** (unchanged from the ~05:4xZ ruling): participation/carry
   provenance stays in the artifact; FE read helpers stay in `pairedProvenanceRead.ts`.
3. **Executed same turn:** portal DEV `45e5843f` (deletion-only, 25+/126-; tsc -b clean;
   ui-smoke render verified; SURFACE_ACK audited citing this ruling, same pattern as
   accepted `68fd700c`).
4. **Deploy state:** with this commit the FE work Andrew named is complete on DEV —
   MDPF pointing (canonical map `7d544d27`, frontier clamp + timestamp hygiene
   `68fd700c` CTO-accepted 173318Z) + LTA->ULT / LTC->LT (`70c884ae`). DT
   (0.4.0_DT, scoped promote authority per Andrew ~1727Z) gets the GO this turn.
5. **Visual smoke protocol this session:** Andrew looks himself on request — agents do
   not burn time driving the authed UI. (ui-smoke headless remains the scripted
   pre-commit instrument.)

— 0.4.0_DE_ClientPlatform
