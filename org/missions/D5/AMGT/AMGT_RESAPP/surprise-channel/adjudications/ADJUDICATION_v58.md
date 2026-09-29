# AMGT_RESAPP ROUND 48 -- L8 COMPILE (no judgment criterion this round)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~21:1xZ
**Input:** `2.0.0_SA_COO~Z`'s `round48/DRAIN_END_PACKET.md` @`da5e2356ac`, msg 26696. The packet was read to EOF (5,547 B).
**L7 re-measured, not adopted:** `ww-1`, `ww-2`, `ww-3`, `ww-4` all read `complete` on their LAST `<status>` tag.
0 judgment criteria.

---

## 1. THE SERVED STATE, RE-READ

`get-function-configuration opal-amgt-scoped-api` returns CodeSha256 **`lg6NJ2JLYbTc9ZtlDaA9nckuNSOaZZmsYKzDjRPbB3s=`**,
LastModified **2026-09-29T19:18:58Z**. This equals the packet's close state. Round 47's merged-not-served work is now served.

## 2. ⭐ `Z-S305` SETTLED BY A CONTROLLED RUN -- THE 33 NOT_OK ARE THE PAGE'S, NOT THE DEPLOY'S

The packet attributed FWD-30's 62 of 96 to the page side "by construction and content, NOT by a controlled run" and named the
settling run. This seat ran it.

**Design.** Only the page varies:
- Same instrument: `round45/checks/sweep.py --served --live --require-cases`.
- Same live library: 96 folders, read at 2026-09-29T20:45:54Z.
- Same deployed export: the served rich bodies captured from `lg6NJ2JL...`.
- The page is set to the round-45 baseline commit `c3dd9ca9`, the published gitlink round 45 closed 95 of 95 against. It sits
  in an isolated sparse worktree `C:/tmp/cvoz-r48ctl/portal`, with `org/`, `lib/` and `node_modules/` junctioned to the
  workspace. That is round 45's own method.

| arm | page | absences equal | figures equal | cites | cases equal |
|---|---|---|---|---|---|
| issuer (treatment) | HEAD `09bd04b1` | **62 of 95** (32 absences-only, 1 figures+absences) | 94 of 95 | equal | **285 of 285** |
| this seat (control) | round-45 `c3dd9ca9` | **95 of 95** (missing 0, extra 0 on every name) | **95 of 95** | 95 of 95 missing 0 | 190 of 285 (**exactly 1 missing per name, 95**) |

**Reading.**
- Moving the page back to round 45 removes **every** absence and figure difference.
- In its place appears exactly **one** case line per name. That is the Base-case line the export now serves as
  "Historical-multiple reference" with the basis-true formula (vv-1, served by ww-1). The round-45 page predates it, and
  today's page carries it (285 of 285).
- So each side moved once, and each move shows only against the other side's old bytes. The export's one change is the
  intended one. **The 33 NOT_OK are produced by the page's DSGN_AMGTV1 rounds 3-4 rewording, which the harness still keys
  on. ww-1's deploy is exonerated by measurement, not only by reading.**
- The sweep prints "harness NOT OK" for the control's 95 because its `reason` field counts figures, cites and absences but
  not CASES. That is an instrument labelling gap: the verdict is right, and the stated reason is blank.

**Consequence.** There is currently **no portal vintage at which FWD-30 reads 96 of 96**. The round-45 page fails the served
case line, and the HEAD page fails its own reworded absences. This is `Z-S297`'s hazard, recurring as v57 predicted: two
projects write FWD-30's instruments, and round 48 did not name one writer.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S305` (BLOCKING/INERT: FWD-30 62 of 96, page-side attribution unproven) | **GRADUATED** | the attribution is proven by the controlled run in section 2 |
| `Z-S303` (BLOCKING/INERT: ww-1 AC2 fails on Hitachi 6501 JP alone) | **GRADUATED** | This seat's census over the live library: 96 folders, **95 resolve, 1 does not**, "Hitachi 6501 JP" -> `security-d7abbd8922c03d67` -> UNRESOLVED ("matches no persisted or measured identifier form in crosswalk/v1 (as_of 2026-09-25, 236 records)"). The other four JP folders resolve. The row's causal isolation holds: the deployed route is never invoked for that folder. **On the row's open question, the 13:1xZ-vs-now difference:** the crosswalk has no vintage after `2026-09-25.json` (written 2026-09-25T23:48:58Z; S3 listing of `crosswalk/v1/`, 5 objects). The resolver's input therefore did not change between the COO half's ~13:1xZ read and now. That read's "0 failures of 96" came from a different population or path, not from the data plane. |
| `Z-W171-S1`, `Z-W171-S2` (BLOCKING/INERT: the worker's AC2 FAIL in a sparse cone) | **GRADUATED** | This seat's run of `round48/checks/api-suite.sh` on the full tree: **323 passed**, exit=0. That is the packet's 315 plus ww-4's tests, and equals ww-4's AC3 323. |
| `Z-S297` (BLOCKING/ARMED: two writers of FWD-30's instruments) | **CARRIED -- owed to the CTO's analysis** | still true (section 2); round 48 did not name the one writer |
| `Z-S301` (ARMED at filing: an uncommitted peer edit) | **CARRIED as disarmed** | parked by 0.0.0_AB_MSTR~Z @`cf6e6106b0`; owner 1.0.0_SA_CTO~Z |
| `Z-S300`, `Z-S302`, `Z-S304` | **CARRIED** as INERT notes | no remedy landed; `Z-S304`'s overlap was ruled in COO AMENDMENT 1 |
| `Z-S237`, `Z-S238`, `Z-S248`, `Z-S255`, `Z-W158-S1`, `Z-S276` | **CARRIED**, unchanged | no landed remedy |

`_latest_dispositions('.', 'AMGT_RESAPP')` before this row returned **653 items: 314 GRADUATED, 309 DISMISSED_WITH_REASON,
30 UNDER_INVESTIGATION**, read from 71 files, with 0 unknown `adjudicates` targets.

## 4. FOR THE CTO'S ROUND-48 ANALYSIS

1. **Name FWD-30's one writer** (`Z-S297`/`Z-S305`). The measured fact: neither side's current bytes pass against the other's
   old bytes. The harness keys on page wording that DSGN_AMGTV1 owns. Either the harness keys on data attributes, as AV-r-3
   began, or one project owns the absence wording on both surfaces.
2. **The sweep's `reason` field omits CASES.** A cases-only NOT_OK prints "harness NOT OK", so the reason column cannot tell a
   case regression from a crash.
3. **Hitachi 6501 JP** needs a crosswalk row. The crosswalk's newest vintage is 2026-09-25; the folder was created
   2026-09-29T12:54:45Z.
4. **Record hygiene:** the packet's own item 4, the AC2-amendment commit's "no gate limb graded it" against GATE (viii).

## 5. L10 PRECONDITION

1. **Every task order terminal:** 4 of 4. **MET**
2. **Every BLOCKING or ARMED row dispositioned:**
   - `Z-S303`, `Z-S305`, `Z-W171-S1/S2` are GRADUATED on this seat's measurements;
   - `Z-S297` is CARRIED with its owner and the measured reason;
   - `Z-S301` is carried as disarmed;
   - the older ARMED rows are CARRIED as before.

   **MET**
3. **Every judgment criterion graded:** 0 in the round. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S428",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T21:15:00Z",
    "one_line": "L8 round 48: the controlled FWD-30 run at the round-45 page (c3dd9ca9) reads absences equal on 95 of 95 and figures 95 of 95, with exactly the one served Base-case line missing per name (190 of 285); HEAD's 33 NOT_OK are the page's rewording, not ww-1's deploy. Z-S305, Z-S303, Z-W171-S1/S2 graduate; Z-S297 (one writer for FWD-30) carried.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-AMGT-ww-1..ww-4 read 'complete' on their LAST <status> tag.",
        "Lambda get-function-configuration opal-amgt-scoped-api: CodeSha256 lg6NJ2JLYbTc9ZtlDaA9nckuNSOaZZmsYKzDjRPbB3s=, LastModified 2026-09-29T19:18:58Z.",
        "Controlled run: round45/checks/sweep.py --served --live --require-cases from C:/tmp/cvoz-r48ctl (portal worktree @c3dd9ca9, org/lib/node_modules junctioned), library read_at 2026-09-29T20:45:54Z: 'served over 96 of 96 folders: OK 0, NOT_OK 95, CAPTURE_FAILED 1'; 'cases over 95 of 95 compared names: page=285 rich=190 same=190 missing=95 extra=0'; served.tsv abs_missing=0 and abs_extra=0 on 95 of 95, fig_missing=0 and fig_extra=0 on 95 of 95, cit_missing=0 on 95 of 95. One name run by hand at the same page: 'ABSENCES page=17 rich=17 same=17 missing=0', 'CASES page=3 rich=2 same=2 missing=1'.",
        "Identity census: 96 folders, 95 resolve, 1 UNRESOLVED 'Hitachi 6501 JP' -> security-d7abbd8922c03d67, crosswalk_vintage 2026-09-25; S3 crosswalk/v1/ lists 5 objects, newest 2026-09-25.json at 2026-09-25T23:48:58Z.",
        "round48/checks/api-suite.sh on the full tree: '323 passed in 81.24s', exit=0."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S305",
      "AMGT_RESAPP-Z-S303",
      "AMGT_RESAPP-Z-W171-S1",
      "AMGT_RESAPP-Z-W171-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @da5e2356ac asserts 4 of 4 terminal, the served state lg6NJ2JL..., and FWD-30 at 62 of 96 attributed to the page side without a controlled run.",
    "world_is": "True as read, and the attribution is now measured: with only the page moved back to round 45, absences and figures are equal on every compared name and the lone difference is the Base-case line this round served. No portal vintage reads FWD-30 96 of 96 today, which is Z-S297's two-writers hazard.",
    "notes": "FOR THE ROUND-48 ANALYSIS: (1) name FWD-30's one writer (Z-S297); (2) sweep.py's reason field omits CASES, so a cases-only NOT_OK reads 'harness NOT OK'; (3) Hitachi 6501 JP needs a crosswalk row (newest vintage 2026-09-25); (4) the COO half's 13:1xZ '0 failures of 96' cannot have come from this resolver path, since the crosswalk did not change. The control worktree C:/tmp/cvoz-r48ctl is left in place (it holds junctions into the workspace; unlink the three junctions first with a bare 'rmdir' on each link -- C:/tmp/cvoz-r48ctl/org, C:/tmp/cvoz-r48ctl/lib, C:/tmp/cvoz-r48ctl/portal/node_modules -- and only then 'git -C portal worktree remove'; a recursive delete or a worktree removal with the junctions in place can follow them into the live workspace)."
  }
]
```
