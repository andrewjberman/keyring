# TCKT_VNEXT -- round 8 L10 slug to `1.0.0_SA_CTO~DELL2`

**From:** `2.0.0_SA_COO~V2` (issuer), 2026-10-12 ~01:1xZ. **One slug, round 8** (your analysis @8cccf94651: one read cell).

## 1. Verdict

**The read is in, claim MEASURED. A status check in the ticket service would lock out exactly two users rows, and sign-in
already refuses both.** One of the two reads as a PERSON. Nothing was built and nothing was applied. **FWD-1 is NOT REALIZED and
was not run.**

## 2. Measured at the slug (2026-10-12 01:1xZ)

| item | value | instrument |
|---|---|---|
| round-8 orders | 1 of 1 complete (TO-READ-R8-ds1 @e377de62b6) | `round-close-check --round 8`: orders=1, judgment=0, verdict=MAY-CLOSE (this seat) |
| the findings file | `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r8_ds1/DISABLED_USERS_READ_20261012.json`; its check re-run by this seat: `DS1-READ-OK profile_rows=56 status_values=2 disabled_internal=2 files_read=11` | this seat |
| everything in section 3 | the applier's reads, NOT re-made by this seat; this seat read the findings file | msg 6233 and the file |

## 3. The three parts, as the applier measured them

**Part 1, the code.**
- Sign-in REFUSES a user whose `status` is not exactly the string `active` (`infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts:106`
  and `:255`); an absent status would be refused too, and no live row has one. The deployed sign-in is tied three ways to that
  source (live hash equals the source map's artifact hash; no source change since the recorded commit; the guards present at it).
- Refresh REFUSES a user disabled since sign-in (`auth.ts:538`).
- NEITHER authorizer reads the caller's users row on a request (zero hits with a working positive control, on HEAD and on the
  recorded build input). So a token issued before the disabling works until it expires: the access token lives 15 minutes
  (`jwt.ts:17`); the refresh token lives 7 days (`jwt.ts:18`) but refresh is guarded, so **the window on the portal path is about
  15 minutes, not 7 days.**
- **What that does not bound:** the direct-invoke path (row D2-S46). There a disabled address is admitted with no time limit.

**Part 2, the two disabled internal rows** (no address here; digests only):

| digest | reads as | row last updated | last ticket event | no disabled-date attribute exists on any row |
|---|---|---|---|---|
| `04fc361f3802` | **a PERSON**: a given name at an external company's domain, `userType` null, firm `opal-capital` | 2026-07-14 | none, on any of 27 tickets | -- |
| `e95c05c7ae90` | non-human tooling (`userType` Dev, a `.test` domain); round 7's twin arm N3 | 2026-10-11T22:41:40Z | none | -- |

**Part 3, the status values, a closed set:** 56 PROFILE rows: `active` 54, `disabled` 2; the counts sum to 56; no row has an
absent status; no other attribute carries the same meaning. Internal rows alone: 23 = 21 + 2.
**Sign-in admits 54; the ticket service admits all 56 by existence. The gap is exactly those 2.**

## 4. What the read showed that you did not ask

- **Row TCKT_VNEXT-D2-S52 (INERT):** the portal authorizer's source at HEAD (450 lines) is 188 lines ahead of the build input the
  source map records as deployed (262 lines, commit `26ffa22b79`): a render-token path. Either a release is owed or the map is
  behind; it reads as IRPT_BCKEND's (the file cites TO-IB-rtr-2). The round's answer was measured on both and holds on both.
- **An external-domain person carries the internal firm id `opal-capital`** (the disabled row `04fc361f3802`). While it was
  active it was an INTERNAL caller to every service that classes by firm id, with no firm list. Whether any ACTIVE row has that
  shape was not counted by this read: the round-7 count's 21 active internal rows were classed by firm id, not by domain.
- **The tooling row was last touched at 22:41:40Z on 2026-10-11**, hours before round 7 used it as the twin. Who touched it and
  why is not in the table.
- `opal-portal-rest-authorizer` cannot be tied to a commit: its source-map entry has no deployed commit.

## 5. Defects in round 8

1. This issuer's order called the HEAD file "the authorizer's source". The applier measured the recorded build input as well and
   found they differ. Had it not, part 1's answer would have been a read of code that is not live.
2. Carried from round 7 and corrected in this round's decomposition: round 7's read reported the authorizer as not in this
   checkout because my order named the wrong folder.
3. The applier's first heuristic for "a person" tested the address's domain against Opal's and would have classed the external
   person as non-human; it caught this itself and says so first in its report.

## 6. BLOCKING and ARMED rows since the round-7 slug

| row | class / hazard | disposition |
|---|---|---|
| D2-S46 any holder of the invoke permission can be any caller | OBS / **ARMED** | OPEN, owner you; waits on the laptop |
| D2-S50 a disabled row still admits | OBS / **ARMED** | OPEN, owner you; this round's read is its ground: 2 rows, both refused at sign-in, reachable only by direct invoke or inside a 15-minute token |
| D2-S52 the authorizer's source is ahead of its recorded build input | OBS / INERT | OPEN; not this project's to close |
| D2-S48, D2-S40 | OBS / INERT | OPEN, `2.0.0_SA_COO~Y2`'s |

No BLOCKING row. No judgment criterion; no L9 grade is owed.

## 7. Enrichment list for round 9

1. **The status line, if your addendum says so:** the contract sentence would read "admits exactly `active`, as sign-in does".
   By this read it locks out the two disabled rows and nobody who can sign in. The build is one condition in `_profile_scope`
   and its tests; the pair is the round-7 shape, with the twin moved to an ACTIVE row (the disabled tooling row becomes the
   REFUSED arm). An active non-human row to stand as the twin has to be named: round 7's count classes 4 of the 21 active rows
   as non-human (2 with `userType` service, 2 with none), but that class came from the domain heuristic the applier has now
   found wrong for the disabled person, so each of the 4 is re-read by form before one is used. A person's address is not used.
2. **A count this read did not make:** active rows with firm `opal-capital` and an address outside Opal's domains. The round-7
   count's `reads_as` used the same domain test and classed the disabled external person as non-human; its 2 active rows
   classed non-human with no `userType` are the first to re-read.
3. Carried: the four staged reads; arm F2, `commentary_sent` on the page, rows D2-S48 and D2-S40 (`2.0.0_SA_COO~Y2`); the
   secret's readers and row D2-S46's census (the laptop); row D2-S49's data fix; run 3's request id; the crawl and the staff
   list (Andrew).
4. **Nothing here moves FWD-1** until Andrew's answer on the vendor path or his sitting.

**Closer:** eight rounds, thread n. The one stop on FWD-1 has an owner and it is Andrew; I do not re-pitch it.
