# 4.0.0_SA_CRO — Session Close 2103–0114Z — reachability recovery, the Azure billing re-registration, and the 49F SmartX custodian investigation

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, EXPLORE, IMPLEMENT

**Serial:** 4.0.0_SA_CRO (base, no lane) · **Session:** re-registered 2026-09-02T21:2xZ, PID 102792
**Window:** 2026-09-02T21:03Z → 2026-09-03T01:14Z · **Commits (mine): 0** · **MCP: 4 in / 0 out** · **Deploys: 0**
**Closed on Andrew's PENCILS-DOWN** (msg `92879`, relayed verbatim by `2.0.0_SA_COO` 01:12Z, device restart).

⛔ **NOTHING WAS IN FLIGHT AT THE STOP.** No commit, deploy, push, TO, grade or dispatch was
half-landed. The Azure writes below completed and were verified; the investigation below is complete
and its findings are carried IN THIS LOG, which is their only durable carrier.

---

## What happened

### 1. Reachability recovery (21:2xZ)
The prior window closed DEAF — Monitor `bf85ke7r5` had stopped and the broker registration had dropped.
Re-registered (PID 102792) and armed Monitor **`btu33517z`**, confirmed `running` by `TaskOutput` AND by
a live `[INBOX]` event (the one oracle an orphan cannot forge). **No orphan reaped:** the only
`inbox-watch.sh` on the box was `4.0.0_SA_CRO~A` — a DIFFERENT lane serial that my grep matched as a
substring. Killing it would have made another seat deaf. Left alone per self-scoping.

Acked `92741` / `92749` / `92773` via `ack_messages`. `92773` carries the Andrew-direct routing of the
custodian residual to THIS seat, verbatim: *"On call 2, 4.0.0_SA_CRO Base can look into that they are
already online."*

### 2. Azure billing re-registration (AJ/LDT, ~21:4xZ) — PARTIAL, and the failure is the finding
AJ email 21:09Z: *"We need to get the account in Opal's name as the entity."* Address confirmed by AJ
in Teams 21:39Z.

- **DONE + VERIFIED by read-back:** billing account `displayName` + `soldTo` →
  **Opal Capital LLC, 1825 NW Corporate Blvd, Boca Raton, FL 33432**. Merge-PATCH on
  api-version 2020-05-01. Confirmed independently in Andrew's own portal screenshot.
- ⛔ **NOT DONE:** billing PROFILE `I6HW-JUCK-BG7-PGB` `billTo` is STILL `Andrew` / 5200 Town Center Cir.
  **The profile does NOT inherit from the account soldTo, and the profile is what prints on invoices.**
  API refuses it: merge-patch → 400; RFC-6902 on 2019-10-01-preview → 500. Portal route given to Andrew
  (Billing profiles → Properties → Update address), UNVERIFIED from here.
- ⛔ **NOT POSSIBLE VIA API — AND IT IS A SILENT FALSE-SUCCESS.** PATCHing `accountType` to `Enterprise`
  returns **rc=0 with a full 200 body and no error**, and changes NOTHING — `accountType` stays
  `Individual` and `lastModifiedAt` does not even advance. **Reading the exit code would have made me
  report a change that never happened.** Business/Organization is fixed at signup; conversion needs
  Microsoft support or a new business-signed billing account + subscription transfer.
- **Andrew's plan validated:** a new business billing account does NOT require a new tenant
  (`primaryBillingTenantId` is already `6810043e-…`), and Microsoft docs confirm **subscription IDs and
  resource IDs are preserved** on a billing-ownership transfer — so the subscription id `1e594a38-…`
  he already sent LDT survives.

### 3. The 49F SmartX custodian investigation (Andrew-directed via COO `92741`/`92773`) — COMPLETE

**Denominator: `fact_allocation_account_map`, ALL 50 partitions 2026-07-14 → 2026-09-02** (36 populated,
14 weekend stubs), 26.4 MiB pulled locally. Schema is **10 columns**, not the 9 the ask inherited
(`date` is carried in the file itself).

**(a) A non-Schwab custodian IS present.** At `date=2026-09-02`, denominator **7,403 rows**:

| token | 8-digit (7,385) | 9-digit (18) |
|---|---|---|
| `SCHWAB` | **4,403** | **0** |
| `FMTC` / `FMT CO` | **0** | **15** |
| `FIDELITY` | 0 | 0 |
| `PERSHING` | 0 | 0 |

**Zero overlap in either direction.** Account-number LENGTH and REGISTRATION TEXT are two independent
carriers and they agree perfectly — which is what makes the conclusion hold; length alone would be weak.
Registration shape (names redacted): `FMT CO CUST IRA FBO ~`, `FMTC CUSTODIAN ROTH IRA FBO ~`.
**3 of 18** carry no custodian token at all (plain names), $2.14M of the $12.18M.

⛔ **THE TRAP, AND IT IS THE TRANSFERABLE HALF: `FIDELITY` = 0 of 7,403 is TRUE AND USELESS.**
`0.4.0_DS_ClientPlatform~N` reported the same zero on 08-30 and I reproduced it. **ANDREW SUPPLIED THE
IDENTIFICATION: FMTC = Fidelity Management Trust Company.** So the custodian IS Fidelity — under an
abbreviation the name-census structurally cannot see. **A token census on a firm's NAME misses that firm
when it lands as an ABBREVIATION.** Both seats' zeros were honest and would have produced the wrong
conclusion. The gap closed the way the ask required — from a source, never by inference.

**(b) It IS growing — the phase-in test, all 50 partitions:**
```
2026-07-14   11 rows /  9 keys /  $5,109,688.24   (7 FMTC-tokened)
2026-08-14   16 rows / 13 keys /  $6,759,064.13   <- STEP
2026-08-24   18 rows / 13 keys / $12,379,954.84   <- STEP
2026-09-02   18 rows / 13 keys / $12,181,264.06   (flat 8 sessions)
```
`08-28` reproduces DS~N's independent measurement **to the cent** ($12,293,768.23 / 18 rows / 13 keys).

**(c) ORIGIN: UNDATABLE FROM THE ESTATE.** All three candidate instruments fail, each for a different
reason:
- **Silver map** — retains 50 days; already at 11 rows on day one.
- **Gold `dim_identity_crosswalk`** — 542 dated partitions 2024-07-08 → 2026-09-01, but **541 are
  BACKFILLED from a single map vintage.** Two INDEPENDENT tests, which **agree on magnitude (2 of 542)
  and DISAGREE on membership**: in-band (`map_asof == asof`) → `08-28`,`09-01`; out-of-band (S3
  `LastModified` within 1 day) → `08-31`,`09-01`. **Intersection = 1 partition (`2026-09-01`).**
  `map_asof == asof` is NOT proof of contemporaneity — satisfiable by accident when a backfill runs near
  the date it writes. Write census: 310 objects created 08-29, 224 on 08-28; median lag **390 days**, max **781**.
- **Bronze landing** — bottoms out at `20260714` for the nine-digit accounts AND, by control, for
  **8-digit Schwab accounts at the same timestamps (08:54–08:57)**. It is a GENESIS WALL of the whole
  SmartX landing, not an account signal.

**(d) MECHANISM — why nobody saw it.** `data/assets/scripts/gold/runners_49f/a06_dim_identity_crosswalk.py`
`:114` renames the vendor's generic `account_number` to **`schwab_account_number`**; `:116` filters
`fullmatch(r"\d{8}")`; `:118-119` leave non-matching rows with `account_id = None`. The chain reads
**3 of 9 columns** (`MAP_COLUMNS`, `:36`) and never touches `account_name`, so the custodian text is
structurally invisible to it. **The estate has been COUNTING them all along** — `:152` emits
`non_8digit_account_numbers` in every manifest and prints it on every run.

**NOT ASKED, NOT DONE:** a remedy; the firm-name expansion (Andrew supplied it, I did not derive it).
**SURFACED, NOT CHASED:** `schwab_account_number` is now a false content assertion under the 2a naming
rule, and the 8-digit filter silently drops $12.2M of real AUM from identity resolution. Owner = the
49F gold lane.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-read --enumerate` | `a06_dim_identity_crosswalk.py` × 4 (MAP_COLUMNS, filter, manifest, write target) | **PASS** | Located the `\d{8}` filter and the `schwab_account_number` rename at source. The DEF/CODE/COMMENT banding separated the live filter from its docstrings. |
| `comp-find --name` | `*a06*`, `runner_common.py`, `_provenance` | **PASS** | Denominators printed; found the 49F runner among 105 name hits. |
| `comp-find` (content) | `^GOLD\|^SILVER\|^BUCKET` over the 49F runner dir | **PASS** | Gave `GOLD_BUCKET` + `GOLD_ROOT` incl. the 2026-08-18 GOLDHOME re-point, which is what located the manifests. |
| `comp-which` | (not run this window) | — | The targets were already named by the ask; routing would have added nothing. |

**What worked.** The **control discipline** was the whole investigation. Three separate conclusions
turned on a control rather than on the primary reading: the Schwab token count as a positive control on
the 9-digit separation; the 8-digit accounts as the control that turned `20260714` from an origin signal
into a genesis wall; and the S3 write-date as a second carrier that disagreed with the manifest's
self-report about WHICH days are genuine.

**What failed.** `pyarrow.read_table` raised `ArrowMemoryError: malloc of size 16384 failed` on a
full-table read; re-reading with an explicit `columns=[...]` subset fixed it. Also an MSYS/Windows path
mismatch — a bash `> /tmp/x.txt` redirect is invisible to Windows Python; the scratchpad path works.
Also hit the Rule-21 rail on a bare `find` in a TEMP dir (not a repo search); avoided the token rather
than override the gate.

**Gap found — SURFACED, NOT CHASED.** `dim_identity_crosswalk` presents **542 dated partitions of which
1 is fully genuine.** This is NOT a defect of the backfill — carrying a dimension backward is CORRECT
when the source retains 50 days, and the manifest discloses it in-band via `map_asof`. **The hazard is
narrower: `non_8digit_account_numbers` and `coverage_end_to_end` sit next to `asof` and LOOK like
per-date measurements while being governed by `map_asof`.** `date=2024-07-08` reports
`coverage_end_to_end 3531/7356 = 0.48` — today's identity map scored against that date's account
universe, two vintages in one ratio. Whether any consumer reads a non-current partition for a
point-in-time question is **UNMEASURED**; I did not census consumers and am not claiming harm.

---

## MCP traffic

**In (4):** `92741` + `92773` (COO — the Andrew-directed custodian investigation and its
re-confirmation to this seat), `92749` (`0.8.0_AE_CloudComp`, comp-kuzu wrapper retirement; no scripted
call held, no reply owed), `92879` (**[STOP]** pencils-down). First three READ-acked via `ack_messages`.
**Out (0)** at time of writing; the one-line confirmation to `2.0.0_SA_COO` required by `92879` step 3
goes out immediately after this commit.

---

## Files Modified

**No repo files changed this window.** Two Azure control-plane writes (external to git, subscription
`1e594a38-9247-4744-a33d-eb2b29dd64e6`): billing-account `soldTo`/`displayName`, and an `accountType`
PATCH that was accepted and silently ignored. One memory file updated
(`project_azure_subscription_and_cli_setup_20260828.md`, untracked memory dir).

---

## Blockers

**NONE owned by this seat.** Sequence state only, each with its holder:
1. **[Andrew]** Billing profile `billTo` still personal — portal-only, one action, ~30s.
2. **[Andrew / LDT]** `accountType` Individual → Business needs a Microsoft support ticket or a new
   business-signed billing account. Neither tested.
3. **[Andrew / 2.0.0_SA_COO]** The custodian findings above are answered but NOT routed — COO asked that
   the answer return to Andrew via that seat. Held under pencils-down.

---

## Current State

*Written for a reader with zero prior context.*

- **Repo:** no commits by this seat in the window. Local HEAD carries other seats' work; **every commit
  today is LOCAL and a restart does not lose them** (per `92879`). No push attempted — pencils down.
- **Azure:** subscription `1e594a38-9247-4744-a33d-eb2b29dd64e6` "Opal Capital", tenant
  `6810043e-d171-4adc-9975-068b35e179da`. TWO Owners (Andrew + `LDTAdmin@opalinvest.com`). ONE budget
  `Monthly_Budget` $100 **Monthly**, alerts 50/80/100 actual + 100 forecast. Billing account soldTo =
  **Opal Capital LLC / 1825 NW Corporate Blvd / 33432**; billing profile `I6HW-JUCK-BG7-PGB` billTo
  **still personal**; `accountType` **still Individual**.
- **Investigation artifacts:** all analysis was in the session scratchpad
  (`…/scratchpad/custodian/` 50 partitions, `…/scratchpad/xw/` 542 manifests). **These are TEMP and do
  not survive the restart.** Every substantive number is transcribed into this log deliberately, because
  this log is their only durable carrier. Re-deriving costs one `aws s3 sync` and ~10 minutes.
- **Reachability at close:** registered PID 102792, Monitor `btu33517z` armed and confirmed by a live
  event. Idling per `92879` step 3.

---

## Next Steps

1. **[4.0.0_SA_CRO, post-restart]** `/watcher` FIRST. Then route the custodian answer to Andrew via
   `2.0.0_SA_COO` (RAVC ack owed on `92741`/`92773`), if he still wants it.
2. **[Andrew]** The billing-profile `billTo` portal edit; and whether LDT opens the Microsoft ticket for
   the Individual→Business conversion.
3. **[49F gold lane]** The two surfaced items in §3(d) — the `schwab_account_number` naming assertion and
   the $12.2M dropped by the 8-digit filter. Characterize-not-fix; no remedy was asked for.
4. **[whoever owns `dim_identity_crosswalk`]** If any consumer reads a non-current partition for a
   point-in-time question, the two-vintage ratio in §Gap matters. Unmeasured.

---

## Archetype rationale

**MIXED.** **VALIDATE** primary — the window's substance was falsification under control: a token census
whose zero was true and misleading, a phase-in test, a backfill detection where two independent
instruments agreed on magnitude and disagreed on membership, and an Azure API that returned success
while changing nothing. **EXPLORE** for the S3/bronze traversal, **IMPLEMENT** for the Azure billing
writes. No DEPLOY, no dispatch, nothing shipped.
