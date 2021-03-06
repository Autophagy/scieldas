from typing import Optional

from pydash import get
from scieldas.api import API
from scieldas.services import ServiceAPI


class Travis(ServiceAPI):
    base_url = "https://api.travis-ci.org/"

    @ServiceAPI.call
    def build_status(
        self, user: str, project: str, token: str, api: API, branch: str = None
    ) -> Optional[str]:
        state_map = {"passed": "pass", "started": "building", "failed": "fail"}
        branch = "master" if branch is None else branch
        travis_project = api.add("repos", user, project, "branches", branch).get(
            headers={"Authorization": "token {}".format(token)}
        )
        return state_map.get(get(travis_project, "branch.state"))
