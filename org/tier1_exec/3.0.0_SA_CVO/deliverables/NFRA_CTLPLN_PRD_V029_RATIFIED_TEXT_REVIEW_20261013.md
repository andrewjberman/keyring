# NFRA_CTLPLN PRD v0.29 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on the L4-R delivery 1.0.0_SA_CTO msg 108762 (and msg 108763). 2026-10-13 ~14:3xZ.
**Verdict:** SIGNED.

## What was read

- PRD at aca7293 (v0.29), unchanged at HEAD; ratified-text half_hash `b443719459b6dd09474c1b5cd0d3b650fbe45691cd38d412b30c000fb4246503`.
- `git diff 5a2b425 aca7293`: inside the ENDPOINT section only FWD-14 and FWD-27 change. FWD-9, FWD-11 and FWD-13 are
  re-scoped in the addendum only; their cards are untouched, so every citation resolves.
- Andrew's words in `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_140xZ_FOUR_OPEN_CALLS_ANSWERED_DEVPLN_TAILNET_SSH_BDFEE_CTLPLN_SCOPE.md`
  (lines 11-13, 24).
- `tailscale status` from the laptop: rc (100.98.173.75, macOS), muse (100.113.31.20) and cloud-local (100.96.167.100) are
  tailnet devices.

## Checks

1. **Faithful to the words.** Each phrase traces to the record, verbatim:
   - the source devices: "within tailnet devices only ... from 'rc' 'muse' and 'cloud-local'";
   - the laptop as a target: "'muse' also needs to be able to remote into laptop";
   - the bound: "no external ssh available nor any external rdp available (aside from IT services like splashtop)";
   - the RDP from rc kept: "Currently we have rdp access from 'rc'".
2. **Coherent.** FWD-14 keeps rc's RDP into the laptop and bars RDP from outside the tailnet. Both hold, because rc is a tailnet
   device. FWD-27's ACCEPT binds RDP "the same way (FWD-14)", so the two outcomes agree.
3. **Provable on demand.** Each limb is an act a seat or Andrew can take: a key login from each source, a refused off-tailnet
   attempt, the local account's Administrators membership re-read after one Intune sync. The Intune behaviour is stated as
   unread, not assumed.
4. **Today's state matches the new text.** This seat measured key logins from the laptop to sitez, dell1 and dell2 (rc 0), and
   the laptop's own refusal (Entra), on 2026-10-12/13. Password login is still on at all three, so FWD-27 stays GATED.

## Notes (not blocking)

- FWD-27's ACCEPT now carries a dated measurement and a seat serial ("measured by 0.0.0_AB_MSTR 2026-10-13 ~00:5xZ, msg 108757";
  "dell1, dell2 and sitez answer muse today"). These will go stale inside ratified text. Move them to the addendum at the next
  ENDPOINT bump, together with the earlier seat-name notes.
- "rc" is a source device, not a box, so its absence from `org/devices/DEVICES.json` is consistent with C-REGISTRY ("the ONE
  place a box is named").
