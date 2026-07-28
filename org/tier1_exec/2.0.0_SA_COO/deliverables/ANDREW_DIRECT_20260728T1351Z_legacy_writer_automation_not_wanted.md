# ANDREW-DIRECT 2026-07-28 ~1351Z -- the legacy MDPF writer's AUTOMATION is not wanted

**Recorded by:** `2.0.0_SA_COO` · **Channel:** Andrew directly at the COO terminal
**Received:** 2026-07-28T1351Z · **Recorded + broadcast:** same turn, per `org/XXX.md` Andrew-direct protocol
**Related:** MDPF P0 (Andrew-direct ~1315Z + ~1328Z, both recorded by `1.0.0_SA_CTO`)

---

## VERBATIM

> "yes we dont need a legacy writer being automated if the automation is a clobber of a deprecated path"

**NOT A PARAPHRASE. The phrasing is the ruling.**

Context in which it was said: I had reported that (a) the 07-23 REVAMP restore had landed and was
byte-verified, (b) the legacy rollup step `mdpf-daily-dispatch.sh:391` writes the exact served keys and
will clobber the restore at ~15:00Z, and (c) my recommended hold was a **temporary** one whose cost is that
the served keys would then have no automated producer at all.

---

## WHAT IT BINDS (surfaced, NOT adjudicated -- I am the receiving agent)

1. The legacy writer's **AUTOMATION** of the deprecated served path is **not wanted**. This converts the
   `:391` hold from a **temporary stopgap needing an un-hold condition** into a **decommission**.
2. It therefore **discharges** the "who owns the un-hold, and when" question I raised at 134905Z. There is
   no un-hold. That concern is withdrawn.
3. **IT DOES NOT DISCHARGE THE OPPOSITE HALF -- IT SHARPENS IT.** With the legacy writer's automation gone,
   the served MDPF keys have **NO automated producer whatsoever** until the REVAMP scheduled publisher
   lands. The schedule half of the P0 stops being the second item and becomes **load-bearing**.

## SCOPE QUESTION I AM EXPLICITLY NOT RESOLVING -- routed to CTO

The ruling names "a legacy writer ... whose automation is a clobber of a deprecated path." Two readings
differ materially and I do not adjudicate scope:

- **(A) NARROW** -- stop the `json/mdpf/*` dual-write only (the clobber). `build_aggregate_aua_timeseries.py`
  :626-634 and :651-662 are the two `try/except -> WARN + continue` mirrors; the platinum write at :615 is
  the authoritative one and is NOT a clobber of a served key.
- **(B) BROAD** -- stop the whole Stage-4 rollup.

**(B) CARRIES A MEASURED HAZARD (`mdpf-daily-dispatch.sh:388-397, :399-425`):** Stage 4 is fail-fast
(`CHAIN_STATUS="failed"; exit 1`), and **Stage 5 (OWNTS per-ticker ETF ownership timeseries, 4 Opal ETFs,
explicitly consumer-facing) runs AFTER it.** Killing Stage 4 kills OWNTS as collateral. **The ruling says
"clobber of a deprecated path"; OWNTS is neither deprecated nor a clobber.** On the plain words, (A) is the
faithful reading and (B) would exceed it -- but the call is CTO's, not mine.

## GROUNDING BEHIND THE "DEPRECATED PATH" CHARACTERISATION (measured by me this session)

- `build_aggregate_aua_timeseries.py:651` writes `json/mdpf/{firm_id}/aggregate-aua-timeseries.json` -- the
  exact keys the portal serves. Source-confirmed, not inferred.
- Yesterday's served global (07-27T15:10:34Z, 162,937 B) is a **different size** from that day's REVAMP gold
  (158,943 B) and **predates it by 49s** -- i.e. the portal was serving the legacy writer's output. That is
  the mechanism behind Andrew's observed "regressed back to the 1.78b frozen number of the legacy path."
- The artifact the legacy path was producing **fails its own internal sum identity on 425 of 425 testable
  rows** (`opal_aggregate_aua == model_aua + non_model_aua`); the 07-23 REVAMP artifact fails 0 of 423.

## STATUS AT TIME OF RECORD

Restore landed 13:41:05-13:41:10Z, byte-verified GREEN (served global MD5 `5f758b47...` == gold 07-23
source, 254,419 B, independently hashed by me). Cottonwood untouched at `194e5bb0`. All four keys on one
07-23 generation, as-of 2026-07-22 (**3 trading days behind the T-1 frontier**, weekend excluded).
**Clobber still live at ~15:00Z until the hold lands.** No IAM and no runner config touched by me.

-- `2.0.0_SA_COO`, 2026-07-28T1351Z
