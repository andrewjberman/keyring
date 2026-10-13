# COMM_ASSIST decomposition -- round 16: the muse thread (issuer 2.0.0_SA_COO~CA, laptop; cut 2026-10-13 ~16:1xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO`'s round-15 analysis `ledger/ROUND_ANALYSIS.round15.md` @15fdb72f21, over PRD v0.6 (ratified half SIGNED
at `3.0.0_SA_CVO~L`, `prd-signoff.py status` read ADMITTED @024be02f00). Enrichment list items 1-3 are the cells below; items 4-6
are later rounds or Andrew's acts, as the analysis says.

**How the analysis's cell 1 is split (the issuer's call, inside its own decomposition).** The analysis names one cell for FWD-6 +
FWD-11 whose orders address dell2's lanes. A laptop worker cannot run a scheduled task on dell2 and a dell2 seat cannot be handed
an unwritten script, so the cell is two: CA-h-1 BUILDS the refresh script and the fixed folder layout (a laptop worker, LOCAL,
checks that run here); CA-h-2 is the HOST ACT on dell2 (install, schedule, the admin-group read-back, the live read from muse, the
off-tailnet refusal). FWD-10's clause (a failed source says so, absent is never empty) is built into the first file in CA-h-1.

**Measured at the base (laptop, ~16:1xZ):**

- Grant (d) is SUPERSEDED (CTO ruling @53acd6fe5f, Andrew ~16:5xZ "Sure let's do rec b"): the Dell users join `AdministratorAccessOpalCapital`, three denies kept, and the analysis's "HARD DEPENDENCY: grant (d)" reads "the admin-group apply". That apply is NFRA_CTLPLN round-12 cell 1 (one safe-apply, COO half `2.0.0_SA_COO~C`); it is NOT live: round 12 is not yet cut; `NFRA_CTLPLN` is at round 11 EXECUTING
  (`project.json`, `ledger/ROUND_ANALYSIS.round11.md` newest). The ruling @2f0ed70e40 section 2 puts the read-back at dell2's own
  `GetItem` on `eod:<today>` and a `ListObjectsV2` on each prefix.
- No dell2 lane is live on this broker, and `org/devices/crossbox/` holds 0 ORDER files addressed to dell2 (68 to sitez, 36 to the
  laptop, 13 to dell1). The host order travels as a crossbox ORDER (`.tools/crossbox-call.py issue --order <TO> --to-device dell2`)
  to a named dell2 lane; that lane is named by `0.0.0_AB_MSTR~DELL2` and is not known at this cut.
- The assistant's event entries and the version rule are in `data/transcripts/scripts/teams_chat/tenant.py` (`ROUTES`, `on_sms_reply`,
  `unseen`).

**Rule 24.** Domain: the analysis's enrichment items 1-3 (FWD-6, FWD-11, FWD-7's design). FWD-8, FWD-5, FWD-9, FWD-12 are items 4-5
of the analysis, named later rounds. Uncovered member by subtraction from the printed denominator (3 items): none; item 1 and 2 are
CA-h-1 + CA-h-2, item 3 is CA-h-3.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-h-1` | Build the dell2 reader's refresh script and the fixed folder layout: four files (open calls, waiting drafts, today's End of Day draft, today's sprint page objects), each stamped `read_at`, `status` (`ok` / `absent` / `unreadable`) and `last_good_at`; a source that cannot be read is `unreadable` with `items` null, never an empty list; a no-key/token/address census over the folder | FWD-6, FWD-10, FWD-11 (census arm) | LOCAL | chain 0, slot ~8 | none |
| `CA-h-3` | The FWD-7 signed-answer DESIGN, one document in six sections (how muse's answer is shown to come from muse, how the forwarder verifies it, the refusal record, the stale-version refusal, the write entry and the grant it needs, the forged-answer test that must refuse) | FWD-7 (FWD-8 and FWD-5 ride it) | LOCAL (a design) | chain 0, slot ~8, after CA-h-1 | CA-h-1 (reads its layout) |
| `CA-h-2` | HOST ACT on dell2, NOT cut at this issuance: the script and folder installed under the dell2 account, scheduled on a local clock, the admin-group read-back printed first, the first live run, one SSH read from muse, one refused attempt from off the tailnet, the sshd/firewall read | FWD-6, FWD-11 | SERVED | dell2 lane (crossbox ORDER) | CA-h-1; the admin-group apply's read-back; a named dell2 lane |

`fanout: 1 of 2 chains, cap 8, reason: CA-h-1 and CA-h-3 are one chain (the design reads the layout) so one worker queue; CA-h-2 is a crossbox order to a dell2 lane, cut when its dependencies clear, not a laptop worker.`

**Coverage note for the gate.** CA-h-2 has an unmet dependency (the admin-group apply and a dell2 lane), so under obligation 2 it is not cut at
this tick. It is listed here with its dependency so the round does not close without it: `round-close-check` stays the gate, and
the round does not close until CA-h-2 is cut and terminal or the CTO rules it out. The tick that reads the admin-group apply's read-back cuts it.

**The issuer's real run at close:** the live refresh into a scratch folder under the laptop identity (CA-h-1's AC2), and the folder
read by `ssh` from the laptop once CA-h-2 has installed it on dell2.
