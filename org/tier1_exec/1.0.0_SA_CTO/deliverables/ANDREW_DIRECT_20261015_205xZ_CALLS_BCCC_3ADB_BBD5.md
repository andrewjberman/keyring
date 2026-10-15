# ANDREW-DIRECT 2026-10-15 ~20:5xZ -- answers to dell1 calls bccc, 3adb, bbd5

**Channel:** the `1.0.0_SA_CTO~DELL1` terminal. **Recorded by:** `1.0.0_SA_CTO~DELL1`, same turn.

## Verbatim

> "Call bccc: Yes it was there to be super secret, i can break glass just let me know what to do for that. Call 3adb: yeah sure. Call bbd5: yes
> fix only round now"

## What each settles (scope as worded)

- **`dell1-20261015T203148Z-bccc` (ADVI_COTBKF): the CRM zip WAS uploaded.**
  - The round-88 job's 403 is therefore not "not landed". It is a wrong key, a wrong place, or a refusal.
  - The live bucket policy, read by this seat, lets the job's role through every deny: it matches `*-cot-*` on DenyForeignFirmPrincipals and
    was in the readers list.
  - A key that does not exist also reads 403 to a role with no List, so the likely cause is that the job's key differs from where the file
    sits.
  - His offer to "break glass": the first step needs no break-glass. `Andrew_Berman_Console` is already a reader and lister of the restricted
    prefix, so he can open it in the console and give the exact key (name only).
  - A second one-job window follows on that key, with the C-S3 fix landed first. His (a) word on d3cc covers the job's limits. The second
    window re-runs the same job under the same limits.
- **`dell1-20261015T194123Z-3adb` (ADVI_COTBKF): option (a), the swap.** Served Yahoo-priced days for securities held in V2 stay, labelled
  interim-Yahoo. Each security's points are replaced the day its Bloomberg series lands. Nothing new is drawn from Yahoo for active names.
- **`dell1-20261015T201007Z-bbd5` (ETFS_RIVALS): option (a), "now".** One fix-only round 31 (the D1-S16 precedence cell alone) is cut now. The
  project parks after it, and the twice-daily reads end when it deploys.

-- 1.0.0_SA_CTO~DELL1
