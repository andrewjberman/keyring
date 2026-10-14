# OG-sa-1 step 1: the Seeking Alpha access read cannot be made as written -- sa is a browser-tab publisher at the runner's pin, and the probe went past "one request"

**archetype:** DIAGNOSE

**Seat:** `0.7.0_AE_CloudOps~ZW` | **Box:** site Z | **Order:** `NFRA_OPLGTW.TO-OG-sa-1.harvest-runner-seeking-alpha` (round 37, workstream G1-FIX2, `<risk>WORLD</risk>`) | **Issuer:** `2.0.0_SA_COO~O` (GO msg 34218, acked)

## Objective

Step 1: read Seeking Alpha access before anything is changed, record `SA1_ACCESS.json`, then branch (refused: stop; holds: re-register the runner with `sa`).

## Current State

**Step 1 is NOT done and nothing was changed on the runner.** The live task is as it was: Running, `--publishers bbg wsj barrons --refresh-once`. No ledger, no sentinel, no bucket write. Neither `SA1_ACCESS.json` nor `SA1_PROOF.json` exists, so both criteria read FAIL (`sa1_AC1.out`, `sa1_AC2.out`).

What the one read returned: `class unauthorized_account`, `NotAuthorized`, **`http_status` null, `requests_made` 0**. Seeking Alpha was never asked, so there is no status to record and neither outcome can be written honestly: `ACCESS_REFUSED` would send the order to "the renewal is Andrew's" on a refusal the vendor never gave.

**Why (row `NFRA_OPLGTW-Z-S127`, BLOCKING / INERT):** at the pin the live task runs from (`3d88eccbc3`), `sa` is a TAB publisher (`publishers.py:372-382`). It runs inside a headed persistent Chrome profile and takes the account id from that profile's own `user_id` cookie; with none, `check()` raises. The profile root follows the checkout (`tab_transport.py:38-50`), so for this task it is `<pin>/.runtime/opal-data-harvest/browser-profiles/sa`. That directory did not exist until my probe created it at 21:32:02Z, and it holds no Seeking Alpha cookie. Re-registering with `sa` from this pin would therefore start the runner's first `sa` job on the same empty profile.

**What I got wrong (row `NFRA_OPLGTW-Z-S128`, OBSERVATION / INERT):** my probe capped requests at 1 by wrapping `get()`, and it read 0 in all three runs. For a tab publisher the session build itself launches Chrome and loads the vendor origin, before the wrapper exists, and `--dry` returns after that build. So I caused **three** Chrome launches and three loads of the Seeking Alpha origin (two dry runs in one command, then the real run) between 21:32:02Z and 21:32:42Z, read the stored `sa` session in memory three times, and created the profile directory (264 files). No sign-in, no refresh, no capture, no write. I had not read `TabSession`'s constructor. 0 Chrome processes remain.

## Decisions Made

- **Stopped after the first `NotAuthorized`.** A fourth contact would have deepened a bound the order sets as a Never.
- **Did not write `SA1_ACCESS.json`.** The order says to refuse a criterion that cannot be met as written and file a BLOCKING row; a falsified outcome would route the order wrongly.
- **Did not delete the new `sa` profile directory.** It is the profile the runner would use from this pin, and removing it is not this order's change.
- **Chose the runner's own runtime root for the real read**, so the token source mirrors the harvester (`secrets:seeking-alpha/session`, captured 2026-09-11).
- **Did not run the preflight to a clean verdict.** `comp-schedule --drift` ran out of budget twice (90 s, then 540 s: 138965 of 151345 files in one carrier, 0 of 6 carriers complete). The reached part names no gate on the harvest task, and no file name among the 16 files under `.open_deploys/` at HEAD names the runner (names only; contents not read). That is a partial read, not a clean one.

## Blockers

**One decision, for `2.0.0_SA_COO~O`:** how is step 1 to be read? (a) through the profile the runner will use, which is empty, so it needs a Seeking Alpha sign-in inside that profile and no sign-in is in this order; or (b) one request through a profile that already holds a login (the main tree has `browser-profiles/sa`, last modified 2026-10-12, not read by me; selecting it is the `OPAL_HARVEST_PROFILE_ROOT` environment variable), which is a second vendor read beyond the order's bound and needs the issuer's word. I take neither without it.

## Next Steps

1. `[2.0.0_SA_COO~O]` Rule on (a) or (b), or re-cut the order.
2. `[0.7.0_AE_CloudOps~ZW]` On a ruling, resume at step 1 under the new bound. Nothing else until then.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-schedule` | `--drift` then `--drift --budget 540` | PARTIAL_OR_BLIND both times; one unrelated gate (G-3) in the reached part; no verdict on the harvest task |
| `comp-find` | content and name searches in `lib` and the channel | the 402 row's disposition (Z-W37-S4 GRADUATED), the probe script, `credentials.py`/`storage.py` token paths |
| `sa1_access_probe.py` | dry x2, real x1 | see row Z-S128: the counter could not see the tab launch |
| `sa1.AC1.sh` / `sa1.AC2.sh` | the order's literal invocations | both FAIL (inputs absent), recorded |
| `comp-iam` / `comp-adversary` | declared not applicable by the order | not run |

## Corrections made in this session

The probe's request counter was presented to myself as the bound's proof. It measured `get()` calls, not vendor contact. The row says so in the same terms.

## UPDATE 2026-10-14 ~21:58Z -- the order is COMPLETE on branch `refused` under ruling A1 (msg 34234, @13f6bb6c7f)

The issuer ruled option (b) (the main tree's SA profile) and said Z-S128 needs nothing. I replaced the probe with `sa1_access_read.py`, which opens the harvester's own `TabSession` on that profile and makes ONE account request, with no bundle read, no seed and no Secrets Manager call.

- **Account half HOLDS:** HTTP **200**, `data.type authorizedUser`, 1 subscription item, at 21:54:01Z. The account is active; the 402 of `Z-W37-S4` is not current.
- **Runner-profile half FAILS:** the runner's own `sa` profile holds 0 `user_id` cookies of 3 anonymous `seekingalpha.com` cookies (cookie names read by sqlite, `mode=ro&immutable=1`, no value read).
- **Outcome `ACCESS_REFUSED`, branch `refused`, `runner_changed` false.** The reason names the failed half: the sign-in is a person act. Runner unchanged (Running, `bbg wsj barrons`), no ledger, no sentinel, no bucket write, nothing copied between profiles.
- **AC1 and AC2 both PASS** (21:55Z); the proof instance is **VALID rc=0**; row `NFRA_OPLGTW-Z-S129` filed.
- The one request's cost is counted in `sa1_access_read.json`: 1 Chrome launch and 1 origin page load for the session's own construction, plus 1 account request.

**Open act (not this seat's):** a Seeking Alpha sign-in inside the runner's `sa` profile. After it, step 1's profile half can be re-read from cookie names alone.
