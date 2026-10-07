# ANDREW-DIRECT 2026-10-07 ~02:5xZ -- tailnet names to manage cross-box identity; check in with the CTO

**Channel:** typed at the `2.0.0_SA_COO~C` terminal (laptop), mid-turn, while this seat was amending NFRA_CTLPLN's CT-b-1 order so that a
Dell's fabric manager may send to every box's inbound queue and receive only its own (the CTO's msg 105931, "Andrew asked"). Clock read at
recording: 02:50:49Z. **Recorded by:** `2.0.0_SA_COO~C`, same turn.

## Verbatim

"check in with CTO on that, i think using the tailnet names is the easiest way to manage cross box ID"

## What it states (as written)

- This seat checks in with `1.0.0_SA_CTO` on "that": the per-box identity of the bus and IAM work then in hand (which box a queue, a user and a
  policy belong to).
- His view: the tailnet names are the easiest way to manage cross-box identity.

## Measured beside it (not his words)

- Tailnet names (laptop `tailscale status`, 2026-10-07 ~01:0xZ): the laptop is `cloud-local` (100.96.167.100); site Z is `sitez`; the Dells
  are `dell1` and `dell2`. So three of four tailnet names equal the register names; the laptop's does not.
- The register (`org/devices/DEVICES.json`) carries each box's `tailnet_name`; each box's identity today comes from its `AGENTBUS_DEVICE`
  setting resolved through the register (FWD-2).

## Not stated, so not assumed

- Whether the laptop's tailnet name changes, or the register maps `cloud-local` to `laptop`; whether queue and IAM names key on the tailnet
  name. These are the CTO's to rule.

-- 2.0.0_SA_COO~C
