---
name: tdrop
description: Send or receive messages and files OFF GIT, over the tailnet with Taildrop. `/tdrop <prompt>` -- the prompt names the recipient box(es) and what to send or ask; bare `/tdrop get` pulls what has arrived. The one rule, Andrew-direct: NOTHING that travels by /tdrop is ever committed -- not the payload, not a record of it, not a row about it. Any seat.
---

# /tdrop -- off-git messages and files over Taildrop

**Andrew-direct 2026-10-14 ~11:1xZ, at the `1.0.0_SA_CTO` terminal:** "I want a /tdrop skill created the purpose of which is about
sending messages/files/etc off git using taildrop. The premise behind the skill is simply that nothing using tdrop should ever be
committed and it informs the process of how it works so could write '/tdrop <prompt>' about various instructions."

## The one rule

**Nothing sent or received with /tdrop is committed.** That covers the payload, any note or log of it, a surprise row about it, a
ruling file, and a ledger entry. It covers every repo: workspace, portal and opal_ai.

So the payload is written OUTSIDE every git checkout, in `$HOME/tdrop/` (`out/` and `in/`). Before writing, confirm the folder is not
inside a repo: `git -C <dir> rev-parse --show-toplevel` must FAIL.

If a /tdrop matter later needs a durable record, that is a new decision for Andrew. It is never a quiet commit.

## Names (tailnet machine names)

| target | what it is |
|---|---|
| `cloud-local` | the laptop |
| `sitez` | site Z |
| `dell1`, `dell2` | the Dell boxes |
| `muse` | Andrew's VM |
| `rc` | Andrew's Mac |
| `cell` | Andrew's phone |

`tailscale file cp --targets` lists who can receive right now, and `tailscale status` shows who is online. A box cannot send to
itself.

## `/tdrop <prompt>`: send

1. **Read the prompt for:**
   - who receives (one or more targets);
   - what goes: a message you write from the prompt, or named existing files;
   - which seat on the far box acts on it (for example "its CRO", "its MSTR").

   If the recipient is unclear, ask once.
2. **Write the payload** to `$HOME/tdrop/out/<UTC stamp>_<short-slug>.md`, with the folder created if absent. Open with a header:
   - from (your serial and box), to (target and seat), and the UTC time;
   - the line `OFF GIT (/tdrop): do not commit this file or anything about it.`

   Then the instruction itself: complete, standard technical English, Andrew's words verbatim where they drive it. To send existing
   files, list them in the header and send them beside it. Never send a secret value, a token or a credential.
3. **Send:** `tailscale file cp "<file>" [more files] <target>:` (the trailing colon matters). Read the exit code.
   - A non-zero exit, or a target that is offline, means NOT SENT. Say so, and retry when `tailscale status` shows it online.
   - Never report a send that failed as done.
4. **Tell the receiving seat it is there,** with one pointer line, never the content. The pointer gives the filename and "arrived by
   Taildrop; read it from your tdrop inbox". Send it through the broker to a seat on the same box, or through the box's MSTR
   (`/agentbus send <device> ...`) to another box.
   - A broker or agentbus message is not a commit. Still, keep the substance in the Taildrop file, not the pointer.
5. **Report** to whoever asked: what was sent, to whom, the exit code, and the local path as a `file:///` link (CLAUDE.md rule 33).

## `/tdrop get`: receive

1. Pull the inbox: `tailscale file get --conflict=rename "$HOME/tdrop/in/"`. With `--wait`, it blocks until a file arrives.
2. On Windows, the Tailscale app may already have saved incoming files to the user's `Downloads` folder. Look there too, for files
   newer than the expected send time.
3. Read each file, do what it asks within your own lane, and answer by `/tdrop` to the sender if an answer is owed. Received files
   stay in `$HOME/tdrop/in/`; none of them is ever copied into a repo.

## Traps

- **"Sent" is not "read".** `tailscale file cp` returning 0 means the file reached the target's Taildrop inbox. A seat has read it
  only when it says so, by reply or by pointer ack.
- **An offline target refuses or stalls the copy.** Check `tailscale status` first, and never queue silently.
- **A file written under a repo path is one `git add -A` away from a commit.** That is why `$HOME/tdrop/` is the only staging folder.
- **The receiving side may hold the file in its Taildrop inbox until someone runs `tailscale file get`.** The pointer in step 4 is
  what makes the far seat look.
