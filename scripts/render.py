import os
import shutil
from contextlib import suppress
from pathlib import Path

max_uses = os.environ.get("INVITE_MAX_USES", "100")
if max_uses == "0":
    max_uses = "∞"


template_variables = {
    "SERVER_NAME": os.environ.get("SERVER_NAME", "Your Server Name"),
    "FULL_URL": os.environ.get("FULL_URL", "https://your-server-org.github.io/your-server-invites-repo/"),
    "TWITTER_HANDLE": os.environ.get("TWITTER_HANDLE", "@serverhandler"),
    "TITLE": os.environ.get("TITLE", "Join Your Server Name!"),
    "SUBTITLE": os.environ.get("SUBTITLE", "Welcome"),
    "BUTTON_TEXT": os.environ.get("BUTTON_TEXT", "Get Invite"),
    "NUM_MEMBERS": os.environ.get("NUM_MEMBERS", "?"),
    "NUM_MEMBERS_ONLINE": os.environ.get("NUM_MEMBERS_ONLINE", "?"),
    "INVITE_URL": os.environ.get("INVITE_URL"),
    "VALID_UNTIL": os.environ.get("INVITE_VALID_UNTIL"),
    "MAX_USES": max_uses,
}

with suppress(IOError):
    shutil.rmtree("pub")

shutil.copytree("src", "pub")
index = Path("pub/index.html")
contents = index.read_text()
for key, value in template_variables.items():
    if value is not None:
        contents = contents.replace(f"__{key}__", value)
index.unlink()
index.write_text(contents)