# Lykeion CLI examples

Before using a workspace-scoped command, follow the account and workspace checks in [the skill](../SKILL.md). Replace the example study numbers, rule IDs, and research text with values from the request.

## Explain why a study is blocked

```sh
lyk board
lyk card show 12
lyk decisions
```

Report the stage, the recorded blocker, and any Decision tied to study #12. If the reason is unavailable, say so. Leave pending Decisions for the owner.

## Draft feedback or steer a study

For “Draft feedback for study #12 and keep it paused,” inspect the study and return the draft in chat. An owner's comment can restart a blocked study, so treat posting as a separate action.

If the user authorizes posting feedback that may resume the study, recheck the target and use:

```sh
lyk card comment 12 'Use a matched control and explain how the samples were selected.'
lyk card show 12
```

Report the observed state. A restart can happen asynchronously.

## Create a study and check its state

```sh
lyk card new 'How does sleep restriction affect next-day working memory in healthy adults?' --title 'Sleep restriction and working memory'
```

Use the study number returned by the command in `lyk card show NUMBER`. Report its current stage and state. If the create call times out, inspect `lyk card list` for its effect before considering a retry.

## Run an existing Autoresearch once

```sh
lyk autoresearch list
lyk autoresearch show 1234abcd
lyk autoresearch run 1234abcd
lyk autoresearch runs 1234abcd
```

Replace the example ID with the selected rule's ID, and check its title and execution mode before starting it. Report the new run's ID and status. Triggering once leaves the rule's schedule as configured.
