# CTO ruling (self-drive dell2-box tick 1) -- call 2402: the Ticket Center commentary-PDF reader is an Opal-internal page; APPROVED

From `1.0.0_SA_CTO~DELL2`, 2026-10-15 ~02:2xZ, under the arming record `ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.

The candidate `cand/dell2/anlreq-ticket-commentary-pdf-reader` (`2.0.0_SA_COO~Y2`, FWD-1's fourth attachment reader) was registered
client-facing, the conservative class. Its page is the Ticket Center. This seat read `portal/src/App.tsx`, where `/ticket-center` is behind
`ProtectedRoute requireInternal` and the partner firm allowlist omits the path. Andrew-direct 2026-10-14 ~15:2xZ: "Ticket Center does not
need to be displayed for client users at this time, only opal users need to see it". So no partner-firm or client login can open the page:
by the law's definition (CLAUDE.md, the portal approval route), it is Opal-internal, and the building box's CTO approves it. The same
reading approved `dell2-20261014T202745Z-2131`.

**APPROVED** for DEV by `portal-merge-forward.sh`. PROD is a chosen-set promote after the FWD-1 run's after-read. If the Ticket Center is
later shown to client users, this page's class becomes client-facing, and that change goes to Andrew.

-- 1.0.0_SA_CTO~DELL2
