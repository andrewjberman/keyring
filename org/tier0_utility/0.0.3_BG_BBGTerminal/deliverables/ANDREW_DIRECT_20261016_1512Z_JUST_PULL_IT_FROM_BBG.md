# ANDREW-DIRECT 2026-10-16T15:12:44.354Z -- "Just pull it from BBG"

**Recorded by:** `0.0.3_BG_BBGTerminal`, same turn.
**Channel:** Microsoft Teams, 1:1 Andrew Berman <-> Opal Bloomberg.
**Message id:** `1792163564354` · **contentType:** text · **sender:** `Andrew@opalinvest.com`
(Entra oid `2e21f8e5-55ca-45c1-91b9-a4607bf28d4f`, Opal tenant `6810043e-...`, sender gate PASS).

## VERBATIM

> Just pull it from BBG

Nothing else; that is the whole message.

## What it answered

My message `1792163530538` (15:12:10.538Z) surfaced a DENIED demand: Alyssa Keith asked for the full
names of 13 bond CUSIPs, and I declined. My stated reasons were (a) 13 CUSIP lookups is a fresh
terminal pull for data the scheduled job never delivered, which the view-never-download tie-breaker
classes as a DOWNLOAD, and (b) the data we already hold -- Schwab silver `dim_asset`, one row per
CUSIP with ticker and description -- is in `opal-data-assets`, which `refs/BUCKET_ALLOWLIST.yaml`
denies as a pre-serving tier. I offered him two options: a one-off pull by someone entitled to that
table, or widening my allowlist to it.

**He chose neither and authorised the Bloomberg route instead.**

## SCOPE -- narrow, and I am not widening it

`refs/BLOOMBERG_GUARDRAILS.md` makes the download/view call Andrew's alone
(*"Unclassifiable = download-side until Andrew says otherwise"*). He has said otherwise, **for this
request**. Relayed verbatim, adjudicated neither wider nor narrower (CLAUDE.md section 2):

- **IS authorised:** the Bloomberg reference read that answers Alyssa's 13 CUSIPs. Executed
  15:13Z, `bloomberg_reference_data`, fields `NAME` + `SECURITY_DES`, all 13 resolved; served to her
  15:14:17Z and re-sent legibly 15:14:42Z.
- **IS NOT authorised by this, and still needs his word:** a standing allowance for ad-hoc CUSIP or
  reference pulls; any change to `refs/BUCKET_ALLOWLIST.yaml`; adding securities or fields to the
  SCHEDULED pull; any bulk or historical series request. **None of those were asked and none are
  implied.** The next similar ask gets the same decline and the same escalation unless he rules again.
- **The guardrail text is unchanged.** This is a ruling on one request, not an edit to the rule, and
  `refs/` is unwritable from this seat by design anyway.

## FINDING: my own documented fence did NOT bind, and I would have reported it as binding

`prompt.md` states the mechanical fence caps `bloomberg_reference_data` at **2 securities**. I sent
**13 in one call and it returned all 13.** So either the cap has moved, or it was never expressed
that way at the tool layer.

**I predicted a refusal and measured a success.** The honest reading is the one my own standing rule
already names for capabilities: **a restriction is a figure too, and it carries an exercise date.**
I was about to tell Andrew his instruction could not be executed as given because of a cap I had
only read about. Had I done that, I would have reported a false blocker against his direct word.

Surfaced to `1.0.0_SA_CTO~Z` and `0.0.0_AB_MSTR~Z`: either `prompt.md`'s "capped at 2" is stale and
should be corrected (MSTR is its named integrator; this seat cannot write it), or the fence intends
a cap that is not in force -- and a fence believed to bind while not binding is the worse of the two.

## Partial, reported as partial

12 of 13 returned both `NAME` and `SECURITY_DES`. **`204744AK2` returned `NAME` =
`COMPTON WATER REV` but `SECURITY_DES` echoed the CUSIP** rather than a ticker/coupon/maturity --
normal for a muni. Told her so explicitly and offered to go back for that one. Never served as
complete.
