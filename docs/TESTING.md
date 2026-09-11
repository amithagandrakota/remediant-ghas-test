# GHAS Test Plan

## Code Scanning
`app.py` contains intentionally insecure patterns for CodeQL testing, including SQL injection, command injection, and path traversal.

## Dependency Scanning
`requirements.txt` intentionally uses old package versions so dependency/security tooling can identify vulnerable dependencies.

## Secret Scanning
No real secret is included. Use an approved GitHub test/dummy secret procedure if your organization wants to test secret scanning. Never commit a real API key.

## Remediant API Test
After alerts appear in GitHub, retrieve them through the GitHub Code Scanning API and inspect the JSON before implementing the Remediant connector.
