# Lykeion CLI skill

Use Claude Code or Codex to operate your [Lykeion](https://app.lykeion.tech/) lab through the authenticated `lyk` CLI. The [skill](skills/lykeion/SKILL.md) covers studies, pending Decisions, machines, and Autoresearch.

## Install

Install the [Lykeion CLI](https://app.lykeion.tech/download/#cli) in the environment where your agent runs. Sign in as yourself and check that `lyk whoami` shows the expected account.

From this repository, copy the skill folder for your client.

| Client | User-level skill directory | Invoke in a new session |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/` | `/lykeion` |
| Codex | `~/.agents/skills/` | `$lykeion` |

For example, to install in Codex:

```sh
mkdir -p ~/.agents/skills
cp -R skills/lykeion ~/.agents/skills/
```

Try asking “In the Atlas workspace, show me study #12 and any pending Decisions.”
