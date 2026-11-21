# Lykeion CLI skill

Use Claude Code or Codex to operate your [Lykeion](https://app.lykeion.tech/) lab through the authenticated `lyk` CLI. The [skill](skills/lykeion/SKILL.md) covers studies, pending Decisions, machines, and Autoresearch.

## Install

Install the [Lykeion CLI](https://app.lykeion.tech/download/#cli) v0.1.8 or newer in the environment where your agent runs. Sign in as yourself and check that `lyk whoami` shows the expected account.

### Claude Code

Run these commands in Claude Code.

```text
/plugin marketplace add lykeion-tech/lykeion-cli
/plugin install lykeion-cli@lykeion
```

Invoke the skill with `/lykeion-cli:lykeion`.

### Codex

Ask Codex to use `$skill-installer` to install the skill from [lykeion-tech/lykeion-cli/skills/lykeion](https://github.com/lykeion-tech/lykeion-cli/tree/main/skills/lykeion). Start a new session and invoke it with `$lykeion`.

### Manual install

Copy the entire `skills/lykeion` folder to `~/.claude/skills/` for Claude Code or `~/.agents/skills/` for Codex. In a new session, invoke `/lykeion` or `$lykeion`, respectively.

## Examples

Try asking “In the Atlas workspace, show me study #12 and any pending Decisions.” See the [Lykeion CLI examples](skills/lykeion/references/examples.md) for more workflows.

## Compatibility checks

CI checks the documented command paths and flags against the minimum supported and latest released CLI. Run the same check locally with `python3 scripts/check-cli.py` when `lyk` is on your PATH.
