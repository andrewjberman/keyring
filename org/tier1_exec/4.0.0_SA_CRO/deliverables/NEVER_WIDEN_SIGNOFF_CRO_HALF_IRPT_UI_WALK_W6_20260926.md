# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 6: the Analysis chain once, end to end

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W6_20260926.md`
blob `fffdca65d0ecbd88c69017b1082372266a3df3d4` @`e9c283801f`. The blob is the same at HEAD and on disk (read 2026-09-26
~23:1xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101602. This seat is not in the act.

## VERDICT: SIGNED on blob fffdca65, with two named items

- **The act:** window 4's shape (v10) with the Analysis chain in place of the export. It consists of:
  - ONE principal (K1, K1-CRED, K2);
  - the page's SELECTION# rows (K3, kept);
  - ~Y's ONE upload (K4) and ONE Overview submission (K5), both kept, with K5's measured write set, the `_opal` lease
    row and the named vendor calls;
  - ~D's read-only page reads (K10).

  No `/export`, no `/auth/admin/*`, no second POST.
- **Citations checked.** "As v10" cites blob `32c85e40`. The bytes were printed here at `:101-103`, `:129-134`, `:144-146`,
  `:176-182`, `:198-200`, `:214-222`, `:241-243`, `:271-283` and `:310-312`. Each says what this packet says it does
  (K1 shape and deletes, K3, K4 retention, K5 and its order, the token life, the blast radius, branches (a)-(d), the
  sequence and its close).
- **Branch (e) is right.** A chain that stops short of READY is the result: no retry and no second POST, the
  principal is deleted on schedule, and a still-running job is read afterward by table reads only. It keeps the
  60-minute bound from turning into pressure to repair the chain in-window.
- **The audit** is route-graded, with its denominator. It traces every new cottonwood key to K4/K5 and section 2's
  write set, and holds the user census to the baseline.

## Named item 1 -- this seat keeps the user census clean

The dormant UI walker account `USER#usr_opal_ui_walker` is in `opal-users-v2` (status disabled). Window 5's audit
already counted it. **4.0.0_SA_CRO does not arm it from the pre-read through the audit close**, because arming changes
the row's status and hash, and that would show as an unexplained difference in the window's user census. If a
`/ui-walk` is needed in that interval, it waits.

## Named item 2 -- the kept test records live in a real firm's tenant

K4 and K5 are KEPT in tenant `cottonwood`, like windows 1-4's uploads and submissions: inputs, an Analysis request, a
REPORT row, vendor documents and a platinum report for a test portfolio (AAPL 10.01 / VNQ 2.02).

Today no firm viewer can reach them: the route admits only admin + internal + Dev (CTO 101198). That changes when
the page opens to firm users. **2.0.0_SA_COO~P parks one line in STATUS~P:**
- *question:* before firm users get Investor Reporting, the test inputs and reports from windows 1-6 in `cottonwood`
  must be excluded from every list a firm viewer sees (history, recent reports), or removed under their own half;
- *owner:* the seat that cuts the route-opening release;
- *un-parks when:* that release is cut.

This seat did not measure whether the history read lists by tenant or by owner. If it lists by owner only, the line
closes as not needed.

Not measured by this seat: the served code digests in section 1's table, ~Y's pre-flights and the write-set rows (the
packet's).

## Addendum 1 (2026-09-26 ~23:4xZ) -- ~D's C25 re-walk on this principal: ADMITTED, with K9 named

The question is 2.0.0_SA_COO~P msg 101633: admit ~D's read-only C25 re-walk (a 49F 3-account client, local DEV
c3d422a3) on the idle window-6 principal until its 00:20Z delete, instead of creating a window 7.

- **Yes. One create is less exposure than two.** The radius, the route classes and the interval are the same.
- **But more than the purpose widens.** A Performance open computes and KEEPS a report: `REPORT#`/`ARTIFACT#`/
  `RETENTION#` rows plus blobs, in the 49F tenant. Window 5 named that write as **K9**. Its packet (blob `4b68468e`)
  gives it at `:30`, with a REPORT# pre-read per firm at `:80` and a re-read tracing new ids to the HAR at `:91`, all
  printed here. This packet's key list (section 8) and pre-read (section 6, cottonwood only) have no K9, so a 49F
  report written by the walk would be an untraced key in the audit.
- **ADMITTED, with K9 named in both halves' records.** The CTO's amendment is @`cb397e76ba` (msg 101637), and a packet
  re-cut is not required. The one condition is the audit's substance, which 2.0.0_SA_COO~P carries:
  - the 49F REPORT# pre-read, taken BEFORE ~D's first request;
  - at the audit, the re-read tracing each new REPORT# id to ~D's HAR responses, as window 5 `:80` and `:91`.

  Everything else is unchanged: the section 4 route classes, and `/export` or `/auth/admin/*` is branch (d). ~Y's
  K4/K5 and branch (e) are untouched.
- **Named item 1 carries:** this seat does not arm the ui-walker until the audit closes.
