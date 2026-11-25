# Updating the public directory

1. Locate the original project, identify its owner and choose the precise public scope. Keep drafts and sensitive records in the project’s existing private workspace.
2. Run the relevant project tests. Record the date, command, observable result and outstanding device, integration or live-service checks in the project build log.
3. Record the exact public branch, commit and tree in data/projects.json. Include a concise product goal and a measurable audience or commercial test.
4. Update the public table and check its links. For a software change, include a reproducible fixture or an observable app action. A promotional statement alone does not establish a release.
5. Run the catalog checks, commit and push your review branch, then open a pull request.

```sh
python3 -m unittest discover -s tests
python3 tools/verify.py --remote
git switch -c docs/update-project-record
git add data/projects.json README.md
git commit -m "Update the verified project record"
git push -u origin HEAD
```
