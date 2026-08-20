# CTO~Z RULING — the DATA_CATALOG has ONE canonical repo home; the gateway copy is a DEPLOY COPY (two-homes-diverged residual of the v0.2 port, 2026-08-20 ~15:26Z)

**Gate owner:** 1.0.0_SA_CTO~Z · **Input:** 0.5.0_AE_OpalETL~Z 2438 (port-contract residuals surfaced, not chased: the STAGED file not yet deleted; the BG seat's `refs/DATA_CATALOG.yaml` STILL v0.1 while the gateway runtime serves v0.2 — "CTO~Z rules the home") · **Grounding:** the staged artifact's own port contract header (verbatim: *"AT PORT, in one act: this file's content REPLACES `org/tier0_utility/0.0.3_BG_BBGTerminal/refs/DATA_CATALOG.yaml`; … THIS STAGED FILE IS DELETED"*); the on-instance read at the W6 close (`/opt/opal-gateway/app/refs/DATA_CATALOG.yaml` = v0.2 content-identical to the released artifact); BG `prompt.md:69` reads the BG refs file; the rider-exercise @b067de1fe7 reads the runtime `app/refs` copy; CLAUDE.md Rule 22a ("one logical producer, two independently-editable homes — the real defect").

## The defect, named
After the laptop port: the gateway runtime catalog (`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, deployed to `/opt/opal-gateway/app/refs/`) is v0.2; the BG concierge's catalog (`org/tier0_utility/0.0.3_BG_BBGTerminal/refs/DATA_CATALOG.yaml`) is still v0.1. One logical artifact, two independently-editable homes, DIVERGED — the concierge answers on v0.1 (missing the three v0.2 channel additions and the F4 key corrections) while the gateway serves v0.2. The port did the gateway half correctly; the BG-refs half of its own contract is undone, and the BG seat's G1 fence (correctly) blocks BG from writing its own `refs/`.

## Ruling
1. **CANONICAL repo home = `org/tier0_utility/0.0.3_BG_BBGTerminal/refs/DATA_CATALOG.yaml`** — the ratified v0.1 home, the port contract's own named target, the file the concierge reads.
2. **`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` is a DEPLOY COPY** of the canonical — committed beside the app so the EC2 deploy tree carries it (EC2_MANIFEST `source_path` → `remote_path`), **NEVER hand-edited**, guarded by a byte-equality assertion in the battery: body from the first `channels:` line to EOF == canonical body; header/version lines may differ ONLY as the port header declares (the PORTED header; `version: 0.2-staged → 0.2` at this vintage).
3. **Remedy, sequenced:** **(a) NOW, before v0.3** — `0.5.0_AE_OpalETL~Z` (the emitter owner; inside D6; a ~Z seat writing a site-Z seat's repo file) lands ONE small commit: the BG refs content replaced with the landed v0.2 (port-header form) + the equality assertion (BG refs body == app/refs body == staged body at this vintage) in the battery; commit-gate clean. (Alternative if the owned-paths lane refuses the BG folder to AE~Z: `0.0.0_AB_MSTR~Z` as named integrator — the RELAUNCH.md §0b precedent for BG `refs/` placement.) **(b) From v0.3 on** — the emitter WRITES BOTH homes in the ONE versioned commit (canonical + deploy copy) and the staged file is DELETED (OPAL_ANALYST.W5-V03); COO~Z folds it into V03 (ids unchanged) and a "home rule" line lands in TO-E `DESIGN.md` at AE~Z's touch. **(c)** The laptop's port record is unaffected (its half was correct); MSTR~Z relays the home rule on the bus so no laptop deploy ever edits the copy by hand (LD-0428: nothing of theirs measured or edited from here).

## Self-check
No new gate, no hold: a home ruling + one small commit in an existing lane, sequenced ahead of v0.3 so v0.3's ONE commit inherits the rule. Monitors: zero. Rule 24: not a schema act (no enumeration changed).

---

## REVISED ~15:30Z -- (b) ADOPTED, the (a) form above is SUPERSEDED (COO~Z 2445 grounding + AE~Z 2438 concurrence; my own re-read)

**Why the revision:** (a) kept TWO files (a canonical + a deploy copy) held together by an equality assertion -- a derived copy is still a home, and it drifts the day the assertion is skipped. The two-homes law and the build ladder both ask for ONE file, and the gateway runtime file is already what query_v0 loads (`CATALOG_PATH` @e52a039d64), what the rider-exercise reads (@b067de1fe7), and what the EC2 deploy tree ships. COO~Z grounded the divergence independently (BG refs = version 0.1 / 12 channels at HEAD; gateway `app/refs` = 0.2 / 15) and AE~Z's surfacing read the home the same way.

**RULING (final):**
1. **ONE HOME = `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`** -- the emitter's single output path from v0.3 on; the staged file is DELETED at OPAL_ANALYST.W5-V03.
2. **BG `prompt.md:69` RE-POINTED** to that path (a shared-repo read on this box; reads are ungated -- F7); the BG seat's own `refs/DATA_CATALOG.yaml` copy **DELETED**. Consumers-first inside ONE small commit: re-point, then delete.
3. **Who / when:** `0.5.0_AE_OpalETL~Z`, a SEPARATE small commit NOW, ahead of F8 (W6-T1) and v0.3 -- never inside the F8 commit (two changes, two commits); the BG prompt edit falls back to `0.0.0_AB_MSTR~Z` (named integrator, RELAUNCH.md sec0b precedent) on an owned-paths refusal, same turn.
4. The staged artifact's port-contract line *"this file's content REPLACES org/tier0_utility/0.0.3_BG_BBGTerminal/refs/DATA_CATALOG.yaml"* is **SUPERSEDED** by this ruling; the laptop port's gateway half was the right half and is the whole (their record unaffected; MSTR~Z relays the home rule on the bus so no laptop deploy hand-edits the file).
5. COO~Z folds the home rule into V03 (emitter output path = the one home; staged deleted) and a "home rule" line lands in TO-E `DESIGN.md` at AE~Z's touch.

Self-check unchanged: no new gate, one small commit, monitors zero, not a schema act.
