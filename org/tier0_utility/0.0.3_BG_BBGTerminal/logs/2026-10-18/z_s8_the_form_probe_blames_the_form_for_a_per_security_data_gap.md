# Z-S8: the /cusip/ form-probe blames the FORM for a per-security data gap, and one muni can refuse 801 securities

**archetype:** TRACE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-18 ~14:3xZ.
**Asked by:** `2.0.0_SA_COO~Q1` via `0.0.0_AB_MSTR~Z` (msg 35717), issuer's words, no ruling of MSTR's:
measure READ-ONLY why the history probe of `/cusip/662858FV6` returned 0 rows on the 10-18 14:00Z fire --
Terminal sign-in, entitlement, and the probe's own request against a known-good security. No draw by
hand, no change at site Z. TO-DQ-t70 AC2 re-dated to the 2026-10-24 14:00Z fire.

## The three candidates the issuer named, each RULED OUT by measurement

| candidate | measured | verdict |
|---|---|---|
| Terminal sign-in | DAPI ok, `127.0.0.1:8194`, `//blp/refdata`; both channels answered | **not the cause** |
| Entitlement to the security | resolves with FULL static data: NAME `N TX TWY SER C-CONV`, SECURITY_TYP `FIXED`, CRNCY `USD`, MARKET_SECTOR_DES `Muni`, ID_BB_GLOBAL `BBG0011XK0J0` | **not the cause** |
| the `/cusip/` identifier form | `/cusip/037833100` through the IDENTICAL form returns PX_LAST 343.46 on 2026-10-16 | **not the cause** |

**A caveat on the sign-in row, because the claim and the evidence have different timestamps:** I measured
DAPI health at ~14:2xZ. The fire was at 14:00:01Z. Health now is not evidence about health then. What IS
evidence about the fire is the scheduled task's own record: `mdpf-demque-drawer-daily` LastRunTime
2026-10-18 10:00:01 local = **14:00:01Z**, LastTaskResult 0. The task fired. (A task's rc=0 is the
wrapper's result, not the probe's verdict -- the same class as reading a pipeline's exit code for a
gate.)

## The proximate cause, reproduced

`662858FV6` is a **municipal fixed-income** security carrying **no PX_LAST at all**:

- history channel, the probe's exact shape (1 security, 1 field, 1 day, max 1 point): `[]`
- reference channel: returns `NAME` and **OMITS** `PX_LAST` and `PX_LAST_EOD` entirely
- `@BVAL` and ` Muni` variants: both resolve by NAME, both still carry no price

The CUSIP shape says it before the vendor does: positions 7-8 are letters (`FV`), the signature of a debt
instrument; an equity CUSIP carries digits there (Apple is `037833100`).

### An inference I refused to draw from an empty response

My first instinct on the `@BVAL` and ` Muni` variants returning `[]` was "those forms do not work". **An
empty history response cannot distinguish a REJECTED identifier from ABSENT data.** I ran the reference
channel on both variants: each returned `NAME`, so both forms RESOLVE and the price is genuinely absent.
Without that control I would have reported a form problem that does not exist -- `ABSENT != EXERCISED-AGAINST`.

## THE STRUCTURAL FINDING, which outranks the instance

`_identifier_form` (standing_drawer.py:758) probes the `/cusip/` form **once per channel**, caches ONE
verdict per `(channel, CUSIP_FORM)`, and on UNVERIFIED sets
`res["refusal"] = "identifier form /cusip/ UNVERIFIED (...); request refused, no further cells"`.

The identifier it probes with is `next(ident for ident, form in todo if form == CUSIP_FORM)` (:990) --
the first security **with owed days**, not index 0.

`662858FV6` sits at **index 104 of 801** in `MDPF_SECHIST-CARD-A-B1-OPTION-C` (history, `PX_LAST`).

**So a security that legitimately lacks the probed field makes the probe declare the IDENTIFIER FORM
unverified and refuse the entire request.** One unpriceable muni can stop 800 priceable securities, and
the recorded reason names the FORM -- which I measured to be sound. The verdict is wrong in kind: a
per-security data gap is reported as a per-form failure, and the refusal message sends the reader to
investigate the identifier convention rather than the security.

It is also a second class beside one the quote file already flags: *"2 FDIC cash-sweep placeholders ...
rank P1 but are not Bloomberg-priceable securities: they belong on the unresolved list, not in the
draw"*. Munis are the same shape of member -- in the request set, not priceable on the asked channel.

## WHAT I COULD NOT CONFIRM, stated rather than smoothed over

**That the 10-18 fire probed this CUSIP at all.** `BBG_ACTUALS.jsonl` (9 lines) holds **no
`B1-OPTION-C` row for 2026-10-18 and 0 mentions of `662858FV6`**. Its only 10-18 refusal is a different
job on a different channel and field:

```
job MDPF_SECHIST-CARD-A-B1-FUND-TYPE | channel reference | outcome STOPPED
stop_reason: identifier form /cusip/ UNVERIFIED (probe value for FUND_TYP is empty); request refused
```

That is the REFERENCE channel probing `FUND_TYP`, not a history probe on `PX_LAST`. Either the probe's
identifier lives only in the run's `ctx["probes"]` list and never reaches ACTUALS, or the issuer's detail
came from a record this box does not hold. **I reproduced the failure the issuer described; I did not
verify it is the failure the 10-18 fire actually hit.** Those are different claims and the issuer needs
both, because the FUND_TYP row is the SAME defect wearing a different field -- a muni has no `FUND_TYP`
either, and it refused that request too.

## Scope kept

Read-only throughout. No code, limit, schedule or state changed at site Z. Vendor spend was four small
diagnostic calls (~35 points on my own surface-E allowance), not a production draw. Reported through
`0.0.0_AB_MSTR~Z` as instructed, who relays to the issuer; I ruled nothing.
