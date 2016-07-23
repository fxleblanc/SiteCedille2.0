# Contributing to cedille website

## Testing
You need the Docker **container ID** to run the next steps. You can get the container_id by running ```docker ps```.
Ex: *44fcfefb015e*

```
docker exec -it [container_id] bash
python3 django/cedille/manage.py test [project]
```


## Useful resources

* [Coding style guide](https://www.python.org/dev/peps/pep-0008/)
* [CI server (Travis)](https://travis-ci.org/)

* [Semantic UI](http://semantic-ui.com/)
* [Creating a Pull Request on GitHub](https://help.github.com/articles/creating-a-pull-request/)


## Additional notes

### Issue labels

| Label name | Description |
| --- | --- |
| `enhancement` | Feature requests. |
| `bug` | Confirmed bugs or reports that are very likely to be bugs. |
| `question` | Questions more than bug reports or feature requests (e.g. how do I do X). |
| `help-wanted` | The Sous-Chef core team would appreciate help from the community in resolving these issues. |
| `beginner` | Less complex issues which would be good first issues to work on for users who want to contribute to Sous-Chef. |
| `duplicate` | Issues which are duplicates of other issues, i.e. they have been reported before. |
| `wontfix` | The core team has decided not to fix these issues for now, either because they're working as intended or for some other reason. |
| `invalid` | Issues which aren't valid (e.g. user errors). |

### Issue topics

| Label name | Description |
| --- | --- |
| `client` | Related to client management. |
| `order` | Related to the orders and order items management. |
| `documentation` | Related to any kind of documentation. |
| `frontend` | Related to Semantic UI integration, or Javascript problems. |
| `migration` | Related to the data migration from the old application. |
| `i18n` | Related to any kind of internationalization problem. |
| `python` | Related to python programming. |
| `tests` | Related to unit tests, functional tests or manual testing. |
| `ux/ui` | Related to user experience, user interface, design. |
