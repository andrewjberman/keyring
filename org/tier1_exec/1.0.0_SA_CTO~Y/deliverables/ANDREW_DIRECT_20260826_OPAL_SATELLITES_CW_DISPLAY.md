# ANDREW-DIRECT 2026-08-26 ~21:2xZ — Opal Satellites (Cottonwood) display fold-in

**Channel:** direct at the `1.0.0_SA_CTO~Y` terminal, mid-session. **Verbatim (three messages):**

> "Another thing, since you're already here working on Cottonwood, let's direct some of your energy to
> focusing on an additional product that just came through the wire that we are going to have to wire in
> somewhere, im not sure which directive it would fall underneath but I need you to check the "Tax SMA"
> Microsoft Teams thread and look at the messages between Manav Yang and I about the Opal Satellites
> frontend work and connection for the opalinvest.dev "Model Portfolios" portal page. I think this should
> be fairly light work, we just need to brainstorm where we would want to display this, which is really
> going to be just folding it in to something somewhere because we really do not want to be making a
> whole new tab or something for these guys. Read it, parse the images if possible, and let's discuss."

> "I just checked the images, the only one that really matters is here:
> "C:\Users\AndrewBerman\Downloads\image (6).png" "C:\Users\AndrewBerman\Downloads\image (5).png". I am
> pretty sure these are not actually correct figures and that Manav is off-base, because we have gone
> through these things extensively on Rebalance BD endpoint today and maybe some of these are right but
> I wouldnt defer to the image, the only purpose of the image is to know what data we need to have
> structurally to be able to present."

> "So We've established we need to display this stuff somehow as well as yield. We have all the model
> characteristics data that we serve on the Portal's "Positioning" page, so any yield or etc is easy
> enough to calculate for the display based on the real constituents per satellite"

## What the Teams thread establishes (Tax SMA group chat, 08-25 18:05Z – 08-26 18:11Z; Manav Shah, Yang Liu, Andrew)

- **Product:** "Opal Satellites" for Cottonwood — 9 satellites (Satellite 15/30/40/50/60/70/80/90 +
  Ultra Short Term), each composed of ONE OR TWO Opal models at **fixed model weights** (Manav:
  *"model weight per satellite will never change"*; *"No this will be it, each satellite is just
  composed of a single Opal model or two"*).
- **Derived display columns** (image 5 shape): Equity / Fixed Income / Gold / Cash / Hedge per
  satellite, summing to 100% — these FLOW from the underlying models (Manav: *"If the underlying
  models change wouldn't the data just flow downstream automatically?"*). Plus **yield** per satellite
  (Manav 08-26: *"Can we add yield for each satellite somewhere"*; Andrew: *"Yes no prob"*).
- **Mapping is the one source** (Yang: *"Is there a way to keep this mapping as the one source
  somewhere? So the dashboard can always pull it from there?"* … *"Mostly static, but make it editable
  for Manav and me."*).
- **No BD dependency; snapshot-only v1** (Manav: *"I don't think we need BD for this"*; Andrew: BD has
  no model time-series).
- **Andrew's display float in-thread:** *"maybe we could make like a toggle view where they see the
  normal model radial/circle chart but can move from 'Core' to 'Satellite' or something."*
- ⛔ **FIGURE PROVENANCE RULING (his second message above): the image figures are NOT authoritative —
  the images bind STRUCTURE only.** Real numbers come from our own model data (Rebalance BD endpoint
  work today + the Positioning-page characteristics), never transcribed from the screenshots.

## Images parsed (structure only)

Image 6 (mapping): satellite → {asset model, model weight}; 1–2 rows per satellite; weights 25/50/75/100.
Image 5 (allocation): satellite → {Equity, Fixed Income, Gold, Cash, Hedge, Total=100%}.

## Disposition

`1.0.0_SA_CTO~Y` produced placement options + a rec for discussion with Andrew (this session);
directive placement itself surfaced to Andrew (his own open: "im not sure which directive it would
fall underneath"). No build authorized yet beyond the brainstorm.
